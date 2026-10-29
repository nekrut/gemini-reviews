# Review of FEXP_ANON_087

**Overall Score:** **4.4 / 10.0** (Flawed / Overstated) | **Scientific Core Score:** **3.6 / 8.0**  
* **Score Breakdown:** Rigor: 1.3/3.5 | Claims: 1.1/2.5 | Biology: 1.2/2.0 | Reproducibility: 0.8/2.0

---

## 1. Blinded Metadata Perception

* **Perceived Role / Domain:** Translational cardiovascular bioinformatics and clinical biomarker validation study investigating peripheral blood mononuclear cell (PBMC) transcriptomic signatures (`CLU`, `FOS`, `CXCL8`) in heart failure following acute myocardial infarction (HFpAMI).
* **Blinded Document Assessment:** This manuscript combines a public microarray reanalysis (`GSE59867`) with a small single-center clinical validation cohort ($n = 18$ HFpAMI vs. $n = 9$ non-HF AMI controls) assayed by RNA-seq, RT-qPCR, and flow cytometry. While the inclusion of an independent clinical cohort with echocardiography (`LVEF`, `LVEDD`), `NT-proBNP`, RT-qPCR, and flow cytometry is a positive design element, the bioinformatics analysis suffers from unadjusted $P$-value screening, severe sex-chromosome confounding (`UTY`, `USP9Y`, `EIF1AY`), longitudinal sample selection ambiguity in `GSE59867`, overstatement of non-significant clinical immune findings ($P = 0.28$ for neutrophils, non-significant M2 macrophages), and failure to deposit the newly generated RNA-seq dataset.

---

## 2. Executive Summary & Editorial Verdict

The authors screen the `GSE59867` PBMC microarray dataset ($n = 30$ HFpAMI vs. $n = 34$ non-HF AMI samples) using `limma` (`|logFC| > 0.585`, unadjusted $P < 0.05$) to identify 27 DEGs. Intersecting PPI network clustering (MCODE) with three machine learning feature selectors (LASSO, SVM-RFE, and Random Forest) yields three upregulated candidate biomarkers (`CLU`, `FOS`, `CXCL8`). CIBERSORT deconvolution on `GSE59867` suggests elevated neutrophils and reduced naive $\text{CD4}^+$ T cells and naive B cells in HFpAMI. To validate these findings, the authors recruit 18 HFpAMI patients and 9 post-AMI patients without HF, performing whole-blood PAXgene RNA-seq, PBMC RT-qPCR (`CLU`, `FOS`, `CXCL8`, `TLR4`, `MYD88`), automated blood neutrophil counts, and PBMC flow cytometry ($\text{CD4}^+$ T, $\text{CD8}^+$ T, M1/M2 macrophages).

**Editorial Verdict: Reject / Major Re-analysis Required (Flawed / Overstated).** Although the clinical validation confirms higher `CLU`, `FOS`, and `CXCL8` mRNA levels in established HFpAMI patients compared to non-HF post-AMI patients, several major methodological flaws undermine the study:
1. **Unadjusted $P$-Value Screening and Uncontrolled Sex Confounding in `GSE59867`:** The 27 discovery DEGs were called using an unadjusted $P < 0.05$ cutoff across 28,869 genes. Because patient sex was not controlled for, male Y-chromosome genes (`EIF1AY`, `USP9Y`, `UTY`) dominated both the GO enrichment ("protein demethylation" / "MLL3/4 complex" driven by `UTY`) and the machine learning feature rankings (1 of 4 LASSO genes, 3 of 6 SVM-RFE genes, and 2 of 5 Random Forest genes are on the Y chromosome; line 163). Furthermore, `GSE59867` is a longitudinal cohort (4 time points per patient across 436 arrays), and the authors never specify which time points were selected to form the 30 vs. 34 comparison or whether repeated measures from the same patient were included.
2. **Contradiction Between Abstract Claims and Negative Flow Cytometry / Hematology Results:** The Abstract (line 9) claims that *"RT-qPCR and flow cytometry further corroborated these expression trends and their correlations with neutrophil infiltration, CD4T cells and M2 macrophage concentration reductio, aligning with bioinformatics predictions."* In the actual Results (line 211, Fig. 7F, L, M) and Discussion (chunk 2, line 5), neither clinical neutrophil counts ($P = 0.28$) nor flow-cytometric M1/M2 macrophage proportions differed significantly between HFpAMI and non-HF patients, and the correlation between `CXCL8` and neutrophil count was not statistically significant ($r = 0.45, p = 0.063$).
3. **Cross-Sectional Confounding with Established Heart Failure (`NT-proBNP`) Rather Than Early Prediction:** While the Introduction frames `CLU`, `FOS`, and `CXCL8` as biomarkers for *early prediction* of HF progression after AMI, the external clinical cohort sampled patients who already had overt heart failure (`LVEF` $39.17 \pm 6.63\%$ vs. $61.33 \pm 3.77\%$; median `NT-proBNP` $1,149.5$ vs. $114.7\text{ pg/ml}$, $P < 0.001$; Table 2), where `NT-proBNP` and `LVEF` already separate the two groups almost completely.

