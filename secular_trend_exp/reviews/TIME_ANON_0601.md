<Blinded Review: TIME_ANON_0601>
OVERALL_SCORE: 7.4/10
VERDICT: PASS
ESTIMATED_DECADE: 2010s
**Composite Score:** 7.4 / 10.0 (Rigor: 2.3/3.5 | Claims: 1.9/2.5 | Biology: 1.6/2.0 | Reproducibility: 1.6/2.0)
**Scientific Core Score:** 5.8 / 8.0
**Bias Category:** Statistical/Design
**Verdict:** Minor Revision
**Study Modality:** Hybrid Computational + Wet-Lab
**Technology Maturity:** Mid-Stage High-Throughput
**Epistemic Stage:** Basic/Mechanistic Discovery

---

### 1. Executive Summary (SUMMARY)
This study presents the first transcriptome-based phylogenomic analysis of the arthropod class Diplopoda (millipedes), generating Illumina HiSeq paired-end 50-bp RNA-seq data for 8 millipede exemplars and 1 centipede outgroup (*Lithobius*) and combining them with public EST/genome data for 1 additional millipede (*Archispirostreptus gigas*) and 2 outgroups (*Ixodes scapularis* and *Daphnia pulex*). Using HaMStR orthology prediction followed by SCaFoS, Gblocks, and Aliscore/ALICUT filtering, the authors assemble a supermatrix of 221 nuclear protein-coding genes (61,641 aligned amino acid sites) and infer phylogenies using RAxML (partitioned PROTGAMMAWAG) and PhyloBayes (CAT/default), alongside CONSEL topology tests, parsimony ancestral state reconstructions, and relaxed-clock divergence dating. The dataset strongly supports the monophyly of Helminthomorpha, Colobognatha, Eugnatha, and Coelocheta, while recovering a novel placement of Stemmiulida sister to Juliformia (rendering Nematophora paraphyletic). The authors appropriately temper their taxonomic conclusions given the sparse taxon sampling (10 millipede species covering 9 of 16 orders), though the manuscript contains several table cross-reference mix-ups and a contradiction between the text and Figure 4 caption regarding fossil calibrations.

### 2. Methodological & Statistical Audit (STRENGTHS, WEAKNESSES & METHODOLOGICAL AUDIT)
**Strengths:**
* Expands the nuclear character sampling for Diplopoda from 3 genes in prior studies to 221 orthologous loci (61,641 amino acid positions) with stringent paralog, compositional divergence (>75% difference filter), and alignment-ambiguity masking (Gblocks + Aliscore).
* Performs explicit outgroup-removal sensitivity analyses (confirming ingroup topology stability) and likelihood-based topology tests (AU, SH, KH, WSH in CONSEL) against three historical morphological/combined hypotheses.
* Explicitly acknowledges the limitations of taxon sampling and refrains from premature formal nomenclatural changes.

