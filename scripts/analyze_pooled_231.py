#!/usr/bin/env python3
"""
Pool all N = 231 Wild Papers across:
- Cohort C (101 wild papers: C01-C101)
- OOD Generalization (60 wild papers: D01-D20, E01-E20, F01-F20)
- Secular Trend (70 wild papers across 1991-2025: SEC_01-SEC_70)
Classify Study Modality, Technology Maturity, Epistemic Stage, Author Count,
Megajournal status, and Annual Field Volume across all 231 papers, and run
stratified + multivariable OLS regression analyses.
"""
import json
import math
import re
from pathlib import Path
import numpy as np
from scipy import stats

base_dir = Path("/Users/sergei/Projects/lit-estimation")
sec_dir = base_dir / "secular_trend_exp"

r200 = json.load(open(base_dir / "results_200.json"))
cohort_c = list(r200["cohort_c"])
ood_60 = json.load(open(base_dir / "ood_exp" / "ood_results_60.json"))
sec_70 = json.load(open(sec_dir / "secular_results_70.json"))
pub_vol = json.load(open(sec_dir / "pubmed_annual_volume.json"))

PURE_MEGA = {
    "plos one", "scientific reports", "sci rep", "frontiers", "front ",
    "international journal of molecular sciences", "int j mol sci", "animals",
    "viruses", "genes", "cells", "cancers", "microorganisms", "plants",
    "peerj", "heliyon", "medicine (baltimore)", "bmc ", "aging (albany",
    "world j ", "j clin med", "diagnostics", "biomolecules", "life (basel)",
    "antibiotics", "pathogens", "vaccines", "toxins", "metabolites"
}

def is_megajournal(j_name: str) -> bool:
    jl = (j_name or "").lower()
    return any(k in jl for k in PURE_MEGA)

def classify_paper_covariates(title: str, domain: str, journal: str, raw_text: str) -> dict:
    t_low = (title + " " + raw_text).lower()
    title_l = title.lower()

    # 1. Study Modality
    wet_hits = sum(1 for w in [
        "western blot", "transfect", "mice", "mouse", "flow cytometry",
        "immunohistochemistry", "rt-qpcr", "qpcr", "cell line", "cultured",
        "incubated", "elisa", "stained", "microscopy", "biops", "sera", "serum",
        "plasmid", "cloned", "mutagenesis", "crystallograph",
        "cryo-em", "electrophoresis", "extracted dna", "extracted rna",
        "fmri", "eeg", "patch-clamp", "optogenetic",
        "field survey", "transect", "collected from", "centrifuged", "pcr amplification"
    ] if w in t_low)
    sec_db_hits = sum(1 for w in [
        "tcga", "geo database", "gene expression omnibus", "uk biobank", "nhanes",
        "global burden of disease", "gisaid", "genbank", "downloaded from",
        "publicly available dataset", "mendelian randomization", "gwas summary", "finngen",
        "cbioportal", "gtex", "human connectome project", "abcd study",
        "gbif", "worldclim", "molecular docking", "network pharmacology", "autodock"
    ] if w in t_low)
    has_theory_sim = any(w in title_l for w in [
        "simulation", "algorithm", "estimator", "statistical method", "benchmark",
        "mathematical model", "likelihood", "bayesian method", "software", "package",
        "framework for", "deep learning model", "neural network for", "graph neural",
        "paper2agent", "alphafold", "language model"
    ]) or any(w in t_low[:4000] for w in [
        "we propose a novel", "we develop a method", "simulated datasets", "monte carlo simulation",
        "benchmark dataset"
    ])

    if sec_db_hits >= 1 and wet_hits <= 1 and not has_theory_sim:
        modality = "Dry-Lab Secondary Cohort/Database Re-Analysis"
    elif has_theory_sim and wet_hits <= 1:
        modality = "Dry-Lab Theory/Methods/Simulation"
    elif wet_hits >= 2 and (sec_db_hits >= 1 or "rna-seq" in t_low or "scrna-seq" in t_low or "docking" in t_low):
        modality = "Hybrid Computational + Wet-Lab Functional Validation"
    elif wet_hits >= 2:
        modality = "Wet-Lab Primary Experimental"
    else:
        modality = "Dry-Lab Secondary Cohort/Database Re-Analysis"

    # 2. Technology Maturity
    is_commodity = any(w in t_low for w in [
        "mendelian randomization", "two-sample mr", "network pharmacology",
        "lasso", "cibersort", "ssgsea", "wgcna", "nomogram", "molecular docking",
        "autodock", "vina", "gromacs", "mmpbsa", "mm-pbsa", "kegg", "go enrichment",
        "cytohubba", "string database", "ppi network", "hub gene", "maxent",
        "biomarker signature", "prognostic signature", "risk score ="
    ])
    is_mid_ht = any(w in t_low for w in [
        "rna-seq", "scrna-seq", "single-cell", "microarray", "illumina", "whole-genome",
        "metagenom", "16s rrna", "proteom", "mass spectrometry", "gwas", "fmri",
        "resting-state", "tractography", "alphafold", "cryo-em", "chip-seq", "atac-seq"
    ])
    if is_commodity:
        tech = "Commodity/Hype-Cycle Template"
    elif is_mid_ht:
        tech = "Mid-Stage High-Throughput"
    else:
        tech = "Mature/Classical"

    # 3. Epistemic Stage
    is_clinical = any(w in t_low[:4000] for w in [
        "patients with", "clinical outcome", "overall survival", "case-control",
        "cohort study", "retrospective study", "epidemiolog", "prevalence",
        "mortality", "hospitalized", "outbreak", "surveillance", "clinical trial"
    ])
    is_translational = any(w in t_low[:4000] for w in [
        "biomarker", "prognostic", "diagnostic", "therapeutic target", "drug discovery",
        "inhibitor", "virtual screening", "vaccine", "neutralizing", "preclinical",
        "xenograft", "ic50"
    ])
    if is_clinical and not is_translational:
        stage = "Clinical/Epidemiological Observational"
    elif is_translational:
        stage = "Translational/Preclinical/Biomarker"
    else:
        stage = "Basic/Mechanistic Discovery"

    return {
        "study_modality": modality,
        "tech_maturity": tech,
        "epistemic_stage": stage,
    }

