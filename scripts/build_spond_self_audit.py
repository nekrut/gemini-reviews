#!/usr/bin/env python3
"""
Fetch, extract, and strictly de-identify all full-text PubMed papers matching:
  kosakovsky pond[au] OR pond sl[au] OR pond sk[au]
Saves:
- ./spond_self_audit/raw_papers/SP_RAW_XXX_PMCXXXX.md
- ./spond_self_audit/anon_papers/SP_ANON_XXX.md
- ./spond_self_audit/manifest.json
"""
import json
import random
import re
import time
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from bs4 import BeautifulSoup

base_dir = Path(str(Path(__file__).resolve().parent.parent))
sp_dir = base_dir / "spond_self_audit"
for sub in ["raw_papers", "anon_papers", "reviews"]:
    (sp_dir / sub).mkdir(parents=True, exist_ok=True)

def clean_text(el):
    if el is None:
        return ""
    return re.sub(r"\s+", " ", el.get_text(" ", strip=True)).strip()

def scrub_spond_manuscript(raw_md: str, meta: dict, anon_id: str) -> str:
    lines = raw_md.splitlines()
    body_lines = []
    in_body = False
    for line in lines:
        if line.strip().startswith("## Abstract"):
            in_body = True
        if in_body:
            body_lines.append(line)
    text = "\n".join(body_lines) if body_lines else raw_md

    # Scrub title
    title = meta.get("title", "")
    if title and len(title) > 12:
        text = re.sub(re.escape(title), "[TITLE REDACTED]", text, flags=re.IGNORECASE)
        t_clean = re.sub(r"<[^>]+>", "", title).strip().rstrip(".")
        if len(t_clean) > 12:
            text = re.sub(re.escape(t_clean), "[TITLE REDACTED]", text, flags=re.IGNORECASE)

    # Scrub journal
    journal = meta.get("journal", "")
    if journal and len(journal) > 3:
        text = re.sub(re.escape(journal), "[JOURNAL REDACTED]", text, flags=re.IGNORECASE)

    # Scrub identifiers
    for k in ("pmcid", "pmid", "doi"):
        val = str(meta.get(k, "")).strip()
        if val:
            text = re.sub(re.escape(val), f"[{k.upper()}_REDACTED]", text, flags=re.IGNORECASE)

    # Scrub author names and institutional self-identifiers
    text = re.sub(r"\bKosakovsky[\s\-]+Pond\b", "[AUTHOR]", text, flags=re.IGNORECASE)
    text = re.sub(r"\bPond\s+SLK?\b", "[AUTHOR]", text, flags=re.IGNORECASE)
    text = re.sub(r"\bPond\s+SK\b", "[AUTHOR]", text, flags=re.IGNORECASE)
    text = re.sub(r"\bPond\s+and\s+(Muse|Frost)\b", "[AUTHORS]", text, flags=re.IGNORECASE)
    text = re.sub(r"\bPond\s+et\s+al\.", "[AUTHOR] et al.", text, flags=re.IGNORECASE)
    text = re.sub(r"\bspond\b", "[USER_REDACTED]", text, flags=re.IGNORECASE)
    text = re.sub(r"https?://github\.com/spond/[^\s\)\]]+", "[GITHUB_REPO_URL]", text, flags=re.IGNORECASE)

    # Cut trailing Acknowledgments / Author Contributions / Funding / Competing Interests sections
    text = re.sub(
        r"\n##\s*(Acknowledgments|Acknowledgements|Funding|Author Contributions|Competing Interests|Conflict of Interest|Declarations|Supporting Information|Supplementary Material)\b.*",
        "",
        text,
        flags=re.IGNORECASE | re.DOTALL,
    )

    header = (
        f"# De-Identified Manuscript: {anon_id}\n\n"
        f"> **Blinding Note:** All title, author, affiliation, journal, and identifier metadata have been scrubbed for unbiased methodological review.\n\n"
    )
    return header + text.strip() + "\n"

def determine_authorship_role(author_str: str) -> tuple[str, int]:
    al = [x.strip() for x in author_str.rstrip(".").split(",") if x.strip()]
    n_auth = max(len(al), 1)
    if not al:
        return ("Co-Author (Middle)", 1)
    first_match = "pond" in al[0].lower()
    last_match = "pond" in al[-1].lower()
    if first_match and n_auth == 1:
        return ("First Author (Solo)", 1)
    elif first_match:
        return ("First Author", n_auth)
    elif last_match:
        return ("Senior / Last Author", n_auth)
    else:
        return ("Co-Author (Middle)", n_auth)

