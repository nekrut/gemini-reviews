# Review of OOD_ANON_09

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **6.4 / 10.0** (Mixed / Salvageable)  
* **Score Breakdown:** Rigor: 2.0/3.5 | Claims: 1.7/2.5 | Biology: 1.4/2.0 | Reproducibility: 1.3/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This neuroimaging study investigates resting-state fMRI functional connectivity (FC) and nodal betweenness centrality (BC) across the 90-region Automated Anatomical Labeling (AAL) atlas to classify the presence of sleep disorders ($\text{PSQI} \ge 11$) among 117 adolescents hospitalized with depression. Using a temporal split, 86 patients recruited between June 2022 and June 2024 form the discovery cohort ($44$ with sleep disorder, $42$ without) and 31 patients recruited between June 2024 and October 2024 form an independent external validation cohort ($21$ with sleep disorder, $10$ without). In the discovery cohort, two-sample $t$-tests controlling for sex, age, illness duration, head motion, and HAMD depression severity identify significant BC alterations in 3 nodes (elevated right middle temporal gyrus [`MTG.R`], reduced left median cingulate [`DCG.L`] and left caudate [`CAU.L`]) and 9 FC edges (predominantly occipital-to-`MTG.R` connections). A linear support vector machine (SVM) trained on the top 100 $F$-score-filtered whole-brain BC+FC features achieves $81.40\%$ accuracy ($\text{AUC} = 89.34\%$) under 86-fold leave-one-out cross-validation (LOOCV) and $74.19\%$ accuracy ($\text{AUC} = 69.05\%$) on the independent validation cohort.

The study is thoughtfully designed in several key respects: the authors explicitly recognize the danger of feature-selection leakage in prior neuroimaging ML studies, perform normalization and $F$-score filtering strictly inside each LOOCV training fold, evaluate significance via 1,000 label-permutation tests, and test generalization on a temporally independent validation cohort. However, three technical and statistical issues weaken the strength of the conclusions: (1) the external validation cohort has a $21:10$ ($67.7\%$) class imbalance, where the reported $74.19\%$ accuracy ($23/31$ correct) exceeds the majority-class baseline ($67.74\%$) by only 2 patients and exhibits inverted sensitivity/specificity ($66.67\%$ sensitivity vs. $80.00\%$ specificity, which is mathematically impossible for integers out of $21$ and $10$ if accuracy is $74.19\%$); (2) the subgroup sample sizes in the validation cohort ($n = 12$ and $n = 29$) sum to $41$ instead of $31$; and (3) depression severity (HAMD) is significantly higher in the sleep-disorder group ($33.66 \pm 7.31$ vs. $29.00 \pm 8.70, p = 0.009$, Table 1), and while HAMD was controlled in the univariate $t$-tests, it was not regressed out of the features fed to the SVM classifier.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Group differences in nodal BC (`MTG.R`, `DCG.L`, `CAU.L`) and 9 occipital-temporal FC edges after controlling for HAMD and Bonferroni correction (Tables 3–4, Figure 2A): [Well Supported].**  
  The mass-univariate two-sample $t$-tests in the discovery cohort ($n=86$) appropriately include age, sex, disease duration, head motion (mean FD), and HAMD scores as covariates and apply Bonferroni correction across tests. The convergence of both nodal hubness (elevated BC in `MTG.R` and reduced BC in `CAU.L`) and pairwise edge strength (6 of 9 significant edges connecting bilateral lingual, calcarine, and occipital gyri to `MTG.R`, all $t = 4.82$–$5.27$) provides coherent evidence of hyper-connectivity between visual and middle temporal cortices in sleep-disturbed depressed adolescents.

* **Internal LOOCV classification performance of the combined BC+FC linear SVM ($\text{Accuracy} = 81.40\%, \text{AUC} = 89.34\%, p < 0.001$): [Moderately Supported].**  
  Unlike many clinical neuroimaging ML studies that pre-select features on the whole dataset, the authors perform z-score standardization, $F$-score ranking (top 100 out of $4,005\text{ FC} + 90\text{ BC} = 4,095$ features), and $C$ grid search strictly inside each of the 86 LOOCV training folds, with a 1,000-permutation null test. However, because the two groups in the discovery cohort differ significantly in overall depression severity ($\text{HAMD} = 33.66$ vs. $29.00, p = 0.009$, Table 1)—and the 24-item HAMD itself contains three insomnia items (early, middle, and late insomnia)—the unadjusted whole-brain FC/BC features fed to the SVM may partly classify overall depression severity rather than sleep disturbance specifically.

