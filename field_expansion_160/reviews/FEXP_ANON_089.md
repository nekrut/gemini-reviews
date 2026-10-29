# Review of FEXP_ANON_089

**Overall Score:** **2.5 / 10.0** (Fundamentally Invalid) | **Scientific Core Score:** **2.0 / 8.0**  
* **Score Breakdown:** Rigor: 0.7/3.5 | Claims: 0.6/2.5 | Biology: 0.7/2.0 | Reproducibility: 0.5/2.0

---

## 1. Blinded Metadata Perception

* **Perceived Role / Domain:** Bioinformatics single-cell and bulk transcriptomic prognostic modeling study of $\text{CD8}^+$ T cell-associated genes in ovarian cancer (`GSE184880`, `TCGA-OV`, `GSE30161`, `GSE63885`).
* **Blinded Document Assessment:** A formulaic single-cell + TCGA LASSO prognostic signature manuscript containing severe template and numerical errors: referring to the ovarian cancer cohorts as *"breast cancer samples"* in the Methods, claiming a *"17-gene"* model while only listing 16 genes across the entire paper, omitting the risk score formula after the colon *"using the following formula:"*, reporting identical 4-timepoint ROC AUCs (`0.81, 0.73, 0.76, 0.66`) for two independent GEO cohorts (`GSE30161` and `GSE63885`), applying *paired* Wilcoxon tests to independent patient groups, and contradicting itself between Results and Discussion on whether immune pathways are enriched in the high-risk or low-risk group.

---

## 2. Executive Summary & Editorial Verdict

The authors reanalyze scRNA-seq data from seven treatment-naive ovarian tumors (`GSE184880`, 27,045 cells) to identify 1,020 $\text{CD8}^+$ T cell marker genes. Using univariate Cox regression (64 genes) followed by LASSO Cox regression in the `TCGA` ovarian cancer cohort, they construct a prognostic risk score claimed to comprise 17 genes (though only 16 genes are named: `SLFN5`, `CD40LG`, `EMB`, `ISG20`, `CD226`, `CCR7`, `S1PR4`, `RNF167`, `MLLT3`, `PLEKHF1`, `RNPEPL1`, `STK39`, `FXYD5`, `BTN3A3`, `WNK1`, `SUSD3`) and validate survival stratification in `GSE30161` and `GSE63885`. They further compare GO/GSEA/GSVA pathways, tumor mutation burden (TMB), ESTIMATE/CIBERSORT immune infiltration, TIDE/IPS/IMvigor210 immunotherapy metrics, and `oncoPredict` chemotherapy IC50 values between median-split risk groups.

**Editorial Verdict: Reject (Fundamentally Invalid).** The manuscript contains pervasive numerical, methodological, and editorial defects that render its primary findings unverifiable and internally contradictory:
1. **Omitted Risk Formula, 17-vs.-16 Gene Count Mismatch, and "Breast Cancer" Copy-Paste Error:** In Methods line 32, the authors state they *"analyzed the RNA expression matrices of breast cancer samples in the TCGA, GSE30161, and GSE63885 datasets"*—a clear leftover from a template manuscript on breast cancer. Throughout the text (lines 32, 89, 145), the model is described as containing **17 genes**, yet only **16 gene symbols** are listed in every instance. Worse, line 34 states *"we calculated the risk score for each patient in the training set using the following formula:"* followed by a blank line with no equation or regression coefficients provided anywhere in the main text.
2. **Duplicate 4-Timepoint AUC Numbers Across Independent Validation Cohorts (`GSE30161` and `GSE63885`):** In Results line 94, the 1-, 2-, 3-, and 5-year ROC AUC values in `GSE30161` are reported as **`0.81, 0.73, 0.76, and 0.66`**, and two sentences later the 1-, 2-, 3-, and 5-year AUC values in the independent cohort `GSE63885` are also reported as **`0.81, 0.73, 0.76, and 0.66`**.
3. **Internal Contradiction on Immune Pathway Enrichment and Invalid Paired Wilcoxon Tests:** Results line 99 (Figure 3A) states that the **high-risk group** is significantly enriched in B-cell receptor signaling, T-cell receptor complex, and antigen binding pathways, whereas Results line 109 (Figure 4A–D) and Discussion line 147 state the exact opposite—that the **low-risk group** has higher ESTIMATE immune scores, higher $\text{CD8}^+$ T cell infiltration, and higher B-cell receptor and T-cell receptor signaling. In addition, Figures 3D, 4C, and 4D apply a **paired** two-sided Wilcoxon test to compare independent high-risk and low-risk patient groups.

