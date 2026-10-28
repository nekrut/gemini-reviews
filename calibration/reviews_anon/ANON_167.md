# Review of ANON_167

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **4.4 / 10.0** (Flawed / Overstated)  
* **Score Breakdown:** Rigor: 1.3/3.5 | Claims: 1.0/2.5 | Biology: 1.2/2.0 | Reproducibility: 0.9/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This study integrates three single-cell RNA-seq datasets of lung adenocarcinoma (LUAD) spanning atypical adenomatous hyperplasia (AAH), adenocarcinoma in situ (AIS), minimally invasive adenocarcinoma (MIA), and invasive adenocarcinoma (IAC) (`GSE150938`, `GSE189357`, and `HRA001130`). Using `inferCNV` with endothelial cells as a reference, the authors isolate malignant epithelial cells, re-cluster them into nine subpopulations (Clusters 0–8), and apply GSVA, Monocle2 pseudotime, `scMetabolism`, and `CytoTRACE` to characterize Cluster 0 and Cluster 6. Marker genes from Clusters 0 and 6 are then entered into a 10-algorithm machine learning benchmark trained on TCGA-LUAD and evaluated across six GEO microarray cohorts (`GSE13213`, `GSE26939`, `GSE29016`, `GSE30219`, `GSE31210`, `GSE42127`) and the OAK/POPLAR clinical trials, yielding a `CoxBoost + plsRcox` Composite Prognostic Model (CPM). Finally, the authors perform immune deconvolution and knock down `S100A16` with siRNA in A549 and H1299 cells to assay colony formation, wound healing, and transwell migration/invasion.

While integrating single-cell data across pre-invasive to invasive LUAD stages is a reasonable design, the manuscript has major methodological and reporting defects. First, the Abstract claims that the CPM model was validated for its *"mutation landscape"* and *"predicted genomic alterations, chemotherapy drug sensitivity"*, yet the Results section contains no mutation analysis or chemotherapy drug-sensitivity analysis (and the Discussion explicitly admits mutation frequencies were not analyzed). Second, the authors never report the actual gene list or regression weights of the CPM model anywhere in the text or figures, rendering the signature impossible to reproduce. Third, selecting the winning ML algorithm by maximizing the average C-index across the six GEO validation cohorts introduces validation-set selection bias when benchmarking against 144 published signatures on those same cohorts. Fourth, the pseudotime analysis inverts the biological trajectory by placing Clusters 0 and 6 at the "nascent/initial stages" that "diminish over time" (Section 3.2), directly contradicting Section 3.4, which shows Clusters 0 and 6 *increase* from pre-invasive AAH to invasive IAC.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **The CPM model predicts genomic alterations, mutation landscapes, and chemotherapy drug sensitivity in LUAD: [Methodologically Flawed].**  
  The Abstract (page 1, line 8) explicitly states that the CPM model was *"validated across multiple cohorts for its... mutation landscape"* and *"predicted genomic alterations, chemotherapy drug sensitivity, and immunotherapy responsiveness."* However, there is no analysis, figure, or table examining somatic mutations, copy-number alterations by CPM group, or chemotherapy IC50/drug sensitivity anywhere in the Results (Sections 3.1–3.8), and the Discussion (lines 185, 189) contradicts the Abstract by noting that gene mutation frequencies were not analyzed. Furthermore, in the OAK/POPLAR cohort (Fig. 6I), the authors only show a Kaplan–Meier curve of overall survival by CPM group without testing treatment-by-biomarker interaction (atezolizumab vs. docetaxel) or objective response rate, which conflates general prognostic value with "immunotherapy responsiveness."

* **Clusters 0 and 6 represent an "early developmental stage" that diminishes over pseudotime while simultaneously increasing from AAH to IAC: [Methodologically Flawed].**  
  In Section 3.2 (line 104, Fig. 3C), the authors state that *"Clusters 0 and 6 localize to the nascent stages of development, with a subsequent diminution in prevalence over time."* Conversely, Section 3.4 (line 126, Fig. 5A–B) shows that Clusters 0 and 6 are minimal in pre-invasive AAH/AIS and progressively *increase* to peak abundance in invasive adenocarcinoma (IAC). This contradiction arises because Monocle2 trajectories are undirected unless rooted on biologically earliest samples (AAH), and `CytoTRACE` measures total expressed gene diversity—which is elevated in hyper-transcribing, highly proliferative (MYC-high, glycolytic) advanced IAC cells—causing the authors to mistake late-stage neoplastic dedifferentiation/hypertranscription for an "early developmental stage."

* **The CoxBoost + plsRcox CPM model outperforms 144 published LUAD signatures across six independent GEO validation cohorts: [Overstated].**  
  In Section 3.5 (line 137), the authors state: *"The criterion for model selection was based on the average c-index across the six validation cohorts."* Selecting the best model out of $\sim 100$ algorithm pairs by evaluating their C-index on the six GEO validation cohorts uses the validation cohorts for model selection (lookahead/selection bias). Subsequently comparing this validation-optimized winner against 144 fixed published signatures on the exact same six GEO datasets (Section 3.6, Fig. 7) is an asymmetric comparison that inflates the apparent superiority of CPM. In addition, Method 2.1 (line 29) states that all GEO datasets were *"converted into transcripts per million (TPM) format"*, which is mathematically invalid for microarray datasets (`GSE13213`, `GSE30219`, `GSE31210`, `GSE42127`).

