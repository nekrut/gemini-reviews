# Blinded Review: SP_ANON_132

**Composite Score:** 6.5 / 10.0 (Rigor: 2.0/3.5 | Claims: 1.6/2.5 | Biology: 1.5/2.0 | Reproducibility: 1.4/2.0)
**Bias Category:** Reference-Mapping Ascertainment Bias & Homozygous-Only Low-Coverage Filtering
**Verdict:** Major Revision
**Study Modality:** Wet-Lab Primary Experimental
**Technology Maturity:** Mid-Stage High-Throughput
**Epistemic Stage:** Basic/Mechanistic Discovery

---

## 1. Executive Summary

This study sequences complete mitochondrial genomes (10,840 bp aligned across 63 specimens) and low-coverage partial nuclear genomes (24.5–106.2 Mb of autosomal sequence and 0.8–5.6 Mb of X-chromosomal sequence via 35-bp Illumina GAII reads) for four Przewalski's horses representing all four surviving matrilines, alongside one Somali wild ass outgroup (`Equus asinus somalicus`, 100-bp reads), mapped against the domestic Thoroughbred reference genome (`eca2`). While the complete mitochondrial phylogeny solidly resolves the placement of the four Przewalski's matrilines within domestic horse clades (`A–G`), the nuclear genomic inferences—estimating nucleotide diversity, Przewalski's vs. domestic horse divergence time (0.118 Mya), and reciprocal monophyly—are compromised by an aggressive homozygous-only filtering rule at ~2x depth, stringent reference-alignment mismatch caps against the Thoroughbred genome, and the inclusion of only a single domestic horse nuclear genome (`eca2`).

---

## 2. Methodological & Statistical Audit

* **Severe Bias from Discarding All Polymorphic/Heterozygous Sites at Low Coverage (Methods, line 35):** Because shotgun coverage of the four Przewalski's horses was very low (yielding only 24.5–106.2 Mb of covered autosomal sequence per horse, with an intersection across all five sequenced equids of just **~2.5 Mb**), the authors applied the following genotype-calling rule: *"To ensure high quality of sequences, we only used sites supported by at least two uniquely mapped sequencing reads with an identical call, and all polymorphic sites were discarded."*
  Discarding all heterozygous ("polymorphic") sites within an individual while requiring $\ge 2$ identical reads has profound population-genetic consequences:
  1. In diploid individuals with high heterozygosity (or in the outbred Somali wild ass vs. inbred captive Przewalski's horses), discarding all sites where two reads carry different alleles selectively censors heterozygous loci, artificially depressing within-group genetic distance in individuals with higher read depth or higher heterozygosity.
  2. When comparing the Thoroughbred reference (`eca2`, where a single haplotype consensus is represented without the $\ge 2$ identical-read filter) against the 35-bp Przewalski's reads, the asymmetry in calling rules distorts terminal branch lengths.
* **Reference Bias from Mapping 35-bp Reads with $\le 2$ Mismatches to the Domestic Horse Reference (`eca2`):** For the four Przewalski's horses, 35-bp single-end reads were mapped to `eca2` (`EquCab2.0`) allowing at most 2 mismatches (`BWA`). Any genomic window where a Przewalski's horse haplotype differs from the Thoroughbred reference by $\ge 3$ substitutions (or an indel) within 35 bp fails to map, systematically censoring the most divergent loci between Przewalski's and domestic horses and biasing the estimated divergence time (0.118 Mya) downward toward the Thoroughbred reference. Moreover, the Somali wild ass outgroup was sequenced with 100-bp reads mapped with up to 6 mismatches (`2 mismatches per 35-bp` equivalent), creating read-length and mapping-stringency asymmetry between the ingroup and outgroup.
* **Single Domestic Horse Nuclear Genome (`N = 1`) Cannot Test Reciprocal Monophyly or Progenitor Status:** In the mitochondrial analysis (Fig. 2), dozens of domestic horses across clades A–G are included, showing paraphyly/interleaving of Przewalski's and domestic mtDNA lineages. In contrast, the autosomal and X-chromosomal nuclear trees (Fig. 3) contain **only one single domestic horse** (the Thoroughbred reference `eca2`) alongside the four Przewalski's horses and one Somali wild ass. In a tree with 4 closely related captive Przewalski's horses (which passed through a 12-individual captive bottleneck), 1 domestic horse, and 1 distant outgroup, it is nearly inevitable that the 4 bottlenecked Przewalski's horses cluster together relative to the single Thoroughbred. Concluding from $N=1$ domestic horse that Przewalski's horses form a separate clade and "are not the direct progenitors of domestic horses" (Abstract) overreaches what a single domestic genome can establish (though the authors appropriately acknowledge in the Discussion that additional domestic breeds must be sequenced).
* **Male Y-to-X Mismapping Artifact on the X Chromosome:** The authors candidly identify and report that the male Przewalski's horse (`Bars`) exhibits an anomalously long branch on the X chromosome (Fig. 3B, 0.00201 vs. 0.00051–0.00090 in females) because Y-chromosomal reads mismapped to homologous regions of the female `eca2` X chromosome reference. While their transparency in diagnosing this artifact via simulation is commendable, retaining the contaminated male X-chromosome alignments in the primary X-chromosomal divergence calculations inflates the reported X-chromosome diversity ($7.2 \times 10^{-4}$).

---

## 3. Biological / Experimental Grounding & Claim Proportionality

* **`[Well Supported]` Persistence of Two Divergent Mitochondrial Clades (`I` and `II`) Across the Four Surviving Przewalski's Horse Matrilines:** The 10,840-bp complete mtDNA analysis across 63 equids is well powered, high coverage (33.5x–201.3x), and robustly places matrilines `O`, `B`, `K` and `S` within the broader caballine mitochondrial tree with an estimated TMRCA of ~0.145 Mya.
* **`[Well Supported]` Absence of Ascertainment Bias Relative to Commercial Equine SNP Arrays:** Demonstrating via subsampling simulations that whole-genome shotgun pairwise distances avoid the heterozygosity inflation of commercial SNP arrays (which were ascertained on polymorphic SNPs in domestic breeds) is a valid methodological point.
* **`[Overstated]` Nuclear Monophyly and Exclusion of Przewalski's Horses as Direct Progenitors of Domestic Horses:** Because nuclear data were analyzed for only a single domestic horse (`eca2`) under reference-biased 35-bp mapping and homozygous-only filtering, claims of species-level nuclear monophyly and ancestral exclusion are overstated relative to the taxonomic sampling ($N=1$ domestic horse).

---

## 4. Reproducibility & Data Completeness

* **Data Availability:** Complete mitochondrial genome assemblies and raw Illumina GAII sequencing reads are deposited in GenBank/SRA under accession numbers `JN398377–JN398457` and `SRA039947.2`.
* **Simulation Details:** The parametric tree simulation protocol used to verify Neighbor-Joining topology recovery under non-overlapping pairwise nuclear alignments (2,500 replicates across five tree topologies) is well documented in the Methods and Figure 4.
