# Review of ANON_18

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **8.3 / 10.0** (Strong / Sound) | **Scientific Core Score:** **6.8 / 8.0**  
* **Score Breakdown:** Methodological Rigor: 2.8/3.5 | Claim-Evidence Alignment: 2.1/2.5 | Biological Plausibility: 1.9/2.0 | Reproducibility: 1.5/2.0  
* **Score Breakdown (Compact):** Rigor: 2.8/3.5 | Claims: 2.1/2.5 | Biology: 1.9/2.0 | Reproducibility: 1.5/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript presents the reference genome assembly (`gasAcu1.0`) of the threespine stickleback (*Gasterosteus aculeatus*, generated at $9.0\times$ Sanger coverage with contig N50 of 83.2 kb, scaffold N50 of 10.8 Mb, and 400.4 Mb anchored to linkage groups) alongside whole-genome short-read resequencing ($2.3\times$ average Illumina coverage per individual; $48\times$ combined) of 20 additional fish from global Pacific and Atlantic marine-freshwater population pairs. To identify genomic loci underlying parallel ecological adaptation, the authors apply two complementary methods across the 21 genomes: a self-organizing map / iterative Hidden Markov Model (SOM/HMM) of local phylogenetic topologies and a sliding-window (2,500 bp window, 500 bp step) Cluster Separation Score (CSS) with permutation-based FDR control, supplemented by Bayesian data-driven clustering (DDC). They identify 242 divergent regions ($0.5\%$ of the genome) by either method and 147 regions ($0.2\%$) by both, successfully recovering the positive-control *EDA* locus on chromosome IV, discovering three large chromosomal inversions (on chrI, chrXI, and chrXXI) validated by marine BAC paired-end anomalies, and estimating from the top 64 high-confidence regions that $41\%$ map entirely to non-coding intervals, $43\%$ span coding and non-coding sequence without ecotype-specific nonsynonymous SNPs, and $17\%$ carry consistent nonsynonymous substitutions.

This is a foundational genomic resource and evolutionary genomics study that integrates de novo reference assembly, global population resequencing, BAC-based structural variant validation, hybrid-zone differentiation (River Tyne), and common-garden microarray expression profiling. The primary methodological limitations lie in the downstream inference of regulatory versus coding predominance from low-coverage ($2.3\times$ per fish) SNP calls: requiring "perfect allele-ecotype association" across 21 fish at $2.3\times$ depth suffers from substantial allele-dropout and genotype-imputation uncertainty, and classifying an entire 3–5 kb window containing coding sequence as "regulatory" whenever it lacks a *perfectly fixed* nonsynonymous SNP (while possessing at least one perfectly associated non-coding SNP) systematically inflates the regulatory fraction when multiple non-coding SNPs exist per window. Addressing this bias requires probabilistic genotype likelihoods and symmetric criteria for coding versus regulatory variant classification.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **High-quality anchored reference genome assembly (`gasAcu1.0`) and recovery of 147–242 parallel marine-freshwater divergent genomic regions across global stickleback populations: [Well Supported].**  
  The Sanger reference assembly exhibits high contiguity (83.2 kb contig N50; 86.9% anchored to linkage groups), and the concordance between the topology-based SOM/HMM and distance-based CSS scans (147 shared regions, median size $<5$ kb), recapture of the 16 kb minimal *EDA* haplotype (Figure 2c), and 91% validation rate (10/11 tested regions) via Sequenom genotyping in independent populations provide strong support.

* **Chromosomal inversions on chromosomes I (442 kb), XI (412 kb), and XXI (1,700 kb) maintain divergent ecotypic haplotypes across marine-freshwater hybrid zones: [Well Supported].**  
  The sharp CSS and DDC cluster boundaries are orthogonally validated by size and orientation anomalies of paired-end reads from a marine large-insert ($\sim 220$ kb) BAC library mapped against the freshwater reference (Figure 5a–b), flanked by inverted repeats and showing steep allele-frequency clines across hybrid zones (Supplementary Table 10).

