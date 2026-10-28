# Review of OOD_ANON_54

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **3.4 / 10.0** (Flawed / Overstated)  
* **Score Breakdown:** Rigor: 0.9/3.5 | Claims: 0.9/2.5 | Biology: 1.0/2.0 | Reproducibility: 0.6/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This cross-sectional resting-state fMRI (R-fMRI) study compares seed-based functional connectivity (FC) of six occipital gyrus subregions (bilateral superior, middle, and inferior occipital gyri from the AAL template) across 30 patients with tremor-dominant (TD) Parkinson's disease (PD), 43 patients with postural instability and gait disturbance (PIGD) PD, and 42 healthy controls (HCs). Using ANCOVA (controlling for age, sex, and gray matter volume) followed by post-hoc two-sample $t$-tests in SPM12, the authors report decreased occipital FC in PIGD relative to TD and HCs across multiple cingulate, parietal, sensorimotor, and striatal regions, correlate extracted FC values with clinical scales (PIGD, BBS, MDS-UPDRS II), and fit binary logistic regression models to generate receiver operating characteristic (ROC) curves. They report an AUC of 0.910 for distinguishing TD from PIGD, 0.874 for TD vs. HC, and 1.000 (100% sensitivity and 100% specificity) for distinguishing PIGD from HCs, concluding that occipital FC serves as an effective diagnostic biomarker for PD motor subtypes. Raw imaging and clinical data are explicitly withheld ("Research data are not shared").

The study's primary biomarker claims and group comparisons suffer from three severe methodological flaws: (1) textbook circular "double-dipping" and in-sample overfitting in the ROC classification analysis, where dozens of features were selected based on whole-dataset $t$-tests and then combined in an unregularized in-sample logistic regression (fitting ~43 predictors to 85 subjects for PIGD vs. HC, mathematically guaranteeing the spurious $\text{AUC} = 1.000$); (2) unadjusted clinical confounding between the TD and PIGD groups, where PIGD patients have significantly more advanced Hoehn and Yahr stage ($3.05 \pm 0.60$ vs. $2.33 \pm 0.42$, $p < 0.001$) and non-motor/motor complication severity (UPDRS I, II, IV), confounding motor subtype differences with overall disease progression; and (3) pooling TD and PIGD subgroups together to correlate subtype-selected FC features against the very PIGD and balance (BBS) scores used to define the subtypes, creating an artificial bimodal cluster correlation (visible in Figure 3). Salvaging this work requires controlling for Hoehn-Yahr stage and head motion (framewise displacement) in the group models, computing within-group correlations, and evaluating classification performance via nested out-of-sample cross-validation.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Multiple occipital FC indicators distinguish PIGD patients from HCs with 100% sensitivity, 100% specificity, and $\text{AUC} = 1.000$, and distinguish TD from PIGD with $\text{AUC} = 0.910$: [Methodologically Flawed].**  
  First, the ROI-to-cluster FC features entered into the ROC analysis (Table 5: 12 features for TD vs. PIGD; ~43 features for PIGD vs. HC) were identified using voxel-wise two-sample $t$-tests across the exact same 115 subjects ("double-dipping" / data leakage). Second, the authors entered all significant clusters into a single binary logistic regression model on the same sample without train/test splitting, cross-validation, or regularization (Section 2.3). In the PIGD ($n = 43$) vs. HC ($n = 42$) comparison (total $N = 85$), Table 3 and Table 5 list roughly 41–43 significant FC clusters; fitting a binary logistic regression with $\sim 42$ continuous predictors on $N = 85$ observations hits the Cover-Vapnik linear separability bound ($p \approx N/2$), producing complete quasi-complete separation of the training data ($\text{AUC} = 1.000$, 100% sensitivity/specificity) purely as an algebraic artifact of overfitting.

* **TD PD patients exhibit significantly higher FC than PIGD PD patients between occipital subregions (SOG, MOG, IOG) and the cingulate gyrus, inferior parietal lobule, paracentral lobule, and right caudate: [Fragile].**  
  While voxel-wise ANCOVA and post-hoc $t$-tests were FWE-corrected at the cluster level ($p < 0.05$ with voxel-level $p < 0.001$), the analysis tested 6 correlated seed ROIs across 3 pairwise comparisons without Bonferroni correction across the 6 seeds ($p < 0.05 / 6 = 0.0083$). More importantly, Table 1 reveals that the PIGD group is at a significantly more advanced Hoehn and Yahr stage than the TD group ($3.05 \pm 0.60$ vs. $2.33 \pm 0.42$, $p = 0.000$), with higher UPDRS I ($13.30$ vs. $9.20$, $p = 0.004$), UPDRS II ($21.58$ vs. $12.23$, $p = 0.000$), UPDRS IV ($6.93$ vs. $4.37$, $p = 0.007$), and ESS ($7.33$ vs. $4.13$, $p = 0.013$). Because the ANCOVA controlled only for age, sex, and total GM volume (Section 2.3), the reported FC reductions in PIGD vs. TD are confounded by overall PD stage and non-motor burden rather than isolating motor-subtype-specific circuitry. Furthermore, continuous framewise displacement (head motion) was not included as a covariate, which is critical when comparing tremor-dominant patients against akinetic-rigid/PIGD patients.