### Specific Conclusions and Assessment of Support

* **Single-cell identification of 1,020 $\text{CD8}^+$ T cell marker genes in `GSE184880`: [Moderately Supported].**  
  The basic Seurat/Harmony reclustering of 27,045 cells across seven ovarian tumors identifies canonical stromal, epithelial, and lymphoid compartments, although no doublet removal (`DoubletFinder`/`Scrublet`) was performed and many of the 1,020 genes (e.g., `SUSD3`, `STK39`, `WNK1`, `MLLT3`) are broadly expressed outside $\text{CD8}^+$ T cells (as acknowledged in line 149).
* **Construction and external validation of the "17-gene" $\text{CD8}^+$ T cell prognostic signature in `TCGA`, `GSE30161`, and `GSE63885`: [Methodologically Flawed].**  
  Only 16 genes are listed despite claiming 17 genes; the risk score equation and LASSO coefficients are completely missing (line 34); the Methods misidentify the cohorts as "breast cancer samples" (line 32); and `GSE30161` and `GSE63885` are assigned identical 1-, 2-, 3-, and 5-year AUCs (`0.81, 0.73, 0.76, 0.66`, line 94).
* **Functional and immune microenvironment differences between high- and low-risk groups: [Methodologically Flawed].**  
  Results line 99 (Fig. 3A) claims B-cell and T-cell receptor signaling pathways are enriched in the **high-risk** group, directly contradicting Results line 109 (Fig. 4C) and Discussion line 147, which state that B-cell and T-cell receptor signaling are enriched in the **low-risk** group. Furthermore, independent high-risk vs. low-risk cohorts were compared using a *paired* Wilcoxon test (Figs. 3D, 4C, 4D) without multiple-testing correction across 16–22 parallel tests.
* **Prediction of immunotherapy response (`IMvigor210`) and chemotherapy sensitivity (`oncoPredict`) in ovarian cancer: [Overstated].**  
  `IMvigor210` is a urothelial (bladder) carcinoma cohort rather than ovarian cancer (where immune checkpoint monotherapy has historically low response rates of ~10%), and `oncoPredict` cell-line extrapolations do not establish clinical drug resistance.

---

## 3. Forensic Defect Inventory

1. **Template Copy-Paste Error ("Breast Cancer Samples"), 17-vs.-16 Gene Count Mismatch, and Omitted Formula (Pillar 3 & Pillar 7):**
   * **Location:** Materials and Methods ("Construction and validation of a CD8+ T cell-related prognostic signature", lines 32–35), Results (line 89), and Discussion (line 145).
   * **Defect:**
     * Line 32 states: *"We then analyzed the RNA expression matrices of **breast cancer samples** in the TCGA, GSE30161, and GSE63885 datasets"*.
     * Lines 32, 89, and 145 state that **17** prognostic signature genes were identified, but list only **16** genes (`SLFN5, CD40LG, EMB, ISG20, CD226, CCR7, S1PR4, RNF167, MLLT3, PLEKHF1, RNPEPL1, STK39, FXYD5, BTN3A3, WNK1, SUSD3`).
     * Line 34 ends with *"we calculated the risk score for each patient in the training set using the following formula:"* followed by a blank line; the mathematical formula and all gene coefficients are absent from the manuscript.
2. **Identical 4-Timepoint ROC AUC Values Reported for `GSE30161` and `GSE63885` (Pillar 4 & Pillar 7):**
   * **Location:** Results ("Construction and validation of a prognostic model...", line 94).
   * **Defect:** Line 94 reports 1-, 2-, 3-, and 5-year AUCs of `0.81, 0.73, 0.76, and 0.66` for `GSE30161` (Fig. 2J) and then reports the exact same four numbers (`0.81, 0.73, 0.76, and 0.66`) for `GSE63885` (Supplementary Fig. 2D).
