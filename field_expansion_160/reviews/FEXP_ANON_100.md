# Forensic Review of `FEXP_ANON_100`

**Overall Score:** **1.6 / 10.0** (Fundamentally Invalid) | **Scientific Core Score:** **1.3 / 8.0**
* **Score Breakdown:** Rigor: 0.4/3.5 | Claims: 0.4/2.5 | Biology: 0.5/2.0 | Reproducibility: 0.3/2.0

---

## 1. Blinded Metadata Perception

* **Perceived Field & Subfield:** Cancer Bioinformatics / Computational Oncology (Single-cell and bulk transcriptomic cuproptosis prognostic signature in hepatocellular carcinoma).
* **Study Design Archetype:** Formulaic in silico pipeline combining GEO scRNA-seq (`GSE166635`) and bulk RNA-seq from TCGA, GEO, and ICGC with `Seurat`, `Harmony`, `CopyKAT`, `GSVA`/`ssGSEA` (regulated cell death scoring), `randomForest`, `Monocle2`, `CytoTRACE`, `scMetabolism`, `WGCNA`, `LASSO`/multivariate Cox regression, `IMvigor210`, and nomogram construction, with zero experimental validation.
* **Temporal & Venue Signals:** Classic paper-mill / template-generated multi-package prognostic signature manuscript containing explicit cross-cancer copy-paste artifacts ("cholangiocarcinoma" in Methods; "CRC patients" in Data Availability).

---

## 2. Executive Summary & Editorial Verdict

This manuscript purports to analyze single-cell RNA-seq data (`GSE166635`, 17,924 cells) and bulk transcriptomic cohorts (TCGA, plus unspecified GEO and ICGC datasets) in hepatocellular carcinoma (HCC) to identify a cuproptosis-enriched malignant subpopulation (`C2`), intersect its marker genes with `WGCNA` modules to build a 10-gene LASSO/Cox prognostic signature, and evaluate pathway enrichment and `IMvigor210` therapy response.

**Editorial Verdict: Reject (Fundamentally Invalid).** Forensically, this manuscript exhibits unmistakable hallmarks of automated template assembly and cross-cancer copy-pasting. Although the title and narrative focus on hepatocellular carcinoma (HCC), the Methods section states that time-dependent ROC curves were computed to evaluate overall survival in *"patients with cholangiocarcinoma"* (line 60), while the Data Availability section states that *"scRNA-seq data from CRC [colorectal cancer] patients were retrieved from the GEO database"* (line 164). Internally, the manuscript fails basic scientific and mathematical sanity checks: the 10-gene risk model omits all regression coefficients ($\beta_i$), mutates gene symbol `SCGN` in Results (line 110) into `CGN` in Discussion (line 152) while hallucinating an 11th gene (`SPON2`) in the middle of the 10-gene biological summary, states three mutually contradictory single-cell filtering thresholds, confuses 30 PCA components with "30 characteristic marker genes," mislabels `IMvigor210` anti-PD-L1 immunotherapy as "chemotherapy," and reverses its therapeutic conclusion from *inducing* cuproptosis (Introduction/Discussion) to administering *"cuproptosis inhibitors"* (Conclusion).

### Assessment of Specific Claims

* **Cuproptosis is the most defining programmed cell death feature of HCC cells and specifically characterizes the C2 stem-like malignant subpopulation (Abstract; Results, lines 84–97; Figs. 4–5): `[Methodologically Flawed]`**  
  The authors claim in Methods (line 33) to score 18 regulated cell death (RCD) pathways via `GSVA`, but in Results (line 84) switch to `ssGSEA` on 12 types of programmed cell death and train a `randomForest` classifier without specifying what response label the Random Forest was predicting (tumor vs. normal, cluster identity, or high/low risk—note that Fig. 4B caption contradicts the text by stating *"key pathway enrichment scores in high- and low-risk groups"* before any risk model has even been constructed). Furthermore, in Results (line 97), they run univariate Cox regression on bulk TCGA-LIHC data to find 4,326 prognostic genes and compute a single `GSVA` score across all 4,326 genes simultaneously in single cells—ignoring whether the Cox hazard ratios are positive (risk) or negative (protective)!