### Specific Conclusions and Assessment of Support

* **Identification of 27 HFpAMI-related DEGs and three ML consensus biomarkers (`CLU`, `FOS`, `CXCL8`) in `GSE59867`: [Fragile].**  
  Using an unadjusted $P < 0.05$ cutoff in `limma` without FDR correction (line 38) and without adjusting for sex allowed Y-chromosome genes (`EIF1AY`, `USP9Y`, `UTY`) to account for half of the top ML features (line 163). In addition, the three ML algorithms (LASSO, SVM-RFE, RF) were fit on the 27 pre-selected DEGs across the same 64 samples used for DEG discovery, introducing feature-selection circularity into the `GSE59867` ROC AUCs (Fig. 4D–F).
* **Upregulation of `CLU`, `FOS`, and `CXCL8` (and `TLR4`/`MYD88`) in the external clinical HFpAMI cohort ($n = 18$ vs. $n = 9$): [Moderately Supported].**  
  Consistent upregulation of `CLU`, `FOS`, and `CXCL8` is observed in both whole-blood RNA-seq (`DESeq2` adjusted $P < 0.05$, Fig. 6D–F) and PBMC RT-qPCR ($P < 0.01$, Fig. 7A–C), and `CLU`/`CXCL8` correlate with `NT-proBNP`, `LVEDD`, and `LVEF` (Fig. 9). However, the cohort is small ($n = 27$ total), cross-sectional (established HF rather than prospective pre-HF baseline), and compares whole-blood PAXgene RNA-seq against Ficoll-isolated PBMC microarrays/qPCR.
* **Dysregulated neutrophil and M2 macrophage infiltration corroborated by clinical blood counts and flow cytometry: [Overstated].**  
  In the clinical cohort, blood neutrophil counts did not differ significantly between groups ($P = 0.28$, Fig. 7F), flow-cytometric M2 macrophage fractions did not differ significantly between groups (Fig. 7M; Discussion line 5 of chunk 2), and the `CXCL8`–neutrophil correlation had $p = 0.063$ (yet is called "a significant positive correlation" in line 211). Moreover, Ficoll-isolated PBMCs exclude mature neutrophils by density centrifugation, so CIBERSORT "neutrophil" signals in `GSE59867` reflect low-density granulocyte contamination or myeloid transcriptional overlap.

---

## 3. Forensic Defect Inventory

1. **Uncontrolled Sex Confounding Driving Y-Chromosome Feature Selection and GO Enrichment in `GSE59867` (Pillar 2 & Pillar 3):**
   * **Location:** Results ("Functional enrichment analysis of DEGs", line 153; "PPI network and candidate biomarkers selection", line 163, Figure 3C–E).
   * **Defect:** Half of the genes selected by SVM-RFE (`USP9Y`, `UTY`, `EIF1AY`) and two of the five genes selected by Random Forest (`UTY`, `USP9Y`) are located on the male-specific Y chromosome, and the top GO biological process/cellular component terms ("protein demethylation," "MLL3/4 complex," "protein demethylase activity," line 153) are driven by the Y-linked histone demethylase `UTY`. This indicates an unadjusted sex imbalance between the 30 HFpAMI and 34 non-HF arrays selected from `GSE59867`.
2. **Unspecified Longitudinal Sampling From `GSE59867` and Unadjusted $P < 0.05$ Cutoff (Pillar 2 & Pillar 4):**
   * **Location:** Methods ("Data collection and quality control", line 33; "DEGs screening", line 38).
   * **Defect:** `GSE59867` is a longitudinal study profiling 111 AMI patients at four time points (admission, discharge, 1 month, and 6 months post-AMI; 436 samples total). The authors state only that the final dataset included *"64 PBMCs samples from AMI patients with or without HF development during a 6-month follow-up (HFpAMI, n = 30 vs. non-HF, n = 34)"* without specifying which time point(s) were extracted or whether multiple time points from the same individual were included as independent observations. Furthermore, DEGs were screened at raw $P < 0.05$ without Benjamini–Hochberg correction.
3. **Inappropriate Application of `voom` Normalization to Microarray Data for CIBERSORT (Pillar 3):**
   * **Location:** Methods ("Immune infiltration analysis", line 58).
   * **Defect:** Line 58 states that `GSE59867` microarray data *"were normalized using the 'voom' method to adjust for sequencing depth and variance"* before running CIBERSORT. `limma::voom` models mean–variance relationships in RNA-seq read counts ("sequencing depth"), not Affymetrix Human Gene 1.0 ST microarrays, and CIBERSORT requires anti-logged (linear-scale) expression values rather than log-CPM `voom` weights.
