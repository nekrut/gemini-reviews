#!/usr/bin/env python3
"""Rogan-Gladen prevalence + percentile-bootstrap 95% intervals for the N=200 study.

Resamples Cohorts A, B and C jointly (with replacement, within cohort), so the
intervals include Se, Sp and p_obs uncertainty. Estimates are clipped to [0, 1].
Usage: python3 -I scripts/rg_bootstrap.py [--reps 5000] [--seed 20261028]
"""
import argparse
import json
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
UPSTREAM = {"A07", "A11", "A19", "A24", "A25"}  # excluded from "Internal A" (N=45)
CUTS = (5.0, 5.5, 6.0, 6.5)


def rg(a, b, c, cut):
    se = sum(s < cut for s in a) / len(a)
    sp = sum(s >= cut for s in b) / len(b)
    p = sum(s < cut for s in c) / len(c)
    den = se + sp - 1
    if den <= 0:
        return float("nan")
    return min(1.0, max(0.0, (p + sp - 1) / den))


def pct(v, q):
    v = sorted(v)
    k = (len(v) - 1) * q
    lo, hi = int(k), min(int(k) + 1, len(v) - 1)
    return v[lo] + (v[hi] - v[lo]) * (k - lo)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--reps", type=int, default=5000)
    ap.add_argument("--seed", type=int, default=20261028)
    args = ap.parse_args()
    d = json.loads((ROOT / "calibration" / "results_200.json").read_text())
    a_all = [x["overall"] for x in d["cohort_a"]]
    a_int = [x["overall"] for x in d["cohort_a"] if x["cohort_id"] not in UPSTREAM]
    b = [x["overall"] for x in d["cohort_b"]]
    c = [x["overall"] for x in d["cohort_c"]]
    rng = random.Random(args.seed)
    for label, a in (("All A", a_all), ("Internal A", a_int)):
        print(f"{label} (N_A={len(a)}, N_B={len(b)}, N_C={len(c)})")
        boots = {cut: [] for cut in CUTS}
        for _ in range(args.reps):
            ra = rng.choices(a, k=len(a))
            rb = rng.choices(b, k=len(b))
            rc = rng.choices(c, k=len(c))
            for cut in CUTS:
                v = rg(ra, rb, rc, cut)
                if v == v:
                    boots[cut].append(v)
        for cut in CUTS:
            v = boots[cut]
            print(f"  S<{cut}: RG={rg(a, b, c, cut):.1%}  "
                  f"95% CI [{pct(v, .025):.1%}, {pct(v, .975):.1%}]")


if __name__ == "__main__":
    main()
