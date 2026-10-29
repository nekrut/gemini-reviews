<Blinded Review: TIME_ANON_0965>
**Composite Score:** 8.4 / 10.0 (Rigor: 3.1/3.5 | Claims: 2.2/2.5 | Biology: 1.6/2.0 | Reproducibility: 1.5/2.0)
**Bias Category:** None (Methodologically Sound)
**Verdict:** Minor Revision
**Study Modality:** Dry-Lab Secondary Cohort/Database
**Technology Maturity:** Mid-Stage High-Throughput
**Epistemic Stage:** Translational/Preclinical/Biomarker

OVERALL_SCORE: 8.4/10
VERDICT: PASS
ESTIMATED_DECADE: 2010s

---

### 1. Executive Summary / SUMMARY
This quantitative genetics and animal breeding study investigates how the effective evolutionary "age" (coalescence depth) of genetic relationship matrices affects the accuracy of genomic selection (`GS`) in an elite commercial pig breeding population (`Norsvin` Norwegian Landrace; 8,187 pedigreed animals across 5 generations, of which 3,250 animals—2,553 boars and 697 nucleus dams—were genotyped for 38,453 informative SNPs on the Illumina `PorcineSNP60` array). The authors hypothesize that standard pedigree relationships (`A`) and genome-wide linkage analysis relationships (`G_LA`, computed via `LDMIP` segregation probabilities averaged across all 38,453 marker loci) trace relationships that are too recent, whereas single-SNP identity-by-state (`IBS`) genomic relationship matrices (`G`, VanRaden method) trace relationships back to ancient SNP mutations ($1/(2\nu)$ generations ago, inflated by high-MAF SNP ascertainment) that predate more recent quantitative trait locus (`QTL`) mutations under artificial selection. To capture intermediate-aged relationships (~223 generations ago, matching the 18th/19th-century European–Asian pig hybridization and maximizing haplotype heterozygosity $\text{Het} = 4N_e\theta/(1+4N_e\theta) \approx 0.47$ for $N_e \approx 100$ and $\theta \approx 0.0022$), the authors construct a dynamic-boundary haplotype relationship matrix (`G_H`, 54,303 haplotype blocks averaging 8.4 SNPs, split whenever distinct phased `Beagle` alleles exceed 10).

To incorporate phenotypic records from ungenotyped pedigree members (up to 4,143 ungenotyped records for 3-week weight `W3W` and 3,626 for teat number `NT`) without the scaling and founder-adaptation biases of single-step `H`-matrix (`ssGBLUP`) methods, the authors impute genotype/haplotype probabilities via `LDMIP` and add the conditional residual relationship matrix $\mathbf{R} = \mathbf{G}_{\text{LA},11} - \mathbf{G}_{\text{LA},12}\mathbf{G}_{\text{LA},22}^{-1}\mathbf{G}_{\text{LA},21}$. Evaluating forward prediction accuracy on masked phenotypes of the youngest 424–486 selection candidates across four traits (`GR` growth rate, `M%` CT lean meat percentage, `W3W` 3-week weight, and `NT` number of teats) using a paired trivariate likelihood-ratio test in `ASReml`, they show that relationship variance increases strictly in the expected temporal order (`A [0.00129] < G_LA [0.00145] < G_H [0.00219] < G [0.00292]`), that `G` and `G_H` significantly outperform `A` and `G_LA`, and that `G_H` slightly (though non-significantly) outperforms `G` for the two heavily selected production traits (`GR`: $r_{\text{GS}} = 0.370$ vs. $0.353$; `M%`: $0.620$ vs. $0.609$).

### 2. Methodological & Statistical Audit / STRENGTHS & WEAKNESSES & METHODOLOGICAL AUDIT

