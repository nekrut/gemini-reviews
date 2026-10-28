# Review of ANON_96

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **3.5 / 10.0** (Flawed / Overstated)  
* **Score Breakdown:** Rigor: 1.0/3.5 | Claims: 0.9/2.5 | Biology: 1.0/2.0 | Reproducibility: 0.6/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This study constructs a nine-gene cancer stem cell (CSC)-related prognostic signature for liver hepatocellular carcinoma (LIHC) using public bulk transcriptomic cohorts (TCGA-LIHC, $n = 357$ tumors and $44$ non-tumor controls; ICGC-LIRI-JP, $n = 113$ tumors), a sorafenib clinical trial microarray dataset (GSE109211, $n = 140$), and a single-cell RNA-seq dataset (GSE156625). Intersecting 3,630 TCGA-LIHC differentially expressed genes (DEGs) with ~657 CSC biomarkers from `BCSCdb` yields 206 `DE-BCSCs`, which are filtered via univariate Cox, LASSO, and multivariate Cox regression into a nine-gene risk score (`ADM`, `CCL5`, `CD274`, `DLGAP5`, `HOXD9`, `IGF1`, `SOCS2`, `TNFRSF11B`, and `S100A9`). The authors evaluate survival stratification in TCGA-LIHC and ICGC, build a clinical nomogram, and perform downstream GSEA, somatic mutation (`oncoplot`), `ESTIMATE`, `CIBERSORT`, `CellPhoneDB`/`LIANA`, and `oncoPredict` drug sensitivity analyses. Public accession numbers are cited, but no analysis scripts are provided.

Although multi-cohort validation (TCGA-LIHC and ICGC) is a positive feature of the design, the manuscript is compromised by pervasive internal contradictions, corrupted gene symbols in the single-cell section, incompatible ROC AUC values across figures for the same cohort, and conflicting statistical statements within the same paragraphs. Most glaringly, in Section 2.7 (line 109), six of the nine model genes are replaced by completely different or garbled gene names (`ADH1` for `ADM`, the non-existent symbol `DLSGPS` for `DLGAP5`, `ISG15` for `IGF1`, `TNFSF11` for `TNFRSF11B`, `SDC3` for `SOCS2`, and `ADO2` for `ACKR1`). Furthermore, Section 2.6 states both that resting CD4 memory T-cells are significantly elevated in the high-risk group and, four sentences later, that they are negatively correlated with the risk score; Section 2.2 claims a 3-year ROC AUC $> 0.82$ (Figure 2J) while Section 2.3 reports an AUC of $0.735$ (Figure 3D) in the same TCGA-LIHC cohort; and Section 2.8 states that sorafenib treatment shows no significant difference in model gene expression (Figure S2) whereas the Discussion claims the exact opposite. A comprehensive re-audit of the underlying R/Python outputs and text is required.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **The nine-gene BCSC signature (`ADM`, `CCL5`, `CD274`, `DLGAP5`, `HOXD9`, `IGF1`, `SOCS2`, `TNFRSF11B`, `S100A9`) achieves strong survival discrimination with a 3-year AUC $> 0.82$ across the LIHC cohort: [Fragile].**  
  First, the manuscript contradicts itself regarding how the risk coefficients were derived: Section 2.2 (line 42) states that LASSO was followed by multivariate Cox regression to obtain the nine genes and weights, whereas Section 4.3 (line 155) states that the risk model was constructed directly using LASSO coefficients. Second, the reported AUC in TCGA-LIHC is internally inconsistent: Section 2.2 (line 56, Figure 2J) states that the 3-year time-dependent ROC AUC is $> 0.82$, whereas Section 2.3 (line 61, Figure 3D) states that the risk score achieved an AUC of $0.735$. Third, although Section 4.4 (line 160) states that 1-, 3-, and 5-year time-dependent ROC AUCs were calculated for both TCGA and ICGC, no ROC curve or numerical AUC values are reported for the external ICGC validation cohort.

