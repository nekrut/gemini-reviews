# Review of FEXP_ANON_004

**Overall Score:** **8.3 / 10.0** (Strong / Sound) | **Scientific Core Score:** **6.3 / 8.0**  
* **Score Breakdown:** Rigor: 2.7/3.5 | Claims: 2.1/2.5 | Biology: 1.5/2.0 | Reproducibility: 2.0/2.0

---

## 1. Blinded Metadata Perception
* **Anonymized Manuscript ID:** `FEXP_ANON_004`
* **Perceived Domain & Design:** Experimental evolutionary ecology and virology; comparative experimental host-range susceptibility screen (84 wild strains across 44 *Caenorhabditis* species in 8 blocks) and 5-passage serial transmission assay (21 susceptible strains in 2 blocks) of Orsay virus (+ssRNA virus of *C. elegans*), analyzed with Bayesian phylogenetic generalized linear mixed models (`MCMCglmm`).
* **Blinding Integrity:** Double-blind review maintained; evaluated strictly on internal experimental, statistical, and phylogenetic modeling merits at $t_0$.

---

## 2. Executive Summary & Editorial Verdict

This study introduces the *Caenorhabditis*–Orsay virus host–pathogen system as a tractable laboratory model for studying cross-species viral spillover and emergence. The authors first screen 84 wild strains across 44 *Caenorhabditis* species (1–3 strains per species, typically 3 replicate plates of 5 founding adults exposed to $3\,\mu\text{L}$ of Orsay virus filtrate at $428.1\text{ TCID}_{50}/\mu\text{L}$ and grown to starvation) using RT-qPCR alongside 5 sets of negative/positive controls and residual-inoculum benchmarks. Using a plate-wash residual threshold ($\text{Ct} < 29.5$, derived from cell-free lawn Benchmark 4), they identify 21 susceptible strains across 14 species (13 novel host species plus *C. elegans*). They then subject all 21 susceptible strains to a 5-passage serial transmission experiment (transferring 20 random adults per passage to virus-free plates), finding dead-end infection (score 1) in 10 strains, stuttering transmission lost by passage 1–4 (score 2) in 5 strains, and sustained persistence through passage 5 (score 3) in 6 strains (all 3 *C. elegans* strains plus 1 strain each of *C. sulstoni*, *C. latens*, and *C.* sp. 65). Fitting Bayesian phylogenetic mixed models (`MCMCglmm`), they show that susceptibility declines significantly with phylogenetic distance from *C. elegans* ($\text{pMCMC} = 0.044$) and that onward transmission is strongly predicted by viral amplification ($\text{Ct}$) in the primary exposure population ($\text{pMCMC} = 0.009$).

**Editorial Verdict: Minor Revision (Strong / Sound).** This is a well-designed, carefully controlled experimental study with exemplary open data and code (`[GITHUB_REPO_REDACTED]`) and thoughtful physical benchmarks (Benchmark 4 lawn-wash and Benchmark 5 total-inoculum dilution) to separate true viral replication from residual inoculum. Two methodological issues in the statistical modeling and experimental protocol warrant attention: (1) modeling a bounded 4-level ordinal transmission score ($0, 1, 2, 3$) using a Gaussian linear mixed model (`family = "gaussian"`) instead of an ordinal probit/threshold model (`family = "ordinal"` or `"threshold"` in `MCMCglmm`), and over-interpreting poorly identified marginal $R^2$ point estimates whose 95% credible intervals span `[0%, 88.3%]` and `[0%, 89.0%]`; and (2) harvesting primary susceptibility plates "when freshly starved," which varied from 3 to 28 days across species, thereby confounding intrinsic per-capita host susceptibility with host reproductive rate, generation count, and viral RNA thermal decay over 4 weeks at $20^\circ\text{C}$.

### Assessment of Specific Claims
* **Claim 1 (Orsay virus can infect at least 14 of 44 *Caenorhabditis* species [21 of 84 strains], with susceptibility declining with phylogenetic distance from *C. elegans*): [Well Supported].**  
  The experimental screen includes rigorous negative, positive, and no-worm residual-virus controls across every block, confirms active replication via time-series assays in novel hosts, and demonstrates that 17 of the 21 susceptible strains even exceed the ultra-conservative unwashed-inoculum Benchmark 5 ($\text{Ct} < 22.0$). The phylogenetic distance effect on susceptibility is statistically supported ($\text{pMCMC} = 0.044$, $\Delta\text{DIC} = 2.37\text{–}4.37$ vs. models without distance from *C. elegans*).
* **Claim 2 (Susceptible *Caenorhabditis* strains vary qualitatively in transmission competence, spanning dead-end hosts [10 strains], stuttering chains [5 strains], and sustained 5-passage persistence [6 strains]): [Well Supported].**  
  The serial passage assay is internally consistent with the primary susceptibility screen ($r = 0.85$ between Passage 0 and susceptibility assay $\text{Ct}$ values) and replicated across 12 passages in follow-up experiments for *C. sulstoni* SB454 and *C. latens* VX80.
