# Review of OOD_REP2_01

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **4.9 / 10.0** (Flawed / Overstated)  
* **Score Breakdown:** Rigor: 1.5/3.5 | Claims: 1.3/2.5 | Biology: 1.3/2.0 | Reproducibility: 0.8/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This study investigates resting-state fMRI functional connectivity (FC) and nodal betweenness centrality (BC) across 90 Automated Anatomical Labeling (AAL) regions to classify comorbid sleep disorders (defined as Pittsburgh Sleep Quality Index [PSQI] $\ge 11$) among adolescents hospitalized with depression. Using a discovery cohort of $n = 86$ patients (44 with sleep disorders, 42 without) and a temporal validation cohort of $n = 31$ patients (21 with sleep disorders, 10 without), the authors report significant group differences in 3 regional BC values and 9 FC edges, correlate these features with continuous PSQI scores, and train a linear Support Vector Machine (SVM) on the top 100 $F$-score features per leave-one-out cross-validation (LOOCV) fold. They report $81.40\%$ LOOCV accuracy ($\text{AUC} = 89.34\%$) in the discovery cohort and $74.19\%$ accuracy ($\text{AUC} = 69.05\%$) in the external validation cohort. Raw data are restricted to requests to the authors, and analysis scripts are not publicly archived.

While combining topological centrality with pairwise connectivity and evaluating an temporally separated inpatient test cohort are positive design choices, the manuscript's primary conclusions are undermined by mathematical contradictions in the classification and demographic tables, circular post-hoc correlation tests, and unaddressed clinical confounding. Specifically, the sensitivity and specificity values reported in Table 5 are mathematically incompatible with the reported overall accuracies in five of the six model rows, the external validation performance ($\text{AUC} = 69.05\%$, true accuracy $22/31 = 70.97\%$) barely exceeds a naive majority-class classifier ($21/31 = 67.74\%$), and the correlation analyses double-dip by testing features pre-selected for dichotomous PSQI group differences against continuous PSQI in the same sample. Resolving these issues requires auditing and recomputing the confusion matrices, removing circular correlation claims, and controlling for depression severity and psychotropic medication load.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **The combined BC + FC SVM model generalizes robustly to the independent validation cohort with 74.19% accuracy: [Methodologically Flawed].**  
  In the independent validation cohort ($n = 31$: $P = 21$ with sleep disorder, $N = 10$ without sleep disorder; Table 2), Table 5 reports a sensitivity of $66.67\%$ ($14/21$ true positives) and a specificity of $80.00\%$ ($8/10$ true negatives) for the combined BC + FC model. The exact overall accuracy for 14 true positives and 8 true negatives is $(14 + 8) / 31 = 22 / 31 = 70.97\%$, contradicting the reported $74.19\%$ ($23/31$). The same mathematical impossibility occurs across Table 5: for validation BC alone, sensitivity $42.86\%$ ($9/21$) and specificity $80.00\%$ ($8/10$) yield $(9 + 8) / 31 = 54.84\%$, not the reported $64.52\%$ ($20/31$); for discovery FC alone ($P = 44, N = 42$), sensitivity $79.55\%$ ($35/44$) and specificity $83.33\%$ ($35/42$) yield $70 / 86 = 81.40\%$, not the reported $76.74\%$ ($66/86$); and for discovery BC alone, sensitivity $79.55\%$ ($35/44$) and specificity $78.57\%$ ($33/42$) yield $68 / 86 = 79.07\%$, not $77.91\%$ ($67/86$). Furthermore, because $21/31$ ($67.74\%$) of the validation cohort has a sleep disorder, a trivial classifier predicting the majority class for all patients achieves $67.74\%$ accuracy; the combined model's true accuracy of $70.97\%$ (22 vs. 21 correct predictions) and $\text{AUC} = 69.05\%$ represent weak discrimination.

* **Depressed adolescents with sleep disorders show Bonferroni-significant alterations in 3 nodal BC hubs (MTG.R, DCG.L, CAU.L) and 9 FC edges: [Fragile].**  
  Although the two-sample $t$-tests include sex, age, disease duration, head motion, and 24-item Hamilton Depression Rating Scale (HAMD) scores as covariates, two methodological issues affect these comparisons. First, the discovery groups differ significantly in total HAMD ($33.66 \pm 7.31$ vs. $29.00 \pm 8.70, p = 0.009$, Table 1), and the 24-item HAMD includes three insomnia items (items 4–6) that directly measure the outcome used to split the groups, introducing collider/over-adjustment distortion when covarying total HAMD rather than non-sleep HAMD. Second, the text states that Bonferroni correction was applied across whole-brain tests, yet for 4,005 unique AAL-90 FC edges ($\alpha = 0.05 / 4005 = 1.25 \times 10^{-5}$), a two-sample $t$-statistic with $df = 79$ requires $|t| \ge 4.66$; while the 9 reported edges have $t \in [4.702, 5.266]$, the manuscript never specifies whether the Bonferroni denominator was 90 (for BC) and 4,005 (for FC, vs. $90 \times 89 = 8,010$ as written on line 90), nor does it control for inpatient psychotropic or sedative medications.

* **The 3 altered BC regions and 9 altered FC edges correlate significantly with continuous PSQI scores ($p < 0.0042$): [Methodologically Flawed].**  
  The two patient groups were defined solely by dichotomizing the continuous PSQI score at $\ge 11$ versus $< 11$ in the discovery cohort ($n = 86$). Selecting the top 3 BC regions and 9 FC edges that survive $t$-tests between PSQI $\ge 11$ and PSQI $< 11$ and then computing Pearson correlations of those exact same features against continuous PSQI in the same $n = 86$ subjects is circular post-hoc selection ("double dipping"). Features selected for extreme between-group differences across a thresholded continuous variable are mathematically guaranteed to correlate with that continuous variable in the discovery sample.

