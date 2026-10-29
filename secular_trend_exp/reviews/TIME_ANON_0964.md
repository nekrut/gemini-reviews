<Blinded Review: TIME_ANON_0964>
**Composite Score:** 5.3 / 10.0 (Rigor: 1.7/3.5 | Claims: 1.3/2.5 | Biology: 1.2/2.0 | Reproducibility: 1.1/2.0)
**Bias Category:** Over-Interpretation/Clinical
**Verdict:** Major Revision
**Study Modality:** Hybrid Computational + Wet-Lab
**Technology Maturity:** Mature/Classical
**Epistemic Stage:** Translational/Preclinical/Biomarker

OVERALL_SCORE: 5.3/10
VERDICT: CAVEATS
ESTIMATED_DECADE: 2020s

---

### 1. Executive Summary / SUMMARY
This small cross-sectional clinical biomarker study evaluates `TNF-alpha` protein levels (ELISA in serum, 24-h unstimulated PBMC culture supernatants, and saliva), `TNF-alpha` mRNA expression (qRT-PCR in PBMCs normalized to `RPS18`), `TNF-alpha` promoter methylation (bisulfite pyrosequencing across 4 CpG sites in whole blood gDNA), and `miR-130a-3p` expression (qRT-PCR in serum and saliva normalized to `miR-16`, selected via `TargetScan`, `miRTargetLink 2.0`, and `miEAA 2`) in 14 patients with relapsing-remitting multiple sclerosis (`RRMS`, 7 males and 7 females in clinical remission, treatment-free for $\ge 3$ months) compared against 14 age- and sex-matched healthy controls (`HC`, 6 males and 8 females).

The authors report higher `TNF-alpha` protein in serum ($14.4 \pm 6.5$ vs. $5.8 \pm 3.2\text{ pg/mL}$, $p = 0.007$), PBMC supernatants, and saliva ($66.6 \pm 23.03\text{ pg/mL}$, $p = 0.002$), elevated PBMC `TNF-alpha` mRNA, lower `TNF-alpha` promoter methylation at CpGs 2–4 ($p = 0.001$), and lower `miR-130a-3p` in serum and saliva ($p < 0.001$) in RRMS patients relative to controls, proposing salivary `TNF-alpha` and `miR-130a-3p` as noninvasive biomarkers for MS diagnosis and monitoring.

While the study addresses a clinically convenient biofluid (saliva) and restricts enrollment to treatment-free remission patients, forensic audit reveals **internal contradictions in reported serum `TNF-alpha` values, mismatch between statistical distribution summaries (`median ± SD`), a PyroMark bisulfite sequence-to-analyze string containing un-converted cytosines outside CpG context, unvalidated endogenous normalization (`miR-16` in biofluids), and absence of any diagnostic performance metrics (`ROC/AUC`) or statistically significant correlation ($r = -0.13, p = 0.71$) to support the biomarker claims**.

### 2. Methodological & Statistical Audit / STRENGTHS & WEAKNESSES & METHODOLOGICAL AUDIT

#### Major Methodological & Statistical Flaws
1. **Internal Contradiction in Serum `TNF-alpha` Concentrations and Missing Control Saliva Values:**
   - In Results line 112, serum `TNF-alpha` in RRMS patients vs. HC is reported as **`14.4 ± 6.5 pg/mL vs. 5.8 ± 3.2 pg/mL`** ($p = 0.007$).
   - Yet in Results line 186, the authors write: *"Interestingly, TNFα levels detected in saliva were higher than those measured in serum (66.6 ± 23.03 pg/mL and 14.13 ± 7 pg/mL, respectively)..."* Here, the RRMS serum `TNF-alpha` level has inexplicably changed from `14.4 ± 6.5 pg/mL` to **`14.13 ± 7 pg/mL`**, and the healthy control salivary `TNF-alpha` concentration is never stated in the text at all!
   - Furthermore, note that the healthy control serum mean (`5.8 ± 3.2 pg/mL`) is **below the manufacturer's stated assay sensitivity limit of `7 pg/mL`** (Methods line 54: *"sensitivity of 7 pg/mL"*), meaning most healthy control serum readings were extrapolated below the lower limit of quantification (`LLOQ`).
2. **Inconsistent / Hybrid Summary Statistics (`Median ± SD` vs. `Mean ± SD` vs. `Median (IQR)`):**
   - Methods line 83 states that quantitative variables were summarized as **`median and interquartile range (IQR)`** and compared by the non-parametric `Mann-Whitney U test`.
   - Yet `Table 1` reports Age as `mean (DS)` (`45 ± 9`), while every single figure caption (`Figures 1, 2, 3, 5, 6`) states **`Data are reported as median ± standard deviation (SD)`**—a statistically improper hybrid pairing a non-parametric location estimator (`median`) with a parametric dispersion estimator (`SD`).
