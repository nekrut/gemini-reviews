# Review of OOD_REP3_11

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **4.4 / 10.0** (Flawed / Overstated)  
* **Score Breakdown:** Rigor: 1.2/3.5 | Claims: 1.2/2.5 | Biology: 1.1/2.0 | Reproducibility: 0.9/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This study investigates resting-state fMRI functional connectivity (FC) and nodal betweenness centrality (BC, integrated across sparsity thresholds of $6\%\text{--}34\%$ using the AAL-90 atlas) in 117 hospitalized depressed adolescents classified into groups with ($\text{PSQI} \ge 11$) and without ($\text{PSQI} < 11$) sleep disorders. In a discovery cohort of 86 patients ($n=44$ with sleep disorder, $n=42$ without), two-sample $t$-tests controlling for sex, age, disease duration, head motion, and HAMD score identify altered BC in three regions (MTG.R, DCG.L, CAU.L) and altered FC across nine edges (predominantly linking occipital/calcarine regions to MTG.R). The authors also train linear support vector machine (SVM) classifiers using within-fold $F$-score selection of the top 100 features across 86-fold leave-one-out cross-validation (LOOCV) and evaluate a 62-feature consensus model on a temporally subsequent validation cohort of 31 patients ($n=21$ with sleep disorder, $n=10$ without), reporting $81.40\%$ accuracy ($\text{AUC} = 89.34\%$) in LOOCV and $74.19\%$ accuracy ($\text{AUC} = 69.05\%$) in the validation cohort. Neither the raw connectivity matrices nor the analysis scripts are publicly deposited.

