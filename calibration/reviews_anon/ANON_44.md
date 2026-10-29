# Review of ANON_44

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **8.6 / 10.0** (Strong / Sound) | **Scientific Core Score:** **6.8 / 8.0**  
**Overall Score:** 8.6 / 10.0  
* **Score Breakdown:** Rigor: 2.9/3.5 | Claims: 2.2/2.5 | Biology: 1.7/2.0 | Reproducibility: 1.8/2.0  
**Score Breakdown:** Methodological Rigor: 2.9/3.5 | Claim-Evidence Alignment: 2.2/2.5 | Biological Plausibility: 1.7/2.0 | Reproducibility: 1.8/2.0  
**Verdict:** Strong / Sound

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT (Executive Summary)

This manuscript presents `UFBoot2`, an accelerated and bias-corrected version of the ultrafast bootstrap approximation (`UFBoot`) implemented in IQ-TREE v1.6. The authors address three primary challenges in maximum-likelihood (ML) phylogenetic branch support estimation: (1) computational speed, achieved via RAxML-style reversible root-pulley likelihood pruning and SIMD (SSE/AVX) vectorization across site pairs/quartets, yielding a $2.4\times$ median speedup over UFBoot v0.9.6, $778\times$ over standard nonparametric bootstrap (`SBS`), and $8.4\times$ over RAxML rapid bootstrap (`RBS`) across 70 DNA and 45 protein TreeBASE alignments; (2) false-positive branch support on unresolved polytomies, addressed by randomly tie-breaking among candidate trees within $\varepsilon_{\text{boot}} = 0.5$ RELL log-likelihood units of the best score (validated on 100 4-taxon star-tree simulations); and (3) overestimation of branch supports under severe substitution model violations, resolved by `UFBoot2 + NNI` (`-bnni`), which applies hill-climbing nearest-neighbor interchange (NNI) optimization directly on each bootstrap alignment starting from the best RELL tree (validated across 5,690 simulated PANDIT DNA alignments, Fig. 1). Finally, the authors implement partition-aware resampling schemes (`MSA-site`, `gene`, and `gene-site`, `-bsam`) for phylogenomic supermatrices, demonstrated on a 21-species, 225-gene metazoan dataset (Fig. 2) and 14 additional empirical matrices.

`UFBoot2` and `UFBoot2 + NNI` provide a practical, well-engineered advance that substantially mitigates the two principal failure modes of RELL-based bootstrap approximations while retaining a $424\times\text{--}778\times$ speedup over standard bootstrapping. The primary methodological limitations are: (1) the polytomy tie-breaking tolerance $\varepsilon_{\text{boot}} = 0.5$ is fixed as an absolute constant without analyzing how RELL log-likelihood variance scales with alignment length $L$ or taxon count $N$ beyond a 4-taxon star tree, (2) RAxML rapid bootstrap (`RBS`) is omitted from the model-violation benchmark (Fig. 1B) on the grounds that RAxML only implements GTR+$\Gamma$, whereas simulating under a more complex model (e.g., codon or site-heterogeneous mixture models) and inferring under GTR+$\Gamma$ would have permitted a symmetric comparison, and (3) the comparison of resampling strategies across 14 empirical phylogenomic datasets is cited as "(data not shown)" rather than tabulated in the supplement. All three issues can be resolved through straightforward supplementary additions and text clarifications.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT (Detailed Rubric Evaluation)

* **Reversible root-pulley pruning and SIMD vectorization accelerate `UFBoot2` to $778\times$ (median) faster than `SBS` and $8.4\times$ faster than RAxML `RBS` (Section "Accelerating UFBoot", Supplementary Figs. S1–S3): [Well Supported].**  
  Across 115 empirical TreeBASE alignments (70 DNA, 45 protein; archived at Zenodo DOI `10.5281/zenodo.854445`), `UFBoot2` achieves a $2.4\times$ median speedup (max $77.3\times$) over `UFBoot` v0.9.6 and $778\times$ (range $200\text{--}1,848\times$) over `SBS`, while `UFBoot2 + NNI` remains $424\times$ faster than `SBS` and $5.0\times$ faster than `RBS`.

* **Optimizing RELL bootstrap trees via hill-climbing NNI (`UFBoot2 + NNI`, `-bnni`) eliminates the severe overestimation of branch support under model misspecification (Section "Reducing the Impact of Model Violations", Fig. 1): [Well Supported].**  
  Across 5,690 simulated PANDIT DNA alignments, standard `UFBoot2` is well calibrated under the true substitution model (Fig. 1A, lying near the $y = x$ diagonal) but substantially overestimates branch probability under severe model violations (Fig. 1B, curve well below the diagonal because suboptimal candidate topologies from the misspecified original tree search constrain the RELL pool). Adding direct NNI refinement on each bootstrap replicate (`UFBoot2 + NNI`) restores calibration in Fig. 1B to slightly conservative levels closely tracking `SBS` at only a $2\times$ runtime cost over `UFBoot2`.

* **Randomized RELL tie-breaking within $\varepsilon_{\text{boot}} = 0.5$ prevents false-positive resolution of polytomies (Section "Correction for Polytomies"): [Moderately Supported].**  
  On 100 simulated 4-taxon star-tree alignments ($L = 15,000$ bp, terminal branches 0.05 under JC), selecting uniformly among encountered trees within $\varepsilon_{\text{boot}} = 0.5$ log-likelihood units of the maximum RELL score caps internal branch support at $\le 88\%$ (zero false positives at the $\ge 95\%$ threshold), matching Simmons & Norton (2014). However, a 4-taxon star tree has only three possible bifurcating topologies, all of which are guaranteed to be visited during the search; in larger trees ($N \ge 50$) with internal polytomies or multiple short internodes, whether the candidate tree pool uniformly samples all $2k-3$ resolutions of a multifurcation—and whether a fixed $\varepsilon_{\text{boot}} = 0.5$ threshold remains optimal across varying alignment lengths $L$—is not tested.

