# Review of OOD_ANON_11

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **5.5 / 10.0** (Mixed / Salvageable)  
* **Score Breakdown:** Rigor: 1.7/3.5 | Claims: 1.5/2.5 | Biology: 1.3/2.0 | Reproducibility: 1.0/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This prospective single-arm longitudinal study examines whether baseline resting-state functional connectivity (rsFC) of the subgenual anterior cingulate cortex (sgACC) predicts 12-week clinical remission (HAMD-17 $\le 7$) in 87 medication-free outpatients with major depressive disorder (MDD) treated with escitalopram (10–20 mg/day). Using a 4 mm spherical seed at the right sgACC (MNI: $5, 25, -10$), the authors perform two-sample $t$-tests comparing remitters (RD, $n=42$) and non-remitters (NRD, $n=45$), correlate significant cluster connectivity with percent HAMD-17 reduction, and train an $L_2$-regularized logistic regression classifier following principal component analysis (PCA) dimensionality reduction in 10-fold cross-validation. They report higher baseline right sgACC connectivity with bilateral dorsolateral prefrontal cortex (DLPFC) and inferior parietal lobule (IPL) in remitters, positive correlations with symptom improvement ($r = 0.321\text{--}0.453$), and 10-fold cross-validated classification accuracy of 72.64% ($\text{AUC} = 0.74 \pm 0.21$, $p < 0.001$). Neither raw neuroimaging data nor analysis scripts are publicly deposited ("available on request").

While the clinical cohort is well-characterized, medication-free at baseline, and prospectively followed on a standardized monotherapy protocol, the statistical and machine-learning pipeline suffers from circular post-hoc correlation analysis ("double-dipping"), unnested hyperparameter tuning during cross-validation, circular interpretation of Haufe-transformed feature overlap, and the absence of a placebo or active-comparator control arm. Furthermore, baseline depression severity differs at the margin of statistical significance between groups ($p = 0.050$), which directly confounds a binary remission cutoff ($\text{HAMD-17} \le 7$). These limitations can be substantially resolved through computational re-analysis—specifically by implementing nested cross-validation, adjusting for baseline HAMD-17 in the predictive model, and replacing circular ROI correlations with whole-brain or out-of-fold estimates—paired with tempered framing around treatment specificity.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Higher baseline right sgACC–FPN (bilateral DLPFC and IPL) rsFC in remitters compared to non-remitters: [Moderately Supported].**  
  The whole-brain two-sample $t$-test is appropriately thresholded at voxel-wise $p < 0.001$ with cluster-level FWE $p < 0.05$ controlling for age, sex, education, and mean framewise displacement (Table 2). However, baseline HAMD-17 scores are lower in the RD group ($19.86 \pm 3.71$) than in the NRD group ($21.53 \pm 4.13$, $t = -1.99, p = 0.050$, Table 1). Because remission is defined by an absolute threshold ($\text{HAMD-17} \le 7$) rather than relative change, patients starting with milder symptoms require less absolute improvement to cross the remission boundary, and baseline HAMD-17 was not included as a covariate in the voxel-wise GLM.

* **Positive linear correlation ($r = 0.321\text{--}0.453$) between sgACC–DLPFC/IPL rsFC and percent HAMD-17 improvement: [Methodologically Flawed].**  
  The four clusters (left/right DLPFC, left/right IPL) were selected specifically because they survived whole-brain thresholding for the contrast between RD ($\text{week 12 HAMD-17} \le 7$) and NRD ($\text{week 12 HAMD-17} > 7$). Because percent HAMD-17 improvement is mathematically coupled to week-12 HAMD-17 status ($t = 10.23, p < 0.001$ between RD and NRD), extracting mean connectivity from clusters defined by RD vs. NRD and correlating them with percent improvement in the same 87 subjects constitutes classic non-independent circular analysis ("double-dipping"), which inflates correlation coefficients $r$ and invalidates the nominal $p$-values ($p \le 0.002$).

* **Baseline sgACC whole-brain rsFC predicts 12-week escitalopram remission with 72.64% accuracy and AUC = 0.74: [Fragile].**  
  Although PCA transformation was performed inside each training fold, the Methods state that *"Model performance was evaluated using 10-fold cross-validation, and the optimal model parameters were determined based on the average prediction accuracy."* Selecting the number of PCA components and the $L_2$ regularization penalty ($C$) by maximizing 10-fold CV accuracy without an inner cross-validation loop leaks test-fold information into hyperparameter selection. In addition, the reported cross-validation AUC standard deviation of $0.21$ across folds (roughly $8\text{--}9$ subjects per test fold) indicates substantial fold-to-fold instability.

* **82.78% spatial overlap between $K$-means Cluster 1 of top 1% Haufe-transformed predictive voxels and the between-group $t$-test ROIs validates the FPN biomarker: [Overstated].**  
  Both the two-sample $t$-test and the Haufe forward-model transformation ($\text{Cov}(X, \hat{y})$) were computed on the exact same sample of $n = 87$ patients using the same binary outcome label (RD vs. NRD). High spatial overlap between univariate mass-univariate $t$-statistics and linear classifier activation patterns fitted to the same data is a mathematical identity of linear models rather than an independent validation. Furthermore, applying $K$-means clustering after zeroing out 99% of whole-brain voxels (leaving 144,705 zero-valued voxels and 1,367 non-zero voxels) trivially forces one cluster (Cluster 0) to capture the zeroed background and the remaining two clusters to partition positive/high-magnitude versus lower-magnitude non-zero weights.

