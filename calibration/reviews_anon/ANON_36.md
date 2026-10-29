# Review of ANON_36

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **8.9 / 10.0** (Strong / Sound) | **Scientific Core Score:** **7.0 / 8.0**  
**Overall Score:** 8.9 / 10.0  
* **Score Breakdown:** Rigor: 3.0/3.5 | Claims: 2.2/2.5 | Biology: 1.8/2.0 | Reproducibility: 1.9/2.0  
**Score Breakdown:** Methodological Rigor: 3.0/3.5 | Claim-Evidence Alignment: 2.2/2.5 | Biological Plausibility: 1.8/2.0 | Reproducibility: 1.9/2.0  
**Verdict:** Strong / Sound

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT (Executive Summary)

This manuscript presents the architectural and methodological advances in the BEAST 2.5 Bayesian evolutionary analysis platform since its initial 2.0 release. The authors review core improvements (faster Felsenstein pruning with invariant sites, NEXUS calibration and multifurcating constraint import in BEAUti, versioned package management) and synthesize over 30 modular packages spanning generalized phylogenetic structures: sampled-ancestor fossilized birth-death trees (`SA`, `BDSKY`), structured birth-death and coalescent approximations (`bdmm`, `MultiTypeTree`, `BASTA`, `MASCOT`, `PhyDyn`), within-host transmission trees (`SCOTTI`, `BadTrIP`), multispecies coalescent models (`StarBEAST 2`, `STACEY`, `SNAPP`, `PoMo`), reticulate evolution (`BACTER` bacterial gene conversion, `SpeciesNetwork` MSNC, `DENIM`, and `AIM` isolation-with-migration), reversible-jump site model averaging (`bModelTest`), nested sampling (`NS`), and posterior predictive model adequacy (`TreeModelAdequacy`, `MASTER`). Four worked empirical analyses are presented with complete XML, alignment, and post-processing scripts archived on Zenodo and GitHub.

This is a well-engineered, mathematically coherent software synthesis backed by exemplary open data and reproducible configuration files. Its primary limitations are: (1) in the West African Ebola `bdsky` + `SA` case study (Fig. 3), applying an unstructured panmictic birth-death skyline model across three countries with distinct epidemic waves leads to systematic over- and under-estimation of the sampling proportion $p = \psi/\delta$ (exceeding empirical case counts in mid-2014), (2) in the Princess cichlid `AIM` analysis (Fig. 5), fixing the root calibration to a point value (9.2 Mya) and using a single informative prior on migration scalers leaves Bayes factor sensitivity untested, and (3) third-party package quality assurance is acknowledged as informal, lacking a centralized continuous-integration calibration suite. All of these issues can be addressed through targeted discussion and minor supplementary sensitivity checks.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT (Detailed Rubric Evaluation)

* **Reversible-jump MCMC in `bModelTest` integrates over nucleotide substitution model uncertainty without committing to a single a priori model (Section "Site models", Fig. 2): [Well Supported].**  
  Applied to 906 bp of mtDNA across 36 mammalian species, `bModelTest` demonstrates that posterior probability mass is spread across an 8-model 95% credible set rather than concentrated on a single canonical model (such as HKY or GTR), while seamlessly averaging the tree topology and branch lengths over this credible set.

* **The birth-death skyline (`bdsky`) with sampled ancestors (`SA`) recovers the temporal trajectory of $R_e$ and origin time $t_0$ for the 2013–2016 West African Ebola epidemic (Section "Population dynamic models for trees", Fig. 3): [Moderately Supported].**  
  Across 811 coding genomes sampled through October 2015, the inferred origin $t_0$ aligns with the December 2013 index case and $R_e$ tracks the September–October 2014 epidemic turning point. However, the monthly sampling proportion $p$ (Fig. 3c) significantly overestimates the empirical ratio of sequenced to confirmed cases during peak transmission (mid-2014) and underestimates it in late 2015. Because `bdsky` assumes a single panmictic population, unmodeled spatial structure across Guinea, Liberia, and Sierra Leone violates panmixia and biases skyline demographic/sampling parameters—a classic case where structured models (`bdmm` or `MASCOT`) introduced in the very next section would be more appropriate.

* **Multispecies coalescent (`StarBEAST 2`, `STACEY`) and isolation-with-migration (`AIM`) models resolve species trees and inter-specific gene flow while avoiding concatenation bias (Sections "Multispecies coalescent models" & "Reticulate evolution", Figs. 4–5): [Well Supported].**  
  The theoretical exposition of the $2N_e$ speciation-time overestimation and anomaly-zone inconsistency under concatenation is rigorous, and coordinated MCMC operators plus analytical integration of population sizes yield documented 2–10$\times$ locus-scaling gains. In the empirical `AIM` analysis of 100 orthologous nuclear genes from five *Neolamprologus* Princess cichlid species (Fig. 5), the inferred introgression pathways (Bayes Factor $>10$) corroborate prior genomic studies, though fixing the root age to 9.2 Mya without variance and relying on a fixed exponential(0.05) rate-scaler prior could influence exact Bayes factor magnitudes.

