# Review of ANON_144

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **6.6 / 10.0** (Mixed / Salvageable)  
* **Score Breakdown:** Rigor: 2.1/3.5 | Claims: 1.6/2.5 | Biology: 1.4/2.0 | Reproducibility: 1.5/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This study evaluates whether integrating polygenic risk scores for quantitative risk factors (RFPRSs) with disease-specific polygenic risk scores (disease PRSs) improves genetic risk prediction across hundreds of ICD-10 phenotypes in the UK Biobank (UKB). The authors partition $n = 348,977$ unrelated White British UKB participants into a discovery GWAS subset ($n = 174,488$) and a PRS training/selection subset ($n = 174,489$), supplemented by a held-out European-ancestry validation subset ($n = 56,192$). Using PLINK v2.00 and LDpred2-infinitesimal across ~1.14 million HapMap3 SNPs, they construct 112 quantitative RFPRSs ($h_g^2 > 10\%$) and test $112 \times 700 = 78,400$ logistic regression associations in the PRS set, identifying 6,157 Bonferroni-significant associations ($p < 6.38 \times 10^{-7}$) spanning 109 RFPRSs and 247 diseases. For 70 heritable diseases that remain significant in validation, they use 10-fold cross-validated elastic net regression (`glmnet`) in the PRS set to combine each disease PRS with its associated RFPRSs into a composite `RFDiseasemetaPRS`. In the validation set, `RFDiseasemetaPRS` achieves a statistically significant increase in $R^2$ (via `r2redux`, $p < 1.16 \times 10^{-3}$) alongside positive continuous Net Reclassification Improvement (NRI) in 31 of 70 diseases, increasing the mean top-10% vs. bottom-90% odds ratio from 1.56 to 1.76. Summary statistics (GWAS Catalog GCST90309819–GCST90309930; Zenodo) and PRS SNP weights (PGS Catalog PGP000561) are publicly deposited.

The three-way sample split ($174\text{k}$ GWAS / $174\text{k}$ PRS elastic-net training / $56\text{k}$ validation) and the use of `r2redux` to formally test correlated $R^2$ differences represent a solid large-scale biobank framework. However, several methodological and statistical issues limit the strength of the conclusions: (1) all PRSs are restricted to the `LDpred2-inf` (infinitesimal) model rather than grid/auto sparse Bayesian models (`LDpred2-grid`/`LDpred2-auto` or `PRS-CS`), which artificially depresses baseline single-disease PRS accuracy for oligogenic/moderately polygenic traits; (2) the validation cohort ($n = 56,192$) consists of the non-White-British/related residual European samples excluded from the $348,977$ unrelated White British QC set, meaning cryptic relatedness with the discovery/training sets was not purged across the split boundary; (3) the continuous NRI metric (`PredictABEL`) is known to be poorly calibrated and sensitive to arbitrary scaling when applied to uncalibrated logistic scores; and (4) the "relative contribution" metric in Equation 8 sums raw signed (or absolute) elastic net weights across up to 32 highly collinear bioimpedance/anthropometric traits without accounting for predictor covariance. These issues can be resolved through targeted sensitivity analyses and textual refinements.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Across 112 heritable quantitative traits and 700 diseases in the UK Biobank, 6,157 trait-PRS-to-disease associations reach Bonferroni significance ($p < 6.38 \times 10^{-7}$), heavily concentrated in musculoskeletal and cardiometabolic disorders: [Well Supported].**  
  The discovery GWAS ($n = 174,488$) and the PRS-disease association scan ($n = 174,489$) are performed in non-overlapping subsets of unrelated White British individuals, controlling for age, sex, genotyping array, and PC1–PC10. Note, however, that 32 of the 112 risk factors are redundant bioimpedance measures (e.g., whole-body, left/right arm, left/right leg, and trunk fat mass, fat-free mass, and predicted mass in Table 1), which inflates the raw count of associations in the musculoskeletal and cardiometabolic categories.