* **Claim 3 (Transmission ability is strongly driven by viral amplification [Ct] in the primary exposure population [$\text{pMCMC} = 0.009$]): [Well Supported].**  
  Every model containing primary-exposure $\text{Ct}$ outperforms models without it by $\Delta\text{DIC} > 3.1$ (combined DIC weight $0.862$), and the negative slope between $\text{Ct}$ (inverse viral load) and passage persistence is robust across specifications.
* **Claim 4 (Phylogenetic effects explain 50.9% [and distance from *C. elegans* explains 46.6%] of the variance in transmission ability, with DIC weights supporting phylogenetic effects on transmission): [Overstated].**  
  In Table 4, the top four transmission models—with and without `phylo. dist.` and `pairwise phylo. dist.`—are within $\Delta\text{DIC} = 0.908$ of each other (a difference that is statistically indistinguishable from MCMC Monte Carlo noise in DIC), and the fixed effect of phylogenetic distance from *C. elegans* is non-significant ($\text{pMCMC} = 0.132$). Moreover, the reported $R^2$ point estimates for transmission (`44.8%` for $\text{Ct}$ and `46.6%` for phylogenetic distance) have 95% credible intervals of `[0%, 88.3%]` and `[0%, 89.0%]`, indicating severe collinearity ($r = 0.477$) and non-identifiability of variance partitioning across only 21 strains (16 of which are placed on the phylogeny).

---

## 3. Forensic Defect Inventory

1. **Pillar 3 Violation — Gaussian Likelihood Applied to Bounded 4-Level Ordinal Transmission Scores (Methods line 121, Figure 4):**  
   The transmission score takes discrete ordinal values $Y \in \{0, 1, 2, 3\}$ (where $1 =$ lost at P1, $2 =$ lost at P2–P4, $3 =$ persisted to P5) with a heavy point mass at $Y = 1$ (10 of 21 strains had all replicates at $\le 1$). Fitting `family = "gaussian"` in `MCMCglmm` violates homoscedasticity and normality of residuals, allows linear predictions outside $[0, 3]$, and treats the interval between dead-end ($1$) and stuttering ($2$) as metric-equivalent to the interval between stuttering ($2$) and censored persistence at passage 5 ($3$). `MCMCglmm` natively supports ordinal probit models (`family = "ordinal"` or `"threshold"`) or discrete-time survival / passage-count modeling (number of passages survived, $0\text{–}5$).
2. **Pillar 4 Violation — Misuse of DIC and Non-Identifiable $R^2$ Partitioning in Small-Sample Phylogenetic GLMMs (Methods lines 97, 125; Results lines 138, 158; Tables 3–4):**  
   * **DIC instability in GLMMs:** As the authors briefly acknowledge in the Discussion (line 169), DIC in `MCMCglmm` (focused at the latent level) is poorly calibrated for non-Gaussian (binomial logit) and multi-level random-effects models. In Table 4, the four models containing `Ct` have $\Delta\text{DIC} = 0, 0.518, 0.633, 0.908$; converting $\Delta\text{DIC} < 0.91$ into model-averaged "posterior probabilities that a component is in the true model" (DIC weights of $0.558$ and $0.546$) overstates support for phylogenetic effects on transmission when $\Delta\text{DIC} < 2$ indicates complete model equivalence.
   * **Excluding unplaced species (`C. sp. 62–66`):** Five of the 21 susceptible strains in the transmission assay (*C.* sp. 63 JU4056, *C.* sp. 65 JU4093 & JU4087, *C.* sp. 66 JU4094, JU4088, JU4096—actually 6 of the 21 strains!) belong to species without phylogenetic placement (Figure 1 legend, line 136). With only ~15 phylogenetically placed strains in the transmission model, estimating two phylogenetic terms (`phylo. dist.` + `pairwise phylo. dist.`) plus `Ct`, `species`, and `strain` random effects over-parameterizes the covariance structure, producing $R^2$ credible intervals spanning `0% to 89%`.
3. **Pillar 2 & 6 Violation — Variable Starvation Time (3 to 28 Days) Confounds Susceptibility and Inoculum Degradation (Methods line 32):**  
   Populations were initiated with 5 adults and harvested "until freshly starved," which took "anywhere from 3 to 28 days" depending on the strain (line 32). Slow-growing gonochoristic (sexual) strains that took 20–28 days to exhaust the OP50 lawn experienced fewer host generations per unit time, lower peak worm density, and up to 4 weeks of extracellular thermal degradation of the initial $3\,\mu\text{L}$ viral inoculum and shed virions at $20^\circ\text{C}$, whereas fast-growing hermaphroditic *C. elegans* starved the plate in 3–5 days. Neither days-to-starvation nor reproductive mode (hermaphroditic vs. gonochoristic, which impacts mating-dependent population growth and density during 5-worm founding and 20-worm passaging) was included as a covariate in the susceptibility or transmission models.
