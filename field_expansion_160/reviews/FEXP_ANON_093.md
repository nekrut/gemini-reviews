# Forensic Peer Review: FEXP_ANON_093

**Overall Score:** **3.3 / 10.0** (Flawed / Overstated) | **Scientific Core Score:** **2.4 / 8.0**
* **Score Breakdown:** Rigor: 0.8/3.5 | Claims: 0.8/2.5 | Biology: 0.8/2.0 | Reproducibility: 0.9/2.0

---

## 1. Blinded Metadata Perception
* **Perceived Study Type:** Multi-cohort bioinformatic diagnostic signature study integrating scRNA-seq (`GSE167363`), four bulk whole-blood transcriptomic cohorts (`GSE65682`, `GSE26440`, `GSE95233`, `GSE26378`), four machine learning algorithms (`RF`, `SVM`, `XGB`, `GLM`), and Western blot protein verification (`n = 6` per group) in human sepsis.
* **Perceived Subfield:** Sepsis Immunology / Translational Bioinformatics / Single-Cell Transcriptomics.
* **Tier Classification:** Flawed / Overstated (3.0–4.9).

---

## 2. Executive Summary & Editorial Verdict
This manuscript attempts to identify key genes regulating "apoptosis in classical monocytes during sepsis" by combining a peripheral blood single-cell RNA-seq dataset (`GSE167363`, `n = 12` samples) with four public bulk whole-blood gene expression cohorts (`GSE65682` as the training cohort and `GSE26440`, `GSE95233`, and `GSE26378` as validation cohorts), followed by machine learning feature selection (`RF`, `SVM`, `XGB`, `GLM`) and Western blot assay of four selected proteins (`G0S2`, `GZMA`, `ITM2A`, `PAG1`) in peripheral blood samples from 6 sepsis patients and 6 healthy controls.

Forensic audit reveals four severe methodological and biological defects that invalidate the central conclusions:
1. **Vacuous GeneCards "Apoptosis" Filtering ($21,896$ Genes):** To define "apoptosis-related genes," the authors queried GeneCards with the keyword `"apoptosis"` and retrieved **`21,896` genes** without applying any relevance score threshold (Methods lines 51–53; Results lines 127–131). Because the entire human genome contains only $\sim 20,000$ protein-coding genes, intersecting candidate differentially expressed genes (DEGs) with a list of $21,896$ GeneCards entries is a mathematically vacuous filter that labels almost any human gene as "apoptosis-related."
2. **Test-Set Data Leakage Prior to Machine Learning Feature Selection:** Before training the four machine learning classifiers (`RF`, `SVM`, `XGB`, `GLM`) on `GSE65682`, the authors first screened all four bulk cohorts (`GSE65682`, `GSE26440`, `GSE95233`, and `GSE26378`) for differentially expressed genes (`|log2FC| > 0.5`, adjusted `p < 0.05`) and intersected them with the `GSE167363` classical monocyte DEGs and GeneCards to obtain `40` consensus genes (lines 127–131, Figure 3A). Because the three external "validation" cohorts (`GSE26440`, `GSE95233`, `GSE26378`) were directly used to select the 40 input features, they are no longer independent validation sets; evaluating diagnostic ROC curves on those same three cohorts (Figure 5A–C) constitutes textbook test-set feature-selection leakage.
3. **Severe Classifier Overfitting (`AUC = 1.000` in Training):** In the training cohort (`GSE65682`, `n = 802`), three of the four machine learning classifiers (`RF`, `SVM`, and `XGB`) achieved an exact `AUC = 1.000` (`GLM AUC = 0.997`, Figure 3D) without any reported hyperparameter tuning, regularization constraints, or out-of-fold cross-validation separation for the ROC curves, demonstrating evaluation of resubstitution (in-sample training) predictions.
4. **Lineage Confounding Between Bulk Whole Blood and Classical Monocytes (`GZMA`, `ITM2A`):** Three of the four selected signature genes (`GZMA`, `ITM2A`, and `PAG1`) are not intrinsic regulators of classical monocyte apoptosis. `GZMA` (Granzyme A) and `ITM2A` are canonical cytotoxic T-cell and NK-cell markers; their marked downregulation in bulk whole-blood sepsis transcriptomes (`GSE65682`, `GSE26440`, `GSE95233`, `GSE26378`) and unfractionated peripheral blood Western blots (Figure 7) reflects well-known sepsis-induced lymphopenia (depletion of circulating T and NK cells relative to neutrophilia/monocytosis), which the authors misattribute to classical monocyte apoptosis.