def fetch_one_paper(h: dict):
    pmcid = h.get("pmcid", "")
    pmid = str(h.get("pmid", ""))
    title = re.sub(r"<[^>]+>", "", h.get("title", "")).strip()
    journal = h.get("journalInfo", {}).get("journal", {}).get("title", "") or h.get("journalTitle", "")
    yr = int(h.get("pubYear", 2020))
    author_str = h.get("authorString", "")
    role, n_auth = determine_authorship_role(author_str)
    if yr < 2010:
        decade = "2000s (2004–2009)"
    elif yr < 2020:
        decade = "2010s (2010–2019)"
    else:
        decade = "2020s (2020–2026)"

    meta = {
        "pmcid": pmcid,
        "pmid": pmid,
        "doi": h.get("doi", ""),
        "title": title,
        "authors": author_str,
        "author_count": n_auth,
        "authorship_role": role,
        "is_first_or_senior": role.startswith("First") or role.startswith("Senior"),
        "journal": journal,
        "year": yr,
        "decade": decade,
        "citedByCount": int(h.get("citedByCount", 0)),
    }

    # 1. Try Europe PMC JATS XML
    for attempt in range(3):
        try:
            url = f"https://www.ebi.ac.uk/europepmc/webservices/rest/{pmcid}/fullTextXML"
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            xml_bytes = urllib.request.urlopen(req, timeout=15).read()
            soup = BeautifulSoup(xml_bytes, "xml")
            body = soup.find("body")
            if body and len(body.get_text(" ", strip=True)) >= 2500:
                abs_el = soup.find("abstract")
                abs_txt = clean_text(abs_el) if abs_el else ""
                lines = [
                    f"# {pmcid} ({yr})",
                    f"**Title:** {title}",
                    f"**Authors:** {author_str}",
                    f"**Journal:** {journal} ({yr})",
                    "",
                    "## Abstract",
                    abs_txt,
                    "",
                    "## Main Text",
                ]
                for el in body.find_all(["sec", "p", "preformat", "table-wrap"]):
                    if el.name == "sec":
                        st = el.find("title")
                        if st and el.parent == body:
                            lines.append(f"\n## {clean_text(st)}\n")
                    elif el.name in ("p", "preformat"):
                        t = clean_text(el)
                        if len(t) > 20:
                            lines.append(t + "\n")
                    elif el.name == "table-wrap":
                        cap = clean_text(el.find("caption"))
                        if cap:
                            lines.append(f"\n**Table:** {cap}\n")
                        for tr in el.find_all("tr")[:35]:
                            cells = [clean_text(c) for c in tr.find_all(["th", "td"])]
                            if cells:
                                lines.append("| " + " | ".join(cells) + " |")
                md = "\n".join(lines)
                if len(md) >= 3500:
                    return (meta, md)
            break
        except Exception:
            time.sleep(0.4)

    # 2. Fallback to NCBI PMC HTML
    for attempt in range(2):
        try:
            url = f"https://pmc.ncbi.nlm.nih.gov/articles/{pmcid}/"
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            html = urllib.request.urlopen(req, timeout=15).read()
            soup = BeautifulSoup(html, "html.parser")
            art = soup.find("article")
            if not art:
                break
            for r in art.find_all("section", class_="ref-list"):
                r.decompose()
            lines = [
                f"# {pmcid} ({yr})",
                f"**Title:** {title}",
                f"**Authors:** {author_str}",
                f"**Journal:** {journal} ({yr})",
                "",
                "## Abstract & Main Text",
            ]
            for el in art.find_all(["h2", "h3", "p", "table"]):
                if el.name in ("h2", "h3"):
                    t = clean_text(el)
                    if t and t.lower() not in ("references", "acknowledgments", "acknowledgements"):
                        lines.append(f"\n## {t}\n")
                elif el.name == "p":
                    t = clean_text(el)
                    if len(t) > 20:
                        lines.append(t + "\n")
                elif el.name == "table":
                    for tr in el.find_all("tr")[:35]:
                        cells = [clean_text(c) for c in tr.find_all(["th", "td"])]
                        if cells:
                            lines.append("| " + " | ".join(cells) + " |")
            md = "\n".join(lines)
            if len(md) >= 3500:
                return (meta, md)
            break
        except Exception:
            time.sleep(0.4)

    return None

