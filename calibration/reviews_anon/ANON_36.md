# Review of ANON_36

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **9.0 / 10.0** (Exemplary)  
* **Score Breakdown:** Rigor: 3.3/3.5 | Claims: 2.2/2.5 | Biology: 1.9/2.0 | Reproducibility: 1.6/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript investigates the timing and origin of the earliest sustained SARS-CoV-2 community transmission networks in North America (Washington state) and Europe (Bavaria, Germany, and Northern Italy). Combining forward epidemiological and evolutionary simulations in `FAVITES` (1,000 replicates parameterized with empirical doubling times of 4.7 days for Washington and 3.4 days for Italy and substitution rates of $0.8 \times 10^{-3}$ to $1.6 \times 10^{-3}$ substitutions/site/year), forensic sequence quality auditing, and Bayesian generalized linear model (GLM) phylogeographic inference incorporating air passenger flow and unsampled ("ghost") taxa from 12 undersampled regions, the authors test whether the earliest detected introductions (`WA1` on January 15, 2020, in Washington; `BavPat1` in late January 2020 in Germany) founded the subsequent continental outbreaks. They reject a direct `WA1` origin for the Washington outbreak clade ($P < 0.001$ across 294 genomes; $P = 0.010$ across 1,000 genomes including late basal isolate `WA-S566`), demonstrate that apparent evolutionary intermediates in British Columbia lacking `C17747T` are amplicon primer-trimming artifacts (`nCov2019_58_RIGHT`), date the independent founding of the Washington clade to late January / early February 2020, and reject a German (`BavPat1`) origin for the Northern Italian `B.1` outbreak ($P = 0.004$; posterior probability = 0.84 for independent introductions from China).

This is a methodologically rigorous study that demonstrates how forward coalescent/transmission-network simulations and covariate-informed Bayesian phylogeography can resolve competing epidemiological hypotheses when viral genetic diversity is near zero. The forensic identification of the ARTIC primer overwrite at nucleotide 17,747 prevents a major phylogeographic misinterpretation. Minor limitations include assuming random rather than contact-clustered genomic sampling in the `FAVITES` topological null distributions, fixing the molecular clock rate in forward simulations rather than integrating over rate uncertainty, and a nucleotide swap typo in the Figure 1 caption.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **The Washington state outbreak clade did not descend directly from the January 15, 2020 `WA1` case, but arose from a later independent introduction from China around late January / early February 2020: [Well Supported].**  
  Across 1,000 `FAVITES` epidemic simulations initiated by `WA1` on January 15, 0% of simulated 294-tip phylogenies produced a single outbreak clade separated by $\ge 2$ mutations (`C17747T` and `A17858G`) without leaving basal polytomy or single-mutation sibling lineages ($P < 0.001$; Figure 2). Even when expanding to 1,000 genomes including the late-sampled `WA-S566` lineage, observing only two basal lineages remains improbable ($P = 0.010$), and Bayesian GLM phylogeography independently places the introduction at February 1, 2020 (95% HPD: January 14 – February 15) with unsampled taxa or January 26, 2020 (95% HPD: January 15 – February 7) without unsampled taxa.

* **Apparent intermediate `A.1` genomes in British Columbia and U.S. states carrying the ancestral `C17747` state alongside `A17858G` are ARTIC primer-incorporation artifacts rather than evolutionary intermediates: [Well Supported].**  
  The authors show that six British Columbia `C17747` genomes share 1 to 4 derived downstream tips mutations with locally co-circulating `C17747T` genomes (Figure 3, Table S2), a pattern incompatible with true basal divergence or independent back-mutation and explained by failure to trim the overlapping `nCov2019_58_RIGHT` primer containing the reference `C17747` allele.

* **The Northern Italy (`B.1`) outbreak was established by an independent introduction from Hubei/China around January 28, 2020 (95% HPD: January 20 – February 6), rather than descending from the extinguished Bavarian (`BavPat1`) outbreak: [Well Supported].**  
  Forward simulations conditioned on `BavPat1` founding the Italian outbreak show that the complete absence of basal polytomy lineages in Germany/Italy is unlikely ($P = 0.004$, Figure S7), and Bayesian GLM phylogeography with travel history and unsampled Italian/Hubei diversity supports independent introductions from China into Germany and Italy ($\text{pp} = 0.84$ vs. $\text{pp} = 0.16$; Figure 5).

* **Public health containment extinguished the earliest mid-January introductions (`WA1` and `BavPat1`), delaying sustained community transmission in the United States and Europe by several weeks: [Moderately Supported].**  
  The extinction of the `BavPat1`-specific transmission chain in Bavaria and the absence of `WA1`-identical or 1-mutation-derived descendants in early Washington surveillance (including 6,908 retrospective Seattle Flu Study swabs that were negative until late February) strongly support successful containment of those index cases, though the exact number of undetected dead-end introductions during late January and February cannot be bounded from genomic data alone.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Evaluate the Sensitivity of `FAVITES` Topological $P$-Values to Clustered (Non-Uniform) Case Ascertainment
* **WHY:** In the `FAVITES` simulations, 294 (or 1,000) viral genomes are subsampled uniformly at random from the simulated infected population at the end of the 61-day window. In practice, early genomic sequencing in Washington state and Northern Italy was often clustered by hospital, household, or nursing home outbreak (e.g., the Life Care Center in Kirkland, WA). Strong overdispersion in sampling ($k \ll 1$) reduces the effective number of independent transmission lineages captured in a sample of size $N$, which can increase the probability of missing rare basal sibling lineages.
* **WHAT:** Quantify how clustered sampling affects the probability of observing the empirical topologies in Figure 2D and Figure S7.
* **HOW:** Using the existing 1,000 `FAVITES` transmission network outputs, resample 294 (and 1,000) tips using a two-stage cluster-sampling scheme (selecting transmission clusters/infector nodes with Dirichlet-multinomial overdispersion before sampling descendants) and report the resulting empirical $P$-values for scenarios (i)–(iv) in Figure 2.

#### 2. Incorporate Travel Restriction Indicator Variables Directly into the Unsampled-Taxa GLM Phylogeography
* **WHY:** In the main text (lines 35 and 39), the authors note that the time-homogeneous GLM phylogeographic reconstruction incorporating unsampled taxa does not account for the abrupt suspension of non-U.S. resident air travel from China on February 2, 2020 (and the January 23 Wuhan lockdown), which shifts the inferred Washington introduction date slightly later (February 1 vs. January 26 without unsampled taxa).
* **WHAT:** Combine the epoch-based (time-inhomogeneous) air-traffic covariate model (Figure S4–S5) with the unsampled-taxa dataset so that both sampling gaps and February travel reductions are modeled simultaneously.
* **HOW:** Specify a two-epoch GLM diffusion matrix in BEAST (splitting at January 23 / February 2, 2020, with reduced post-restriction passenger flow from Hubei/China) on the dataset containing the unsampled taxa, and report the updated Markov jump introduction date HPD for the WA outbreak clade.

#### 3. Technical and Editorial Correction in Figure 1 Caption
* **WHY:** The caption to Figure 1B contains a nucleotide transposition typo at the two clade-defining sites.
* **WHAT & HOW:** In the Figure 1B caption (line 66), change `"Hypothetical phylogeny in which A17747 and C17858 from the original WA1 virus are maintained"` to `"Hypothetical phylogeny in which C17747 and A17858 from the original WA1 virus are maintained"`, matching the ancestral nucleotides of `C17747T` and `A17858G` stated in the main text (line 21).
