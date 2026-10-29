<Blinded Review: TIME_ANON_0630>
**Composite Score:** 6.4 / 10.0 (Rigor: 2.0/3.5 | Claims: 1.6/2.5 | Biology: 1.2/2.0 | Reproducibility: 1.6/2.0)
**Bias Category:** Statistical/Design
**Verdict:** Major Revision
**Study Modality:** Hybrid Computational + Wet-Lab
**Technology Maturity:** Mid-Stage High-Throughput
**Epistemic Stage:** Basic/Mechanistic Discovery

OVERALL_SCORE: 6.4/10
VERDICT: CAVEATS
ESTIMATED_DECADE: 2010s

---

### SUMMARY / 1. Executive Summary
This study profiles the transcriptomic and alternative splicing response of human hepatoblastoma HepG2 cells (cultured in lipoprotein-deficient serum) to 10 µM atorvastatin for 24 hours ($n=3$ biological/technical replicate wells per group) using paired-end Illumina RNA-seq (2x100 bp, ~25M reads/sample) and Affymetrix Human Exon 1.0 ST arrays, with RT-qPCR validation of *HMGCR* and *IL21R*. While RNA-seq (analyzed via TopHat/Cufflinks/Cuffdiff at 5% FDR) identifies 121 differentially expressed genes (strongly enriched for cholesterol/mevalonate biosynthesis), 98 differentially expressed splice variants, 11 differentially spliced genes, and 1 gene with differential promoter usage (*RAP1GAP*), the Exon 1.0 ST array detects zero differentially expressed genes after Benjamini-Hochberg correction. The study is well-deposited (GEO GSE57071, BioSample SAMN02808181–86), transparently reports its small sample size ($n=3$), and confirms canonical statin targets, but suffers from low statistical power for isoform-level deconvolution, unvalidated splice variant calls, and several internal numerical/sign inconsistencies in the tables.

### STRENGTHS
- **Appropriate physiological pre-conditioning:** Culturing HepG2 cells in lipoprotein-deficient serum (LPDS) coupled with an initial 6-point dose-response curve (0 to 40 µM atorvastatin, $n=4$ independent experiments) ensured that 10 µM lay in the linear dynamic range of *HMGCR* induction (1.7-fold).
- **Direct platform comparison on matched RNA:** Running both RNA-seq and Affymetrix Human Exon 1.0 ST arrays on the exact same RNA samples clearly illustrates the dynamic range compression of exon microarrays (fold-change range $-1.6$ to $+1.9$, 0 FDR-significant genes) relative to RNA-seq (121 FDR-significant genes, $R = 0.81$ global correlation).
- **Data availability:** Both exon array data (GSE57071) and raw sequence reads (SAMN02808181–SAMN02808186) are deposited in public repositories.

### WEAKNESSES & METHODOLOGICAL AUDIT / 2. Methodological & Statistical Audit
- **Internal inconsistencies and sign inversions in Table 3 and Table 2:**
  - In **Table 3** ("The 11 genes uniquely identified by differential expression analysis of transcript splice variants"), the reported fold-change signs are inverted relative to the FPKM columns (`FPKM Atv` vs `FPKM Ctr`) and contradict the text and Figure 2:
    - For *BCL2L11* (`NM_138621`), Table 3 lists `FPKM Atv = 3.9`, `FPKM Ctr = 2.0`, and `Fold Change = -2.0`. Yet the text (line 173) and Figure 2 legend (line 135) state that `NM_138621` was **downregulated** upon atorvastatin treatment! This means either the `FPKM Atv` and `FPKM Ctr` column headers in Table 3 are swapped, or the fold-change signs are inverted across the entire table (e.g., *ZNF195* has Atv 3.6 vs Ctr 1.6 with FC `-2.3`; *MICA* has Atv 11.8 vs Ctr 17.1 with FC `+1.5`; *C10orf58* has Atv 42.7 vs Ctr 51.3 with FC `+1.2`).
    - Furthermore, 5 of the 11 transcripts in Table 3 (*DTNA*, *PLCXD2*, *ZNF419*, *SP1*, *ZNF674*) have `FPKM = 0.0` in one condition and tiny FPKM values (`0.5` to `1.3`) in the other, with `Fold Change = N/A`. Calling differential isoform expression on transcripts with 0.0 vs 0.5 FPKM at ~25M reads in $n=3$ wells is highly prone to Cufflinks multi-mapping/EM deconvolution artifacts.
  - In **Table 2**, row 3 ("Cholesterol Biosynthesis III (via Desmosterol)") reports a ratio of `2/13 (0.92)` with $p = 5.46 \times 10^{-25}$—clearly a typo for `12/13 (0.92)`.
