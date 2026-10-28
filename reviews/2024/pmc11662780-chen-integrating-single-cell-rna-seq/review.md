# Review of PMC11662780 (PMID:39707393)

**Manuscript Title:** Integrating single-cell RNA-Seq and machine learning to dissect tryptophan metabolism in ulcerative colitis  
**Authors:** Chen G, Qi H, Jiang L, Sun S, Zhang J, Yu J, Liu F, Zhang Y, Du S.  
**Journal / Preprint:** *J Transl Med* (2024; `PMC11662780` / `PMID:39707393` / `10.1186/s12967-024-05934-w`)  
**Calibration Study Cohort:** Cohort C — Wild Literature Sample (`C21` | Double-Blinded as `ANON_72`)  
**Overall Score:** **2.8 / 10.0** (Fundamentally Invalid)  
* **Score Breakdown:** Rigor: 0.7/3.5 | Claims: 0.6/2.5 | Biology: 0.8/2.0 | Reproducibility: 0.7/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript combines single-cell RNA-seq datasets (`GSE214695` and `GSE125527`; 13 ulcerative colitis [UC] and 14 healthy control [HC] samples, 39,080 cells) with bulk transcriptomic cohorts (`GSE887466` [sic] and `GSE53306`) to investigate tryptophan metabolism in UC. The authors score 48 curated tryptophan metabolism-related genes (TrMGs) across single cells using five gene-set scoring tools (`AUCell`, `UCell`, `singscore`, `ssGSEA`, `AddModuleScore`), split all 39,080 cells at the mean score into "high" and "low" TrMG groups, intersect 78 genes upregulated in the high group with 385 score-correlated genes ($r > 0.1$) to obtain 22 genes, and apply five machine-learning feature selectors (Boruta, LASSO, SVM-RFE, GBM, Random Forest) on bulk data to identify *CTSS*, *S100A11*, and *TUBB*. They then examine *CTSS*+ vs. *CTSS*− macrophages using `CellChat`, `Monocle 2`, and `CytoTRACE`. No analysis code is provided.

The study is fundamentally compromised by a circular analytical design, biological misattribution, and evidence of template-pasted methods that were never executed: (1) splitting all 39,080 cells across 11 distinct cell types into "high-TrMG" (mostly macrophages, fibroblasts, and epithelial cells) versus "low-TrMG" (mostly T, B, and NK lymphocytes) and running differential expression does not identify regulators of tryptophan metabolism—it merely recovers general myeloid/stromal and housekeeping genes (*CTSS*, *S100A11*, *TUBB*, *ENO1*, *SOD2*, *HLA-DPA1*, *ANXA2*); (2) none of the three highlighted genes (*CTSS* [Cathepsin S], *S100A11*, *TUBB* [beta-tubulin]) belong to the 48 TrMGs or participate biochemically in tryptophan metabolism, yet the Abstract, Methods, and Conclusions repeatedly mischaracterize them as "key tryptophan metabolism-related genes" and "key regulators of tryptophan metabolism"; (3) the bulk training accession `GSE887466` does not exist in NCBI GEO; and (4) the Methods section describes Kaplan–Meier overall survival analysis and log-rank tests (line 87), GSVA across "distinct risk groups" (line 72), and `SCENIC` gene regulatory network inference (line 77), none of which exist in the Results or apply to non-malignant UC data.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* ***CTSS*, *S100A11*, and *TUBB* are key tryptophan metabolism-related genes (TrMGs) and regulators of tryptophan metabolism in UC: [Methodologically Flawed].**  
  Neither *CTSS* (a lysosomal cysteine protease for MHC class II antigen processing), *S100A11* (a calcium-binding EF-hand protein), nor *TUBB* (tubulin beta class I, a structural microtubule subunit) is a tryptophan metabolism gene or known regulator of the kynurenine, serotonin, or indole pathways. They were selected because the authors pooled all 39,080 cells across all lineages, dichotomized them by the 48-gene TrMG module score (which is naturally higher in macrophages/fibroblasts/epithelium than in lymphocytes, Figure 2c,f), and ran `FindMarkers` between the two cell pools. Comparing a macrophage/stromal-enriched cell pool against a lymphocyte-enriched cell pool trivially yields abundant myeloid and cytoskeleton transcripts (*CTSS*, *S100A11*, *TUBB*, *HLA-DPA1*, *ENO1*, *SOD2*). Calling these lineage confounders "hub TrMGs" (line 67) and "key regulators of tryptophan metabolism" (line 26) is biologically unfounded.

