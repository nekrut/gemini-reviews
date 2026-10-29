# Review of ANON_07

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **7.4 / 10.0** (Strong / Sound) | **Scientific Core Score:** **6.5 / 8.0**  
* **Score Breakdown:** Methodological Rigor: 2.7/3.5 | Claim-Evidence Alignment: 2.0/2.5 | Biological Plausibility: 1.8/2.0 | Reproducibility: 0.9/2.0  
* **Score Breakdown (Compact):** Rigor: 2.7/3.5 | Claims: 2.0/2.5 | Biology: 1.8/2.0 | Reproducibility: 0.9/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript investigates the relationship between nonadaptive molecular convergence and evolutionary divergence across 13 concatenated mitochondrial protein-coding genes from 629 tetrapod species (3,596 aligned amino acid sites) alongside biophysical and phenomenological sequence evolution simulations. Using Bayesian ancestral state reconstruction (PLEX under the mtMam+$\Gamma_5$ substitution model) on a fixed cytochrome oxidase 1 (CO1) tree topology, the authors compute the ratio of convergent ($C$) to divergent ($D$) double substitutions across non-sister, non-ancestral branch pairs separated by varying patristic distances. They observe that $C/D$ begins around $0.40$–$0.45$ at short patristic distances and decays to below $0.20$ at larger distances. Specifically—in terms of the primary analytical distinction—even when conditioning on branch pairs that share an identical ancestral amino acid at a site, $C/D$ declines over evolutionary distance (linear slope $99\%$ credible interval $[-0.109, -0.094]$), whereas time-homogeneous site-heterogeneous mixture models (such as CAT-60) predict an increasing $C/D$ with distance for identical-ancestor sites due to survivorship bias toward low-entropy sites. A thermodynamic Stokes–Fisher (SF) folding simulation model incorporating pairwise contact potentials (PDB `1QHW`) reproduces the empirical decline in $C/D$. No public repository, accession list for the 641 downloaded GenBank sequences, or simulation source code is provided (`[ACCESSION_REDACTED in scrubbed input]`).

The central theoretical insight—that spatial heterogeneity alone (e.g., CAT-60) predicts an upward slope in $C/D$ over time for identical-ancestor sites whereas epistatic/temporal constraint fluctuations predict the empirically observed downward slope—is a sharp and valuable contribution to molecular evolution. However, the empirical analysis is weakened by several methodological vulnerabilities: ancestral substitutions are inferred under a site- and time-homogeneous model (`mtMam`+$\Gamma_5$) on a single gene tree (`CO1`) that ignores topological discordance and strand-asymmetric compositional drift across the mitochondrial genome; display filtering uses a hard posterior threshold ($>90\%$) and divergent-count cutoffs ($D \ge 20$, $D \ge 7$, or $D \ge 10$) that introduce ratio-estimator truncation bias; and branch pairs on a shared phylogeny are treated as independent observations in linear regression without correcting for phylogenetic non-independence. These limitations can be resolved computationally through phylogenetic block-bootstrapping, ancestral reconstruction under site-heterogeneous models, and open archival of the alignment and simulation code.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Nonadaptive convergence ($C/D$) in vertebrate mitochondrial proteins declines steeply with patristic distance, including at sites with identical ancestral amino acids: [Moderately Supported].**  
  The decline in $C/D$ from $\sim 0.45$ to $<0.20$ for identical-ancestor sites (Figure 2A) is supported by integrating over posterior ancestral reconstructions in PLEX (Supplementary Figure S2). However, inferring ancestral states under a single global empirical matrix (`mtMam`) systematically biases ancestral reconstructions at constrained sites toward globally common residues at deeper nodes, and using a single `CO1` topology for all 13 concatenated mitochondrial proteins can create artifactual double substitutions on short branches wherever gene-tree discordance or alignment error occurs. Additionally, the $99\%$ credible interval for the slope ($[-0.109, -0.094]$) does not account for the severe statistical non-independence among the $\sim O(N^2)$ branch pairs that share internal evolutionary paths on the same tree.

* **Time-homogeneous site-heterogeneous models (CAT-60) cannot explain the decline in $C/D$ among sites sharing the same ancestral state, whereas epistatic Stokes–Fisher models capture this trend: [Well Supported].**  
  The mathematical demonstration in Figure 6A is sound: under a static site-specific amino acid profile (CAT-60), conditioning on the ancestral state remaining unchanged over patristic distance $d$ progressively enriches the surviving site pool for low-entropy (slowly evolving, highly constrained) sites, which forces $C/D$ upward over time. The empirical observation of the opposite trend provides direct qualitative evidence that site-specific amino acid propensities fluctuate over time.

