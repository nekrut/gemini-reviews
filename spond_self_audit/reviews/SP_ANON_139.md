# Blinded Review: SP_ANON_139

**Composite Score:** 8.3 / 10.0 (Rigor: 3.0/3.5 | Claims: 2.3/2.5 | Biology: 1.5/2.0 | Reproducibility: 1.5/2.0)
**Bias Category:** None (Methodologically Sound)
**Verdict:** Accept
**Study Modality:** Dry-Lab Theory/Methods/Simulation
**Technology Maturity:** Mature/Classical
**Epistemic Stage:** Basic/Mechanistic Discovery

---

## 1. Executive Summary

This theoretical and simulation study directly addresses Rodrigue's (2013) critique of fixed-effects maximum-likelihood (FE-ML) phylogenetic models (where a separate parameter is estimated for each codon site, such as `FEL` or site-specific mutation-selection models). Rodrigue argued that FE-ML methods suffer from the classic Neyman-Scott incidental parameters problem, where adding more sites increases the number of parameters linearly and allegedly prevents consistency. By clarifying the mathematical structure of the phylogenetic likelihood and conducting controlled parametric simulations under two K80 models—Model 1 (estimating a separate rate $r_i$ at each site as taxa $N$ grow from 64 to 1,024) and Model 2 (estimating branch lengths $t_b$ as sites $S$ grow from 64 to 1,024)—the authors prove that site-specific parameters depend asymptotically on the number of **taxa ($N$)** (vertical information), not the number of **sites ($S$)** (horizontal information), and converge to their true values with Gaussian asymptotic distributions as $N \to \infty$.

---

## 2. Methodological & Statistical Audit

* **Orthogonal Resolution of the Neyman-Scott Fallacy in Site-Independent Phylogenetic Models:** The manuscript makes a crisp, mathematically exact distinction that resolves a recurring confusion in the molecular evolution literature. When global parameters (such as branch lengths and transition/transversion ratio $\kappa$) are shared across sites while site-specific rate parameters $r_i$ act independently within site $i$, the log-likelihood separates additively across sites once global parameters are consistent ($\hat{\theta}_{\text{global}} \to \theta_0$ at rate $O_p(S^{-1/2})$). Consequently, estimating $r_i$ at site $i$ is not corrupted by adding more sites $S$; rather, the information for $r_i$ scales with the number of branches/taxa $N$ (specifically, with total tree length $T_N$).
* **Empirical Convergence and Normality Verification (Tables 1 and 2):** The simulation design tests $N \in \{64, 128, 256, 512, 1024\}$ across 100 replicates under a K80 model ($\kappa = 2.0$, internal branch lengths 0.05, terminal branch lengths 0.10, site rates $r_1 = 1.0, r_2 = 2.0, r_3 = 3.0$). Table 1 demonstrates that as $N$ increases from 64 to 1,024:
  1. Mean point estimates converge tightly to the true values ($1.00, 2.00, 3.00$).
  2. The empirical standard deviation across the 100 replicates shrinks at the theoretical $O(N^{-1/2})$ rate (e.g., for $r_1 = 1.0$, $\text{SD}$ drops from $0.16$ at $N=64$ to $0.04$ at $N=1024$, an exact 4-fold reduction for a 16-fold increase in $N$).
  3. Kolmogorov-Smirnov tests confirm no significant departure from normality for non-boundary site rates.
* **Distinction Between Point-Estimate Variance and Hypothesis Testing (`LRT` Calibration):** The authors make an important statistical point in the Discussion: even on small trees where site-specific MLE point estimates have high variance (or hit $\hat{\beta}_s = 0$ when zero nonsynonymous substitutions occur), a 1-degree-of-freedom likelihood ratio test (`FEL`) comparing $\alpha_s = \beta_s$ vs. $\alpha_s \neq \beta_s$ properly accounts for estimation uncertainty via the curvature of the log-likelihood surface, avoiding false positives rather than "overfitting noise."
* **Tree Growth Regime Caveat:** In Model 1, adding taxa increases total tree length $T_N$ linearly because new internal and terminal branches have fixed lengths ($0.05$ and $0.10$). In empirical datasets where additional sequences are sampled from a fixed coalescent clade (infill asymptotics where total tree length $T_N$ converges to a finite bound or grows as $\log N$), site-rate variance shrinks with $T_N^{-1/2}$ rather than $N^{-1/2}$—a nuance well known in phylogenetic consistency theory that complements the authors' increasing-domain simulation.

---

## 3. Biological / Experimental Grounding & Claim Proportionality

* **`[Well Supported]` Statistical Consistency of Site-Specific Fixed-Effects MLEs as Taxon Sampling ($N$) Increases:** The simulation results in Table 1 and Figure 1 conclusively refute the claim that site-by-site fixed-effects likelihood estimation is statistically inconsistent as data dimensions grow.
* **`[Well Supported]` Complementary Roles of Random-Effects (`REL`/`FUBAR`) and Fixed-Effects (`FEL`/`MEME`) Frameworks:** The balanced discussion explaining when shrinkage/empirical Bayes random-effects models are advantageous (small alignments, estimating alignment-wide distributions) versus when fixed-effects LRTs are preferable (avoiding parametric prior misspecification at individual sites) is proportional and sound.

---

## 4. Reproducibility & Data Completeness

* **Simulation Pipeline:** The exact model parameters (`Seq-Gen`, `HyPhy`), tree structures, branch lengths, and summary statistics across all 1,000 simulated alignments are fully specified in the Methods and Tables 1–2, allowing straightforward independent replication.
