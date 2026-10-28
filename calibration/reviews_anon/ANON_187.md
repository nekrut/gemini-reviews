# Review of ANON_187

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **3.0 / 10.0** (Flawed / Overstated)  
* **Score Breakdown:** Rigor: 0.8/3.5 | Claims: 0.7/2.5 | Biology: 0.8/2.0 | Reproducibility: 0.7/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript constructs a 13-lncRNA prognostic risk score—termed the necroptosis-related lncRNA signature (`NRLS`)—in diffuse glioma using public bulk RNA-seq datasets (`TCGA LGG+GBM`, $n=663$ as training; `CGGA mRNAseq_693 + mRNAseq_325`, $n=1,018$ as validation; plus `GTEx` normal brain) and performs qRT-PCR for 5 lncRNAs across 5 non-tumor epilepsy brain tissues and 10–11 glioma specimens. The authors merge `TCGA` glioma and `GTEx` normal brain counts using `limma::removeBatchEffect()`, run `DESeq2` (`|log2FC| > 2`, $\text{adj. } P < 0.05$) to identify 20 differentially expressed necroptosis genes out of a literature list of 67, intersect lncRNAs correlated with these 20 genes ($|r| > 0.5$, $P < 0.001$) and significantly associated with overall survival (univariate Cox $P < 0.001$) across *both* `TCGA` and `CGGA` to obtain 43 lncRNAs, and then fit a `LASSO` Cox model on `TCGA` to select 13 lncRNAs. They evaluate the resulting risk score via Kaplan–Meier curves, multivariate Cox regression, time-dependent ROC curves, `GSEA`, immune deconvolution (`CIBERSORT`, `ESTIMATE`, `TIDE`, 7-algorithm bubble plots), `pRRophetic` drug `IC50` prediction, and `ConsensusClusterPlus` ($k=2$). Public repository homepages are cited, but no custom analysis code or processed data matrices are deposited.

While the manuscript applies a broad battery of standard bioinformatics visualization tools, its core conclusions are undermined by severe methodological flaws, data leakage, clinical confounding, and direct self-contradictions: (1) merging `TCGA` (almost entirely tumors) and `GTEx` (100% normal brain) via `limma::removeBatchEffect()` completely confounds technical study batch with biological disease state, and passing batch-corrected continuous values into `DESeq2` violates `DESeq2`'s requirement for unadjusted integer counts; (2) using univariate Cox survival outcomes in the `CGGA` validation cohort to pre-filter the 43 candidate lncRNAs before `LASSO` training constitutes direct test-set data leakage; (3) pooling WHO grade 2–3 lower-grade gliomas (`LGG`) with grade 4 glioblastomas (`GBM`) confounds the 13-lncRNA signature with canonical molecular classifiers (`IDH1/2` mutation and `1p/19q` codeletion); and (4) the manuscript contradicts itself on immunotherapy response, concluding in Section 3.6 that the **low-risk group** is more susceptible to immunotherapy (based on lower `TIDE` scores) and then concluding in Section 3.8 that **Cluster 1** (which is the **high-risk group**) is more susceptible to immunotherapy.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Differential expression analysis between `TCGA-Glioma` and `GTEx-Brain` via `removeBatchEffect()` and `DESeq2` identifies 20 dysregulated necroptosis genes in glioma: [Methodologically Flawed].**  
  First, `TCGA` (`LGG + GBM`) contains virtually exclusively tumor samples (only 5 normal brain samples exist across `TCGA-GBM` and 0 in `TCGA-LGG`), whereas `GTEx-Brain` contains exclusively normal post-mortem brain samples. Running `limma::removeBatchEffect()` across two datasets where batch (`TCGA` vs. `GTEx`) is collinear with biological condition (`Tumor` vs. `Normal`) is statistically unidentifiable unless an explicit design matrix preserving the condition effect is supplied, which still cannot separate sequencing-center/protocol artifacts (post-mortem `GTEx` vs. surgical `TCGA`) from tumor biology. Second, `DESeq2` models raw negative-binomial integer counts; feeding continuous batch-adjusted values from `removeBatchEffect()` into `DESeq2` is mathematically invalid.

* **The 13-lncRNA `NRLS` signature is independently validated in the `CGGA` cohort and serves as an independent prognostic factor beyond WHO 2021 molecular classification: [Methodologically Flawed].**  
  This conclusion is compromised by two flaws:
  1. **Direct survival leakage from `CGGA` during feature selection:** Section 2.2 (line 54) states: *"Next, the repeated genes were applied to univariate Cox regression in two cohorts [TCGA and CGGA] with a threshold of P < 0.001. For further analyses, we intersected the lncRNAs screened from the TCGA and CGGA cohorts. Subsequently, a total of 43 reliably expressed lncRNAs were detected."* Selecting the 43 input features by requiring $P < 0.001$ in `CGGA` survival analysis leaks the test set's survival outcomes into model construction, invalidating `CGGA` as an independent validation cohort.
  2. **Confounding by `LGG` vs. `GBM` pooling and incomplete multivariate adjustment:** In the WHO 2021 classification (cited in the Introduction), adult-type diffuse gliomas are stratified first by `IDH1/2` mutation and `1p/19q` codeletion (`IDH`-mutant oligodendroglioma, `IDH`-mutant astrocytoma, and `IDH`-wildtype glioblastoma). While Section 2.4 mentions `IDH` and `1p/19q` status, Section 3.3 (line 133) states *"Univariate Cox regression shows risk score, grade, age, and histology subtype in each cohort were significantly related to prognosis"* and the nomogram (Fig. 4c) omits `IDH` and `1p/19q` status (and its caption mislabels Fig. 4c as *"Nomograph plot of predicted 1-, 3-, and 5-year overall survival probability based on prognosis lncRNAs"*).

