# Review of PMC6428572 (PMID:30895923)

**Manuscript Title:** Reduced signal for polygenic adaptation of height in UK Biobank  
**Authors:** Berg JJ, Harpak A, Sinnott-Armstrong N, Joergensen AM, Mostafavi H, Field Y, Boyle EA, Zhang X, Racimo F, Pritchard JK, Coop G.  
**Journal / Preprint:** *Elife* (2019; `PMC6428572` / `PMID:30895923` / `10.7554/elife.39725`)  
**Calibration Study Cohort:** Cohort B — Validated Control (`B18` | Double-Blinded as `ANON_34`)  
**Overall Score:** **9.2 / 10.0** (Exemplary)  
* **Score Breakdown:** Rigor: 3.3/3.5 | Claims: 2.3/2.5 | Biology: 1.9/2.0 | Reproducibility: 1.7/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript re-evaluates population-genetic evidence for polygenic adaptation of human height across Eurasia ($Q_X$ neutrality tests, latitudinal and longitudinal clines) and within Britain (Singleton Density Score, tSDS, and bivariate LD Score regression) across seven GWAS summary statistic datasets: GIANT ($n = 253\text{k}$), the original 2015 sibling meta-analysis release (`R15-sibs`, $n = 35\text{k}$), its bug-fixed replacement (`R15-sibs-updated`), and four UK Biobank analyses (`UKB-GB` [$n = 337\text{k}$], `UKB-Eur` [$n = 459\text{k}$], `UKB-GB-NoPCs` [$n = 337\text{k}$], and a newly computed `UKB-sibs` family analysis [$n = 35,524$ individuals in 19,268 sibling pairs]). The authors demonstrate that previously reported strong signals of selection in GIANT and `R15-sibs` fail to replicate in the UK Biobank datasets and in `R15-sibs-updated`. Beyond showing that GIANT and `R15-sibs` effect-size discrepancies covary with European North–South (`GBR-TSI`) and Eurasian (`TSI-CHB`) allele frequency differences, the manuscript makes two important theoretical and empirical advances: (1) it demonstrates that bivariate LD Score regression slopes are not robust to population stratification because background selection (BGS) increases genetic drift and squared allele frequency differentiation in high-LD regions; and (2) it introduces a spatial pair-covariance decomposition ($pQ_X(k)$, Appendix 1) showing that residual $Q_X$ inflation in dense SNP ascertainments stems from physical linkage violating the neutral model's independence assumption. All newly generated GWAS summary statistics and analysis scripts are archived on Dryad and GitHub.

This is a thorough, transparent, and methodologically incisive work that overturns earlier conclusions by several of the authors' own previous studies and provides a mechanistic explanation for why multiple ostensibly orthogonal validation strategies (sibling meta-analysis, coalescent SDS, and bivariate LD Score regression) previously converged on a false positive. Minor technical items—such as a missing exponent in the block-jackknife variance equation, unconstrained LD Score regression genetic correlation estimates exceeding 1.0 in Table 2, and hard-calling dosages without a threshold in the QFAM sibling pipeline—are straightforward to clarify.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Previously reported signals of polygenic adaptation on height across Europe/Eurasia ($Q_X$, latitudinal, and longitudinal clines) and in Britain (genome-wide tSDS) do not replicate in UK Biobank or corrected sibling GWAS datasets: [Well Supported].**  
  Across 1,700 approximately independent LD blocks, both latitudinal ($p_{\text{lat}}$) and general overdispersion ($Q_X$) tests drop from highly significant in GIANT and `R15-sibs` to null or marginal across `UKB-GB`, `UKB-Eur`, `UKB-GB-NoPCs`, `UKB-sibs`, and `R15-sibs-updated` (Figure 1, Figure 1—figure supplement 1, Figure 2, Figure 2—figure supplement 1).

* **Effect estimates in GIANT and the original `R15-sibs` release are confounded by population stratification along major European (`GBR-TSI`) and Eurasian (`TSI-CHB`) axes: [Well Supported].**  
  Differences in estimated effect sizes $(\hat{\beta}_{\text{GIANT}} - \hat{\beta}_{\text{UKB-GB}})$ and $(\hat{\beta}_{\text{R15-sibs}} - \hat{\beta}_{\text{UKB-GB}})$ correlate significantly with `GBR-TSI` allele frequency differences ($r^2 = 0.06$ and $r^2 = 0.07$, $p < 2.2 \times 10^{-16}$; Figure 3B,D) and yield massive bivariate LD Score regression intercepts with `GBR-TSI` ($p = 4 \times 10^{-80}$ and $p = 9 \times 10^{-161}$; Figure 4D,E), whereas `UKB-GB` and `R15-sibs-updated` show near-zero intercepts.