pooled = []

for x in cohort_c:
    anon_path = base_dir / "papers_anon" / f"{x['anon_id']}.md"
    raw_txt = anon_path.read_text(encoding="utf-8") if anon_path.exists() else ""
    cov = classify_paper_covariates(x["title"], x["domain"], x["journal"], raw_txt)
    a_str = x.get("authors", "")
    a_cnt = len([a for a in a_str.split(",") if a.strip()]) if a_str else 1
    yr = int(x["year"])
    v_info = pub_vol.get(str(min(max(yr, 1991), 2025)), pub_vol["2025"])
    sci_core = round(x["rigor"] + x["claims"] + x["biology"], 2)
    pooled.append({
        "dataset": "Cohort C (Core Wild, 2024–2026)",
        "id": x["cohort_id"],
        "pmcid": x["pmcid"],
        "title": x["title"],
        "journal": x["journal"],
        "year": yr,
        "domain": x["domain"],
        "author_count": a_cnt,
        "is_megajournal": is_megajournal(x["journal"]),
        "log10_core_vol": round(math.log10(max(v_info["core_domain_volume"], 1)), 4),
        "overall": x["overall"],
        "rigor": x["rigor"],
        "claims": x["claims"],
        "biology": x["biology"],
        "reproducibility": x["reproducibility"],
        "sci_core_8": sci_core,
        **cov,
    })

for x in ood_60:
    anon_path = base_dir / "ood_exp" / "anon_papers" / f"{x['anon_id']}.md"
    raw_txt = anon_path.read_text(encoding="utf-8") if anon_path.exists() else ""
    cov = classify_paper_covariates(x["title"], x["domain"], x["journal"], raw_txt)
    a_str = x.get("authors", "")
    a_cnt = len([a for a in a_str.split(",") if a.strip()]) if a_str else 1
    yr = int(x["year"])
    v_info = pub_vol.get(str(min(max(yr, 1991), 2025)), pub_vol["2025"])
    sci_core = round(x["rigor"] + x["claims"] + x["biology"], 2)
    pooled.append({
        "dataset": "OOD Wild (Ecology/Neuro/DrugAI, 2024–2026)",
        "id": x["cohort_id"],
        "pmcid": x["pmcid"],
        "title": x["title"],
        "journal": x["journal"],
        "year": yr,
        "domain": x["domain"],
        "author_count": a_cnt,
        "is_megajournal": is_megajournal(x["journal"]),
        "log10_core_vol": round(math.log10(max(v_info["core_domain_volume"], 1)), 4),
        "overall": x["overall"],
        "rigor": x["rigor"],
        "claims": x["claims"],
        "biology": x["biology"],
        "reproducibility": x["reproducibility"],
        "sci_core_8": sci_core,
        **cov,
    })

