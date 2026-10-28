#!/usr/bin/env python3
"""
Deterministic verification script for spond/gemini-reviews:
Recomputes all calibration sensitivity matrices (Pilot vs. Held-Out, B02/A26 label sensitivity,
Upstream/Internal definitions, Retraction-subset sensitivity, Cohort B control composition,
Europe PMC domain-volume reweighting), Repeatability (Pooled & Per-Cohort ICC(2,1), ICC(3,1),
ICC(2,3), sub-score ICCs, Fleiss' kappa, wave ANOVA), and Out-of-Domain (Stage-1 vs Stage-1+2,
D20 sensitivity, and Citations-per-Year / within-year correlations) directly from committed JSON files.
"""
import json
import math
import os
import statistics

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def mean_sd(xs):
    if not xs:
        return (0.0, 0.0)
    m = sum(xs) / len(xs)
    sd = math.sqrt(sum((x - m) ** 2 for x in xs) / (len(xs) - 1)) if len(xs) > 1 else 0.0
    return m, sd


def mann_whitney_auc(pos_scores, neg_scores):
    """P(score_B > score_A) + 0.5 * P(score_B == score_A)."""
    u = 0.0
    for b in pos_scores:
        for a in neg_scores:
            if b > a:
                u += 1.0
            elif b == a:
                u += 0.5
    return u / (len(pos_scores) * len(neg_scores))


def rogan_gladen(p_obs, se, sp):
    denom = se + sp - 1.0
    if denom <= 0:
        return 0.0
    val = (p_obs + sp - 1.0) / denom
    return max(0.0, min(1.0, val))


def compute_icc_matrix(mat):
    """
    mat: list of N rows, each row is list of K rater/run scores.
    Returns dict with ICC(2,1), ICC(3,1), ICC(2,K), ICC(3,K), SD_e, SD_w_oneway, F_wave, MS_B, MS_W, MS_J, MS_E.
    """
    n = len(mat)
    k = len(mat[0])
    grand = sum(sum(r) for r in mat) / (n * k)
    row_means = [sum(r) / k for r in mat]
    col_means = [sum(mat[i][j] for i in range(n)) / n for j in range(k)]

    ss_total = sum((mat[i][j] - grand) ** 2 for i in range(n) for j in range(k))
    ss_rows = k * sum((rm - grand) ** 2 for rm in row_means)
    ss_cols = n * sum((cm - grand) ** 2 for cm in col_means)
    ss_err = ss_total - ss_rows - ss_cols
    ss_within = ss_total - ss_rows

    ms_b = ss_rows / (n - 1)
    ms_j = ss_cols / (k - 1)
    ms_e = ss_err / ((n - 1) * (k - 1))
    ms_w = ss_within / (n * (k - 1))

    icc_2_1 = (ms_b - ms_e) / (ms_b + (k - 1) * ms_e + k * (ms_j - ms_e) / n)
    icc_3_1 = (ms_b - ms_e) / (ms_b + (k - 1) * ms_e)
    icc_2_k = (ms_b - ms_e) / (ms_b + (ms_j - ms_e) / n)
    icc_3_k = (ms_b - ms_e) / ms_b

    sd_e = math.sqrt(ms_e)
    sd_w_oneway = math.sqrt(ms_w)
    mean_per_paper_sd = sum(
        math.sqrt(sum((x - rm) ** 2 for x in r) / (k - 1)) for r, rm in zip(mat, row_means)
    ) / n
    f_wave = ms_j / ms_e if ms_e > 0 else 0.0

    return {
        "n": n,
        "k": k,
        "ICC2_1": icc_2_1,
        "ICC3_1": icc_3_1,
        "ICC2_k": icc_2_k,
        "ICC3_k": icc_3_k,
        "SD_e": sd_e,
        "SD_w_oneway": sd_w_oneway,
        "mean_per_paper_sd": mean_per_paper_sd,
        "MS_B": ms_b,
        "MS_J": ms_j,
        "MS_E": ms_e,
        "F_wave": f_wave,
    }