* **Integrating RFPRSs with disease PRS via elastic net (`RFDiseasemetaPRS`) significantly improves $R^2$ (`r2redux`) and risk reclassification in 31 of 70 heritable diseases: [Moderately Supported].**  
  While the `r2redux` variance-adjusted $R^2$ comparison on the held-out set ($n = 56,192$) is appropriate for comparing correlated scores, the average $R^2$ gain across the 31 significant diseases is modest ($+0.21\%$ on average, ranging from $+0.06\%$ to $+0.59\%$). Furthermore, because the authors used `LDpred2-inf` (which assumes 100% of variants are causal with uniform prior variance) and restricted disease GWAS to $n = 174,488$ with standard PLINK logistic regression (rather than Firth/SAIGE saddlepoint approximation for low-prevalence ICD-10 codes down to $0.1\%$), part of the gain from continuous RFPRSs reflects noisy baseline disease PRS estimation rather than novel pathway capture.

* **The ratio of summed RFPRS elastic-net weights to the disease PRS weight (Equation 8) quantifies the relative biological contribution of risk factor pathways vs. direct disease genetics (e.g., a 4.62-fold effect in chronic renal failure): [Methodologically Flawed].**  
  In the Discussion (line 136) and Methods (Equation 8), the authors compute $\text{Ratio} = |\sum_{i=1}^n \gamma_i| / \gamma_{\text{disease PRS}}$. When dozens of positively correlated RFPRSs (e.g., 32 body-impedance traits and 6 body-size traits) are entered into an elastic net model, the L2 penalty distributes weight across all collinear predictors, and the L1/L2 shrinkage of the single noisy binary disease PRS relative to 20–80 high-powered quantitative trait PRSs depends on the number of included redundant traits and their sign orientation. Summing $\gamma_i$ without accounting for the covariance matrix $\Sigma_{\text{RFPRS}}$ or variable sign polarity does not measure relative variance explained.

* **Early-onset cardiovascular disease ($\le 55$ years) shows a 1.13-fold higher hazard ratio with `RFDiseasemetaPRS` than with `disease PRS` in Cox regression: [Fragile].**  
  In the Methods ("Statistics and reproducibility", line 65), the authors state that for the early-onset Cox models, `"the cases with late onset were excluded and the control cases were censored at the upper limit of the early onset age"`. Dropping individuals who develop disease after age 55 from the risk set at ages $\le 55$ (rather than treating them as event-free up to age 55 and censoring them at age 55) conditions on future outcomes and distorts the baseline hazard and hazard ratio estimates.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Verify Genetic Unrelatedness Between the Validation Set ($n = 56,192$) and the Discovery/Training Sets ($n = 348,977$)
* **WHY:** In the Results (line 86) and Methods (line 161), the validation set ($n = 56,192$) is extracted from the remaining UKB European-ancestry samples after excluding the $348,977$ unrelated White British individuals. In the UK Biobank, the standard unrelated White British subset was created by dropping one member of each related pair (kinship $> 0.0442$) plus non-White-British Europeans; therefore, the excluded pool of $487,409 - 348,977 = 138,432$ individuals contains thousands of first-, second-, and third-degree relatives of the $348,977$ discovery/training individuals. Any close relatives shared between the training/GWAS sets and the validation set will inflate validation $R^2$ and ORs.
* **WHAT:** Filter the $n = 56,192$ validation set using the UKB kinship table to remove any individual with 3rd-degree or closer relatedness ($\phi > 0.0442$) to any participant in the $n = 348,977$ GWAS + PRS sets.
* **HOW:** Cross-reference the sample IDs in the $n = 56,192$ validation set against UKB Field 22021 / the UKB kinship file (`ukb_rel.dat`), exclude all validation individuals linked to a GWAS or PRS set participant with kinship $> 0.0442$, and recompute Supplementary Tables 6–12 on the strictly unrelated validation subset.

#### 2. Replace the Collinear Weight-Sum Ratio (Equation 8) with Variance-Partitioned Semi-Partial $R^2$
* **WHY:** Equation 8 ($\sum \gamma_i / \gamma_{\text{disease PRS}}$) is confounded by predictor multiplicity (e.g., 32 collinear bioimpedance traits) and sign cancellations (where protective RFPRSs such as HDL-C or heel BMD have negative $\gamma_i$ that cancel positive $\gamma_i$ from BMI or triglycerides before taking the absolute value).
* **WHAT:** Quantify the relative contribution of RFPRSs versus the disease PRS using the ratio of semi-partial $R^2$ (or the variance of the linear predictor $\text{Var}(\sum_{i=1}^n \gamma_i \text{RFPRS}_i) / \text{Var}(\gamma_{\text{disease}} \text{PRS}_{\text{disease}})$) calculated directly on the validation cohort.
* **HOW:** For each of the 31 diseases in Supplementary Table 13, compute the empirical standard deviation of the composite RFPRS component $S_{\text{RF}} = \text{SD}(\sum_{k=1}^c \gamma_k \text{RFPRS}_k)$ and the disease PRS component $S_D = \text{SD}(\gamma_D \text{PRS}_D)$ in the validation set, and replace the raw weight-sum ratio with $S_{\text{RF}} / S_D$ (or variance ratio $S_{\text{RF}}^2 / S_D^2$) in Supplementary Table 13 and Supplementary Fig. 31.