* ***CTSS*, *S100A11*, and *TUBB* are predominantly expressed in macrophages and validated in scRNA-seq: [Overstated].**  
  First, the Abstract (line 21) states that *"CTSS, S100A11, and TUBB were predominantly expressed in macrophages,"* which is directly contradicted by Results line 139: *"TUBB was predominantly expressed in B cells and fibroblasts, CTSS showing significant expression in macrophages, and S100A11 was highly expressed in macrophages, fibroblasts, and neutrophils."* Second, the "validation" in Figure 5d (line 139)—testing whether *CTSS*, *S100A11*, and *TUBB* are higher in the high-TrMG cell group than in the low-TrMG cell group ($p < 0.01$)—is completely circular because those exact same cells and groups were used in Figure 2g–i to select those genes in the first place. Third, the GSEA result for high-*CTSS* macrophages in Figure 5g reports only `NSE = 1.2918` (a typo for Normalized Enrichment Score, `NES`), omitting both the nominal $p$-value and the FDR $q$-value.

* **Tryptophan metabolism gene-set scores are elevated in UC macrophages and fibroblasts relative to healthy controls: [Moderately Supported].**  
  Scoring the 48 actual TrMGs across single cells (Figure 2a–d) shows higher module activity in macrophages, fibroblasts, and epithelial cells than in lymphocytes, consistent with known myeloid/epithelial expression of *IDO1* and kynurenine pathway enzymes in inflamed colonic mucosa. However, taking an unstandardized arithmetic average of five scoring algorithms with incompatible numerical ranges (`AUCell` and `UCell` in $[0,1]$ vs. signed `AddModuleScore` and unscaled `ssGSEA`; line 106) and performing cell-level Wilcoxon tests across 39,080 cells without pseudobulk aggregation at the patient level ($n = 13$ UC vs. $n = 14$ HC) inflates statistical significance.

* ***CTSS*+ macrophages reside in the early stages of macrophage developmental pseudotime (`Monocle 2` / `CytoTRACE`), with *CTSS* expression simultaneously declining and increasing over pseudotime: [Methodologically Flawed].**  
  Lines 150 contains a direct internal contradiction: it first states that as pseudotime progresses, *"the proportion of CTSS+ cells initially increasing in the early stages of development before declining in the later stages (Fig. 6e),"* and two sentences later states that *"CTSS expression in macrophages gradually increased over time (Fig. 6g)."* Furthermore, running trajectory inference on total colonic macrophages without separating infiltrating blood monocytes from resident lamina propria macrophages conflates distinct ontogenies with a single differentiation axis.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Restrict Differential Expression and Correlation Analyses to Within-Macrophage Comparisons or Actual TrMGs
* **WHY:** Dichotomizing all 39,080 cells across 11 cell types by TrMG score compares macrophages/fibroblasts against lymphocytes, isolating generic lineage markers (*CTSS*, *S100A11*, *TUBB*) rather than tryptophan metabolism regulators.
* **WHAT:** Either (a) perform feature selection and machine learning strictly within the 48 curated TrMGs to identify which actual tryptophan enzymes/transporters (e.g., *IDO1*, *KYNU*, *KMO*, *TDO2*, *SLC7A5*) distinguish UC from HC, or (b) stratify the high- vs. low-TrMG comparison strictly *within* macrophages (adjusting for patient ID via pseudobulk) so cell-type identity does not confound the DEG list.
* **HOW:** Subset the Seurat object to macrophages (`subset(seurat_obj, idents = "Macrophages")`), compute pseudobulk expression per donor ($13$ UC, $14$ HC), correlate genes with the macrophage TrMG score controlling for cell count, and re-run the machine-learning feature selection on the 48 TrMGs directly.

