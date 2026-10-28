# Review of ANON_168

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **5.9 / 10.0** (Mixed / Salvageable)  
* **Score Breakdown:** Rigor: 1.4/3.5 | Claims: 1.5/2.5 | Biology: 1.4/2.0 | Reproducibility: 1.6/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript presents a computational workflow that integrates single-cell RNA-seq data from high-grade serous ovarian cancer (HGSOC; 6 patients with paired pre- and post-chemotherapy samples across `GSE165897`, `GSE191301`, and `GSE201047`, plus 10 normal fallopian tube/ovary control samples from `GSE151214` and `GSE184880`; 118,173 total cells) to infer gene regulatory networks (GRNs) and extract prognostic gene features for bulk RNA-seq survival classification in TCGA ($n = 342$). To mitigate single-cell sparsity and computational cost, the authors aggregate single cells into 1,921 metacells using `SEACells` (retaining 1,211 cell-type-pure metacells expressing 10,504 features) and infer 312 transcription factor (TF) regulons via `pySCENIC`. They then evaluate 10,000 combinations of top $N \in [1, 100]$ regulons and top $M \in [1, 100]$ target genes in a binary classification task ($\ge 2$-year overall survival) on an 80%/20% train/validation split of TCGA-HGSOC, concluding that treatment-status-specific regulon features outperform differentially expressed (DE) features, that cell-type-specific GRNs generally do not outperform all-metacell GRNs, and that `SNX8` is a shared prognostic candidate ($p = 0.0041$). Code and exact package versions are publicly available on GitHub.

