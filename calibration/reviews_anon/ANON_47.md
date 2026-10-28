# Review of ANON_47

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **8.3 / 10.0** (Strong / Sound)  
* **Score Breakdown:** Rigor: 2.8/3.5 | Claims: 2.0/2.5 | Biology: 1.8/2.0 | Reproducibility: 1.7/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript presents version 2 of IQ-TREE, a maximum-likelihood phylogenetic inference package. Key additions over IQ-TREE 1 include support for non-time-reversible substitution models (99 Lie Markov DNA models, the general unrestricted DNA model UNREST, and a general 20-state non-reversible amino acid model NONREV) using complex eigendecomposition with a scaling-and-squaring numerical fallback and local root search (`--root-dist`); customizable profile mixture models (`MIX{...}`); terrace-aware partitioned search via `terraphast`; parallelized single-locus tree inference (`-S`); fast quartet likelihood mapping; constrained (`-g`) and fast (`-fast`) heuristic tree searches; parallelized branch (SH-aLRT, aLRT, aBayes) and topology (SH, AU, ELW) tests; and half-memory (`-mem 0.5`) and numerical underflow protection (`-safe`) modes. The authors benchmark these features on two empirical phylogenomic alignments (a DNA dataset from Fong et al. 2012 and an amino acid dataset from Whelan et al. 2017).

IQ-TREE 2 delivers substantial algorithmic and engineering advances—particularly its numerically stable implementation of non-reversible substitution matrices, terrace detection, and parallelized quartet mapping and branch support tests (achieving $>1,000$-fold speedups over PhyML for SH-aLRT and $>250$-fold over TREE-PUZZLE for quartet mapping). However, the empirical evaluations in the manuscript focus almost exclusively on wall-clock runtime while omitting critical statistical and topological accuracy checks: (1) for the newly introduced non-reversible models (especially the 379-parameter amino acid `NONREV` model and the `--root-dist 2` heuristic), no evidence is provided showing whether the inferred root positions are biologically accurate or statistically identifiable on the two benchmark datasets; (2) the `-fast` search benchmark reports runtime against FastTree2 without reporting log-likelihoods or topological accuracy; and (3) the dimensions of the two benchmark datasets and hardware specifications are omitted from the main text. Adding topological/rooting validation metrics and complete benchmark metadata will substantially strengthen the paper.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **IQ-TREE 2 achieves orders-of-magnitude speedups in quartet likelihood mapping, SH-aLRT branch testing, and AU topology testing: [Well Supported].**  
  Direct benchmarks on the DNA and amino acid datasets demonstrate a $>280\times$ single-core speedup over TREE-PUZZLE for quartet likelihood mapping, a $1,300\times$ to $>2,000\times$ speedup over PhyML 3.3 for SH-aLRT branch support, and a $2.8\times$ to $3.9\times$ 4-core speedup over CONSEL for the AU topology test while computing site log-likelihoods internally.

* **Memory-saving mode (`-mem 0.5`) halves RAM consumption with only a 9%–21% runtime penalty: [Well Supported].**  
  Empirical timings on the DNA dataset (27 min vs. 32.8 min, +21%) and AA dataset (5.7 h vs. 6.2 h, +9%) directly support the practical utility of the memory-saving implementation for large mixture and partitioned models.

* **IQ-TREE 2 enables accurate rooted tree inference under non-reversible DNA (UNREST, Lie Markov) and amino acid (NONREV) substitution models: [Moderately Supported].**  
  While the hybrid complex eigendecomposition / scaling-and-squaring matrix exponentiation and rooted pruning algorithm are mathematically sound, the manuscript reports only wall-clock runtimes (10.7 min for DNA UNREST; 5.8 h for protein NONREV) without evaluating whether the inferred root placements on the Fong et al. (2012) and Whelan et al. (2017) phylogenies match known outgroup roots. Furthermore, the unrestricted 20-state amino acid model (`NONREV`) estimates $20 \times 19 - 1 = 379$ free exchangeability parameters (plus state frequencies), raising unaddressed questions regarding parameter identifiability and overfitting on standard alignments, and the default root search (`--root-dist 2`) only tests branches within 2 steps of the current root.