* **External SVM classification performance is invariant to depression severity across validation subgroups: [Fragile].**  
  In Materials and Methods (line 110), the authors state that the $n = 31$ validation cohort was stratified into a lower-severity subgroup ($\text{HAMD} \le 35, n = 12$) and a higher-severity subgroup ($\text{HAMD} > 35, n = 29$), which sums to $41$ rather than $31$. In Results (line 264), the accuracy in the higher-severity subgroup is reported as $73.68\%$ ($14/19$), indicating $n = 19$ rather than $29$. Moreover, no class-balance breakdown (PSQI $\ge 11$ vs. $< 11$), sensitivity, specificity, or AUC is provided for these small subgroups ($n = 12$ and $n = 19$), making it impossible to tell whether the reported accuracies simply mirror the majority-class base rate within each stratum.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Reconcile Confusion Matrices and Classification Metrics in Table 5
* **WHY:** In a binary classification cohort with fixed positive ($P$) and negative ($N$) counts, overall accuracy is strictly determined by sensitivity and specificity via $\text{Accuracy} = (\text{Sensitivity} \cdot P + \text{Specificity} \cdot N) / (P + N)$. Five of the six rows in Table 5 violate this identity, indicating either that different decision thresholds were used to compute accuracy versus sensitivity/specificity (e.g., Youden's index on the ROC curve vs. the raw SVM hyperplane sign) or that sample counts were miscalculated.
* **WHAT:** Report the exact $2 \times 2$ confusion matrix ($\text{TP}, \text{FP}, \text{TN}, \text{FN}$) at a single, pre-specified decision boundary (the training-set SVM hyperplane $f(x) = 0$) for every model in Table 5, and benchmark external validation against the majority-class baseline ($67.74\%$) and Balanced Accuracy.
* **HOW:** Extract the predicted class labels from `svmpredict` in LIBSVM for each of the 86 LOOCV folds and the 31 external test subjects, tabulate $\text{TP}, \text{FP}, \text{TN}, \text{FN}$ directly from those binary predictions, and recompute Accuracy, Sensitivity, Specificity, and Balanced Accuracy $= (\text{Sensitivity} + \text{Specificity}) / 2$ from the same predictions.

#### 2. Eliminate Circular Correlation Testing and Evaluate Continuous Prediction Out-of-Sample
* **WHY:** Correlating brain features with continuous PSQI in the discovery sample after selecting those features for significant differences between $\text{PSQI} \ge 11$ and $\text{PSQI} < 11$ in the same sample inflates effect sizes and invalidates $p$-values.
* **WHAT:** Remove the in-sample discovery correlation claims or replace them with out-of-sample correlation tests in the independent validation cohort ($n = 31$).
* **HOW:** Compute the Pearson/Spearman correlations between the 3 discovery-identified BC nodes and 9 FC edges and continuous PSQI strictly within the held-out $n = 31$ validation dataset, and optionally train a support vector regression (SVR) model within the LOOCV loop to predict continuous PSQI out-of-fold.

#### 3. Separate Non-Sleep Depressive Symptoms from HAMD Covariates and Audit Feature Selection Leakage
* **WHY:** Controlling for total 24-item HAMD removes variance attributable to the three HAMD insomnia items, whereas the SVM pipeline ignores demographic and clinical covariates entirely and selects "consensus features" across all 86 LOOCV folds before retraining the final model on the full discovery set with a fixed $C = 16$.
* **WHAT:** Recompute group comparisons using a modified HAMD score that excludes the three sleep items ($\text{HAMD}_{\text{non-sleep}}$), and verify that SVM classification is not driven by depression severity or age/sex differences.
* **HOW:** Subtract items 4, 5, and 6 from the 24-item HAMD total, re-run the GRETNA two-sample $t$-tests with $\text{HAMD}_{\text{non-sleep}}$ as the covariate, and test whether the out-of-fold SVM decision values predict PSQI status in a logistic regression controlling for $\text{HAMD}_{\text{non-sleep}}$, age, sex, and medication class.

#### 4. Correct Numerical and Statistical Errors in Tables 1 and 2 and Methods
* **WHY:** Multiple test statistics and sample sizes in the text and demographic tables are internally inconsistent, undermining confidence in data curation.
* **WHAT & HOW:** Fix the following specific errors:
  1. **Methods (line 110):** Change the higher-severity validation subgroup size from $n = 29$ to $n = 19$ so that $12 + 19 = 31$ matches the total validation sample size and the $14/19 = 73.68\%$ accuracy reported in Results.
  2. **Table 1 (line 135):** Recompute the two-sample $t$-statistic and $p$-value for Head motion ($0.08 \pm 0.04$ vs. $0.07 \pm 0.04$, $n = 44$ vs. $42$), which yields $t \approx 1.16, p \approx 0.25$ rather than $t = 0.112, p = 0.911$ (or report 3 decimal places for the means if the true difference was $0.001$).
  3. **Table 2 (lines 149–153):** Correct the swapped/miscalculated $p$-values and statistics in the validation cohort: for Gender ($15/6$ vs. $5/5$), $\chi^2 = 1.359$ corresponds to $p = 0.244$, whereas $p = 0.662$ is the two-tailed $p$-value for Age ($t = 0.442, df = 29$); for HAMD ($38.81 \pm 7.03$ vs. $34.50 \pm 9.56$), recompute the $t$-statistic ($t \approx 1.27$, not $0.220$).
  4. **Methods (line 90):** Clarify that a symmetric undirected connectivity matrix over 90 ROIs contains $90 \times 89 / 2 = 4,005$ unique edges rather than $90 \times 89 = 8,010$.
