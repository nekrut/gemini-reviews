# Review of ANON_18

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **7.8 / 10.0** (Strong / Sound) | **Scientific Core Score:** **6.1 / 8.0**  
**Overall Score:** 7.8 / 10.0  
* **Score Breakdown:** Rigor: 2.5/3.5 | Claims: 2.0/2.5 | Biology: 1.6/2.0 | Reproducibility: 1.7/2.0  
**Score Breakdown:** Methodological Rigor: 2.5/3.5 | Claim-Evidence Alignment: 2.0/2.5 | Biological Plausibility: 1.6/2.0 | Reproducibility: 1.7/2.0  
**Verdict:** Strong / Sound

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT (Executive Summary)

This application note summarizes functional, algorithmic, and software engineering extensions added to the maximum-likelihood phylogenetic inference package RAxML since its 2006 release. The updates span four bootstrap/branch support schemes (standard non-parametric bootstrap, rapid bootstrap, SH-like support, RELL bootstrap, and automated bootstopping), expanded data types (binary, multi-state morphological, RNA secondary structure) with Lewis ascertainment bias correction, rate-dependent protein substitution models (LG4M, LG4X, GTR, automated model selection, and ML base frequency estimation), coarse- and fine-grained parallelization (PThreads, MPI, hybrid), tree post-analysis operations (Robinson–Foulds distances, consensus trees, rogue taxon identification, Internode/Tree Certainty, and large-tree plausibility checking), short-read Evolutionary Placement Algorithm (EPA) and sliding-window phylogenetic signal scanning, x86 vector intrinsics (SSE3, AVX, AVX2), and missing-data memory footprint reduction. Source code is released under the GNU GPL alongside a 50-page user manual.

As a concise software update note, the manuscript documents a mature, widely used, open-source computational tool whose core algorithms have largely been validated in prior peer-reviewed publications. Its primary limitations lie in the lack of empirical validation or benchmarking for the newly introduced or unpublished features mentioned in the note—specifically the unpublished sliding-window NGS signal algorithm (Section 2.5), the RELL bootstrap implementation (Section 2.1), and the quartet calculation routines (Section 2.8)—as well as an under-specified vectorization benchmark on a single DNA alignment of unstated dimensions (Section 2.6). These issues can be resolved through targeted benchmark reporting and documentation updates without new methodological development.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT (Detailed Rubric Evaluation)

* **SIMD vector intrinsics (SSE3, AVX, AVX2) substantially accelerate likelihood and parsimony calculations (Section 2.6): [Moderately Supported].**  
  The author reports wall-clock runtimes decreasing from 111.5 s (unvectorized) to 84.4 s (SSE3, 24.3% reduction) and 66.22 s (AVX, 40.6% reduction) on a single-gene DNA alignment under GTR+$\Gamma$ on an Intel i7-2620M processor at 2.70 GHz. However, the dimensions of this test alignment (number of taxa $N$ and site patterns $m$) are not reported, multi-gene/protein vectorization scaling is omitted, and the hardware specified (Intel Core i7-2620M, a Sandy Bridge microarchitecture processor) does not support the AVX2/FMA instruction set, leaving unclear what hardware was used to evaluate the claimed $<5\%$ AVX-to-AVX2 runtime difference.

* **Expanded substitution models and ascertainment bias corrections improve phylogenetic modeling across diverse data types (Section 2.2): [Well Supported].**  
  Integration of Lewis (2001) ascertainment bias correction for all-variable morphological and SNP matrices and Le et al. (2012) distribution-free/gamma rate-dependent protein mixture matrices (LG4M, LG4X) directly implements established, peer-reviewed likelihood formulations appropriate for heterogeneous sequence data.

* **Tree post-analysis and short-read placement tools scale to tens of thousands of taxa (Sections 2.4–2.5): [Moderately Supported].**  
  The Evolutionary Placement Algorithm (EPA), rogue taxon detection, consensus tree building, Internode/Tree Certainty (IC/TC), and large-tree plausibility checker are grounded in cited methodological papers (Berger et al. 2011; Pattengale et al. 2011; Salichos and Rokas 2013; Dao et al. 2013). By contrast, the sliding-window algorithm in Section 2.5 for identifying 16S/gene regions with stable phylogenetic signal is explicitly noted as "(unpublished)" and is presented without mathematical definition, window-size parameterization, or validation benchmarks.

