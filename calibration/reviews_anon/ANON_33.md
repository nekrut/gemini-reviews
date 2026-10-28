# Review of ANON_33

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **9.1 / 10.0** (Exemplary)  
* **Score Breakdown:** Rigor: 3.3/3.5 | Claims: 2.3/2.5 | Biology: 1.8/2.0 | Reproducibility: 1.7/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript re-evaluates widely cited signals of polygenic adaptation on human height across modern and ancient European populations ($Q_X$ overdispersion, latitudinal clines, and ancient hunter-gatherer/farmer/steppe differences) and within the British population (trait Singleton Density Score, tSDS). Comparing summary statistics from the heterogeneous GIANT consortium meta-analysis ($N = 253,288$) against the more homogeneous UK Biobank White British GWAS controlled for 10 principal components ($N = 336,474$), a UK Biobank linear mixed model GWAS ($N = 459,327$), unadjusted UK Biobank cohorts, and within-family sibling GWAS estimates across 1,112 ancient and 1,005 modern 1000 Genomes individuals plus 19 POPRES populations, the authors demonstrate that strong polygenic adaptation signals at sub-significant SNPs vanish or severely attenuate when using well-controlled UK Biobank or sibling summary statistics. They show that despite high genome-wide effect-size concordance between GIANT and UK Biobank ($r_g = 0.94 \pm 0.0078$), GIANT effect sizes covary systematically with European North–South population structure PCs and GBR–TSI allele frequency differences, which also align with demographic clines in UK10K singleton density to generate spurious tSDS correlations ($\rho = 0.078, p = 1.55 \times 10^{-65}$ in GIANT vs. $p = 0.077$ in UK Biobank). Full source data and reproducible code repositories on GitHub are provided.

This is a rigorous, self-correcting methodological and empirical investigation that resolves a major problem in human evolutionary genomics. The study systematically varies GWAS cohort composition, PC adjustment, sibling-based estimation, and SNP clumping/thresholding strategies to isolate how tiny systematic biases per SNP accumulate across thousands of sub-significant loci to dominate polygenic score comparisons. Only minor technical and editorial issues exist—such as a sign discrepancy in the reported UK Biobank tSDS Spearman correlation between the text and Figure 1b caption, use of 1000 Genomes Phase 1 rather than Phase 3 for PC loading regressions, and minor typographical omissions in the text equations.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Polygenic adaptation signals for height based on sub-significant SNPs (both between-population polygenic score differences and within-UK tSDS correlations) are driven by uncorrected population stratification in GIANT: [Well Supported].**  
  The authors demonstrate that GIANT betas correlate significantly with 1000 Genomes PC loadings (specifically PCs 4 and 11, which track the GBR–TSI North–South cline; Figure 2a,c) and that deliberately omitting PC correction in a multi-ancestry UK Biobank GWAS (`UKB all no PCs`) reproduces the artificial GIANT polygenic score clines and tSDS slopes (Figure 2—figure supplements 1–3, Figure 3a,c).

* **Demographic stratification in Singleton Density Scores (SDS) interacts with stratified GWAS betas to create false-positive tSDS selection signals: [Well Supported].**  
  Because northern Europeans (GBR) have lower genetic diversity and thus lower singleton density (higher SDS) for alleles common in the north compared to southern Europeans (TSI) (Figure 2b,d), aligning SDS with north-biased GIANT betas yields a highly significant false-positive correlation across the entire $P$-value spectrum that can be mimicked simply by substituting GBR–TSI allele frequency differences for SDS (Figure 3a vs. 3c).

* **Family-based sibling GWAS estimates in the UK Biobank (`UKB sibs WB`) eliminate residual $Q_X$ overdispersion and restore uniform null $P$-value calibration: [Well Supported].**  
  Random draws of ~1,700 independent SNPs in POPRES show inflated $Q_X$ and latitude $P$-values for standard UK Biobank GWAS summary statistics, whereas within-sibling UK Biobank effect estimates yield a uniform null $P$-value distribution (Figure 4—figure supplement 3) and eliminate population-level $Q_X$ overdispersion ($P_{Qx} > 0.05$, Figure 4).

