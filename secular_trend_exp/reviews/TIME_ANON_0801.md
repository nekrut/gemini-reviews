<Blinded Review: TIME_ANON_0801>
**Composite Score:** 9.2 / 10.0 (Rigor: 3.1/3.5 | Claims: 2.3/2.5 | Biology: 1.9/2.0 | Reproducibility: 1.9/2.0)
**Bias Category:** None (Methodologically Sound)
**Verdict:** Minor Revision
**Study Modality:** Hybrid Computational + Wet-Lab
**Technology Maturity:** Mid-Stage High-Throughput
**Epistemic Stage:** Basic/Mechanistic Discovery

OVERALL_SCORE: 9.2/10
VERDICT: PASS
ESTIMATED_DECADE: 2010s

---

### 1. Executive Summary (SUMMARY)
This genome-wide association and fine-mapping study identifies the genetic architecture governing sea age at sexual maturation (1 sea-winter [1SW] vs. 3 sea-winters [3SW]) in male Atlantic salmon (*Salmo salar*). Using whole-genome Pool-seq ($12.32\times$ mean uniquely mapped read coverage per pool across 4,326,591 SNPs) of 240 PCR-sex-verified wild males (20 1SW and 20 3SW fish from the same smolt year class across each of six rivers in Western Norway), Cochran–Mantel–Haenszel (CMH) testing at a 0.1% false discovery rate ($p < 5.2 \times 10^{-8}$) reveals a major selective sweep on chromosome 25 containing 74 of the 138 genome-wide significant SNPs within a ~370-kb region spanning *chmp2b*, *vgll3*, and *akap11*. Individual Sequenom MassARRAY genotyping of 11 top SNPs validates the association in all 240 discovery individuals, replicates the haplotype effects in two independent wild smolt year classes from Eidselva ($n=28$) and Suldalslågen ($n=26\text{–}28$) ($44\%$ and $22\%$ variance explained), and fine-maps the signal in 97 domesticated Mowi salmon from four full-sib families reared under common-garden ambient-light sea-cage conditions down to a 2,386-bp haplotype spanning *vgll3* that includes two missense substitutions (Thr54Met and Lys323Asp) explaining 33–36% of phenotypic variance. Comparative sequencing across brown trout, rainbow trout, Arctic char, and a 10,000-year landlocked Swedish salmon population (Gullspång) establishes that the late-maturing 3SW allele (Thr54–Lys323) is ancestral.

### 2. Methodological & Statistical Audit (STRENGTHS, WEAKNESSES & METHODOLOGICAL AUDIT)
**Strengths:**
* **Cohort-Matched Multi-River Pool-Seq Design + Multi-Cohort Individual Validation:** Sampling 1SW and 3SW wild males originating from the *same* smolt migration year class across six replicate rivers controls for early freshwater/marine cohort environmental confounding, and the CMH test across six river strata isolates consistent allele-frequency divergence. Following up pooled sequencing with individual MassARRAY genotyping in (i) the 240 discovery fish, (ii) two independent wild year classes, and (iii) 97 common-garden domesticated fish across four pedigreed families provides three tiers of validation and leverages historical recombination in the domesticated strain to narrow the 370-kb wild sweep to 2.4 kb at *vgll3*.
* **Rigorous Handling of Salmonid Genome Duplication & Assembly Artifacts:** Because the Atlantic salmon genome is partially tetraploid (Ss4R whole-genome duplication), the authors enforce strict end-to-end `Bowtie2` mapping ($Q > 20$), manually audit ambiguously mapped reads at the two tandem paralogous *vgll3* loci on Chr 21 to confirm absence of trait-associated SNPs, and identify and correct a misassembled 16,885-bp contig containing exons 1–2 of *chmp2b* in assembly `AKGD00000000.4`.

**Weaknesses & Methodological Audit:**
* **Upward Bias (Winner's Curse) in Discovery Cohort Variance Explained:** In Results (line 33), the 1SW haplotype is reported to explain $54\%$ ($\beta = -1.0, p = 3.88 \times 10^{-40}$) of phenotypic variance in the 240 wild fish from the discovery year class. Because these 240 fish are the exact individuals used to select the top 11 SNPs from 4.33 million markers, in-sample $R^2$ is upwardly biased by selection; the out-of-sample replications in independent wild year classes ($44\%$ and $22\%$) and common-garden domesticated families ($33\text{–}36\%$) represent the unbiased effect size estimates.
* **Family Structure Accounting in PLINK Regression for Domesticated Sibships:** The 97 domesticated Mowi fish belong to four full-sib families ($n = 36, 24, 13, 24$). While parental genotypes were used to prevent Mendelian errors and phase haplotypes (line 58), the Methods state that association testing used *"a standard linear regression of phenotype on allele dosage (Wald test 1% FDR)"* in `Plink v1.8` (line 73) without specifying whether a family fixed effect or linear mixed model was included to account for within-family relatedness.
* **Minor Sample Count Discrepancy Between Results and Methods:** For the Suldalslågen replication year class, Results (line 38) reports `(13 1SW, 13 3SW)`, whereas Materials and Methods (line 56) reports `14 1SW and 14 3SW`.

### 3. Biological / Experimental Grounding & Claim Proportionality
* **Claim 1 (A single major locus on Chr 25 spanning *vgll3* explains a large fraction [33–54%] of phenotypic variance in male Atlantic salmon sea age at maturity across wild and domesticated populations): `[Well Supported]`** — Replicated across six wild rivers, multiple smolt cohorts, and common-garden aquaculture families.
* **Claim 2 (Two linked missense variants in *vgll3* [Thr54Met and Lys323Asp] within a 2.4-kb haplotype are top candidate variants, with the 3SW Thr–Lys allele being ancestral in salmonids): `[Well Supported]`** — Fine-mapped in the Mowi strain and polarized across *Salmo trutta*, *Oncorhynchus mykiss*, *Salvelinus alpinus*, and landlocked Gullspång salmon, while the authors appropriately caution that causality between the two missense SNPs and adjacent noncoding variants (including an upstream assembly gap) remains to be functionally dissected.
* **Claim 3 (Evolutionary conservation of *VGLL3* in vertebrate puberty timing): `[Moderately Supported]`** — Supported by prior human GWAS linking *VGLL3* to age at menarche/puberty and mouse data on *Vgll3* in adipogenesis and embryonic testis steroidogenesis, appropriately framed as a hypothesis for functional follow-up.

### 4. Reproducibility & Data Completeness
* **Exemplary Open Data & Parameter Reporting:** Raw Illumina HiSeq2000 Pool-seq reads for all 24 libraries are deposited in NCBI SRA (`PRJNA293012`), the full 4.33M SNP callset is hosted at `http://marineseq.imr.no/salmatsnp/`, exact `Bowtie2`, `SAMtools`, `PoPoolation2`, and `Plink v1.8` command parameters are documented, and all Sequenom MassARRAY primers and significant SNP coordinates are provided in Supporting Information Tables S1–S2.
</Blinded Review: TIME_ANON_0801>
