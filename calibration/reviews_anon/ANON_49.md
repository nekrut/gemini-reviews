# Review of ANON_49

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **9.1 / 10.0** (Exemplary) | **Scientific Core Score:** **7.2 / 8.0**  
**Overall Score:** 9.1 / 10.0  
* **Score Breakdown:** Rigor: 3.1/3.5 | Claims: 2.2/2.5 | Biology: 1.9/2.0 | Reproducibility: 1.9/2.0  
**Score Breakdown:** Methodological Rigor: 3.1/3.5 | Claim-Evidence Alignment: 2.2/2.5 | Biological Plausibility: 1.9/2.0 | Reproducibility: 1.9/2.0  
**Verdict:** Exemplary

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT (Executive Summary)

This foundational genomic resource manuscript presents the GENCODE 7 reference gene annotation of the human genome, integrating manual curation by HAVANA, automated gene building by Ensembl (`HavanaAdder` merge), and targeted experimental validation via multiplexed RT-PCR-seq, CAGE, polyA-seq, comparative genomics (`PhyloCSF`), protein structural/functional conservation (`APPRIS`), and tandem mass spectrometry (`X!Tandem` against PeptideAtlas/GPM). GENCODE 7 catalogs 20,687 protein-coding loci (140,066 transcripts, including 33,977 CDSs absent from RefSeq and UCSC), 9,640 long noncoding RNA (lncRNA) loci (15,512 transcripts), 8,801 small ncRNAs, and 11,224 manually curated pseudogenes (7,183 Level 1 three-way consensus pseudogenes and 934 transcribed pseudogenes). Targeted RT-PCR-seq across eight human tissues validates 82% of 5,871 tested low-confidence splice junctions (5$\times$ higher sensitivity than deep unstranded RNA-seq) and 73% of novel Illumina Human Body Map 2.0 (HBM) transcript models (confirming 1,168 novel loci), while mass spectrometry at 1% target-decoy FDR maps 83,054 tryptic peptides to 8,098 protein-coding genes (39.1%) and detects alternative isoform translation at 194 loci. All annotations and evidence tracks are publicly available via `gencodegenes.org`, Ensembl, and the UCSC Genome Browser.

GENCODE 7 represents a gold-standard, multi-tiered genomic resource backed by rigorous manual curation rules, automated consistency checks (`AnnoTrack`), and orthogonal wet-lab validation. Its primary technical caveats are: (1) first-pass manual curation was completed on only 18 of 24 chromosomes in release 7 (leaving chromosomes 14–19 dependent on Level 3 automated annotation, which induces chromosome-level ascertainment skew for lncRNAs and alternative isoforms), (2) 85% of lncRNA 5' ends and 83.2% of lncRNA 3' ends lack CAGE/polyA support, meaning the sharp two-exon modal peak reported for lncRNAs (Fig. 2) remains partially sensitive to 5'/3' terminal exon truncation, and (3) the proteomics method combines per-experiment `X!Tandem` $P$-values across repositories without specifying the mathematical combination formula or controlling for correlated decoy hits across repeated spectra. These caveats can be clarified through explicit methodological documentation and chromosome-stratified summary statistics.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT (Detailed Rubric Evaluation)

* **Combining HAVANA manual genomic curation with Ensembl automated annotation and targeted RT-PCR-seq yields the most comprehensive, high-accuracy catalog of human coding transcripts, lncRNAs, and pseudogenes (Figs. 1, 4, 7, 8): [Well Supported].**  
  By curating directly on the finished reference genome rather than full-length cDNAs alone, GENCODE captures 33,977 unique coding sequences outside RefSeq/UCSC while flagging partial transcripts (`start_not_found` / `end_not_found`) and classifying evidence into Levels 1–3. Targeted RT-PCR-seq across 8 tissues confirms 82% of 5,871 tested splice junctions, outperforming 5-billion-read unbiased RNA-seq (16% detection on single-transcript junctions) by $5\times$ for low-abundance isoforms.

