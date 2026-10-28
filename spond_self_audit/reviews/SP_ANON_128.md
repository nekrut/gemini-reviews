# Blinded Review: SP_ANON_128

**Composite Score:** 9.2 / 10.0 (Rigor: 3.3/3.5 | Claims: 2.4/2.5 | Biology: 1.7/2.0 | Reproducibility: 1.8/2.0)
**Bias Category:** None (Methodologically Sound)
**Verdict:** Accept
**Study Modality:** Dry-Lab Theory/Methods/Simulation
**Technology Maturity:** Mature/Classical
**Epistemic Stage:** Basic/Mechanistic Discovery

---

## 1. Executive Summary

This manuscript introduces `FUBAR` (Fast Unconstrained Bayesian AppRoximation), a codon-based random-effects method for inferring pervasive purifying and diversifying selection across protein-coding alignments. By precomputing conditional site likelihoods over a dense, fixed $N \times N$ grid of synonymous ($\alpha$) and nonsynonymous ($\beta$) substitution rates ($20 \times 20 = 400$ points) and using Markov chain Monte Carlo (MCMC) over a Dirichlet hyperprior to infer the grid weight vector $\theta$, `FUBAR` decouples phylogenetic likelihood evaluation from parameter optimization. The authors benchmark `FUBAR` against `FEL`, `REL`, and `PAML` (`M2a`, `M8`) across extensive parametric simulations and 16 empirical datasets, and demonstrate its scalability on a 3,142-sequence human Influenza A H3 hemagglutinin alignment. Aside from a single unremoved internal author note in the Results section, the mathematical formulation, adversarial simulation design, and empirical validation are exemplary.

---

## 2. Methodological & Statistical Audit

* **Decoupling Phylogenetic Likelihoods via Fixed Grid Discretization and MCMC:** Standard random-effects likelihood (`REL` / `PAML`) methods optimize the locations and weights of a small number (typically 3 to 10) of rate classes by recomputing Felsenstein's pruning algorithm across the entire tree at every optimization step, resulting in severe computational bottlenecks and local optima. By fixing a dense $20 \times 20$ grid of $(\alpha, \beta)$ values and precomputing the $400 \times S$ conditional likelihood matrix $P(X_s \mid \alpha_i, \beta_j)$ once, `FUBAR` reduces inference of the alignment-wide rate distribution $\theta$ to fast matrix-vector multiplications during Metropolis-Hastings MCMC over a conjugate-like Dirichlet prior $\text{Dir}(\alpha_D)$.
* **Adversarial Demonstration of Model Misspecification in Coarse Discrete REL (`PAML M2a/M8`):** One of the sharpest methodological contributions of the paper is the 4-category simulation experiment ($\beta \in \{0.2, 1, 3, 11\}$ with $\alpha = 1$). Because `PAML M2a` has only a single positive selection rate class ($\omega_2 > 1$), the presence of a strong selection category ($\beta = 11$) drags the estimated $\hat{\omega}_2$ upward to $\approx 5.95$. Consequently, moderately selected sites ($\beta = 3$) are closer to $\omega_1 = 1$ than to $\hat{\omega}_2 = 5.95$ whenever random variation yields fewer than the expected substitutions, causing `M2a` posterior probabilities for $\beta = 3$ sites to become pathologically bimodal (clustering near $P = 0$ and $P = 1$) with a 28% false-positive rate for neutral sites when $\alpha_D$ is not regularized! `FUBAR`'s dense 400-point grid completely eliminates this artifact.
* **Conditioning on Point Estimates of Topology, Branch Lengths, and GTR Parameters:** To achieve its speed, `FUBAR` fixes the tree topology, relative branch lengths, and nucleotide substitution parameters at their nucleotide-level maximum likelihood estimates rather than integrating over their posterior uncertainty. The authors explicitly acknowledge this approximation in the Discussion and show via simulation that empirical Bayes posterior probabilities remain conservative ($<5\%$ FPR at $P \ge 0.95$).
* **Editorial Oversight on Line 207:** In the middle of the *Empirical Data Sets* results section (line 207), an internal drafting note was accidentally left in the manuscript text: `"Discussion of what we would hope for should go in Discussion."` This sentence should be deleted in proof correction.

---

## 3. Biological / Experimental Grounding & Claim Proportionality

* **`[Well Supported]` Order-of-Magnitude Speedups Without Loss of Statistical Power or False-Positive Control:** Across both the 16 empirical datasets and the simulated alignments, `FUBAR` runs 10- to 300-fold faster than `FEL` and `PAML` (analyzing 3,142 Influenza H3 sequences in 7.3 minutes on 4 CPU cores versus 32.5 hours for `FEL` on 64 cores) while maintaining empirical FPR $\le 0.02$ at posterior probability $\ge 0.95$ and matching or exceeding the power of `FEL` and `PAML M8`.
* **`[Well Supported]` Structural Localization of Positively Selected H3 Hemagglutinin Sites:** Mapping the 25 positively selected sites identified in the 3,142-sequence Influenza A H3 alignment onto the HA crystal structure confirms strong spatial clustering on the solvent-exposed globular head within canonical antibody-binding epitopes ($p < 0.0001$ vs. random surface permutations).

---

## 4. Reproducibility & Data Completeness

* **Code & Data Availability:** `FUBAR` is openly distributed both within the `HyPhy` software package (`www.hyphy.org`) and on the `Datamonkey` web server (`www.datamonkey.org`), and all simulated alignments, empirical datasets, and analysis scripts are archived at `www.hyphy.org/pubs/fubar/`.
