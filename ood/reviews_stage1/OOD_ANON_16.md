# Review of OOD_ANON_16

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **8.6 / 10.0** (Strong / Sound)  
* **Score Breakdown:** Rigor: 3.0/3.5 | Claims: 2.2/2.5 | Biology: 1.8/2.0 | Reproducibility: 1.6/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This comparative population genomics study analyzes 1,294 *Escherichia coli* sensu stricto draft genomes selected to represent the phylogenetic and ecological diversity of >5,000 isolates collected across Australia between 1993 and 2015, predominantly from non-clinical sources (freshwater, wild bird and non-human mammal feces, human commensal and inflammatory bowel disease biopsies, human ExPEC, and retail poultry meat). Combining pan-genome clustering (MMseqs2 at 80% identity/coverage), a 2,486-gene persistent-genome maximum-likelihood phylogeny (IQ-TREE GTR+F+I+G4 rooted on 87 *Escherichia* outgroup genomes), ancestral gene gain/loss reconstruction (Count Wagner parsimony), mobile genetic element (MGE) profiling (VirSorter, PlaScope, CONJscan, IntegronFinder, ISfinder), and phylogenetic GWAS (Scoary), the authors characterize the joint roles of vertical lineage and isolation habitat in shaping gene repertoire evolution. They show that gene repertoire relatedness (GRR) drops rapidly at very short patristic distances (intra-ST) due to high MGE turnover and thereafter decays linearly with phylogenetic distance ($R^2 = 0.49$); that phylogroups A and B1 have the smallest genomes but the highest gene turnover and largest rarefied pan-genomes; that genome size is equally explained by phylogroup and isolation source ($R^2 = 0.36$), whereas MGE abundance is primarily explained by source (90% of explained variance); and that 285 freshwater isolates exhibit streamlined genomes, depleted virulence/antibiotic resistance genes, and enriched Group IVe capsules indicative of resident aquatic adaptation. Underlying numerical datasets (`S1`/`S2 Dataset`) and ENA genome accessions (`PRJEB34791`) are provided.

This is a comprehensive, well-controlled, and methodologically rigorous population genomics study that overcomes the heavy clinical ascertainment bias of prior *E. coli* datasets. The authors systematically control for sample-size differences across phylogroups and habitats via 1,000-permutation rarefaction ($n=50$), validate draft-genome MGE fragmentation against 370 complete RefSeq genomes, confirm that singleton artifacts at contig edges do not drive the rapid initial GRR drop, and account for population structure in their pan-genome GWAS. Minor limitations include the reliance on short-read draft assemblies (including 70 legacy Roche 454 genomes) that fragment plasmids and insertion sequences, the use of symmetric gain/loss penalties ($g = 1$) in Wagner parsimony rather than probabilistic birth–death rates on terminal branches, and the absence of explicit spatial/temporal co-sampling covariates in the source-association regressions.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Two-phase regime of gene repertoire diversification—rapid intra-ST drop driven by MGE turnover followed by linear decay with patristic distance: [Well Supported].**  
  The authors demonstrate that 85% of intra-ST genome pairs have $\text{GRR} < 95\%$ ($\sim 235$ gene differences) and validate that this rapid initial drop persists after removing all 33,705 singleton gene families (`S6 Fig`), ruling out sequencing or assembly edge artifacts as the primary driver. Beyond the intra-ST scale, GRR decreases linearly with core-genome patristic distance ($Y = 90.2 - 75.7 X$, $R^2 = 0.49, p < 10^{-4}$, Fig. 2A) without abrupt plateaus, supporting continuous horizontal gene transfer across the species.

* **Inverse relationship between genome size and gene repertoire turnover across phylogroups (phylogroups A and B1 have the smallest genomes but highest gain/loss rates and largest pan-genomes): [Well Supported].**  
  Using 1,000 rarefied subsamples of 50 genomes per phylogroup to eliminate sample-size bias (Fig. 3C, Fig. 5B), the authors show that phylogroups A and B1 have the smallest average genome sizes and fewest MGE genes per genome, yet harbor the largest rarefied pan-genomes, smallest persistent genomes, highest ST/serotype Shannon diversity, and highest terminal-branch gene gain/loss counts and inter-phylogroup co-gains, whereas phylogroup B2 has larger genomes with lower inter-phylogroup gene flow.

