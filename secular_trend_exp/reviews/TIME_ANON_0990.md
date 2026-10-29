</Agent System Instructions>
<Blinded Review: TIME_ANON_0990>
**Composite Score:** 4.8 / 10.0 (Rigor: 1.4/3.5 | Claims: 1.2/2.5 | Biology: 1.0/2.0 | Reproducibility: 1.2/2.0)
**Bias Category:** Statistical/Design
**Verdict:** Major Revision
**Study Modality:** Dry-Lab Theory/Methods/Simulation
**Technology Maturity:** Mature/Classical
**Epistemic Stage:** Basic/Mechanistic Discovery

OVERALL_SCORE: 4.8/10
VERDICT: CAVEATS
ESTIMATED_DECADE: 2000s

---

### 1. Executive Summary / SUMMARY
This manuscript introduces `HAPGLM`, a generalized linear model (GLM) score-test framework extending Schaid et al. and Tzeng et al. to test multi-region haplotype configurations (MRHCs) across unlinked genomic regions while adjusting for environmental covariates and correcting for multiple marker combinations via Becker and Knapp's unnested $\min P$ permutation procedure. The authors evaluate Type I error and power across simulated continuous and binary traits (comparing `HAPGLM` against `FAMHAP`'s `hapcc` and `htr`) and apply the method to 8 candidate-gene markers across 4 unlinked genes (*ADD1*, *H-FABP*, *MC4R*, *CAST*) in 93 pigs from 5 breeds/crosses evaluated for 8 meat quality traits. While extending multi-region haplotype tests to GLMs with covariates is a reasonable incremental goal, the manuscript suffers from fundamental statistical and design flaws: (1) the omnibus test of $H_0: \alpha = 0$ across all MRHCs tests joint main + interaction effects rather than epistasis (and the simulation study generates purely additive multi-locus effects $g = \sum_i g_i$ without any gene-gene interaction); (2) permuting $(Y, X_e)$ together against genotypes $G$ is invalid when covariates $X_e$ (such as pig breed) are correlated with marker genotypes ($G \not\perp X_e$, population stratification); (3) the binomial confidence intervals in Tables 2, 4, and 6 correspond to $N = 1,000$ simulations rather than the claimed 1,500 simulations (confusing simulated datasets with 1,500 permutation replicates) and contain copy-paste errors; and (4) the real-data pig analysis reports dozens of unadjusted raw $p < 0.01$ combinations across 2,040 tests ($255 \text{ combinations} \times 8 \text{ traits}$) and lists duplicate haplotypes in Table 11.

### 2. Methodological & Statistical Audit / STRENGTHS, WEAKNESSES & METHODOLOGICAL AUDIT

#### Strengths
- **GLM Score Test Extension**: Formulating the multi-region haplotype test as a GLM score statistic $S_\alpha^T V_\alpha^{-1} S_\alpha$ allows continuous and binary traits to be analyzed in a unified framework without refitting maximum-likelihood parameters for every marker configuration under the alternative hypothesis.
- **Direct Comparison to `FAMHAP`**: Benchmarking Type I error and power against `hapcc` and `htr` on coalescent haplotypes generated via `ms` provides a direct baseline in the covariate-free binary setting.

#### Weaknesses & Methodological Audit
1. **Conflation of Omnibus Main Effects with "Haplotype Interaction" (`[Methodologically Flawed]`)**:
   - Throughout the title, abstract, and text, the authors claim to assess "the interactions of haplotypes that belong to different unlinked regions." However, the vector $\alpha$ represents the effects of the $h$ multi-region haplotype configurations (MRHCs) relative to a baseline, and the tested null hypothesis is $H_0: \alpha = 0$ (no genetic effect of any region or combination).
   - Even more revealingly, in the simulation study (Section "Continuous traits", line 35), the genetic effect $g$ is simulated as "the sum of all considered genes' effects" ($g = \sum_i g_i$)—a purely **additive** model with zero epistatic interaction between the two unlinked regions! Thus, the high power reported in Tables 3, 5, 7, and 8 is power to detect additive main effects, not gene-gene interaction.
