# Review of ANON_98

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **9.5 / 10.0** (Exemplary)  
* **Score Breakdown:** Rigor: 3.3/3.5 | Claims: 2.4/2.5 | Biology: 1.9/2.0 | Reproducibility: 1.9/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript presents a comprehensive empirical and theoretical benchmark of 14 statistical methods for differential expression (DE) analysis across experimental conditions in single-cell, single-nucleus, and spatial transcriptomics. Recognizing that synthetic simulations can favor methods matching the simulator's parametric assumptions, the authors curate 18 gold-standard datasets with matched bulk RNA-seq (and bulk proteomics) on the same purified cell populations from four studies, alongside an ERCC synthetic spike-in dataset, a compendium of 46 published scRNA-seq/snRNA-seq datasets, a spatial transcriptomics dataset, and `Splatter` null simulations. They demonstrate that pseudobulk methods (`edgeR`, `DESeq2`, and `limma` applied to replicate-aggregated counts) consistently outperform cell-level tests (`Seurat::FindMarkers` Wilcoxon, $t$-test, logistic regression, Poisson/NB GLMs, LRT, and `MAST`) and linear mixed models. By systematically disabling aggregation or permuting cell-to-replicate assignments into "pseudo-replicates," the authors prove that ignoring biological replicate variance causes cell-level methods to underestimate the variance of highly expressed, replicate-variable genes, generating hundreds of false-positive DE genes even when unperturbed control replicates are randomly split into two groups. They then generate a new snRNA-seq dataset of 19,237 nuclei from the mouse lumbar spinal cord after chronic thoracic spinal cord injury (SCI) and perform an in vivo `RNAscope` validation screen of 19 genes in `Pecam1+` endothelial cells ($n = 4$ mice/group), confirming 5/6 `edgeR-LRT` candidates versus only 3/13 single-cell Wilcoxon candidates. All data (`GSE165003`, Zenodo `10.5281/zenodo.5048449`), reproducible analysis code, and the `Libra` R package are publicly available.