#### 3. Fix the Right-Censoring Rule in Early-Onset Cardiovascular Cox Models
* **WHY:** Excluding late-onset cases (onset age $> 55$) entirely from the early-onset ($\le 55$) Cox regression (line 65) introduces lookahead survival bias because individuals who were disease-free at age 55 but developed CAD at age 62 were part of the at-risk population prior to age 55.
* **WHAT:** Retain all individuals in the risk set up to age 55 and right-censor all participants (including late-onset cases) who have not experienced an event by age 55 at $t = 55$.
* **HOW:** In the R `survival::coxph` script for Supplementary Table 14, define `time = pmin(age_at_event_or_censoring, 55)` and `status = ifelse(event == 1 & age_at_event <= 55, 1, 0)` across the full validation cohort, and update the hazard ratios in Supplementary Table 14.

#### 4. Benchmark Against Non-Infinitesimal `LDpred2-auto` / `LDpred2-grid` for Top Diseases
* **WHY:** The authors use `LDpred2-inf` (Methods, line 1 of second chunk), which forces all 1.14M SNPs to have non-zero Gaussian effects. For traits with sparser architectures (such as autoimmune diseases, gout, or specific neoplasms), `LDpred2-inf` substantially underperforms sparse `LDpred2-grid` or `LDpred2-auto`, which may exaggerate the apparent benefit of adding elastic-net-selected RFPRSs.
* **WHAT:** Perform a sensitivity check on the 6 highlighted diseases in Figure 5 (I10, T2D, CAD, E78, N18, J44) comparing `RFDiseasemetaPRS` against a disease PRS built with `LDpred2-auto`.
* **HOW:** Run `snp_ldpred2_auto` from `bigsnpr` on the existing summary statistics for the 6 diseases in Figure 5, evaluate the resulting single-disease PRS in the validation set, and report how much of the $\Delta R^2$ remains when the baseline disease PRS uses sparse Bayesian shrinkage.

#### 5. Technical, Mathematical, and Editorial Cleanup
* **WHY:** Several equations and sample counts in the Methods contain typographical errors.
* **WHAT & HOW:**
  1. **Methods, "Study population and design" (line 161):** Correct `"GWAS ( n = 177,488)"` to `"GWAS ( n = 174,488)"` so that $174,488 + 174,489 = 348,977$.
  2. **Methods, "Estimation of RFPRS and disease PRS" (lines 1–5 of chunk 2):** Reconcile the SNP count (`1,141,242 SNPs` on line 176 vs. `1,149,057 SNPs` on line 1 of chunk 2) and fix the index typo in Equation 3 from $\sum_{i=1}^m \hat{b}_1 x_{ij}$ to $\sum_{i=1}^m \hat{b}_i x_{ij}$.
  3. **Methods, Equation 5 (line 30 of chunk 2):** Add the missing subscript $c$ to the last standard deviation denominator so $\frac{\gamma_c}{\sigma} \alpha_{jc}$ reads $\frac{\gamma_c}{\sigma_c} \alpha_{jc}$.
  4. **Methods, "Statistics and reproducibility" (lines 43–47 of chunk 2):** In Equation 6, the formula writes `Disease (coded as 1 or 0)` while line 47 immediately below states `(coded as 1 for control or 2 for case)`—standardize to `0 for control or 1 for case`.
  5. **Methods, "Statistics and reproducibility" (line 49 of chunk 2):** Clarify why the validation set ($n = 56,192$) was split into a Modeling set ($n = 28,096$) and an evaluation set ($n = 28,096$) for NRI when the `RFDiseasemetaPRS` weights were already fixed in the PRS set ($n = 174,489$).