* **Missing-data-aware data structures reduce memory footprints proportionally to alignment sparsity (Section 2.7): [Well Supported].**  
  The gappy-alignment memory optimization relies on the published data structures of Izquierdo-Carrasco et al. (2011), omitting conditional likelihood vectors and ancestral probability pointers for subtrees composed entirely of missing data across partitions.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT (Major Issues, Minor Issues, Concrete Recommendations)

#### Major Issues
1. **Uncharacterized Benchmark Alignment and Hardware Mismatch in Section 2.6:** The single timing experiment in Section 2.6 omits the number of sequences, alignment length, and distinct site patterns of the DNA test dataset, and cites an Intel i7-2620M CPU (which lacks AVX2/FMA support) alongside a claim about AVX vs. AVX2 performance.
2. **Unpublished Sliding-Window Algorithm Lacks Specification (Section 2.5):** The sliding-window method for selecting informative amplicon regions is cited as unpublished with no description of the objective metric (e.g., topological Robinson–Foulds stability vs. likelihood weight) or validation.

#### Minor Issues
1. **Newly Implemented RELL and ML Base Frequency Options Lack Validation Numbers (Sections 2.1–2.2):** While RELL (Minh et al. 2013) is cited, no comparison of RAxML's RELL support values or runtimes against standard rapid bootstrap (RBS) is provided.
2. **Typographical Error in References (Section References):** In the Dao et al. (2013) citation, "phyolgenies" is misspelled.

#### Concrete Recommendations

#### 1. Specify Dataset Dimensions and AVX2 Hardware in Vector Intrinsics Benchmark
* **WHY:** Reporting wall-clock runtimes without alignment dimensions ($N$ taxa, $L$ sites, $m$ distinct patterns) or the exact Haswell/later CPU used for AVX2 prevents independent reproduction of the vectorization speedup claims.
* **WHAT:** Add the taxon count, site count, pattern count, and exact command-line flags for the Section 2.6 DNA alignment, and specify the AVX2-capable processor used to measure the $<5\%$ AVX2/FMA gain.
* **HOW:** Report a compact summary table comparing Unvectorized, SSE3, AVX, and AVX2 runtimes for both a DNA ($\Gamma$) and a protein (LG+$\Gamma$ or LG4X) alignment on an AVX2-capable CPU, and deposit the test alignments in the Supplementary Data or GitHub repository.

#### 2. Document the Mathematical Metric for the Sliding-Window NGS Approach
* **WHY:** Introducing an unpublished algorithm in a software note without defining what statistic it computes leaves users unable to evaluate its statistical validity.
* **WHAT:** Explicitly state the sliding-window input parameters (window size, stride) and the output metric used to quantify "strong and stable phylogenetic signal" in Section 2.5 or Supplementary Material.
* **HOW:** Add a 3–4 sentence mathematical description (or supplementary section) detailing how sliding-window sub-alignments are scored against a reference topology and include the corresponding RAxML command-line flag.

#### 3. Provide Concordance and Runtime Metrics for the RELL Bootstrap Implementation
* **WHY:** Minh et al. (2013) coupled RELL with IQ-TREE's candidate tree sampling (UFBoot); implementing RELL inside RAxML's search heuristic may yield different support calibration depending on how candidate trees are collected.
* **WHAT:** Clarify how candidate trees are sampled during the RAxML ML search for RELL evaluation and report the correlation of branch supports with standard rapid bootstrap (`-f a`).
* **HOW:** Run RAxML RELL and rapid bootstrap on the benchmark DNA alignment from Section 2.6 and report the runtime ratio and Pearson/Spearman correlation of bipartition support values.

#### 4. Technical and Editorial Cleanup
* **WHY:** Minor bibliographic and URL formatting issues affect archival clarity.
* **WHAT & HOW:** Correct "phyolgenies" to "phylogenies" in the Dao et al. (2013) reference entry (line 101), and archive a static copy of the 50-page manual and tutorial in the Supplementary Data in addition to the external lab URLs.
