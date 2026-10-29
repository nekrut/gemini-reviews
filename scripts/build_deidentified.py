from pathlib import Path
import os
import re
import json
import random

os.makedirs(str(Path(__file__).resolve().parent.parent / "papers_anon", exist_ok=True)
os.makedirs(str(Path(__file__).resolve().parent.parent / "reviews_anon", exist_ok=True)

with open(str(Path(__file__).resolve().parent.parent / "cohorts.json") as f:
    cohorts = json.load(f)

ab_papers = cohorts["cohort_a"] + cohorts["cohort_b"]
rng = random.Random(20261028)
shuffled = list(ab_papers)
rng.shuffle(shuffled)

anon_map = {}

def scrub_manuscript(txt, meta, anon_id):
    text = re.sub(r'(?:https?://)?\bgithub\.com/(?!spond/gemini-reviews\b)[A-Za-z0-9_.-]+(?:/[A-Za-z0-9_.-]+)*', '[GITHUB_REPO_REDACTED]', text, flags=re.I)
    lines = txt.splitlines()
    # Drop the top metadata header lines (# A01..., **Title:**..., **Authors:**..., **Venue:**...)
    cleaned_lines = []
    in_body = False
    skip_section = False
    for line in lines:
        s = line.strip()
        if not in_body:
            if s.startswith("## ABSTRACT") or s.startswith("## Abstract") or s.startswith("## MAIN TEXT") or s.startswith("### Abstract") or s.startswith("### Background") or s.startswith("## Introduction") or s.startswith("### Introduction"):
                in_body = True
                cleaned_lines.append(line)
            continue
        # Detect and skip Acknowledgements, Author Contributions, Funding, and Retraction banner sections
        if re.match(r"^#{1,4}\s*(acknowledg|author\s+contribution|funding|competing\s+interest|conflict\s+of\s+interest|retraction)", s, flags=re.IGNORECASE):
            skip_section = True
            continue
        elif re.match(r"^#{1,4}\s+\S", s):
            skip_section = False
        if skip_section:
            continue
        # Skip journal courtesy / license / correspondence / retraction boilerplate lines
        if any(pat in s for pat in [
            "Articles from ",
            "courtesy of ",
            "Corresponding author",
            "Correspondence:",
            "contributed equally",
            "This article is published and distributed under",
            "This article is made available via the PMC Open Access",
            "This article has been retracted",
            "RETRACTED:",
            "Retraction Notice",
            "Received 20",
            "Accepted 20",
            "Published online",
            "Competing interests:",
            "Conflict of interest",
            " Author ",
        ]):
            continue
        cleaned_lines.append(line)

    # Fallback if in_body didn't trigger early enough
    if len("\n".join(cleaned_lines)) < 3000:
        cleaned_lines = []
        for line in lines[5:]:
            s = line.strip()
            if s.startswith("### ") and len(s) < 45 and "," not in s and not any(w in s.lower() for w in ["abstract", "introduction", "method", "result", "discussion", "background", "data", "model", "statistical", "analysis", "conclusion"]):
                # Likely an author name heading from PMC HTML
                continue
            if any(pat in s for pat in ["Articles from ", "courtesy of ", "Corresponding author", "Correspondence:", "contributed equally", "Received 20", "This article has been retracted", "RETRACTED:"]):
                continue
            cleaned_lines.append(line)

    body = "\n".join(cleaned_lines)

    # Strip RETRACTED: / WITHDRAWN: title prefixes anywhere in text
    body = re.sub(r"\b(RETRACTED|WITHDRAWN)\s*:\s*", "", body, flags=re.IGNORECASE)

    # Scrub exact Title (with or without RETRACTED: prefix), DOI, PMCID, PMID, and Journal name
    if meta.get("title"):
        t_clean = re.sub(r"^(RETRACTED|WITHDRAWN)\s*:\s*", "", meta["title"], flags=re.IGNORECASE).rstrip(".")
        if len(t_clean) > 15:
            body = re.sub(re.escape(t_clean), "[REDACTED_TITLE]", body, flags=re.IGNORECASE)
    if meta.get("doi"):
        body = body.replace(meta["doi"], "[REDACTED_DOI]")
    if meta.get("pmcid"):
        body = body.replace(meta["pmcid"], "[REDACTED_ID]")
    if meta.get("pmid"):
        body = body.replace(str(meta["pmid"]), "[REDACTED_ID]")
    if meta.get("journal") and len(meta["journal"]) > 4:
        body = re.sub(r"\b" + re.escape(meta["journal"]) + r"\b", "[REDACTED_VENUE]", body, flags=re.IGNORECASE)

    # Scrub GitHub / GitLab / Bitbucket / Zenodo URLs and user/repo handles that can leak author/lab identity
    body = re.sub(r"https?://(?:www\.)?github\.com/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", "[GITHUB_REPO_REDACTED]", body, flags=re.IGNORECASE)
    body = re.sub(r"\bgithub\.com/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", "[GITHUB_REPO_REDACTED]", body, flags=re.IGNORECASE)
    body = re.sub(r"https?://(?:www\.)?gitlab\.com/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", "[GITLAB_REPO_REDACTED]", body, flags=re.IGNORECASE)
    body = re.sub(r"\bgitlab\.com/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", "[GITLAB_REPO_REDACTED]", body, flags=re.IGNORECASE)
    body = re.sub(r"https?://(?:www\.)?bitbucket\.org/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", "[BITBUCKET_REPO_REDACTED]", body, flags=re.IGNORECASE)

    # Scrub author surnames from the author list (including short surnames when followed by et al. or year citations)
    common_words = {"wang", "chen", "zhang", "yang", "long", "park", "hill", "wood", "hall", "king", "west", "cole", "ross", "cook", "bell", "ward", "cox", "gray", "hunt", "pond", "love", "berg", "field"}
    if meta.get("authors"):
        for part in meta["authors"].split(","):
            tokens = part.strip().split()
            if tokens:
                surname = tokens[0].strip(".")
                # Always scrub 'Surname et al.' self-citations regardless of surname length
                if len(surname) >= 3:
                    body = re.sub(r"\b" + re.escape(surname) + r"\s+et\s+al\.?", "[AUTHOR et al.]", body, flags=re.IGNORECASE)
                if len(surname) >= 5 and surname.lower() not in common_words:
                    body = re.sub(r"\b" + re.escape(surname) + r"\b", "[AUTHOR]", body)

    # Scrub any post-t0 year mentions (years strictly greater than publication year t0)
    pub_year = meta.get("year")
    if isinstance(pub_year, int) and 1990 <= pub_year <= 2026:
        for future_yr in range(pub_year + 1, 2028):
            body = re.sub(r"\b" + str(future_yr) + r"\b", "[POST_T0_YEAR_REDACTED]", body)

    header = [
        f"# De-Identified Manuscript `{anon_id}`",
        "**Title:** [REDACTED FOR BLINDED REVIEW]",
        "**Authors:** [REDACTED FOR BLINDED REVIEW]",
        "**Venue / Year:** [REDACTED FOR BLINDED REVIEW]",
        "",
    ]
    return "\n".join(header) + "\n" + body

if __name__ == "__main__":
    for idx, meta in enumerate(shuffled, 1):
        anon_id = f"ANON_{idx:02d}"
        pmcid = meta["pmcid"]
        cid = meta["cohort_id"]
        src_path = fstr(Path(__file__).resolve().parent.parent / "papers/{cid}_{pmcid}.md"
        raw_txt = open(src_path).read()
        scrubbed = scrub_manuscript(raw_txt, meta, anon_id)
        out_path = fstr(Path(__file__).resolve().parent.parent / "papers_anon/{anon_id}.md"
        with open(out_path, "w") as f:
            f.write(scrubbed)
        anon_map[anon_id] = {
            "anon_id": anon_id,
            "cohort_id": cid,
            "cohort": meta["cohort"],
            "pmcid": pmcid,
            "pmid": meta["pmid"],
            "title": meta["title"],
            "journal": meta["journal"],
            "year": meta["year"],
            "domain": meta["domain"],
            "scrubbed_bytes": len(scrubbed)
        }

    with open("/tmp/anon_map_ab.json", "w") as f:
        json.dump(anon_map, f, indent=2)

    min_sz = min(v["scrubbed_bytes"] for v in anon_map.values())
    print(f"Created 50 de-identified manuscripts in papers_anon/ (min size: {min_sz} bytes)")
