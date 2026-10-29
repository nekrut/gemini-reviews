from pathlib import Path
import os
import re
import json
import time
import urllib.request
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

with open(str(Path(__file__).resolve().parent.parent / "cohorts.json") as f:
    cohorts = json.load(f)

all_papers = cohorts["cohort_a"] + cohorts["cohort_b"] + cohorts["cohort_c"]

def fetch_inline_formula_map(pmcid):
    """Fetch <inline-formula> id -> LaTeX mapping from NCBI efetch JATS XML when PMC HTML uses GIF placeholders."""
    if not pmcid:
        return {}
    url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id={pmcid}&retmode=xml"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (lit-estimation)"})
        xml_bytes = urllib.request.urlopen(req, timeout=15).read()
        root = ET.fromstring(xml_bytes)
        fmap = {}
        for tag in ("inline-formula", "disp-formula"):
            for elem in root.findall(f".//{tag}"):
                fid = elem.attrib.get("id")
                raw = "".join(elem.itertext())
                m = re.search(r"\\begin\{document\}\s*(?:\}\{\})?(.*?)\\end\{document\}", raw, re.S)
                val = m.group(1).strip() if m else " ".join(raw.split())
                if fid and val:
                    fmap[fid] = val
        return fmap
    except Exception:
        return {}

def clean_text(el):
    if el is None:
        return ""
    return " ".join(el.get_text(" ", strip=True).split())

def parse_pmc_html(html_bytes, meta):
    soup = BeautifulSoup(html_bytes, "html.parser")
    # If HTML contains <img alt="Inline graphic"> formula placeholders, substitute LaTeX from JATS XML
    if soup.find("img", attrs={"alt": re.compile(r"Inline graphic|math|formula", re.I)}):
        fmap = fetch_inline_formula_map(meta.get("pmcid"))
        for span_id, latex in fmap.items():
            el = soup.find(id=span_id)
            if el is not None:
                el.replace_with(f" {latex} ")
    article = soup.find("article") or soup.find("main") or soup
    
    lines = [
        f"# {meta['cohort_id']} ({meta['pmcid']} / PMID:{meta['pmid']})",
        f"**Title:** {meta['title']}",
        f"**Authors:** {meta['authors']}",
        f"**Venue:** {meta['journal']} ({meta['year']}) | **DOI:** {meta.get('doi')}",
        ""
    ]
    
    # Extract sections, paragraphs, headings, tables
    for el in article.find_all(["h1", "h2", "h3", "h4", "p", "table", "figcaption"]):
        # Skip reference list items or navigation
        parent_classes = " ".join([" ".join(p.get("class", [])) for p in el.parents if p.get("class")])
        if "ref-list" in parent_classes or "footnotes" in parent_classes:
            continue
        if el.name in ("h1", "h2", "h3", "h4"):
            txt = clean_text(el)
            if txt and txt.lower() not in ("references", "supplementary material", "associated data"):
                level = "#" * int(el.name[1])
                lines.append(f"\n{level} {txt}\n")
        elif el.name == "p":
            if el.find_parent("table") or el.find_parent("figcaption"):
                continue
            txt = clean_text(el)
            if len(txt) > 20:
                lines.append(txt + "\n")
        elif el.name == "figcaption":
            txt = clean_text(el)
            if txt:
                lines.append(f"\n> **Figure/Table Caption:** {txt}\n")
        elif el.name == "table":
            rows = el.find_all("tr")
            if rows:
                lines.append("\n")
                for idx, tr in enumerate(rows[:40]):
                    cells = [clean_text(c).replace("|", "/") for c in tr.find_all(["th", "td"])]
                    if cells:
                        lines.append("| " + " | ".join(cells) + " |")
                        if idx == 0:
                            lines.append("| " + " | ".join(["---"] * len(cells)) + " |")
                if len(rows) > 40:
                    lines.append(f"... ({len(rows) - 40} rows truncated) ...")
                lines.append("\n")
    return "\n".join(lines)

def fetch_if_needed(meta):
    cid = meta["cohort_id"]
    pmcid = meta["pmcid"]
    out_path = fstr(Path(__file__).resolve().parent.parent / "papers/{cid}_{pmcid}.md"
    if os.path.exists(out_path) and os.path.getsize(out_path) > 6000:
        return (cid, pmcid, "already_full", os.path.getsize(out_path))
    
    url = f"https://pmc.ncbi.nlm.nih.gov/articles/{pmcid}/"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"})
        html_bytes = urllib.request.urlopen(req, timeout=20).read()
        md = parse_pmc_html(html_bytes, meta)
        with open(out_path, "w") as f:
            f.write(md)
        return (cid, pmcid, "pmc_html", len(md))
    except Exception as e:
        return (cid, pmcid, f"err:{e}", os.path.getsize(out_path) if os.path.exists(out_path) else 0)

with ThreadPoolExecutor(max_workers=4) as ex:
    res = list(ex.map(fetch_if_needed, all_papers))

full_ok = sum(1 for r in res if r[3] > 6000)
print(f"Total full-text manuscripts (>6KB): {full_ok}/75")
for r in res:
    if r[3] <= 6000:
        print("  Still short:", r)