def fleiss_kappa(mat, cutoff):
    """mat: list of N rows, K runs. Binary classification: x < cutoff."""
    n = len(mat)
    k = len(mat[0])
    p_i_list = []
    pos_total = 0
    for r in mat:
        n1 = sum(1 for x in r if x < cutoff)
        n0 = k - n1
        pos_total += n1
        p_i = (n1 * (n1 - 1) + n0 * (n0 - 1)) / (k * (k - 1))
        p_i_list.append(p_i)
    p_bar = sum(p_i_list) / n
    p1 = pos_total / (n * k)
    p0 = 1.0 - p1
    p_e = p1 ** 2 + p0 ** 2
    kappa = (p_bar - p_e) / (1.0 - p_e) if (1.0 - p_e) > 0 else 1.0
    unanimous = sum(1 for r in mat if len({x < cutoff for x in r}) == 1)
    return {"kappa": kappa, "P_bar": p_bar, "unanimous": unanimous, "n": n, "unanimous_pct": 100.0 * unanimous / n}


def rank_data(xs):
    indexed = sorted(enumerate(xs), key=lambda t: t[1])
    ranks = [0.0] * len(xs)
    i = 0
    while i < len(indexed):
        j = i
        while j + 1 < len(indexed) and indexed[j + 1][1] == indexed[i][1]:
            j += 1
        avg_rank = (i + j + 2) / 2.0
        for m in range(i, j + 1):
            ranks[indexed[m][0]] = avg_rank
        i = j + 1
    return ranks


def pearson_r(xs, ys):
    mx = sum(xs) / len(xs)
    my = sum(ys) / len(ys)
    num = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    den = math.sqrt(sum((x - mx) ** 2 for x in xs) * sum((y - my) ** 2 for y in ys))
    return num / den if den > 0 else 0.0


def spearman_rho(xs, ys):
    return pearson_r(rank_data(xs), rank_data(ys))


