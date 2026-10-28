# Review of PMC4495769 (PMID:25642630)

**Manuscript Title:** LD Score regression distinguishes confounding from polygenicity in genome-wide association studies  
**Authors:** Bulik-Sullivan BK, Loh PR, Finucane HK, Ripke S, Yang J, Schizophrenia Working Group of the Psychiatric Genomics Consortium, Patterson N, Daly MJ, Price AL, Neale BM.  
**Journal / Preprint:** *Nat Genet* (2015; `PMC4495769` / `PMID:25642630` / `10.1038/ng.3211`)  
**Calibration Study Cohort:** Cohort B — Validated Control (`B39` | Double-Blinded as `ANON_79`)  
**Overall Score:** **9.4 / 10.0** (Exemplary)  
* **Score Breakdown:** Rigor: 3.3/3.5 | Claims: 2.4/2.5 | Biology: 1.9/2.0 | Reproducibility: 1.8/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript introduces Linkage Disequilibrium (LD) Score regression (LDSC), a statistical framework that distinguishes genome-wide association study (GWAS) test statistic inflation caused by true polygenic signal from inflation caused by confounding biases such as population stratification and cryptic relatedness. Under a random-effects polygenic model in which normalized genotype effect sizes are drawn independently with constant variance $h^2/M$, the authors derive the linear expectation $\mathbb{E}[\chi_j^2 \mid \ell_j] = N h^2 \ell_j / M + N a + 1$, where $\ell_j = \sum_k r_{jk}^2$ is the LD Score of variant $j$, $N$ is sample size, $M$ is the number of variants, and $N a$ captures confounding bias. Because variants with higher LD Scores tag more causal variation on average whereas pure genetic drift stratification and cryptic relatedness do not correlate with $\ell_j$, regressing GWAS $\chi^2$ statistics on reference LD Scores (estimated from 378 phased European individuals in 1000 Genomes) yields an intercept ($1 + N a$) that isolates confounding from polygenicity ($N h^2 / M$). The authors account for correlated test statistics and heteroskedasticity via weighted least squares, estimate standard errors via a 2,000-SNP block jackknife, validate the estimator across simulations of polygenicity, continental and national population stratification, cryptic relatedness, case–control ascertainment, and MAF-dependent architectures, and apply it to 24 complex trait GWAS datasets. Both the open-source Python command-line package (`ldsc`), simulation scripts, and precomputed European LD Scores are publicly released.

This is a rigorous methodological and empirical contribution that resolves a central problem in statistical genetics: standard genomic control ($\lambda_{\text{GC}}$) scales with $N h^2$ under polygenicity and is overly conservative in large GWAS. The mathematical derivation, weighted regression scheme, attenuation-bias correction, and simulation benchmarks are thorough and transparent about failure modes (such as extreme negative selection where all causal variants have $\text{MAF} < 1\%$, or reference-target LD mismatch across European subpopulations). Only minor mathematical notation typos in the main text and a fuller discussion of how background selection or prior study-level genomic control affect the intercept and slope need to be addressed.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Under an infinitesimal polygenic architecture without LD–$F_{\text{ST}}$ correlation, the LD Score regression intercept minus one ($N a$) is an unbiased estimator of mean test statistic inflation from population stratification and cryptic relatedness (Introduction Equation 1, Results lines 42–67, Figure 1): [Well Supported].**  
  The analytical derivation is verified across null and polygenic simulations in 1,000 Swedes, continental and national stratification simulations using seven European Psychiatric Genomics Consortium (PGC) control cohorts, combined Northern/Southern European stratification and half-chromosome polygenicity in 22,000 WTCCC2 individuals, familial relatedness in the Framingham Heart Study, and liability-threshold case–control ascertainment.

* **Polygenicity, rather than confounding bias, accounts for the majority of $\chi^2$ test statistic inflation across 24 large complex trait GWAS datasets, making $\lambda_{\text{GC}}$ correction overly conservative (Results lines 76–115, Table 1, Figure 2): [Well Supported].**  
  Across all 24 studies in Table 1, the LDSC slope is significantly positive and the intercept is substantially lower than $\lambda_{\text{GC}}$ (mean difference $0.11$; e.g., schizophrenia mean $\chi^2 = 1.613$, $\lambda_{\text{GC}} = 1.484$, LDSC intercept $= 1.070 \pm 0.010$). The authors appropriately note that for meta-analyses where individual contributing cohorts pre-applied genomic control (`GC = 1` or `2`), cohort-level $\lambda_{\text{GC}}$ division cannot be reversed by meta-level re-inflation and pushes the expected no-confounding intercept slightly below 1 (e.g., rheumatoid arthritis intercept $= 0.980$).

