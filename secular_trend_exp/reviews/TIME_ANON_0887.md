<Blinded Review: TIME_ANON_0887>
**Composite Score:** 3.4 / 10.0 (Rigor: 0.9/3.5 | Claims: 0.8/2.5 | Biology: 0.9/2.0 | Reproducibility: 0.8/2.0)
**Bias Category:** Technical/Assay
**Verdict:** Reject (Fundamental Flaws)
**Study Modality:** Hybrid Computational + Wet-Lab
**Technology Maturity:** Mid-Stage High-Throughput
**Epistemic Stage:** Translational/Preclinical/Biomarker

OVERALL_SCORE: 3.4/10
VERDICT: FAILED
ESTIMATED_DECADE: 2020s

---

### 1. Executive Summary / SUMMARY
This study attempts to characterize the chromosomal integration sites, copy number, and amino acid homology of porcine endogenous retrovirus (PERV) subtypes (PERV-A, PERV-B, PERV-C, and recombinant PERV-CA) across three pig breeds—Jeju native pigs (JNPs, $n=3$), Duroc ($n=3$), and Landrace ($n=3$)—using 30x Illumina NovaSeq 6000 whole-genome resequencing (WGR) aligned to the *Sus scrofa* 11.1 reference genome (`GCF_000003025.6`), supplemented by subtype-specific PCR and Sanger sequencing on ear tissue DNA. While PERV surveillance in donor pig breeds is important for xenotransplantation biosafety, a forensic audit of the bioinformatic pipeline and experimental methods reveals fundamental methodological flaws and blatant internal contradictions between the Materials and Methods and Results sections.

### 2. Methodological & Statistical Audit / STRENGTHS & WEAKNESSES & METHODOLOGICAL AUDIT

#### STRENGTHS
- **Relevant comparative cohort:** Samples three individuals each from an isolated native breed (Jeju native pig) alongside two major commercial breeds (Duroc and Landrace) at 30x WGR depth.
- **Combined NGS and PCR screening:** Uses wet-lab PCR and Sanger sequencing of PERV-C *env* amplicons to detect PERV-C sequences missed by the reference-based WGR pipeline.

#### WEAKNESSES & METHODOLOGICAL AUDIT
- **Fatal Bioinformatic Flaw — Detecting polymorphic non-reference ERV insertions by simple reference mapping (`Bowtie2` against *S. scrofa* 11.1):**
  - Endogenous retroviruses are ~9 kb mobile genetic elements whose integration sites are highly polymorphic across individuals and breeds. Above all, the *Sus scrofa* 11.1 reference genome (`GCF_000003025.6`) was assembled from a single Duroc female and lacks PERV-C loci as well as breed-specific PERV insertions present in Jeju native pigs!
  - Simply aligning 2x150 bp paired-end reads to *S. scrofa* 11.1 with `Bowtie2` and calling SNPs/indels with `GATK` (requiring $\text{MAF} \le 0.05$ across only $n=9$ pigs, i.e., 18 chromosomes, where a singleton allele has $\text{MAF} = 1/18 = 0.056 > 0.05$!) cannot discover non-reference proviral insertions without split-read / discordant-mate mobile element insertion (MEI) callers or *de novo* assembly.
  - Furthermore, applying `QUAST` and `BUSCO` (lines 9, 41)—tools designed to evaluate *de novo* genome assemblies—to raw reads or reference-mapped BAM files is bioinformatically nonsensical.
- **Blatant contradiction in PCR amplicon sizes between Methods and Results:**
  - In Materials and Methods (line 50), the authors state: *"The amplicon sizes for PERV-A, -B, -C, and -A/C were approximately 650, 720, 550, and 800 bp, respectively."*
  - In Results (line 82), the authors state: *"PCR amplification was performed using subtype-specific primers, which generated distinct amplicons corresponding to PERV-A (1,157 bp), PERV-B (167 bp), PERV-C (244 bp), and PERV-CA (1,380 bp)."* Every single amplicon size in the Results contradicts the Materials and Methods!
- **Contradictory statements within the text regarding PERV-A homology and PERV-C presence:**
  - In line 65, the authors write: *"The high homology observed in the pol, env, and gag regions of PERV-A exhibited low sequence homology across all breeds compared with the reference genome."* This sentence directly contradicts itself within a single clause ("high homology... exhibited low sequence homology").
  - In the Discussion (line 91), the authors first state that *"PERV C was undetectable"* and *"Because PERV-C does not infect human-derived cell lines, pigs harboring PERV-C may offer advantages as xenotransplantation models"*, and then four sentences later (line 95) state the exact opposite: *"Given that PERV-C is associated with recombination risks and increased zoonotic transmission potential, its absence in JNPs, Duroc, and Landrace pigs may be advantageous for xenotransplantation"*, immediately followed by *"while PERV-C was detected in some Western breeds and all three JNPs analyzed."*
- **Misinterpretation of PERV-CA in germline genomic DNA:** PERV-A/C (PERV-CA) recombinants typically arise somatically in infected tissues/PBMCs rather than as fixed germline proviruses in *S. scrofa* 11.1, and cannot arise in the absence of PERV-C; claiming abundant germline PERV-CA insertions in WGR while simultaneously claiming PERV-C is absent from the WGR data reflects misclassification of reference PERV-A/B elements.
- **qRT-PCR described in Methods but never reported in Results:** Line 50 describes SYBR Green qRT-PCR with melt-curve analysis, yet no quantitative Ct values, copy numbers, or qRT-PCR data appear anywhere in the Results.

### 3. Biological / Experimental Grounding & Claim Proportionality
- **Claim 1:** WGR identified 24 PERV insertions in JNPs, 18 in Duroc, and 15 in Landrace, with PERV-C absent in all breeds by WGR. `[Methodologically Flawed]` — Artifact of aligning short reads to a single Duroc reference assembly (*S. scrofa* 11.1) without split-read/discordant-pair mobile element insertion calling, as proven by the authors' own PCR finding that all three JNPs are PERV-C positive.
- **Claim 2:** PCR and Sanger sequencing of the 244 bp *env* fragment confirm PERV-C presence in all 3 JNPs and some Western pigs. `[Moderately Supported]` — Supported by gel and Sanger alignment, though contradicted by the 550 bp amplicon size stated in Methods.

### 4. Reproducibility & Data Completeness
- **Missing Data:** No NCBI SRA / BioProject accession numbers are provided for the 900 Gb of NovaSeq 6000 WGR data or the Sanger sequences, and the tables/figures referenced in the text are not embedded with raw coordinates.
</Blinded Review: TIME_ANON_0887>
