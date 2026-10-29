<Blinded Review: TIME_ANON_0569>
**Composite Score:** 6.8 / 10.0 (Rigor: 2.3/3.5 | Claims: 1.8/2.5 | Biology: 1.6/2.0 | Reproducibility: 1.1/2.0)
**Bias Category:** Statistical/Design
**Verdict:** Major Revision
**Study Modality:** Hybrid Computational + Wet-Lab
**Technology Maturity:** Mid-Stage High-Throughput
**Epistemic Stage:** Translational/Preclinical/Biomarker

OVERALL_SCORE: 6.8/10
VERDICT: CAVEATS
ESTIMATED_DECADE: 2020s

---

### 1. Executive Summary (SUMMARY)
This applied plant breeding and genomics study reports the marker-assisted backcross breeding (MABB) introgression and pyramiding of two blast resistance genes, *Pi9* (from donor IRBL9W) and *Pi54* (from donor DHMAS 70Q 164-1b), into the blast-susceptible temperate aromatic rice landrace Mushk Budji (MB). Using foreground gene-based markers (*Pi9-Pro* and *Pi54 MAS*), SSR/KASP background selection (~1,502 KASP markers), and Illumina NovaSeq X whole-genome resequencing (15,463 SNPs across 369.43 Mbp), the authors develop near-isogenic and two-gene pyramided lines ($BC_2F_{2:3}$ / $BC_2F_{4:6}$) achieving 84.0%–93.5% recurrent parent genome (RPG) recovery while retaining favorable alleles at *BADH2*, *Wx*, *Rc*, *GS3*, *Hd1/Hd4/Hd5*, and *COLD1/COLD6*. While the breeding execution and allelic validation are solid, the manuscript exhibits several internal numerical inconsistencies, post-hoc statistical grouping errors in Table 1, under-replicated multi-environment yield trials (2 replications per site without a published yield table or ANOVA), and incomplete reporting of multi-location field blast scores and raw sequencing accessions.

### 2. Methodological & Statistical Audit (WEAKNESSES & METHODOLOGICAL AUDIT)
* **Post-Hoc Multiple Comparison Letter Errors and Missing Entries in Table 1:** In Table 1 ("Mean performance of pyramided lines for physico-chemical and cooking quality traits"), the gel consistency (GC) of donor DHMAS 70Q 164-1b is reported as `55.00 ± 0.60 c`, sharing the same letter group `c` as Mushk Budji (`89.00 ± 1.19 c`) and the pyramided lines (`82.75 c` to `92.75 c`), while IRBL9W (`69.25 ± 0.76 b`) is assigned group `b`. It is mathematically impossible for 55.00 and 92.75 to share the same non-significant post-hoc letter group while 69.25 is significantly different from both. Furthermore, the ASV entry for DHMAS 70Q 164-1b (row 12) is left blank, and its Aroma score is listed as `5` without defining the sensory panel scale.
* **Discrepancy Between Multi-Location Blast Nursery Methods and Reported Results:** In Materials and Methods ("Evaluation for blast disease resistance under field conditions"), the authors state that the pyramided lines were screened in the Uniform Blast Nursery across five hotspot locations (Khudwani, Kulgam, Wadura, Sagam-1, and Sagam-2) for leaf and neck blast. However, Results ("Disease reaction of PLs") and Table 2 report field hotspot disease scores from only a single location (Khudwani), with no neck blast data, no multi-location breakdown, and no replication variance.
* **Omission of Quantitative Grain Yield Data and Multi-Environment ANOVA:** The multi-location trial across 5 environments (E1–E5) used a randomized block design with only two replications per environment. Although GGE biplots (Fig. 6) and genotype rankings are discussed extensively, the actual grain yield values (g/plant or t/ha), standard errors, genotype main effects ($G$), environment effects ($E$), and $G \times E$ interaction statistics are never presented in any main-text table.
* **Internal Inconsistencies in Marker Counts and Gene Nomenclature:** The genome-wide KASP marker panel is cited as `>1500` in the Abstract, `1502` in Methods and Results, and `1,501` in the Discussion. Foreground marker names alternate between `Pi9-Pro`, `AP5659/Pi9-Pro`, and `Pro-9`. Similarly, the fragrance and pericarp retention exceptions are inconsistently stated in the Results/Discussion: the text states that all PLs except `SKUA-528-50-1-1-19-2-13` (a single-gene *Pi9* NIL) possessed the 8-bp *BADH2* deletion and white pericarp *Rc* allele, yet Table 1 lists `SKUA-528-50-1-1-19-2-13` (row 8) as having an Aroma score of `2`, identical to aromatic Mushk Budji.
* **Bioinformatic Pipeline Versioning Mismatch:** The methods state that Illumina NovaSeq X reads were demultiplexed with `FASTX Toolkit (v0.0.13)`, checked with `FastQC (v0.11.8)`, and aligned with `BWA (v0.7.5)`, but do not specify the variant caller (e.g., GATK/bcftools), read depth/coverage per line, or quality filtering thresholds used to obtain the 15,463 SNPs with MAF > 40%.

### 3. Biological / Experimental Grounding & Claim Proportionality (STRENGTHS)
* **Introgression of *Pi9* and *Pi54* with High RPG Recovery: `[Well Supported]`**  
  Foreground PCR, carrier-chromosome graphical genotyping delimiting a 3.07 Mb donor segment around *Pi9* on chromosome 6 and a 0.9 Mb donor segment around *Pi54* on chromosome 11, and whole-genome SNP profiling confirm successful gene pyramiding with ~89%–93% RPG recovery in the top two-gene lines.
* **Seedling and Hotspot Leaf Blast Resistance of Pyramided Lines: `[Well Supported]`**  
  Controlled mist-chamber inoculations with diagnostic *M. oryzae* isolates `Mo-nwi-kash-32` and `SKUA-Mo-3` and Uniform Blast Nursery screening at Khudwani demonstrate scores of 0–1 for *Pi9+Pi54* pyramids compared to 5 (controlled) and 7–9 (field) for susceptible Mushk Budji (Table 2).
* **Sequence-Level Retention of Grain Quality and Adaptive Alleles: `[Moderately Supported]`**  
  Resequencing verification across *Wx^in*, *BADH2* (8-bp exon 7 deletion), *Rc* (14-bp exon 6 deletion), *GS3*, *LABA1*, *Hd1/Hd4/Hd5*, and *COLD1/COLD6* provides biologically coherent grounding for the retention of short-bold kernel morphology, low amylose (~16%), and temperate adaptation in the selected pyramids, aside from the unresolved *BADH2*/*Rc* genotype-phenotype discrepancy in line `SKUA-528-50-1-1-19-2-13`.
* **Durable Neck Blast Resistance and Multi-Ecology Yield Superiority: `[Overstated]`**  
  The Abstract claims validation of resistance to "both leaf and neck blast" across hotspot locations and superior yield across target ecologies, but neck blast scores and multi-site field blast data are absent from Table 2, and no formal yield table or statistical test of yield superiority over MB is presented in the main text.

### 4. Reproducibility & Data Completeness
* **Missing Raw Sequencing Accessions:** No NCBI Sequence Read Archive (SRA), BioProject, or ENA accession numbers are provided for the whole-genome resequencing data of Mushk Budji, the two donors, and the derived NILs/PLs.
* **Incomplete Phenotypic Tables:** Raw environment-wise yield and flowering date tables are absent from the main text, and Table 1 requires correction of the post-hoc letter groupings and missing cells.
</Blinded Review: TIME_ANON_0569>
