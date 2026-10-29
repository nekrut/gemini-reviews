# Review of ANON_25

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **7.5 / 10.0** (Strong / Sound) | **Scientific Core Score:** **5.9 / 8.0**  
**Overall Score:** 7.5 / 10.0  
* **Score Breakdown:** Rigor: 2.4/3.5 | Claims: 1.9/2.5 | Biology: 1.6/2.0 | Reproducibility: 1.6/2.0  
**Score Breakdown:** Methodological Rigor: 2.4/3.5 | Claim-Evidence Alignment: 1.9/2.5 | Biological Plausibility: 1.6/2.0 | Reproducibility: 1.6/2.0  
**Verdict:** Strong / Sound

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT (Executive Summary)

This software resource paper describes version 11 of the Molecular Evolutionary Genetics Analysis (MEGA11) suite for cross-platform GUI and command-line (`MEGA-CC`) evolutionary genomics. Methodological additions integrate four previously published algorithms into the MEGA workflow: (1) probability density calibration constraints (normal, lognormal, uniform, exponential) and analytical confidence intervals for `RelTime` relaxed-clock node dating, (2) rapid tip-dating via `RelTime with Dated Tips` (`RTDT`), (3) machine-learning detection of branch rate autocorrelation via `CorrTest`, and (4) Bayesian neutral evolutionary probabilities (`EP`) of alleles across multispecies alignments. Technical updates include dynamic grouping via spatiotemporal metadata tags, memory reduction in maximum-likelihood (ML) and parsimony analyses via identical site-configuration compression, and background multithreading of distance and GUI operations tested on an alignment of 68,000 genomes of 30,000 bp each. Native builds and source code are available at `www.megasoftware.net`.

MEGA11 provides an accessible, unified graphical and command-line interface that lowers the barrier to relaxed-clock dating and evolutionary conservation screening for a broad biological audience. However, the manuscript has three notable weaknesses: (1) compressing identical site patterns ($m/L$) in ML is a decades-old standard procedure in phylogenetics, and MEGA11's reported post-compression memory footprint (2.3 GB for 162 mammals $\times$ 11,010 sites) remains orders of magnitude higher than standard ML engines (`RAxML`, `IQ-TREE`, `PhyML`), (2) the claim that GUI and distance operations handle 68,000 genomes $\times$ 30,000 bases "rapidly" is presented without a single quantitative runtime or memory measurement, and (3) the assertion that alleles with $EP < 0.05$ are non-neutral/disease-associated is stated deterministically without addressing taxon-sampling sensitivity or intramolecular epistasis. These issues can be resolved by reporting quantitative runtime/memory benchmarks and tempering the biological interpretation of $EP$ and ML memory efficiency.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT (Detailed Rubric Evaluation)

* **`RelTime` with node calibration probability densities and `RTDT` tip-dating provide rapid divergence time and confidence interval estimation (Section "Expansion of Relaxed-Clock Dating Facilities", Figs. 1–3): [Well Supported].**  
  The implementation directly incorporates the variance propagation formulas of Tao et al. (2020) and the tip-dating estimator of Miura et al. (2018), accounting for rate heterogeneity across lineages, branch-length estimation variance (when sequence data are provided), and calibration density uncertainty. The authors appropriately note that supplying a pre-computed tree with branch lengths alone yields narrower confidence intervals because sequence-level branch-length estimation variance is omitted.

* **`CorrTest` accurately detects evolutionary rate autocorrelation across branches (Section "Detecting Autocorrelation of Evolutionary Rates"): [Moderately Supported].**  
  While the underlying machine-learning classifier (`CorrScore` and $P$-value) was validated in Tao et al. (2019), the manuscript does not mention that `CorrTest` was trained on specific tree topologies and rate regimes, or discuss its false-positive/false-negative behavior when branch lengths are estimated on short or highly gapped alignments.

* **Neutral Evolutionary Probabilities ($EP < 0.05$) identify non-neutral disease and adaptive variants from multispecies alignments (Section "Calculating Neutral Evolutionary Probabilities"): [Overstated].**  
  The text states categorically that "Alleles with $EP$ less than 0.05 are nonneutral, whereas evolutionary permissible (neutral) alleles show much higher EPs." In practice, phylogenetic $EP$ estimates depend heavily on the depth and balance of the input species alignment, assume site-independence (ignoring compensatory epistasis / background-dependent fitness shifts that frequently make human pathogenic variants benign in other mammals), and conflate deep purifying constraint with acute human pathogenicity.

