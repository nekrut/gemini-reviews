# Review of ANON_03

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **7.4 / 10.0** (Strong / Sound)  
* **Score Breakdown:** Rigor: 2.6/3.5 | Claims: 1.9/2.5 | Biology: 1.5/2.0 | Reproducibility: 1.4/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript tests for polygenic adaptation acting on standing genetic variation in humans by comparing allele frequencies of height-associated variants between Northern and Southern European populations using GIANT consortium GWAS summary statistics ($N > 130,000$), two independent European population datasets (MIGen and POPRES), and a within-sibship association analysis in the Framingham Heart Study ($4,819$ individuals across $1,761$ sibships). The authors show that both the 139 directly genotyped genome-wide significant GIANT height SNPs and an expanded set of $\sim 1,400$ LD-pruned SNPs have systematically higher frequencies of the height-increasing allele in Northern than in Southern Europeans (mean $\Delta\text{AF} = 0.012, p = 4.3\times 10^{-4}$ for 139 SNPs; $p < 1.5\times 10^{-7}$ across pairwise European comparisons for $\sim 1,400$ SNPs). Using a likelihood ratio test comparing neutral Nicholson-Ayodo genetic drift against drift plus directional selection proportional to effect size ($w = s\beta$), they reject genetic drift ($p < 10^{-15}$) and infer per-allele selection coefficients of $10^{-3}$ to $10^{-5}$. Standard consortium cohorts are used and analytical equations are stated, though custom R scripts are not deposited.

This is a well-designed population genetics study that anticipates and tests several major potential confounders, including HapMap SNP ascertainment bias, Northern European power asymmetry in GIANT, Orr's phenotype ascertainment bias, and residual population stratification via a family-based Framingham sibship control. Nevertheless, a critical statistical vulnerability remains in how the $\sim 1,400$-SNP set is selected and validated against residual stratification: failing to reject the null of equal means in a paired $t$-test between noisy Framingham within-sibship estimates and GIANT estimates ($p = 0.36$, $N = 1,761$ sibships) does not prove the absence of subtle stratification across those $\sim 1,400$ SNPs (Pillar 4). Because the directional polarization of each SNP ("height-increasing allele") in the main Table 1 LRT still relies on the GIANT meta-analysis rather than the family-based estimates, even a tiny residual North-South stratification in GIANT ($\sim 1\text{--}2\%$ of the effect size) accumulates across $1,400$ SNPs to inflate the $t$-test and LRT statistics. Re-computing the selection test using exclusively family-based effect signs/weights and reporting the statistical power of the Framingham equivalence test would substantially strengthen the core inference.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **At the 139 genome-wide significant GIANT height loci, height-increasing alleles are elevated in Northern vs. Southern Europeans: [Well Supported].**  
  In MIGen, 85/139 height-increasing alleles have higher frequency in Northern than Southern Europeans (sign test $p = 0.011$; paired $t$-test mean $\Delta\text{AF} = 0.012, p = 4.3\times 10^{-4}$; permutation test against 10,000 frequency-matched SNP sets $p = 0.0056$; Figure 1a), with replication in POPRES (Supplementary Table 2). At genome-wide significant loci ($p < 5\times 10^{-8}$), true additive genetic effects dominate small residual stratification.