* **A 10-gene cuproptosis risk model accurately predicts 1-, 3-, and 5-year survival across TCGA, GEO, and ICGC HCC cohorts (Abstract; Results, lines 110–117; Fig. 7): `[Methodologically Flawed]`**  
  The model is completely irreproducible and internally inconsistent: (1) no regression coefficients ($\beta_i$) are reported anywhere in the text, tables, or figures; (2) the risk score equation in Methods (line 58) is malformed ($\text{Risk Score} = \sum_{i=0}^k \beta_i * \text{exp}_i - 1$); (3) the gene list changes from `SCGN` in Results (line 110) to `CGN` in Discussion (line 152) while Results line 110 inexplicably describes `SPON2` as one of the model genes; and (4) neither the GEO validation cohort nor the ICGC validation cohort is given an accession ID or sample size anywhere in the manuscript.
* **The low-risk group exhibits a significantly higher chemotherapy response rate in the IMvigor210 cohort (Results, line 135; Fig. 9A–B): `[Methodologically Flawed]`**  
  `IMvigor210` is a phase II clinical trial of atezolizumab (anti-PD-L1 **immunotherapy**, not chemotherapy) in metastatic **urothelial (bladder) carcinoma**, not HCC. The text in line 135 repeatedly mischaracterizes `IMvigor210` as predicting *"the efficacy of chemotherapy"* and *"chemotherapy response rate"*, whereas the Fig. 9A caption calls it *"immune therapy responses in the IMvigor210 cohort"*. Meanwhile, `TIDE`, which was described in Methods (line 62), is completely absent from the Results.
* **Targeting HCC with "cuproptosis inhibitors" is supported by the study's findings (Conclusion, line 159): `[Methodologically Flawed]`**  
  Throughout the Introduction (line 18) and Discussion (line 150), cuproptosis is described as copper-overload cell death whose *induction* kills HCC cells (*"inducing cuproptosis in HCC cells could represent a promising novel therapeutic approach"*, line 150). Yet the Conclusion (line 159) inverts the biology and advocates *"integrating cuproptosis inhibitors with other therapies"* and *"the broader therapeutic application of cuproptosis inhibitors"*.

---

## 3. Forensic Defect Inventory

### 3.1. Cross-Cancer Template Copy-Paste Artifacts (Pillar 2 & Pillar 7)
* **Location:** Methods ("Construction and evaluation of the predictive model", line 60) and Data Availability (line 164).
* **Defect:**
  1. Line 60: *"Additionally, ROC curves were plotted using the 'timeROC' package to evaluate the predictive performance of the risk score for 1-year, 3-year, and 5-year overall survival (OS) in patients with **cholangiocarcinoma**."*
  2. Line 164: *"scRNA-seq data from **CRC patients** were retrieved from the GEO database (https://www.ncbi.nlm.nih.gov/geo/)."*
  3. Lines 26 and 68: Section headers contain unedited numbering typos (`## 1Data collection and processing`).