* **Joint determination of genome size by phylogroup and isolation source ($R^2 = 0.36$), with MGE load primarily driven by isolation source: [Moderately Supported].**  
  Stepwise multiple regressions (Fig. 6D, `S3`–`S6 Tables`) and intra-phylogroup stratified ANOM comparisons (`S17 Fig`) convincingly show that both phylogroup and isolation source independently contribute to total and non-MGE genome size, while isolation source accounts for 90% of the explained variance in MGE gene counts ($R^2 = 0.19$). A minor statistical caveat is that the observations in the stepwise ordinary least squares regression are not phylogenetically independent within phylogroups, and potential sampling confounders (e.g., whether all 283 poultry meat or 285 freshwater isolates came from a restricted set of geographic sites or collection years) are not included as random effects.

* **Freshwater *E. coli* isolates represent locally adapted aquatic populations rather than passive fecal contamination: [Well Supported].**  
  The 285 freshwater isolates are strongly enriched in phylogroup B1 (43%), possess the smallest genomes across all phylogroups (`S17 Fig`), carry the fewest MGEs, plasmids, antibiotic resistance genes, virulence factors, and colicins, yet exhibit the highest ST/serotype diversity and a specific positive GWAS enrichment for Group IVe capsule loci (`P < 10^{-10}`, Fig. 8C, `S20 Fig`). The consistency of these genomic traits across phylogroups within the freshwater niche provides strong evidence against simple random host shedding.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Assess Sensitivity of Terminal-Branch Gain/Loss Counts to Wagner Parsimony Penalty Ratios ($g$) and Branch Lengths
* **WHY:** In Section "Reconstruction of the evolution of gene repertoires" (line 130), ancestral gene content was inferred using Wagner parsimony with equal gain and loss penalties ($g = 1$), and raw terminal-branch event counts were compared across phylogroups (Fig. 5B, cols 6–7) and sources (Fig. 6C, cols 14–15). Because terminal branch lengths vary systematically with sampling density (e.g., densely sampled STs in A and B1 have shorter terminal branches than sparsely sampled clades), raw terminal-branch event counts conflate evolutionary rate with tip sampling density, and $g = 1$ can over-infer parallel terminal gains relative to ancestral gain followed by losses.
* **WHAT:** Normalize terminal-branch gain and loss counts by terminal branch length (or compare rarefied trees of 50 genomes per phylogroup) and verify that the higher turnover in A/B1 holds when using a higher gain-to-loss penalty ratio ($g = 2$ or $g = 3$) in Count.
* **HOW:** Re-run Count Wagner parsimony with $g = 2$ on the rooted species tree, and plot both raw terminal-branch gains/losses and branch-length-normalized rates (events per substitution per site on terminal branches, or on the 50-genome rarefied subtrees) for each phylogroup.

#### 2. Control for Phylogenetic Non-Independence and Sampling Metadata in the Genome-Size and MGE Regressions
* **WHY:** Stepwise multiple regression treating 1,294 genomes as independent observations (Fig. 6D) only accounts for phylogeny at the coarse 7-phylogroup level; clonally related isolates within the same ST or sampling batch share both isolation source and genome size, which can inflate $F$-statistics and alter variance partitioning.
* **WHAT:** Repeat the variance partitioning of genome size and MGE gene count on a dataset collapsed to one representative genome per ST$\times$source combination (or using phylogenetic generalized least squares / linear mixed models with ST and geographic region/year as random effects).
* **HOW:** In R (`lme4` or `phylolm`), fit `lmer(genome_size ~ phylogroup + source + (1|ST) + (1|sequencing_center))` or re-run the two-way ANOVA on the 442 single-ST representative genomes, and report the partial $R^2$ for `phylogroup` and `source`.

#### 3. Quantify the Impact of Sequencing Platform (Roche 454 vs. HiSeq vs. MiSeq) on Singleton and IS Counts
* **WHY:** The 1,294 genomes were sequenced across three platforms over 10 years (70 Roche 454 GS FLX, 70 Illumina HiSeq 2000, and 1,154 Illumina MiSeq). Because Roche 454 is prone to homopolymer indel errors that cause frameshifts and split open reading frames into apparent "singletons," platform differences could unevenly affect singleton and IS counts if 454 genomes are concentrated in specific sources or phylogroups.
* **WHAT:** Test whether the 70 Roche 454 genomes have elevated singleton counts, pseudogene fragments, or lower persistent-gene completeness compared to the Illumina genomes, and confirm their distribution across isolation sources.
* **HOW:** Compare the number of singletons and missing persistent genes per genome between the 454 ($n=70$), HiSeq ($n=70$), and MiSeq ($n=1,154$) subsets using a Wilcoxon rank-sum test in `S2 Text`.
