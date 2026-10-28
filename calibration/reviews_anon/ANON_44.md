# Review of ANON_44

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **8.1 / 10.0** (Strong / Sound)  
* **Score Breakdown:** Rigor: 2.5/3.5 | Claims: 1.9/2.5 | Biology: 1.8/2.0 | Reproducibility: 1.9/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript announces version 2.5 of HyPhy (HYpothesis testing using PHYlogenies), an open-source C++14 software package and domain-specific scripting environment (HyPhy Batch Language, HBL) for maximum-likelihood and Bayesian evolutionary modeling of molecular sequence alignments. The v2.5 release introduces a re-engineered computational core utilizing SIMD vectorization, OpenMP multiprocessing, and MPI distributed parallelism; non-interactive command-line keyword execution and Bioconda/Homebrew packaging for pipeline integration; standardized Markdown progress reporting and machine-readable JSON output coupled with the `hyphy-vision` JavaScript visualization library; and continuous integration testing featuring $>90\%$ HBL function unit test coverage and cross-package likelihood verification (`testiphy`). Source code, documentation, test suites, and web interfaces (Datamonkey) are publicly available.

HyPhy 2.5 represents a substantial software engineering upgrade that modernizes a widely used molecular evolution platform for reproducible command-line workflows and automated quality assurance. The primary limitation of the manuscript is the complete absence of empirical benchmarks to substantiate its performance and scalability claims: despite dedicating a section to "Optimized for Larger Data Sets," the paper provides no runtime tables, scaling curves, memory profiles, or numerical concordance comparisons against prior HyPhy versions (e.g., v2.2) or external likelihood engines. Adding a compact benchmark suite quantifying wall-clock speedups across core selection analyses (e.g., MEME, BUSTED, aBSREL, FUBAR) and verifying statistical concordance with earlier releases would directly align the empirical evidence with the manuscript's claims.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **HyPhy 2.5 modernizes CLI usability, package distribution, output standardization, and continuous integration testing: [Well Supported].**  
  The implementation of non-interactive keyword CLI arguments, relative path resolution, Bioconda/Homebrew distribution, standardized JSON output schemas paired with `hyphy-vision`, $>90\%$ HBL unit test coverage, and automated cross-software likelihood checks against IQ-TREE, RAxML, and MrBayes via `testiphy` are concrete, verifiable software engineering improvements.

* **Core numerical routines are optimized via SIMD, OpenMP, and MPI to enable analysis of large-scale alignments containing thousands of sequences: [Moderately Supported].**  
  While the codebase implements SIMD, OpenMP, and MPI parallelization alongside variational/grid approximations (such as FUBAR), the manuscript presents zero quantitative benchmarks demonstrating runtime speedups over previous HyPhy releases or defining the practical alignment size limits ($N$ sequences $\times$ $L$ codons) for computationally intensive branch-site and site-level random-effects models (e.g., BUSTED, MEME, aBSREL, RELAX) versus grid-based approximations (FUBAR).

* **Popular analyses implemented in HyPhy do not significantly benefit from GPU acceleration compared with tuned multicore CPU optimizations: [Fragile].**  
  In the "Optimized for Larger Data Sets" section, the authors state that "the majority of popular analyses implemented in HyPhy do not significantly benefit from GPU acceleration compared with tuned multicore CPU optimizations (in our hands at least, also see Izquierdo-Carrasco et al. 2013)." No experimental timings on modern GPU architectures or BEAGLE v3 codon-model kernels are presented to support this claim, and citing a 2013 nucleotide-level study does not establish CPU vs. GPU performance for 61-state codon transition probability exponentiation and pruning in 2019–2020.

* **The re-engineered computational core and standard libraries maintain backward compatibility and numerical consistency with previous HyPhy releases: [Moderately Supported].**  
  Although `testiphy` validates base likelihood evaluations against external phylogenetic packages, the manuscript does not report regression benchmarks comparing parameter estimates ($\omega$ distributions, branch lengths) and hypothesis test $p$-values from HyPhy 2.5 against HyPhy 2.2 across the standard suite of codon selection models where optimization heuristics and convergence criteria were updated.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Add a Quantitative Runtime and Scalability Benchmark Table Across Core Analyses
* **WHY:** Claiming that HyPhy 2.5 is "optimized extensively to enable analysis of modern large-scale molecular data sets" without providing any empirical runtime or memory measurements leaves readers unable to assess the performance gains of the v2.5 rewrite or the practical scaling limits of each method.
* **WHAT:** Include a benchmark table or figure comparing HyPhy 2.5 against the previous major release (e.g., HyPhy 2.2) across representative empirical alignments ranging from $N=50$ to $N=2,000$ sequences.
* **HOW:** Run the flagship stock analyses (`BUSTED`, `MEME`, `aBSREL`, `RELAX`, `FEL`, and `FUBAR`) on 3–4 standard alignments of increasing size on a specified multicore CPU node (reporting 1, 4, and 16 OpenMP threads), and tabulate wall-clock runtime, peak RAM usage, and relative speedup factor.

#### 2. Validate Statistical Concordance Between HyPhy 2.5 and Prior Releases
* **WHY:** Re-engineering the C++14 optimization core and modifying runtime convergence criteria can alter maximum-likelihood trajectories on multi-modal codon model surfaces, potentially changing biological inferences relative to earlier versions.
* **WHAT:** Summarize the numerical agreement of log-likelihoods, parameter estimates, and selection test results between HyPhy 2.5 and HyPhy 2.2 on a reference validation set.
* **HOW:** Using the method test suite already referenced in the "Software Engineering" section, report the distribution of log-likelihood differences ($\Delta \ln L$) and the concordance of positively selected sites/branches (at $p \le 0.05$ or posterior probability $\ge 0.90$) between HyPhy 2.5 and v2.2.

#### 3. Clarify Method-Specific Scaling Regimes and Temper Unbenchmarked GPU Claims
* **WHY:** Readers may infer from Line 36 ("alignments containing thousands of sequences") that all HyPhy selection analyses scale to thousands of taxa, whereas full maximum-likelihood branch-site models (`aBSREL`, `MEME`, `RELAX`) have much steeper computational scaling with $N$ than grid/variational methods (`FUBAR`) or counting methods (`SLAC`). Similarly, the claim that GPU acceleration offers no significant benefit for codon models is unsupported by data in the manuscript.
* **WHAT:** Explicitly distinguish the scaling regimes of different stock analyses and qualify the GPU statement.
* **HOW:** Add a summary table under "Analyses and Models Supported" listing each stock method, its biological scope (gene-wide, branch, site, branch-site, coevolution, recombination), and its recommended maximum alignment size ($N$ taxa $\times$ $L$ sites) for routine desktop/Datamonkey execution; rephrase the GPU sentence to note that GPU support is omitted in v2.5 pending benchmarking of modern 61-state codon kernels in libraries such as BEAGLE v3.

#### 4. Technical and Editorial Cleanup
* **WHY:** Minor grammatical typos detract from the presentation.
* **WHAT & HOW:**
  * In "Optimized for Larger Data Sets" (Line 36): Fix the missing preposition in *"and refinements open-source libraries supporting gpGPUs"* $\rightarrow$ *"and refinements in open-source libraries supporting GPGPUs"*, and change *"100$\times$ fold speedup"* $\rightarrow$ *"100-fold speedup"*.
  * In "Discussion" (Line 89): Fix the spelling of *"previously developed analyzes"* $\rightarrow$ *"previously developed analyses"*.
