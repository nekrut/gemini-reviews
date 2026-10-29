import urllib.request
import urllib.parse
import json
import random
import re
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup

def clean_text(el):
    if el is None:
        return ""
    return re.sub(r"\s+", " ", el.get_text(" ", strip=True)).strip()

sec_dir = Path(str(Path(__file__).resolve().parent.parent / "secular_trend_exp")
for sub in ["raw_papers", "anon_papers", "reviews"]:
    d = sec_dir / sub
    d.mkdir(parents=True, exist_ok=True)
    for f in d.glob("*.md"):
        f.unlink()

windows = [
    ("W1_1991_1995", "1991–1995", 1991, 1995),
    ("W2_1996_2000", "1996–2000", 1996, 2000),
    ("W3_2001_2005", "2001–2005", 2001, 2005),
    ("W4_2006_2010", "2006–2010", 2006, 2010),
    ("W5_2011_2015", "2011–2015", 2011, 2015),
    ("W6_2016_2020", "2016–2020", 2016, 2020),
    ("W7_2021_2025", "2021–2025", 2021, 2025),
]

tracks = [
    ("Molecular Evolution & Phylogenetics", 3, "phylogenetic AND sequence AND evolution"),
    ("Viral Evolution & Virology", 3, "virus AND mutation AND sequence"),
    ("Population & Statistical Genetics", 2, "genetics AND allele AND polymorphism"),
    ("Gene Expression & Functional Genomics", 2, "expression AND mRNA AND transcription"),
]

# Also exclude any PMCIDs already used in our main 200-paper calibration, OOD, or peer-review cohorts
existing_pmcids = set()
for mf in [
    Path(str(Path(__file__).resolve().parent.parent / "data/cohort_manifest.json"),
    Path(str(Path(__file__).resolve().parent.parent / "ood_exp/manifest.json"),
    Path(str(Path(__file__).resolve().parent.parent / "peer_review_exp/manifest.json"),
]:
    if mf.exists():
        try:
            txt = mf.read_text()
            for m in re.findall(r"PMC\d+", txt):
                existing_pmcids.add(m)
        except Exception:
            pass

print(f"Loaded {len(existing_pmcids)} existing PMCIDs to exclude.")

def parse_epmc_xml(xml_bytes, meta):
    soup = BeautifulSoup(xml_bytes, "xml")
    body = soup.find("body")
    if not body:
        return ""
    lines = [
        f"# {meta['pmcid']} ({meta['year']})",
        f"**Title:** {meta['title']}",
        f"**Authors:** {meta['authors']}",
        f"**Journal:** {meta['journal']} ({meta['year']}) | **PMID:** {meta.get('pmid','')}",
        ""
    ]
    abstract = soup.find("abstract")
    if abstract:
        lines.append("\n## Abstract\n")
        for p in abstract.find_all("p"):
            t = clean_text(p)
            if t:
                lines.append(t + "\n")
    for el in body.find_all(["sec", "p", "table-wrap", "fig"]):
        if el.name == "sec":
            title_el = el.find("title", recursive=False)
            if title_el:
                t = clean_text(title_el)
                if t and t.lower() not in ("references", "supplementary material", "acknowledgments", "acknowledgements", "funding", "author contributions", "competing interests"):
                    lines.append(f"\n## {t}\n")
        elif el.name == "p":
            if el.find_parent("table-wrap") or el.find_parent("fig") or el.find_parent("abstract"):
                continue
            t = clean_text(el)
            if len(t) > 20:
                lines.append(t + "\n")
        elif el.name == "table-wrap":
            lbl = clean_text(el.find("label"))
            cap = clean_text(el.find("caption"))
            lines.append(f"\n### {lbl}: {cap}\n")
            tbl = el.find("table")
            if tbl:
                for tr in tbl.find_all("tr")[:35]:
                    cells = [clean_text(c) for c in tr.find_all(["th", "td"])]
                    if cells:
                        lines.append("| " + " | ".join(cells) + " |")
        elif el.name == "fig":
            lbl = clean_text(el.find("label"))
            cap = clean_text(el.find("caption"))
            if cap:
                lines.append(f"\n> **{lbl}:** {cap}\n")
    return "\n".join(lines)

def scrub_temporal_manuscript(raw_text, meta, anon_id):
    text = re.sub(r'(?:https?://)?\bgithub\.com/(?!spond/gemini-reviews\b)[A-Za-z0-9_.-]+(?:/[A-Za-z0-9_.-]+)*', '[GITHUB_REPO_REDACTED]', text, flags=re.I)
    lines = raw_text.splitlines()
    body_start = 0
    for idx, line in enumerate(lines):
        if line.strip().startswith("## Abstract") or line.strip().startswith("## Introduction") or line.strip().startswith("## INTRODUCTION"):
            body_start = idx
            break
    if body_start == 0:
        body_start = min(6, len(lines))
    body_lines = []
    skip_section = False
    skip_headers = ("acknowledg", "funding", "author contribution", "competing interest", "conflict of interest", "declaration", "ethics", "publisher", "citation", "copyright", "correspondence", "footnote", "abbreviations", "open access", "supplementary", "additional information", "contributor information")
    for line in lines[body_start:]:
        s = line.strip()
        if s.startswith("#"):
            hdr = s.lstrip("#").strip().lower()
            if any(k in hdr for k in skip_headers):
                skip_section = True
                continue
            else:
                skip_section = False
        if not skip_section:
            body_lines.append(line)
    text = "\n".join(body_lines)
    if meta.get("doi"):
        text = text.replace(meta["doi"], "[REDACTED_DOI]")
    if meta.get("pmcid"):
        text = text.replace(meta["pmcid"], "[REDACTED_ID]")
    if meta.get("pmid"):
        text = text.replace(str(meta["pmid"]), "[REDACTED_ID]")
    if meta.get("journal"):
        j = meta["journal"]
        if len(j) > 3:
            text = re.sub(re.escape(j), "[REDACTED_VENUE]", text, flags=re.IGNORECASE)
    for token in re.split(r"[,;\s]+", meta.get("authors", "")):
        t = token.strip(".")
        if len(t) >= 4 and t.lower() not in ("with", "from", "university", "group", "consortium", "study", "team", "gene", "cell", "data", "long", "high", "west", "east", "hall", "king", "wood", "hill", "bell", "ward", "page", "cole", "ross", "cook", "reed", "lane", "ford"):
            text = re.sub(r"\b" + re.escape(t) + r"\b", "[REDACTED_AUTHOR]", text)
    # Scrub 4-digit calendar years (1980-2026) to prevent temporal dating
    text = re.sub(r"\b(19[89]\d|20[0-2]\d)\b", "[YEAR]", text)
    header = f"# Anonymous Manuscript ID: {anon_id}\n\n*(All identifying metadata, author names, journal titles, DOIs, and publication/citation calendar years have been scrubbed for temporally blinded review.)*\n\n"
    return header + text

rng = random.Random(20261028)
selected_papers = []

for w_code, w_label, y1, y2 in windows:
    print(f"\n=== Sampling Window {w_label} ===")
    window_papers = []
    for track_name, target_n, q_terms in tracks:
        q = f'OPEN_ACCESS:Y AND IN_EPMC:Y AND PUB_TYPE:"research-article" AND PUB_YEAR:[{y1} TO {y2}] AND {q_terms} AND NOT PUB_TYPE:"review"'
        u = f"https://www.ebi.ac.uk/europepmc/webservices/rest/search?query={urllib.parse.quote(q)}&resultType=lite&pageSize=120&format=json"
        try:
            d = json.loads(urllib.request.urlopen(u, timeout=20).read().decode())
            cands = [
                r for r in d.get("resultList", {}).get("result", [])
                if r.get("pmcid") and r["pmcid"] not in existing_pmcids
                and "retraction" not in r.get("title", "").lower()
                and "correction" not in r.get("title", "").lower()
                and "erratum" not in r.get("title", "").lower()
            ]
        except Exception as e:
            print("Search err:", e)
            cands = []
        rng.shuffle(cands)

        def try_fetch(r):
            pmcid = r["pmcid"]
            try:
                u_xml = f"https://www.ebi.ac.uk/europepmc/webservices/rest/{pmcid}/fullTextXML"
                xb = urllib.request.urlopen(u_xml, timeout=12).read()
                meta = {
                    "pmcid": pmcid,
                    "pmid": r.get("pmid", ""),
                    "doi": r.get("doi", ""),
                    "title": r.get("title", ""),
                    "authors": r.get("authorString", ""),
                    "journal": r.get("journalTitle", ""),
                    "year": int(r.get("pubYear", y1)),
                    "citedByCount": int(r.get("citedByCount", 0)),
                    "window_code": w_code,
                    "window_label": w_label,
                    "track": track_name,
                }
                md = parse_epmc_xml(xb, meta)
                if len(md) >= 12000 and "## " in md:
                    return (meta, md)
            except Exception:
                pass
            return None

        picked = []
        for i in range(0, min(len(cands), 45), 12):
            batch = [c for c in cands[i:i+12] if c["pmcid"] not in existing_pmcids]
            with ThreadPoolExecutor(max_workers=8) as ex:
                res_list = [x for x in ex.map(try_fetch, batch) if x is not None]
            for meta, md in res_list:
                if meta["pmcid"] not in existing_pmcids and len(picked) < target_n:
                    existing_pmcids.add(meta["pmcid"])
                    picked.append((meta, md))
            if len(picked) >= target_n:
                break

        for meta, md in picked:
            window_papers.append((meta, md))
            print(f"  [{w_label} | {track_name[:20]}] {meta['pmcid']} ({meta['year']}, {meta['journal']}): {len(md)}B | {meta['title'][:45]}")

    selected_papers.extend(window_papers)
    print(f"Window {w_label} total: {len(window_papers)}/10")

print(f"\nTotal sampled across all 7 windows: {len(selected_papers)}/70")

# Assign chronological cohort IDs (SEC_W1_01..SEC_W7_10), then shuffle globally for TIME_ANON_01..70
for idx, (meta, md) in enumerate(selected_papers, 1):
    meta["sec_id"] = f"SEC_{idx:02d}"
    (sec_dir / "raw_papers" / f"{meta['sec_id']}_{meta['pmcid']}.md").write_text(md, encoding="utf-8")

shuffled = list(selected_papers)
rng.shuffle(shuffled)

manifest = {"papers": [], "anon_to_sec": {}}
for idx, (meta, md) in enumerate(shuffled, 1):
    anon_id = f"TIME_ANON_{idx:02d}"
    meta["anon_id"] = anon_id
    scrubbed = scrub_temporal_manuscript(md, meta, anon_id)
    meta["scrubbed_bytes"] = len(scrubbed)
    (sec_dir / "anon_papers" / f"{anon_id}.md").write_text(scrubbed, encoding="utf-8")
    manifest["anon_to_sec"][anon_id] = meta["sec_id"]
    manifest["papers"].append(meta)

manifest["papers"].sort(key=lambda x: x["sec_id"])
with open(sec_dir / "manifest.json", "w") as f:
    json.dump(manifest, f, indent=2)
print("Saved 70 temporally de-identified manuscripts to secular_trend_exp/anon_papers/ and manifest.json!")
