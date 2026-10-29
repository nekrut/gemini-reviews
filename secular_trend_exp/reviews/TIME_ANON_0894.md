<Blinded Review: TIME_ANON_0894>
**Composite Score:** 7.3 / 10.0 (Rigor: 2.5/3.5 | Claims: 2.0/2.5 | Biology: 1.3/2.0 | Reproducibility: 1.5/2.0)
**Bias Category:** None (Methodologically Sound)
**Verdict:** Minor Revision
**Study Modality:** Hybrid Computational + Wet-Lab
**Technology Maturity:** Mid-Stage High-Throughput
**Epistemic Stage:** Basic/Mechanistic Discovery

OVERALL_SCORE: 7.3/10
VERDICT: PASS
ESTIMATED_DECADE: 2020s

---

### 1. Executive Summary / SUMMARY
This mitogenomic and phylogenetic announcement reports the first complete mitochondrial genome of *Tephrinectes sinensis* (Lacepède, 1802), a morphologically enigmatic flatfish endemic to coastal China whose familial placement within Paralichthyidae vs. broader Pleuronectoidei has long been debated. Using 10.28 Gb of filtered Illumina HiSeq 2500 paired-end (2x150 bp) reads from a voucher-archived specimen collected in Shanwei City, China (`LSU-[YEAR]-12-0125`), the authors assemble a circular 17,366 bp mitogenome containing the canonical 37 vertebrate mitochondrial genes (13 PCGs, 22 tRNAs, 2 rRNAs) and a 1,037 bp AT-rich control region (D-loop). Crucially, they cross-validate their reference-guided `BWA-MEM` + `SPAdes` assembly against an independent *de novo* assembly using `GetOrganelle v1.7.7`, recovering the exact same 17,366 bp circular sequence. Maximum-likelihood phylogenetic inference in `IQ-TREE v2.1.2` (`GTR+F+I+G4`, 1,000 bootstraps) across the 13 concatenated PCGs of *T. sinensis*, 14 Paralichthyidae species, and two outgroups (*Takifugu rubripes* and *Lateolabrax japonicus*) places *T. sinensis* with 100% bootstrap support as an early-diverging single-taxon sister lineage to all remaining sampled Paralichthyidae.

### 2. Methodological & Statistical Audit / STRENGTHS & WEAKNESSES & METHODOLOGICAL AUDIT

#### STRENGTHS
- **Orthogonal assembly cross-validation:** Reconstructing the mitogenome via both reference-assisted mapping (`BWA-MEM` to *Paralichthys olivaceus* + `SPAdes`) and reference-free *de novo* organelle assembly (`GetOrganelle v1.7.7` across $k = 21\text{--}127$), and confirming base-for-base identity (17,366 bp) alongside `Pilon` polishing and `SAMtools` coverage verification, eliminates reference-guided chimeric artifacts.
- **High-standard voucher and raw data archiving:** Provides exact GPS collection coordinates, voucher specimen photographs (ocular and blind sides, Fig. 1), museum catalog number (`LSU-[YEAR]-12-0125`), and full NCBI accessions for the assembled mitogenome (`PV021852`), BioProject (`PRJNA1215796`), BioSample (`SAMN46419712`), and raw sequencing reads (`SRR32129885`).
- **Measured phylogenetic interpretation:** The authors explicitly recognize that a single non-recombining maternal locus cannot by itself resolve family-level classification and that multilocus nuclear phylogenomics are required to test whether *T. sinensis* represents a distinct family outside Paralichthyidae or the basal lineage of Paralichthyidae.

#### WEAKNESSES & METHODOLOGICAL AUDIT
- **Restricted taxon sampling across Pleuronectoidei families:** Because all 14 ingroup comparators belong to Paralichthyidae and the only two outgroups are non-pleuronectiform percomorphs (*Takifugu rubripes* and *Lateolabrax japonicus*), topological placement of *T. sinensis* as sister to the 14 sampled Paralichthyidae species is guaranteed so long as *T. sinensis* is not nested inside *Paralichthys*, *Pseudorhombus*, *Ancylopsetta*, *Gastropsetta*, or *Hippoglossina*! To test Hoshino & Amaoka's hypothesis that *T. sinensis* lies outside Paralichthyidae (e.g., closer to Pleuronectidae, Bothidae, Paralichthodidae, Poecilopsettidae, or Citharidae), representatives of those other flatfish families must be included in the ingroup sampling.
- **Unpartitioned nucleotide model (`GTR+F+I+G4`) across all 13 PCGs:** Concatenating 13 protein-coding genes without codon-position partitioning (1st, 2nd, 3rd codon positions) or amino-acid/codon models can be sensitive to 3rd-position compositional saturation across deep teleost divergences.
- **Minor read-count typo in Methods (line 28):** Line 28 states *"yielding 77,061,072 filtered paired-end reads"* in one sentence and *"Quality-filtered reads (77,061,272 paired-end sequences)"* in the very next sentence (a 200-read digit transposition, and $77.06\text{M} \times 150\text{ bp} = 11.56\text{ Gb}$ single-end or $23.1\text{ Gb}$ paired-end, likely representing total single reads rather than pairs for 10.28 Gb).

### 3. Biological / Experimental Grounding & Claim Proportionality
- **Claim 1:** The complete mitochondrial genome of *Tephrinectes sinensis* is 17,366 bp with conserved vertebrate gene order and a 1,037 bp D-loop. `[Well Supported]` — Verified by dual assembly pipelines and multi-tool annotation.
- **Claim 2:** Within a phylogeny of 14 Paralichthyidae species rooted on *Takifugu* and *Lateolabrax*, *T. sinensis* forms a single early-diverging lineage sister to the remaining sampled Paralichthyidae (100% bootstrap). `[Well Supported]` — Directly supported by the ML tree, though testing exclusion from Paralichthyidae requires sampling other Pleuronectiformes families.

### 4. Reproducibility & Data Completeness
- **Exemplary Data Availability:** GenBank (`PV021852`), SRA (`SRR32129885`), BioProject (`PRJNA1215796`), BioSample (`SAMN46419712`), all comparative accession numbers (Fig. 3 legend), and exact software versions are fully provided.
</Blinded Review: TIME_ANON_0894>