* **Posterior predictive simulations in `TreeModelAdequacy` distinguish stochastic from deterministic phylodynamic SIR models on 2009 H1N1 influenza (Section "Model selection and model adequacy", Fig. 6): [Well Supported].**  
  Comparing empirical tree root height against MASTER posterior predictive distributions across 100 North American H1N1 genomes shows that the stochastic birth-death SIR model captures early-pandemic root height whereas the deterministic coalescent SIR model under-predicts root height variance.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT (Major Issues, Minor Issues, Concrete Recommendations)

#### Major Issues
1. **Unstructured Panmixia Violation in the Ebola `bdsky` Case Study (Fig. 3):** In Fig. 3c, the estimated monthly sampling proportion $p$ diverges sharply from the empirical sequence-to-case ratio during mid-2014 and late 2015. While the authors note that unrepresented transmission chains or isolated late-stage chains may contribute, they do not explicitly connect this artifact to applying an unstructured model (`bdsky`) to a multi-country dataset with heterogeneous surveillance and spatial clustering, despite showcasing `bdmm` and `MASCOT` in the same paper.
2. **Informal Third-Party Package Validation (Section "Validation, testing and quality management"):** The manuscript candidly states that quality and verification across BEAST 2 packages have been "informal" and advises end-users that "each package be evaluated independently by users, based on the published documentation." For a modular Bayesian platform where operators and likelihoods interact across packages, relying on end-user verification risks silent posterior miscalibration when combining sub-models.

#### Minor Issues
1. **Figure 6 Caption Duplication Error (Section "Model selection and model adequacy"):** The caption to Figure 6 states "The right column shows the trajectories of the reproductive number over time..." and then immediately states "The right column shows the posterior predictive distributions of the root height..."—the first instance should be "The left column".
2. **Broken DOI String in Reference 33:** Reference 33 (`MASCOT`) lists `doi: 0.1093/bioinformatics/bty406` (missing the leading `1` in `10.1093`).

#### Concrete Recommendations

#### 1. Explicitly Contrast Unstructured `bdsky` vs. Structured `bdmm`/`MASCOT` on the Ebola Dataset
* **WHY:** Demonstrating `bdsky` on a spatially structured 3-country Ebola dataset where the inferred sampling fraction $p$ is visibly biased (Fig. 3c) leaves a pedagogical gap regarding when users must switch from unstructured to structured phylodynamic models.
* **WHAT:** Expand the discussion of Fig. 3c to explicitly explain how unmodeled spatial/country structure inflates or deflates piecewise-constant sampling proportions, and note how `bdmm` or `MASCOT` (with country or region demes) addresses this bias.
* **HOW:** Add a short paragraph in Section "Tree models for structured populations" cross-referencing the late-2015 isolation bias in Fig. 3c as a concrete motivation for `MASCOT`/`bdmm`.

#### 2. Discuss Prior Sensitivity for Indicator Bayes Factors in the Cichlid `AIM` Analysis
* **WHY:** In Bayesian stochastic search variable selection for migration rates (Fig. 5), Bayes factors $>10$ for non-zero gene flow can be sensitive to the prior mean of the rate scaler (set to 0.05) and the fixed 9.2 Mya root height.
* **WHAT:** Note the prior distribution used on the number of active migration arrows (e.g., Poisson prior) and report whether the top supported gene-flow arrows in Fig. 5a–d remain invariant under a wider rate-scaler prior.
* **HOW:** State the exact indicator prior from the archived `AIM` XML file in the text accompanying Fig. 5.

#### 3. Outline a Concrete Automated Calibration Protocol for Package Repositories
* **WHY:** Because BEAST 2.5 already includes `MASTER` and sequence simulators, simulation-based calibration (SBC / well-calibrated Bayesian validation where parameters are drawn from the prior, data simulated, and 95% HPD coverage verified to be $\approx 95\%$) can be standardized across the CBAN package repository.
* **WHAT:** Strengthen Section "Validation, testing and quality management" by outlining a standardized well-calibrated simulation test harness that third-party packages must pass to be listed as verified in the Package Manager.
* **HOW:** Reference the well-calibrated simulation protocol described in Section "New simulation tools" as the formal benchmark standard being deployed for CBAN package acceptance.

#### 4. Technical and Editorial Cleanup
* **WHY:** Fixing caption and bibliography typos improves clarity.
* **WHAT & HOW:**
  1. In the Fig. 6 caption (line 22 of chunk 2), change the first occurrence of `The right column shows the trajectories of the reproductive number` to `The left column shows the trajectories of the reproductive number`.
  2. In Reference 33 (line 148 of chunk 2), change `doi: 0.1093/bioinformatics/bty406` to `doi: 10.1093/bioinformatics/bty406`.
