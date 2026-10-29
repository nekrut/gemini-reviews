# Review of ANON_22

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **9.5 / 10.0** (Exemplary) | **Scientific Core Score:** **7.7 / 8.0**  
**Overall Score:** 9.5 / 10.0  
* **Score Breakdown:** Rigor: 3.4/3.5 | Claims: 2.4/2.5 | Biology: 1.9/2.0 | Reproducibility: 1.8/2.0  
**Score Breakdown:** Methodological Rigor: 3.4/3.5 | Claim-Evidence Alignment: 2.4/2.5 | Biological Plausibility: 1.9/2.0 | Reproducibility: 1.8/2.0  
**Verdict:** Exemplary

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT (Executive Summary)

This manuscript introduces `BOLT-LMM`, a fast linear mixed model (LMM) association method that overcomes the $O(MN^2)$ / $O(N^3)$ computational and $O(N^2)$ memory bottlenecks of existing GWAS mixed models while increasing statistical power under non-infinitesimal genetic architectures. The algorithm operates in four steps requiring a small number of $O(MN)$-time iterations directly on packed 2-bit raw genotypes ($\approx MN/4$ bytes RAM): (1a) Monte Carlo REML variance component estimation via conjugate gradient iteration (circumventing GRM construction and spectral decomposition), (1b) leave-one-chromosome-out (LOCO) infinitesimal mixed-model testing (`BOLT-LMM-inf`) calibrated against prospective LMM statistics at 30 random SNPs, (2a) 5-fold cross-validation over a 2-component Gaussian spike-and-slab mixture prior fit via factored variational Bayes (iterative conditional expectation / cyclic coordinate descent), and (2b) retrospective quasi-likelihood score testing of LOCO mixture residuals calibrated via LD Score regression. Evaluated on mosaic WTCCC2 simulations up to $N = 480,000$ individuals ($M = 300,000$ SNPs) and applied to nine quantitative traits in the Women's Genome Health Study ($N = 23,294$, $M = 324,488$), `BOLT-LMM` scales empirically as $\approx O(MN^{1.5})$, matches `GCTA-LOCO` under the infinitesimal model ($R^2 > 0.999$), controls false positives under ancestry stratification, and increases association power equivalent to up to a 25% sample-size increase in simulations and up to a 10% effective sample-size gain on WGHS lipid traits (ApoB).

This is a mathematically rigorous, thoroughly validated methodological contribution. The authors verify every approximation step—benchmarking variational Bayes against an exact MCMC Gibbs sampler, verifying calibration on null chromosome halves under population stratification, and providing an unusually candid eight-point discussion of methodological boundaries (such as case-control ascertainment loss in low-prevalence diseases and single variance component limits). Only minor statistical refinements (such as increasing the default number of random SNPs used for $c_{\text{inf}}$ calibration and providing the explicit software repository URL in the main text) are recommended.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT (Detailed Rubric Evaluation)

* **`BOLT-LMM` reduces mixed-model computational complexity from $O(MN^2)$ to $\approx O(MN^{1.5})$ time and $\approx MN/4$ bytes of memory, scaling to $N = 480,000$ samples (Section "Computational cost of BOLT-LMM versus existing methods", Fig. 1, Table 1): [Well Supported].**  
  By replacing explicit $N \times N$ GRM formation and $O(N^3)$ eigendecomposition with conjugate gradient linear solvers and Monte Carlo REML trace estimation on 2-bit packed genotypes, `BOLT-LMM` completes analyses up to $N = 480,000$ within 10 days and $<96$ GB RAM, whereas `GCTA-LOCO`, `FaST-LMM`, `GEMMA`, and `EMMAX` fail above $N = 7,500\text{--}30,000$. The authors accurately characterize the empirical $O(N^{0.5})$ scaling of conjugate gradient iteration count with sample size, heritability, and relatedness.

* **Modeling non-infinitesimal architectures via a variational Gaussian mixture prior increases association power in proportion to $h_g^2 N / M_{\text{causal}}$ while controlling Type I error (Section "Power and false positive control of BOLT-LMM in simulations", Fig. 2): [Well Supported].**  
  Across ancestry-stratified WTCCC2 simulations where causal variants reside on the first halves of chromosomes and the second halves serve as null controls, `BOLT-LMM` achieves up to a 25% gain in mean $\chi^2$ at standardized-effect causal SNPs ($M_{\text{causal}} = 1,250$) over `GCTA-LOCO` and `BOLT-LMM-inf` while keeping null-chromosome mean $\chi^2$ and Type I error calibrated. Moreover, replacing Step 2b's variational Bayes updates with an MCMC Gibbs sampler at $N = 5,211$ (Supplementary Table 6a) produces statistically indistinguishable power and calibration, confirming that the factored variational approximation does not degrade inference.

* **`BOLT-LMM-inf` reproduces standard prospective LOCO mixed-model statistics (`GCTA-LOCO`) with $R^2 > 0.999$ while avoiding proximal contamination (Online Methods Eqs. 7–10, Supplementary Table 7): [Well Supported].**  
  Because the prospective denominator $x_{\text{test}}' V_{\text{LOCO}}^{-1} x_{\text{test}}$ is nearly constant across common SNPs in human cohorts without extreme family structure, scaling the retrospective numerator $(x_{\text{test}}' V_{\text{LOCO}}^{-1} y)^2$ by a constant $c_{\text{inf}}$ matches `GCTA-LOCO` almost identically while avoiding the power loss from proximal contamination seen in `EMMAX` and `GEMMA`.