While performing $F$-score feature selection inside each LOOCV training fold and testing on a temporally independent 31-patient cohort are sound design choices, a forensic audit of the reported results reveals pervasive mathematical impossibilities in the classification performance table (Table 5), miscalculated or scrambled test statistics in Table 2, conflation of uncorrected and Bonferroni-corrected $p$-values in Tables 3 and 4, and sample-size and MRI acquisition parameter errors in the Methods. Most critically, in 5 out of the 6 rows of Table 5, the reported `Accuracy (%)` is mathematically incompatible with the reported `Sensitivity (%)` and `Specificity (%)` for the known group sizes ($44/42$ in discovery; $21/10$ in validation)—including two discovery models (`BC` and `FC`) where overall accuracy is reported as strictly lower than *both* sensitivity and specificity, which violates basic probability theory. Because the claim that combining BC and FC outperforms single-feature models rests directly on Table 5, the primary methodological conclusion is unsupported without a complete audit and recalculation of the confusion matrices.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Combining BC and FC features in an SVM classifier outperforms models trained on BC or FC features alone in both the discovery and validation cohorts (Table 5, Fig. 3): [Methodologically Flawed].**  
  Overall classification accuracy is a convex combination of sensitivity and specificity weighted by class prevalence: $\text{Accuracy} = \frac{N_+}{N}\text{Sensitivity} + \frac{N_-}{N}\text{Specificity}$, and therefore *must* lie between $\min(\text{Sensitivity}, \text{Specificity})$ and $\max(\text{Sensitivity}, \text{Specificity})$. In Table 5, 5 of the 6 rows violate this identity:
  1. **Discovery `BC` ($N_+ = 44, N_- = 42$):** $\text{Sensitivity} = 79.55\%$ ($35/44$) and $\text{Specificity} = 78.57\%$ ($33/42$), which requires $\text{Accuracy} = \frac{35+33}{86} = 79.07\%$, yet Table 5 reports `77.91%` ($67/86$)—strictly below both sensitivity and specificity.
  2. **Discovery `FC` ($N_+ = 44, N_- = 42$):** $\text{Sensitivity} = 79.55\%$ ($35/44$) and $\text{Specificity} = 83.33\%$ ($35/42$), which requires $\text{Accuracy} = \frac{35+35}{86} = 81.40\%$ (identical to `BC + FC`), yet Table 5 reports `76.74%` ($66/86$)—nearly 5 percentage points below both sensitivity and specificity.
  3. **Validation `BC + FC` ($N_+ = 21, N_- = 10$):** $\text{Sensitivity} = 66.67\%$ ($14/21$) and $\text{Specificity} = 80.00\%$ ($8/10$), which requires $\text{Accuracy} = \frac{14+8}{31} = 70.97\%$ ($22/31$), yet Table 5 reports `74.19%` ($23/31$).
  4. **Validation `BC` ($N_+ = 21, N_- = 10$):** $\text{Sensitivity} = 42.86\%$ ($9/21$) and $\text{Specificity} = 80.00\%$ ($8/10$), which requires $\text{Accuracy} = \frac{9+8}{31} = 54.84\%$ ($17/31$), yet Table 5 reports `64.52%` ($20/31$).
  5. **Validation `FC` ($N_+ = 21, N_- = 10$):** $\text{Sensitivity} = 80.95\%$ ($17/21$) and $\text{Specificity} = 50.00\%$ ($5/10$), which requires $\text{Accuracy} = \frac{17+5}{31} = 70.97\%$ ($22/31$, identical to `BC + FC`'s $\text{TP}+\text{TN}$), yet Table 5 reports `64.52%` ($20/31$).  
  If the reported sensitivities and specificities are correct, the `FC`-only model achieves the exact same number of correct predictions as `BC + FC` in both the discovery cohort ($70/86 = 81.40\%$) and the validation cohort ($22/31 = 70.97\%$).

* **The 62-feature consensus SVM model generalizes robustly to the independent validation cohort ($\text{Accuracy} = 74.19\%$, $\text{AUC} = 69.05\%$): [Fragile].**  
  Beyond the confusion-matrix arithmetic discrepancy noted above ($22/31 = 70.97\%$ vs. $23/31 = 74.19\%$), the ROC-AUC drops by $20.29$ percentage points from the discovery cohort ($89.34\%$) to the validation cohort ($69.05\%$). Furthermore, selecting 100 features per fold from $4,095$ total features ($90$ BC nodes $+ \binom{90}{2} = 4,005$ FC edges) in a sample of $n = 86$ yields a feature-to-sample ratio $> 1.16$ inside the linear SVM without nested feature-count tuning, contributing to overfitting on the discovery cohort.

* **Depressed adolescents with sleep disorders exhibit Bonferroni-corrected $p < 0.001$ alterations in BC across 3 nodes and FC across 9 edges (Tables 3 and 4): [Moderately Supported].**  
  The regional pattern (elevated occipital-to-MTG.R connectivity and altered MTG.R and CAU.L centrality) passes a family-wise $\alpha = 0.05$ Bonferroni threshold, but the manuscript misreports the *uncorrected* $p$-values ($p < 0.001$) as Bonferroni-corrected $p$-values. With $\text{df} = 86 - 2 - 5 = 79$ (controlling for 5 covariates), a $t$-statistic of $t = 3.750$ for DCG.L in Table 3 has an uncorrected two-sided $p = 3.36 \times 10^{-4}$, which after Bonferroni correction across $90$ AAL regions equals $p_{\text{Bonf}} = 0.030$ (not $< 0.001$). Similarly, across $\binom{90}{2} = 4,005$ unique FC edges, $t = 4.702$ for `ORBsup.L - ANG.L` in Table 4 has an uncorrected $p = 1.07 \times 10^{-5}$, yielding $p_{\text{Bonf}} = 0.043$ (reaching $p_{\text{Bonf}} < 0.001$ across $4,005$ tests requires $t > 5.62$, which none of the 9 edges achieves).

* **Identified BC and FC alterations specifically reflect sleep disorder pathophysiology independent of depression severity and clinical confounders: [Fragile].**  
  First, sleep disorder classification relies exclusively on a subjective self-report questionnaire cutoff ($\text{PSQI} \ge 11$) without objective polysomnography or actigraphy. Second, in the discovery cohort, the sleep-disordered group has significantly higher depression severity ($\text{HAMD} = 33.66 \pm 7.31$ vs. $29.00 \pm 8.70$, $p = 0.009$; Table 1), and the correlation analyses in Fig. 2B–C between network features and PSQI total scores do not report partial correlations controlling for HAMD. Third, psychotropic medication status (antidepressants, sedatives/hypnotics, antipsychotics) was not recorded or controlled for, despite directly affecting both PSQI sleep scores and resting-state BOLD connectivity.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Reconcile and Re-Compute All Confusion Matrix Metrics in Table 5
* **WHY:** Reporting overall accuracies that fall outside the interval $[\min(\text{Sensitivity}, \text{Specificity}), \max(\text{Sensitivity}, \text{Specificity})]$ is mathematically impossible and invalidates the comparison between `BC + FC`, `BC`, and `FC` models.
* **WHAT:** Provide the exact $2 \times 2$ confusion matrices ($\text{TP}, \text{FP}, \text{TN}, \text{FN}$) for all six models in Table 5 and recompute Accuracy, Sensitivity, Specificity, and AUC from the same decision threshold.
* **HOW:** Inspect the LIBSVM prediction output code (`svmpredict`). Verify whether `Sensitivity` and `Specificity` in Table 5 were accidentally extracted from optimal Youden's $J$ points on the ROC curve while `Accuracy` was computed at the default SVM decision value threshold of $0$, or whether rows/columns were transposed. Report the exact integer counts ($\text{TP}/44$, $\text{TN}/42$ for discovery; $\text{TP}/21$, $\text{TN}/10$ for validation) alongside percentages, and run McNemar's test or DeLong's test to formally test whether `BC + FC` significantly outperforms `FC` alone.

#### 2. Report Exact Uncorrected and Bonferroni-Corrected $p$-Values in Tables 3 and 4
* **WHY:** Writing `(t = 3.750, p < 0.001, Bonferroni-corrected)` and `(t = 4.702, p < 0.001, Bonferroni-corrected)` conflates the uncorrected $p$-value ($< 0.001$) with the family-wise error criterion ($p_{\text{Bonf}} < 0.05$).
* **WHAT:** Add separate columns for `Uncorrected p-value` and `Bonferroni-corrected p-value` in Tables 3 and 4.
* **HOW:** From the GRETNA two-sample $t$-test outputs ($\text{df} = 79$), compute the exact two-tailed $p_{\text{uncorr}} = 2(1 - F_{t, 79}(|t|))$, multiply by $90$ for nodal BC (Table 3) and by $4,005$ for edge-wise FC (Table 4), and report both values explicitly.

#### 3. Control for Depression Severity (HAMD) in PSQI Correlation and SVM Feature Selection
* **WHY:** Because HAMD scores differ significantly between the discovery groups ($33.66$ vs. $29.00$, $p = 0.009$) and correlate with PSQI, unadjusted Pearson correlations with PSQI (Fig. 2B–C) and unadjusted $F$-scores during LOOCV feature selection can be driven by overall depression severity rather than sleep disturbance.
* **WHAT:** Compute partial correlations controlling for HAMD (as well as age, sex, disease duration, and head motion), and residualize features against HAMD within each training fold.
* **HOW:** Re-run the 12 correlation tests in Fig. 2B–C and Supplementary Tables 1–2 as partial Pearson correlations controlling for HAMD, age, sex, disease duration, and mean FD. In the SVM pipeline, fit a linear regression of each feature on HAMD inside the training fold, apply the regression coefficients to residualize both the training and test fold features, and report the resulting classification accuracy.

#### 4. Fix Numerical, Statistical, and Technical Errors in Tables and Methods
* **WHY:** Multiple arithmetic and typographical errors across the manuscript impede verification and reproducibility.
* **WHAT & HOW:**
  1. **Validation Subgroup Sample Size Error (Methods, p. 5 vs. Results, p. 8):** In the Methods ("Support vector machine-based machine learning analysis"), the independent validation cohort ($n = 31$) is stratified into `a lower-severity depression group (HAMD score ≤ 35) (n = 12) and a higher-severity depression group (HAMD score > 35) (n = 29)`, which sums to $41$ instead of $31$. Given the reported accuracy of $73.68\%$ ($14/19$), correct `n = 29` to `n = 19`.
  2. **Table 2 Statistical Values and $p$-Values:** In Table 2 ($n_1 = 21, n_2 = 10$):
     - For `Gender (15/6 vs. 5/5)`, $\chi^2 = 1.359$ with $\text{df} = 1$ yields $p = 0.244$, not `0.662`.
     - For `Age (15.48 ± 1.44 vs. 15.20 ± 1.99)`, $t = 0.442$ with $\text{df} = 29$ yields $p = 0.662$, not `0.370` (note that `0.662` was misplaced into the Gender row above).
     - For `HAMD (38.81 ± 7.03 vs. 34.50 ± 9.56)`, the two-sample $t$-statistic corresponding to $p = 0.166$ is $t = 1.419$, not `0.220`. Recalculate and correct all test statistics and $p$-values in Table 2.
  3. **Impossible BOLD EPI Echo Time (Methods, "MRI data acquisition", p. 4):** The resting-state GRE-SS-EPI sequence is listed with `TE = 3.2 ms` (identical to the structural 3D T1 BRAVO `TE = 3.2 ms`). At 3.0 Tesla, $\text{TE} = 3.2\text{ ms}$ yields almost no $T_2^*$ BOLD sensitivity; verify the DICOM headers and correct to the actual EPI echo time (typically $\text{TE} = 30\text{ ms}$).
  4. **Connectivity Matrix Dimension (Methods, p. 4):** Parcellating into 90 ROIs produces a $90 \times 90$ symmetric connectivity matrix containing $\frac{90 \times 89}{2} = 4,005$ unique edges, not a `90 × 89 network connectivity matrix`.
