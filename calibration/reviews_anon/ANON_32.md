# Review of ANON_32

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **9.0 / 10.0** (Exemplary) | **Scientific Core Score:** **7.1 / 8.0**  
**Overall Score:** 9.0 / 10.0  
* **Score Breakdown:** Rigor: 3.1/3.5 | Claims: 2.2/2.5 | Biology: 1.8/2.0 | Reproducibility: 1.9/2.0  
**Score Breakdown:** Methodological Rigor: 3.1/3.5 | Claim-Evidence Alignment: 2.2/2.5 | Biological Plausibility: 1.8/2.0 | Reproducibility: 1.9/2.0  
**Verdict:** Exemplary

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT (Executive Summary)

This manuscript provides a comprehensive architectural and statistical review of the `limma` R/Bioconductor software package for gene expression analysis across microarrays, high-throughput PCR, protein arrays, and RNA sequencing (RNA-seq). The authors synthesize the core statistical principles unifying the package: (1) row-wise linear models (`lmFit`, `contrasts.fit`) that analyze entire multi-factor experimental designs simultaneously, (2) parametric empirical Bayes moderation of residual variances (`eBayes`) incorporating mean-variance trends (`trend=TRUE`) and robust gene-wise outlier hyperparameter estimation (`robust=TRUE`), (3) observation-level and sample-level precision weights (`voom`, `arrayWeights`, `voomWithQualityWeights`) that unlock normal linear modeling and random-effects blocking (`duplicateCorrelation`) for heteroscedastic RNA-seq read counts, (4) thresholded hypothesis testing (`treat`) and exon-level differential splicing (`diffSplice`), and (5) higher-order pathway and signature analyses including true-null proportion estimation (`propTrueNull`), bivariate biological correlation of contrasts (`genas`), and correlation-aware competitive (`camera`, `romer`) and self-contained residual-rotation (`roast`, `mroast`) gene set tests. Illustrative workflows and diagnostic visualizations (`plotMA`, `plotMDS`, `volcanoplot`, `barcodeplot`) are demonstrated using public datasets (`GSE2593`, `GSE52870`, Pickrell et al.).

As a software synthesis and methodological review, the paper presents a cohesive, mathematically principled framework that has set the standard for small-sample functional genomics. Its primary limitations stem from making several strong comparative performance claims in the text—particularly regarding the newly highlighted exon-level splicing module (`diffSplice`), which is claimed to be "considerably faster than alternative approaches to differential splicing" without presenting runtime or accuracy benchmarks, and the prospective extension of `limma`/`voom` to single-cell RNA-seq in the Discussion without addressing zero-inflation and extreme low-count discreteness. Expanding the discussion of these boundary conditions and adding quantitative metrics for the previously unpublished features (`diffSplice`) will strengthen the manuscript.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT (Detailed Rubric Evaluation)

* **Parametric empirical Bayes variance moderation with mean-variance trends and robust gene-wise shrinkage provides stable, exact small-sample inference across microarray and RNA-seq platforms (Section "Statistical principles", Figs. 1, 3A): [Well Supported].**  
  By pooling residual variance information across all genes to estimate a global or mean-trended prior variance ($s_0^2$) with augmented posterior degrees of freedom ($d_0 + d_g$), `limma` prevents false positives from fortuitously small sample variances in low-replicate designs ($n = 2\text{--}5$), while the robustified hyperparameter estimator (`robust=TRUE`) assigns smaller prior degrees of freedom to hyper-variable outlier genes so their variance is not over-squeezed.

* **Precision weights from `voom` and `arrayWeights` adapt normal linear modeling and random-effects blocking (`duplicateCorrelation`) to RNA-seq count data and variable-quality samples (Sections "Pre-processing RNA-seq..." & "Finding differentially expressed genes", Fig. 3): [Well Supported].**  
  Converting $\log_2$-counts-per-million (logCPM) fitted mean-variance trends into inverse-variance observation weights (`voom`) and combining them with sample-specific empirical reproducibility weights (`voomWithQualityWeights`) preserves Type I error control while unlocking random-effects intrablock correlation (`duplicateCorrelation`) and rotation tests that are intractable or computationally prohibitive under negative-binomial GLMs.

* **Variance-inflation-adjusted competitive testing (`camera`) and residual-space multivariate normal rotation (`roast`, `romer`) overcome the false-positive inflation of naive gene-sampling rank tests (Section "Higher-level analyses", Fig. 4C): [Well Supported].**  
  The authors clearly distinguish gene-sampling rank tests (`geneSetTest`, which assume conditional independence across genes and yield anti-conservative $P$-values when co-regulated genes are correlated) from `camera` (which explicitly estimates the inter-gene variance inflation factor from the linear model residuals) and `roast` (which rotates residual vectors in the orthogonal complement of nuisance covariates, preserving gene-gene covariance and accommodating directional prior weights).