* **Occipital-cingulate and occipital-parietal FC values correlate significantly with PIGD scores ($r = -0.402$ to $-0.475$), BBS balance scores ($r = 0.398$), and MDS-UPDRS II scores ($r = -0.396$ to $-0.440$) across PD patients: [Methodologically Flawed].**  
  As shown in the scatter plots in Figure 3 (where TD patients are plotted as blue dots and PIGD patients as yellow dots), the correlation analysis pooled the TD ($n = 30$) and PIGD ($n = 43$) groups after excluding intermediate PD patients. Because the FC masks were pre-selected for having significant differences between TD and PIGD (Section 2.3: "within the mask showing differences among the three groups"), and because TD and PIGD are defined by extreme ratios of tremor to PIGD scores (creating two separated groups on PIGD, BBS, and UPDRS II scales, Table 1), pooling the two groups guarantees a significant correlation across the bimodal cloud (Simpson's/two-group correlation artifact) even if the correlation within TD or within PIGD is zero.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Eliminate Circular Feature Selection and Overfitting in the ROC / Logistic Regression Analysis
* **WHY:** Selecting 12–43 FC clusters on the full dataset and fitting an unregularized logistic regression on the same $N = 73\text{--}85$ subjects leaks test labels into feature selection and causes complete linear separation ($\text{AUC} = 1.000$) when the number of features approaches half the sample size.
* **WHAT:** Implement nested cross-validation with penalized logistic regression (LASSO or Elastic Net) or remove the multivariate ROC claims.
* **HOW:** Use 10-fold stratified cross-validation where, inside each training fold (90% of subjects), seed-to-voxel or AAL-atlas-based occipital FC features are selected and entered into an $L_1$/$L_2$-penalized logistic regression (`glmnet` in R), and predictions are evaluated strictly on the held-out 10% test fold. Report the out-of-sample cross-validated AUC with 95% DeLong confidence intervals.

#### 2. Control for Disease Stage (Hoehn & Yahr) and In-Scanner Head Motion (FD)
* **WHY:** PIGD patients have significantly higher Hoehn and Yahr stage ($3.05$ vs. $2.33$, $p < 0.001$) than TD patients, and tremor vs. postural instability patients exhibit different in-scanner head micro-movements. Without controlling for H-Y stage and mean framewise displacement (FD), group differences may reflect general disease progression or motion artifacts.
* **WHAT:** Re-run the TD vs. PIGD two-sample $t$-test covarying for Hoehn & Yahr stage and mean FD, and apply a Bonferroni correction across the 6 seed ROIs.
* **HOW:** Compute mean Jenkinson FD for each participant from the 6 realignment parameters; report mean FD per group in Table 1; and include mean FD and Hoehn-Yahr stage (plus UPDRS I/IV or levodopa equivalent daily dose) as covariates in the SPM12 second-level design matrix for the TD vs. PIGD comparison, using a cluster-level FWE threshold of $p < 0.05 / 6 = 0.0083$.

#### 3. Perform Within-Group Partial Correlations for Clinical Scales
* **WHY:** Pooling TD and PIGD patients (while excluding intermediate patients) to correlate FC values selected for TD-vs-PIGD differences against PIGD/BBS/UPDRS-II scores (which also differ between TD and PIGD at $p < 0.0001$) induces a circular two-group correlation artifact.
* **WHAT:** Compute partial correlations separately within the PIGD group ($n = 43$) and within the TD group ($n = 30$), or include subtype group membership as a covariate.
* **HOW:** In SPSS or R, calculate partial Pearson/Spearman correlations between extracted FC values and PIGD, BBS, and MDS-UPDRS II scores separately within PIGD and TD (controlling for age, sex, GM volume, and mean FD), as well as across all 73 PD patients while controlling for a binary group indicator (`TD vs. PIGD`).

#### 4. Resolve Contradictions in Informed Consent, Preprocessing Versions, and Sample Size Statements
* **WHY:** Multiple internal contradictions in the Methods and Discussion undermine confidence in the study protocol.
* **WHAT & HOW:**
  * **Section 2.1 (Line 47):** Resolve the direct contradiction between adjacent sentences: `"This retrospective study was approved by the institutional review board (reference number: S2022-572-01), which waived the necessity for written informed consent"` vs. `"The following requirements were applied to all participants: ... (2) a signed informed consent form"`.
  * **Section 2.2 (Line 54):** Clarify the head-motion exclusion criterion `"head shift or angular rotation >2"` by specifying the units (`> 2 mm or 2°`), and explain why functional data were preprocessed in `SPM12 / MATLAB 2022b` while structural 3DFSPGR data were preprocessed in `SPM8 / MATLAB 2013b`.
  * **Section 4 (Line 344):** Fix the contradictory limitation statement: `"Initially, the sample size was small, and patients with intermediate PD were not included. Subsequently, the sample size was increased to include patients with intermediate PD."` No intermediate PD patients are included anywhere in this study.
  * **Figure 4 Caption vs. Section 3.7 (Lines 270, 276):** In Section 3.7, Figure 4B is cited as PIGD vs. HC ($\text{AUC} = 1$) and Figure 4C as TD vs. HC ($\text{AUC} = 0.874$), whereas the Figure 4 caption states `"the classification of TD and HCs (B); the classification of PIGD and HCs (C)"`.
  * **Section 4 (Line 334):** Correct `"bilateral LOG"` to `"bilateral IOG"`.
