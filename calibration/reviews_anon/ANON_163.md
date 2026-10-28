# Forensic Scientific Peer Review: `ANON_163`

**Overall Score:** **6.6 / 10.0** (Mixed / Salvageable)
* **Score Breakdown:** Rigor: 1.9/3.5 | Claims: 1.5/2.5 | Biology: 1.6/2.0 | Reproducibility: 1.6/2.0

---

## 1. Executive Summary & Synthesis

This study investigates how the spatial localization of tertiary lymphoid structures (TLS)—categorized by H&E and multiplex immunohistochemistry (mIHC) into desert TLS (dTLS), peritumoral TLS (pTLS), and intratumoral TLS (iTLS)—shapes the tumor immune microenvironment (TIME) and clinical outcomes in gastric cancer (GC). The authors generate single-cell RNA-seq data from 25 GC patients ($N = 88,100$ cells after QC: 6 dTLS, 9 pTLS, 10 iTLS) and 10x Visium spatial transcriptomics (ST-seq) from 5 patients (1 dTLS, 2 pTLS, 2 iTLS), complemented by bulk RNA-seq/IHC prognostic cohorts ($n = 110$ surgery cohort) and an immunotherapy response evaluation. They report that iTLS tumors are enriched for germinal center B cells (GCBs), follicular dendritic cells (FDCs), $\text{CXCL13}^+\text{CD4}^+$ Tfh-like cells, $\text{CREM}^+\text{CD8}^+$ T cells, $\text{LAMP3}^+\text{CCR7}^+$ mature DCs, and $\text{ACKR1}^+$ high endothelial venules (HEVs), whereas dTLS/pTLS tumors are enriched for $\text{MMP11}^+$ myofibroblastic CAFs and $\text{SPP1}^+$ macrophages. They further perform an in vitro transwell assay with hiPSC-derived endothelial cells overexpressing `ACKR1` and propose a 26-gene signature (`ssTLS`) to predict survival and anti-PD-1 response.

The multi-omic dataset (25 scRNA-seq and 5 Visium samples raw data deposited in GSA-Human `HRA008025`) and the mIHC validations are substantial contributions. However, several statistical, experimental design, and documentation flaws weaken the strength of the mechanistic and clinical claims:
1. **Severe Pseudoreplication in Cell-Level and Spot-Level Hypothesis Tests:** Throughout the scRNA-seq and ST-seq analyses, statistical significance ($p < 0.0001$) between dTLS ($n=6$ patients), pTLS ($n=9$), and iTLS ($n=10$) is computed by treating thousands of individual cells ($N = 88,100$) or Visium spots (from $n = 1\text{--}2$ patients per group) as independent observations in Fisher's exact tests ($R_{o/e}$ heatmaps) and Wilcoxon rank-sum tests, without patient-level aggregation (pseudobulking) or mixed-effects modeling.
2. **Missing Wild-Type / Empty-Vector Control in the In Vitro `ACKR1` Assay (Figure 6j,k):** To test whether CXCL13 signals through ACKR1 on endothelial cells to upregulate VCAM1/ICAM1 and recruit T cells, the authors compare PBS vs. CXCL13 vs. TNF treatment exclusively on `ACKR1`-overexpressing endothelial cells (`ACKR1 OE EC`). Without an empty-vector (WT) or `ACKR1`-knockdown endothelial control treated with CXCL13, the experiment cannot establish that the CXCL13 response is mediated by ACKR1 rather than endogenous chemokine receptors.
3. **Discrepancies in the Immunotherapy Cohort ($n = 39$ vs. $n = 44$ vs. `PRJEB25780` vs. `TCGA`):** The Methods state that 39 GC patients receiving immunotherapy at the PLA General Hospital were enrolled, yet Figure 7d reports $n = 44$ (`NR, n = 33; R, n = 11`—matching the public Kim et al. 2018 pembrolizumab cohort `PRJEB25780`), and the Figure 7g caption erroneously labels the immunotherapy ROC curve (`AUC = 0.795`) as *"prediction of the sensitivity and specificity during immune therapy with the TCGA dataset"*.
4. **Internal Contradiction on Sample Size Calculation and Systematic Gene Symbol Misspellings:** In the same paragraph of the Methods ("Statistics and reproducibility"), the authors state both that *"No statistical methods were used to predetermine the sample size"* and that R package `pwr` was used *"for the sample size determination of patients to assess the role of TLS status on the prognosis of GC"*. In addition, canonical markers are repeatedly misspelled (`MS4A1` as `MASA1`, `ACKR1` as `ACRK1`, `CLDN3/4/7` as `CDLN3/4/7`, and `CCL19` as `CCL9`).

---