def main():
    q_ncbi = "kosakovsky pond[au] OR pond sl[au] OR pond sk[au]"
    u_esearch = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term={urllib.parse.quote(q_ncbi)}&retmax=500&retmode=json"
    pmids = set(json.loads(urllib.request.urlopen(u_esearch, timeout=15).read())["esearchresult"]["idlist"])
    print(f"Total PubMed PMIDs: {len(pmids)}")

    q_epmc = '(AUTH:"Kosakovsky Pond" OR AUTH:"Pond SL" OR AUTH:"Pond SK")'
    u_epmc = f"https://www.ebi.ac.uk/europepmc/webservices/rest/search?query={urllib.parse.quote(q_epmc)}&format=json&pageSize=500&resultType=core"
    hits = json.loads(urllib.request.urlopen(u_epmc, timeout=15).read()).get("resultList", {}).get("result", [])

    # Keep all non-errata/non-correction papers that either match PubMed PMIDs OR have a PMCID in Europe PMC (excluding preprints if published version exists)
    seen_pmcids = set()
    cands = []
    for h in hits:
        pmcid = h.get("pmcid", "")
        pmid = str(h.get("pmid", ""))
        if not pmcid or pmcid in seen_pmcids:
            continue
        t_low = h.get("title", "").lower()
        if any(w in t_low for w in ["erratum", "correction to:", "corrigendum", "author correction", "publisher correction", "retraction"]):
            continue
        # Must be a PubMed-indexed article (has pmid)
        if not pmid:
            continue
        seen_pmcids.add(pmcid)
        cands.append(h)

    print(f"Candidate non-errata PubMed Central articles with PMCID: {len(cands)}")

    fetched = []
    with ThreadPoolExecutor(max_workers=10) as ex:
        futs = {ex.submit(fetch_one_paper, h): h for h in cands}
        for idx, fut in enumerate(as_completed(futs), 1):
            res = fut.result()
            if res:
                fetched.append(res)
            if idx % 25 == 0 or idx == len(cands):
                print(f"  Progress: {idx}/{len(cands)} checked | {len(fetched)} full texts extracted")

    # Sort deterministically by year, then pmid before shuffling
    fetched.sort(key=lambda x: (x[0]["year"], x[0]["pmid"]))
    print(f"Successfully extracted full text for {len(fetched)} papers!")

    # Clean existing files
    for sub in ["raw_papers", "anon_papers"]:
        for f in (sp_dir / sub).glob("*.md"):
            f.unlink()

    for idx, (meta, md) in enumerate(fetched, 1):
        meta["sp_id"] = f"SP_RAW_{idx:03d}"
        (sp_dir / "raw_papers" / f"{meta['sp_id']}_{meta['pmcid']}.md").write_text(md, encoding="utf-8")

    rng = random.Random(20261028)
    shuffled = list(fetched)
    rng.shuffle(shuffled)

    manifest = {"papers": [], "anon_to_sp": {}}
    for idx, (meta, md) in enumerate(shuffled, 1):
        anon_id = f"SP_ANON_{idx:03d}"
        meta["anon_id"] = anon_id
        scrubbed = scrub_spond_manuscript(md, meta, anon_id)
        meta["scrubbed_bytes"] = len(scrubbed)
        (sp_dir / "anon_papers" / f"{anon_id}.md").write_text(scrubbed, encoding="utf-8")
        manifest["anon_to_sp"][anon_id] = meta["sp_id"]
        manifest["papers"].append(meta)

    manifest["papers"].sort(key=lambda x: x["sp_id"])
    with open(sp_dir / "manifest.json", "w") as f:
        json.dump(manifest, f, indent=2)

    roles = {}
    decades = {}
    for m, _ in fetched:
        roles[m["authorship_role"]] = roles.get(m["authorship_role"], 0) + 1
        decades[m["decade"]] = decades.get(m["decade"], 0) + 1
    print("Breakdown by Authorship Role:", roles)
    print("Breakdown by Decade:", decades)

if __name__ == "__main__":
    main()