* **The `NRLS` risk score and consensus clustering reliably predict immunotherapy response in glioma: [Methodologically Flawed].**  
  The manuscript directly contradicts itself between Section 3.6 and Section 3.8:
  * In **Section 3.6 (line 160)**, the authors show that the **high-risk group** has higher `PD-L1`/`PD-1`/`CTLA-4`, higher `TIDE` dysfunction, and a significantly higher overall `TIDE` score (Fig. 6e–g), and conclude: ***"These results suggested that the low-risk group is more susceptible to immunotherapy."***
  * In **Section 3.8 (line 182)**, the authors divide the cohort into `Cluster 1` and `Cluster 2`, show that `Cluster 1` has significantly *worse* OS and significantly *higher* risk scores (matching the **high-risk group**, Fig. 8c–d and Discussion line 214), and yet conclude the exact opposite: ***"We observed that Cluster 1 has stronger immune infiltration than Cluster 2... Therefore, we could consider Cluster 1 was more susceptible to immunotherapy."***
  Furthermore, no actual immunotherapy-treated glioma cohort (e.g., anti-PD-1 treated GBM) is analyzed.

* **High-risk glioma patients are more sensitive to `A-443654`, `Gefitinib`, `Temsirolimus`, `Trametinib`, `Bortezomib`, and `Pazopanib` based on `pRRophetic` `IC50` predictions: [Overstated].**  
  `pRRophetic` extrapolates *in vitro* cancer cell line sensitivity from `GDSC` (predominantly non-CNS epithelial cell lines cultured in serum without a blood–brain barrier) to bulk patient tumor transcriptomes (where differences between high- and low-risk glioma groups are heavily driven by non-neoplastic microglia/macrophage stromal infiltration, as shown by `ESTIMATE` in Fig. 5g–i). Claiming clinical chemosensitivity guidance from unvalidated *in silico* ridge-regression projections without accounting for blood–brain barrier penetration or clinical trial failures of `Gefitinib`/`Temsirolimus`/`Pazopanib` in glioblastoma is unwarranted.

* **qRT-PCR in clinical specimens validates the prognostic value of the 5 selected NRLs: [Overstated].**  
  In Section 3.9 (Fig. 9), the authors measure 5 lncRNAs in 5 epilepsy temporal lobe samples and 10–11 glioma samples without any survival follow-up, statistical test description, or multiple-testing correction, and conclude *"suggesting that the signature based on NRLs could be used to predict the clinical outcome in glioma patients."* Comparing expression between 5 non-tumor epilepsy tissues and 10–11 tumors does not test or validate survival prognosis.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Eliminate `CGGA` Data Leakage by Performing All Feature Selection Strictly Within the `TCGA` Training Cohort
* **WHY:** Filtering candidate lncRNAs by requiring univariate Cox $P < 0.001$ and $|r| > 0.5$ in *both* `TCGA` and `CGGA` before running `LASSO` uses the validation cohort (`CGGA`) to select features, biasing validation performance upward.
* **WHAT:** Perform necroptosis correlation filtering, univariate Cox screening, `LASSO` variable selection, and risk-score cutoff determination exclusively within `TCGA`, locking all model weights and thresholds before evaluating a single statistic in `CGGA`.
* **HOW:** Re-run the pipeline in R using only `TCGA` ($n=663$) to identify prognostic lncRNAs and fit `glmnet(..., family = "cox")`. Apply the locked `TCGA` linear predictor ($\sum \beta_i x_i$) and locked `TCGA` cutoff directly to `CGGA` ($n=1,018$) and report the resulting unbiased `CGGA` Kaplan–Meier log-rank $p$-value and 1-, 3-, and 5-year ROC AUCs.

