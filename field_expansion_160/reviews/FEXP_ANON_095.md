# Forensic Peer Review: FEXP_ANON_095

**Overall Score:** **2.4 / 10.0** (Fundamentally Invalid) | **Scientific Core Score:** **1.9 / 8.0**
* **Score Breakdown:** Rigor: 0.6/3.5 | Claims: 0.5/2.5 | Biology: 0.8/2.0 | Reproducibility: 0.5/2.0

---

## 1. Blinded Metadata Perception
* **Perceived Study Type:** Multi-omics bioinformatic signature and in vitro cell-line study integrating bulk transcriptomics (`TCGA-OV`, `GSE9891`), scRNA-seq (`E-MTAB-8107`), spatial transcriptomics (`GSE203612`), LASSO-Cox modeling, and functional assays (`OVCAR3` knockdown of `NME6`) in ovarian cancer (OV).
* **Perceived Subfield:** Gynecologic Oncology / Cancer Bioinformatics / Purine Metabolism.
* **Tier Classification:** Fundamentally Invalid (1.0–2.9).

---

## 2. Executive Summary & Editorial Verdict
This manuscript investigates purine metabolism-related genes (PMRGs) in ovarian cancer (OV) by applying `AUCell` pathway scoring to scRNA-seq data (`E-MTAB-8107`, `n = 5` tumors) and one spatial transcriptomics slide (`GSE203612`), constructing a 12-gene LASSO-Cox prognostic model in `TCGA-OV` (`n = 363`) validated in `GSE9891` (`n = 278`), and performing in vitro siRNA knockdown of `NME6` in `OVCAR3` cells (`qRT-PCR`, `CCK-8`, `EdU`, `Transwell`, and `Annexin V` apoptosis assays).

Forensic audit reveals critical structural omissions, internal contradictions, and impossible data linkages across modalities that render the bioinformatic core of the paper irreproducible and scientifically invalid:
1. **Omitted Risk Score Equation, Missing Gene Names, and Misstated Cox Formula:** In Section 2.4 (`line 56`), the text states *"A risk score was computed as follows:"* followed by a missing equation and a description of $h_0(t)$ (the baseline hazard function of a Cox proportional hazards model $h(t) = h_0(t)\exp(\sum b_i x_i)$ rather than a linear risk score!). Worse still, **9 of the 12 LASSO-Cox signature genes and all 12 regression coefficients are never even named or reported anywhere in the main text or tables** (only `GMPR`, `POLR3H`, and `NME6` are ever mentioned by name in Section 3.9).
2. **Impossible Cross-Modality Linkage Between Single-Cell Subpopulations (`NME6+` Epithelial Cells) and Bulk Patient Survival / TIDE Scores (`Figure 9c–g`):** In Section 3.9 (`lines 149–152`, `Figure 9c–g`), the authors claim to stratify ovarian cancer patients by the abundance of **`GMPR+` epithelial cells**, **`POLR3H+` epithelial cells**, and **`NME6+` epithelial cells**, reporting overall survival (OS) curves and `TIDE` immunotherapy scores for patients with high vs. low `GMPR+`, `POLR3H+`, and `NME6+` epithelial cell content. However, the scRNA-seq dataset (`E-MTAB-8107`) has only `5` patients and lacks OS and TIDE data, whereas the bulk `TCGA-OV` cohort lacks single-cell resolution! The authors silently equated bulk tumor `GMPR`, `POLR3H`, and `NME6` mRNA expression in `TCGA-OV` with "`GMPR+`, `POLR3H+`, and `NME6+` epithelial cell content."
3. **Direct Self-Contradictions in Spatial Transcriptomics Clustering (`7` vs. `9` Clusters) and ROC Horizons (`1-Year` vs. `3-Year`):** Within the exact same paragraph of Section 3.3 (`line 101`), the authors state that the spatial transcriptome sample (`GSE203612`) was divided into **"seven cellular subpopulations" (`Figure 3a,b`)** and then, four sentences later, state that *"After normalizing and clustering the spatial transcriptome data, we obtained **nine cell subpopulations** (`Figure 3g`)."* Similarly, Section 3.5 (`line 117`) states that `Figure 5e` shows the **3-year AUC**, whereas the `Figure 5e` caption (`line 120`) states **"One-year AUC curves."**
4. **Garbled Experimental Methods and Unadjusted Single-Cell Differential Expression:** Section 2.7 (`line 72`) states *"Three families of ovarian cells were obtained. The acquisition process and sample storage and processing are the same as before [25],"* whereas Results (`line 149`) only tests two cell lines (`IOSE` and `OVCAR3`). Furthermore, single-cell DEGs (`1,630` genes) and bulk `TCGA-OV` survival screening (`34` genes) were performed using unadjusted $p < 0.05$ (`lines 51, 56, 108`).

