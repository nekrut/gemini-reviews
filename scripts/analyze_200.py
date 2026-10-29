from pathlib import Path
import os
import re
import json
import math
import statistics
from collections import defaultdict

with open("/tmp/anon_map_200.json") as f:
    anon_map = json.load(f)

UPSTREAM_A_PMCIDS = {"PMC5182071", "PMC3480734", "PMC4125079", "PMC3935878", "PMC7199730"}
METHODS_B_PMCIDS = {"PMC3395634", "PMC4408417", "PMC8204705", "PMC7182206", "PMC6247931", "PMC4302049", "PMC4495769"}

def parse_anon_review(anon_id):
    path = fstr(Path(__file__).resolve().parent.parent / "reviews_anon/{anon_id}.md"
    if not os.path.exists(path):
        return None
    txt = open(path).read()
    m_overall = re.search(r"\*\*Overall Score:\*\*\s*\*\*([0-9.]+)\s*/\s*10(?:\.0)?\*\*\s*\(([^)]+)\)", txt)
    if not m_overall:
        m_overall = re.search(r"Overall Score:\*?\*?\s*\*?\*?([0-9.]+)\s*/\s*10(?:\.0)?\*?\*?\s*\(([^)]+)\)", txt)
    overall = float(m_overall.group(1)) if m_overall else None
    tier = m_overall.group(2).strip() if m_overall else "Unknown"

    def extract_sub(label, denom):
        m = re.search(rf"{label}:\s*\*?\*?([0-9.]+)\s*/\s*{denom}", txt, re.IGNORECASE)
        return float(m.group(1)) if m else None

    return {
        "overall": overall,
        "tier": tier,
        "rigor": extract_sub("Rigor", "3.5"),
        "claims": extract_sub("Claims", "2.5"),
        "biology": extract_sub("Biology", "2.0"),
        "reproducibility": extract_sub(r"Repro(?:ducibility)?", "2.0"),
        "review_path": f"reviews_anon/{anon_id}.md"
    }

def mann_whitney_auc(x_neg, x_pos):
    wins = 0.0
    total = len(x_neg) * len(x_pos)
    for a in x_neg:
        for b in x_pos:
            if b > a:
                wins += 1.0
            elif b == a:
                wins += 0.5
    return wins / total if total else 0.0

def main():
    records = []
    missing = []
    for anon_id, meta in sorted(anon_map.items(), key=lambda kv: int(kv[0].split("_")[1])):
        res = parse_anon_review(anon_id)
        if res is None or res["overall"] is None:
            missing.append((anon_id, meta["cohort_id"], meta["pmcid"]))
            continue
        row = dict(meta)
        row.update(res)
        records.append(row)

    print(f"Parsed de-identified reviews: {len(records)}/200")
    if missing:
        print(f"Missing ({len(missing)}):", missing[:15])
        return

    ca = sorted([r for r in records if r["cohort"] == "A"], key=lambda x: x["cohort_id"])
    cb = sorted([r for r in records if r["cohort"] == "B"], key=lambda x: x["cohort_id"])
    cc = sorted([r for r in records if r["cohort"] == "C"], key=lambda x: int(x["cohort_id"][1:]))

    sa = [r["overall"] for r in ca]
    sb = [r["overall"] for r in cb]
    sc = [r["overall"] for r in cc]

    auc = mann_whitney_auc(sa, sb)
    ca_internal = [r["overall"] for r in ca if r["pmcid"] not in UPSTREAM_A_PMCIDS]
    cb_empirical = [r["overall"] for r in cb if r["pmcid"] not in METHODS_B_PMCIDS]
    cb_methods = [r["overall"] for r in cb if r["pmcid"] in METHODS_B_PMCIDS]
    auc_emp = mann_whitney_auc(sa, cb_empirical)

    print(f"\n=== 200-PAPER DE-IDENTIFIED SUMMARY ===")
    print(f"Cohort A (Invalid, N={len(ca)}): mean={statistics.mean(sa):.2f}, median={statistics.median(sa):.2f}, sd={statistics.stdev(sa):.2f}")
    print(f"  -> Internal-Flaw Subset (N={len(ca_internal)}): mean={statistics.mean(ca_internal):.2f}, median={statistics.median(ca_internal):.2f}")
    print(f"Cohort B (Valid,   N={len(cb)}): mean={statistics.mean(sb):.2f}, median={statistics.median(sb):.2f}, sd={statistics.stdev(sb):.2f}")
    print(f"  -> Empirical Discovery Controls (N={len(cb_empirical)}): mean={statistics.mean(cb_empirical):.2f}, median={statistics.median(cb_empirical):.2f}")
    print(f"  -> Methodological Controls      (N={len(cb_methods)}): mean={statistics.mean(cb_methods):.2f}, median={statistics.median(cb_methods):.2f}")
    print(f"Cohort C (Wild,   N={len(cc)}): mean={statistics.mean(sc):.2f}, median={statistics.median(sc):.2f}, sd={statistics.stdev(sc):.2f}")
    print(f"ROC-AUC (All Cohort B vs Cohort A): {auc:.4f} | (Empirical Cohort B vs Cohort A): {auc_emp:.4f}")

    print("\n=== PREVALENCE ESTIMATORS & 95% CIs (N_A=50, N_B=50, N_C=100) ===")
    by_dom = defaultdict(list)
    for r in cc:
        by_dom[r["domain"]].append(r["overall"])

    for cutoff in [5.0, 5.5, 6.0, 6.5]:
        se = sum(1 for x in sa if x < cutoff) / len(sa)
        se_int = sum(1 for x in ca_internal if x < cutoff) / len(ca_internal)
        sp = sum(1 for x in sb if x >= cutoff) / len(sb)
        p_obs = sum(1 for x in sc if x < cutoff) / len(sc)

        # Stratified SE for p_obs across H=5 equal strata (n_h=20)
        var_strat = 0.0
        for d, vals in by_dom.items():
            nh = len(vals)
            ph = sum(1 for x in vals if x < cutoff) / nh
            var_strat += (nh / len(sc))**2 * (ph * (1.0 - ph) / nh)
        se_p_strat = math.sqrt(var_strat)
        ci_p_obs = 1.96 * se_p_strat

        denom = se + sp - 1.0
        pi_rg = max(0.0, min(1.0, (p_obs - (1.0 - sp)) / denom))
        # Delta method variance for Rogan-Gladen
        var_se = se * (1.0 - se) / len(sa)
        var_sp = sp * (1.0 - sp) / len(sb)
        var_rg = (var_strat + (pi_rg**2) * var_se + ((1.0 - pi_rg)**2) * var_sp) / (denom**2)
        ci_rg = 1.96 * math.sqrt(var_rg)

        print(f"Cutoff < {cutoff:.1f}:")
        print(f"  Se (All A) = {se*100:5.1f}% ({sum(1 for x in sa if x < cutoff)}/50) | Se (Internal A) = {se_int*100:5.1f}% ({sum(1 for x in ca_internal if x < cutoff)}/{len(ca_internal)}) | Sp = {sp*100:5.1f}% ({sum(1 for x in sb if x >= cutoff)}/50)")
        print(f"  Wild p_obs = {p_obs*100:5.1f}% ({sum(1 for x in sc if x < cutoff)}/100) [Stratified 95% CI: +/- {ci_p_obs*100:4.1f}% -> ({max(0,p_obs-ci_p_obs)*100:4.1f}%, {min(1,p_obs+ci_p_obs)*100:4.1f}%)]")
        print(f"  Rogan-Gladen pi_true = {pi_rg*100:5.1f}% [Delta-Method 95% CI: +/- {ci_rg*100:4.1f}% -> ({max(0,pi_rg-ci_rg)*100:4.1f}%, {min(1,pi_rg+ci_rg)*100:4.1f}%)]")

    print("\n=== COHORT C BY SUBFIELD (n=20 per subfield, 100 total) ===")
    for d in ["Molecular Evolution", "Viral Evolution", "Statistical Genetics", "Cancer & Microbiome", "Transcriptomics & CompBio"]:
        vals = by_dom[d]
        f50 = sum(1 for x in vals if x < 5.0)
        f65 = sum(1 for x in vals if x < 6.5)
        print(f"  {d:26s} (n={len(vals):2d}) | mean={statistics.mean(vals):.2f} (med={statistics.median(vals):.2f}) | <5.0: {f50:2d}/20 ({f50*5:3d}%) | <6.5: {f65:2d}/20 ({f65*5:3d}%)")

    print("\n=== COHORT C BY CITATION TIER (N=100) ===")
    by_cite = defaultdict(list)
    for r in cc:
        by_cite[r["citation_tier"]].append(r["overall"])
    for ct in ["High (>=25)", "Mid (5-24)", "Low (0-4)"]:
        vals = by_cite[ct]
        f50 = sum(1 for x in vals if x < 5.0)
        f65 = sum(1 for x in vals if x < 6.5)
        print(f"  {ct:15s} (n={len(vals):2d}) | mean={statistics.mean(vals):.2f} (med={statistics.median(vals):.2f}) | <5.0: {f50:2d}/{len(vals)} ({f50/len(vals)*100:4.1f}%) | <6.5: {f65:2d}/{len(vals)} ({f65/len(vals)*100:4.1f}%)")

    with open(str(Path(__file__).resolve().parent.parent / "results_200.json", "w") as f:
        json.dump({"cohort_a": ca, "cohort_b": cb, "cohort_c": cc}, f, indent=2)

if __name__ == "__main__":
    main()