3. **Self-Contradiction Between Results and Discussion on High-Risk vs. Low-Risk Immune Enrichment (Pillar 3 & Pillar 5):**
   * **Location:** Results (line 99, Figure 3A) vs. Results (line 109, Figure 4A–D) and Discussion (line 147).
   * **Defect:** Line 99 states that the *high-risk* group has significant enrichment in the B-cell receptor signaling pathway, T-cell receptor complex, and antigen binding pathways (Fig. 3A), whereas line 109 and line 147 state that the *low-risk* group has higher immune infiltration and higher enrichment in the B-cell receptor and T-cell receptor signaling pathways (Fig. 4C). This indicates that the sign of the log-fold change (`high vs. low` vs. `low vs. high`) in `DESeq2` (line 41) was inverted in Figure 3A–B.
4. **Application of Paired Wilcoxon Tests to Unpaired Patient Groups and `DESeq2` on Pre-Normalized Data (Pillar 3 & Pillar 4):**
   * **Location:** Methods (line 27, line 41) and Figure legends 3D (line 102) and 4C–D (line 112).
   * **Defect:** Figures 3D, 4C, and 4D specify a *"Paired two-sided Wilcoxon test"* for comparing independent high-risk and low-risk patient cohorts (which do not have paired observations and may not even have equal sample sizes if $N$ is odd). In addition, `DESeq2` (line 41) requires raw integer read counts, whereas UCSC Xena expression matrices (line 27) are typically log2-transformed normalized matrices unless specifically downloaded as raw counts. Finally, Discussion line 147 repeatedly refers to the survival nomogram (Fig. 7C) as a *"forest plot capable of predicting multi-year survival rates"*.

---

## 4. Quantitative Rubric Scoring

| Rubric Dimension | Score | Max | Forensic Justification |
| :--- | :---: | :---: | :--- |
| **1. Methodological & Statistical Rigor** | **0.7** | **3.5** | Omitted risk score formula and coefficients; 17 vs. 16 gene discrepancy; paired Wilcoxon test applied to unpaired groups; inverted DEG direction between Fig. 3A and Fig. 4C; identical AUCs reported for two validation cohorts. |
| **2. Claim-to-Evidence Alignment** | **0.6** | **2.5** | Contradictory claims regarding immune pathway enrichment in high- vs. low-risk groups; bladder cancer (`IMvigor210`) immunotherapy responses extrapolated to ovarian cancer; nomogram confused with forest plot. |
| **3. Data Integrity & Biological Plausibility** | **0.7** | **2.0** | Methods line 32 refers to ovarian cohorts as "breast cancer samples"; duplicate AUC values across `GSE30161` and `GSE63885` indicate copy-paste data corruption. |
| **4. Reproducibility & Data Integrity** | **0.5** | **2.0** | Because the risk score equation, LASSO coefficients, and 17th gene name are missing from the paper and no code is provided, the model cannot be reproduced by any external researcher. |
| **Scientific Core Score** | **2.0** | **8.0** | Sum of Rigor + Claims + Biology. |
| **Total Composite Score** | **2.5** | **10.0** | **Fundamentally Invalid** |

---

### 5. Constructive and Doable Suggestions for Improvement

1. **Publish the Complete Risk Score Formula, All Gene Symbols, and Coefficients:** Insert the missing mathematical equation at Methods line 34, reconcile whether the LASSO model contains 16 or 17 genes (identifying the missing 17th gene if applicable), and provide a table of exact regression coefficients $\beta_i$.
2. **Audit the `GSE63885` ROC Analysis and Fix the "Breast Cancer" Text Error:** Re-compute and report the true 1-, 2-, 3-, and 5-year time-dependent ROC AUCs for `GSE63885` (replacing the duplicated `GSE30161` numbers in line 94), and correct "breast cancer samples" to "ovarian cancer samples" in Methods line 32.
3. **Resolve the Inverted DEG Contrast in Figure 3A–B and Use Unpaired Statistical Tests:** Verify the contrast direction (`high-risk vs. low-risk`) in `DESeq2` so that the GO enrichment in Figure 3A–B is consistent with the GSEA/GSVA/ESTIMATE results in Figures 3C and 4A–C, and replace the paired Wilcoxon test in Figures 3D, 4C, and 4D with an unpaired two-sample Wilcoxon rank-sum test with Benjamini–Hochberg FDR correction.
