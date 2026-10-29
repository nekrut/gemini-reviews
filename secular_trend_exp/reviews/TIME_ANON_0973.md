<Blinded Review: TIME_ANON_0973>
**Composite Score:** 8.2 / 10.0 (Rigor: 2.9/3.5 | Claims: 2.2/2.5 | Biology: 1.7/2.0 | Reproducibility: 1.4/2.0)
**Bias Category:** None (Methodologically Sound)
**Verdict:** Minor Revision
**Study Modality:** Hybrid Computational + Wet-Lab
**Technology Maturity:** Mid-Stage High-Throughput
**Epistemic Stage:** Basic/Mechanistic Discovery

OVERALL_SCORE: 8.2/10
VERDICT: PASS
ESTIMATED_DECADE: 2020s

---

### 1. Executive Summary / SUMMARY
This statistical genetics and genomics study constructs a high-density, multi-dosage, haplotype-phased genetic linkage map for autotetraploid guinea grass (*Megathyrsus maximus*, $2n = 4x = 32$) using genotyping-by-sequencing (GBS, *Pst*I digestion, Illumina HiSeq Xten 150 bp paired-end) across an $F_1$ biparental mapping population of 224 progeny (215 retained after genomic relationship matrix contaminant filtering) derived from a cross between the sexual maternal accession `S12` and the apomictic paternal cultivar `Miyagui` (each parent replicated $14\times$ across 7 plates). Because *M. maximus* lacks a species-specific reference genome, the authors align reads via `Bowtie2` against six comparative grass genomes/subgenomes (*Urochloa ruziziensis*, *Panicum hallii*, *Panicum virgatum* K and N, *Setaria italica*, and *Setaria viridis*), call continuous/discrete tetraploid allele dosages ($0, 1, 2, 3, 4$) in `GATK v4.1.6.0` (requiring $\text{DP} \ge 50\times$), and build an integrated multilocus linkage map using multidimensional scaling (`MDS`) and a multipoint autotetraploid Hidden Markov Model (`MAPpoly v0.2.3`) with a $5\%$ global emission error rate. The final map places 7,095 markers across 8 homology groups (matching the base chromosome number $x = 8$), spanning $1,573.31\ \text{cM}$ at $4.12\ \text{markers/cM}$, resolves all 64 parental homolog haplotypes, identifies an evolutionary chromosome fusion/insertion rearrangement on Homology Group 3 reducing $x = 9 \to 8$, and confirms strictly polysomic (random bivalent) meiotic pairing ($\approx 0.33$ per configuration) with no preferential pairing.

### 2. Methodological & Statistical Audit / STRENGTHS & WEAKNESSES

#### STRENGTHS
- **Rigorous polyploid dosage calling and pedigree quality control:** Calling allele dosages ($0\text{--}4$) in autotetraploids from GBS requires high sequencing depth to prevent heterozygous under-calling; the authors enforce a strict minimum depth of $50\times$ per individual genotype call, include 14 biological/technical replicates of each parent across the 7 sequencing plates, and use the `AGHmatrix` genomic relationship matrix ($\mathbf{G}$) to identify and remove 9 contaminant/apomictic-escape offspring before linkage mapping.
- **State-of-the-art multipoint HMM phasing (`MAPpoly`):** Rather than restricting analysis to simplex markers ($1 \times 0$ and $0 \times 1$) analyzed under diploid pseudo-testcross approximations, the authors incorporate simplex, double-simplex, and multiplex dosage combinations ($0\text{--}4$) in a full autotetraploid multipoint HMM, computing Genomic Information Content (GIC) profiles for all 64 parental homologs and marginalizing meiotic pairing probabilities to formally test polysomic vs. preferential pairing.
- **Evolutionary synteny discovery:** Cross-mapping against four $x = 9$ diploid Panicoid genomes (*U. ruziziensis*, *P. hallii*, *S. italica*, *S. viridis*) reveals a consistent chromosomal rearrangement in Homology Group 3 (`UR 3,9`, `PH 1,4`, `SI 1,4`, `SV 1,4`) where one ancestral chromosome is inserted into the interior of another segmented chromosome, explaining the karyotypic reduction from $x = 9$ to $x = 8$ in *M. maximus*.

