# Review of FEXP_ANON_081

**Overall Score:** **3.1 / 10.0** (Flawed / Overstated) | **Scientific Core Score:** **2.5 / 8.0**  
* **Score Breakdown:** Rigor: 0.9/3.5 | Claims: 0.7/2.5 | Biology: 0.9/2.0 | Reproducibility: 0.6/2.0

---

## 1. Blinded Metadata Perception

* ** Perceived Role / Domain:** Template multi-step bioinformatics biomarker discovery study combining GEO bulk transcriptomics, WGCNA, consensus clustering, CIBERSORT, machine learning classifiers, scRNA-seq reanalysis, and a small mouse qPCR validation in atherosclerosis.
* ** Blinded Document Assessment:** The manuscript follows a highly formulaic bioinformatics pipeline structure ("DEGs + WGCNA + FerrDb/GenAge intersection + ConsensusClusterPlus + CIBERSORT + 8 ML models + SingleR/Monocle3/CellChat + $n=3$ mouse qPCR") containing numerous internal contradictions, dataset misidentifications, and biologically invalid trajectory inferences.

---

## 2. Executive Summary & Editorial Verdict

This study attempts to identify diagnostic biomarkers linking ferroptosis and cellular senescence in atherosclerosis (AS) by analyzing bulk arterial expression datasets (`GSE10097` [sic] and `GSE132651`), single-cell RNA-seq data from human carotid endarterectomy plaques (`GSE159677`, $n = 6$ samples from 3 patients), and an in vivo mouse model ($n = 3$ wild-type C57BL/6 on normal diet vs. $n = 3$ $ApoE^{-/-}$ on high-fat diet). The authors intersect 2,288 bulk DEGs with 3,695 WGCNA module genes, 905 ferroptosis genes (FerrDb V2), and 866 senescence genes (GenAge) to obtain 23 candidate genes (CF-DEGs). They then cluster the 69 AS samples into two subtypes ($k = 2$), identify 421 between-subtype DEGs, run PPI network centrality (CytoHubba) and eight machine learning algorithms (selecting LASSO) to nominate `IL1B` and `CCL4`, and report elevated `Il1b` and `Ccl4` mRNA in $ApoE^{-/-}$ aortas.

**Editorial Verdict: Reject (Flawed / Overstated).** The manuscript suffers from critical methodological, statistical, and biological defects across every stage of its pipeline. First, the primary training dataset is misidentified and misrepresented: the authors repeatedly state that `GSE10097` (104 arterial samples: 69 AS and 35 controls on platform `GPL96`) was *"generated from transcriptome sequencing"* (RNA-seq), whereas `GPL96` is an Affymetrix DNA microarray and the 104-sample arterial dataset in GEO is actually `GSE100927` on Agilent `GPL17077`. Second, the biomarker selection pipeline commits multi-stage circular data leakage by selecting DEGs and WGCNA modules using case-control labels on the 104-sample training cohort before training eight machine learning models on the same samples, and relies on unadjusted $P < 0.05$ thresholds for both bulk DEGs and subtype DEGs. Third, the CIBERSORT immune deconvolution is run on the 421 subtype DEGs rather than the full transcriptome, violating the LM22 signature matrix requirements. Fourth, the Monocle3 pseudotime analysis in Figure 11e models a biologically impossible developmental trajectory in which monocytes and macrophages differentiate into vascular smooth muscle cells (VSMCs). Finally, the animal experiment ($n = 3$ vs. $n = 3$) simultaneously varies genotype (wild-type vs. $ApoE^{-/-}$) and diet (normal vs. high-fat) and is statistically underpowered.

### Specific Conclusions and Assessment of Support

* **Identification of 23 ferroptosis- and senescence-related DEGs (CF-DEGs) and 421 subtype DEGs in bulk AS transcriptomes: [Methodologically Flawed].**  
  Both differential expression steps (`limma` on `GSE10097` [sic] and between ConsensusClusterPlus subtypes A and B) use an unadjusted $P < 0.05$ cutoff (`|logFC| >= 0.5, P < 0.05`) without Benjamini–Hochberg false discovery rate (FDR) control across ~20,000 probes, inflating false positives. Moreover, the primary accession `GSE10097`, platform `GPL96`, and assay type ("transcriptome sequencing") are misstated.
