# Review of FEXP_ANON_082

**Overall Score:** **2.6 / 10.0** (Fundamentally Invalid) | **Scientific Core Score:** **2.1 / 8.0**  
* **Score Breakdown:** Rigor: 0.7/3.5 | Claims: 0.6/2.5 | Biology: 0.8/2.0 | Reproducibility: 0.5/2.0

---

## 1. Blinded Metadata Perception

* **Perceived Role / Domain:** Bioinformatics and single-cell/bulk transcriptomic prognostic signature study in hepatocellular carcinoma (HCC) using public GEO (`GSE149614`, `GSE25097`) and TCGA-LIHC datasets.
* **Blinded Document Assessment:** This is a template single-cell + TCGA LASSO prognostic signature manuscript exhibiting severe biological misannotations (`APOA2` hepatocyte marker used to define "effector memory CD4+ T cells"; macrophage markers `MARCO`, `LYZ`, and `SPP1` labeled as "T cell-related prognostic genes"), biologically impossible developmental trajectories (NK cells differentiating into $\text{CD4}^+$ and $\text{CD8}^+$ memory T cells), phantom methods claimed in the text (`SCENIC` transcription factor networks) that were never executed, and mathematically impossible Cox regression confidence intervals.

---

## 2. Executive Summary & Editorial Verdict

The authors analyze 53,477 single cells from eight primary HCC tumors and seven normal liver samples (`GSE149614`), extract 12,333 putative T cells, and re-cluster them into three subpopulations: 6,314 NK (or NKT) cells, 5,199 effector memory $\text{CD4}^+$ T cells, and 820 central memory $\text{CD8}^+$ T cells. Using CellChat and Monocle2, they model intercellular signaling and T-cell differentiation trajectories. They then intersect 1,169 single-cell DEGs with 1,629 bulk DEGs from `TCGA-LIHC` ($n = 231$ tumors, $n = 50$ normals) to obtain 21 overlapping genes, apply LASSO regression to select a six-gene prognostic signature (`LYZ`, `SPP1`, `EGR1`, `MARCO`, `FCN3`, `PTTG1`), evaluate survival prediction in `TCGA-LIHC` and `GSE25097` ($n = 221$), and perform Cox regression and CIBERSORT/ESTIMATE immune deconvolution.

**Editorial Verdict: Reject (Fundamentally Invalid).** The study's biological premises and statistical results collapse under forensic inspection. First, the putative "T cell" compartment and its derived signature are heavily confounded by non-T-cell contamination and misannotation: in Figure 2C–D (line 36), the authors identify the hepatocyte-specific apolipoprotein gene `APOA2` (which they themselves used in Figure 1D/F/G as the canonical marker of hepatocytes) as the defining marker gene for "effector memory $\text{CD4}^+$ T cells," and the ribosomal housekeeping gene `RPL17` as the marker for "central memory $\text{CD8}^+$ T cells." Consequently, the six "T cell-related prognostic signature genes" (`LYZ`, `SPP1`, `MARCO`, `FCN3`, `EGR1`, `PTTG1`) are predominantly myeloid/macrophage (`LYZ`, `MARCO`, `SPP1`) and endothelial (`FCN3`) markers, as confirmed by the authors' own Bubble Plot (Figure 6A) and Discussion. Second, the Monocle2 pseudotime analysis (Figure 4C–D) models NK cells differentiating along two branches into $\text{CD4}^+$ effector memory and $\text{CD8}^+$ central memory T cells, violating fundamental hematopoietic lineage biology. Third, the Multivariate Cox regression reports mathematically impossible 95% confidence intervals and $p$-values (e.g., M stage $\text{HR} = 3.005, 95\%\text{ CI} = 0.890\text{--}4.141, p < 0.05$, which includes the null value $\text{HR} = 1.0$ and is asymmetric on the log scale), while the LASSO model achieves an $\text{AUC} \approx 0.60$ (barely above a coin toss) that is overstated as "robust predictive performance."

### Specific Conclusions and Assessment of Support