#### WEAKNESSES & METHODOLOGICAL AUDIT
- **Redundant cross-reference calls of the same underlying *M. maximus* restriction-site SNPs:** Because the same *M. maximus* GBS reads were aligned independently to four conserved reference genomes (*U. ruziziensis*, *P. hallii*, *S. italica*, *S. viridis*) and pooled into the final 7,095-marker map (Table 5: 2,134 from *U. ruziziensis*, 1,765 from *S. viridis*, 1,713 from *S. italica*, 1,483 from *P. hallii*), an orthologous *Pst*I GBS tag that maps to conserved exons in all four reference genomes will be called up to four times as distinct markers. While the authors removed exact dosage-identical redundant markers ($10.13\%$ overall, $863$ across genomes), any slight difference in missingness ($<20\%$) or a single individual's read-depth across alignments causes the same physical *M. maximus* locus to be retained multiple times, inflating unique marker counts and contributing to the local ordering noise and map inflation observed on Homology Group 3 ($324.41\ \text{cM}$).
- **Direct reliance on `GATK GenotypeGVCFs` for tetraploid dosage calling without specialized polyploid empirical Bayes priors:** While the $\text{DP} \ge 50\times$ filter substantially mitigates allele-dropout and overdispersion, standard `GATK` multinomial genotype likelihoods do not model GBS allele-bias or overdispersion as accurately as dedicated polyploid callers (`updog`, `fitPoly`, `polyRAD`), which likely explains why $59\%$ of variants ($28,827 \to 11,818$, Table 3) failed the Bonferroni-corrected Mendelian segregation distortion test ($p < 1.73 \times 10^{-6}$), with severe attrition of duplex and multiplex classes.
- **Arithmetic typo in Table 2 Total row and Table 4 marker class sum:**
  - In Table 2, the sum of the `Variants` column across the 6 rows ($866,361 + 550,295 + 542,114 + 671,353 + 765,041 + 770,317$) is $4,165,481$, whereas the `Total` row prints `5131,997`; similarly, the sum of `Variants (AQCF)` across the 6 rows is $58,480$, whereas the `Total` row prints `79,534`.
  - In Table 4, for each Homology Group, the sum of `Simplex + D-simplex + Multiplex` equals the non-redundant skeletal markers ($6,114 + 156 + 128 = 6,398$ total), while the `Total` column ($7,095$) includes the $697$ re-inserted redundant markers without a separate column header explaining the $697$-marker difference.

### 3. Biological / Experimental Grounding & Claim Proportionality
- **Claim that *M. maximus* exhibits $x = 8$ homology groups with strictly polysomic (random bivalent) inheritance and no preferential pairing:** `[Well Supported]` — Directly supported by the 8 linkage groups and meiotic pairing configuration probabilities ($\approx 0.33$) across all homologs.
- **Claim that Homology Group 3 reflects an evolutionary fusion/insertion of two ancestral $x = 9$ Panicoid chromosomes:** `[Well Supported]` — Independently corroborated across four orthologous reference genomes (`UR 3,9`, `PH 1,4`, `SI 1,4`, `SV 1,4`).
- **Claim that *Urochloa ruziziensis* is the closest genomic reference among tested grasses:** `[Well Supported]` — Supported by the highest read mapping rate ($49.84\%$) and highest number of quality-filtered variants ($12,549$).

### 4. Reproducibility & Data Completeness
The authors provide an interactive R Shiny web application (`https://statgen.esalq.usp.br/megathyrsus-map/`) containing the phased linkage maps and parental haplotypes, and explicitly document all software versions (`Bowtie2 v2.1.0`, `GATK v4.1.6.0`, `AGHmatrix v2.0.0`, `MAPpoly v0.2.3`) and command-line/filtering parameters. However, an NCBI SRA BioProject accession number for the raw GBS FASTQ files is not stated in the manuscript text.
</Blinded Review: TIME_ANON_0973>
