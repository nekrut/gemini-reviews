# Blinded Review: SP_ANON_099
**Composite Score:** 8.5 / 10.0 (Rigor: 2.9/3.5 | Claims: 2.3/2.5 | Biology: 1.5/2.0 | Reproducibility: 1.8/2.0)
**Bias Category:** Fixed-Topology Conditioning (`LG+F` Tree) & Upper-Tail Rate Censoring
**Verdict:** Accept
**Study Modality:** Dry-Lab Theory/Methods/Simulation
**Technology Maturity:** Mature/Classical
**Epistemic Stage:** Basic/Mechanistic Discovery

---

## 1. Executive Summary
`SP_ANON_099` presents a systematic empirical benchmark investigating whether relative site-specific protein evolutionary rate estimates—inferred via the `LEISR` (Likelihood Estimation of Individual Site Rates) method in `HyPhy`, a generalized programmatic extension of `Rate4Site`—are sensitive to the choice of empirical amino acid substitution matrix. Across 419 diverse protein alignments (comprising 100 random `TreeBase` enzyme alignments, 13 mammalian mitochondrial proteins, 79 chloroplast alignments, and 227 mammalian GPCR alignments; 426,678 total columns), the authors compare site-wise rate maximum likelihood estimates (MLEs) across six empirical exchangeability matrices (`LG`, `WAG`, `JTT`, specialist organelle matrices `mtMet` and `gcpREV`, and specialist pathogen matrix `HIVb`) as well as the equal-rates `JC` model, each evaluated with and without four-category discrete gamma ($+\Gamma_4$) branch-length optimization.

The central empirical finding is clear, quantitatively robust, and practically useful for structural bioinformaticians: site-wise relative evolutionary rates are remarkably insensitive to the choice of amino acid substitution matrix (mean Spearman $\rho > 0.92$ and Pearson $r > 0.98$ across all model pairs, rising to $\rho \ge 0.98$ among generalist matrices `LG`, `WAG`, and `JTT`), and incorporating $+\Gamma_4$ during the preliminary branch-length optimization phase has virtually zero effect on normalized site-rate rankings ($\rho > 0.99$). Even more insightfully, the authors do not stop at aggregate correlations; they isolate and biochemically dissect the 118 "diametrically opposed" sites ($0.03\%$ of all sites) where equal-rates `JC` infers top-quartile evolutionary rates ($\ge 75\text{th}$ percentile) while empirical matrices (`LG`, `WAG`, `JTT`) infer below-median conservation ($\le 50\text{th}$ percentile). They demonstrate that these sites are overwhelmingly enriched for rapid toggling among biochemically similar hydrophobic branched-chain residues ($\{\text{I}, \text{L}, \text{V}\}$), which have massive baseline exchangeabilities in empirical matrices ($q_{\text{IL}}, q_{\text{IV}}, q_{\text{LV}}$) and therefore require small site-rate multipliers $r_s$, whereas `JC` treats all amino acid replacements equally and must inflate $r_s$ to accommodate the raw substitution count.

The study is well-executed, appropriately scoped, and transparently reproducible. Two minor methodological caveats merit note: (1) for each alignment, the tree topology was held fixed at the tree inferred under `FastTree2` (`LG+F`), so potential downstream effects of matrix choice on topological reconstruction were not propagated; and (2) raw site-rate MLEs were right-censored at $r_s = 1,000$ prior to Z-score normalization, plus Equation (1) in the Methods contains a minor sign/factor typographical error in the definition of $\text{AIC}$.

---

## 2. Methodological & Statistical Audit

### Strengths in Experimental Design and Mechanistic Dissection
1. **Deliberate "Stress-Testing" with Mismatched Specialist Matrices (`mtMet`, `gcpREV`, `HIVb`) and Equal-Rates `JC`:**
   Rather than comparing only `LG`, `WAG`, and `JTT` (which were trained on overlapping cytosolic/nuclear protein databases and naturally share similar exchangeabilities), the authors deliberately apply mitochondrial (`mtMet`), plastid (`gcpREV`), and viral (`HIVb`) matrices to incompatible nuclear/organelle datasets, plus the flat `JC` model. Showing that even severely mismatched empirical matrices yield $\rho \approx 0.94\text{--}0.96$ in site-rate rankings provides a strong upper bound on model-misspecification sensitivity.
2. **Mechanistic Resolution of "Diametrically Opposed" Outlier Sites:**
   Identifying the exact 118 sites (out of 426,678) where `JC` and empirical matrices strongly disagree and proving via permutation resampling ($p < 10^{-5}$, Figure 3) that they are driven by high-frequency $\{\text{I}, \text{L}, \text{V}\}$ hydrophobic toggling is an elegant mechanistic validation of how exchangeability weights $q_{ij}$ interact with site-rate scalars $r_s$.
3. **Percentile Bin Concordance Analysis (Table 2):**
   Because applied users typically threshold site rates into discrete functional bins (e.g., top 5% most conserved sites as putative catalytic/binding pockets, or top 5% fastest evolving sites), evaluating classification overlap at the $\le 5\text{th}$ and $\ge 95\text{th}$ percentiles ($91.8\%$ to $96.8\%$ overlap across generalist matrices) directly addresses the practical bioinformatics use case.