def main():
    with open(os.path.join(ROOT, "calibration", "results_200.json")) as f:
        res200_dict = json.load(f)
    res200 = res200_dict["cohort_a"] + res200_dict["cohort_b"] + res200_dict["cohort_c"]
    with open(os.path.join(ROOT, "calibration", "cohorts_200.json")) as f:
        coh200 = json.load(f)
    with open(os.path.join(ROOT, "repeatability", "repeatability_results.json")) as f:
        rep_res = json.load(f)
    with open(os.path.join(ROOT, "ood", "ood_results_60.json")) as f:
        ood_res = json.load(f)

    by_cid = {r["cohort_id"]: r for r in res200}
    meta_a = {r["cohort_id"]: r for r in coh200["cohort_a"]}
    meta_b = {r["cohort_id"]: r for r in coh200["cohort_b"]}
    meta_c = {r["cohort_id"]: r for r in coh200["cohort_c"]}

    print("=================================================================")
    print("1. REPEATABILITY: POOLED & PER-COHORT ICC AND KAPPA (N=30 x K=3)")
    print("=================================================================")
    for label, filt in [("Pooled (N=30)", lambda r: True), ("Cohort A (n=10)", lambda r: r["cohort"] == "A"),
                        ("Cohort B (n=10)", lambda r: r["cohort"] == "B"), ("Cohort C (n=10)", lambda r: r["cohort"] == "C")]:
        sub = [r for r in rep_res if filt(r)]
        mat = [[r["run1"]["overall"], r["run2"]["overall"], r["run3"]["overall"]] for r in sub]
        icc = compute_icc_matrix(mat)
        k5 = fleiss_kappa(mat, 5.0)
        k6 = fleiss_kappa(mat, 6.0)
        print(f"{label:16s} | ICC(2,1)={icc['ICC2_1']:.4f} | ICC(3,1)={icc['ICC3_1']:.4f} | ICC(2,3)={icc['ICC2_k']:.4f} | "
              f"SD_e={icc['SD_e']:.3f} | SD_1way={icc['SD_w_oneway']:.3f} | MS_B={icc['MS_B']:.2f} | F_wave={icc['F_wave']:.2f} | "
              f"<5.0 Unan={k5['unanimous']}/{k5['n']} ({k5['unanimous_pct']:.1f}%, P_bar={k5['P_bar']:.3f}, kappa={k5['kappa']:.3f}) | "
              f"<6.0 Unan={k6['unanimous']}/{k6['n']} ({k6['unanimous_pct']:.1f}%, P_bar={k6['P_bar']:.3f}, kappa={k6['kappa']:.3f})")

    print("\nSub-score ICCs (Pooled N=30 & Cohort C n=10):")
    for subkey in ["overall", "rigor", "claims", "biology", "reproducibility"]:
        mat_all = [[r["run1"][subkey], r["run2"][subkey], r["run3"][subkey]] for r in rep_res]
        mat_c = [[r["run1"][subkey], r["run2"][subkey], r["run3"][subkey]] for r in rep_res if r["cohort"] == "C"]
        icc_all = compute_icc_matrix(mat_all)
        icc_c = compute_icc_matrix(mat_c)
        print(f"  {subkey:15s} | Pooled ICC(2,1)={icc_all['ICC2_1']:.4f} (ICC(2,3)={icc_all['ICC2_k']:.4f}, SD_e={icc_all['SD_e']:.3f}) | "
              f"Cohort C ICC(2,1)={icc_c['ICC2_1']:.4f} (ICC(2,3)={icc_c['ICC2_k']:.4f}, SD_e={icc_c['SD_e']:.3f})")

    print("\n=================================================================")
    print("2. CALIBRATION SENSITIVITY MATRIX (ISSUE #3)")
    print("=================================================================")
    a_all_ids = [f"A{i:02d}" for i in range(1, 51)]
    b_all_ids = [f"B{i:02d}" for i in range(1, 51)]
    c_all_ids = [f"C{i:02d}" for i in range(1, 101)]

    a_pilot_ids = [f"A{i:02d}" for i in range(1, 26)]
    b_pilot_ids = [f"B{i:02d}" for i in range(1, 26)]
    c_pilot_ids = [f"C{i:02d}" for i in range(1, 26)]

    a_exp_ids = [f"A{i:02d}" for i in range(26, 51)]
    b_exp_ids = [f"B{i:02d}" for i in range(26, 51)]
    c_exp_ids = [f"C{i:02d}" for i in range(26, 101)]

    fresh_a = [r["cohort_id"] for r in res200 if r["cohort"] == "A" and int(r["anon_id"].split("_")[1]) >= 76]
    fresh_b = [r["cohort_id"] for r in res200 if r["cohort"] == "B" and int(r["anon_id"].split("_")[1]) >= 76]
    fresh_c = [r["cohort_id"] for r in res200 if r["cohort"] == "C" and int(r["anon_id"].split("_")[1]) >= 76]

    scenarios = [
        ("Full 200-Paper Study (As Published: A01-A50 vs B01-B50)", a_all_ids, b_all_ids, c_all_ids),
        ("Original Pilot Labels (PMC8135569 as B02, Starr in B; N_A=49, N_B=51)", [x for x in a_all_ids if x != "A26"], b_all_ids + ["A26"], c_all_ids),
        ("Original Pilot Labels (PMC8135569 as B02, Starr excluded; N_A=49, N_B=50)", [x for x in a_all_ids if x != "A26"], [x for x in b_all_ids if x != "B02"] + ["A26"], c_all_ids),
        ("PMC8135569 Excluded Entirely (N_A=49, N_B=50)", [x for x in a_all_ids if x != "A26"], b_all_ids, c_all_ids),
        ("Phase-1 Pilot Only (ANON_01-75, Original Labels: N_A=25, N_B=25, N_C=25)", a_pilot_ids, [x for x in b_pilot_ids if x != "B02"] + ["A26"], c_pilot_ids),
        ("Held-Out Expansion by ID (A26-A50 vs B26-B50, C26-C100)", a_exp_ids, b_exp_ids, c_exp_ids),
        ("Strictly Held-Out Post-Pilot Wave (ANON_76-200: N_A=24, N_B=26, N_C=75)", fresh_a, fresh_b, fresh_c),
        ("Strict GIANT-Consortium Exclusion (Excl A11, A23, A24; N_A=47)", [x for x in a_all_ids if x not in {"A11", "A23", "A24"}], b_all_ids, c_all_ids),
        ("Pilot-5 Upstream/Congruence Exclusion (Excl A07,A11,A19,A24,A25; N_A=45)", [x for x in a_all_ids if x not in {"A07", "A11", "A19", "A24", "A25"}], b_all_ids, c_all_ids),
        ("Broad-6 Upstream/Congruence Exclusion (Excl A07,A11,A19,A23,A24,A25; N_A=44)", [x for x in a_all_ids if x not in {"A07", "A11", "A19", "A23", "A24", "A25"}], b_all_ids, c_all_ids),
        ("Excl 5 Peer-Review-Sweep Retractions (Excl A44-A47, A50; N_A=45)", [x for x in a_all_ids if x not in {"A44", "A45", "A46", "A47", "A50"}], b_all_ids, c_all_ids),
    ]

    for name, aids, bids, cids in scenarios:
        sa = [by_cid[x]["overall"] for x in aids]
        sb = [by_cid[x]["overall"] for x in bids]
        sc = [by_cid[x]["overall"] for x in cids]
        ma, sda = mean_sd(sa)
        mb, sdb = mean_sd(sb)
        mc, sdc = mean_sd(sc)
        auc = mann_whitney_auc(sb, sa)
        se50 = sum(1 for x in sa if x < 5.0) / len(sa)
        sp50 = sum(1 for x in sb if x >= 5.0) / len(sb)
        se60 = sum(1 for x in sa if x < 6.0) / len(sa)
        sp60 = sum(1 for x in sb if x >= 6.0) / len(sb)
        se65 = sum(1 for x in sa if x < 6.5) / len(sa)
        sp65 = sum(1 for x in sb if x >= 6.5) / len(sb)
        p50 = sum(1 for x in sc if x < 5.0) / len(sc)
        p60 = sum(1 for x in sc if x < 6.0) / len(sc)
        p65 = sum(1 for x in sc if x < 6.5) / len(sc)
        rg50 = rogan_gladen(p50, se50, sp50)
        rg60 = rogan_gladen(p60, se60, sp60)
        rg65 = rogan_gladen(p65, se65, sp65)
        print(f"* {name}:")
        print(f"    Mean A={ma:.2f}±{sda:.2f} (n={len(sa)}), Mean B={mb:.2f}±{sdb:.2f} (n={len(sb)}), Mean C={mc:.2f}±{sdc:.2f} (n={len(sc)}) | AUC={auc:.4f}")
        print(f"    <5.0: Se={100*se50:.1f}% ({sum(1 for x in sa if x<5.0)}/{len(sa)}), Sp={100*sp50:.1f}% ({sum(1 for x in sb if x>=5.0)}/{len(sb)}), C_obs={100*p50:.1f}%, RG={100*rg50:.1f}%")
        print(f"    <6.0: Se={100*se60:.1f}% ({sum(1 for x in sa if x<6.0)}/{len(sa)}), Sp={100*sp60:.1f}% ({sum(1 for x in sb if x>=6.0)}/{len(sb)}), C_obs={100*p60:.1f}%, RG={100*rg60:.1f}%")
        print(f"    <6.5: Se={100*se65:.1f}% ({sum(1 for x in sa if x<6.5)}/{len(sa)}), Sp={100*sp65:.1f}% ({sum(1 for x in sb if x>=6.5)}/{len(sb)}), C_obs={100*p65:.1f}%, RG={100*rg65:.1f}%")

    print("\n=================================================================")
    print("3. COHORT B CONTROL COMPOSITION SENSITIVITY (ISSUE #4)")
    print("=================================================================")
    refutation_b = {"B03", "B05", "B06", "B07", "B10", "B16", "B17", "B18", "B31", "B32", "B33", "B34", "B50"}
    pond_b = {"B01", "B03", "B08", "B12", "B19", "B20", "B21"}
    non_flagship_8 = [cid for cid in b_all_ids if meta_b[cid]["journal"] in {"Virus Evol", "mBio", "Bioinformatics", "Mol Syst Biol", "Microbiome", "BMC Biol", "RNA", "Genome Res"}]
    flagship_42 = [cid for cid in b_all_ids if cid not in non_flagship_8]
    specialist_b = [cid for cid in b_all_ids if meta_b[cid]["journal"] not in {"Nature", "Science", "Cell", "Nat Genet", "Nat Med", "Nat Microbiol", "Nat Commun", "Elife", "PLoS Biol", "PLoS Genet", "Genome Biol"}]
    strictly_non_ncs_b = [cid for cid in b_all_ids if meta_b[cid]["journal"] not in {"Nature", "Science", "Cell"} and not meta_b[cid]["journal"].startswith("Nat ")]
    ncs_b = [cid for cid in b_all_ids if cid not in strictly_non_ncs_b]

    b_subsets = [
        ("Full Cohort B (N=50)", b_all_ids),
        ("Excluding 13 Refutation/Forensic Controls (N=37 Primary Discovery/Methods)", [x for x in b_all_ids if x not in refutation_b]),
        ("13 Refutation/Forensic Controls Alone (N=13)", sorted(list(refutation_b))),
        ("Excluding 7 Pond-Affiliated Controls (N=43)", [x for x in b_all_ids if x not in pond_b]),
        ("Excluding BOTH Refutation AND Pond Controls (N=31 Independent Primary)", [x for x in b_all_ids if x not in (refutation_b | pond_b)]),
        ("High-Impact Flagship Subset of Cohort B (N=42, per Issue #4 definition)", flagship_42),
        ("Non-Flagship / Specialist Journal Subset of Cohort B (N=8, per Issue #4)", non_flagship_8),
        ("Nature / Science / Cell Portfolio Subset of Cohort B (N=31)", ncs_b),
        ("Non-Nature/Science/Cell (Society/Specialist/Open) Subset of Cohort B (N=19)", strictly_non_ncs_b),
        ("Specialist Domain Society Journals incl. MBE (N=11)", specialist_b),
    ]
    sa_full = [by_cid[x]["overall"] for x in a_all_ids]
    for bname, bids in b_subsets:
        sb = [by_cid[x]["overall"] for x in bids]
        mb, sdb = mean_sd(sb)
        medb = statistics.median(sb)
        auc = mann_whitney_auc(sb, sa_full)
        sp50 = sum(1 for x in sb if x >= 5.0) / len(sb)
        sp60 = sum(1 for x in sb if x >= 6.0) / len(sb)
        sp65 = sum(1 for x in sb if x >= 6.5) / len(sb)
        print(f"  {bname:78s} | n={len(sb):2d} | Mean={mb:.2f}±{sdb:.2f} | Med={medb:.2f} | "
              f"Sp(<5.0)={100*sp50:.1f}% | Sp(<6.0)={100*sp60:.1f}% | Sp(<6.5)={100*sp65:.1f}% | AUC={auc:.4f}")
    print("  Specialist Cohort B IDs & Journals:", [(cid, meta_b[cid]["journal"], by_cid[cid]["overall"]) for cid in specialist_b])

    print("\nCohort C Citation-per-Year & Subfield Volume Reweighting:")
    c_records = [by_cid[cid] for cid in c_all_ids]
    c_scores = [r["overall"] for r in c_records]
    c_cites = [meta_c[cid]["citedByCount"] for cid in c_all_ids]
    c_years = [meta_c[cid]["year"] for cid in c_all_ids]
    c_cpy = [meta_c[cid]["citedByCount"] / max(1, 2026 - meta_c[cid]["year"]) for cid in c_all_ids]
    print(f"  Cohort C Spearman(raw cites, score) = {spearman_rho(c_cites, c_scores):.4f}")
    print(f"  Cohort C Spearman(cites/year, score) = {spearman_rho(c_cpy, c_scores):.4f}")
    for yr in [2024, 2025]:
        idx = [i for i, y in enumerate(c_years) if y == yr]
        if len(idx) >= 5:
            print(f"  Cohort C Within-{yr} (n={len(idx)}): Spearman(cites, score) = {spearman_rho([c_cites[i] for i in idx], [c_scores[i] for i in idx]):.4f}, "
                  f"Mean score = {sum(c_scores[i] for i in idx)/len(idx):.2f}")

    epmc_weights = {
        "Transcriptomics & CompBio": 0.36,
        "Cancer & Microbiome": 0.28,
        "Statistical Genetics": 0.18,
        "Viral Evolution": 0.10,
        "Molecular Evolution": 0.08,
    }
    w_mean = 0.0
    w_p50 = 0.0
    w_p60 = 0.0
    w_p65 = 0.0
    for dom, w in epmc_weights.items():
        d_scores = [r["overall"] for r in c_records if r["domain"] == dom]
        w_mean += w * (sum(d_scores) / len(d_scores))
        w_p50 += w * (sum(1 for x in d_scores if x < 5.0) / len(d_scores))
        w_p60 += w * (sum(1 for x in d_scores if x < 6.0) / len(d_scores))
        w_p65 += w * (sum(1 for x in d_scores if x < 6.5) / len(d_scores))
    print(f"  Equal-Allocation Cohort C (20/domain): Mean={sum(c_scores)/100:.2f}, <5.0={sum(1 for x in c_scores if x<5.0)}%, "
          f"<6.0={sum(1 for x in c_scores if x<6.0)}%, <6.5={sum(1 for x in c_scores if x<6.5)}%")
    print(f"  Europe PMC Volume-Weighted Cohort C:   Mean={w_mean:.2f}, <5.0={100*w_p50:.1f}%, <6.0={100*w_p60:.1f}%, <6.5={100*w_p65:.1f}%")

    print("\n=================================================================")
    print("4. OUT-OF-DOMAIN (OOD) STAGE-1 vs STAGE-1+2 & CONFOUNDS (ISSUE #6)")
    print("=================================================================")
    for dom_label, filt in [
        ("All OOD Combined (N=60)", lambda r: True),
        ("Neuroscience & Neuroimaging (n=20)", lambda r: "Neuro" in r["domain"]),
        ("Ecology & Macroevolution (n=20, with D20)", lambda r: "Ecology" in r["domain"]),
        ("Ecology & Macroevolution (n=19, excl D20)", lambda r: "Ecology" in r["domain"] and r["cohort_id"] != "D20"),
        ("Structural Bioinfo & AI Drug Discovery (n=20)", lambda r: "Struct" in r["domain"]),
    ]:
        sub = [r for r in ood_res if filt(r)]
        s1 = [r["stage1"]["overall"] for r in sub]
        sf = [r["overall"] for r in sub]
        m1, sd1 = mean_sd(s1)
        mf, sdf = mean_sd(sf)
        print(f"* {dom_label}:")
        print(f"    Stage-1 Single-Pass: Mean={m1:.2f}±{sd1:.2f} (Med={statistics.median(s1):.2f}) | "
              f"<5.0: {sum(1 for x in s1 if x<5.0)}/{len(s1)} ({100*sum(1 for x in s1 if x<5.0)/len(s1):.1f}%) | "
              f"<6.0: {sum(1 for x in s1 if x<6.0)}/{len(s1)} ({100*sum(1 for x in s1 if x<6.0)/len(s1):.1f}%) | "
              f"<6.5: {sum(1 for x in s1 if x<6.5)}/{len(s1)} ({100*sum(1 for x in s1 if x<6.5)/len(s1):.1f}%)")
        print(f"    Stage-1+2 Consensus: Mean={mf:.2f}±{sdf:.2f} (Med={statistics.median(sf):.2f}) | "
              f"<5.0: {sum(1 for x in sf if x<5.0)}/{len(sf)} ({100*sum(1 for x in sf if x<5.0)/len(sf):.1f}%) | "
              f"<6.0: {sum(1 for x in sf if x<6.0)}/{len(sf)} ({100*sum(1 for x in sf if x<6.0)/len(sf):.1f}%) | "
              f"<6.5: {sum(1 for x in sf if x<6.5)}/{len(sf)} ({100*sum(1 for x in sf if x<6.5)/len(sf):.1f}%)")

    s2_papers = [r for r in ood_res if r.get("is_borderline")]
    s2_mat = [[r["stage1"]["overall"], r["stage2_run2"]["overall"], r["stage2_run3"]["overall"]] for r in s2_papers]
    s2_r23 = [[r["stage2_run2"]["overall"], r["stage2_run3"]["overall"]] for r in s2_papers]
    icc_s2_all = compute_icc_matrix(s2_mat)
    icc_s2_23 = compute_icc_matrix(s2_r23)
    diffs_2_1 = [r["stage2_run2"]["overall"] - r["stage1"]["overall"] for r in s2_papers]
    diffs_3_1 = [r["stage2_run3"]["overall"] - r["stage1"]["overall"] for r in s2_papers]
    diffs_3_2 = [r["stage2_run3"]["overall"] - r["stage2_run2"]["overall"] for r in s2_papers]
    print(f"\nStage-2 Borderline Re-Review Analysis (n={len(s2_papers)}, restricted range 5.2-6.8):")
    print(f"  Mean S1={sum(r['stage1']['overall'] for r in s2_papers)/14:.2f}, "
          f"Mean Run2={sum(r['stage2_run2']['overall'] for r in s2_papers)/14:.2f}, "
          f"Mean Run3={sum(r['stage2_run3']['overall'] for r in s2_papers)/14:.2f}")
    print(f"  Mean(Run2 - S1)={sum(diffs_2_1)/14:+.2f}, Mean(Run3 - S1)={sum(diffs_3_1)/14:+.2f}, Mean(Run3 - Run2)={sum(diffs_3_2)/14:+.2f}")
    print(f"  Within-borderline SD_e (3 runs)={icc_s2_all['SD_e']:.3f}, SD_e (Run2 vs Run3)={icc_s2_23['SD_e']:.3f}")

    ood_s1 = [r["stage1"]["overall"] for r in ood_res]
    ood_sf = [r["overall"] for r in ood_res]
    ood_cites = [r["citedByCount"] for r in ood_res]
    ood_years = [r["year"] for r in ood_res]
    ood_cpy = [r["citedByCount"] / max(1, 2026 - r["year"]) for r in ood_res]
    print(f"\nOOD Citation Correlations (N=60):")
    print(f"  Spearman(raw cites, Final Score) = {spearman_rho(ood_cites, ood_sf):.4f} (Stage-1: {spearman_rho(ood_cites, ood_s1):.4f})")
    print(f"  Spearman(cites/yr,  Final Score) = {spearman_rho(ood_cpy, ood_sf):.4f} (Stage-1: {spearman_rho(ood_cpy, ood_s1):.4f})")
    for yr in [2024, 2025]:
        idx = [i for i, y in enumerate(ood_years) if y == yr]
        print(f"  Within-{yr} (n={len(idx)}): Spearman(cites, Final) = {spearman_rho([ood_cites[i] for i in idx], [ood_sf[i] for i in idx]):.4f}, "
              f"Spearman(cites, Stage-1) = {spearman_rho([ood_cites[i] for i in idx], [ood_s1[i] for i in idx]):.4f}")

    for label, cond in [("High Velocity (>=10 cites/yr)", lambda cpy: cpy >= 10.0),
                        ("Mid Velocity (2.5-9.9 cites/yr)", lambda cpy: 2.5 <= cpy < 10.0),
                        ("Low Velocity (<2.5 cites/yr)", lambda cpy: cpy < 2.5)]:
        idx = [i for i, cpy in enumerate(ood_cpy) if cond(cpy)]
        s1_sub = [ood_s1[i] for i in idx]
        sf_sub = [ood_sf[i] for i in idx]
        print(f"  {label:32s} (n={len(idx):2d}): Stage-1 Mean={sum(s1_sub)/len(s1_sub):.2f} (<5.0: {100*sum(1 for x in s1_sub if x<5.0)/len(s1_sub):.1f}%, <6.0: {100*sum(1 for x in s1_sub if x<6.0)/len(s1_sub):.1f}%), "
              f"Final Mean={sum(sf_sub)/len(sf_sub):.2f} (<5.0: {100*sum(1 for x in sf_sub if x<5.0)/len(sf_sub):.1f}%, <6.0: {100*sum(1 for x in sf_sub if x<6.0)/len(sf_sub):.1f}%)")


if __name__ == "__main__":
    main()