* **The `-fast` tree search matches FastTree2 in speed while avoiding FastTree2's degraded topological accuracy: [Fragile].**  
  In "New Options for Tree Search," the authors report runtimes for default IQ-TREE 2, `iqtree -fast`, and FastTree2 on the DNA (27 min, 82 s, 85 s) and AA (5.7 h, 13.9 min, 4.3 min) datasets, and cite Zhou et al. (2018) to note that FastTree2 produces worse trees than standard IQ-TREE, RAxML, and PhyML. However, Zhou et al. (2018) evaluated standard IQ-TREE 1, not the new `-fast` mode in IQ-TREE 2. Because the manuscript does not report the log-likelihood scores or Robinson–Foulds distances of the trees produced by `iqtree -fast` versus FastTree2 and default IQ-TREE 2 on these two datasets, the accuracy of `-fast` remains unsubstantiated in the text.

* **IQ-TREE 2 `-S` exhibits higher parallel efficiency (101% on DNA, 97.6% on AA) than ParGenes and will perform similarly on very large datasets: [Overstated].**  
  First, reporting 101% parallel efficiency on the DNA dataset (18.6 min on 2 cores vs. 9.2 min on 4 cores) is an artifact of normalizing against a 2-core baseline rather than a 1-core baseline. Second, ParGenes v1.0.1 completed the exact same 4-core analyses in 5.98 min (vs. 9.2 min) on DNA and 0.81 h (vs. 1.05 h) on AA—making ParGenes 23%–35% faster in wall-clock time—and ParGenes supports multi-node MPI scheduling across hundreds of cluster cores for single-locus trees, whereas `-S` schedules across shared-memory CPU cores.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Report Rooting Accuracy, Model Fit (BIC/AICc), and `--root-dist` Sensitivity for Nonreversible Models
* **WHY:** Introducing the first general non-reversible amino acid model (`NONREV`, 379 free rate parameters) and UNREST rooting without showing whether they recover the biological root or improve penalized likelihood (BIC/AICc) leaves their empirical reliability unknown.
* **WHAT:** Report the log-likelihoods, BIC scores, and inferred root splits for `UNREST` (on the DNA dataset) and `NONREV` (on the AA dataset), and compare `--root-dist 2` (default) against an exhaustive root search (`--root-dist` set to tree diameter).
* **HOW:** Extract the log-likelihood, number of free parameters, and BIC from the `.iqtree` output files of the already-executed DNA `UNREST` and AA `NONREV` runs, check whether `--root-dist 2` finds the same maximum-likelihood root as an all-branch root search, and state whether the inferred root agrees with the canonical outgroup rooting of Fong et al. (2012) and Whelan et al. (2017).

#### 2. Include Log-Likelihoods and Topological Distances for the `-fast` Search Benchmark
* **WHY:** Comparing the runtime of `iqtree -fast` against FastTree2 without reporting the resulting tree likelihoods or topologies does not show whether `-fast` retains IQ-TREE's likelihood advantage over FastTree2.
* **WHAT:** Report the final log-likelihood ($\ln L$) evaluated under the exact same model and the Robinson–Foulds (RF) distance to the default IQ-TREE 2 tree for both `iqtree -fast` and `FastTree2`.
* **HOW:** Score the trees output by `iqtree -fast` and `FastTree2` on the DNA and AA datasets in IQ-TREE 2 (`-z` option) and add their $\Delta \ln L$ and RF distances to the "New Options for Tree Search" section.

#### 3. Standardize Parallel Efficiency Against a 1-Core Baseline and Specify Dataset/Hardware Metadata
* **WHY:** Computing parallel efficiency at 4 cores relative to 2 cores yields an unphysical 101% efficiency on the DNA dataset, and readers cannot interpret wall-clock timings without knowing the alignment dimensions (taxa $\times$ sites $\times$ loci) and CPU model.
* **WHAT:** Recompute parallel efficiency relative to 1 CPU core, temper the claim that `-S` will match ParGenes on massive cluster runs, and state the dimensions of `DNA-data` and `AA-data` and the benchmark CPU architecture.
* **HOW:** Add a single sentence at first mention of the benchmarks stating the number of taxa, total alignment length, number of loci, percentage of missing data, and CPU processor model for the Fong et al. (2012) DNA dataset and Whelan et al. (2017) AA dataset, and report 1-core runtimes for the `-S` single-locus benchmark to compute standard strong-scaling efficiency $E_k = T_1 / (k T_k)$.
