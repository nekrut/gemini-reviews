# Review of PMC12471436 (PMID:41003135)

**Manuscript Title:** RETRACTED: Machine-Learning-Based Survival Prediction in Castration-Resistant Prostate Cancer: A Multi-Model Analysis Using a Comprehensive Clinical Dataset  
**Authors:** Lee JH, Jeong J, Ahn YJ, Lee KS, Lee JS, Lee SH, Ham WS, Chung BH, Koo KC.  
**Journal / Preprint:** *J Pers Med* (2025; `PMC12471436` / `PMID:41003135` / `10.3390/jpm15090432`)  
**Calibration Study Cohort:** Cohort A — Known Invalid / Refuted (`A48` | Double-Blinded as `ANON_119`)  
**Overall Score:** **3.7 / 10.0** (Flawed / Overstated)  
* **Score Breakdown:** Rigor: 0.9/3.5 | Claims: 1.0/2.5 | Biology: 1.0/2.0 | Reproducibility: 0.8/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This retrospective two-institution study develops and compares machine learning (ML) models—including Random Survival Forests (RSFs), XGBoost, LightGBM, Random Forest classifiers, Cox proportional hazards, and logistic regression—to predict cancer-specific mortality (CSM), overall mortality (OM), and binary 2-year and 3-year survival in 801 patients with castration-resistant prostate cancer (CRPC) diagnosed between 2005 and 2022. Using 46 clinical, laboratory, pathological, and treatment variables split 80:20 into training ($n = 641$) and test ($n = 160$) sets, the authors report that RSF achieves the highest test-set Harrell's C-index for CSM ($0.772$) and OM ($0.771$), and use SHAP to identify the time interval from CRPC diagnosis to first-line therapy initiation, hemoglobin, and alkaline phosphatase (ALP) as the top predictors. Neither the dataset nor the analysis code is made publicly available.

Despite addressing an important clinical problem in a sizable CRPC cohort, the study's modeling pipeline and reported statistics suffer from critical methodological errors that invalidate its primary conclusions. First, the models predict survival starting from CRPC diagnosis while incorporating post-diagnosis variables—specifically "the time interval from a CRPC diagnosis to the initiation of first-line therapy" (the #1 SHAP feature in Figures 2 and 3) and "the durations of the first, second, and third lines of treatment until disease progression" (Section 2.1)—which introduces severe immortal-time and lookahead bias. Second, the reported survival statistics are mathematically contradictory: Section 3.1 states that $73.4\%$ (588/801) of patients died over the entire study period, yet Table 2 reports a 2-year overall survival rate of only $17.7\%$ and a 3-year overall survival rate of $13.0\%$ (which would require $>82\%$ mortality within 2 years), indicating that right-censored patients were misclassified as dead or that survival and censoring were conflated. Third, missing values were imputed on the entire dataset prior to the 80:20 train/test split (data leakage), and Table 1 reports a biologically implausible median duration from ADT initiation to CRPC of $0.0\text{ months}$ (IQR $0.0\text{--}3.0$). Rebuilding the survival and classification models strictly with baseline CRPC covariates, proper censoring handling, and within-fold imputation is required.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **RSF and XGBoost substantially outperform Cox proportional hazards ($C = 0.772$ vs. $0.621$ for CSM) in predicting survival from CRPC diagnosis: [Methodologically Flawed].**  
  Two forms of data leakage compromise the regression benchmark. First, Section 2.1 and Section 3.3 state that the 46 predictors include the time interval from CRPC diagnosis to initiation of first-line CRPC therapy (the top-ranked SHAP predictor in Figures 2 and 3) as well as the durations and sequences of first-, second-, and third-line CRPC treatments until progression. Because survival time is measured from CRPC diagnosis (Section 2.3.1), a patient must survive long enough after CRPC diagnosis to initiate first-line therapy and complete first-, second-, and third-line treatment durations. Feeding post-baseline time intervals and future treatment durations into nonlinear tree models allows RSF and XGBoost to reconstruct total survival time directly from post-index treatment duration sums (immortal-time / lookahead bias). Second, Section 2.3.1 states that iterative Bayesian ridge imputation was performed on the dataset *before* randomizing into the 80:20 training and test split, leaking test-set covariate distributions into training.

* **The 2-year and 3-year overall survival rates in the cohort are 17.7% and 13.0%, and Random Forest / XGBoost accurately classify 2- and 3-year survival status: [Methodologically Flawed].**  
  Section 3.1 reports that over a median follow-up of $24.0\text{ months}$ (IQR $12.0\text{--}43.0$), 566 patients ($70.6\%$) experienced CSM and 588 ($73.4\%$) experienced OM, meaning at least $26.6\%$ (213/801) of patients never died at any point during follow-up. It is therefore mathematically impossible for 2-year overall survival to be $17.7\%$ and 3-year overall survival to be $13.0\%$ (Table 2), as that would imply $82.3\%$ and $87.0\%$ mortality within 2 and 3 years. This discrepancy indicates that the authors computed "2-year survival" as the crude fraction of the 801 patients who remained uncensored and under active observation beyond 24 and 36 months, treating all patients right-censored before 24 or 36 months as non-survivors in Table 2 and in the binary classification targets (Table 4).

* **SHAP analysis identifies time from CRPC diagnosis to first-line therapy, hemoglobin, and ALP as the primary prognostic drivers of CRPC survival: [Overstated].**  
  While baseline hemoglobin and ALP at CRPC progression are well-established biological prognostic markers, the dominance of "time interval from CRPC diagnosis to first-line therapy" in the SHAP summary plots (Figures 2 and 3) is an artifact of immortal time: patients who deferred first-line systemic CRPC therapy for many months after biochemical/radiographic CRPC progression were, by definition, alive and clinically stable during that untreated window.

