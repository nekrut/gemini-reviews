import urllib.request
import urllib.parse
import json
import random
import re
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup
from fetch_pmc_html import parse_pmc_html, clean_text
from build_deidentified import scrub_manuscript

pr_dir = Path(str(Path(__file__).resolve().parent.parent / "peer_review_exp")

def parse_ppr_xml(xml_bytes, meta):
    soup = BeautifulSoup(xml_bytes, "xml")
    pair_id = meta.get("pair_id", "TEMP")
    ppr_id = meta["ppr_id"]
    title = meta["title"]
    authors = meta.get("authors", "")
    ppr_year = meta["ppr_year"]
    ppr_doi = meta.get("ppr_doi", "")
    lines = [
        f"# {pair_id}_PREPRINT ({ppr_id})",
        f"**Title:** {title}",
        f"**Authors:** {authors}",
        f"**Venue:** Preprint ({ppr_year}) | **DOI:** {ppr_doi}",
        ""
    ]
    abstract = soup.find("abstract")
    if abstract:
        lines.append("\n## Abstract\n")
        for p in abstract.find_all("p"):
            t = clean_text(p)
            if t:
                lines.append(t + "\n")
    body = soup.find("body") or soup
    for el in body.find_all(["sec", "p", "table-wrap", "fig"]):
        if el.name == "sec":
            title_el = el.find("title", recursive=False)
            if title_el:
                t = clean_text(title_el)
                if t and t.lower() not in ("references", "supplementary material", "acknowledgments", "funding", "author contributions", "competing interests"):
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

    # Also extract Data / Code / Materials / Software Availability sections from <back>
    # (Europe PMC preprint JATS XML frequently places <sec sec-type="data-availability">
    # inside <back> rather than <body>; including them ensures symmetric comparison with PMC HTML).
    back = soup.find("back")
    if back:
        for sec in back.find_all(["sec", "notes"]):
            sec_type = (sec.get("sec-type") or sec.get("notes-type") or "").lower()
            title_el = sec.find("title", recursive=False)
            t = clean_text(title_el) if title_el else ""
            t_low = t.lower()
            is_avail = (
                "data-availability" in sec_type
                or "availability" in sec_type
                or any(k in t_low for k in ("availability", "data", "code", "software", "accession", "repository", "resource"))
            )
            if is_avail and t_low not in ("references", "acknowledgments", "acknowledgements", "funding", "author contributions", "competing interests"):
                heading = t if t else "Data and Code Availability"
                lines.append(f"\n## {heading}\n")
                for p in sec.find_all("p"):
                    pt = clean_text(p)
                    if pt:
                        lines.append(pt + "\n")
    return "\n".join(lines)

def split_published_and_decision_letter(pub_md):
    """
    Some open-peer-review journals (notably eLife) append 'Decision letter' and
    'Author response' sections at the end of the PMC HTML article.
    We split those out so:
      1. The blinded AI reviewer auditing the published paper NEVER sees the human peer review or author response!
      2. We save the human decision letter & author response separately for Part B (Human vs AI Peer Review Comparison).
    """
    m = re.search(r"\n##\s+(Decision letter|Peer review|Reviewer reports|Author response|eLife assessment)\b", pub_md, flags=re.IGNORECASE)
    if m:
        return pub_md[:m.start()].strip() + "\n", pub_md[m.start():].strip() + "\n"
    return pub_md, ""

def extra_version_scrub(txt, meta):
    patterns = [
        r"\bbioRxiv\b", r"\bmedRxiv\b", r"\bResearch Square\b", r"\bpreprint\b",
        r"CC-BY-NC-ND", r"CC-BY", r"has not been certified by peer review",
        r"author/funder, who has granted", r"copyright holder for this",
        r"\beLife assessment\b", r"\bDecision letter\b", r"\bAuthor response\b"
    ]
    for pat in patterns:
        txt = re.sub(pat, "[REDACTED]", txt, flags=re.IGNORECASE)
    if meta.get("ppr_doi"):
        txt = txt.replace(meta["ppr_doi"], "[REDACTED_DOI]")
    if meta.get("ppr_id"):
        txt = txt.replace(meta["ppr_id"], "[REDACTED_ID]")
    return txt

tier12_exact = {
    "nature", "nature genetics", "nature communications", "nature microbiology",
    "nature methods", "nature biotechnology", "nature structural & molecular biology",
    "nature ecology & evolution", "nature medicine", "science", "science advances",
    "cell", "cell reports", "cell host & microbe", "cell systems", "molecular cell",
    "genome biology", "genome research", "nucleic acids research", "elife",
    "plos biology", "plos genetics", "plos pathogens", "plos computational biology",
    "molecular biology and evolution", "proceedings of the national academy of sciences of the united states of america",
    "systematic biology", "american journal of human genetics", "bioinformatics",
    "briefings in bioinformatics", "gigascience", "the isme journal", "microbiome",
    "genome biology and evolution", "virus evolution", "journal of virology"
}
tier3_keywords = [
    "scientific reports", "plos one", "frontiers", "bmc ", "viruses", "genes",
    "microorganisms", "international journal of molecular sciences", "cancers",
    "biology", "peerj", "msystems", "msphere", "microbiology spectrum",
    "communications biology", "scientific data", "g3", "infection, genetics and evolution",
    "journal of medical virology", "antibiotics", "pathogens", "animals", "plants",
    "scientific data", "heliyon", "plos global public health", "plos neglected tropical diseases",
    "bmc genomics", "bmc biology", "bmc bioinformatics", "bmc evolutionary biology", "bmc ecology and evolution",
    "bmc infectious diseases", "bmc microbiology", "bmc plant biology", "bmc medical genomics"
]

if __name__ == "__main__":
    for sub in ["raw_preprints", "raw_published", "human_reviews", "wave1_papers", "wave1_reviews", "wave2_papers", "wave2_reviews"]:
        d = pr_dir / sub
        d.mkdir(parents=True, exist_ok=True)
        for f in d.glob("*.md"):
            f.unlink()

    queries = [
        'SRC:PPR AND HAS_FT:Y AND PUB_YEAR:2025 AND ("evolution" OR "genomic" OR "transcriptom" OR "microbiome" OR "single-cell" OR "GWAS" OR "phylogen" OR "virus" OR "RNA-seq" OR "metagenom")',
        'SRC:PPR AND HAS_FT:Y AND PUB_YEAR:2024 AND ("evolution" OR "genomic" OR "transcriptom" OR "microbiome" OR "single-cell" OR "GWAS" OR "phylogen" OR "virus" OR "RNA-seq" OR "metagenom")',
        'SRC:PPR AND HAS_FT:Y AND PUB_YEAR:2025',
    ]

    raw_pairs = []
    seen_pmids = set()
    for q in queries:
        for page in range(1, 7):
            url = f"https://www.ebi.ac.uk/europepmc/webservices/rest/search?query={urllib.parse.quote(q)}&resultType=core&pageSize=250&page={page}&format=json"
            try:
                d = json.loads(urllib.request.urlopen(url, timeout=20).read().decode())
                res = d.get("resultList", {}).get("result", [])
                if not res:
                    break
                for r in res:
                    ppr_id = r.get("id", "")
                    if not ppr_id.startswith("PPR"):
                        continue
                    ppr_num = int(ppr_id[3:])
                    if ppr_num < 950000 and ppr_id != "PPR641536":
                        continue
                    ccl = r.get("commentCorrectionList", {}).get("commentCorrection", [])
                    for c in ccl:
                        if c.get("type") == "Preprint of" and c.get("source") == "MED":
                            pmid = c.get("id")
                            if pmid not in seen_pmids:
                                seen_pmids.add(pmid)
                                raw_pairs.append({
                                    "ppr_id": ppr_id,
                                    "ppr_doi": r.get("doi", ""),
                                    "ppr_year": int(r.get("pubYear", 0)),
                                    "pmid": pmid,
                                    "title": r.get("title", "")
                                })
            except Exception:
                break

    print("Total candidate linked pairs (PPR >= 950000):", len(raw_pairs))

    matched_pairs = []
    for i in range(0, len(raw_pairs), 35):
        batch = raw_pairs[i:i+35]
        pmids_q = " OR ".join(["EXT_ID:" + x["pmid"] for x in batch])
        u2 = f"https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=({urllib.parse.quote(pmids_q)})%20AND%20IN_PMC:Y%20AND%20OPEN_ACCESS:Y&resultType=core&pageSize=100&format=json"
        try:
            d2 = json.loads(urllib.request.urlopen(u2, timeout=20).read().decode())
            med_map = {m.get("pmid"): m for m in d2.get("resultList", {}).get("result", [])}
            for p in batch:
                m = med_map.get(p["pmid"])
                if m and m.get("pmcid"):
                    j = m.get("journalInfo", {}).get("journal", {}).get("title", "")
                    p["pmcid"] = m.get("pmcid")
                    p["journal"] = j
                    p["year"] = int(m.get("pubYear", 0))
                    p["doi"] = m.get("doi", "")
                    p["authors"] = m.get("authorString", "")
                    p["citedByCount"] = int(m.get("citedByCount", 0))
                    matched_pairs.append(p)
        except Exception:
            pass

    t12_pool = [p for p in matched_pairs if p["journal"].lower() in tier12_exact]
    t3_pool = [p for p in matched_pairs if any(k in p["journal"].lower() for k in tier3_keywords) and p not in t12_pool]
    print(f"Strict Tier 1/2 pool: {len(t12_pool)} | Tier 3 pool: {len(t3_pool)}")

    rng = random.Random(20261028)
    rng.shuffle(t12_pool)
    rng.shuffle(t3_pool)

    def try_fetch_both(p):
        ppr_id = p["ppr_id"]
        pmcid = p["pmcid"]
        p["pair_id"] = "TEMP"
        p["cohort_id"] = "TEMP"
        try:
            u_ppr = f"https://www.ebi.ac.uk/europepmc/webservices/rest/{ppr_id}/fullTextXML"
            xml_bytes = urllib.request.urlopen(u_ppr, timeout=12).read()
            ppr_md = parse_ppr_xml(xml_bytes, p)
            if len(ppr_md) < 12000:
                return None
            req_pub = urllib.request.Request(f"https://pmc.ncbi.nlm.nih.gov/articles/{pmcid}/", headers={"User-Agent": "Mozilla/5.0"})
            html_bytes = urllib.request.urlopen(req_pub, timeout=12).read()
            pub_md_full = parse_pmc_html(html_bytes, p)
            pub_md, human_rev_md = split_published_and_decision_letter(pub_md_full)
            if len(pub_md) < 12000:
                return None
            return (p, ppr_md, pub_md, human_rev_md)
        except Exception:
            return None

    with ThreadPoolExecutor(max_workers=10) as ex:
        t12_valid = [x for x in ex.map(try_fetch_both, t12_pool[:30]) if x is not None]
        t3_valid = [x for x in ex.map(try_fetch_both, t3_pool[:35]) if x is not None]

    print(f"Valid full-text pairs fetched -> Tier 1/2: {len(t12_valid)}, Tier 3: {len(t3_valid)}")

    selected_pairs = []
    for tier_label, valid_list in [("Tier 1/2 (Selective Flagship/Society)", t12_valid[:10]), ("Tier 3 (Megajournal / Open-Threshold)", t3_valid[:10])]:
        for p_meta, ppr_md, pub_md, human_rev_md in valid_list:
            pair_id = f"PAIR_{len(selected_pairs)+1:02d}"
            p_meta["pair_id"] = pair_id
            p_meta["cohort_id"] = pair_id
            p_meta["venue_tier"] = tier_label
            p_meta["has_embedded_human_review"] = bool(human_rev_md)
            ppr_id = p_meta["ppr_id"]
            pmcid = p_meta["pmcid"]
            (pr_dir / "raw_preprints" / f"{pair_id}_{ppr_id}.md").write_text(ppr_md, encoding="utf-8")
            (pr_dir / "raw_published" / f"{pair_id}_{pmcid}.md").write_text(pub_md, encoding="utf-8")
            if human_rev_md:
                (pr_dir / "human_reviews" / f"{pair_id}_{pmcid}_human_review.md").write_text(human_rev_md, encoding="utf-8")
            selected_pairs.append((p_meta, ppr_md, pub_md))
            print(f"  {pair_id} [{tier_label[:8]}]: {ppr_id} ({len(ppr_md)}B) -> {pmcid} ({len(pub_md)}B, human_rev={len(human_rev_md)}B) [{p_meta['journal']}] {p_meta['title'][:45]}")

    print(f"Total selected pairs: {len(selected_pairs)} ({len(selected_pairs)*2} manuscripts)")

    wave1_items = []
    wave2_items = []
    for idx, (p_meta, ppr_md, pub_md) in enumerate(selected_pairs):
        if idx % 2 == 0:
            wave1_items.append((p_meta, "preprint", ppr_md))
            wave2_items.append((p_meta, "published", pub_md))
        else:
            wave1_items.append((p_meta, "published", pub_md))
            wave2_items.append((p_meta, "preprint", ppr_md))

    rng.shuffle(wave1_items)
    rng.shuffle(wave2_items)

    manifest = {"pairs": [], "wave1_map": {}, "wave2_map": {}}
    pair_dict = {p["pair_id"]: p for p, _, _ in selected_pairs}

    for idx, (p_meta, ver, md) in enumerate(wave1_items, 1):
        w1_id = f"PR_W1_{idx:02d}"
        scrubbed = extra_version_scrub(scrub_manuscript(md, p_meta, w1_id), p_meta)
        (pr_dir / "wave1_papers" / f"{w1_id}.md").write_text(scrubbed, encoding="utf-8")
        manifest["wave1_map"][w1_id] = {"pair_id": p_meta["pair_id"], "version": ver}
        pair_dict[p_meta["pair_id"]][f"{ver}_anon_id"] = w1_id
        pair_dict[p_meta["pair_id"]][f"{ver}_wave"] = 1
        pair_dict[p_meta["pair_id"]][f"{ver}_bytes"] = len(scrubbed)

    for idx, (p_meta, ver, md) in enumerate(wave2_items, 1):
        w2_id = f"PR_W2_{idx:02d}"
        scrubbed = extra_version_scrub(scrub_manuscript(md, p_meta, w2_id), p_meta)
        (pr_dir / "wave2_papers" / f"{w2_id}.md").write_text(scrubbed, encoding="utf-8")
        manifest["wave2_map"][w2_id] = {"pair_id": p_meta["pair_id"], "version": ver}
        pair_dict[p_meta["pair_id"]][f"{ver}_anon_id"] = w2_id
        pair_dict[p_meta["pair_id"]][f"{ver}_wave"] = 2
        pair_dict[p_meta["pair_id"]][f"{ver}_bytes"] = len(scrubbed)

    manifest["pairs"] = list(pair_dict.values())
    with open(pr_dir / "manifest.json", "w") as f:
        json.dump(manifest, f, indent=2)
    print("Saved wave1_papers, wave2_papers, and manifest.json.")
