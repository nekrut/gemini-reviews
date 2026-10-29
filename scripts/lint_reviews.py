#!/usr/bin/env python3
"""
Lint all reviews/**/review.md files against REVIEW_TEMPLATE.md:
banned phrases (Part 2), required section headers (Part 4), and
Score Breakdown consistency with the sibling metadata.json.

Warning-only by default; pass --strict to exit non-zero on any violation.
"""

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REVIEWS_DIR = ROOT / "reviews"
TEMPLATE_FILE = ROOT / "REVIEW_TEMPLATE.md"

BANNED_PHRASES = [
    "groundbreaking",
    "tour de force",
    "pivotal",
    "crucial",
    "crucially",
    "compelling",
    "delve",
    "tapestry",
    "landscape",
    "it is worth noting",
    "importantly",
    "not only",
    "serves as a testament",
    "landmark",
]
BANNED_RE = re.compile(
    r"\b(" + "|".join(re.escape(p).replace(r"\ ", r"\s+") for p in BANNED_PHRASES) + r")\b",
    re.IGNORECASE,
)
QUOTED_RE = re.compile(r"\"[^\"\n]*\"|“[^”\n]*”")

SCORE_KEYS = [
    ("Rigor", "rigor"),
    ("Claims", "claims"),
    ("Biology", "biology"),
    ("Reproducibility", "reproducibility"),
]
BREAKDOWN_RE = re.compile(
    r"Score Breakdown(?:\s*\([^)]*\))?:?\**:?\s*"
    + r"\s*\|\s*".join(rf"{label}:\s*([0-9]+(?:\.[0-9]+)?)\s*/\s*[0-9.]+" for label, _ in SCORE_KEYS),
    re.IGNORECASE,
)
TOL = 0.05


def required_headers() -> list[str]:
    """Return heading prefixes (levels 1-3) from the Part 4 template block."""
    text = TEMPLATE_FILE.read_text(encoding="utf-8")
    part4 = text.split("## PART 4", 1)[1]
    block = part4.split("```markdown", 1)[1].split("```", 1)[0]
    headers = []
    for line in block.splitlines():
        m = re.match(r"^(#{1,3}) (.+)$", line.strip())
        if m:
            # Bracketed placeholders (e.g. [MANUSCRIPT_ID]) -> prefix match
            headers.append(f"{m.group(1)} {m.group(2).split('[', 1)[0].strip()}")
    return headers


def lint_file(path: Path, headers: list[str]) -> list[tuple[int, str, str]]:
    violations = []
    lines = path.read_text(encoding="utf-8").splitlines()

    # 1. Banned phrases (outside quoted spans)
    for i, line in enumerate(lines, start=1):
        for m in BANNED_RE.finditer(QUOTED_RE.sub("", line)):
            violations.append((i, "BANNED", f"banned phrase '{m.group(1).lower()}'"))

    # 2. Required headers
    stripped = [l.strip() for l in lines]
    for h in headers:
        if not any(l == h or l.startswith(h + " ") for l in stripped):
            violations.append((1, "HEADER", f"missing required header '{h}'"))

    # 3. Score Breakdown vs metadata.json
    bd_line, bd = None, None
    for i, line in enumerate(lines, start=1):
        if "Score Breakdown" in line:
            m = BREAKDOWN_RE.search(line)
            bd_line = i
            if m:
                bd = [float(x) for x in m.groups()]
            break
    if bd_line is None:
        violations.append((1, "SCORE", "missing Score Breakdown line"))
        return violations
    if bd is None:
        violations.append((bd_line, "SCORE", "unparseable Score Breakdown line"))
        return violations

    meta_path = path.parent / "metadata.json"
    if not meta_path.exists():
        violations.append((bd_line, "SCORE", "no sibling metadata.json"))
        return violations
    with open(meta_path, "r", encoding="utf-8") as f:
        scores = json.load(f).get("scores", {})
    for (label, key), val in zip(SCORE_KEYS, bd):
        meta_val = scores.get(key)
        if meta_val is None or abs(float(meta_val) - val) > TOL / 2:
            violations.append((bd_line, "SCORE", f"{label} {val} != metadata.json {meta_val}"))
    overall = scores.get("overall")
    if overall is None:
        violations.append((bd_line, "SCORE", "metadata.json missing overall score"))
    elif abs(sum(bd) - float(overall)) > TOL:
        violations.append((bd_line, "SCORE", f"sub-scores sum {sum(bd):.2f} != overall {overall}"))
    return violations


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.strip().splitlines()[0])
    parser.add_argument("--strict", action="store_true", help="exit 1 if any violation is found")
    parser.add_argument("--strict-score", action="store_true", help="exit 1 if any SCORE violation is found")
    args = parser.parse_args()

    headers = required_headers()
    counts: dict[str, int] = {}
    n_files = 0
    for path in sorted(REVIEWS_DIR.glob("**/review.md")):
        n_files += 1
        for line_no, code, msg in lint_file(path, headers):
            print(f"{path.relative_to(ROOT)}:{line_no}: {code} {msg}")
            counts[code] = counts.get(code, 0) + 1

    total = sum(counts.values())
    summary = ", ".join(f"{code}={n}" for code, n in sorted(counts.items())) or "none"
    print(f"\nLinted {n_files} review(s): {total} violation(s) ({summary}).")
    if (args.strict and total) or (args.strict_score and counts.get("SCORE", 0) > 0):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