* **External validation performance ($\text{Accuracy} = 74.19\%, \text{Sensitivity} = 66.67\%, \text{Specificity} = 80.00\%$) and HAMD subgroup stability in the independent cohort ($n = 31$, Table 5): [Fragile].**  
  A forensic arithmetic check of Table 2 and Table 5 reveals two numerical inconsistencies in the independent validation cohort ($n = 31$, composed of $n_{\text{pos}} = 21$ with sleep disorder and $n_{\text{neg}} = 10$ without sleep disorder):
  1. *Confusion matrix arithmetic contradiction:* In Table 5, for `BC + FC` on the independent validation dataset, Sensitivity is $66.67\%$ ($14/21 = 66.67\%$ true positives) and Specificity is $80.00\%$ ($8/10 = 80.00\%$ true negatives). However, $(14 + 8) / 31 = 22 / 31 = 70.97\%$, whereas Table 5 reports $\text{Accuracy} = 74.19\%$ ($23 / 31$). Similarly, for `BC` alone, Sensitivity is $42.86\%$ ($9/21$) and Specificity is $80.00\%$ ($8/10$), which sums to $(9 + 8) / 31 = 17 / 31 = 54.84\%$, yet Table 5 reports $\text{Accuracy} = 64.52\%$ ($20 / 31$). And for `FC` alone, Sensitivity is $80.95\%$ ($17/21$) and Specificity is $50.00\%$ ($5/10$), which sums to $(17 + 5) / 31 = 22 / 31 = 70.97\%$, yet Table 5 reports $\text{Accuracy} = 64.52\%$ ($20 / 31$). In `BC`, $20/31$ is only possible if Sensitivity ($80\% = 8/10$) and Specificity ($42.86\% = 9/21$) were swapped or miscalculated ($12/21 + 8/10 = 20/31$).
  2. *Subgroup sample size mismatch:* In Section "Support vector machine-based machine learning analysis" (page 5), the authors state: "The independent validation cohort was stratified into two subgroups based on HAMD scores: a lower-severity depression group (HAMD score $\le 35$) ($n = 12$) and a higher-severity depression group (HAMD score $> 35$) ($n = 29$)." However, $12 + 29 = 41$, which exceeds the total independent validation sample size of $n = 31$ by 10 patients (and in Section "External validity," the higher-severity accuracy is reported as $73.68\% = 14/19$, indicating the subgroup size was actually $n = 19$, not $n = 29$).
  3. *Table 2 $t$-statistic typo:* In Table 2, the HAMD comparison ($38.81 \pm 7.03$ vs. $34.50 \pm 9.56$ for $n=21$ vs. $n=10$) reports $t = 0.220, p = 0.166$; for those means and SDs, the two-sample $t$-statistic is $t = 1.419$ (corresponding to $p = 0.166$), not $0.220$.

* **Correlations between the 3 BC nodes / 9 FC edges and continuous PSQI scores ($p < 0.0042$, Figure 2B–C): [Fragile].**  
  The 3 BC nodes and 9 FC edges were first selected because they differed most strongly between the high-PSQI ($\ge 11$) and low-PSQI ($< 11$) groups in the discovery cohort ($p < 0.001$ Bonferroni-corrected). Correlating those same pre-selected features against continuous PSQI scores in the exact same $n=86$ discovery cohort is circular (since the groups were defined by Dichotomizing PSQI at 11) and is guaranteed to yield highly significant correlations.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Reconcile the Confusion Matrix Arithmetic in Table 5 and Subgroup Sizes
* **WHY:** In Table 5, the reported Sensitivity and Specificity values for the independent validation dataset ($n_{\text{pos}}=21, n_{\text{neg}}=10$) do not sum to the reported Accuracy values for any of the three models (`BC+FC`, `BC`, `FC`), and the HAMD subgroup sizes ($12 + 29 = 41$) do not sum to $31$.
* **WHAT:** Report the exact integer counts ($\text{TP}, \text{FN}, \text{TN}, \text{FP}$) for the discovery ($n=86$) and validation ($n=31$) datasets, recompute Accuracy, Sensitivity, Specificity, and Balanced Accuracy, and fix the higher-severity subgroup count.
* **HOW:** Verify whether the positive and negative class labels were swapped when computing Sensitivity and Specificity on the validation set, update Table 5 so that $\text{Accuracy} = (\text{TP} + \text{TN}) / 31$, change "$n = 29$" to "$n = 19$" in the Methods ($12 + 19 = 31$), and fix the HAMD $t$-value in Table 2 from $0.220$ to $1.419$.

#### 2. Control for Non-Sleep Depression Severity (HAMD Excluding Insomnia Items) in Both Univariate and SVM Analyses
* **WHY:** The 24-item HAMD includes three sleep-disturbance items (items 4, 5, and 6), which both inflates the HAMD difference between groups ($p = 0.009$) and partially removes sleep-related variance when total HAMD is regressed out as a covariate in the univariate $t$-tests. Conversely, the SVM features were not adjusted for depression severity at all.
* **WHAT:** Compute a modified HAMD score excluding the three insomnia items ($\text{HAMD}_{\text{non-sleep}}$), use $\text{HAMD}_{\text{non-sleep}}$ as the covariate in the mass-univariate analyses, and test whether residualizing FC/BC features against $\text{HAMD}_{\text{non-sleep}}$ (fit on the training folds) preserves SVM accuracy.
* **HOW:** Subtract items 4–6 from total HAMD; within each LOOCV training fold, fit a linear regression of each FC/BC feature on age, sex, mean FD, and $\text{HAMD}_{\text{non-sleep}}$, apply the regression coefficients to residualize both the training and test fold features, and report the resulting covariate-adjusted SVM performance.

#### 3. Test PSQI Correlations in the Independent Validation Cohort
* **WHY:** Correlating the 3 BC nodes and 9 FC edges with PSQI in the discovery dataset ($n=86$) where those exact features were selected by dichotomizing PSQI at $\ge 11$ is circular.
* **WHAT:** Evaluate the Pearson/partial correlations between the 3 BC nodes / 9 FC edges and PSQI total scores in the independent validation cohort ($n = 31$) and within the sleep-disorder group alone ($n = 44$).
* **HOW:** Compute partial correlations (controlling for age, sex, and $\text{HAMD}_{\text{non-sleep}}$) between the 12 discovery-identified network features and PSQI in the $n=31$ validation set and report them alongside Figure 2B–C.