* **Exon-level linear modeling in `diffSplice` provides fast, accurate differential splicing detection across continuous and categorical designs (Section "Testing for differential splicing"): [Moderately Supported].**  
  While testing for differences in $\log_2$-fold-change between individual exons and the rest of the gene via moderated $t$- and $F$-statistics within `limma` is computationally fast ($O(GN)$ time), the manuscript states that "`diffSplice`... is considerably faster than alternative approaches to differential splicing" and emphasizes "features that have not been previously described" without presenting any simulation or empirical benchmark comparing `diffSplice` against established splicing tools (`DEXSeq`, `Cuffdiff2`, `MATS`) on runtime, FDR calibration, or sensitivity.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT (Major Issues, Minor Issues, Concrete Recommendations)

#### Major Issues
1. **Unbenchmarked Performance Claims for `diffSplice` (Section "Testing for differential splicing"):** The Abstract and Introduction highlight differential splicing of RNA-seq data (`diffSplice`) as one of the two major recent expansions of `limma` "that have not been previously described." However, unlike `voom`, `camera`, `roast`, and `genas`—which are backed by dedicated methodological papers cited in the references—`diffSplice` has no cited validation paper and no mathematical specification or benchmark data in the text to support its statistical calibration or speed advantage over `DEXSeq`.
2. **Unaddressed Low-Count and Zero-Inflation Boundary Conditions for `voom` and Single-Cell RNA-Seq (Discussion):** The Discussion states that "we expect the popularity of this approach to continue to grow, with new applications in the analysis of single cell gene expression data." However, when read counts per feature are near zero across most samples (as in droplet/plate single-cell RNA-seq or unexpressed low-depth exons in `diffSplice`), $\log_2(\text{count} + 0.5)$ exhibits severe bimodal discreteness (a point mass at zeros vs. positive integers) where continuous normal linear modeling and `voom` smooth mean-variance weights can miscalibrate tail probabilities unless low-abundance features are stringently filtered.

#### Minor Issues
1. **Assumption of a Single Consensus Intrablock Correlation in `duplicateCorrelation` (Section "Blocking and random effects"):** The manuscript notes that "all genes are constrained to share the same intrablock correlation" without mentioning the potential bias if a subset of cell-cycle or donor-specific genes has much stronger within-individual correlation ($\rho \sim 0.8$) than the transcriptome-wide consensus ($\bar{\rho} \sim 0.1\text{--}0.2$).
2. **Function Name Typo in Section "Graphical exploration of data quality" (Line 61):** Line 61 refers to `(plotFG)` ("foreground–background plots mentioned above (plotFG)"), whereas line 55 and Figure 2 correctly name the function `plotFB`.
3. **Missing Symbol in Figure 1 Caption (Line 43):** In the caption to Figure 1 (line 43), the symbol for the empirical Bayes posterior variance estimator inside the parentheses `obtain posterior variance estimators ( )` is blank ($\tilde{s}_g^2$).

#### Concrete Recommendations

#### 1. Add the Mathematical Formulation and a Summary Benchmark for `diffSplice`
* **WHY:** Because `diffSplice` is presented as a primary new capability not previously published elsewhere, readers need its statistical formulation and basic operating characteristics.
* **WHAT:** Specify the exon-level linear model contrast tested by `diffSplice` (comparing each exon's $\log_2$-fold-change against the precision-weighted average of all other exons in the same gene via exon-level moderated $t$-tests and Simes/gene-level $F$-tests), and include a brief runtime and concordance comparison (e.g., against `DEXSeq`) on an example RNA-seq dataset.
* **HOW:** Add a 1-paragraph mathematical summary of `diffSplice` in Section "Testing for differential splicing" and report the wall-clock runtime (in seconds) of `voom` + `lmFit` + `diffSplice` on the `GSE52870` dataset.

#### 2. Specify Minimum Count Filtering Guidelines for `voom`, `diffSplice`, and Single-Cell Applications
* **WHY:** Applying `voom` without filtering genes/exons with very low counts or high zero fractions violates the continuity assumptions of normal empirical Bayes and linear regression.
* **WHAT:** Explicitly state the recommended minimum count threshold (e.g., `cpm > k` in at least $n_{\min}$ samples) required before running `voom` and `diffSplice`, and caveat the Discussion's single-cell remark regarding zero-inflation/dropout.
* **HOW:** Add a sentence in Section "Pre-processing RNA-seq and other sequencing data" detailing count filtering prior to `voom`, and note in the Discussion that single-cell applications require either high-coverage protocols, pseudo-bulk aggregation, or zero-inflation handling.

#### 3. Technical and Editorial Cleanup
* **WHY:** Fixing function name typos and missing notation ensures accuracy for package users.
* **WHAT & HOW:**
  1. On line 43 (Figure 1 caption), insert $\tilde{s}_g^2$ inside `obtain posterior variance estimators ( )`.
  2. On line 61 ("Graphical exploration of data quality"), change `(plotFG)` to `(plotFB)`.