for x in sec_70:
    pooled.append({
        "dataset": f"Secular Wild ({x['window_label']})",
        "id": x["sec_id"],
        "pmcid": x["pmcid"],
        "title": x["title"],
        "journal": x["journal"],
        "year": int(x["year"]),
        "domain": x["track"],
        "author_count": x["author_count"],
        "is_megajournal": x["is_megajournal"],
        "log10_core_vol": x["log10_core_vol"],
        "overall": x["overall"],
        "rigor": x["rigor"],
        "claims": x["claims"],
        "biology": x["biology"],
        "reproducibility": x["reproducibility"],
        "sci_core_8": x["sci_core_8"],
        "study_modality": x["study_modality"],
        "tech_maturity": x["tech_maturity"],
        "epistemic_stage": x["epistemic_stage"],
    })

print(f"Total Pooled Wild Manuscripts: N = {len(pooled)}")
with open(sec_dir / "pooled_wild_230.json", "w") as f:
    json.dump(pooled, f, indent=2)

for field_key, title in [
    ("study_modality", "POOLED N=230: Study Modality (Physical/Functional Outcome vs. Dry-Lab Cohort/Database)"),
    ("tech_maturity", "POOLED N=230: Technology Maturity"),
    ("epistemic_stage", "POOLED N=230: Epistemic Stage (Discovery vs. Translational vs. Clinical)"),
]:
    print(f"\n=== {title} ===")
    groups = {}
    for x in pooled:
        groups.setdefault(x[field_key], []).append(x)
    for k, sub in sorted(groups.items(), key=lambda kv: -np.mean([z["overall"] for z in kv[1]])):
        sc = [z["overall"] for z in sub]
        c8 = [z["sci_core_8"] for z in sub]
        f5 = sum(1 for s in sc if s < 5.0) * 100.0 / len(sc)
        f6 = sum(1 for s in sc if s < 6.0) * 100.0 / len(sc)
        print(
            f"  {k:55s} (n={len(sub):3d}): "
            f"Comp={np.mean(sc):.2f}±{np.std(sc,ddof=1):.2f} (Med={np.median(sc):.2f}) | "
            f"SciCore(/8)={np.mean(c8):.2f} (Scaled10={np.mean(c8)*10/8:.2f}) | <5.0={f5:4.1f}% | <6.0={f6:4.1f}%"
        )

print("\n=== POOLED N=230: VENUE TYPE (Legacy/Society/Selective vs. Open-Access Megajournal) ===")
for flag, label in [(False, "Legacy / Society / Selective Disciplinary Journals"), (True, "Open-Access Megajournals / APC Volume Venues")]:
    sub = [x for x in pooled if x["is_megajournal"] == flag]
    sc = [x["overall"] for z in [sub] for x in z]
    c8 = [x["sci_core_8"] for x in sub]
    f5 = sum(1 for s in sc if s < 5.0) * 100.0 / len(sc)
    f6 = sum(1 for s in sc if s < 6.0) * 100.0 / len(sc)
    print(
        f"  {label:55s} (n={len(sub):3d}): "
        f"Comp={np.mean(sc):.2f}±{np.std(sc,ddof=1):.2f} (Med={np.median(sc):.2f}) | "
        f"SciCore(/8)={np.mean(c8):.2f} | <5.0={f5:4.1f}% | <6.0={f6:4.1f}%"
    )