* **Once ancestral amino acids at a site have diverged between two lineages, the site retains no detectable site-specific information about convergence probabilities beyond the identity of the ancestral amino acids: [Fragile].**  
  The authors base this claim on a permutation test (Supplementary Figure S4) that resamples descendant amino acids across all sites sharing the same ancestral amino acid, finding $C/D \approx 0.08$ matching Figure 2B. However, pooling across all 3,596 sites averages out local structural environments; the lack of difference in the global mean $C/D$ ratio does not prove that individual sites have lost site-specific biophysical constraints (an effective alphabet of $m = 13.4$ residues under a Jukes–Cantor approximation is an aggregate across heterogeneous sites, not proof of site-level panmixia).

* **Excessive molecular convergence at short evolutionary distances cannot be assumed to be adaptive under standard null models: [Well Supported].**  
  Both the empirical mitochondrial trajectories and the analytical model comparisons (Figures 4–6) demonstrate that standard homogeneous matrices (JC, WAG, Ziheng codon model) underestimate baseline nonadaptive convergence by 2- to 4-fold at short branch distances, invalidating naive parametric tests of adaptive convergence that rely on homogeneous exchangeability matrices.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Correct for Non-Independence of Branch Pairs and Ratio Truncation Bias
* **WHY:** In Figures 1–3, $C/D$ is plotted and regressed across all eligible branch pairs satisfying $D \ge 20$ (or $D \ge 7, 10$). Because $\binom{2N-2}{2}$ branch pairs on a tree of 629 taxa share internal branches and node reconstructions, treating branch pairs as independent inflates precision, while truncating on $D \ge D_{\min}$ biases the expectation $E[C/D \mid D \ge D_{\min}]$ downward as branch lengths or divergence times change.
* **WHAT:** Replace the truncated $C/D$ linear regression with a phylogenetic node-jackknife or non-overlapping clade comparison, and model $C$ directly using a binomial/Poisson generalized linear mixed model conditioned on $C+D$.
* **HOW:** Fit $\text{logit}(P(\text{Convergent} \mid \text{Double Substitution})) = \beta_0 + \beta_1 d_{ij} + u_i + u_j$, where $d_{ij}$ is patristic distance and $u_i, u_j$ are random effects for branches $i$ and $j$, without excluding pairs where $D < 20$. Compute confidence intervals via block-bootstrapping across the 13 mitochondrial genes or non-overlapping tetrapod subtrees.

#### 2. Test Sensitivity of Empirical Ancestral Reconstructions to Site-Heterogeneous Prior Models
* **WHY:** Ancestral states for the empirical data were inferred in PLEX using the site-homogeneous `mtMam`+$\Gamma_5$ model, which assumes identical equilibrium frequencies and exchangeabilities across all 3,596 sites. Misspecified homogeneous priors can induce systematic errors in ancestral state probabilities as a function of node depth.
* **WHAT:** Re-estimate ancestral states and posterior substitution mappings using a site-heterogeneous profile mixture model (e.g., CAT or empirical profile mixtures C20/C60).
* **HOW:** Run PhyloBayes (`pb` with `-cat -gtr` or `-catfix C60`) or IQ-TREE/PLEX equivalents on the concatenated mitochondrial alignment (or on the `CO1` alignment alone to eliminate topological mismatch between `CO1` and the other 12 genes) and verify that the downward slope of $C/D$ for identical-ancestor sites (Figure 2A) persists when ancestral states are reconstructed under site-specific equilibrium profiles.

#### 3. Fix Text-Figure Contradiction and Deposit Alignment and Simulation Code
* **WHY:** On line 36, the text states: *"The 99% credible region for the slope of a linear model fit to the data from figure 2B shows a clear decrease in C/D ratios with divergence (-0.109, -0.094; supplementary fig. S3)"*—referencing Figure 2B (different ancestral states, which the text says is *"approximately constant at 0.08"*) instead of Figure 2A (identical ancestral states). Furthermore, the list of 641 GenBank accessions, the curated 629-taxon alignment, and the Stokes–Fisher C/C++ simulation code are not deposited.
* **WHAT & HOW:** Correct *"figure 2B"* to *"figure 2A"* on line 36; verify whether Supplementary Figure S3A cited at the end of line 36 should be Supplementary Figure S5A; and deposit the 629-taxon concatenated alignment, the `CO1` MrBayes tree, and the Stokes–Fisher simulation scripts in Dryad or Zenodo.