* **Regulatory changes predominate over protein-coding changes (~84% vs. ~17%) among loci underlying parallel marine-freshwater stickleback evolution: [Overstated].**  
  To partition the 64 strictest regions into coding versus regulatory categories (Figure 6a), the authors require every region to contain at least one SNP with "perfect allele-ecotype association" across the 21 fish. First, at $2.3\times$ average Illumina coverage per diploid individual, the probability of observing both alleles at a heterozygous site or calling all 21 individuals without dropout is low, making "perfect association" highly sensitive to coverage variance and imputation. Second, the classification rule is asymmetric: the 43% of regions that span *both* coding and non-coding sequence are assigned to regulatory evolution simply because they lack a *perfectly* associated nonsynonymous SNP, even though a causal nonsynonymous variant with 1–2 missing/imperfect calls or an uncalled indel is excluded while any of dozens of linked non-coding SNPs passing the threshold qualifies the locus as regulatory.

* **Locally differentiated loci across the River Tyne marine-freshwater hybrid zone substantially overlap globally shared parallel adaptation regions (35.3% of top 0.1% divergent windows): [Moderately Supported].**  
  While the enrichment of globally shared CSS signal within the top 0.1% divergent windows of the River Tyne pair (Figure 4b) is clear, the Tyne marine and freshwater individuals were themselves included among the 21 fish used to define the global CSS and SOM/HMM scores, introducing partial circularity between local divergence and global score calculation, and single-fish comparisons at $2.3\times$ depth have high sampling variance.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Correct for Low-Coverage Ascertainment and Asymmetric Window Classification in the Coding vs. Regulatory Partition
* **WHY:** At $2.3\times$ per-individual sequencing depth, requiring "perfect allele-ecotype association" across 21 individuals favors regions with higherSNP density (such as non-coding flanking sequences) where at least one variant happens to achieve complete coverage and concordance by chance, while penalizing single causal nonsynonymous sites that suffer a single read-depth dropout or incomplete penetrance in one population.
* **WHAT:** Re-evaluate the relative contribution of coding versus non-coding variants across the 64 (and 147) parallel regions using genotype likelihoods and site-level (rather than asymmetric window-level) enrichment statistics.
* **HOW:** Compute site-specific marine-freshwater $F_{ST}$ or CSS directly from genotype likelihoods (e.g., SAMtools/ANGSD) across all callable sites, and compare the empirical excess of high-differentiation nonsynonymous SNPs, synonymous SNPs, Conserved Non-Coding Elements (CNEs), and intergenic SNPs relative to their genome-wide background densities.

#### 2. Eliminate Sample Overlap When Quantifying Global Parallelism in the River Tyne Hybrid Zone
* **WHY:** Including the River Tyne marine and freshwater individuals inside the 21-fish discovery panel inflates the overlap between the top 0.1% divergent windows in the River Tyne pair and the globally shared divergent regions (35.3%).
* **WHAT:** Recompute the global CSS and SOM/HMM scores on the 19 non-Tyne individuals (leave-one-pair-out cross-validation).
* **HOW:** Recalculate the $19 \times 19$ pairwise $\pi$ matrices excluding the two River Tyne fish, call global divergent windows at the same 2% and 5% FDR thresholds, and report the leave-one-pair-out overlap percentage with the top 0.1% River Tyne divergent windows.

#### 3. Account for Recombination Rate Variation and Background Selection in Window Scans
* **WHY:** Both CSS (based on between-ecotype versus within-ecotype $\pi$) and SOM/HMM are sensitive to local reductions in within-population diversity ($\pi_w$) driven by low recombination rates and background selection, which also correlate with gene density and CNE density.
* **WHAT:** Test whether the parallel divergent regions show elevated absolute divergence ($d_{XY}$) between marine and freshwater ecotypes rather than solely reduced within-ecotype diversity ($\pi_w$).
* **HOW:** Using the genetic cross linkage map anchored in `gasAcu1.0`, stratify the 2,500 bp windows by local recombination rate (cM/Mb) and report both absolute divergence ($d_{XY}$) and relative divergence (CSS/$F_{ST}$) for the 147 shared regions and the gene/CNE density enrichment tests (Supplementary Figures 8–9).
