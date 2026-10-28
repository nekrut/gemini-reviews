# Blinded Review: SP_ANON_153
**Composite Score:** 9.1 / 10.0 (Rigor: 3.3/3.5 | Claims: 2.4/2.5 | Biology: 1.8/2.0 | Reproducibility: 1.6/2.0)
**Bias Category:** None (Methodologically Sound)
**Verdict:** Accept (Minor Revision)
**Study Modality:** Dry-Lab Theory/Methods/Simulation
**Technology Maturity:** Mature/Classical
**Epistemic Stage:** Basic/Mechanistic Discovery

---

### 1. Executive Summary
This manuscript introduces a fully Bayesian nonparametric codon substitution model that places a Dirichlet process prior (DPP) over site-specific nonsynonymous-to-synonymous rate ratios ($\omega = d_N/d_S$). Unlike standard maximum-likelihood and empirical-Bayes approaches (e.g., Nielsen & Yang's M3/M8 models) that fix a parametric rate distribution with a predetermined number of classes and condition site-level inference on point estimates of the tree topology, branch lengths, and substitution parameters, this method treats the number of selection classes $k$, the site-to-class partition vector $z$, class-specific $\omega_i$ values, tree topology $\tau$, branch lengths $\nu$, transition/transversion ratio $\kappa$, and codon frequencies $\pi$ as random variables jointly sampled via Markov chain Monte Carlo (using Neal's Algorithm 8 auxiliary-variable Gibbs sampler for nonconjugate Dirichlet process mixtures). Applying the model across six classic benchmark alignments (vertebrate $\beta$-globin, Japanese encephalitis virus `env`, human influenza A `HA1`, and HIV-1 `env`, `pol`, and `vif`) under three prior expectations for the number of classes ($E(k) \approx 1, 5, 10$), the authors show that $k \le 2$ rate classes have negligible posterior probability and that integrating over phylogenetic and parameter uncertainty yields more conservative, better-calibrated posterior probabilities of positive selection ($\Pr(\omega > 1 \mid X) > 0.95$) that recover the core model-robust sites of Yang et al. (2000).

This is a mathematically rigorous and conceptually foundational contribution to Bayesian molecular evolution. Minor points concern the sensitivity of the posterior number of classes $k$ to the fixed concentration parameter $\alpha$, the heavy tail of the base distribution $G_0(\omega)$, and missing typeset equations in the manuscript file.

---

### 2. Methodological & Statistical Audit
* **Full Joint Bayesian Integration Over Tree, Branch Lengths, and Nonparametric Rate Partition:** Conditioning empirical Bayes site assignments on point estimates of $(\hat{\tau}, \hat{\nu}, \hat{\kappa}, \hat{\pi}, \hat{\omega})$ ignores estimation variance and is known to produce overconfident posterior probabilities ($\ge 0.99$) on small or noisy alignments. By jointly sampling $(\tau, \nu, \kappa, \pi, z, k, \omega)$ over 2 million MCMC cycles (verified across two independent runs per alignment) and computing $\Pr(\omega_j > 1 \mid X)$ directly as the MCMC ergodic fraction of states in which site $j$ belongs to a class with $\omega > 1$, the method naturally tempers overconfident marginal calls while retaining high power on strongly selected sites.
* **Sensitivity of Cluster Count $k$ to Fixed Concentration Parameter $\alpha$:** Rather than placing a gamma hyperprior on the Dirichlet process concentration parameter $\alpha$ (which can be updated effortlessly via Escobar & West's 1995 auxiliary beta-variable Gibbs step without adding likelihood evaluations), the authors fix $\alpha$ at three discrete values corresponding to $E(k) \approx 1, 5, 10$. As shown in Tables 1–6, while the data decisively reject $k = 1$ (and $k = 2$ for four of six genes) even when $\Pr(k=1) \approx 0.94$ a priori, the posterior mean $E(k \mid X)$ tracks the prior mean closely between $E(k) = 5$ and $E(k) = 10$ (e.g., HIV-1 `vif`: $E(k \mid X) = 6.33$ vs. $10.21$; $\beta$-globin: $5.65$ vs. $8.95$). Fortunately, Figure 2 and Table 7 demonstrate that the marginal site-level distributions $\Pr(\omega_j > 1 \mid X)$ stabilize once $E(k) \ge 5$ because additional clusters simply subdivide the purifying/neutral regime or merge/split redundant rate values.
* **Heavy-Tailed Base Measure $G_0(\omega)$:** The base distribution $G_0(\omega) = (1 + \omega)^{-2}$ (the ratio of two i.i.d. exponential variables) is symmetric in $\log \omega$ around $\omega = 1$ ($\Pr(\omega > 1) = 0.50$) but has no finite mean ($E[\omega] = \infty$). While convenient and scale-free, a 50% prior mass on $\omega > 1$ for newly drawn auxiliary components in Neal's Algorithm 8 means that the prior probability of positive selection at a site is 0.50; noting how site-level posteriors behave under a more conservative base measure (e.g., $\text{Gamma}$ or log-normal centered below 1) would be informative.

---

### 3. Biological / Experimental Grounding & Claim Proportionality
* **Inadequacy of 1- or 2-Class Selection Models Across Protein-Coding Genes [Well Supported]:** Across all six viral and vertebrate alignments, posterior support for $k=1$ is $0.0000$ under all priors, and support for $k \le 2$ is $0.0000$ for HIV-1 `vif`, HIV-1 `pol`, and vertebrate $\beta$-globin even when $>99\%$ of prior mass is placed on $k \le 2$.
* **Concordance and Calibration of Positively Selected Sites Relative to Parametric Empirical Bayes [Well Supported]:** On the negative controls (vertebrate $\beta$-globin and JEV `env`), the DPP model calls zero sites at $\Pr(\omega > 1 \mid X) > 0.95$ across all three priors, whereas on HIV-1 `env`, `pol`, `vif`, and influenza `HA1`, it consistently recovers the sites that were invariant across Yang et al.'s (2000) parametric M3–M13 models.

---

### 4. Reproducibility & Data Completeness
* **Missing Mathematical Equations in the Manuscript Text:** In the Materials and Methods section, seven displayed equations (the codon rate matrix $Q_{ij}$, the Stirling number of the second kind $S(c,k)$, the alignment likelihood $\mathcal{L}$, Bayes' theorem for the joint posterior, the Ewens/DPP partition distribution $f(z, k \mid \alpha, c)$, the marginal prior $f(k \mid \alpha, c)$, and the prior expectation $E(k)$) are missing from the text and appear only as empty table boxes (`| |`). These equations must be restored.
* **Minor Typos and Software Availability:**
  1. In Table 7, under `HIV-1 vif` for $E(k) = 1$, codon **`33`** is listed twice (`33, 167, 33, 127, 39...`).
  2. In Table 8, *"Tree topoology"* is misspelled.
  3. The manuscript states *"We wrote a computer program that implements the MCMC method"*, but provides no URL or source code repository for the C/C++ implementation. Providing a permanent link to the source code and executable would substantially enhance reproducibility.