* **Bivariate LD Score regression slopes can be confounded by the interaction of population stratification and background selection (BGS): [Well Supported].**  
  The authors test and refute the standard LD Score regression assumption that allele frequency differentiation is independent of LD Score: squared frequency differences $[\text{GBR}-\text{TSI}]^2$ ($p = 2.5 \times 10^{-5}$), White British vs. Irish in UKB ($p = 2.5 \times 10^{-7}$), and $\text{SDS}^2$ ($p = 2.9 \times 10^{-42}$) all increase significantly with LD Score (Figure 5). The analytical derivation in Appendix 3 parameterized by McVicker's $B$ (Appendix 3—figures 1–3) convincingly explains how higher drift in low-recombination/high-LD regions generates spurious bivariate slopes when a GWAS is stratified along an axis correlated with the second trait/statistic.

* **Residual $Q_X$ overdispersion in densely ascertained UKB SNP sets (e.g., 5k–20k SNPs) is partially an artifact of physical linkage and diffuse non-specific variance rather than adaptive divergence: [Well Supported].**  
  The distance-binned pair-covariance statistic $pQ_X(k)$ (Appendix 1—figures 1–5) and the uniform inflation of the eigenvalue-projected $Q_U$ statistics on the QQ plot (Appendix 1—figure 6) demonstrate that including multiple SNPs per LD neighborhood violates the diagonal locus-independence assumption of the neutral covariance matrix $\mathbf{F}$.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Clarify Dosage Hard-Calling and Between-Family Variance Weighting in the `UKB-sibs` QFAM Pipeline
* **WHY:** In Materials and methods ("Newly calculated GWAS"), `UKB-sibs` was generated by *"converting dosages from imputation to genotype calls using no hard calling threshold"* and running PLINK 1.9 `--qfam mperm=100000`. Standard PLINK `QFAM` (total association) regresses phenotype on genotype while permuting within and between families to calibrate $P$-values, whereas `QFAM-within` specifically regresses on the within-family deviation from the family mean to eliminate between-family stratification in the effect-size point estimate $\hat{\beta}$. Furthermore, converting imputed dosages without a hard-call certainty threshold introduces genotype call noise at poorly imputed variants.
* **WHAT:** Specify whether `--qfam` or `--qfam-within` was used to extract the beta coefficients for `UKB-sibs`, and confirm that applying a standard hard-call threshold (e.g., dosage distance $< 0.1$) does not alter the `UKB-sibs` genetic correlations or polygenic score results.
* **HOW:** Document the exact PLINK QFAM output column used for $\hat{\beta}$ in Materials and methods and Appendix 4, and verify concordance on the 1,700 ascertained SNPs (which have MAF $> 0.05$ in GBR and high imputation quality).

#### 2. Discuss Boundary Behavior for LD Score Genetic Correlations Exceeding 1.0 in Table 2
* **WHY:** In Table 2, several pairwise bivariate LD Score regression genetic correlation estimates exceed the theoretical maximum of 1.0 (e.g., `UKB-Eur` vs. `GIANT` = 1.03, `UKB-GB` vs. `GIANT` = 1.03, `UKB-sibs` vs. `UKB-Eur` = 1.06, `UKB-sibs` vs. `UKB-GB` = 1.06). While unconstrained ratio estimators of $\hat{r}_g = \widehat{\text{cov}}_g / \sqrt{\hat{h}_1^2 \hat{h}_2^2}$ can exceed 1.0 due to sampling variance or slightly underestimated denominator heritabilities when LD Score assumptions are violated, a brief explanation would aid readers.
* **WHAT & HOW:** Add a sentence to the Table 2 caption or text noting that unconstrained LDSC ratio estimates can slightly exceed 1.0 within sampling error (or when BGS slightly biases the univariate $h^2$ denominator slope relative to the bivariate numerator).

#### 3. Mathematical and Editorial Fixes
* **WHY:** Minor typos in mathematical formulas and table headers should be cleaned up.
* **WHAT & HOW:**
  1. **Materials and methods ("tSDS vs. GWAS significance"):** In the block-jackknife variance formula, add the missing square exponent `^2` to the summand: change `σ^2 = (b−1)/b ∑_{i=1}^b (ρ^(−i)b − ρb¯)` to `σ^2 = (b−1)/b ∑_{i=1}^b (ρ^(−i)b − ρb¯)^2`.
  2. **Table 2 headers:** Standardize the capitalization of column headers `Giant` $\to$ `GIANT` and `Ukb-gb` $\to$ `UKB-GB`.
  3. **Introduction (Paragraph 5):** Remove the duplicated word `the` in `"While our focus here is on the the distribution of height polygenic scores"` and in the Abstract (`"based on the the UK Biobank"`).