### Specific Conclusions and Assessment of Support
* **Claim 1:** Intersecting DEGs with `21,896` GeneCards entries specifically isolates "apoptosis-related genes" in classical monocytes (`40` intersecting genes). — `[Methodologically Flawed]` (A list of `21,896` GeneCards genes encompasses virtually the entire human protein-coding genome; the intersection provides near-zero specificity for apoptosis pathways.)
* **Claim 2:** `G0S2`, `GZMA`, `ITM2A`, and `PAG1` are core hub genes regulating classical monocyte apoptosis during sepsis. — `[Methodologically Flawed]` (`GZMA` and `ITM2A` are canonical cytotoxic lymphocyte [CD8+ T/NK cell] genes whose apparent expression in classical monocytes in `GSE167363` reflects ambient RNA/doublet contamination, and whose downregulation in bulk blood reflects sepsis lymphopenia rather than monocyte apoptosis.)
* **Claim 3:** Machine learning models (`RF`, `SVM`, `XGB`, `GLM`) achieve `AUC = 0.997–1.000` in `GSE65682`, and the 4-gene nomogram achieves `AUC = 0.962–0.996` across three independent external validation cohorts (`GSE26440`, `GSE95233`, `GSE26378`). — `[Overstated]` (The `1.000` training AUCs reflect in-sample resubstitution on `GSE65682`, and the three "external validation" cohorts were already used to filter the 40 candidate DEGs prior to machine learning.)
* **Claim 4:** Western blot analysis of peripheral blood from 6 sepsis patients and 6 healthy controls confirms upregulated `G0S2` and `PAG1` and downregulated `GZMA` and `ITM2A` in classical monocytes. — `[Fragile]` (Western blotting was performed on whole peripheral blood lysates rather than isolated CD14+ classical monocytes, confounding cell-type abundance shifts [neutrophilia and lymphopenia] with per-cell protein regulation.)

---

## 3. Forensic Defect Inventory

### Defect 1: Vacuous GeneCards "Apoptosis" Gene Set ($21,896$ Genes)
* **Location:** Section 2.1 (`Data download and processing`, lines 51–53) and Section 3.3 (`Identification of candidate apoptosis-related genes`, lines 127–131; Figure 3A).
* **Audit Finding:** The authors state: *"The keyword 'apoptosis' was used to search the GeneCards database (https://www.genecards.org/), resulting in the retrieval of 21,896 apoptosis-related genes."* In the Venn diagram (Figure 3A), the intersection of `GSE167363` classical monocyte DEGs (`718` genes) and the four bulk cohorts reduces to `40` genes almost entirely via the transcriptomic DEG filters, while the `21,896`-gene GeneCards set encompasses nearly every annotated human gene (because GeneCards returns any gene with even a single text-mined co-mention of "apoptosis"). Calling `G0S2`, `GZMA`, `ITM2A`, and `PAG1` "apoptosis-related hub genes" on the basis of membership in a `21,896`-gene set is scientifically invalid.

### Defect 2: Multi-Cohort Test-Set Data Leakage in Feature Selection
* **Location:** Section 2.3 (lines 67–69), Section 3.3 (lines 127–131, Figure 3A), and Section 3.5 (lines 147–156, Figure 5A–C).
* **Audit Finding:** In Section 3.3, the authors perform differential expression analysis (`limma`, `|log2FC| > 0.5`, adjusted `p < 0.05`) across `GSE65682` (`4,060` DEGs), `GSE26440` (`3,738` DEGs), `GSE95233` (`4,897` DEGs), and `GSE26378` (`3,309` DEGs) simultaneously, and take their intersection (`40` genes) as the input to `RF`, `SVM`, `XGB`, and `GLM` feature selection. Subsequently, in Section 3.5, the authors use `GSE26440`, `GSE95233`, and `GSE26378` as "independent external validation sets" to evaluate the diagnostic ROC AUCs (`0.962`, `0.996`, and `0.985`, Figure 5A–C). Because a gene could only enter the 40-gene candidate pool if it already achieved `|log2FC| > 0.5` and adjusted `p < 0.05` between sepsis and control samples in `GSE26440`, `GSE95233`, and `GSE26378`, the validation cohorts were directly leaked into the feature-selection pipeline.

### Defect 3: Unregularized Resubstitution Overfitting (`AUC = 1.000`) in Machine Learning Screening
* **Location:** Section 2.4 (`Machine learning screening of diagnostic biomarkers`, lines 73–77) and Section 3.3 (lines 131–138, Figure 3B–D).
* **Audit Finding:** In Figure 3D, `RF`, `SVM`, and `XGB` each report an exact `AUC = 1.000` (and `GLM` reports `AUC = 0.997`) on `GSE65682`. Achieving `AUC = 1.000` across three distinct model families on a heterogeneous clinical cohort of `n = 802` ICU subjects (`760` sepsis vs. `42` healthy controls, massive 18:1 class imbalance) is a hallmark of evaluating ROC curves on the training set (resubstitution error) without held-out fold predictions or class-imbalance correction. Furthermore, in Section 3.3 (line 133), the authors select the top 10 features from each model based on *"the lowest root mean square error (RMSE)"*, even though sepsis vs. control is a binary classification problem where RMSE on uncalibrated scores is an improper selection metric.