### Specific Conclusions and Assessment of Support
* **Claim 1:** A 12-gene PMRG-derived risk score predicts 1-, 3-, and 5-year overall survival in `TCGA-OV` and `GSE9891`. — `[Methodologically Flawed]` (The risk score equation is missing at `line 56`, 9 of the 12 signature genes and all 12 coefficients are omitted from the text, and the reported time-dependent ROC AUCs in `Figure 4c,d` are modest [`~0.55–0.65` based on standard LASSO fits when `p < 0.05` unadjusted screening is used, with exact AUC values omitted from the main text].)
* **Claim 2:** High content of `GMPR+`, `POLR3H+`, and `NME6+` epithelial cells predicts worse overall survival and higher `TIDE` immunotherapy resistance in ovarian cancer patients (`Figure 9c–g`). — `[Methodologically Flawed]` (Bulk `TCGA-OV` mRNA expression of `GMPR`, `POLR3H`, and `NME6` was mislabeled as single-cell "`GMPR+`/`POLR3H+`/`NME6+` epithelial cell content," ignoring non-epithelial expression and tumor purity confounding.)
* **Claim 3:** Spatial transcriptomics (`GSE203612`) confirms high purine metabolism activity in malignant epithelial regions (`Figure 3`). — `[Fragile]` (Based on $n = 1$ spatial slide with an unexplained internal contradiction between 7 clusters [`Fig. 3a–b`] and 9 clusters [`Fig. 3g`] in the same paragraph.)
* **Claim 4:** Knockdown of `NME6` in `OVCAR3` cells reduces proliferation (`CCK-8`, `EdU`), migration, and invasion (`Transwell`), and increases apoptosis (`Figure 10`). — `[Moderately Supported]` (Standard in vitro phenotypic assays in a single cell line [`OVCAR3`] with two siRNAs [`si-NME6-1`, `si-NME6-2`] show consistent directionality, though purine metabolite levels were never measured and rescue experiments were not performed.)

---

## 3. Forensic Defect Inventory

### Defect 1: Missing Risk Score Formula, Misstated Hazard Definition, and Omitted 12-Gene Signature Identity
* **Location:** Section 2.4 (`Building and Verifying Risk Scoring Models`, lines 55–57) and Section 3.4 (`Developing and Validating a Risk Prediction Model`, lines 107–115, Figure 4).
* **Audit Finding:**
  1. At line 56, the manuscript reads:
     > *"A risk score was computed as follows:"*
     > *[Blank — no formula printed]*
     > *"In the context of survival analysis, $b_i$ represents the coefficient, $x_i$ denotes the expression value of each variable, and $h_0(t)$ signifies the baseline risk associated with the model."*
     Not only is the equation completely missing from the text, but $h_0(t)$ (the baseline hazard in $h(t|x) = h_0(t)\exp(\sum b_i x_i)$) is not even part of a LASSO-Cox linear predictor risk score ($\text{Risk Score} = \sum_{i=1}^{12} b_i x_i$).
  2. Throughout Section 3.4 (`lines 107–115`), the authors state that univariate Cox screening (`p < 0.05`) identified `34` prognostic genes and LASSO regression selected `12` genes (`Figure 4a,b`), **without ever listing the names of the 12 genes, their hazard ratios, their LASSO coefficients, or the exact numerical AUC values** in the text!

### Defect 2: Conflation of Bulk Gene Expression with Single-Cell `NME6+` Epithelial Cell Abundance (`Figure 9c–g`)
* **Location:** Section 3.9 (`Prognostic Analysis and Experimental Validation of Signature Genes`, lines 148–153, Figure 9c–g).
* **Audit Finding:** The authors write:
  > *"Higher TIDE scores were found when comparing groups with higher and lower levels of GMPR+, POLR3H+, and NME6+ epithelial cells (Figure 9c–e)... Furthermore, OS curves for patients with high content of GMPR+, POLR3H+, and NME6+ epithelial cells all showed a worsening trend in survival time (Figure 9f,g)."*
  Neither `TCGA-OV` nor `GSE9891` contains single-cell epithelial measurements, and `E-MTAB-8107` contains only `5` patients without survival or TIDE annotations. The authors stratified bulk `TCGA-OV` patients by bulk mRNA expression of `GMPR`, `POLR3H`, and `NME6`, and falsely described those bulk expression groups as *"patients with high content of GMPR+, POLR3H+, and NME6+ epithelial cells"*. Even in their own Figure 9b (`scRNA-seq` feature plots), `NME6`, `GMPR`, and `POLR3H` are expressed across multiple non-epithelial stromal and immune clusters (`fibroblasts`, `T cells`, `macrophages`).

