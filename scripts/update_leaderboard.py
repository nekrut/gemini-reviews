#!/usr/bin/env python3
"""
Rebuild index.json from all reviews/**/metadata.json files and update the
Running Tab leaderboard table in README.md.
"""

import html
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REVIEWS_DIR = ROOT / "reviews"
INDEX_FILE = ROOT / "index.json"
README_FILE = ROOT / "README.md"

START_MARKER = "<!-- LEADERBOARD_START -->"
END_MARKER = "<!-- LEADERBOARD_END -->"

TIERS = [
    (9.0, "Exemplary"),
    (7.0, "Strong / Sound"),
    (5.0, "Mixed / Salvageable"),
    (3.0, "Flawed / Overstated"),
    (0.0, "Fundamentally Invalid"),
]
SUB_RANGES = {"rigor": 3.5, "claims": 2.5, "biology": 2.0, "reproducibility": 2.0}
# Entries with known pre-existing inconsistencies: warn instead of raising.
KNOWN_EXCEPTIONS: set[str] = set()


def tier_for(score: float) -> str:
    s = round(float(score), 1)
    for threshold, name in TIERS:
        if s >= threshold:
            return name
    return TIERS[-1][1]


def validate(data: dict, meta_path: Path) -> None:
    scores = data.get("scores", {})
    errors = []
    for key, hi in SUB_RANGES.items():
        v = float(scores.get(key, 0.0))
        if not 0.0 <= v <= hi:
            errors.append(f"{key}={v} outside [0, {hi}]")
    overall = float(scores.get("overall", 0.0))
    total = round(sum(float(scores.get(k, 0.0)) for k in SUB_RANGES), 2)
    if abs(total - overall) > 0.05:
        errors.append(f"sub-score sum {total} != overall {overall}")
    expected = tier_for(overall)
    if data.get("tier") != expected:
        errors.append(f"tier {data.get('tier')!r} != {expected!r} for {overall}")
    if errors:
        rel = meta_path.relative_to(ROOT)
        msg = f"{rel}: " + "; ".join(errors)
        if str(rel) in KNOWN_EXCEPTIONS:
            print(f"WARNING: {msg}", file=sys.stderr)
        else:
            raise ValueError(msg)


def cell(text: str) -> str:
    text = html.unescape(str(text))
    text = re.sub(r"</?i>", "*", text, flags=re.IGNORECASE)
    text = text.replace("|", "\\|")
    return re.sub(r"\s*[\r\n]+\s*", " ", text).strip()


def collect_reviews() -> list[dict]:
    entries = []
    if REVIEWS_DIR.exists():
        for meta_path in sorted(REVIEWS_DIR.glob("**/metadata.json")):
            with open(meta_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            validate(data, meta_path)
            rel_review = meta_path.parent.relative_to(ROOT) / "review.md"
            data["review_path"] = str(rel_review)
            entries.append(data)
    # Sort descending by overall score, then descending by review date
    entries.sort(
        key=lambda x: (
            float(x.get("scores", {}).get("overall", 0.0)),
            x.get("reviewed_at", ""),
        ),
        reverse=True,
    )
    return entries


def format_table(entries: list[dict]) -> str:
    if not entries:
        return "_No manuscripts reviewed yet. Open an [Issue](../../issues/new?template=review_request.yml) to trigger an automated review._"

    lines = [
        "| Rank | Date | Manuscript Title | Authors | Venue / Year | Rigor (/3.5) | Claims (/2.5) | Biology (/2.0) | Repro (/2.0) | **Overall (/10)** | Tier | Review |",
        "| :---: | :---: | :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :---: |",
    ]
    for idx, item in enumerate(entries, start=1):
        scores = item.get("scores", {})
        rigor = f"{scores.get('rigor', 0.0):.1f}"
        claims = f"{scores.get('claims', 0.0):.1f}"
        biology = f"{scores.get('biology', 0.0):.1f}"
        repro = f"{scores.get('reproducibility', 0.0):.1f}"
        overall = f"**{scores.get('overall', 0.0):.1f}**"
        tier = item.get("tier", "")
        title = cell(item.get("title", "Untitled"))
        doi_url = item.get("url", "")
        title_cell = f"[{title}]({doi_url})" if doi_url else title
        authors = cell(item.get("authors_short", item.get("authors", "")))
        venue = cell(item.get("venue", ""))
        date_str = item.get("reviewed_at", "")[:10]
        review_link = f"[Review]({item.get('review_path', '')})"
        if item.get("issue_number"):
            review_link += f" ([#{item['issue_number']}](../../issues/{item['issue_number']}))"
        lines.append(
            f"| {idx} | {date_str} | {title_cell} | {authors} | {venue} | {rigor} | {claims} | {biology} | {repro} | {overall} | {tier} | {review_link} |"
        )
    return "\n".join(lines)


def main() -> None:
    entries = collect_reviews()
    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        json.dump(entries, f, indent=2, ensure_ascii=False)
        f.write("\n")

    table_md = format_table(entries)
    if README_FILE.exists():
        content = README_FILE.read_text(encoding="utf-8")
        if START_MARKER in content and END_MARKER in content:
            before, rest = content.split(START_MARKER, 1)
            _, after = rest.split(END_MARKER, 1)
            updated = f"{before}{START_MARKER}\n{table_md}\n{END_MARKER}{after}"
            README_FILE.write_text(updated, encoding="utf-8")
            print(f"Updated {README_FILE.name} and {INDEX_FILE.name} with {len(entries)} review(s).")
            return
    print(f"Wrote {INDEX_FILE.name} ({len(entries)} review(s)).")


if __name__ == "__main__":
    main()