Using `SEACells` metacell aggregation prior to `pySCENIC` GRN inference is a practical strategy for reducing single-cell dropout, and the authors deserve credit for transparently reporting negative results (specifically, that cell-type-specific GRNs do not outperform global metacell GRNs, Fig. 5A–B) and sharing their codebase. However, three statistical and methodological flaws undermine the core machine learning conclusions: (1) right-censored TCGA patients were assigned to binary $<2$-year versus $\ge 2$-year survival classes based simply on their observed follow-up time (Abstract, line 8), which misclassifies living patients lost to follow-up within 2 years as short-term deaths; (2) evaluating 10,000 $(N, M)$ feature-set combinations on a single 20% validation split ($n \approx 69$ patients) and comparing the "top 1%" (best 100 validation scores) against a 1D DE-feature ranking (of only 170–442 DE genes) introduces severe selection bias (winner's curse) without an independent test set; and (3) relying on positive-class F1 score in an imbalanced dataset where 74.9% (256/342) of patients belong to the majority class ($\ge 2$-year survival) inflates apparent accuracy. Fortunately, all three issues can be resolved computationally using the authors' existing GitHub pipeline and public data.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Treatment-status-specific regulon feature extraction significantly outperforms DE-feature-based extraction and control regulons in predicting 2-year HGSOC survival: [Fragile].**  
  To evaluate regulon features, the authors searched a $100 \times 100$ two-dimensional grid ($N$ regulons $\times M$ genes = 10,000 models) on a single 80%/20% TCGA split ($n \approx 69$ validation samples, containing only $\sim 17$ deaths within 2 years) and selected the top 1% validation scores (100 models; Fig. 3A–B). By contrast, the DE-feature baseline (Fig. 3C) only varied a 1D cutoff across the available DE genes (170 in Before-chemotherapy, 442 in After-chemotherapy). Selecting the top 100 validation scores out of 10,000 trials on a 69-patient validation split without nested cross-validation or a held-out test set guarantees upward bias from overfitting to the validation split. Furthermore, as stated in the Abstract (line 8), *"censored cases at last follow-up [were] assigned to the appropriate class by observed time"*, which conflates right-censoring before 2 years with death before 2 years.

* **Cell-type-specific GRNs do not generally outperform all-metacell treatment-status GRNs for bulk survival prediction: [Well Supported].**  
  In Section *"Cell-type-specific GRNs did not generally outperform all-cell models"* (Fig. 5A–B, Table S16), the authors test the same $100 \times 100$ grid within individual cell types and transparently report that none of the Before-chemotherapy cell-type GRNs and only T-cell After-chemotherapy GRNs exceeded the all-metacell baseline. Because TCGA RNA-seq measures bulk tumor mixtures rather than purified cell types, this negative finding is both biologically coherent and honestly framed.

* **Differentially expressed features in Before-chemotherapy, After-chemotherapy, and Control conditions are significantly enriched within top 1% TF regulons: [Moderately Supported].**  
  The overlap analysis showing that 360 DE features map into the top 1% `pySCENIC` TF–target interactions ($p < 0.0001$, Fig. S5A) and segregate by treatment status ($p = 0.0033$, Fig. S5B) is internally consistent, because `pySCENIC` (GRNBoost2) derives TF–target importance weights from co-expression across the exact same 1,211 metacells used for DE testing. However, DE features were called using a Wilcoxon rank-sum test across metacells (`n = 1,211`) rather than across patients (`n = 6` HGSOC, `n = 10` controls), which treats multiple metacells from the same donor as independent replicates (pseudo-replication).

* **`SNX8` is a shared multi-cell-type regulon target associated with poor prognosis in HGSOC: [Moderately Supported].**  
  `SNX8` emerges reproducibly as the sole gene shared across the four-way intersection of Before/After-chemotherapy and cell-type/all-cell regulons in more than half of cell types (endothelial, epithelial, fibroblast, and myeloid/macrophage; Fig. 5C) and stratifies overall survival in TCGA-HGSOC ($p = 0.0041$, Fig. S24B). However, its prognostic value is only assessed via a univariate Kaplan–Meier log-rank test on the same TCGA cohort used for feature prioritization, without multivariable adjustment for clinical covariates (e.g., FIGO stage III vs. IV, age, or residual disease status) or external cohort validation.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Correct the Handling of Right-Censored Patients in the 2-Year Survival Outcome
* **WHY:** Assigning patients who are right-censored (alive at last follow-up) at $<2$ years to the $<2$-year survival class based on observed follow-up time mislabels living, lost-to-follow-up patients as having died within 2 years.
* **WHAT:** Either (a) exclude patients who were right-censored prior to 24 months (alive with follow-up $< 730$ days) when constructing the binary 2-year survival label, or (b) replace the binary classifier with a censored survival model (e.g., `scikit-survival` Coxnet / Random Survival Forest evaluated by Harrell's C-index and Inverse-Probability-of-Censoring Weighted [IPCW] 2-year Brier/AUC score).
* **HOW:** In the TCGA clinical data cleaning script, verify `vital_status` and `days_to_last_follow_up`; filter out any patient with `vital_status == "Alive"` and `days_to_last_follow_up < 730` before running the binary classification models, or apply `sksurv.metrics.cumulative_dynamic_auc` at $t = 730$ days across all 342 patients.

#### 2. Replace the Single 80/20 Split and 10,000-Grid Cherry-Picking with Repeated Nested Cross-Validation
* **WHY:** Evaluating 10,000 $(N, M)$ hyperparameter pairs on a single 20% validation set ($n \approx 69$) and reporting the top 1% of validation scores overfits to the validation split and creates an unfair comparison against the much smaller 1D DE-feature baseline. Furthermore, with a 74.9% majority class, standard F1 is dominated by majority-class prediction.
* **WHAT:** Use $5 \times 5$-fold repeated stratified nested cross-validation (selecting optimal $(N, M)$ in the inner loop and evaluating out-of-fold predictions in the outer loop) and report ROC-AUC, PR-AUC (for the minority $<2$-year death class), and balanced accuracy alongside F1.
* **HOW:** Using `scikit-learn`'s `RepeatedStratifiedKFold(n_splits=5, n_repeats=5)`, compute out-of-fold ROC-AUC and minority-class F1 across matched feature-set sizes $K \in \{10, 25, 50, 100, 200, 500\}$ for (1) Before-chemo regulons, (2) After-chemo regulons, (3) Control regulons, and (4) DE features, and test significance using a paired Wilcoxon test corrected for cross-validation fold dependence.

#### 3. Account for Donor-Level Clustering in Metacell Differential Expression and Adjust `SNX8` Survival for Clinical Covariates
* **WHY:** Running a Wilcoxon test across 1,211 metacells derived from 16 individuals inflates false positives via pseudo-replication, and univariate KM analysis of `SNX8` in TCGA does not control for stage or debulking status.
* **WHAT:** Aggregate metacell expression to donor-level pseudobulks (or include donor ID as a random effect) to confirm the core DE/regulon overlaps, and fit a multivariable Cox proportional hazards model for `SNX8` in TCGA-HGSOC.
* **HOW:** Fit `coxph(Surv(time, status) ~ SNX8_expr + age + stage)` in R (`survival` package) on the 342 TCGA patients and report the adjusted hazard ratio and 95% confidence interval for `SNX8` alongside Figure S24B.

#### 4. Technical, Mathematical, and Editorial Cleanup
* **WHY:** The description of sample counts in the Results is numerically inconsistent, and processed metacell/regulon matrices should be deposited directly in the GitHub/Zenodo repository rather than "upon request."
* **WHAT & HOW:**
  1. **Results (page 2, line 83):** Clarify *"We collected 31 samples from five datasets, comprising six patient samples and ten control samples (Table S1)."* Because $6 + 10 = 16 \neq 31$, revise the wording to state *"comprising 21 paired pre-/post-chemotherapy tumor samples from six HGSOC patients and 10 control samples"* (matching the 31 total samples).
  2. **Data Availability (page 5, line 184):** Upload the processed `1,211 × 10,504` metacell count matrix and the 312 `pySCENIC` regulon tables directly to the existing GitHub repository (`https://github.com/bsml320/HGSOC`) or Zenodo instead of restricting them to *"available upon request."*
