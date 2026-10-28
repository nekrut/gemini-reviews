# Blinded Review: SP_ANON_145
**Composite Score:** 9.1 / 10.0 (Rigor: 3.2/3.5 | Claims: 2.3/2.5 | Biology: 1.8/2.0 | Reproducibility: 1.8/2.0)
**Bias Category:** None (Methodologically Sound)
**Verdict:** Accept (Minor Revision)
**Study Modality:** Dry-Lab Theory/Methods/Simulation
**Technology Maturity:** Mature/Classical
**Epistemic Stage:** Basic/Mechanistic Discovery

---

### 1. Executive Summary
This manuscript introduces Contrast-FEL, a fixed-effects maximum likelihood codon model and likelihood-ratio test (LRT) framework implemented in HyPhy for identifying individual alignment sites experiencing different nonsynonymous substitution rates ($\beta_i$, or $\omega_i = \beta_i/\alpha$) across $K \ge 2$ predefined sets of phylogenetic branches. The authors evaluate the method across 3,706 simulated alignments (1,594,400 codon sites) generated via Latin Hypercube Sampling over tree topologies, branch lengths, alignment sizes, and branch partitions, as well as under a random-effects branch-site model to assess misspecification robustness, and apply it to five empirical datasets (HIV-1 RT drug resistance, HIV-1 `env` transmission mode, *Brassicaceae* `BLT`, C3/C4 plant `rbcL`, and Haemosporidian `cytB`).

The statistical formulation is sound, the simulation benchmark is comprehensive, and the manuscript convincingly demonstrates why common post-hoc heuristics (running separate selection tests on branch subsets and comparing significance calls) suffer from either massive false positive inflation (53.0% FPR under discordant-call rules) or severe power loss (17.1% power under positive-vs-neutral rules). Minor methodological points involve the sequential stopping rule used for the 20-iteration branch permutation test and conditioning on point estimates of global nuisance parameters.

---

### 2. Methodological & Statistical Audit
* **Rigorous Direct Formulation vs. Post-Hoc Subgroup Comparisons:** Contrast-FEL directly tests $H_0: \beta_1 = \beta_2 = \dots = \beta_K$ (and all pairwise contrasts $\beta_i = \beta_j$ with Holm–Bonferroni FWER control and Benjamini–Hochberg FDR $q$-values) while estimating a site-specific synonymous rate $\alpha$. The direct comparison against post-hoc FEL heuristics on 185,070 simulated sites provides a textbook demonstration of the "difference between significant and not significant is not itself statistically significant" fallacy in molecular evolution.
* **Calibration, Saturation Limits, and Boundary Behavior:** Across >1 million null variable sites, the asymptotic $\chi^2_d$ LRT maintains nominal or slightly conservative Type I error control (due to boundary constraints $\hat{\beta}_i = 0$ at low-divergence sites), and the authors explicitly identify and quantify the regime where the test becomes anticonservative: extreme site saturation where the product of the maximum rate estimate and tree length exceeds $10^2$ expected substitutions per site (Figure 1A, E).
* **Coarse Granularity and Sequential Stopping Bias in the Permutation Test:** In the Materials and Methods, the optional branch-set permutation test is described as shuffling branch labels *"up to 20 times. If we find the LRT as high or higher as observed on the original partition for any of the tests, at iteration $j$, we report permutation $P$-value of $1/j$ (and stop the process); otherwise, we report a permutation $P$-value of 0.05."* Stopping at the first exceedance ($j$) and reporting $p = 1/j$ is a biased estimator of the permutation tail probability (for example, if the first random permutation happens to exceed the observed statistic, reporting $p = 1/1 = 1.0$, or if the second exceeds it, $p = 1/2 = 0.50$, overestimates $p$, whereas capping non-exceedances at 20 trials floors the minimum achievable $p$-value at $0.05$, which is why permutation $p$-values cannot be used for BH FDR correction across hundreds of sites). Increasing the default permutation cap (e.g., to $M = 100$ or an adaptive sequential Monte Carlo rule requiring $r \ge 5$ exceedances with $\hat{p} = (r+1)/(M+1)$) would make the permutation $p$-value properly calibrated.
* **Model Misspecification Scope:** Evaluating Contrast-FEL on alignments simulated under a random-effects branch-site model (BUSTED-S / CV3o6) is a useful check showing slight LRT inflation (FPR = 0.07 at $\alpha = 0.05$) mitigated by branch permutation (FPR = 0.045), though the authors appropriately note that a single misspecification scenario cannot guarantee robustness under severe clade-specific heterotachy or multinucleotide substitutions.

---

### 3. Biological / Experimental Grounding & Claim Proportionality
* **Superior Precision-Recall of Contrast-FEL Over Post-Hoc FEL Heuristics [Well Supported]:** Supported by 185,070 simulated sites (FPR 3.4%, PPV 62.0% for Contrast-FEL vs. FPR 53.0%, PPV 15.2% for discordant post-hoc FEL).
* **Recovery of Known HIV-1 Drug Resistance Mutations in RT [Well Supported]:** On the 476-sequence HIV-1 RT dataset comparing treatment-naive vs. post-treatment terminal branches, 12 of 15 sites at $p \le 0.05$ (PPV = 80%) and 4 of 4 sites at $q \le 0.20$ (codons 103, 181, 184, 190; PPV = 100%) are established antiretroviral resistance mutations, outperforming the specialized MEDS directional model (PPV 58.9%).
* **Empirical Re-Analyses as Hypothesis Generation [Well Supported]:** The authors carefully frame the sites detected in `env`, `BLT`, `rbcL`, and Haemosporidian `cytB`—particularly "CC" sites conserved in both groups but with differing purifying selection intensity—as statistical candidates requiring experimental follow-up rather than dispositive proof of phenotypic adaptation.

---

### 4. Reproducibility & Data Completeness
* **Code and Data Availability:** Contrast-FEL is integrated into open-source HyPhy (v2.5.2+) and Datamonkey, and all 3,706 simulated alignments, parameter settings, and 5 empirical NEXUS files are publicly archived at `data.hyphy.org/web/contrast-FEL/`.
* **Missing Equation and Minor Typographical Errors:**
  1. In Materials and Methods, the displayed equation for the MG-REV-$CF3\times 4$ codon substitution rate matrix $q_{ij}$ is missing between *"follows the standard codon-substitution model structure:"* and *"Here, $\delta(i,j)$ counts..."* (the symbols $\delta(i,j)$, $AA(x)$, $\theta$, and $\Pi$ are defined in the text, but the matrix formula itself was omitted during typesetting).
  2. In the Results text discussing Table 2, *"increases the power to 0.860 see 3"* contains an unresolved cross-reference.