**Weaknesses & Methodological Audit:**
* **Sparse Taxon Sampling and Severe Missing Data in *Archispirostreptus*:** Only 9 of the 16 extant millipede orders are represented (missing *Polyxenida*, *Glomerida*, *Sphaerotheriida*, *Siphonocryptida*, *Siphonophorida*, *Siphoniulida*, and *Spirobolida*), and most orders are represented by a single exemplar. Moreover, the EST-derived taxon *Archispirostreptus* is present in only 33 of the 221 post-optimization loci (14.93% coverage; Table 4), which can destabilize branch lengths and divergence time estimates within Juliformia.
* **Discordance Between ML and BI Placement of Polydesmida (*Pseudopolydesmus*):** PhyloBayes places *Pseudopolydesmus* sister to `Juliformia + Stemmiulida` ($\text{PP} = 0.99$), whereas RAxML places it at the base of Eugnatha (though with low bootstrap support, $\text{BS} = 20$, and CONSEL AU/SH tests cannot statistically distinguish the two topologies). Because RAxML used a homogeneous `PROTGAMMAWAG` model across all partitions while PhyloBayes used site-heterogeneous profiles, the authors should explicitly discuss compositional heterogeneity or long-branch effects for *Pseudopolydesmus* rather than simply declaring the BI tree preferred.
* **Use of `FastTree 2.1` Site Likelihoods for CONSEL Topology Tests:** In the Methods ("Phylogenetic Inference"), per-site log-likelihoods for CONSEL were computed using `FastTree 2.1` rather than RAxML under the partitioned `PROTGAMMAWAG` model used for ML tree inference.
* **Contradiction Between Main Text and Figure 4 Caption on Molecular Clock Calibrations:** The Methods text ("Molecular Divergence Dating", line 92) states that **two** fossil constraints were used (*Pneumodesmus newmani* at 428 MYA and *Sigmastria dilata* at 410 MYA) and the root prior was set at **560 MYA** ($\text{SD} = 560\text{ MY}$). However, the Figure 4 caption states: *"A single fossil constraint was used, Pneumodesmus newmani - ~428 MYA, and the root prior was set at 510 MYA"* (even though two orange calibration circles appear on Figure 4 and both constrained nodes are listed in Results lines 188–190).
* **Systematic Misnumbering of Table Cross-References and Omission of *Daphnia* from Tables 1 and 4:**
  1. In Results line 100, *"summarized in Table 2"* actually refers to **Table 1** (read counts, contigs, HaMStR orthologs).
  2. In Results line 125, *"summarized in Table 4"* actually refers to **Table 2** (pre- and post-optimization loci, characters, gaps, missing data), and *"summarized in Table 5"* actually refers to **Table 4** (taxon inclusion levels).
  3. In Results line 125, the total pre-optimization gaps (`1,788,558`) and missing data (`1,833,905`) are described as among `532,002` aligned sites (they are actually counts across the `532,002 × 12 = 6,384,024` taxon-site cells).
  4. Both Table 1 and Table 4 list only 11 taxa, omitting the 12th taxon (*Daphnia pulex* outgroup), and the Methods text (line 75) inconsistently writes *"less than 11 of the 12 included taxa were deleted. The cutoff for taxon inclusion (11 of 13)..."*.

### 3. Biological / Experimental Grounding & Claim Proportionality
* **Monophyly of Helminthomorpha, Colobognatha, Eugnatha, and Coelocheta (*Callipodida + Chordeumatida*): [Well Supported].** Strongly supported ($\text{PP} = 1.00$, high ML bootstrap) in both BI and ML analyses and insensitive to outgroup removal.
* **Paraphyly of Nematophora (with *Stemmiulida* grouping with *Juliformia* rather than *Coelocheta*) and non-homology/loss of spinnerets: [Moderately Supported].** Strongly supported by the 221-gene matrix ($\text{PP} = 0.99–1.00$), though *Prostemmiulus* had the lowest transcriptome completeness (33.47% complete CEGs, 84.16% locus inclusion) and the enigmatic order *Siphoniulida* was unavailable.
* **Novel clade of `Juliformia + Merocheta (Polydesmida) + Stemmiulida`: [Fragile].** Supported by PhyloBayes ($\text{PP} = 0.99$) but not by the RAxML best tree, and not statistically distinguishable by AU/SH topology tests in CONSEL.

### 4. Reproducibility & Data Completeness
* **Data Availability:** Raw Illumina RNA-seq reads are deposited in the NCBI SRA (`SRX326775–SRX326777`, `SRX326779–SRX326784`), and physical voucher specimens are deposited in the Auburn University Museum of Natural History. (Note: the concatenated 221-gene alignment matrix and tree files should also be deposited in Dryad or TreeBASE.)
* **Pipeline Transparency:** All software tools (`FASTX Toolkit`, `Trinity`, `CEGMA`, `HaMStR`, `MAFFT`, `SCaFoS`, `Gblocks`, `Aliscore`, `ALICUT`, `FASconCAT`, `RAxML 7.2.8`, `PhyloBayes 3.3b`, `CONSEL`, `Mesquite`) and command-line parameters are thoroughly documented.
</Blinded Review: TIME_ANON_0601>
