# Blinded Review: SP_ANON_134

**Composite Score:** 5.2 / 10.0 (Rigor: 1.5/3.5 | Claims: 1.1/2.5 | Biology: 1.3/2.0 | Reproducibility: 1.3/2.0)
**Bias Category:** Unadjusted Bivariate Sparse-Cell Association Misreported as Independent & Uncorrected Multiple Testing
**Verdict:** Major Revision
**Study Modality:** Wet-Lab Primary Experimental
**Technology Maturity:** Mature/Classical
**Epistemic Stage:** Clinical/Epidemiological Observational

---

## 1. Executive Summary

This cross-sectional observational study evaluates associations between self-reported recreational substance use and transmitted HIV-1 drug resistance (TDR) among 115 newly diagnosed, antiretroviral-naive individuals (out of 168 enrolled) in San Diego between 2004 and 2006, supplemented by *pol* synonymous-distance phylogenetic clustering and `HyPhy` $F_{\text{ST}}$ genetic subdivision tests. The authors report that active methamphetamine use in the prior 30 days is associated with NNRTI TDR (`OR = 6.6`, 95% CI `1.94–22.21`, $p = 0.002$), whereas phylogenetic $F_{\text{ST}}$ and clustering analyses show no genetic segregation by methamphetamine use or TDR status. While the molecular phylogenetic analyses are competently executed and candidly reported as null, the primary epidemiological headline—claiming in the Abstract that methamphetamine use is **"independently associated"** with NNRTI TDR and suggesting in the Discussion that clinicians consider protease-inhibitor regimens instead of NNRTIs for methamphetamine users—is undermined by the complete absence of multivariable regression adjustment, uncorrected multiple hypothesis testing across decenas of drug/window/outcome combinations, and small-sample sparse-cell instability ($n = 13$ NNRTI TDR events total).

---

## 2. Methodological & Statistical Audit

* **False Claim of an "Independent" Association Without Multivariable Adjustment (Abstract line 12 vs. Methods line 31 & Results line 42):**
  * In the Abstract (line 12), the authors state: *"Recent active methamphetamine use was **independently associated** with TDR to NNRTI (OR: 6.6; p=0.002)."*
  * Yet in the Methods (line 31), the text explicitly states: *"Looking at the association between TDR and individual recreational substance use, multivariate analyses were not performed given that none of the demographic, behavioral and base-line clinical conditions was significantly associated with TDR."* And in Results (line 42): *"Again, because we did not detect any significant differences in any of the potentially confounding demographic categories for any of the categories of TDR, we did not adjust for these variables."*
  In biostatistics, reporting a bivariate unadjusted $2 \times 2$ contingency table odds ratio as "independently associated" is a textbook reporting error. Moreover, using $p > 0.05$ bivariate screening in a small sample ($N = 115$) to justify omitting potential confounders (such as partner count, income, sex-with-IDU, EDI duration, or calendar month/sub-network) fails to control for confounding, as variables that do not reach $p < 0.05$ individually in $N = 115$ can still substantially shift an exposure odds ratio when adjusted jointly.
* **Multiple Testing Across Exposure Windows, Substances, and Resistance Classes without Correction:** The study screened 7 substance categories (alcohol, marijuana, methamphetamine, cocaine, GHB, poppers, any club drug, plus polydrug combinations) $\times$ 2 exposure windows ("ever" vs. "last 30 days") $\times$ 4 resistance outcomes (overall TDR, NNRTI, NRTI, PI). Across $>50$ implicit bivariate comparisons, no Bonferroni or Benjamini-Hochberg false discovery rate correction was applied. Notably, "ever" using methamphetamine showed a weaker association with NNRTI TDR (`OR = 3.94`, $p = 0.04$), and active methamphetamine use showed zero association with NRTI or PI resistance.
* **Sparse-Cell Small-Sample Bias ($n = 13$ NNRTI Events):** Among the 115 genotyped subjects, only **13 individuals** had NNRTI TDR, and only **21 individuals** reported active methamphetamine use in the prior 30 days (yielding approximately 7 exposed cases in the $2 \times 2$ cell, as reflected in the wide 95% confidence interval `1.94–22.21`). Ordinary maximum-likelihood odds ratios in sparse $2 \times 2$ tables overestimate effect sizes; exact conditional logistic regression or Firth's penalized likelihood should be used.
* **Soundness of Synonymous Distance and $F_{\text{ST}}$ Analyses:** The evolutionary methods (`HyPhy` recombination screening, synonymous codon distances avoiding DRM convergent bias, and 1,000-permutation $F_{\text{ST}}$ tests via Hudson, Slatkin, and $K_{\text{ST}}$ estimators) are rigorous and appropriately demonstrate no sub-epidemic genetic subdivision between methamphetamine users and non-users ($p > 0.15$).

---

## 3. Biological / Experimental Grounding & Claim Proportionality

* **`[Well Supported]` Absence of Phylogenetic Segregation Between Methamphetamine Users and Non-Users in the San Diego MSM Sub-Epidemic:** The $F_{\text{ST}}$ and synonymous-distance clustering results convincingly show that HIV-1 lineages circulating among methamphetamine users are genetically well mixed with the broader local MSM epidemic.
* **`[Methodologically Flawed]` Claim that Active Methamphetamine Use is "Independently Associated" with NNRTI TDR:** Because no multivariable model was fitted and no multiple-testing correction was applied across dozens of bivariate screens on 13 NNRTI events, describing this association as "independent" is methodologically flawed.
* **`[Overstated]` Clinical Recommendation to Empirically Switch Methamphetamine Users from NNRTI to PI Regimens (Discussion line 98):** Suggesting empirical regimen changes ("perhaps PI-based regimens instead of NNRTI should be used to treat HIV infection among individuals who continue to use methamphetamine") based on 13 unadjusted cross-sectional cases—especially when baseline resistance genotyping is already standard of care—is clinically disproportionate.

---

## 4. Reproducibility & Data Completeness

* **Data Completeness:** Summary demographic and drug-use percentages are listed in Table 1, and phylogenetic/statistical tools (`HyPhy`, `SAS v9.1`) are cited, but neither the raw $2 \times 2$ contingency cell counts for each substance/TDR class nor GenBank accession numbers for the 115 *pol* sequences are provided in the manuscript.