* **Single-cell reclustering of 12,333 T cells into NK/NKT cells (`CMC1`), effector memory $\text{CD4}^+$ T cells (`APOA2`), and central memory $\text{CD8}^+$ T cells (`RPL17`): [Methodologically Flawed].**  
  `APOA2` encodes apolipoprotein A-II, a liver-specific hepatocyte secreted protein that the authors themselves used to annotate hepatocytes in Figure 1D ("APOA2-high hepatocytes"). Its prominence as the top marker of 5,199 "effector memory $\text{CD4}^+$ T cells" demonstrates unremoved hepatocyte doublets or severe ambient RNA contamination in `GSE149614` combined with flawed `SingleR` automated annotation. Additionally, the 6,314 cells are inconsistently labeled as "NK T cells" in the Abstract/Discussion (lines 9, 87) and "NK cells" in the Results/Figures (line 36, Fig. 2B).
* **Monocle2 trajectory showing NK cells at the early differentiation stage giving rise to effector memory $\text{CD4}^+$ and central memory $\text{CD8}^+$ T cells at terminal stages: [Methodologically Flawed].**  
  Innate NK cells do not differentiate into adaptive MHC-II-restricted $\text{CD4}^+$ T cells or MHC-I-restricted $\text{CD8}^+$ T cells. Feeding distinct lymphoid lineages (contaminated with hepatocyte ambient RNA) into Monocle2 forces an artificial branching tree that reflects transcriptional dissimilarity rather than ontogeny.
* **Identification of six "T cell-related" prognostic biomarkers (`LYZ`, `SPP1`, `EGR1`, `MARCO`, `FCN3`, `PTTG1`) with "robust predictive performance": [Overstated].**  
  `LYZ`, `SPP1`, and `MARCO` are canonical macrophage/monocyte markers and `FCN3` is a hepatic endothelial lectin; Figure 6A shows that these genes are minimally expressed in T cells compared to myeloid/endothelial compartments. Furthermore, the time-dependent ROC curves in both training and validation cohorts yield $\text{AUC} \approx 0.6$ (line 60: *"AUC ≈ 0.6 in both the training and testing sets"*), which represents poor discrimination, not "robust predictive performance."
* **Multivariate Cox regression confirming tumor stage, T stage, M stage, and risk score as independent prognostic factors: [Methodologically Flawed].**  
  In Results line 71, multivariate M stage is reported as $\text{HR} = 3.005, 95\%\text{ CI} = 0.890\text{--}4.141, p < 0.05$. A 95% confidence interval spanning $1.0$ ($0.890$ to $4.141$) cannot have $p < 0.05$, and the interval bounds are not symmetric around $\ln(\text{HR})$ ($\sqrt{0.890 \times 4.141} = 1.920 \ne 3.005$).
* **Transcription factor regulatory network analysis via SCENIC and immune profiling via ssGSEA: [Methodologically Flawed].**  
  The Introduction (line 20) and Conclusion (line 100) claim the authors analyzed T-cell subtypes using `SCENIC` to uncover *"transcription factor regulatory networks,"* yet `SCENIC` is completely absent from the Methods, Results, and Figures. Likewise, line 79 attributes the 22 CIBERSORT LM22 cell fractions (e.g., M0/M1/M2 macrophages, resting mast cells) to "ssGSEA analysis."

---

## 3. Forensic Defect Inventory

1. **Severe Ambient RNA / Doublet Contamination and Misannotation of T-Cell Subsets (Pillar 2 & Pillar 6):**
   * **Location:** Results ("Single-cell atlas of liver cancer", line 28 vs. "Single-cell atlas and enrichment analysis of T cells", line 36, Fig. 2C–D).
   * **Defect:** No doublet detection tool (`DoubletFinder`, `Scrublet`) or ambient RNA correction (`SoupX`, `DecontX`) was applied during QC (Methods line 108). When 12,333 "T cells" were subsetted and re-clustered, 5,199 cells were annotated as "effector memory $\text{CD4}^+$ T cells" based on high expression of `APOA2` (a hepatocyte marker from Fig. 1F), and 820 cells as "central memory $\text{CD8}^+$ T cells" based on `RPL17` (a ribosomal subunit). Furthermore, the remaining 6,314 cells are called "NK T cells" in lines 9 and 87 but "NK cells" in line 36 and Fig. 2B.