### Defect 4: Lineage Confounding (`GZMA` and `ITM2A`) and Whole-Blood Western Blot Misattribution
* **Location:** Section 2.9 (`Western blot validation`, lines 97–107), Section 3.7 (`Single-gene GSEA and immune cell infiltration analysis`, lines 168–186, Figure 6), and Section 3.8 (`Validation of hub gene expression by Western blot`, lines 188–194, Figure 7).
* **Audit Finding:**
  1. `GZMA` (Granzyme A, a cytolytic serine protease secreted by cytotoxic CD8+ T cells and NK cells) and `ITM2A` (Integral Membrane Protein 2A, a T-cell activation marker regulated by GATA3/PAX5) are lymphocyte-specific transcripts, not classical monocyte genes. Indeed, the authors' own CIBERSORT analysis (Section 3.7, lines 179–184; Figure 6E–F) shows that `GZMA` and `ITM2A` correlate strongly **positively** with CD8+ T cells and resting NK cells and **negatively** with monocytes and neutrophils, while `G0S2` and `PAG1` show the exact opposite pattern!
  2. In Section 2.9 (lines 99–101), Western blotting was performed on whole peripheral blood samples (`n = 6` sepsis vs. `n = 6` healthy controls) lysed directly in RIPA buffer—not on FACS- or MACS-sorted classical monocytes. Because sepsis patients experience profound lymphopenia (loss of T/NK cells) alongside marked neutrophilia and monocytosis, whole-blood protein lysates from sepsis patients inevitably contain less T/NK-derived `GZMA`/`ITM2A` and more myeloid-derived `G0S2`/`PAG1`. Presenting whole-blood abundance shifts as proof of "classical monocyte apoptosis regulation" is a fundamental biological misinterpretation.

### Defect 5: Misclassification of Pediatric Septic Shock Cohorts as General Adult Sepsis
* **Location:** Section 2.1 (lines 47–51) and Discussion.
* **Audit Finding:** Two of the three validation cohorts (`GSE26440` and `GSE26378`) are pediatric septic shock cohorts, whereas `GSE65682` and `GSE95233` are adult ICU cohorts, and `GSE167363` is an adult PBMC scRNA-seq cohort. Age-related differences in thymic output and lymphocyte-to-myeloid ratios between young children and older adults are never addressed or controlled for.

---

## 4. Quantitative Rubric Scoring

| Rubric Dimension | Max | Awarded | Justification |
| :--- | :---: | :---: | :--- |
| **1. Methodological & Statistical Rigor** | 3.5 | **0.8** | Vacuous `21,896`-gene GeneCards filter; direct test-set data leakage across all three validation cohorts during the 40-gene DEG intersection; resubstitution overfitting (`AUC = 1.000` for RF, SVM, XGB) on an 18:1 imbalanced cohort (`760` vs. `42`). |
| **2. Claims-to-Evidence Alignment** | 2.5 | **0.8** | Diagnostic generalization claims (`AUC = 0.962–0.996`) are inflated by pre-filtering features on the test sets; mechanistic claims regarding classical monocyte apoptosis are unsupported by whole-blood Western blots. |
| **3. Biological & Clinical Plausibility** | 2.0 | **0.8** | Severe lineage confounding: `GZMA` and `ITM2A` are cytotoxic T/NK cell markers whose decrease in bulk blood reflects sepsis lymphopenia, not monocyte intrinsic apoptosis (as confirmed by the authors' own CIBERSORT correlations in Fig. 6E–F). |
| **4. Reproducibility & Transparency** | 2.0 | **0.9** | Public GEO accessions (`GSE65682`, `GSE26440`, `GSE95233`, `GSE26378`, `GSE167363`) and a public GitHub repository (`Duanwj112/Duanwj_sepsis`) are provided, though ML hyperparameter settings, cross-validation splits, and clinical patient demographics for the `n = 6` WB samples are omitted. |
| **Total** | **10.0** | **3.3** | **Scientific Core Score:** **2.4 / 8.0** |

---

### 5. Constructive and Doable Suggestions for Improvement
1. **Replace the `21,896`-Gene GeneCards Query with Curated Apoptosis Pathways:** Restrict apoptosis candidate genes to curated pathway databases (e.g., KEGG `hsa04210 Apoptosis`, Hallmark `HALLMARK_APOPTOSIS`, or GO `GO:0006915` structural regulators) or apply a strict GeneCards Relevance Score threshold ($\ge 10$) so the gene set genuinely reflects apoptotic machinery.
2. **Eliminate Test-Set Data Leakage:** Perform differential expression screening and machine learning feature selection strictly within the training cohort (`GSE65682` plus `GSE167363` scRNA-seq), locking the final 4-gene logistic regression coefficients before ever touching `GSE26440`, `GSE95233`, or `GSE26378`.
3. **Remove Ambient Lymphocyte Contamination and Isolate CD14+ Monocytes for Validation:** Filter out ambient T/NK cell transcripts (`GZMA`, `ITM2A`, `CD3D`, `NKG7`) from the `GSE167363` monocyte cluster using tools such as `SoupX` or `DecontX`, and perform Western blot and Annexin V/PI flow cytometry validation on MACS-isolated CD14+ monocytes rather than unfractionated whole blood.