4. **Pillar 4 Violation — Ad-Hoc Susceptibility Threshold Definition (`1 SD` below the minimum Ct of Benchmark 4, line 74):**  
   Line 74 reports that Benchmark 4 (cell-free plates washed 5 times) had $\text{mean(Ct)} = 38.4$, $\text{SD(Ct)} = 2.6$, and a minimum observed $\text{Ct} = 33.6$ ("maximum amount of virus detected in benchmark 4 plates"). The authors then computed the pooled within-strain $\text{SD(Ct)} = 4.1$ across experimental plates (assigning $\text{Ct} = 40$ to non-detects) and subtracted $1 \times 4.1$ from $33.6$ to get $\text{Ct} < 29.5$, classifying a strain as susceptible if *at least 1 of 3 replicates* had $\text{Ct} < 29.5$. Fortunately, because 17 of 21 strains also crossed the strict Benchmark 5 ($\text{Ct} < 22.0$), this ad-hoc rule only affects 4 borderline strains (`JU2837`, `JU4056`, `JU4088`, `JU4096`), all 4 of which were largely dead-end hosts in the transmission assay.

---

## 4. Quantitative Rubric Scoring

| Rubric Dimension | Score | Max | Forensic Justification |
| :--- | :---: | :---: | :--- |
| **1. Methodological & Statistical Rigor** | **2.7** | **3.5** | Strong experimental controls (Benchmarks 4 and 5) and time-series replication validation; penalized for fitting Gaussian linear mixed models to a 4-level ordinal transmission score and over-parameterizing phylogenetic variance components across ~15 placed strains ($R^2$ CIs spanning $0\text{–}89\%$). |
| **2. Claim-to-Evidence Alignment** | **2.1** | **2.5** | Core claims on host range, phylogenetic signal in susceptibility, and viral load driving transmission are well bounded; claims of DIC support for phylogenetic effects on transmission ($\Delta\text{DIC} \le 0.91$) are slightly overstated. |
| **3. Data Integrity & Biological/Behavioral Plausibility** | **1.5** | **2.0** | Days to starvation varied 9-fold (3 to 28 days) across strains and reproductive modes (hermaphrodite vs. mated female transfers) without covariate adjustment in the models. |
| **4. Reproducibility & Data Integrity** | **2.0** | **2.0** | Exemplary reproducibility: complete raw Ct datasets, strain/block metadata, and R analysis scripts deposited on GitHub (`clarashaw/Caenorhabditis-Orsay-virus-spillover`) and in supplementary materials. |
| **Total Composite Score** | **8.3** | **10.0** | **Strong / Sound** (Scientific Core Score: **6.3 / 8.0**) |

---

### Constructive and Doable Suggestions for Improvement

1. **Refit the Transmission Model Using an Ordinal Probit (`family = "ordinal"`) or Passage-Survival Likelihood:**  
   * **WHY:** Treating a bounded 0–3 ordinal score as Gaussian produces invalid residual variance estimates and predictions outside the support of the score.  
   * **WHAT & HOW:** In `MCMCglmm`, change `family = "gaussian"` to `family = "ordinal"` (or model the number of passages with detectable virus $k \in \{0, 1, 2, 3, 4, 5\}$ per replicate plate directly rather than collapsing to a 0–3 score) using the existing R script in the GitHub repository.
2. **Test Days-to-Starvation and Reproductive Mode (Hermaphrodite vs. Gonochoristic) as Covariates:**  
   * **WHY:** Plates that took 28 days to starve experienced longer viral decay and slower host density build-up than plates that starved in 3 days, and transferring 5 or 20 mated females in sexual species has different demographic variance than transferring hermaphrodites.  
   * **WHAT & HOW:** Add `days_to_starvation` (recorded in Table S1/S2) and `reproductive_mode` as fixed covariates in the susceptibility and transmission `MCMCglmm` suites to verify that the phylogenetic distance effect is not confounded by life-history speed or mating system.
3. **Temper Claims of Phylogenetic Support in the Transmission Model:**  
   * **WHY:** $\Delta\text{DIC} \le 0.91$ between models with and without phylogenetic terms in Table 4 represents statistical tie/indistinguishability, and the $R^2$ 95% CI for phylogenetic distance in transmission spans `[0%, 89.0%]`.  
   * **WHAT & HOW:** Revise lines 158 and 167 to state that once primary-exposure viral amplification ($\text{Ct}$) is accounted for, any residual direct effect of phylogeny on transmission cannot be statistically resolved with the current sample of 15 phylogenetically placed susceptible species.