* **CIBERSORT immune infiltration differences across eight immune cell subsets between AS molecular subtypes: [Methodologically Flawed].**  
  In both the Methods and Results, the authors state that CIBERSORT was executed *"based on differentially expressed genes between subtypes"* ("Immune infiltration analysis of the 421 key genes was performed using the 'CIBERSORT' package"). CIBERSORT requires un-subsetted gene expression matrices covering the 547 genes in the LM22 reference matrix; feeding only 421 DEGs invalidates the support vector regression deconvolution. Wilcoxon rank-sum tests across the 22 cell types are also reported without multiple-testing correction.
* **Machine learning diagnostic nomogram based on `IL1B` and `CCL4` accurately predicts early-stage AS onset (AUC = 0.931 and 0.825): [Overstated].**  
  The 421 candidate features input to the eight machine learning classifiers were derived from 23 CF-DEGs that had already been filtered for case-vs.-control differential expression and WGCNA trait correlation on the exact same 104 training samples, inducing severe feature-selection leakage. Furthermore, `IL1B` and `CCL4` are generic pro-inflammatory myeloid markers rather than specific indicators of ferroptosis or cellular senescence, and the external validation set (`GSE132651`, $n = 6$ vs. $n = 13$) measures coronary endothelial reactivity in blood-derived endothelial cells from young subjects rather than atherosclerotic plaque onset.
* **Single-cell pseudotime trajectory showing dynamic transition of macrophages and monocytes into VSMCs regulated by `IL1B` and `CCL4`: [Methodologically Flawed].**  
  Figure 11e explicitly depicts a *"Trajectory of macrophage and monocyte differentiation into VSMC cells predicted by the Monocle3 algorithm"*, and Figure 11d connects all six annotated lineages (endothelial cells, fibroblasts, VSMCs, T cells, monocytes, macrophages) along a single developmental graph. Myeloid cells do not differentiate into mesenchymal VSMCs; applying Monocle3 across developmentally disjoint lineages produces meaningless pseudotime trajectories.
* **Experimental validation of `IL1B` and `CCL4` upregulation in $ApoE^{-/-}$ atherosclerotic mice: [Fragile].**  
  With only $n = 3$ mice per group, an unpaired parametric $t$-test cannot verify distributional assumptions and has minimal statistical power. In addition, comparing wild-type C57BL/6 mice on normal chow against $ApoE^{-/-}$ mice on a 24-week high-fat diet confounds genetic $ApoE$ deficiency with dietary lipid overload.

---

## 3. Forensic Defect Inventory

1. **Dataset Accession, Platform, and Assay Misrepresentation (Pillar 2 & Pillar 7):**
   * **Location:** Methods ("Data Acquisition and Processing", line 30) and Results ("Single-Cell Analysis Results", line 165).
   * **Defect:** The authors claim `GSE10097` is on the `GPL96` platform, *"was generated from transcriptome sequencing and contains 104 arterial tissue samples, including 69 Atherosclerosis samples and 35 non-Atherosclerosis controls."* In NCBI GEO, `GSE10097` is a 2008 study of human B-cell subsets, whereas the 104-sample human arterial dataset (69 atherosclerotic vs. 35 control arteries) is `GSE100927` on Agilent microarray platform `GPL17077`. Furthermore, neither `GPL96` nor `GPL17077` is "transcriptome sequencing" (RNA-seq); both are microarrays, making the use of `limma::normexp` and `normalizeBetweenArrays` (line 37) inconsistent with the text's description of RNA-seq data.