3. **Cellular Compartment Mismatch Between DNA Methylation (Whole Blood) and mRNA Expression (PBMCs) Without Cell-Type Deconvolution:**
   - `TNF-alpha` mRNA was measured in Ficoll-isolated **PBMCs** (lymphocytes + monocytes, lacking neutrophils/granulocytes), whereas genomic DNA for `TNF-alpha` promoter bisulfite pyrosequencing was extracted from **whole blood** (`Methods` line 66; `Results` line 140), where neutrophils constitute 50–70% of leukocytes. Because DNA methylation at cytokine promoters differs markedly between granulocytes and lymphoid/monocytic subsets, mild shifts in the neutrophil-to-lymphocyte ratio (`NLR`) in MS patients directly confound whole-blood CpG methylation percentages.
   - In addition, the reported PyroMark `Sequence to Analyze` in Methods line 66 (`CTCA/GATTTCTTCTCCATCA/GCA/GAAAACA/GAAAATTT`) represents a reverse-strand bisulfite sequence (`A/G` polymorphisms at CpG sites), but contains multiple non-CpG `C` nucleotides (`CTC...CTTCTCCATC...`) that would be converted to `T` (or `A` on the opposite strand) during bisulfite conversion unless the primer sequence and target strand are misannotated.
4. **Null Intra-Cohort Correlation ($r = -0.13, p = 0.71$) and Overstated Epigenetic/miRNA Causality:**
   - The authors claim that `miR-130a-3p` downregulation post-transcriptionally drives `TNF-alpha` upregulation in serum and saliva, yet their own Spearman correlation between `TNF-alpha` and `miR-130a-3p` in saliva is essentially zero ($r = -0.13, p = 0.71$, line 191), and no correlation coefficient or $p$-value is reported for serum `miR-130a-3p` vs. `TNF-alpha` or for `TNF-alpha` promoter methylation vs. mRNA (line 135 mentions a "negative association" without providing $r$ or $p$).
   - Normalizing biofluid (serum and saliva) extracellular miRNA qRT-PCR solely to `miR-16` (`Methods` line 73) without spike-in control (`cel-miR-39`) or hemolysis check is well known to be sensitive to red blood cell hemolysis in serum and epithelial cell shedding in saliva.
5. **Very Small Sample Size ($n = 14$ per group) and Lack of Disease-Control Specificity:**
   - With only 14 RRMS patients and 14 healthy controls (and no other neuroinflammatory or periodontal/oral inflammation controls), no ROC curves, sensitivity/specificity estimates, or external validation are provided.

#### Strengths
1. **Treatment-Free Remission Cohort Selection:** Enrolling RRMS patients free of immunomodulatory therapy and clinical relapses for $\ge 3$ months avoids acute steroid or interferon/natalizumab confounding.
2. **Candid Discussion of Limitations:** In the Discussion (lines 208, 222–226), the authors fairly acknowledge the small sample size ($n=14$), the null correlations ($r = -0.13, p = 0.71$), the potential influence of oral health on salivary cytokines, and the inability to establish direct causal regulation without functional perturbation.

### 3. Biological / Experimental Grounding & Claim Proportionality
- **Claim 1:** Treatment-free RRMS patients in remission exhibit elevated `TNF-alpha` levels in serum, PBMC supernatants, and saliva compared to healthy controls. `[Moderately Supported]` — Supported within this $n=14$ cohort, though HC serum values (`5.8 pg/mL`) fall below the ELISA sensitivity limit (`7 pg/mL`).
- **Claim 2:** `TNF-alpha` upregulation in RRMS is driven by coordinated `TNF-alpha` promoter hypomethylation and `miR-130a-3p` downregulation. `[Overstated]` — Purely observational group-difference associations in $n=14$ patients, with whole-blood vs. PBMC compartment mismatch for methylation and a non-significant correlation ($r = -0.13, p = 0.71$) between `miR-130a-3p` and `TNF-alpha`.
- **Claim 3:** Salivary `TNF-alpha` and `miR-130a-3p` represent minimally invasive biomarkers for MS early diagnosis and monitoring. `[Overstated]` — `TNF-alpha` is a non-specific general inflammatory cytokine elevated in gingivitis, periodontitis, and systemic infections; no neurological disease controls or ROC analyses were performed.

### 4. Reproducibility & Data Completeness
- **Data Completeness:** Primer sequences for `TNF-alpha` and `RPS18` mRNA and `TNF-alpha` pyrosequencing are provided, though LNA primer catalog numbers/sequences for `miR-130a-3p` and `miR-16` are omitted, and numerical values (medians, IQRs, exact $p$-values, and correlation coefficients) for Figures 2, 3, 5, and 6 are omitted from the text.
</Blinded Review: TIME_ANON_0964>