* **The directional shift across the expanded set of $\sim 1,400$ sub-significant SNPs is "not confounded by ancestry" (Abstract) because a paired $t$-test between GIANT and Framingham within-sibship effects yields $p = 0.36$: [Fragile].**  
  This conclusion rests on conflating failure to reject a null hypothesis in a small family sample with proof of no stratification (Pillar 4):
  1. *Low power of the within-sibship comparison:* The Framingham sample contains $4,819$ individuals in $1,761$ sibships (effective independent sample size for within-sibship Mendelian segregation is roughly equivalent to $\sim 1,500\text{--}2,000$ unrelated individuals, or $\sim 1.5\%$ of GIANT's sample size). Standard errors on within-sibship regression coefficients per SNP are nearly an order of magnitude larger than GIANT's. A non-significant paired $t$-test ($p = 0.36$) between GIANT and FHS across $\sim 1,400$ SNPs has wide confidence intervals and cannot rule out a 15–25% stratification-driven attenuation.
  2. *Selection on GIANT $p$-values and polarization:* Even after restricting to the top $\sim 1,400$ SNPs, Table 1 defines the "height-increasing allele" and the weight $\beta$ using GIANT summary statistics, not the FHS within-sibship estimates. Notice in Figure 1a that even the 10,000 *randomly matched* genome-wide SNP sets have a positive mean frequency difference of $+0.0035$ (30% as large as the $+0.012$ signal at the 139 known loci, and nearly Half of the $+0.0079$ difference reported in Table 1 for the $\sim 1,400$ SNPs in MIGen!). This genome-wide background offset demonstrates that ordering or polarizing SNPs by GIANT summary statistics carries an intrinsic North-South covariance across the entire genome.

* **Allele frequency differences at the $\sim 1,400$ SNPs reject neutral genetic drift ($p < 10^{-15}$) in favor of weak selection ($s \sim 10^{-3}\text{--}10^{-5}$): [Moderately Supported].**  
  The Nicholson-Ayodo normal approximation to drift variance, $\text{Var}(\Delta\text{AF}) = p(1-p)(2F_{ST} + \frac{1}{N_1} + \frac{1}{N_2})$, and the additive selection shift $\Delta\text{AF}_{\text{Sel}} \approx T w p(1-p)$ (since $\frac{wp^2 + wp + p}{1 + 2wp} - p = \frac{wp(1-p)}{1 + 2wp} \approx wp(1-p)$ for $w \ll 1$) are mathematically sound when SNP polarizations ($\text{sign}(\beta)$) are assigned independently of the North-South drift vector. However, if GIANT $\hat{\beta}$ estimates contain residual correlation with the North-South allele frequency difference $\Delta\text{AF}_{N-S}$, the null variance $p(1-p)(2F_{ST} + 1/N_1 + 1/N_2)$ Centered at mean $0$ is misspecified because the mean under neutrality with residual GWAS stratification is strictly positive (as seen in the purple curve of Figure 1a at $+0.0035$). Subtracting the empirical genome-wide baseline shift ($+0.0035$) from Table 1's MIGen shift ($0.0079$) cuts the estimated selection gradient in half and substantially alters the LRT $p$-value.

* **HapMap SNP ascertainment, GIANT sample composition, and Orr's trait ascertainment bias do not explain the North-South frequency shift: [Well Supported].**  
  The authors perform thorough controls: verifying that height-increasing alleles are equally distributed between major and minor alleles ($70/138$ and $752/1,434$, $p > 0.05$), re-ranking GIANT SNPs by Southern European discovery power, and simulating $10,000$ neutral polygenic traits to bound trait ascertainment bias (main text lines 69–71).

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Recalculate the Table 1 Selection LRT Polarizing and Weighting SNPs Exclusively by Within-Sibship Estimates
* **WHY:** In Table 1, FHS is used only as a threshold filter to pick the top $\sim 1,400$ SNPs (based on $p = 0.36$), after which the GIANT effect sizes $\hat{\beta}_{\text{GIANT}}$ are plugged back into the $t$-test and LRT ($w = s\beta$). Because $\hat{\beta}_{\text{GIANT}}$ is derived from a population-based meta-analysis with known residual North-South structure (evidenced by the $+0.0035$ baseline shift in matched random SNPs in Figure 1a), using $\hat{\beta}_{\text{GIANT}}$ in the LRT leaks stratification into the selection test.
* **WHAT:** Perform a stratification-free selection test in which the trait-increasing allele polarization and effect size $\beta$ come from the family-based FHS within-sibship regression (or in which the LRT for the 139 strictly genome-wide significant SNPs is reported in Table 1 alongside the $\sim 1,400$ SNPs).
* **HOW:** 
  1. Add a section to Table 1 reporting the exact same pairwise population $t$-tests and LRTs ($w = s\beta$) restricted to the 139 (MIGen) and 109 (POPRES) genome-wide significant GIANT SNPs.
  2. For the $\sim 1,400$ SNPs, compute the polygenic score difference $\sum_i \hat{\beta}_{i,\text{FHS}} (p_{i,N} - p_{i,S})$ where $\hat{\beta}_{i,\text{FHS}}$ is the within-sibship regression coefficient from Framingham, and compare it against its null drift variance $\sum_i \hat{\beta}_{i,\text{FHS}}^2 p_i(1-p_i)(2F_{ST} + 1/N_1 + 1/N_2)$.

#### 2. Report Confidence Intervals and Equivalence Power for the Framingham vs. GIANT Effect-Size Comparison
* **WHY:** Reporting a non-significant paired $t$-test ($p = 0.36$) between FHS within-sibship and GIANT effect sizes across $\sim 1,400$ SNPs does not establish that the two sets of effect sizes are equal; it only shows that the difference is smaller than the sampling noise of $1,761$ sibships.
* **WHAT:** Quantify the 95% confidence interval of the ratio (or difference) between mean within-sibship and GIANT effect sizes for the $\sim 1,400$ SNPs, and propagate that uncertainty into the LRT.
* **HOW:** Compute the mean and 95% CI of $\bar{\beta}_{\text{FHS}} - \bar{\beta}_{\text{GIANT}}$ (and the regression slope of $\hat{\beta}_{\text{FHS}}$ on $\hat{\beta}_{\text{GIANT}}$ via Deming/errors-in-variables regression). Then evaluate the Table 1 LRT under a conservative null where the expected neutral drift mean is shifted by the lower bound of residual stratification (or by the $+0.0035$ empirical background shift observed in the 10,000 matched SNP sets in Figure 1a).

#### 3. Account for Chromosome- vs. Individual-Level Sample Sizes in the Drift Variance Formula
* **WHY:** There is an ambiguity between the main text (line 57) and Online Methods (line 110) in the drift variance formula $p(1-p)(2F_{ST} + 1/N_1 + 1/N_2)$. Line 57 defines $N_i$ as "population sample sizes" (which in Table 1 are listed as diploid individuals: e.g., $257, 254$ for MIGen), whereas Online Methods line 110 correctly defines $N_1$ and $N_2$ as "total chromosome counts" ($2n_1, 2n_2$). Using diploid individual counts vs. haploid chromosome counts changes the binomial sampling variance term $p(1-p)(\frac{1}{2n_1} + \frac{1}{2n_2})$ by a factor of 2.
* **WHAT & HOW:** Verify in the R code whether $N_1, N_2$ in the likelihood calculation used $n_{\text{ind}}$ or $2n_{\text{ind}}$ (haploid chromosomes), harmonize the notation across line 57, Table 1, and line 110, and confirm that $F_{ST}$ was estimated using the unbiased Weir-Cockerham or Hudson estimator (which already subtracts finite-sample binomial variance) so that $1/(2n_1) + 1/(2n_2)$ is not double-counted.

#### 4. Temper the Abstract Claim that the Signal is "Not Confounded by Ancestry"
* **WHY:** While the 139 known loci and the FHS running-average permutation test (Figure 2b) provide real evidence of a genetic height gradient, Figure 2a explicitly shows that genome-wide FHS effect estimates decay toward zero faster than GIANT estimates—which the authors themselves note "could be due to low power in the smaller family-based sample and/or residual stratification in the remaining GIANT data" (line 49).
* **WHAT:** Qualify the Abstract's categorical statement ("is not confounded by ancestry") to distinguish between the validated signal and the residual stratification present in sub-significant genome-wide tails.
* **HOW:** Revise the Abstract sentence to: *"Within-family analyses in an independent sibship cohort confirm that a substantial fraction of this directional difference reflects true genetic effects rather than ancestry confounding alone."*

#### 5. Technical, Mathematical, and Editorial Cleanup
* **WHY:** Minor mathematical formatting issues, truncated text, and typos should be cleaned up for clarity.
* **WHAT & HOW:**
  * **Truncated Table 1 footnote (line 37):** The footnote ends mid-sentence at *"likely to span the actual (unknown) value of"*—complete the sentence with *"T."*
  * **Equation formatting (lines 61 and 116):** The selection equation $\Delta\text{AF}_{\text{Sel}} \approx T \times \left(\frac{wp^2 + wp + p}{1 + 2wp} - p\right)$ is rendered inline without fraction bars as `T × ( w p 2 + w p + p 1 + 2 w p - p )`; format with proper fraction delimiters and note the algebraic simplification $\frac{wp(1-p)}{1+2wp}$.
  * **Missing internal cross-reference (line 112):** Online Methods states *"(see section 4.1 for derivation)"*, which refers to a numbered section in the Supplementary Note—update to *"(see Supplementary Note Section 4.1 for derivation)"*.
  * **Grammatical and spelling fixes:** Line 47: *"we must also considered"* $\rightarrow$ *"we must also consider"*; Line 69: *"Kolmagoroff-Smirnov"* $\rightarrow$ *"Kolmogorov-Smirnov"*.