* **A modest residual signal of selection persists at independent genome-wide significant SNPs ($p < 5 \times 10^{-8}$), including in within-sibling tSDS: [Moderately Supported].**  
  Restricting to 506 LD-independent genome-wide significant UK Biobank SNPs polarized by within-sibling beta signs shows a positive tSDS shift (Figure 3b) without significant GBR–TSI frequency differentiation (Figure 3d). However, because SNP ascertainment ($p < 5 \times 10^{-8}$) was still performed in the population-level UKB GWAS before polarizing with sibling betas—and ancient HG/EF/SP scores shift even at genome-wide significant SNPs depending on the discovery cohort—the authors appropriately remain cautious about interpreting this residual signal.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Separate Discovery Ascertainment from Sibling Effect Estimation in the Genome-Wide Significant tSDS Test
* **WHY:** In Figure 3b, the 506 LD-independent SNPs were ascertained as genome-wide significant ($p < 5 \times 10^{-8}$) in the population-level UKB GWAS and then polarized by the sign of the beta coefficient from the UKB within-sibling analysis. While polarizing by sibling beta sign removes directional bias in effect estimation, conditioning on $p < 5 \times 10^{-8}$ in the population GWAS can still ascertain SNPs whose marginal association test statistic was boosted by subtle within-UK structure or high derived allele frequency.
* **WHAT:** Test whether the positive mean tSDS shift in Figure 3b holds when SNP discovery/ranking is performed entirely within an independent cohort or using sibling-only $P$-values, or quantify the expected ascertainment shift via simulation.
* **HOW:** Compute the mean and $t$-test/permutation $P$-value of tSDS for the top $K$ (e.g., $K = 100, 500, 1700$) LD-pruned SNPs ranked strictly by `UKB sibs WB` $P$-values, and compare against the population-ascertained set in Figure 3b.

#### 2. Harmonize 1000 Genomes Phase 1 and Phase 3 Panels Across PCA and Polygenic Score Analyses
* **WHY:** Polygenic scores and LD clumping use the 1000 Genomes Phase 3 release ($N = 1,005$ across 10 populations; Materials and methods, "Population genetic data for ancient and modern samples"), whereas the PC loading regressions in Figure 2 use the older 1000 Genomes Phase 1 dataset (Materials and methods, "Population structure analysis").
* **WHAT:** Confirm that the PC loading correlations in Figure 2a–b are consistent when computed on the same 1000 Genomes Phase 3 European/global samples used in Figure 1.
* **HOW:** Re-run the PLINK PCA and SNP loading regressions on the 1000 Genomes Phase 3 genotype matrix (MAF $> 0.05$, LD-pruned at $r^2 < 0.2$) and verify that the GBR–TSI-correlated PCs yield identical correlation profiles with GIANT, UKB, and SDS.

#### 3. Technical, Mathematical, and Editorial Cleanup
* **WHY:** Minor sign mismatches and missing mathematical operators in the text formatting should be corrected for clarity.
* **WHAT & HOW:**
  1. **Results ("Discrepancies in GWAS: height evolution within a single population") vs. Figure 1b caption:** The main text reports the UK Biobank tSDS Spearman correlation as `ρ = 0.009, p=0.077`, whereas the Figure 1b caption (two occurrences) reports `Spearman r = −0.009, p=0.077`. Reconcile the sign (`+0.009` vs. `-0.009`) with `Figure 1—source data 1`.
  2. **Materials and methods ("Polygenic scores"):** Fix the typographical rendering of the standardized score formula from `Al polygenic scores are plotted in centered standardized form (Z-μVA)` to `All polygenic scores are plotted in centered standardized form ((Z - μ) / √VA)`, and fix the 95% credible interval width formula from `1.96VZ` to `1.96√VZ`.