2. **Myeloid and Endothelial Genes Mischaracterized as "T Cell-Related" Signature Genes (Pillar 1 & Pillar 3):**
   * **Location:** Results (line 60, Fig. 5A, Fig. 6A), Discussion (line 91), and Methods (line 125).
   * **Defect:** Because `FindAllMarkers` (`|log2FC| > 2`, adjusted $p < 0.05$) was run across all single-cell clusters without restricting to genes positively enriched and specifically expressed inside verified T cells, the intersection with `TCGA-LIHC` DEGs selected `LYZ`, `SPP1`, `MARCO` (macrophage markers), and `FCN3` (endothelial marker). Figure 6A visually confirms that these genes are predominantly expressed in macrophages, monocytes, hepatocytes, and endothelial cells rather than T cells.
3. **Biologically Invalid Monocle2 Developmental Trajectory (Pillar 3 & Pillar 6):**
   * **Location:** Results ("T cell trajectory analysis", line 52, Fig. 4A–E).
   * **Defect:** The authors run Monocle2 across NK cells, $\text{CD4}^+$ T cells, and $\text{CD8}^+$ T cells, concluding that NK cells represent the early progenitor state that differentiates into terminal $\text{CD4}^+$ effector memory and $\text{CD8}^+$ central memory T cells (line 52). NK cells and $\text{CD4}^+/\text{CD8}^+$ $\alpha\beta$ T cells diverge during early thymic/lymphoid hematopoiesis and do not transdifferentiate in adult liver tumors.
4. **Mathematically Impossible Confidence Intervals and $P$-Values in Cox Regression (Pillar 4 & Pillar 7):**
   * **Location:** Results ("Clinical correlation analysis", line 71, Fig. 7A–B).
   * **Defect:** In multivariate Cox regression (line 71), M stage is reported as $\text{HR} = 3.005$ with $95\%\text{ CI} = 0.890\text{--}4.141$ and $p < 0.05$. First, a 95% CI that crosses $1.0$ ($0.890 < 1.0$) corresponds to $p > 0.05$ ($p \approx 0.10$), contradicting $p < 0.05$. Second, standard Cox proportional hazards CIs are $\exp(\hat{\beta} \pm 1.96\,\text{SE})$, requiring the geometric mean of the lower and upper bounds to equal the HR; instead, $\sqrt{0.890 \times 4.141} = 1.920 \ne 3.005$. Similar arithmetic failures occur for multivariate T stage ($\text{HR} = 2.594$, CI $2.013\text{--}3.911 \implies \text{geometric mean } 2.806$) and univariate risk score ($\text{HR} = 2.337$, CI $1.799\text{--}3.306 \implies \text{geometric mean } 2.439$). In addition, staging covariates (`pathologic stage`, `T stage`, `N stage`, `M stage`) are collinear because pathologic stage is a deterministic composite of T, N, and M stages.
5. **Unreported LASSO Coefficients and Refitting Ambiguity (Pillar 3 & Pillar 7):**
   * **Location:** Methods ("Lasso regression analysis", line 145) and Results (line 60).
   * **Defect:** Methods line 145 states *"Both the construction and validation of the model employed the Least Absolute Shrinkage and Selection Operator (LASSO) method,"* suggesting the model or median cutoff was refit on `GSE25097` rather than applying locked training weights. Worse, the explicit linear predictor formula (regression weights $\beta_i$ for `LYZ`, `SPP1`, `EGR1`, `MARCO`, `FCN3`, `PTTG1`) is omitted from the manuscript, making external validation impossible to reproduce.