* **On nine quantitative traits in WGHS ($N = 23,294$), `BOLT-LMM` significantly improves cross-validated prediction $R^2$ (9/9 traits, $p < 0.0002$) and known-locus $\chi^2$ statistics (6/9 traits, up to 10% gain for ApoB) while eliminating false-positive *LCT* stratification on height (Section "Application of BOLT-LMM to WGHS phenotypes", Fig. 3): [Well Supported].**  
  Empirical gains track the inferred sparsity of each trait's genetic architecture and match the theoretical asymptotic effective sample-size relationship $1 / (1 - R_{\text{pred}}^2)$. Uncorrected marginal regression yields a spurious genome-wide significant signal at the lactase (*LCT*) locus for height due to European substructure, which is completely abolished by `PCA`, `BOLT-LMM-inf`, and `BOLT-LMM`.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT (Major Issues, Minor Issues, Concrete Recommendations)

#### Major Issues
None; the mathematical derivations, simulation controls, and empirical validations are sound.

#### Minor Issues
1. **Monte Carlo Variance in $c_{\text{inf}}$ Calibration from 30 Random SNPs (Online Methods, Step 1b):** Estimating the constant calibration factor $c_{\text{inf}}$ in Equation (9) using only 30 pseudorandom SNPs with $\chi^2_{\text{GRAMMAR}} < 5$ introduces a $\sim 1\%$ standard error in the scale of all genome-wide $\chi^2_{\text{BOLT-LMM-inf}}$ test statistics (and by extension the target LD Score regression intercept for Step 2b). Because a 1% shift in $\chi^2$ at the genome-wide significance threshold ($\chi^2 = 29.7$, $p = 5 \times 10^{-8}$) alters $p$-values by $\approx 15\%$, reducing this Monte Carlo noise is desirable.
2. **Typographical Formatting in Eq. (13) and Parameter Grid (Online Methods):** In Equation (13) (line 100), the normal prior is typeset as $\beta_m \sim N(0, \sigma_g^2) / M_{\text{LOCO}}$ instead of $\beta_m \sim N(0, \sigma_g^2 / M_{\text{LOCO}})$, and on line 133 the grid for $p$ has a period instead of a comma (`p \in {0.5, 0.2. 0.1, 0.05, 0.02, 0.01}`).

#### Concrete Recommendations

#### 1. Increase or Adaptively Stop the Random SNP Sample Size for $c_{\text{inf}}$ Calibration
* **WHY:** A $\sim 1\%$ calibration standard error from averaging 30 SNPs in Equation (9) translates to a $\sim 0.3$ shift in $\chi^2$ at $\chi^2 = 30$, which can flip borderline genome-wide significant loci across runs with different random seeds.
* **WHAT:** Increase the default number of calibration SNPs (or implement an adaptive stopping rule based on the Jackknife standard error of the ratio in Eq. 9) so that the standard error of $c_{\text{inf}}$ is $\le 0.2\%$.
* **HOW:** Solve $V_{\text{LOCO}}^{-1} x_{\text{test}}$ via conjugate gradients for 100–150 random SNPs (or block-CG across multiple RHS vectors simultaneously, which amortizes memory bandwidth over the genotype matrix $X$) so that calibration variance becomes negligible with minimal runtime overhead.

#### 2. Quantify the Breakdown of Constant-Denominator Approximation for Rare Variants
* **WHY:** In the Discussion, the authors note that treating the prospective denominator $x_{\text{test}}' V_{\text{LOCO}}^{-1} x_{\text{test}}$ as constant (after normalizing $x_{\text{test}}$) may be violated for very rare variants or cohorts with strong family relatedness.
* **WHAT:** Provide a quantitative MAF or variance-ratio diagnostic guideline indicating when the constant-denominator retrospective approximation diverges from the exact prospective statistic.
* **HOW:** Using the 30–100 calibration SNPs stratified across MAF bins in the WTCCC2/WGHS datasets, report the coefficient of variation of $x_{\text{test}}' V_{\text{LOCO}}^{-1} x_{\text{test}}$ (for unit-variance normalized $x_{\text{test}}$) as a function of MAF.

#### 3. Technical and Editorial Cleanup
* **WHY:** Minor equation typesetting errors should be corrected for clarity.
* **WHAT & HOW:**
  1. In Online Methods Equation (13) (line 100), move `/ M_{\text{LOCO}}$` inside the variance argument of the normal distribution: $\beta_m \sim \mathcal{N}(0, \sigma_g^2 / M_{\text{LOCO}})$.
  2. In Online Methods Step 2a (line 133), change `p \in {0.5,0.2.0.1,0.05,0.02,0.01}` to `p \in {0.5, 0.2, 0.1, 0.05, 0.02, 0.01}`.
  3. In Online Methods Step 2a (line 129), fix the typo `analyis` to `analysis`.