#### 2. Stratify All Survival and Microenvironment Analyses by WHO 2021 Molecular Subtypes (`IDH`-Wildtype GBM vs. `IDH`-Mutant LGG)
* **WHY:** Combining `IDH`-mutant lower-grade gliomas with `IDH`-wildtype glioblastomas into a single pooled cohort creates massive confounding: `IDH`-wildtype status simultaneously drives poor survival (median ~14 months vs. ~7+ years) and high macrophage/microglia and immune-checkpoint infiltration (`ESTIMATE` ImmuneScore).
* **WHAT:** Evaluate whether the locked `NRLS` risk score retains statistically significant independent prognostic value (multivariate Cox HR, 95% CI, and time-dependent ROC AUC) *within* `IDH`-wildtype glioblastoma (`GBM`) and *within* `IDH`-mutant lower-grade glioma (`LGG`) separately, and include `IDH` mutation, `1p/19q` codeletion, and `MGMT` promoter methylation in the multivariate Cox models and nomogram.
* **HOW:** Report the exact multivariate Cox HRs, 95% CIs, and $p$-values for `NRLS` when adjusting simultaneously for age, WHO grade, `IDH` status, `1p/19q` codeletion, and `MGMT` status in both `TCGA` and `CGGA`, and compute ΔAUC / C-index improvement of `Clinical + Molecular + NRLS` versus `Clinical + Molecular` alone.

#### 3. Resolve the Direct Contradiction Between Sections 3.6 and 3.8 on Immunotherapy Susceptibility
* **WHY:** Section 3.6 concludes that the **low-risk group** is more susceptible to immunotherapy (due to lower `TIDE` dysfunction/exclusion scores), whereas Section 3.8 concludes that **Cluster 1** (the **high-risk group**) is more susceptible to immunotherapy (due to higher raw immune cell infiltration). Both statements cannot simultaneously be true.
* **WHAT:** Reconcile the interpretation of immune infiltration versus T-cell dysfunction/exhaustion across Sections 3.6, 3.8, and the Discussion, and test the `NRLS` score in an actual anti-PD-1 treated glioblastoma cohort (e.g., Zhao et al. 2019 *Nature Medicine* `PRJNA482620` or Cloughesy et al. 2019 *Nature Medicine* `GSE121810`).
* **HOW:** Remove the contradictory claim in Section 3.8 (line 182), explain clearly that myeloid/Treg-dominated infiltration in high-risk (`Cluster 1`) gliomas is immunosuppressive rather than immunotherapy-responsive, and evaluate `NRLS` directly on published RNA-seq data from anti-PD-1 treated GBM patients.

#### 4. Replace the Invalid `removeBatchEffect()` + `DESeq2` Step with Proper Count-Based Normalization
* **WHY:** `DESeq2` requires raw integer read counts and cannot be run on continuous matrices output by `limma::removeBatchEffect()`. Furthermore, `TCGA` (tumor) vs. `GTEx` (normal) is completely confounded by study batch.
* **WHAT:** Use the pre-harmonized `UCSC Toil RNA-seq Recompute` (`TCGA TARGET GTEx`) raw count or `limma-voom` pipeline (or compare `TCGA` tumors against the 5 internal `TCGA-GBM` solid tissue normal samples and `CGGA` normal brain controls) instead of running `removeBatchEffect()` followed by `DESeq2`.
* **HOW:** If using `DESeq2`, input unadjusted integer counts from the uniform `Toil` alignment pipeline; if using `limma`, apply `voom` and `lmFit` on log-CPM values and verify overlap with `CGGA` normal-vs-glioma DEGs.

#### 5. Correct Numerous Factual, Mathematical, and Editorial Errors Throughout the Text
* **WHY:** The manuscript contains several basic biological misstatements, impossible mathematical values ($r^2 < 0$), and sample-count discrepancies.
* **WHAT & HOW:**
  1. **Introduction line 31:** Change `"isocratic dehydrogenase (IDH)"` to `"isocitrate dehydrogenase (IDH)"`.
  2. **Introduction line 37:** Change `"lncRNAs are a subclass of non-coding RNA with a length of up to 200 nucleotides"` to `"with a length of more than 200 nucleotides"` (RNAs $<200\text{ nt}$ are small non-coding RNAs, not lncRNAs).
  3. **Methods line 97 vs. Figure 9 caption (line 199):** Line 97 states `"including five non-tumor brain tissues, three WHO grade 2, three WHO grade 2, and four GBM"` (which repeats `"three WHO grade 2"` twice and sums to $3+3+4 = 10$ glioma tissues), whereas the Figure 9 caption states `"5 non-tumor brain tissues and 11 glioma tissues"`. Correct the duplicate `"WHO grade 2"` (presumably `"WHO grade 3"`) and reconcile the total glioma sample count (`10` vs. `11`).
  4. **Results line 144:** Change `"We selected terms with adjusted P value > 0.01"` to `"adjusted P value < 0.01"`, and change `"IL6-JAK-TAT3"` to `"IL6-JAK-STAT3"`.
  5. **Results line 155:** Change `"r^2 = 0.59"`, `"r^2 = 0.60"`, and `"r^2 = -0.41"` to `"r = 0.59"`, `"r = 0.60"`, and `"r = -0.41"` (a squared correlation coefficient $r^2$ cannot be negative), and fix `"neglective related to the risk score"` to `"negatively related to the risk score"`.
  6. **Figure 9 caption (line 199):** Fix gene symbol typo `"FAM18A-AS1"` to `"FAM181A-AS1"`.
  7. **Introduction line 39 & Discussion line 208:** Remove leftover template/editing artifacts `"(p1)"` and `"(p2)"`.