### 3.2. Mutually Contradictory Methods, Gene Lists, and Equations (Pillar 3 & Pillar 7)
* **Contradictory scRNA-seq Filtering Thresholds:** Methods (line 28) states that cells with `< 200` or `> 7,000` genes were excluded. Results (line 70) states in a single paragraph that *"each cell was required to express a minimum of 250 genes"* and immediately in the next sentence *"ensuring that each cell expressed between 100 and 10,000 genes"*.
* **Confusion of Principal Components with Marker Genes:** Results (line 70) states: *"The integrated dataset was subjected to PCA for dimensionality reduction, retaining the top 30 characteristic marker genes (Fig. 1D)"*, confusing 30 principal components (`npcs = 30`) with 30 marker genes.
* **Inconsistent Gene Symbols (`SCGN` vs. `CGN` vs. `SPON2`):** Results (line 110) lists the 10 signature genes as `SCGN, PPP1R1A, TUSC1, C1S, AHCY, TFPI, MLEC, DNAJB1, TXN, and LDHA`, but in the very same paragraph discusses `SPON2` (*"Furthermore, SPON2, a core marker of the TIMES system..."*) as if it were in the signature. Then in Discussion (line 152), `SCGN` is replaced twice by `CGN` (*"CGN, PPP1R1A, TUSC1..."*).
* **Malformed Formula & Omitted Coefficients:** Methods (line 58) writes the risk score formula as $\text{Risk Score} = \sum_{i=0}^k \beta_i * \text{exp}_i - 1$ (starting at index $0$ for a 10-gene model and subtracting $1$ or indexing $\text{exp}_{i-1}$), and never reports the values of $\beta_i$.
* **Nomogram Regression Contradiction:** Methods (line 62) states *"A nomogram was built based on the results of multivariate logistic regression analysis"*, whereas Results (line 143) states it was built from *"multivariate Cox regression analysis"*.

### 3.3. Pervasive Figure-Text Misalignments & Missing Cohort Provenance (Pillar 7)
* **Non-Existent `Fig. 2G` and Shifted `Fig. 6` & `Fig. 8` Panels:**
  * Results (line 70) cites `Fig. 2G` for `CopyKAT` tumor cell identification, `Fig. 2E` for cell numbers, and `Fig. 2F` for cell proportions, whereas the Fig. 2 legend (line 76) only has panels `A–F` (with `CopyKAT` in `Fig. 2F`).
  * Results (lines 105, 110) cites `Fig. 6B` for soft-threshold power $\beta=6$, `Fig. 6C` for the dendrogram, `Fig. 6D` for module-cuproptosis correlations, and `Fig. 6E` for the 447-gene Venn diagram; however, in the Fig. 6 legend (line 100), `6B` is a violin plot of prognostic scores, `6C` is network topology, `6D` is the dendrogram, `6E` is module-copper death correlations, and `6F` is top five DEGs.
  * Results (line 122) cites `Fig. 8A` for the univariate Cox forest plot (`HR: 2.718`), whereas `Fig. 8B` is the univariate analysis.
* **Unidentified Validation Cohorts:** Neither the GEO bulk validation cohort nor the ICGC validation cohort (line 117) has an accession number (e.g., `GSE...`, `LIRI-JP`), sample size, or clinical summary anywhere in the text.

---

## 4. Quantitative Rubric Scoring

| Rubric Dimension | Score | Max | Forensic Justification |
| :--- | :---: | :---: | :--- |
| **1. Methodological & Statistical Rigor** | **0.4** | 3.5 | Unspecified Random Forest labels; unsigned GSVA scoring of 4,326 univariate Cox genes; malformed risk equation with missing $\beta_i$ coefficients; contradictory scRNA-seq QC thresholds; unannotated GEO/ICGC cohorts. |
| **2. Claim-to-Evidence Alignment** | **0.4** | 2.5 | Mischaracterizes bladder cancer anti-PD-L1 (`IMvigor210`) as HCC "chemotherapy response"; contradicts its own thesis by advocating "cuproptosis inhibitors" in Conclusion; claims a 10-gene model while mutating `SCGN` to `CGN` and inserting `SPON2`. |
| **3. Data Integrity & Biological Plausibility** | **0.5** | 2.0 | Cross-cancer copy-paste contamination ("cholangiocarcinoma" in Methods, "CRC patients" in Data Availability); zero experimental validation; biological confusion between cuproptosis induction and inhibition. |
| **4. Reproducibility & Data Integrity** | **0.3** | 2.0 | Missing GEO/ICGC accession numbers, missing model coefficients, shifted figure panel references (`Fig. 2G`, `Fig. 6B–F`, `Fig. 8A–B`), raw LaTeX preamble leak in line 105, and no source code. |
| **Total Composite Score** | **1.6** | **10.0** | **Fundamentally Invalid** (**Scientific Core Score: 1.3 / 8.0**) |