* **Human lncRNAs exhibit a distinct two-exon modal structure and low evolutionary coding potential, whereas few unannotated conserved protein-coding loci remain in the human genome (Sections "Analyzing long noncoding transcript annotation" & "Assessing coding potential of RNA-seq models using PhyloCSF", Fig. 2): [Moderately Supported].**  
  Screening 3,689 novel intergenic HBM RNA-seq loci with `PhyloCSF` across 33 placental mammals yields only 5 manually confirmed novel coding genes (plus 9 from `Scripture`), strongly supporting the conclusion that the conserved human protein-coding gene catalog is near completion. However, because only 15% of GENCODE lncRNA TSSs and 16.8% of 3' ends are supported by CAGE and polyA features, the conclusion that the two-exon distribution of lncRNAs is a bona fide biological property rather than an assembly/truncation artifact is only moderately supported: short-read HBM assemblies (`Exonerate` / `Scripture`) used for corroboration are themselves prone to fragmenting multi-exonic low-abundance transcripts at GC-rich or repetitive junctions.

* **Nearly 60% of alternative translated isoforms lose functional domains, structural integrity, or catalytic residues relative to the constitutive `APPRIS` principal isoform, while ~40% of coding loci have mass-spectrometry peptide support (Sections "Analyzing the protein-coding complement..." & "Assessing coding potential... using mass spectrometry data"): [Well Supported].**  
  `APPRIS` structural and Pfam domain mapping across 84,408 translated transcripts demonstrates that 59.9% of alternative isoforms (and 79.5% of NMD-predicted isoforms) alter or lose conserved domains/residues. At the protein level, 83,054 peptides at 1% target-decoy FDR map uniquely to 8,098 coding genes, validating 83 "novel"/"putative" transcripts and 8 NMD-candidate isoforms, though the exact $P$-value combination formula across PeptideAtlas/GPM experiments should be stated in Methods.

* **Multi-pipeline consensus and RT-PCR-seq identify 7,183 Level 1 pseudogenes and hundreds of locus-specific transcribed pseudogenes (Section "Integration of pseudogenes into GENCODE", Fig. 3): [Well Supported].**  
  Cross-validating `PseudoPipe` (18,046), `RetroFinder` (13,644), and HAVANA manual curation (11,224) establishes a 7,183-locus Level 1 consensus set, with 63 of 162 tested transcribed pseudogene candidates confirmed by RT-PCR-seq across 8 tissues.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT (Major Issues, Minor Issues, Concrete Recommendations)

#### Major Issues
1. **Incomplete Manual Annotation on Chromosomes 14–19 Creates Chromosome-Level Ascertainment Bias (Section "Evolution of the GENCODE gene set", Figs. 5, 8):** Because HAVANA had completed first-pass manual curation on only 18 chromosomes in GENCODE 7 (leaving chr14–19 without full manual curation), Level 2 lncRNAs, pseudogenes, and alternative splice variants are severely depleted on chr14–19 (clearly visible in the chromosome-stratified bars of Fig. 5 and Fig. 8B). Downstream users performing genome-wide window or chromosome enrichment analyses on GENCODE 7 could mistake this curation boundary for biological depletion if not prominently warned.
2. **Unspecified Multi-Experiment $P$-Value Combination Rule in Mass Spectrometry Validation (Section "Assessing coding potential of putative models using mass spectrometry data"):** The text states that peptide $P$-values were generated "by combining the X!Tandem $P$-values for each individual experimental peptide-spectrum match, and a target-decoy approach is used to determine false-discovery rates," referring to an unpublished manuscript ("in prep."). Combining raw PSM $P$-values (e.g., via Fisher's method or Stouffer's Z) across dozens of experiments without accounting for repeated non-independent fragmentation spectra of common contaminants/homologs can inflate multi-experiment false positives unless the decoy distribution is subjected to the identical multi-experiment aggregation procedure.