This is an exemplary methodological and biological study that resolves a pervasive statistical flaw in single-cell transcriptomics. The experimental design—combining matched bulk RNA-seq/proteomics ground truth, negative-control ERCC spike-ins, real-data null splits across 14 cohorts, mechanistic variance decomposition ($\Delta$-variance), and blinded wet-lab `RNAscope` validation in mouse SCI—provides converging proof for its central thesis. Only minor technical points warrant clarification: in the 18 gold-standard benchmarks, using the same six bulk DE tools (`DESeq2`, `edgeR`, `limma`) to define the bulk reference rankings naturally shares distributional assumptions with pseudobulk methods, and a minor count/test discrepancy appears between the Results and Methods for the `RNAscope` screen (6 vs. 7 `edgeR-LRT` probes and use of a $\chi^2$ test instead of Fisher's exact test on $N = 19$ genes). These can be addressed with minor textual clarifications and an exact test check.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Pseudobulk DE methods (`edgeR`, `DESeq2`, `limma`) substantially outperform cell-level single-cell DE methods in recovering biological ground truth across 18 matched bulk/single-cell datasets and matched proteomics: [Well Supported].**  
  The superiority of pseudobulk aggregation holds across gene-level AUCC (Figure 1c–d), transcriptome-wide Spearman rank correlations (Supplementary Figure 1a–d), GO term GSEA concordance (Figure 1e–f), and independent bulk label-free proteomics (Supplementary Figure 1e–f). While defining bulk RNA-seq DE ground truth using the same six tools (`DESeq2-LRT/Wald`, `edgeR-LRT/QLF`, `limma-trend/voom`) shares parametric shrinkage assumptions with the pseudobulk methods, the proteomics benchmark, ERCC spike-ins, and `RNAscope` in situ hybridization provide orthogonal, model-independent confirmation.

* **Cell-level DE methods systematically underestimate the variance of highly expressed, replicate-variable genes, generating hundreds of false discoveries under the null hypothesis: [Well Supported].**  
  The two mechanistic perturbation experiments—(1) applying `edgeR`/`DESeq2`/`limma` directly to unaggregated single cells (Figure 3a–b) and (2) aggregating cells into randomized "pseudo-replicates" that destroy biological replicate structure while preserving cell counts and sparsity (Figure 3c–d)—demonstrate that accounting for inter-replicate variance ($\Delta$-variance across 98.2% of genes and all 46 datasets; Figure 3e–f), rather than zero-inflation reduction or package implementation, explains pseudobulk performance. The ERCC spike-in analysis (Figure 2d–e) and the random partitioning of unstimulated control replicates across 14 scRNA-seq studies and spatial transcriptomics (Figure 4d–f) conclusively demonstrate massive Type I error inflation in cell-level tests.

* **In chronic mouse spinal cord injury (`snRNA-seq`, 19,237 nuclei), pseudobulk `edgeR-LRT` identifies true hypoxia-associated transcriptional changes in lumbar endothelial cells (`Igfbp6`, `Slc7a11`), whereas single-cell Wilcoxon yields predominantly false positives: [Well Supported].**  
  In vivo `RNAscope` quantification in `Pecam1+` endothelial cells ($n = 4$ biological replicates per condition, 10 cells per mouse) corroborated 5/6 `edgeR-LRT`-specific DE genes versus 3/13 Wilcoxon-specific DE genes (Figure 5f–h), and immunohistochemistry confirmed atrophic `Pecam1+` blood vessels below the lesion (Figure 5i). A minor technical point is that the Results (line 130) state 6 `edgeR-LRT` genes were tested ($6 + 13 = 19$ total) and report $p < 0.05$ by a $\chi^2$ test, whereas the Methods (line 95) state `"7 genes identified by edgeR-LRT"` while listing 6 gene names, and for a $2 \times 2$ contingency table with $N = 19$, Fisher's exact test is preferable to an asymptotic $\chi^2$ test.

* **Generalized linear mixed models (GLMMs) with replicate random effects match pseudobulk accuracy at $\ge 500$ cells but require orders-of-magnitude greater computation time (mean 13.5 hours per cell type vs. minutes): [Well Supported].**  
  Evaluating eight Poisson and negative binomial GLMM parameterizations (with/without library size offsets, Wald vs. LRT; Supplementary Figure 10a–f) across downsampled cell counts (25 to 1,000 cells) thoroughly documents why count aggregation is both statistically sufficient and computationally far more tractable than cell-level GLMMs in typical scRNA-seq experiments.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Reconcile the `RNAscope` Gene Count (6 vs. 7) and Report Fisher's Exact Test alongside the $\chi^2$ Test
* **WHY:** In the Results (line 130), the text states that RNAscope probes were obtained for 19 genes and validated `"five of the six genes called as DE by edgeR-LRT"` and `"three of thirteen genes called as DE by the Wilcoxon rank-sum test (p < 0.05, χ2 test)"`. In the Methods ("RNAscope," line 95 of offset 46080), the text states `"7 genes identified by edgeR-LRT (Slc7a11, catalog no. 422511; Gjb2, catalog no. 518881; Pi16, catalog no. 451311; Rbp4, catalog no. 508501; Col1a1, catalog no. 319371; Igfbp6, catalog no. 425721)"`—which lists 6 genes, not 7. Additionally, in a $2 \times 2$ table with total $N = 19$ ($\begin{smallmatrix} 5 & 1 \\ 3 & 10 \end{smallmatrix}$), three of the four cells have expected counts $< 5$, where Pearson's $\chi^2$ approximation is less accurate than Fisher's exact test.
* **WHAT:** Change `"7 genes"` to `"6 genes"` in the Methods and report the exact Fisher's exact test $p$-value in the Results.
* **HOW:** Update the Methods ("RNAscope") to read `"6 genes identified by edgeR-LRT"` and report Fisher's exact test ($p = 0.041$ two-sided, $p = 0.022$ one-sided; odds ratio $= 13.8$) in line 130.

#### 2. Discuss the Shared Parametric Structure Between Bulk Reference DE and Pseudobulk DE in the 18 Gold-Standard Benchmarks
* **WHY:** In Figure 1c–d, bulk RNA-seq DE was computed using the same six methods (`DESeq2-LRT/Wald`, `edgeR-LRT/QLF`, `limma-trend/voom`) that constitute the six pseudobulk methods. Even when averaged across the six bulk methods, empirical Bayes dispersion/variance shrinkage is shared between the bulk reference and pseudobulk test methods.
* **WHAT:** Add a brief note in the Methods or Results clarifying that while the bulk RNA-seq AUCC benchmark shares count-model families with pseudobulk methods, the model-free bulk fold-change rankings, bulk proteomics (Supplementary Figure 1e–f), ERCC spike-ins (Figure 2d–e), and null split experiments (Figure 4d–f) confirm that the performance gap is not an artifact of shared software packages.
* **HOW:** As an additional check in Supplementary Figure 1, show that ranking the 18 bulk RNA-seq datasets purely by unshrunk empirical mean log-fold change or an ordinary Welch $t$-test across bulk replicates preserves the AUCC advantage of pseudobulk over single-cell methods.

#### 3. Technical and Editorial Cleanup
* **WHY:** A few minor typographical omissions appear in figure captions and the Methods section.
* **WHAT & HOW:**
  1. **Missing gene name in Figure 3g caption (line 80):** Change `"Left, expression of the gene c in biological replicates"` to `"Left, expression of the gene Txnrd3 in biological replicates"`.
  2. **Missing strainer mesh size in Methods ("Single-nucleus RNA sequencing," line 60 of offset 46080):** Change `"filtered through a µm cell strainer"` to specify the exact pore size (e.g., `"filtered through a 40 µm [or 70 µm] cell strainer"`).
  3. **Unformatted reference superscripts in Methods (lines 15 and 25 of offset 46080):** Change `"poly-I:C12"` to `"poly-I:C 12"` and `"dataset24"` to `"dataset 24"`.
  4. **Duplicate Roman numeral in Methods ("Literature review," line 156):** Change `"(i) studies present in the curated database... and (i) studies within the 500 most recent entries"` to `"(i) ... and (ii) ..."`.