* **Baseline clinicopathological characteristics accurately reflect a standard consecutive CRPC progression cohort: [Fragile].**  
  Table 1 reports that the median *"Duration from ADT administration to CRPC (months)"* is **0.0 (IQR: 0.0–3.0)** across all 801 patients. By Prostate Cancer Working Group 2 criteria, CRPC requires disease progression *despite* castrate testosterone levels induced by prior ADT; a median ADT-to-CRPC duration of 0.0 months implies that over half of the cohort was diagnosed with CRPC on the exact day ADT was started, which is clinically impossible and points to a date-subtraction or coding error in data preparation.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Remove Post-CRPC Lookahead Variables and Anchor Prediction at a Well-Defined Landmark Time
* **WHY:** Including post-CRPC treatment initiation delays and first-, second-, and third-line CRPC treatment durations when time zero ($t_0$) is CRPC diagnosis introduces severe immortal-time and lookahead bias, as patients who live longer naturally accumulate longer treatment durations and more lines of therapy.
* **WHAT:** Restrict the predictor matrix to variables strictly known at $t_0$ (either at initial CRPC diagnosis or at initiation of first-line CRPC systemic therapy).
* **HOW:** Drop `time from CRPC diagnosis to first-line therapy` and all first-, second-, and third-line CRPC treatment duration variables from the feature matrix (or move $t_0$ to the date of first-line CRPC therapy initiation and include only pre-first-line variables), re-train Cox, RSF, and XGBoost models, and update Table 3 and the SHAP plots (Figures 2 and 3).

#### 2. Correct Right-Censoring Handling in Table 2 and Binary 2-/3-Year Classification Models
* **WHY:** Treating patients lost to follow-up or administratively censored prior to 24 or 36 months as "events" (or excluding uncensored survivors) produced impossible survival rates in Table 2 ($17.7\%$ 2-year OS vs. $73.4\%$ total mortality) and biased binary classification labels in Table 4.
* **WHAT:** Report true Kaplan–Meier survival probabilities (with $95\%$ CIs) at 24 and 36 months in Table 2, and account for right-censoring in the 2-year and 3-year binary classification evaluation.
* **HOW:** Extract the 24- and 36-month survival estimates directly from the Kaplan–Meier estimator (`lifelines.KaplanMeierFitter.predict([24, 36])`) for Table 2. For binary 2- and 3-year classification in Table 4, either apply Inverse Probability of Censoring Weighting (IPCW) when computing AUC, Brier score, and F1-score (`sksurv.metrics.cumulative_dynamic_auc`), or restrict binary classification to patients with complete 24-/36-month follow-up weighted by censoring probability.

#### 3. Perform Imputation Strictly Inside Training Folds and Account for Competing Risks in CSM
* **WHY:** Imputing missing values across all 801 patients before the 80:20 split leaks test-set information, and treating non-cancer deaths as independent censoring in CSM ignores competing risks.
* **WHAT:** Encapsulate imputation inside a `scikit-learn` `Pipeline` fitted solely on the training split/folds, and evaluate a competing-risks model (Fine–Gray subdistribution hazard or competing-risk RSF) for CSM.
* **HOW:** Fit `IterativeImputer` and mode imputation exclusively on the 80% training set ($n = 641$) and apply `.transform()` to the 20% test set ($n = 160$). In addition, clarify in Section 2.3.1 and Table 3 that "Valid score" represents the mean 10-fold cross-validation C-index within the 641-patient training cohort while "Test score" represents the held-out 160-patient test cohort.

#### 4. Audit the ADT-to-CRPC Duration Calculation in Table 1
* **WHY:** A median duration from ADT initiation to CRPC of $0.0\text{ months}$ (IQR $0.0\text{--}3.0$) in Table 1 contradicts the clinical natural history of hormone-sensitive prostate cancer (which typically responds to ADT for 12–36 months before castration resistance).
* **WHAT:** Verify the date columns used to compute `Duration from ADT administration to CRPC` in the source database.
* **HOW:** Check whether `ADT initiation date` was inadvertently overwritten with `first-line CRPC therapy date` or `CRPC diagnosis date` for patients who received ADT at referring clinics, recalculate the true interval from initial hormone-sensitive ADT start to CRPC progression, and update Table 1.

#### 5. Technical, Mathematical, and Editorial Cleanup
* **WHY:** Inconsistent model naming and missing reproducibility statements hinder verification.
* **WHAT & HOW:**
  1. **Section 3.2 (Paragraph 3, line 183) vs. Table 4:** The text refers to the binary classifier in Table 4 as *"the RSF model"* (*"For 2-year survival predictions, the RSF model achieved the best overall performance..."*), whereas Section 2.3.2 and Table 4 list *"Random Forest"* (a standard binary classifier, not a Random Survival Forest). Correct the text in Section 3.2 to distinguish the binary Random Forest classifier from the survival RSF model.
  2. **Section 2.3.2 (line 57):** Clarify how *"grid search"* and *"the Optuna optimization framework"* were used together (e.g., whether Optuna's `GridSampler` or Bayesian TPE sampler was used).
  3. **Code and Data Availability:** Deposit the Python preprocessing, Optuna tuning, RSF/XGBoost training, and SHAP evaluation scripts in a public GitHub/Zenodo repository and include an explicit Data Availability Statement.