2. **Absence of Multiple-Testing Correction in Differential Expression and Immune Deconvolution (Pillar 4):**
   * **Location:** Methods ("Screening of Differentially Expressed Genes", line 37; "Consensus Clustering Analysis of Genes", line 47; "Immune Infiltration Analysis", line 52) and Results (lines 108, 127, 135).
   * **Defect:** Both genome-wide DEG screening steps use raw $P < 0.05$ (`|logFC| >= 0.5` and `P-value < 0.05`) instead of FDR-adjusted $q$-values. Across ~20,000 genes, raw $P < 0.05$ yields ~1,000 false positives under the complete null. Similarly, the 22 Wilcoxon rank-sum tests in CIBERSORT (line 135, reporting e.g. plasma cells at $p = 0.04$ and Tfh at $p = 0.036$) lack FDR adjustment.
3. **Invalid Restricted-Gene Input to CIBERSORT (Pillar 3):**
   * **Location:** Methods (line 52: *"The 'CIBERSORT' package in R was used to perform immune infiltration analysis based on differentially expressed genes between subtypes"*) and Results (line 135: *"Immune infiltration analysis of the 421 key genes was performed using the 'CIBERSORT' package"*).
   * **Defect:** Deconvolution via CIBERSORT requires expression values across the full 547-gene LM22 leukocyte signature matrix. Restricting the input expression matrix to the 421 subtype DEGs removes the majority of cell-type-defining marker genes in LM22, rendering the inferred cell fractions (such as "naive CD4 T cells" and "Macrophages M0") mathematical artifacts.
4. **Two-Stage Data Leakage in Machine Learning Biomarker Discovery (Pillar 2 & Pillar 3):**
   * **Location:** Methods ("Screening and Validation of Diagnostic Biomarkers", line 57) and Results (line 146, Figures 7–8).
   * **Defect:** The 23 CF-DEGs were selected using the full 104-sample training cohort (`GSE10097` [sic]) by requiring significant differential expression and WGCNA module correlation with the AS vs. control label. Those 23 CF-DEGs were then used to define subtypes among AS patients and extract 421 DEGs, which were subsequently fed into eight supervised ML models (DT, XGBoost, C5.0, NNET, KNN, LASSO, SVM, GBM) to predict AS vs. control on the same training cohort. Because feature selection used the test labels of the training set outside cross-validation, the training AUCs (`0.931` for `IL1B`, `0.825` for `CCL4`) and residual distributions (Figure 7c–e) suffer from optimistic selection bias.
5. **Biologically Invalid Monocle3 Trajectory Across Disjoint Cell Lineages (Pillar 3 & Pillar 6):**
   * **Location:** Results ("Single-Cell Analysis Results", line 165) and Figure 11d–e.
   * **Defect:** Figure 11e is explicitly captioned *"Trajectory of macrophage and monocyte differentiation into VSMC cells predicted by the Monocle3 algorithm"*, and Figure 11d places endothelial cells, fibroblasts, macrophages, monocytes, T cells, and VSMCs onto a single connected pseudotime graph. Hematopoietic myeloid cells (monocytes/macrophages) and lymphoid T cells do not differentiate into mesenchymal VSMCs or endothelial cells.
6. **Internal Contradictions in Single-Cell Clustering and Annotation (Pillar 7):**
   * **Location:** Methods (line 67) vs. Results (line 165) vs. Figure 10d–h.
   * **Defect:** Methods line 67 states that clustering results *"were annotated based on literature searchings."* Results line 165 contradicts this, stating *"Principal component analysis and clustering analysis of the dataset identified 15 clusters (Figure 10c and d). After annotation using the 'SingleR' package, six different cell types were identified... Further analysis of IL1B and CCL4 expression across the 12 cell types..."*, while Figure 10d caption states *"Cells were clustered into 14 distinct groups."* The cluster/cell-type counts (15 vs. 14 vs. 12 vs. 6) and annotation method (manual literature vs. automated SingleR) contradict one another within the same paragraph.