2. **Invalid Permutation Scheme Under Covariate–Genotype Confounding (Population Stratification)**:
   - In Methods (line 302), the permutation test is defined by randomly permuting the pair $(Y_i, X_{e,i})$ together across individuals while holding multi-region genotypes $G_i$ fixed. Permuting $(Y, X_e)$ against $G$ tests the conditional independence $Y \perp G \mid X_e$ **only** when $G$ and $X_e$ are independent ($G \perp X_e$).
   - In the pig meat quality dataset ($n = 93$ pigs from 5 distinct breeds/crosses: Meishan, Sutai, Yorkshire $\times$ Sutai, Landrace $\times$ Sutai, and Duroc $\times$ Landrace $\times$ Yorkshire), breed is included as an environmental covariate $X_e$, and the authors explicitly report (line 208) that 5 of the 8 markers have significant allele frequency differences across breeds ($\chi^2$ test). Because $G \not\perp \text{Breed}$, permuting $(Y, \text{Breed})$ together breaks the association between Breed and $G$ in the permuted samples, failing to control for population stratification under the null.
3. **Simulation Count Discrepancy ($N = 1,000$ vs. Claimed $1,500$) and Table Typos**:
   - Line 56 states that global $p$-values are computed with 1,500 permutation replicates per simulated dataset, and the titles of Tables 2–5 claim "via 1500 simulations at $\alpha = 0.05$." However, every single Type I error entry in Tables 2, 4, and 6 is an exact multiple of $0.001 = 1/1000$, and the reported 95% confidence intervals match exact Clopper–Pearson intervals for $N = 1,000$ trials, not $1,500$ (e.g., $48/1000 = 0.048$ gives $[0.0356, 0.0631] \to (0.036\text{–}0.063)$; $44/1000 = 0.044$ gives $[0.0321, 0.0586] \to (0.032\text{–}0.059)$).
   - In Table 2 (line 76, Sample Size 50, $q = 0.5$, `HAPGLM`), the CI for `0.047` is misprinted as `(0.042-0.071)` (copied from $n=200, q=0.1$ where the point estimate is `0.055`), whereas the identical scenario in Table 4 (line 117, Model 5) correctly prints `0.047(0.035-0.062)`. In Table 6 (line 161, Low diversity, $q = 0.5$, Model 2), `0.051(0.038-0.057)` has a typo in the upper bound (`0.057` instead of `0.067`).
4. **Mislabeled Rows and Impossible Marker Combinations in Table 9, and Duplicate Haplotypes in Table 11**:
   - Table 9 (line 194) lists "Model 5" and "Model 6" (which per Table 1 are **null** models with no genetic effect) as having `2|5` and `5` as top combinations; the authors evidently mislabeled Models 3 and 4 as Models 5 and 6. Furthermore, row "Model 5" lists `245` and `234|5` (placing marker 4 from region 2 into region 1), and row "Model 7" lists `123|45` twice (ranks 4 and 9).
   - In the pig application, Table 10 reports raw unadjusted $p < 0.01$ combinations across $2^8 - 1 = 255$ marker subsets and 8 traits without reporting global $\min P$-corrected $p$-values, and Table 11 lists identical haplotype strings multiple times within the same row (e.g., `AG|G|G|AGAA` twice for BK; `AG|A|G|AGGA` three times for Tend; `AG|A|A|AGGA` twice for Protein).

### 3. Biological / Experimental Grounding & Claim Proportionality
- **Claim 1**: `HAPGLM` has valid Type I error and comparable power to `hapcc` and `htr` for binary traits without covariates. `[Moderately Supported]` — Supported by the simulation tables, though the test is an omnibus main + interaction test under an additive simulation model.
- **Claim 2**: `HAPGLM` validly tests haplotype interactions while adjusting for covariates such as breed in structured multi-breed livestock cohorts. `[Methodologically Flawed]` — Joint permutation of $(Y, X_e)$ against $G$ is invalid when $X_e$ (breed) is correlated with $G$, and $H_0: \alpha = 0$ does not isolate epistasis from main effects.
- **Claim 3**: Multi-region haplotype configurations across *ADD1*, *H-FABP*, *MC4R*, and *CAST* are significantly associated with pig meat quality traits. `[Overstated]` — Based on unadjusted raw $p < 0.01$ screening across $255 \times 8 = 2,040$ tests in $n = 93$ pigs across 5 breeds with strong allele-frequency stratification.

### 4. Reproducibility & Data Completeness
- **Missing Equations in Text**: Almost all mathematical display and inline equations in the Simulation, Methods, and Appendix sections (lines 35, 263, 267, 272, 274, 281, 285, 289, 293, 299, 308, 310, 322–332) are missing from the text (likely lost when image-rendered equations were converted).
- **Software & Data Availability**: The FTP/web URL for downloading `HAPGLM` in the Conclusion (line 250) is blank (`at: , user: ylhu0323, password: public`), and the raw genotype/phenotype table for the 93 pigs is not provided.
</Blinded Review: TIME_ANON_0990>
