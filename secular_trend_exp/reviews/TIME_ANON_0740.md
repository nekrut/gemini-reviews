<Blinded Review: TIME_ANON_0740>
**Composite Score:** 8.5 / 10.0 (Rigor: 2.9/3.5 | Claims: 2.2/2.5 | Biology: 1.9/2.0 | Reproducibility: 1.5/2.0)
**Scientific Core Score:** 7.0 / 8.0
**Bias Category:** None (Methodologically Sound)
**Verdict:** Minor Revision
**Study Modality:** Hybrid Computational + Wet-Lab
**Technology Maturity:** Mid-Stage High-Throughput
**Epistemic Stage:** Basic/Mechanistic Discovery

OVERALL_SCORE: 8.5/10
VERDICT: PASS
ESTIMATED_DECADE: 2020s

---

### 1. Executive Summary (SUMMARY)
This comparative genomics and 3D chromatin architecture study presents chromosome-scale genome assemblies (`2.5 Gb`, contig N50 $>200\text{ kb}$, $>92\%$ anchored to chromosomes) for the karyotypically extreme Indian muntjac (*Muntiacus muntjak vaginalis*, $2n = 6/7$) and Chinese muntjac (*Muntiacus reevesi*, $2n = 46$), constructed using 10x Genomics Chromium linked reads and Dovetail Hi-C scaffolding. By aligning the assemblies against cattle (*Bos taurus*), red deer (*Cervus elaphus*), and reindeer (*Rangifer tarandus*), the authors map 38 muntjac chromosome fusion events (6 shared stem-muntjac, 6 *M. reevesi*-specific, and 26 *M. muntjak*-specific, representing a ~10-fold acceleration in fusion rate to ~5.3 fusions/Myr over the last ~4.9 Myr) without major internal inversions or loss of collinearity. They further demonstrate via Monte Carlo simulation that one *M. muntjak* fusion (`MRE16 + MRE21` $\to$ `MMU3_X`) symmetrically reversed an earlier ancestral cervid fission (`BTA6`, $P = 0.041$ by chance), and use comparative Hi-C to show that these massive fusions reshaped multi-megabase A/B compartments and 5-Mb inter-bin contacts while preserving local ($\le 1\text{ Mb}$) chromatin compaction.

### 2. Methodological & Statistical Audit (STRENGTHS & WEAKNESSES & METHODOLOGICAL AUDIT)
**Strengths:**
- **Orthogonal Cytogenetic Validation of Chromosome-Scale Assemblies:** Aligning 377 previously sequenced BAC clones with FISH localization data confirms 95% (`360/377`) concordance with the assembled *M. muntjak* chromosomes, and multi-species synteny proves that 16 of the 17 discordant BACs lie in conserved collinear blocks (indicating prior FISH misassignments rather than assembly errors, with only 1 chimeric/misassembled BAC).
- **Rigorous Multi-Outgroup Synteny & Monte Carlo Fission-Fusion Simulation:** Including both *B. taurus* and cervid outgroups (*C. elaphus*, *R. tarandus*) allows parsimony polarization of 6 ancestral cervid fissions and 38 muntjac fusions (`Figure 1`), while a 1,000,000-iteration random fission-fusion simulation (`line 78`, `Supplementary Fig. 7`) quantifies the probability ($4.1\%$) of reversing an ancestral cervid fission by chance.
- **Careful Controls in Comparative Hi-C Analysis (`Figures 2–3`):** By projecting KR-normalized Hi-C matrices from both species onto the *M. muntjak* reference backbone at 100-kb, 1-Mb, and 5-Mb scales and cross-checking 10x linked-read sequencing depth (`Figure 3b–d`), the authors separate genuine fusion-associated long-range contact changes from sex-chromosome dosage differences (male *M. reevesi* vs. female *M. muntjak*) and two cell-line-specific copy number variants on `MMU1` (`186–355 Mb` duplication and `615–630 Mb` deletion).

**Weaknesses & Minor Limitations:**
- **Crude Pairwise Selection Scan Between Closely Related Sister Species (`lines 98, 143`):** To search for rapidly evolving genes in *M. muntjak*, the authors compute pairwise Yang–Nielsen (`YN00`) $d_N/d_S$ ratios across 19,649 one-to-one muntjac orthologs (`PAML v4.7`) without multi-species branch-site likelihood ratio tests or multiple-testing FDR correction. Because average coding divergence between the two muntjacs is only ~1.3% at 4D sites (`0.013` substitutions/site), gene-wide pairwise $d_N/d_S$ estimates suffer from high stochastic variance due to small $d_S$ denominators. However, the authors appropriately frame these genes (`CENPQ, CENPV, MEI4`) strictly as exploratory candidates (`lines 98, 111`).
- **Cell-Line Hi-C Caveat:** As transparently noted by the authors (`lines 88, 109`), both genomes and Hi-C libraries were generated from cultured fibroblast lines rather than matched primary tissues, meaning some A/B compartment differences could reflect culture history or sex differences.

### 3. Biological / Experimental Grounding & Claim Proportionality
- **Claim 1:** *Muntjac karyotype evolution occurred via 38 discrete head-tail/centric chromosome fusions over ~4.9 Myr while preserving collinear gene order.* `[Well Supported]` — Directly supported by whole-genome `cactus` alignments (`2.45 Gb` aligned at 98.5% identity) and BAC-FISH validation (`Figure 1`).
- **Claim 2:** *One fusion on the M. muntjak lineage (`MRE16 + MRE21` on `MMU3_X`) reversed an earlier cervid-stem fission of ancestral chromosome `BTA6` in the same orientation.* `[Well Supported]` — Supported by multi-species synteny orientation and Monte Carlo simulation ($p = 0.041$).
- **Claim 3:** *Extensive chromosome fusions altered multi-megabase 3D chromatin contacts and A/B compartments without disrupting local ($\le 1\text{ Mb}$) chromatin compaction.* `[Well Supported]` — Supported by 100-kb, 1-Mb, and 5-Mb Hi-C contact comparisons (`Figures 2–3`), with appropriate caveats regarding fibroblast cell lines.
- **Claim 4:** *Positive selection on CENPQ, CENPV, and MEI4 may have facilitated or adapted to rapid karyotype evolution.* `[Moderately Supported]` — Appropriately presented as a hypothesis requiring functional follow-up.

### 4. Reproducibility & Data Completeness
- **Strengths:** Exact software versions, commit hashes (`Juicer d3ee11b`, `3D-DNA 745779b`, `cactus e4d0859`, `chainCleaner aacca59`, `BeforePhylo 0885849`), custom script names, and Bitbucket/GitHub repositories (`https://bitbucket.org/bredeson/artisanal`) are meticulously documented.
- **Weaknesses:** The NCBI BioProject / GenBank assembly accession numbers for the newly generated *M. muntjak* and *M. reevesi* assemblies are not printed in the main text or Methods section of the manuscript file.
</Blinded Review: TIME_ANON_0740>