* **Site, gene, and gene-site resampling strategies (`-bsam`) can yield discordant branch supports on empirical phylogenomic matrices (Section "Resampling Strategies for Phylogenomic Data", Fig. 2): [Moderately Supported].**  
  On the 21-species, 225-gene metazoan alignment (171,077 amino acid sites; Salichos & Rokas 2013), `MSA-site` and `gene` resampling yield $>95\%$ support along backbone internodes whereas `gene-site` resampling yields 80% support (Fig. 2). However, the broader claim across 14 additional empirical phylogenomic datasets—that some branches show $\le 10\%$ support under one scheme and $\ge 95\%$ under the other two with "no tendency toward systematically lower supports"—is presented as "(data not shown)", preventing verification of the underlying distributions.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT (Major Issues, Minor Issues, Concrete Recommendations)

#### Major Issues
1. **Unreported Empirical Results for the 14 Phylogenomic Datasets ("data not shown", Line 61):** In Section "Resampling Strategies for Phylogenomic Data", the authors analyze 14 published phylogenomic datasets and report striking discrepancies ($\le 10\%$ vs. $\ge 95\%$ support across `MSA-site`, `gene`, and `gene-site` resampling) as "(data not shown)". Since the runs have already been executed, withholding the summary statistics and branch support distributions from the Supplementary Material violates data completeness standards.
2. **Narrow Validation of Polytomy Correction ($\varepsilon_{\text{boot}} = 0.5$) on a 4-Taxon Tree Only (Section "Correction for Polytomies"):** In a 4-taxon tree, there is only 1 internal branch and 3 possible topologies, so visiting all resolutions is trivial. On larger trees ($N = 20\text{--}100$) with one or more zero-length internal branches, `UFBoot2` only evaluates trees encountered during the original MSA search; if the search heuristic does not visit all three NNI resolutions around a polytomy equally often, random selection within $\varepsilon_{\text{boot}} = 0.5$ could still be biased unless combined with NNI exploration (`-bnni`).

#### Minor Issues
1. **Omission of `RBS` from Figure 1B:** The authors state that `RBS` is omitted from Figure 1B "because RAxML does not support simpler models" (i.e., when PANDIT data were simulated under GTR+$\Gamma$ and inferred under JC). While true for JC, model violation in RAxML can be evaluated either by using `RAxML-NG` / `ExaML` or by simulating under a codon/mixture model and inferring under unpartitioned GTR+$\Gamma$ (or at minimum noting how `UFBoot2 + NNI` compares to `SBS` on the subset of models supported by both).

#### Concrete Recommendations

#### 1. Replace "(data not shown)" with a Supplementary Table Summarizing the 14 Phylogenomic Datasets
* **WHY:** Reporting extreme support discrepancies ($\le 10\%$ vs. $\ge 95\%$) across 14 empirical datasets as "data not shown" deprives readers of the empirical evidence supporting the section's conclusions.
* **WHAT:** Add a Supplementary Table (e.g., Table S2) listing all 15 empirical phylogenomic datasets (number of taxa, number of genes, total sites, mean/median branch support under `MSA-site`, `gene`, and `gene-site` resampling, and number of branches with $|\Delta \text{support}| \ge 20\%$ or discordant $\ge 95\%$ vs. $\le 10\%$ calls).
* **HOW:** Tabulate the existing `UFBoot2` log outputs from the 14 datasets cited on line 61 and include them in the Supplementary Material and the Zenodo archive (`10.5281/zenodo.854445`).

#### 2. Evaluate Polytomy Calibration on Embedded Multifurcations in Larger Trees and Under `-bnni`
* **WHY:** A 4-taxon star tree cannot test whether IQ-TREE's candidate tree pool explores all resolutions of an internal polytomy embedded within a larger tree, nor how $\varepsilon_{\text{boot}} = 0.5$ interacts with `UFBoot2 + NNI`.
* **WHAT:** Test `UFBoot2` and `UFBoot2 + NNI` on a simulated tree with $N \ge 20$ taxa containing internal zero-length branches (or on the PANDIT trees with near-zero internal branches) and report the false-positive rate (support $\ge 95\%$) on the zero-length branches.
* **HOW:** Collapse 2–3 internal branches to length 0.0 on a 20-taxon topology, simulate 100 alignments in `Seq-Gen` at $L = 1,000$ and $L = 15,000$, and verify that both `UFBoot2` and `UFBoot2 + NNI` maintain support $< 95\%$ on the collapsed branches across alignment lengths.

#### 3. Clarify the Theoretical Variance of `gene-site` Resampling vs. `MSA-site` and `gene` Resampling
* **WHY:** On line 61, the authors note that `gene-site` resampling yields lower support (80% vs. $>95\%$) on the metazoan tree (Fig. 2) but state there is no systematic tendency across datasets. Statistically, two-stage resampling (resampling $G$ genes with replacement, AND resampling sites with replacement within each sampled gene) doubles the bootstrap variance relative to one-stage resampling because it compounds inter-gene variance with intra-gene multinomial site variance.
* **WHAT:** Add a brief statistical explanation in Section "Resampling Strategies for Phylogenomic Data" noting that `gene-site` resampling injects both gene-level and site-level resampling variance simultaneously, whereas `gene` resampling alone is the standard non-parametric cluster bootstrap when genes are the independent sampling units.
* **HOW:** Add 2–3 sentences discussing the two-stage cluster bootstrap variance properties of `-bsam GENESITE` vs. `-bsam GENE` to guide users on which flag is statistically appropriate when testing species trees against gene-tree heterogeneity.