#### 2. Remove Circular "Validation" Tests and Report Calibrated GSEA Statistics
* **WHY:** Re-testing *CTSS*, *S100A11*, and *TUBB* between the high- and low-TrMG groups in Figure 5d repeats the exact selection filter from Figure 2g. In Figure 5g, reporting `NSE = 1.2918` without an adjusted $p$-value or FDR does not establish statistical significance.
* **WHAT:** Remove Figure 5d as a "validation" claim, fix `NSE` to `NES`, and report the exact permutation $p$-value and Benjamini–Hochberg FDR $q$-value for the KEGG tryptophan metabolism pathway in Figure 5g.
* **HOW:** Extract `pvalue` and `p.adjust` from the `clusterProfiler::GSEA` result object for Figure 5g and display them on the plot and in the text.

#### 3. Standardize Single-Cell Module Scores Before Averaging and Use Patient-Level Pseudobulk Testing
* **WHY:** `AUCell`, `UCell`, `singscore`, `ssGSEA`, and `AddModuleScore` produce values on completely different scales (some strictly positive in $[0,1]$, others mean-centered around $0$ or spanning large positive/negative ranges). Averaging raw scores weights the composite score by whichever algorithm has the largest numerical variance.
* **WHAT:** Z-score standardize (or rank-normalize) each of the five single-cell module scores across cells before computing their mean, and test UC vs. HC differences at the donor level ($n = 13$ vs. $n = 14$).
* **HOW:** Apply `scale()` to each of the five score columns in `seurat_obj@meta.data` prior to averaging, aggregate the mean composite score per donor and cell type, and compare UC vs. HC donors using a two-sample Wilcoxon rank-sum test ($N = 27$).

#### 4. Correct the Misclassification of *CTSS*, *S100A11*, and *TUBB* in the Title, Abstract, and Conclusions
* **WHY:** Calling *CTSS*, *S100A11*, and *TUBB* "key tryptophan metabolism-related genes" and "key regulators of tryptophan metabolism" misleads readers about the biochemical identity of these proteins, and the Abstract's claim that *TUBB* is predominantly expressed in macrophages contradicts Results line 139.
* **WHAT:** Accurately describe *CTSS*, *S100A11*, and *TUBB* as macrophage/stromal-associated transcripts whose expression co-varies with tryptophan pathway activity in inflamed UC mucosa, and correct the cell-type attribution of *TUBB* in the Abstract.
* **HOW:** Revise Abstract lines 21–26 and Conclusion line 176 to state that *CTSS*, *S100A11*, and *TUBB* are UC-upregulated genes correlated with cellular TrMG scores rather than metabolic enzymes or direct regulators of tryptophan catabolism.

#### 5. Purge Template-Pasted Methods and Fix Corrupted GEO Accessions and Discrepancies
* **WHY:** The Methods contain multiple paragraphs describing oncology analyses that were never performed, a non-existent GEO accession, and numerical contradictions with the Results.
* **WHAT & HOW:**
  1. **Line 52 (`GSE887466`):** Correct the bulk training dataset accession `GSE887466` (which does not exist in GEO; likely `GSE87466`, a mucosal microarray cohort of UC patients and controls) and note that `GSE87466` and `GSE53306` are microarray datasets rather than "Bulk RNAseq data."
  2. **Line 87 (Survival analysis):** Delete *"Subtype-specific overall survival (OS) was estimated and compared employing the Kaplan-Meier method and log-rank test,"* which is an artifact copied from a cancer survival manuscript.
  3. **Line 72 (GSVA risk groups) & Line 77 (`Scenic`):** Delete the unexecuted GSVA "distinct risk groups" section and the unexecuted `SCENIC` regulatory network sentence, or provide the corresponding results.
  4. **Line 62 vs. Line 106:** Reconcile Methods line 62 (*"with the top 100 most correlated genes being included"*) with Results line 106 (*"identified 385 genes significantly related to tryptophan expression ($r > 0.1, p < 0.01$)"*).