* **The 1000 Genomes pan-European (EUR) LD Score reference panel is sufficiently accurate for GWAS of predominantly Northern European ancestry, bounding intercept bias from intra-European LD differences to at most $\pm 10\%$ of total inflation (Results lines 35–38, Online Methods lines 143–148): [Well Supported].**  
  Subpopulation analyses across CEU ($\bar{\ell} = 109$), GBR ($104$), FIN ($117$), and TSI ($102$) against combined EUR ($110$) quantify both attenuation bias (from random measurement noise) and directional bias (from population bottlenecks such as in Finland), providing clear analytical bounds ($7 \times \text{slope} + 0.05(\overline{\chi^2} - 1)$).

* **LD Score regression remains well-calibrated under neutral MAF-dependent genetic architectures where per-allele effect sizes are independent of MAF, but breaks down if causal variants are restricted to rare alleles ($\text{MAF} < 1\%$) (Results lines 69–74, Supplementary Figures 6–7): [Well Supported].**  
  Because common variants ($\text{MAF} > 1\%$) have higher mean LD Scores than rare variants, neutral architectures ($2pq a^2 \propto p(1-p)$) induce a positive correlation between per-SNP variance explained and $\ell_j$. Simulations confirm that the resulting downward bias on the intercept is small for neutral traits (mean intercept $0.994$), while transparently showing that rare-only causal architectures ($\text{MAF} < 1\%$) yield negative slopes and upwardly biased intercepts.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Correct Mathematical Notation Typos in Variance Scaling and Unbiased $r^2$ Inequality
* **WHY:** Several mathematical expressions in the main text and Online Methods contain typographical errors in exponents or inequality signs that conflict with the underlying derivations in the Supplementary Note.
* **WHAT & HOW:** Make the following exact corrections:
  * **Line 15:** Change `"distributions with variance proportional to p(1-p)^-1/2"` to `"distributions with variance proportional to [2p(1-p)]^-1 (i.e., standard deviation proportional to [2p(1-p)]^-1/2)"`, since $\text{Var}(\beta_{\text{allele}}) \propto [2p(1-p)]^{-1}$ is required for per-normalized-genotype variance $2p(1-p)\text{Var}(\beta_{\text{allele}})$ to be constant.
  * **Line 19 (Equation 1):** Replace the forward slash `/` in `E [ χ 2 / ℓ j ]` with a vertical conditioning bar `|` and subscript $j$: $\mathbb{E}[\chi_j^2 \mid \ell_j] = N h^2 \ell_j / M + N a + 1$.
  * **Line 46:** Change `"drawn from N(0, h^2 / (2p(1-p))^-1/2 / M)"` to `"drawn from N(0, h^2 / [2 M p(1-p)])"`, fixing both the negative exponent in the denominator and the variance vs. standard deviation exponent.
  * **Line 119 (Figure 2 Caption):** Fix the truncated first word `"D Score regression plot"` to `"LD Score regression plot"`.
  * **Line 136 (Online Methods):** In the discussion of $\hat{r}^2_{\text{adj}} := \hat{r}^2 - \frac{1-\hat{r}^2}{N-2}$, change `"it is possible to have r_adj^2 < 1, which is a mathematically necessary feature of any unbiased estimator of r^2"` to `"it is possible to have r_adj^2 < 0, which is a mathematically necessary feature of any unbiased estimator of r^2 at r^2 = 0"`.

#### 2. Discuss the Impact of Background Selection and Local LD–Heritability Correlations on the Intercept
* **WHY:** In the real human genome, background selection and purifying selection reduce allele frequencies and local LD ($\ell_j$) in functionally conserved regions, while also inducing a slight positive correlation between $F_{\text{ST}}$ and $\ell_j$ (which produced a small positive LDSC slope in pure stratification simulations, line 53 and Supplementary Tables 3c, 4c). Conversely, if per-SNP heritability is depleted or enriched in high-LD regions independent of MAF, the single-component linear regression slope and intercept will absorb that curvature.
* **WHAT:** Expand the Discussion and "Frequency-Dependent Genetic Architectures" section to briefly explain how linked/background selection affects both $\text{Cov}(F_{\text{ST}}, \ell_j)$ and $\text{Cov}(h^2_j, \ell_j \mid \text{MAF})$.
* **HOW:** Add 2–3 sentences on page 4 (lines 71–74) noting that partitioning LD Scores by MAF bins or functional/evolutionary conservation categories can mitigate bias when per-SNP heritability varies with local LD density or background selection.