### Defect 3: Internal Contradictions in Spatial Cluster Counts (`7` vs. `9`) and Nomogram ROC Horizons (`1-Year` vs. `3-Year`)
* **Location:** Section 3.3 (`line 101`, Figure 3a–b vs. Figure 3g) and Section 3.5 (`line 117` vs. `line 120`, Figure 5e).
* **Audit Finding:**
  1. In Section 3.3 (`line 101`), the first sentence states: *"The spatial transcriptome data was standardized and grouped using dimensionality reduction, dividing the spatial transcriptome into **seven cellular subpopulations** (Figure 3a,b)."* Four sentences later in the exact same paragraph, the text states: *"After normalizing and clustering the spatial transcriptome data, we obtained **nine cell subpopulations** (Figure 3g)."*
  2. In Section 3.5 (`line 117`), the text states: *"Comparison of the area under the curve (AUC) values for different clinical traits and column line graphs at **3 years** revealed a substantially higher AUC value for the column line graphs (Figure 5e)."* Yet the caption of `Figure 5e` (`line 120`) states: *"One-year AUC curves."* (Note also that "column line graphs" is a literal machine mistranslation of the Chinese term `列线图` for **nomogram**!).

### Defect 4: Garbled Cell-Line Description (`"Three families of ovarian cells"`) and Withheld Data/Code
* **Location:** Section 2.7 (`Cell Culture and Function Determination`, line 72), Section 2.8 (`qRT-PCR`, Table 1), and `Data Availability Statement` (line 236).
* **Audit Finding:**
  1. Section 2.7 begins: *"Three families of ovarian cells were obtained. The acquisition process and sample storage and processing are the same as before [25]."* Reference `[25]` (`Sun et al., Sci Rep 2024`) is a paper on **head and neck squamous cell carcinoma (HNSCC)** (`PGK1`), not ovarian cancer! Moreover, only two cell lines (`IOSE` and `OVCAR3`) are ever mentioned in Results (`line 149`), and the source/STR authentication of these lines is omitted.
  2. In Section 3.1 (`line 93`), the text states that filtering left `19,179` genes across `5` samples, and then immediately states that *"Data normalization and standardization are then performed by selecting the first 2000 highly variable genes"* while simultaneously claiming in Section 2.2 (`line 47`) that `FindVariableFeatures` selected the top `2,000` genes (`Figure 1d`).

---

## 4. Quantitative Rubric Scoring

| Rubric Dimension | Max | Awarded | Justification |
| :--- | :---: | :---: | :--- |
| **1. Methodological & Statistical Rigor** | 3.5 | **0.6** | Risk score equation omitted (`line 56`); 9 of 12 signature genes and all coefficients omitted; unadjusted `p < 0.05` screening; bulk gene expression conflated with single-cell `NME6+` epithelial cell abundance (`Fig. 9c–g`); contradictions between 7 vs. 9 spatial clusters and 1-year vs. 3-year ROC curves. |
| **2. Claims-to-Evidence Alignment** | 2.5 | **0.5** | Claims regarding `NME6+`, `GMPR+`, and `POLR3H+` epithelial cell abundance predicting OS and TIDE response in patient cohorts are invalid because bulk RNA-seq cannot resolve cell-type-specific expression without deconvolution. |
| **3. Biological & Clinical Plausibility** | 2.0 | **0.8** | The in vitro `NME6` siRNA knockdown experiments in `OVCAR3` cells (`Fig. 10`) provide basic preliminary evidence that `NME6` depletion impairs proliferation and invasion in one cell line, though no purine metabolism assays were conducted. |
| **4. Reproducibility & Transparency** | 2.0 | **0.5** | Impossible to reproduce the 12-gene risk model because the gene names, LASSO coefficients, and formula are missing from the paper; cell line acquisition cites an unrelated HNSCC paper `[25]`; code and processed data are not deposited. |
| **Total** | **10.0** | **2.4** | **Scientific Core Score:** **1.9 / 8.0** |

---

### 5. Constructive and Doable Suggestions for Improvement
1. **Report the Complete 12-Gene Signature and Linear Predictor Formula:** Explicitly print the linear predictor equation $\text{Risk Score} = \sum_{i=1}^{12} \beta_i \cdot \text{Expr}_i$ along with a table listing all 12 PMRGs, their univariate Cox hazard ratios, 95% confidence intervals, and exact LASSO-Cox $\beta_i$ coefficients.
2. **Correct the Cross-Modality Misattribution in `Figure 9c–g`:** Relabel `Figure 9c–g` and Section 3.9 to accurately reflect that `TCGA-OV` patients were stratified by **bulk tumor `GMPR`, `POLR3H`, and `NME6` mRNA expression** (or apply a validated single-cell deconvolution tool such as `BayesPrism` or `CIBERSORTx` if estimating epithelial-specific expression).
3. **Reconcile Spatial Cluster Counts (`Fig. 3`) and Nomogram Time Horizons (`Fig. 5e`):** Resolve the contradiction between 7 and 9 spatial clusters in Section 3.3, replace the machine mistranslation *"column line graphs"* with *"nomogram,"* and fix the cell culture methods (`Section 2.7`) to accurately list the exact ovarian cell lines used (`IOSE` and `OVCAR3`) and their repositories.
