# Blinded Review: SP_ANON_043
**Composite Score:** 8.4 / 10.0 (Rigor: 2.7/3.5 | Claims: 2.0/2.5 | Biology: 1.7/2.0 | Reproducibility: 2.0/2.0)
**Bias Category:** Unbenchmarked Scalability Claims & Absence of Ground-Truth Error Evaluation
**Verdict:** Minor Revision
**Study Modality:** Dry-Lab Theory/Methods/Simulation
**Technology Maturity:** Mature/Classical
**Epistemic Stage:** Basic/Mechanistic Discovery

---

### 1. Executive Summary
This software note introduces LEISR (Likelihood Estimation of Individual Site Rates), a maximum-likelihood (ML) fixed-effects method implemented in HyPhy ($\ge 2.3.8$) for inferring relative site-wise evolutionary rates from nucleotide or amino acid alignments. Generalizing the ML framework of Rate4Site, LEISR estimates alignment-wide branch lengths under a user-specified nucleotide or protein substitution model and then fits a site-specific branch-length scaling parameter $r_s$ at every alignment site (including gapped sites ignored by Rate4Site), with support for GARD-partitioned alignments and MPI parallelization. Using pyvolve simulations (10 replicates of 100-site protein alignments on 25-, 50-, and 100-taxon trees under WAG + discrete Gamma) and an empirical 23-taxon mammalian HRH1 alignment (478 gap-free sites), the authors show high linear concordance ($R^2 > 0.89$ on simulations; $R^2 = 0.93$ on HRH1) between LEISR and Rate4Site ML estimates.

LEISR is a well-engineered, practical addition to the HyPhy suite, and all validation code and simulated datasets are openly available on GitHub. The primary limitations of the manuscript are that (1) its headline claims of scalability up to 10,000 sequences, MPI high-throughput speed, and recombination-partitioned inference are asserted in the Introduction without any corresponding benchmarks in the Results, and (2) the simulation study evaluates only concordance between LEISR and Rate4Site ML ($R^2$) rather than estimation accuracy against the true simulated site rates or comparison against Rate4Site's default empirical Bayes shrinkage estimator.

---

### 2. Methodological & Statistical Audit
* **Comparison Against Rate4Site ML Rather Than Ground-Truth Simulated Rates:** In the simulation experiments (25, 50, and 100 taxa, 100 sites simulated under a 20-category discrete Gamma distribution with $\alpha = 0.4$), the Results report only the Pearson $R^2$ between LEISR and Rate4Site ML rate inferences (Figs. 1–2). Because both tools optimize the same two-step fixed-effects site likelihood under the WAG model, high correlation between them verifies numerical optimization equivalence rather than statistical accuracy relative to the true simulated site rates. Evaluating root-mean-square error (RMSE) or rank correlation against the true simulated rates—and benchmarking profile-likelihood 95% CI coverage—would directly establish estimator performance.
* **Fixed-Effects ML Variance vs. Empirical Bayes Shrinkage on Small Alignments:** Rate4Site's default and most widely used mode is empirical Bayes (random effects with a Gamma prior), which shrinks extreme site rate estimates on small or low-divergence alignments. Fixed-effects ML estimation infers an independent parameter $r_s$ per site, which yields $\hat{r}_s = 0$ at invariant sites and noisy, upward-biased estimates at rapidly evolving sites when the taxon count or tree length is small (such as the 23-taxon empirical HRH1 alignment with total tree length 3.30). While the authors note that empirical rate distributions can be zero-inflated and overdispersed (suggesting median normalization, line 34), a brief comparison against empirical Bayes rate estimates on the 25-taxon simulations and 23-taxon HRH1 dataset would clarify the bias-variance trade-off for users analyzing small alignments.
* **Identifiability and Conflation of Branch Lengths with Site Rates:** The authors provide a clear and accurate methodological discussion (line 30) explaining why enabling parametric rate heterogeneity (+G or GDD) during the alignment-wide branch-length optimization step conflates branch-length scaling with site-level rates, and they appropriately recommend optimizing branch lengths without parametric rate variation (`LEISR` rather than `LEISR+G`).

---

### 3. Biological / Experimental Grounding & Claim Proportionality
* **Unbenchmarked Scalability and Partitioning Claims:** The Abstract and Introduction emphasize that LEISR *"has been successfully tested with alignments containing up to 10,000 sequences, several orders of magnitude beyond what Rate4Site can fit,"* supports partitioned alignments to correct for recombination breakpoints, and uses MPI for rapid high-throughput analysis. However, the Results section tests only 25-, 50-, and 100-taxon alignments of 100 sites and a 23-taxon empirical alignment, noting only qualitatively that Rate4Site failed with 16 gamma categories at 100 taxa. Including even a single runtime and memory scaling table across $N = 100, 1,000, \text{ and } 10,000$ sequences (where Rate4Site fails due to underflow) would substantiate the paper's central motivation.
* **Handling of Gapped Sites and Substitution Models:** Computing rates across all alignment columns (rather than dropping sites gapped in an arbitrary reference sequence, as Rate4Site does) and expanding support to GTR/HKY85 nucleotide and specialist protein models (`mtMet`, `mtVer`, `HIV B/W`) are practical improvements for comparative genomics. Nonetheless, at heavily gapped sites where the effective subtree contains very few non-gap characters, fixed-effects ML point estimates have very wide confidence intervals; reminding users to filter or weight by the profile-likelihood 95% CI width reported in `.leisr.json` would prevent over-interpretation of gapped columns.

---

### 4. Reproducibility & Data Completeness
* **Open-Source Software & Validation Pipeline:** Reproducibility is exemplary. LEISR is distributed directly within the open-source HyPhy platform ($\ge 2.3.8$, `LEISR.bf`) with documented JSON output schemas, and the complete Python (`pyvolve`) simulation pipeline, empirical alignment, and figure-generation scripts are publicly archived at `https://github.com/sjspielman/leisr_validation`.