* **`CIBERSORT` deconvolution shows consistent immune infiltration differences between high- and low-risk groups, including resting CD4 memory T-cells: [Methodologically Flawed].**  
  Within a single paragraph in Section 2.6 (lines 94–102), the text first repeats a four-sentence block nearly verbatim claiming that *"The high-risk cohort contained significantly higher proportions of resting CD4 memory T-cells, follicular helper T-cells, M0 macrophages, and neutrophils"*, and then immediately states the opposite: *"Conversely, six TIC types—M1 Macrophages, resting Mast cells, resting NK cells, resting CD4 memory T-cells, CD8 T-cells, and gamma delta T-cells—showed a negative association with the risk signature."* A cell population cannot be significantly enriched in the high-risk group (median split of the risk score) while exhibiting a significant negative linear correlation with the same risk score without severe outlier distortion or a sign/labeling error. Moreover, the Figure 6C caption (line 100) states that the unpaired high-risk and low-risk patient groups were compared using the *Wilcoxon signed-rank test*, which is a paired test inapplicable to independent patient subgroups.

* **Single-cell RNA-seq (`GSE156625`) confirms the cell-type expression distribution of the nine model genes and `CCL5` receptor interactions: [Methodologically Flawed].**  
  In Section 2.7 (line 109), the authors state: *"Gene-expression analysis of key model genes, such as ADH1, CCL5, CD274, DLSGPS, HOXD9, ISG15, TNFSF11, S100A9, SDC3, SDC4, and ADO2, demonstrated variable expression patterns across different cell clusters (Figure 7 B,D)."* Five of the nine prognostic signature genes (`ADM`, `DLGAP5`, `IGF1`, `TNFRSF11B`, and `SOCS2`) have been substituted with unrelated or non-existent symbols (`ADH1`, `DLSGPS`, `ISG15`, `TNFSF11`, and `SDC3`), and the `CCL5` receptor `ACKR1` (line 109) is misprinted as `ADO2` in both line 109 and the Figure 7D caption (line 115). In addition, Section 4.1 (line 145) misdescribes `GSE109211` as a single-cell RNA-seq dataset alongside `GSE156625`.

* **Expression of the nine BCSC signature genes predicts clinical response to sorafenib in `GSE109211`: [Overstated].**  
  In Section 2.8 (line 120), the authors report that *"Patients treated with sorafenib showed no significant differences in the expression levels of these nine genes compared to those receiving a placebo treatment (Figure S2),"* and then state that lower `ADM`, `CCL5`, `DLGAP5`, and `SOCS2` and higher `CD274` and `HOXD9` were associated with "better treatment outcomes (Figure 8B)" without specifying whether Figure 8B analyzes the sorafenib arm, the placebo arm, or both pooled together. The Discussion (line 135) then directly contradicts Section 2.8 by claiming that *"genes associated with the CSC model showed significant expression differences in response to Sorafenib."*

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Audit and Correct the Corrupted Gene Symbols in Section 2.7 and Figure 7
* **WHY:** Reporting `ADH1`, `DLSGPS`, `ISG15`, `TNFSF11`, `SDC3`, and `ADO2` in Section 2.7 (line 109) when the prognostic signature consists of `ADM`, `DLGAP5`, `IGF1`, `TNFRSF11B`, and `SOCS2` (and the chemokine receptor is `ACKR1`) indicates either severe optical character recognition (OCR) corruption of figure labels or querying the wrong genes in the scRNA-seq dataset.
* **WHAT:** Verify which genes were actually plotted in Figure 7B–D in Python/`LIANA` and correct all gene symbols in the text and figure labels.
* **HOW:** Inspect the Python script used to generate Figure 7B–D from `GSE156625`. Ensure that the exact nine signature genes (`ADM`, `CCL5`, `CD274`, `DLGAP5`, `HOXD9`, `IGF1`, `SOCS2`, `TNFRSF11B`, `S100A9`) and the three `CCL5` receptors (`SDC1`, `SDC4`, `ACKR1`) are queried, regenerate Figure 7 if wrong genes were plotted, and replace `ADH1`, `DLSGPS`, `ISG15`, `TNFSF11`, `SDC3`, and `ADO2` in Section 2.7 and Figure 7D.