### Methodological & Statistical Vulnerabilities
1. **Conditioning on a Single Fixed `LG+F` Phylogeny (`FastTree2`):**
   - *Technical critique:* In Materials and Methods (line 93), the authors infer a single phylogeny per alignment using `FastTree2` under the `LG+F` model and hold this topology fixed across all 14 `LEISR` model runs (only re-optimizing branch lengths under each respective matrix). While holding the topology fixed isolates the direct effect of the substitution matrix on site-rate estimation, in a complete pipeline where a user selects a model for *both* tree inference and `LEISR` rate estimation, matrix differences (especially `JC` or `HIVb` vs. `LG`) can alter poorly supported internal branches, which in turn alters parsimony/likelihood substitution counts at variable sites.
   - *Impact:* The reported correlations ($\rho > 0.92\text{--}0.99$) strictly measure *conditional* rate robustness given a fixed topology, slightly underestimating total pipeline variance when topology is co-estimated.
2. **Upper-Tail Censoring at $r_s = 1,000$ and Pearson Correlation on Log-Transformed Rates:**
   - *Technical critique:* To prevent numerical divergence at hypervariable or gapped sites, the authors cap raw site rate MLEs at $1,000$ (setting any $r_s \ge 1,000$ to $1,000$, line 105) before Z-score standardization, and then exclude invariant/censor-bound outlier points when computing Pearson $r$ on $\log_{10}(r_s)$ (`Figure 1` caption, line 40: *"Linear regressions blocked by alignment data set were largely comparable regardless of which rate tier is compared (the cluster of points holding large values outline rates which were driven to infinity during estimation and set to the upper limit of 1,000 by LEISR)"*).
   - *Impact:* Because `LEISR` optimizes an unconstrained maximum-likelihood scalar $r_s \in [0, 1000]$ at each site independently (rather than shrinking extreme sites toward a prior via Empirical Bayes), gapped or saturated columns frequently hit the upper boundary $r_s = 1,000$ across all matrices simultaneously. Clamping these upper-tail sites to an identical constant $1,000$ artificially pins the extreme upper-right corner of the scatter plot, which slightly inflates parametric Pearson $r$ relative to rank-based Spearman $\rho$ (explaining why Pearson $r > 0.98$ exceeds Spearman $\rho \approx 0.92\text{--}0.97$). Using Spearman $\rho$ (which the authors appropriately emphasize throughout the text and Figure 2) is more robust to this boundary clamping.
3. **Typographical Error in the $\text{AIC}$ Formula (Line 99):**
   - *Technical critique:* Line 99 writes: *"Briefly, $\text{AIC} = 2(\log L - K)$ where $\log L$ is the log-likelihood and $K$ is the number of estimated parameters."* Standard Akaike Information Criterion is $\text{AIC} = 2K - 2\log L = -2(\log L - K)$ (minimized), or if maximized as a penalized log-likelihood, $\log L - K$. Writing $2(\log L - K)$ flips the sign while stating on line 36 that *"the model with the lowest AIC score is considered the best fit."* Fortunately, this is purely a typographical slip in the manuscript text, as the actual `HyPhy` scripts in the linked repository compute standard $-2\log L + 2K$, as confirmed by `LG` and `gcpREV`/`mtMet` winning their respective datasets in Table 1.

---

## 3. Biological / Experimental Grounding & Claim Proportionality
* **Claim:** *Relative site-specific evolutionary rates inferred by `LEISR` are highly robust to the choice of empirical amino acid substitution matrix and to whether $+\Gamma_4$ rate variation is included during branch-length optimization.* — **[Well Supported]**. Exhaustively demonstrated across 419 alignments and 426,678 sites via Spearman rank correlations, linear mixed-effects regressions, and percentile overlap metrics.
* **Claim:** *Sites where equal-rates `JC` infers rapid evolution while empirical matrices infer strong conservation are driven by frequent substitutions among biochemically interchangeable hydrophobic residues ($\{\text{I}, \text{L}, \text{V}\}$).* — **[Well Supported]**. Directly proven by the amino acid composition enrichment and $10^5$-replicate permutation test in Figure 3.
* **Claim:** *Users can safely bypass computationally expensive model selection when estimating relative protein site rates with `LEISR`, provided they use a reasonable generalist empirical matrix such as `LG`, `WAG`, or `JTT`.* — **[Well Supported]**. Proportional to the empirical evidence and directly actionable for high-throughput phylogenomic pipelines.

---

## 4. Reproducibility & Data Completeness
* **Code & Data Archival:** Exemplary. All 419 alignments, inferred trees, `LEISR` rate outputs, and analysis scripts are permanently archived on GitHub (`github.com/sjspielman/aa_rate_models`) and Zenodo (`doi:10.5281/zenodo.1297092`), and `LEISR` is distributed in open-source `HyPhy` ($\ge$ v2.3.8).