* **Site-configuration compression and background threading enable memory-efficient ML and responsive analysis of very large datasets (Sections "Memory Efficient ML Analyses" & "Enhanced GUI for Exploring Large Data Sets"): [Moderately Supported].**  
  Deduplicating identical alignment columns reduces MEGA's internal memory from 870 MB to 209 MB on 229 birds (2,728 sites) and from 6.8 GB to 2.3 GB on 162 mammals (11,010 sites). While this is a substantial internal improvement over MEGA X, consuming 2.3 GB of RAM for 162 taxa $\times$ 11,010 sites (fewer than $1.1 \times 10^4$ patterns) is still extremely memory-heavy compared to standard phylogenetic software, which requires $<50$ MB for an alignment of that size. Moreover, for the 68,000-genome $\times$ 30,000-bp test set, no quantitative wall-clock times for file loading, pairwise distance calculation, or neighbor-joining tree inference are reported.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT (Major Issues, Minor Issues, Concrete Recommendations)

#### Major Issues
1. **Unquantified Performance on the 68,000-Genome Dataset (Section "Enhanced GUI for Exploring Large Data Sets"):** The authors state that they evaluated MEGA11 on a 68,000-genome $\times$ 30,000-base alignment (presumably SARS-CoV-2) and that "large input data files are read rapidly, and calculations of pairwise distance matrices, selection tests, and phylogeny construction for distance-based methods are performed in a background thread," without reporting any execution times, peak RAM usage, or hardware specifications.
2. **High Absolute ML Memory Footprint Despite Site-Pattern Compression (Section "Memory Efficient ML Analyses"):** Requiring 2.3 GB of RAM after pattern compression for a 162-taxon $\times$ 11,010-site alignment indicates that conditional likelihood vectors or tree structures are still being duplicated across search states or threads; presenting this without context or external baseline comparison overstates MEGA11's memory efficiency for genome-scale ML.

#### Minor Issues
1. **Deterministic Framing of $EP < 0.05$ Threshold (Section "Calculating Neutral Evolutionary Probabilities"):** Presenting $EP < 0.05$ as a hard boundary for non-neutrality without discussing alignment depth requirements or epistatic divergence can mislead users analyzing poorly sampled gene families.
2. **Default Outgroup and Focal Taxon Selection in Wizards:** The `EP wizard` automatically selects the first sequence in the alignment as the focal taxon, which is error-prone in batch `MEGA-CC` workflows if FASTA ordering varies across genes.

#### Concrete Recommendations

#### 1. Report Quantitative Runtimes and Memory Footprints for the 68,000-Genome Benchmark
* **WHY:** Claims of scalability to 68,000 genomes $\times$ 30,000 bp cannot be evaluated without wall-clock timings and memory metrics (especially since an $N \times N$ double-precision pairwise distance matrix for $N = 68,000$ requires $\approx 37$ GB of RAM).
* **WHAT:** Add a benchmark table or paragraph reporting the exact wall-clock time and peak RAM for (a) FASTA import, (b) pairwise distance calculation, and (c) Neighbor-Joining/RTDT timetree inference on subsets (e.g., $N = 5,000$, $10,000$, $68,000$) on a specified desktop machine.
* **HOW:** Log peak working-set memory and elapsed time in `MEGA11` on the 68,000-genome alignment and state the provenance of the test alignment.

#### 2. Contextualize ML Site-Pattern Memory Savings and Clarify Remaining Memory Overhead
* **WHY:** Informing users why a 162-taxon $\times$ 11,010-site alignment still requires 2.3 GB of RAM helps them anticipate hardware limits when scaling to larger phylogenomic matrices.
* **WHAT:** Report the exact number of distinct site configurations $m$ for the Claramunt & Cracraft (2015) bird dataset ($L = 2,728$) and Meredith et al. (2011) mammal dataset ($L = 11,010$), and explain what data structures account for the 2.3 GB footprint.
* **HOW:** Add $m$ and the empirical compression ratio $m/L$ to the text in Section "Memory Efficient ML Analyses".

#### 3. Add Methodological Caveats on Taxon Sampling and Epistasis for $EP$ Estimates
* **WHY:** Neutral evolutionary probabilities inferred from a single site column across species assume site-independent substitution rates and sufficient evolutionary depth; shallow alignments yield high neutral probabilities by default, whereas compensatory substitutions at interacting sites can cause benign human alleles to appear forbidden in distant lineages.
* **WHAT:** Temper the statement "Alleles with $EP$ less than 0.05 are nonneutral" and note the minimum recommended tree depth/taxon representation for reliable $EP$ inference.
* **HOW:** Revise the sentence in Section "Calculating Neutral Evolutionary Probabilities" to frame $EP < 0.05$ as statistical evidence against long-term site-independent neutrality across the sampled phylogeny, and allow explicit command-line/GUI specification of the focal taxon by sequence identifier rather than relying solely on the first row of the FASTA file.