* **Specificity of sgACC–FPN hyperconnectivity as a biomarker for escitalopram pharmacotherapy efficacy: [Overstated].**  
  Because the study lacks a placebo control arm or an active comparator (e.g., rTMS or psychotherapy), the design cannot distinguish a treatment-specific pharmacotherapy biomarker from a general prognostic marker of spontaneous remission, regression to the mean, or non-specific clinical engagement. Moreover, the Discussion acknowledges that stringent screening excluded individuals intolerant or unresponsive to escitalopram or deviating from monotherapy guidelines, which introduces survivorship/selection bias into the analyzed sample.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Control for Baseline Depression Severity in Group Comparisons and Outcome Definitions
* **WHY:** Baseline HAMD-17 differs between RD ($19.86 \pm 3.71$) and NRD ($21.53 \pm 4.13$, $p = 0.050$). Because remission ($\text{HAMD-17} \le 7$) is an absolute threshold, baseline severity confounds the RD vs. NRD contrast.
* **WHAT:** Re-run the whole-brain two-sample $t$-test including baseline HAMD-17 as a covariate alongside age, sex, education, and mean FD, and report a secondary classification analysis predicting clinical *response* ($\ge 50\%$ HAMD-17 reduction), which is less sensitive to baseline score differences.
* **HOW:** Add baseline HAMD-17 to the SPM12/DPARSFA second-level design matrix, re-compute the FWE-corrected cluster statistics in Table 2, and report the resulting cluster coordinates and $T$-values.

#### 2. Eliminate Circularity in Symptom Improvement Correlations
* **WHY:** Computing Pearson correlations between percent HAMD-17 improvement and ROI clusters selected from the RD vs. NRD contrast in the same dataset violates statistical independence and inflates effect sizes.
* **WHAT:** Replace the post-hoc ROI correlation with either (a) a whole-brain voxel-wise regression of baseline sgACC rsFC against continuous percent HAMD-17 improvement (controlling for baseline HAMD-17, age, sex, education, and mean FD), or (b) correlations computed strictly within independent *a priori* anatomical/functional atlas definitions of the DLPFC and IPL (e.g., Yeo 7-network FPN parcellation).
* **HOW:** Extract mean sgACC rsFC within the predefined Yeo FPN DLPFC and IPL parcels across all 87 subjects, or run a whole-brain multiple regression in SPM12 with percent HAMD-17 improvement as the predictor of interest at voxel-wise $p < 0.001$, cluster FWE $p < 0.05$.

#### 3. Implement Nested Cross-Validation and Out-of-Fold Feature Interpretation
* **WHY:** Tuning PCA dimensionality and $L_2$ regularization parameters by maximizing 10-fold CV accuracy across the full dataset introduces optimistic bias, and zero-masking 99% of voxels prior to $K$-means clustering is an arbitrary heuristic.
* **WHAT:** Implement a nested cross-validation scheme (e.g., 10-fold outer loop with a 5-fold inner loop for PCA variance threshold and $L_2$ penalty tuning, repeated 100 times to stabilize fold variance) and compare the rsFC model against a clinical-only baseline model (age, sex, education, illness duration, baseline HAMD-17).
* **HOW:** In `scikit-learn`, wrap `Pipeline([('pca', PCA()), ('clf', LogisticRegression(penalty='l2'))])` inside `GridSearchCV` (inner 5-fold CV) and evaluate out-of-sample predictions via `cross_val_predict` across 100 repeated stratified 10-fold splits, reporting the mean and 95% confidence interval of AUC, accuracy, sensitivity, and specificity.

#### 4. Clarify Patient Attrition and Selection Criteria
* **WHY:** In the Methods (lines 34–51), 110 patients were enrolled, 13 were lost to follow-up, and 10 were excluded for head motion ($n = 87$), yet the Limitations (line 181) state that *"Stringent criteria were applied in this study to exclude individuals intolerant or unresponsive to escitalopram, as well as those deviating from monotherapy guidelines."* Excluding treatment-unresponsive patients prior to analysis would severely bias remission rates and invalidate predictive modeling.
* **WHAT:** Provide a CONSORT-style participant flow diagram clarifying exactly how many patients were screened, enrolled, excluded for non-adherence/intolerance versus clinical non-response, and lost to follow-up.
* **HOW:** Add a flow chart to the Methods or Supplement detailing the exact reasons for the 13 dropouts and any pre-enrollment exclusions, and verify whether any non-responders were excluded from the 97 completers.

#### 5. Deposit De-Identified Connectivity Matrices and Analysis Code
* **WHY:** Both the raw data and the Python 3.10.6 analysis scripts are currently unavailable, preventing independent verification of the PCA + $L_2$ logistic regression and Haufe transformation pipeline.
* **WHAT & HOW:** Deposit the unthresholded group $T$-maps on NeuroVault and upload the subject-level extracted ROI connectivity values, demographic/clinical table, and Python `scikit-learn` scripts to a public repository (e.g., GitHub/Zenodo or OSF).