## 2. Claim-by-Claim Evaluation

* **Claim 1 (Results, lines 20–24; Figure 1c,d): "We found the TLS status was gradually evolved in the GC cohort, with approximately 38.2% dTLS, 35.5% pTLS, and 26.4% iTLS... patients with iTLS showing significantly optimal survival rates (OS, P = 0.0051; DFS, P = 0.0029), followed by those with pTLS, and the worst prognosis in patients with dTLS."** — `[Well Supported]`
  * **Evidence & Audit:** The histopathologic classification of $n = 110$ surgical GC cases (42 dTLS [38.2%], 39 pTLS [35.5%], 29 iTLS [26.4%]; Table 1) and the patient-level Kaplan-Meier log-rank tests (`OS P = 0.0051`, `DFS P = 0.0029`) are appropriately powered at the patient level and consistent across clinical endpoints.
* **Claim 2 (Results, lines 28–36, 54–78; Figures 1g, 3e, 3f, 4d, 4e, 5c, 5d, 6c, 6g): Cell-type tissue prevalence ($R_{o/e}$, Fisher's exact test `**** p < 0.0001`) and pathway/gene expression scores (Wilcoxon test) differ significantly across dTLS, pTLS, and iTLS.** — `[Fragile]`
  * **Evidence & Audit:** In all $R_{o/e}$ contingency tables (Figures 1g, 3e, 4d, 5c, 6c) and cell-level violin/boxplots (Figures 2g, 3f, 4e, 5d, 6g), the unit of statistical replication is the cell ($N = 88,100$) or spatial spot rather than the patient ($n = 6, 9, 10$ for scRNA-seq; $n = 1, 2, 2$ for ST-seq). For example, in Figure 2g (`TLS scores in each region of ST-seq, **** p < 0.0001`), spots are pooled from only 1 dTLS patient, 2 pTLS patients, and 2 iTLS patients. While several major cellular trends (such as $\text{CXCL13}^+\text{CD4}^+$ T cells, $\text{CREM}^+\text{CD8}^+$ T cells, $\text{LAMP3}^+\text{CCR7}^+$ DCs, and $\text{ACKR1}^+$ ECs) are independently corroborated by patient-level mIHC images and cell counts (Figures 4h, 5i, 6i), the nominal scRNA-seq and ST-seq $p$-values are severely inflated by pseudoreplication.
* **Claim 3 (Results, line 87; Figure 6j,k): "Using human induced pluripotent stem cell-derived endothelial cells (hiPSC-EC) that over-expressed ACKR1 (ACKR1 OE EC), our in vitro transwell experiments verified that CXCL13 could stimulate ACKR1+ ECs to express VCAM1 and ICAM1, thereby promoting T-cell migration and recruitment."** — `[Fragile]`
  * **Evidence & Audit:** In Figure 6k, all three treatment groups (`PBS`, `CXCL13`, `TNF`, $n = 4$ biological replicates) use `ACKR1 OE EC`. There is no control group of wild-type (empty-vector) hiPSC-ECs or `ACKR1`-knockout/knockdown ECs stimulated with CXCL13. Consequently, this design only shows that CXCL13 treatment of `ACKR1 OE EC` increases VCAM1/ICAM1 and T-cell migration relative to PBS; it does not prove that the effect is mediated by ACKR1. Furthermore, ACKR1 (Duffy antigen receptor for chemokines) lacks the canonical DRY motif required for G-protein signaling and functions primarily in chemokine transcytosis/scavenging rather than direct transcriptional activation of VCAM1/ICAM1, making an `ACKR1`-negative control essential to support a direct signaling claim.
* **Claim 4 (Results, line 95–97; Figure 7d–g): "We further examined the predictability of the ssTLS signature in the response to immunotherapy of GC patients... Patients with sensitive clinical responses... displayed a significantly elevated level of ssTLS signature (Fig. 7d), with the AUC value reaching 0.795 in the training cohort (Fig. 7g)."** — `[Overstated]`
  * **Evidence & Audit:** There are three major issues with this claim:
    1. **Cohort identity confusion:** The Methods ("Clinical cohorts") state that 39 GC patients receiving immunotherapy at the Chinese PLA General Hospital were enrolled to evaluate TLS via H&E staining, whereas the Methods ("Gene set scoring") and Data Availability state that bulk RNA-seq from the public Kim et al. 2018 cohort (`PRJEB25780`) was used. Figure 7d reports `NR, n = 33; R, n = 11` ($n = 44$, matching `PRJEB25780`), while the Figure 7g caption states *"during immune therapy with the TCGA dataset"* (TCGA STAD is not an immunotherapy-treated response cohort).
    2. **No independent test set:** Calling the cohort the "training cohort (Fig. 7g)" when there is no validation cohort for the `ssTLS` signature overstates generalizability.
    3. **Corrupted gene symbol in the signature definition:** Both the Results (line 94) and Methods ("Gene set scoring") list `MASA1` instead of the HUGO symbol `MS4A1` (CD20) among the 26 genes of `ssTLS`.

---

## 3. Technical & Methodological Critique

### 3.1 Pseudoreplication in Single-Cell and Spatial Transcriptomics
In multi-patient scRNA-seq ($n = 25$) and ST-seq ($n = 5$) studies, cells or spots from the same tumor biopsy share patient-level genetic, clinical, and batch effects. Applying Fisher's exact test to a contingency table of 88,100 cells (the $R_{o/e}$ plots in Figures 1g, 3e, 4d, 5c, 6c) or a two-sided Wilcoxon test across thousands of cells or Visium spots (Figures 2g, 3f, 4e, 5d, 6g) treats each cell/spot as an independent patient, inflating effective sample size from $n = 25$ (or $n = 5$) to $N = 88,100$. To test whether a cell subset proportion or pathway score differs across dTLS ($n=6$), pTLS ($n=9$), and iTLS ($n=10$), proportions and pseudobulk expression means must be aggregated per patient first and compared across the $n = 25$ patient-level summaries (e.g., via Kruskal-Wallis / Wilcoxon tests on patient proportions or `muscat` / `dream` mixed-effects models).

### 3.2 Contradictory Statistical Power Statements
In the Methods section ("Statistics and reproducibility"), the first sentence reads:
> *"No statistical methods were used to predetermine the sample size."*

Yet six lines later in the exact same paragraph, when listing software packages, the text reads:
> *"R packages included Seurat... pwr (for the sample size determination of patients to assess the role of TLS status on the prognosis of GC), Survminer..."*

These two statements directly contradict one another.

### 3.3 Gene Nomenclature Errors and Ligand-Receptor Mismatches
Multiple gene symbols and ligand-receptor pairs are misprinted across the text and figure legends:
* `MS4A1` (encoding B-cell marker CD20) is misspelled as `MASA1` in Results (line 94) and Methods ("Gene set scoring").
* `ACKR1` is misspelled as `ACRK1` in Results (line 83: *"notably in ACRK1+ ECs"*) and in the Figure 6g legend (line 89: *"particularly in ACRK1+ ECs"*).
* `CLDN3`, `CLDN4`, and `CLDN7` are misspelled as `CDLN3`, `CDLN4`, and `CDLN7` in Results (line 31).
* In Results (line 70), the chemokine `CCL19` is misspelled as `CCL9` (*"higher levels of chemokines CXCL16 and CCL9"*), and in the corresponding Figure 5g caption (line 76), the receptor pair for `CXCL16` and `CCL19` is misstated as `(CXCR5 and CCR7)` instead of `(CXCR6 and CCR7)` (even though the body text on line 70 correctly states *"their counter-receptors CXCR6 and CCR7"*).

### 3.4 Actionable Recommendations for Revision
1. **Perform Patient-Level (Pseudobulk) Hypothesis Testing:** Recompute the cell-type proportion comparisons across dTLS ($n=6$), pTLS ($n=9$), and iTLS ($n=10$) using patient-level cell-type fractions (Kruskal-Wallis / Wilcoxon rank-sum tests with $n = 6, 9, 10$ or Dirichlet-multinomial regression) and pseudobulk differential expression, reporting patient-level $p$-values alongside the $R_{o/e}$ descriptive heatmaps.
2. **Add an `ACKR1`-Negative Control to the Endothelial Assay:** Include wild-type (empty-vector) hiPSC-ECs (and/or `ACKR1` siRNA knockdown in `ACKR1 OE ECs`) treated with PBS vs. CXCL13 in Figure 6k to test whether VCAM1/ICAM1 induction and T-cell transwell migration specifically require ACKR1 expression.
3. **Clarify the Immunotherapy Datasets and Fix the Figure 7g Legend:** Clearly distinguish between the 39-patient in-house PLA General Hospital H&E cohort and the 44-patient public `PRJEB25780` RNA-seq cohort, correct the Figure 7g legend so it does not attribute the immunotherapy ROC curve to `TCGA`, and reconcile the contradictory `pwr` sample-size statement in the Methods.
4. **Correct Gene Symbols:** Fix `MASA1` $\to$ `MS4A1`, `ACRK1` $\to$ `ACKR1`, `CDLN3/4/7` $\to$ `CLDN3/4/7`, `CCL9` $\to$ `CCL19`, and `CXCR5` $\to$ `CXCR6` (in Figure 5g).