#### Strengths
1. **Coalescent & Population-Genetic Grounding of Relationship Matrix Depth:** The theoretical framing linking relationship matrices (`A`, `G_LA`, `G_H`, `G`) to base-population coalescence time ($1/(2\theta)$ vs. $1/(2\nu)$), effective population size ($N_e \approx 100$), expected multi-allelic haplotype heterozygosity ($\text{Het} = 0.47$), and off-diagonal relationship variance (`Table 2`) is exceptionally clear and mathematically rigorous.
2. **Unbiased Forward Validation on Masked Phenotypes Rather Than Deregressed Proofs (`DP`):** The authors provide a sharp algebraic proof (`Cov(GEBV, DP) = Cov(GEBV, TBV) + Cov(GEBV, ERR)`) showing why validating genomic selection on deregressed proofs or daughter yield deviations inflates apparent prediction accuracy when training and validation records share linear-model estimation errors, and instead validate directly on masked raw phenotypes adjusted for non-genetic fixed/random effects via Equation (1): $1 - \rho_x^2 = (1 - \rho_0^2)(1 - r_x^2)$.
3. **Paired Trivariate `ASReml` Likelihood-Ratio Test for Correlated Predictions:** Because competing models (`y_1^hat`, `y_2^hat`) predict the exact same validation cohort (`y_i`) and are highly correlated ($r_{12}$), standard independent Fisher-$z$ SE comparisons are underpowered. Fitting an unstructured $3 \times 3$ covariance matrix for $(y_i, \hat{y}_{1i}, \hat{y}_{2i})$ and testing the constraint $r_{01} = r_{02}$ via a 1-df LRT (`Section: Significance testing`) properly accounts for prediction covariance $r_{12}$ (equivalent to Williams' / Hotelling's test for dependent correlations).
4. **Honest Reporting of Null/Non-Significant Differences Between `G_H` and `G`:** Despite developing the `G_H` method as the central hypothesis of the paper, the authors do not exaggerate its performance: they state in the Abstract, Results, and Discussion that the accuracy gains of `G_H` over `G` for `GR` (`0.307` vs. `0.294`) and `M%` (`0.475` vs. `0.468`) are not statistically significant and explain this via the bias–variance trade-off of fitting 54,303 multi-allelic haplotype blocks vs. 38,453 biallelic SNPs in a training set of ~2,500 genotyped animals.

#### Weaknesses & Minor Issues
1. **Minor Addition Typo in `Table 1` (`Number of phenotypes` for `GR`):**
   - In `Table 1`, for Growth Rate (`GR`), the row `Genotyped` is `2504` and `Non-genotyped` is `154`. Their sum is $2,504 + 154 = \mathbf{2,658}$, whereas the `Total` row lists **`2668`** (a 10-record typo in either `Total`, `Genotyped` [`2514`], or `Non-genotyped` [`164`]). Similarly, in the Abstract (line 9), the total number of phenotypes for `NT` (number of teats) is stated as **`5851`**, whereas `Table 1` correctly lists `Total = 6851` ($3,225\text{ Genotyped} + 3,626\text{ Non-genotyped} = 6,851$).
2. **Fixed Pedigree-Estimated Variance Components Across All Relationship Matrices:** As noted in Methods line 61, the additive genetic variance $\sigma_a^2$ estimated from pedigree `A` was held fixed across `A`, `G_LA`, `G_H`, and `G` rather than re-estimated per matrix, though the authors justify this by showing in `Table 2` that the regression coefficients $B$ of `G_LA` (`1.001`), `G_H` (`0.925`), and `G` (`0.922`) onto `A` are close to `1.0`.

### 3. Biological / Experimental Grounding & Claim Proportionality
- **Claim 1:** Off-diagonal relationship variance and effective coalescence age increase in the order `A < G_LA < G_H < G`, with regressions onto younger relationships near 1.0. `[Well Supported]`
- **Claim 2:** `G` and `G_H` yield significantly higher genomic prediction accuracy than pedigree (`A`) and linkage analysis (`G_LA`) in this pig breeding cohort (where only ~1 generation of genotyped animals limits within-family linkage tracking by `G_LA`). `[Well Supported]`
- **Claim 3:** Intermediate-aged haplotype relationships (`G_H`) tend to improve prediction accuracy slightly over `G` for heavily selected traits (`GR`, `M%`), but the difference is not statistically significant at the current sample size ($N = 3,250$ genotyped pigs). `[Well Supported]` — Exemplary scientific restraint.

### 4. Reproducibility & Data Completeness
- **Algorithmic & Mathematical Completeness:** All linear mixed models, variance components (`Table 1`), relationship matrix equations (`G*`, `R`, `G_H` dynamic 10-allele boundary rule), validation accuracy derivations (`Eq. 1`), and LRT covariance structures are specified with complete mathematical clarity.
</Blinded Review: TIME_ANON_0965>