* **`S100A16` knockdown inhibits proliferation, "DNA replication capabilities," migration, and invasion of A549 and H1299 cells: [Moderately Supported].**  
  The colony formation, scratch wound-healing, and Matrigel transwell assays (Fig. 9) support an in vitro pro-proliferative and pro-migratory phenotype for `S100A16` in A549 and H1299 cells, consistent with prior LUAD literature cited in the Discussion (refs. 32–42). However, the claim in Section 3.8 (line 170) and the Discussion (line 187) that `S100A16` knockdown inhibited *"DNA replication capabilities"* is unsupported because crystal violet colony counts do not specifically measure DNA synthesis (e.g., EdU/BrdU incorporation). Moreover, only a single siRNA duplex (`si-S100A16`) was tested without a second independent siRNA to exclude off-target effects, and the number of biological replicates ($n$) is omitted from the Methods and Figure 9 caption.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Disclose the Complete CPM Gene List, Coefficients, and Pre-Processing Pipeline
* **WHY:** The manuscript never states which genes are included in the final `CoxBoost + plsRcox` model or what their regression weights are, making it impossible to verify or apply the CPM score. Additionally, microarray probe intensities cannot be converted to RNA-seq TPM.
* **WHAT:** Provide a table in the main text listing every gene in the CPM signature alongside its `plsRcox` coefficient, and accurately describe how microarray intensity matrices were normalized (e.g., RMA or quantile normalization) prior to ComBat batch correction.
* **HOW:** Export the non-zero features selected by `CoxBoost` and the fitted linear predictor weights from `plsRcox` into a new **Table 1**, write out the explicit risk score formula $\text{CPM} = \sum_i \beta_i x_i$, and deposit the R scripts in a public repository (GitHub/Zenodo).

#### 2. Eliminate Validation-Set Selection Bias Using Nested Cross-Validation Within TCGA
* **WHY:** Picking the winning algorithm pair out of 100 combinations by maximizing average C-index across the six GEO validation cohorts leaks test-set information into model selection and invalidates the subsequent benchmark against 144 published signatures on those same GEO cohorts.
* **WHAT:** Select the optimal ML algorithm strictly via 10-fold cross-validation *within the TCGA training cohort* (or hold out a subset of GEO cohorts untouched during model selection).
* **HOW:** Rank the ML combinations in Figure 6A by their mean 10-fold cross-validated C-index within TCGA-LUAD alone, lock the top model and its weights on TCGA, and only then evaluate out-of-sample C-index and 1/3/5-year ROC AUCs across the six untouched GEO cohorts and the 144-signature benchmark.

#### 3. Root the Monocle2 Trajectory on Pre-Invasive AAH Cells to Resolve the Pseudotime Contradiction
* **WHY:** Placing Clusters 0 and 6 (which peak in invasive IAC and express high cell-cycle/MYC/glycolysis programs) at the beginning of pseudotime contradicts the histopathological progression data in Figure 5A–B.
* **WHAT:** Explicitly root the Monocle2 pseudotime tree using cells derived from the earliest histopathological stage (AAH) rather than relying on `CytoTRACE` gene-count diversity (which is confounded by hypertranscription in aneuploid invasive tumor cells).
* **HOW:** In Monocle2 `orderCells()`, set `root_state` to the state containing the highest proportion of AAH-derived epithelial cells, re-plot Figure 3B–C, and revise Sections 3.2–3.4 so that pseudotime directionality aligns with the histological progression from AAH $\to$ AIS $\to$ MIA $\to$ IAC.

#### 4. Align Abstract Claims with Performed Analyses and Clarify Experimental Reporting
* **WHY:** Claiming in the Abstract that the model predicts *"genomic alterations, chemotherapy drug sensitivity, and immunotherapy responsiveness"* when no mutation or chemotherapy analyses are presented (and when OAK/POPLAR is not stratified by treatment arm vs. chemotherapy control) misleads readers. Similarly, colony formation does not measure DNA replication.
* **WHAT:** Remove unperformed analyses from the Abstract, replace *"DNA replication capabilities"* with *"clonogenic proliferation"*, and report exact biological replicate counts ($n$) and statistical test details in Figure 9.
* **HOW:** Edit the Abstract (lines 8–9) to delete references to *"mutation landscape"*, *"genomic alterations"*, and *"chemotherapy drug sensitivity"*; if OAK/POPLAR trial arm annotations (atezolizumab vs. docetaxel) are available, plot separate KM curves for immunotherapy vs. chemotherapy arms in Figure 6I. In Figure 9's caption, state the exact number of independent biological replicates (e.g., $n = 3$) and the specific statistical test used.

#### 5. Technical, Mathematical, and Editorial Cleanup
* **WHY:** Several typographical and citation errors appear in the text and captions.
* **WHAT & HOW:**
  1. **Section 2.5 (page 2, line 49):** Correct `TIMMER` to `TIMER`.
  2. **Figure 2 Caption (page 3, line 99):** Correct the truncated GSA accession `HRA00113` to `HRA001130`.
  3. **Data Availability Statement (page 6, lines 229, 239):** Add the GSA repository link and accession (`HRA001130`) alongside TCGA and GEO, and remove the stray spaces in the URL `https://www . ncbi.nlm.nih.gov/geo /`.