7. **Confounded and Underpowered Animal Experiment with Methodological Inconsistencies (Pillar 4 & Pillar 6):**
   * **Location:** Methods ("Animals", line 75; "qPCR Analysis", line 85; "Statistical Analysis", line 100) and Figure 12.
   * **Defect:** The control group ($n = 3$) consists of wild-type C57BL/6 (misspelled `C56BL/6` in line 75) mice on a normal diet, whereas the model group ($n = 3$) consists of $ApoE^{-/-}$ mice on a high-fat diet. This design confounds genetic knockout with diet. A sample size of $n = 3$ biological replicates per group is insufficient to justify an unpaired $t$-test. Furthermore, line 85 states *"The total RNA of the cells was extracted"* and *"The experiment was repeated three times"*, leaving it unclear whether the $n = 3$ reported in Figure 12 represents biological replicates (3 mice) or technical qPCR triplicates.

---

## 4. Quantitative Rubric Scoring

| Rubric Dimension | Score | Max | Forensic Justification |
| :--- | :---: | :---: | :--- |
| **1. Methodological & Statistical Rigor** | **0.9** | **3.5** | Unadjusted $P < 0.05$ in microarray DEG screens; invalid 421-DEG input to CIBERSORT; feature-selection leakage into the 8 ML classifiers; Monocle3 run across unrelated cell lineages; $n = 3$ parametric $t$-test. |
| **2. Claim-to-Evidence Alignment** | **0.7** | **2.5** | Claims that `IL1B` and `CCL4` are specific ferroptosis- and senescence-related diagnostic biomarkers for early AS are unsupported; both are canonical inflammatory myeloid cytokines/chemokines selected via circular filtering. |
| **3. Data Integrity & Biological Plausibility** | **0.9** | **2.0** | Misidentification of `GSE10097` (actually `GSE100927`) and false claim that `GPL96` microarray data are "transcriptome sequencing"; biologically impossible monocyte/macrophage-to-VSMC differentiation trajectory; confounded mouse control group. |
| **4. Reproducibility & Data Integrity** | **0.6** | **2.0** | Public GEO accessions are cited (though `GSE10097` is wrong), but no analysis scripts or ML model code are provided, and internal numbers (15 vs. 14 clusters; 6 vs. 12 cell types; manual vs. SingleR annotation) conflict. |
| ** Scientific Core Score** | **2.5** | **8.0** | Sum of Rigor + Claims + Biology. |
| ** Total Composite Score** | **3.1** | **10.0** | **Flawed / Overstated** |

---

### 5. Constructive and Doable Suggestions for Improvement

1. **Correct Dataset Provenance and Preprocessing:** Verify the exact GEO accession (`GSE100927` vs. `GSE10097`) and microarray platform, remove all claims that `GPL96`/`GPL17077` datasets were generated by "transcriptome sequencing," and apply Benjamini–Hochberg FDR correction ($\text{FDR} < 0.05$) to all `limma` differential expression analyses.
2. **Eliminate Feature-Selection Leakage in Machine Learning:** Nest all feature selection (DEG filtering, WGCNA module selection, and LASSO penalty tuning) strictly inside outer cross-validation folds on the training cohort, and report out-of-fold AUCs and calibration curves with 95% bootstrap confidence intervals.
3. **Re-run CIBERSORT on the Full Transcriptome:** Supply the complete normalized gene expression matrix (containing all available LM22 signature genes) to CIBERSORT rather than the 421 subtype DEGs, and adjust Wilcoxon $P$-values across the 22 immune cell types using the Benjamini–Hochberg procedure.
4. **Restrict Monocle3 Pseudotime to Biologically Connected Lineages:** Subset the `GSE159677` scRNA-seq object to the myeloid compartment (monocytes and macrophages) before running `monocle3::learn_graph` and `order_cells`, removing the artifactual monocyte-to-VSMC and T-cell differentiation trajectories in Figure 11d–e, and reconcile the conflicting cluster counts (6 vs. 12 vs. 14 vs. 15) in the text and figure legends.
5. **Expand and Properly Control the In Vivo Validation:** Include an age-matched $ApoE^{-/-}$ normal-diet control group (or C57BL/6 high-fat diet group) with at least $n = 6\text{--}8$ biological replicates (individual mice) per group to separate dietary and genetic effects with adequate statistical power.