- **Pseudoreplication vs. biological replication ambiguity:** Methods (line 28) state that for the dose-response curve, cells were treated in "four independent experiments," whereas for the RNA-seq and exon array experiments, "cells were treated with or without 10 µM atorvastatin for 24 hours in triplicate wells." Triplicate wells seeded simultaneously on a single 12-well plate represent technical/well replicates rather than independent biological passages, which underestimates biological variance and inflates Cuffdiff significance.
- **No experimental validation of any novel splice variants:** Despite the paper's title and focus on atorvastatin-responsive splice variants, RT-qPCR validation was performed on only two genes at the total gene level (*HMGCR* and *IL21R*). None of the 11 differentially spliced genes (*SYCP3*, *ZNF195*, *MYD88*, etc.), the 4 minor splice variants (*ZNF195*, *SP1*, *DTNA*, *FAM189B*), or the *BCL2L11* / *RAP1GAP* isoforms were validated by isoform-specific RT-qPCR.
- **Failure of Exon Array analysis to examine exon-level splicing:** Although the authors used the Affymetrix Human Exon 1.0 ST Array (~4 probes per exon), they collapsed all core probes to a single gene-level average in Partek (line 43) and never performed exon-level ANOVA/FIRMA/SI splicing analysis on the array data to cross-check the RNA-seq splicing calls.

### 3. Biological / Experimental Grounding & Claim Proportionality
- **Claim 1:** 10 µM atorvastatin strongly upregulates the mevalonate and cholesterol biosynthesis pathway (12/13 pathway genes) in LPDS-cultured HepG2 cells `[Well Supported]`.
- **Claim 2:** *IL21R* mRNA is upregulated by atorvastatin in HepG2 cells, detectable by RNA-seq (4.1-fold) and TaqMan RT-qPCR (7.1-fold) despite low baseline abundance (FPKM 0.74) that escaped detection on the exon array `[Moderately Supported]`.
- **Claim 3:** Atorvastatin specifically alters the alternative splicing patterns of 11 genes and expression of 4 minor splice variants (*DTNA*, *SP1*, *ZNF195*, *FAM189B*) `[Fragile]` — relies entirely on unvalidated Cuffdiff isoform deconvolution at low FPKM (0.0 to 1.3) in $n=3$ replicate wells, with swapped FPKM/fold-change columns in Table 3.

### 4. Reproducibility & Data Completeness
- **Data Accessions:** Exon array data deposited in GEO (`GSE57071`); RNA-seq reads deposited in NCBI BioSample (`SAMN02808181`–`SAMN02808186`).
- **Assay Identifiers:** TaqMan assay IDs explicitly provided (`Hs01102990_m1`, `Hs00222310_m1`, `Hs99999904_m1`, `Hs99999910_m1`).
- **Software & Parameters:** Genome build (`hg19`) and tools (`Bowtie/TopHat`, `Cufflinks/Cuffdiff`, `CummeRbund`, `Partek Genomics Suite`) are named, though exact software version numbers and TopHat/Cuffdiff command-line parameters are not specified.
</Blinded Review: TIME_ANON_0630>