# Within Legacy/Society/Selective Journals ONLY across decades in N=70 Secular Cohort:
print("\n=== WITHIN NON-MEGAJOURNALS ONLY IN N=70 SECULAR COHORT (Testing Pure Within-Venue-Class Drift) ===")
for dec in ["1990s (1991–1999)", "2000s (2000–2009)", "2010s (2010–2019)", "2020s (2020–2025)"]:
    sub = [x for x in sec_70 if x["decade"] == dec and not x["is_megajournal"]]
    sc = [x["overall"] for x in sub]
    c8 = [x["sci_core_8"] for x in sub]
    f5 = sum(1 for s in sc if s < 5.0) * 100.0 / len(sc)
    print(f"  {dec:20s} (n={len(sub):2d} non-mega): Comp={np.mean(sc):.2f}±{np.std(sc,ddof=1):.2f} (Med={np.median(sc):.2f}) | SciCore(/8)={np.mean(c8):.2f} | <5.0={f5:4.1f}%")
    sub_m = [x for x in sec_70 if x["decade"] == dec and x["is_megajournal"]]
    if sub_m:
        scm = [x["overall"] for x in sub_m]
        c8m = [x["sci_core_8"] for x in sub_m]
        f5m = sum(1 for s in scm if s < 5.0) * 100.0 / len(scm)
        print(f"  {dec:20s} (n={len(sub_m):2d} megajour): Comp={np.mean(scm):.2f}±{np.std(scm,ddof=1):.2f} (Med={np.median(scm):.2f}) | SciCore(/8)={np.mean(c8m):.2f} | <5.0={f5m:4.1f}%")

# Multivariable OLS Regression on N=230 Pooled Wild Papers
# Predictors:
# 1. Year (decades since 1990: (year - 1990)/10.0)
# 2. log2(author_count)
# 3. is_megajournal (0/1)
# 4. Modality: Dry-Lab Secondary Cohort/Database Re-Analysis (0/1)
# 5. Tech Maturity: Commodity/Hype-Cycle Template (0/1)
# 6. Epistemic Stage: Translational or Clinical vs. Basic Discovery (0/1)
Y = np.array([x["overall"] for x in pooled], dtype=float)
X_cols = [
    ("Intercept", np.ones(len(pooled))),
    ("Decade ((Year-1990)/10)", np.array([(x["year"] - 1990.0) / 10.0 for x in pooled])),
    ("log2(Author Count)", np.array([math.log2(max(x["author_count"], 1)) for x in pooled])),
    ("Megajournal / APC Venue", np.array([1.0 if x["is_megajournal"] else 0.0 for x in pooled])),
    ("Secondary Cohort/DB Only (No Physical Outcome)", np.array([1.0 if x["study_modality"] == "Dry-Lab Secondary Cohort/Database Re-Analysis" else 0.0 for x in pooled])),
    ("Commodity / Hype-Cycle Template Tech", np.array([1.0 if x["tech_maturity"] == "Commodity/Hype-Cycle Template" else 0.0 for x in pooled])),
    ("Translational / Clinical (vs. Basic Discovery)", np.array([0.0 if x["epistemic_stage"] == "Basic/Mechanistic Discovery" else 1.0 for x in pooled])),
]
X = np.column_stack([c[1] for c in X_cols])
beta, residuals, rank, s = np.linalg.lstsq(X, Y, rcond=None)
y_hat = X @ beta
resid = Y - y_hat
n, k = X.shape
sigma2 = np.sum(resid ** 2) / (n - k)
cov_beta = sigma2 * np.linalg.inv(X.T @ X)
se_beta = np.sqrt(np.diag(cov_beta))
t_stats = beta / se_beta
p_vals = [2 * (1 - stats.t.cdf(abs(t), df=n - k)) for t in t_stats]
r2 = 1.0 - np.sum(resid ** 2) / np.sum((Y - np.mean(Y)) ** 2)
adj_r2 = 1.0 - (1.0 - r2) * (n - 1) / (n - k)

print(f"\n=== MULTIVARIABLE OLS REGRESSION (N = {n} WILD PAPERS, R^2 = {r2:.3f}, Adj R^2 = {adj_r2:.3f}) ===")
for idx, (col_name, _) in enumerate(X_cols):
    print(f"  {col_name:48s}: beta = {beta[idx]:+6.3f} ± {se_beta[idx]:.3f} | t = {t_stats[idx]:+6.2f} | p = {p_vals[idx]:.4e}")