#### Minor Issues
1. **Inconsistent Protein-Coding Locus Counts Between Abstract/Main Text and Proteomics Section:** The Abstract states that GENCODE 7 contains `20,687` protein-coding loci, whereas the mass spectrometry section (line 165) states that peptides mapped to `8,098 of the 20,700 annotated protein-coding genes`.
2. **Exon-Count Peak Discrepancy Between Text Sections (Lines 59 vs. 103):** Line 59 states that lncRNA and protein-coding exon distributions peak "at two and five exons, respectively (see Fig. 2)", whereas line 103 states "Transcripts annotated at protein-coding loci demonstrate a peak at four exons per transcript, while lncRNAs... with a distinct peak at two exons." Inspection of Fig. 2 should be reconciled to report the exact mode (4 vs. 5 exons).
3. **Minor Typos:** Line 73 ("pseuodgene decorated resource") and Chunk 2 Line 44 ("12.5 $\mu$Ll").

#### Concrete Recommendations

#### 1. Explicitly Flag Chromosomes 14–19 in Genome-Wide Summary Statistics and Completeness Analyses
* **WHY:** Including the 6 manually unannotated chromosomes (chr14–19) in genome-wide averages of lncRNA density, transcripts per locus, and polyA coverage dilutes the metrics of the manually curated set and creates artificial inter-chromosomal variance.
* **WHAT:** Report key GENCODE 7 summary statistics (transcripts per coding locus, lncRNA density per Mb, and % polyA/CAGE support) stratified by the 18 manually completed chromosomes versus chr14–19, and mark chr14–19 with an asterisk in Figures 5 and 8.
* **HOW:** Add a column to Supplemental Table 4 / Table 6 reporting metrics restricted to the 18 manually curated chromosomes alongside the whole-genome totals, and update the captions of Figs. 5 and 8.

#### 2. Test Whether the Two-Exon lncRNA Peak Persists in the Subset of Full-Length (5'-CAGE + 3'-polyA Supported) lncRNAs
* **WHY:** Because ~85% of annotated lncRNAs lack 5' CAGE and 3' polyA support, the two-exon modal peak in Fig. 2 could be inflated by incomplete 5'/3' terminal exon annotation.
* **WHAT:** Plot or report the exon-count distribution specifically for the subset of GENCODE 7 lncRNA transcripts that have both 5' CAGE cluster overlap and 3' polyA support.
* **HOW:** Filter the 15,512 lncRNA transcripts to those validated at both termini (the ~15–16.8% subset described on line 59) and compare their median and modal exon counts against the full lncRNA catalog in Figure 2.

#### 3. Document the Exact Proteomics $P$-Value Combination and Target-Decoy Aggregation Protocol in Methods
* **WHY:** Because the proteomics validation paper is cited as "in prep.", the current manuscript must provide enough mathematical detail in the Methods section for readers to verify the 1% peptide-level FDR calculation.
* **WHAT:** Add a "Mass spectrometry validation" subsection to the Methods detailing the `X!Tandem` search parameters (mass tolerances, cleavage rules, decoy database construction), the exact mathematical formula used to combine PSM $P$-values across experiments, and how peptide-level 1% FDR was enforced.
* **HOW:** Write out the multi-experiment score combination equation and confirm that decoy peptides were aggregated across experiments identically to target peptides before applying the 1% FDR cutoff.

#### 4. Reconcile Numerical Discrepancies and Fix Typos
* **WHY:** Exact numerical consistency across sections is essential for a reference annotation paper.
* **WHAT & HOW:**
  1. Reconcile the coding gene count (`20,687` on line 5 vs. `20,700` on line 165).
  2. Reconcile the modal exon number for protein-coding transcripts (`five exons` on line 59 vs. `four exons` on line 103).
  3. Fix `pseuodgene` to `pseudogene` (line 73) and `12.5 μLl` to `12.5 μL` (Methods, "Amplification and sequencing").