6. **Phantom `SCENIC` Analysis and `ssGSEA` / `CIBERSORT` Confusion (Pillar 7):**
   * **Location:** Introduction (line 20), Results (line 79), and Conclusion (line 100).
   * **Defect:** The Introduction and Conclusion state that `SCENIC` transcription factor network analysis was performed on T-cell subtypes, but no such analysis exists in the paper. In Results line 79, CIBERSORT LM22 deconvolution results are misdescribed as "ssGSEA analysis."

---

## 4. Quantitative Rubric Scoring

| Rubric Dimension | Score | Max | Forensic Justification |
| :--- | :---: | :---: | :--- |
| **1. Methodological & Statistical Rigor** | **0.7** | **3.5** | Mathematically impossible Cox regression CIs and $p$-values; collinear TNM + Pathologic Stage in multivariate Cox; Monocle2 applied across NK and $\text{CD4}^+/\text{CD8}^+$ T cells; LASSO weights omitted. |
| **2. Claim-to-Evidence Alignment** | **0.6** | **2.5** | "Robust predictive performance" claimed for $\text{AUC} \approx 0.60$; macrophage/endothelial markers (`MARCO`, `LYZ`, `SPP1`, `FCN3`) claimed as T-cell prognostic biomarkers; unexecuted `SCENIC` analysis claimed in Introduction and Conclusion. |
| **3. Data Integrity & Biological Plausibility** | **0.8** | **2.0** | Hepatocyte marker `APOA2` used to define effector memory $\text{CD4}^+$ T cells due to unremoved ambient RNA/doublets; biologically impossible NK-to-T-cell differentiation trajectory. |
| **4. Reproducibility & Data Integrity** | **0.5** | **2.0** | Public accessions (`GSE149614`, `GSE25097`, `TCGA-LIHC`) are cited, but no code is provided, the 6-gene risk score formula is missing, and text descriptions (`SCENIC`, `ssGSEA`, NK vs. NKT) contradict the figures and methods. |
| **Scientific Core Score** | **2.1** | **8.0** | Sum of Rigor + Claims + Biology. |
| **Total Composite Score** | **2.6** | **10.0** | **Fundamentally Invalid** |

---

### 5. Constructive and Doable Suggestions for Improvement

1. **Remove Doublets/Ambient RNA and Re-annotate T-Cell Subsets Using Canonical Markers:** Run `SoupX`/`DecontX` and `DoubletFinder` on `GSE149614` to remove hepatocyte ambient RNA (`APOA2`, `ALB`, `APOA1`), and annotate T/NK subsets using canonical lineage markers (`CD3D`, `CD3E`, `CD4`, `CD8A`, `CCR7`, `SELL`, `GZMB`, `NCAM1`/`FCGR3A`) rather than automated `SingleR` correlations that misassign `APOA2`-high cells as $\text{CD4}^+$ T cells.
2. **Restrict Pseudotime Trajectory Inference to Homogeneous Lineages:** Exclude NK cells before running Monocle2, and analyze $\text{CD8}^+$ T-cell activation/exhaustion and $\text{CD4}^+$ T-cell differentiation separately.
3. **Select Truly T-Cell-Intrinsic Genes for Prognostic Modeling:** Filter candidate genes to those with significant positive log-fold enrichment (`log2FC > 1`) and expression in $\ge 25\%$ of verified T cells, preventing macrophage (`MARCO`, `LYZ`, `SPP1`) and endothelial (`FCN3`) markers from dominating the signature.
4. **Audit Cox Regression Models and Report the Exact Risk Score Formula:** Re-compute univariate and multivariate Cox proportional hazards models in R (`survival::coxph`), remove collinear composite `pathologic stage` when individual `T`, `N`, and `M` stages are included, verify that $\exp(\hat{\beta} \pm 1.96\,\text{SE})$ matches all reported HRs and $p$-values, and publish the exact LASSO coefficients $\beta_i$.
5. **Remove Phantom Method Claims:** Delete references to `SCENIC` and transcription factor regulatory networks in the Introduction and Conclusion (or include the actual SCENIC regulon analysis), and correct "ssGSEA" to "CIBERSORT" in Results line 79.