#### 2. Reconcile the Contradictory `CIBERSORT` Results and Statistical Tests in Section 2.6
* **WHY:** Resting CD4 memory T-cells cannot be both significantly higher in the high-risk group (Figure 6C) and negatively correlated with the risk score (Figure 6E), and unpaired patient groups cannot be tested with a paired Wilcoxon signed-rank test.
* **WHAT:** Re-compute the unpaired Wilcoxon rank-sum tests and Spearman/Pearson correlations for all 22 `CIBERSORT` cell types, remove the duplicated text block in Section 2.6, and apply multiple-testing correction (Benjamini–Hochberg FDR).
* **HOW:** Run `wilcox.test(fraction ~ risk_group, paired = FALSE)` and `cor.test(fraction, risk_score)` across all 22 `CIBERSORT` cell types in TCGA-LIHC, verify the sign of the difference and correlation for `T cells CD4 memory resting`, update Section 2.6 (lines 94–102) and Figure 6C caption to state "Wilcoxon rank-sum test," and delete the repeated paragraph text on lines 94–102.

#### 3. Resolve the TCGA-LIHC ROC AUC Discrepancy and Report ICGC Validation AUCs
* **WHY:** Figure 2J reports a 3-year ROC AUC $> 0.82$ in TCGA-LIHC, whereas Figure 3D reports an AUC of $0.735$ for the exact same risk score in TCGA-LIHC, and no ROC curve is shown for the external ICGC-LIRI-JP validation cohort.
* **WHAT:** Clarify the time horizon (1-, 3-, or 5-year) used in Figure 3D, explain why its AUC ($0.735$) differs from Figure 2J ($>0.82$), and add the 1-, 3-, and 5-year time-dependent ROC curves and 95% confidence intervals for the ICGC validation cohort.
* **HOW:** Using the `timeROC` package in R, compute 1-, 3-, and 5-year AUCs (with bootstrap 95% CIs) using the identical risk score formula in both TCGA-LIHC and ICGC-LIRI-JP, add the ICGC ROC panel to Figure 2, and state in Section 4.3 whether the final formula coefficients (`0.145 * ADM - 0.148 * CCL5 ...`) came from `glmnet` LASSO or `coxph` multivariable regression.

#### 4. Clarify the `GSE109211` Sorafenib vs. Placebo Stratification and Remove Contradictory Claims
* **WHY:** In `GSE109211` (the STORM trial), patients received either sorafenib or placebo. Pooling both arms or contradicting Section 2.8 (no difference between sorafenib and placebo) in the Discussion invalidates the claim of sorafenib-specific biomarker utility.
* **WHAT:** Restrict the responder vs. non-responder analysis in Figure 8B strictly to the sorafenib-treated arm of `GSE109211` (and show the placebo arm separately as a negative control), and align the Discussion with Section 2.8.
* **HOW:** Subset `GSE109211` metadata to sorafenib-treated patients ($n = 67$), compare the nine signature genes and the composite `BCSC score` between sorafenib responders and non-responders using Wilcoxon rank-sum tests with FDR adjustment, and remove the misstatement in Section 4.1 (line 145) calling `GSE109211` a single-cell RNA-seq dataset.

#### 5. Fix Broken Figure Cross-References and Truncated Statements
* **WHY:** Multiple figure panel callouts in the text and captions point to the wrong panels.
* **WHAT & HOW:**
  1. **Section 2.2 (line 42):** Change `"nine prognostic genes were identified: ... (Figure 3 G)"` to `"(Figure 2 G)"` (Figure 3G is the 5-year calibration curve).
  2. **Figure 5 caption (line 85):** Change `"(A, B) Oncoplots of genetic alterations in the low-risk group (E) and high-risk group (F)"` to `"low-risk group (A) and high-risk group (B)"`.
  3. **Discussion (line 135):** Change `"GSEA revealed that the differential genes between risk groups are mainly enriched in pathways... (Figure 6)"` to `"(Figure 4)"`.
  4. **Code availability:** Deposit the R and Python scripts used for the TCGA/ICGC/GSE156625 analyses in a public repository and include the link in the Data Availability Statement.