4. **Overstatement of Non-Significant Clinical Validation Results and $p = 0.063$ Correlation (Pillar 1 & Pillar 4):**
   * **Location:** Abstract (line 9) and Results ("Validation of the expression pattern...", line 211, Figures 7F, 7M, 8F).
   * **Defect:** The Abstract claims flow cytometry and clinical tests corroborated neutrophil infiltration and M2 macrophage reduction, whereas Results line 211 shows neutrophil counts were non-significant ($P = 0.28$) and M2 macrophages showed no significant difference between groups. Line 211 also describes `CXCL8` vs. neutrophil count ($r = 0.45, p = 0.063$) as a *"significant positive correlation"* despite $p > 0.05$.
5. **Compartment Mismatch Between Whole-Blood PAXgene RNA-seq and PBMC Microarray/qPCR (Pillar 2 & Pillar 6):**
   * **Location:** Methods ("Sample collection and RNA extraction", line 91 vs. "PBMCs isolation...", line 106).
   * **Defect:** The external RNA-seq was performed on whole venous blood collected in PAXgene tubes (which contains ~60–70% neutrophils and abundant erythrocyte transcripts), whereas `GSE59867` and the RT-qPCR validation were performed on Ficoll-isolated PBMCs (monocytes and lymphocytes depleted of neutrophils). In addition, Table 2 (line 195) mislabels the units of BMI as `kg/cm^2` instead of `kg/m^2`, and Figure 3A text vs. caption disagree on the PPI edge count (`27 edges` in line 158 vs. `25 edges` in line 161).
6. **Missing Repository Accession for Newly Generated Human RNA-seq Data (Pillar 7):**
   * **Location:** Data Availability Statement (chunk 2, lines 24 and 40).
   * **Defect:** The Data Availability Statement retains the journal template placeholder (*"The names of the repository/repositories and accession number(s) can be found in the article/Supplementary Material"*), and no GEO/SRA/GSA accession number is provided for the 27-patient clinical RNA-seq cohort.

---

## 4. Quantitative Rubric Scoring

| Rubric Dimension | Score | Max | Forensic Justification |
| :--- | :---: | :---: | :--- |
| **1. Methodological & Statistical Rigor** | **1.3** | **3.5** | Unadjusted $P < 0.05$ microarray DEG screen; uncontrolled sex confounding yielding Y-chromosome ML hits; unspecified time-point selection in longitudinal `GSE59867`; `voom` applied to microarray data; unadjusted correlations. |
| **2. Claim-to-Evidence Alignment** | **1.1** | **2.5** | Abstract overstates non-significant neutrophil ($P=0.28$) and M2 macrophage flow cytometry results as corroboration; cross-sectional comparison of overt HF (`LVEF` 39%) framed as early prediction of HF progression; $p=0.063$ called significant. |
| **3. Data Integrity & Biological Plausibility** | **1.2** | **2.0** | Real clinical cohort ($n=27$) with echo, `NT-proBNP`, qPCR, and flow cytometry, but mixes whole-blood PAXgene RNA-seq with Ficoll PBMC assays and misinterprets CIBERSORT neutrophils in neutrophil-depleted PBMCs. |
| **4. Reproducibility & Data Integrity** | **0.8** | **2.0** | Primer sequences and clinical baseline table are provided, but the newly sequenced 27-patient RNA-seq dataset has no repository accession number (template placeholder left in Data Availability) and no code is shared. |
| **Scientific Core Score** | **3.6** | **8.0** | Sum of Rigor + Claims + Biology. |
| **Total Composite Score** | **4.4** | **10.0** | **Flawed / Overstated** |

---

### 5. Constructive and Doable Suggestions for Improvement

1. **Control for Patient Sex and Specify Time Points in `GSE59867`:** Document exactly which single time point (e.g., admission or discharge) was extracted for each unique patient in `GSE59867` so that no patient is represented more than once, include sex as a covariate in `limma` (`~ group + sex`) or exclude sex-chromosome probes prior to ML feature selection, and report Benjamini–Hochberg FDR-adjusted $q$-values.
2. **Align Abstract and Text with Actual Flow Cytometry and Neutrophil Findings:** Revise the Abstract and Results to state accurately that peripheral neutrophil counts ($P = 0.28$) and M2 macrophage proportions did not differ significantly between HFpAMI and non-HF groups in the validation cohort, and correct the description of $r = 0.45, p = 0.063$ from "significant" to "a non-significant positive trend."
3. **Evaluate Incremental Predictive Value Beyond `NT-proBNP` and `LVEF`:** Because `NT-proBNP` ($1,149.5$ vs. $114.7\text{ pg/ml}$) and `LVEF` ($39.2\%$ vs. $61.3\%$) already separate the two clinical groups, fit a multivariable logistic regression testing whether `CLU`, `FOS`, or `CXCL8` adds statistically significant discrimination over `NT-proBNP` alone, and temper claims regarding "early prediction" prior to HF onset.
4. **Deposit the Clinical RNA-seq Data and Analysis Code:** Upload the 27-sample PAXgene RNA-seq count matrix and FASTQ/BAM files to NCBI GEO/SRA or NGDC GSA and insert the accession number into the Data Availability Statement.
