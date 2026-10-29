from pathlib import Path
import os
import json
import random
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from fetch_pmc_html import parse_pmc_html
from build_deidentified import scrub_manuscript

with open(str(Path(__file__).resolve().parent.parent / "cohorts_200.json") as f:
    cohorts = json.load(f)

with open("/tmp/anon_map_ab.json") as f:
    already_anon = json.load(f)
with open("/tmp/anon_map_c.json") as f:
    already_anon.update(json.load(f))

done_pmcids = {v["pmcid"]: k for k, v in already_anon.items()}

all_200 = cohorts["cohort_a"] + cohorts["cohort_b"] + cohorts["cohort_c"]
new_papers = [r for r in all_200 if r["pmcid"] not in done_pmcids]
print(f"New papers to fetch & de-identify: {len(new_papers)}")

def fetch_one(meta):
    cid = meta["cohort_id"]
    pmcid = meta["pmcid"]
    out_path = fstr(Path(__file__).resolve().parent.parent / "papers/{cid}_{pmcid}.md"
    if os.path.exists(out_path) and os.path.getsize(out_path) > 5500:
        return (cid, pmcid, "cached", os.path.getsize(out_path))
    
    # Try Europe PMC XML first, then PMC HTML
    urls = [
        f"https://pmc.ncbi.nlm.nih.gov/articles/{pmcid}/",
    ]
    for url in urls:
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"})
            html_bytes = urllib.request.urlopen(req, timeout=20).read()
            md = parse_pmc_html(html_bytes, meta)
            with open(out_path, "w") as f:
                f.write(md)
            return (cid, pmcid, "pmc_html", len(md))
        except Exception as e:
            return (cid, pmcid, f"err:{e}", 0)

with ThreadPoolExecutor(max_workers=6) as ex:
    res = list(ex.map(fetch_one, new_papers))

short = [r for r in res if r[3] < 5500]
print(f"Fetched >5.5KB: {len(res) - len(short)}/{len(new_papers)}")
for s in short:
    print("  Short:", s)
