<Blinded Review: TIME_ANON_0636>
**Composite Score:** 6.8 / 10.0 (Rigor: 2.2/3.5 | Claims: 1.7/2.5 | Biology: 1.4/2.0 | Reproducibility: 1.5/2.0)
**Bias Category:** Statistical/Design
**Verdict:** Minor Revision
**Study Modality:** Hybrid Computational + Wet-Lab
**Technology Maturity:** Mid-Stage High-Throughput
**Epistemic Stage:** Basic/Mechanistic Discovery

OVERALL_SCORE: 6.8/10
VERDICT: CAVEATS
ESTIMATED_DECADE: 2010s

---

### SUMMARY / 1. Executive Summary
This study performs a genome-wide identification and characterization of the 14-3-3 gene family (`PvGF14s`) in common bean (*Phaseolus vulgaris* L.) using the Phytozome reference genome, identifying 9 loci (`PvGF14a–e, g, h, n, q`) distributed across 5 chromosomes. Phylogenetic and exon-intron structural analyses classify 5 genes into the $\epsilon$-like group (6–7 exons) and 4 into the non-$\epsilon$ group (4 exons), with each `PvGF14` clustering with two soybean (`GmSGF14`) co-orthologs ($K_a/K_s = 0.000\text{–}0.153$), reflecting the post-divergence whole-genome duplication in *Glycine max*. Using public Phytozome RNA-seq FPKM data, RT-PCR, and time-course qRT-PCR across cold ($4^\circ\text{C}$), drought (withholding water up to 9 days), and salinity (200 mM NaCl) treatments, the authors show that 8 of the 9 genes are transcribed (`PvGF14q` lacks ESTs and RT-PCR amplification, paralleling silent soybean orthologs `GmSGF14q/r`) and exhibit isoform- and stress-specific transcriptional responses. Finally, a yeast two-hybrid (Y2H) assay demonstrates that `PvGF14a` forms homodimers and heterodimers with all 7 other transcribed `PvGF14` isoforms. While the comparative evolutionary framing (1:2 syntenic relationship with soybean) and Y2H validation are solid, the qRT-PCR stress experiments rely on only $n=2$ biological replicates and use an unadjusted Fisher's LSD test across 6–7 time points.

### STRENGTHS
- **Coherent comparative evolutionary analysis with soybean:** The 1:2 orthology between the 9 *Phaseolus vulgaris* `PvGF14` genes and the 18 *Glycine max* `GmSGF14` genes—including the shared transcriptional silencing of the `PvGF14q` / `GmSGF14q/r` clade and strong purifying selection ($K_a/K_s < 0.16$)—is biologically well-grounded in legume paleopolyploidy (~19.2 MYA divergence followed by *Glycine*-specific WGD).
- **Experimental verification of cDNA sequences and protein dimerization:** Cloning all 8 expressed full-length cDNAs and testing `PvGF14a` in a yeast two-hybrid dilution series with proper empty-vector negative controls (Figure 6) confirms that the predicted ORFs encode functional dimerizing 14-3-3 proteins.

### WEAKNESSES & METHODOLOGICAL AUDIT / 2. Methodological & Statistical Audit
- **Underpowered biological replication ($n=2$) and liberal post-hoc testing in qRT-PCR:**
  - The legend to Figure 5 (line 129) states: "Error bars indicate SE of **two biological** and three technical replicates." Computing standard errors and running one-way ANOVA with $n=2$ biological replicates per time point provides extremely low statistical power and unstable variance estimates.
  - Furthermore, the authors used Fisher's Least Significant Difference (LSD) test (line 55) across 6 to 7 time points per stress condition without multiple-comparison correction (e.g., Dunnett's test against 0 h control or Tukey's HSD), inflating the false positive rate for small fold-changes (such as the 1.42- to 1.54-fold changes claimed as significant in salinity stress, line 133).
  - Unstressed parallel time-point controls (e.g., seedlings sampled at 1, 3, 6, 12, 24 h under normal temperature/watering to control for circadian/diurnal rhythm effects on 14-3-3 transcription) were not collected; all stress time points were normalized solely to the $t = 0$ control.
- **Ambiguous fold-change terminology for downregulated genes:** On line 131, the authors write: "the expression of *PvGF14e*, *PvGF14g* and *PvGF14h* was decreased to 5.3, 13.0 and 2.9 fold on 9, 7 and 5 days after treatment" (and similarly on line 133: "gradually decreased... maximum fold changes were up to 3.54, 1.97, 1.83 and 1.67"). Reporting a decrease to $1/5.3$ or $1/13.0$ of baseline as "decreased to 5.3, 13.0 and 2.9 fold" is mathematically imprecise (should be reported as decreased *by* 5.3-fold, or to 0.19, 0.08, and 0.34 of control levels).
- **Over-interpretation of ubiquitous short promoter motifs:** PlantCARE scans of 1.5 kb upstream sequences predict MYB drought-inducibility sites in *all 9* `PvGF14` genes and TC-rich repeats in 8 of 9 genes (line 135), yet several of these genes are strongly downregulated under drought (`PvGF14e`, `PvGF14g`, `PvGF14h`). Without functional promoter-reporter assays or statistical enrichment testing against genomic background, 4–6 bp motif occurrences in 1.5 kb windows are largely coincidental.

### 3. Biological / Experimental Grounding & Claim Proportionality
- **Claim 1:** The common bean genome encodes 9 `PvGF14` genes (5 $\epsilon$-like with 6–7 exons, 4 non-$\epsilon$ with 4 exons) that stand in a 1:2 orthologous relationship with soybean `GmSGF14` genes under strong purifying selection `[Well Supported]`.
- **Claim 2:** Only 8 of the 9 `PvGF14` genes are actively transcribed in common bean vegetative and reproductive tissues, whereas `PvGF14q` is transcriptionally silent or pseudogenized `[Well Supported]`.
- **Claim 3:** `PvGF14a` forms homodimers and heterodimers with all 7 other transcribed `PvGF14` isoforms in yeast two-hybrid assays `[Well Supported]`.
- **Claim 4:** Specific `PvGF14` isoforms are significantly upregulated or downregulated at specific time points of cold, drought, and salinity stress `[Moderately Supported]` — overall trends (such as drought induction of `PvGF14a` by 5.3-fold) are clear, but minor fold changes (1.4-fold) lack diurnal controls and rely on $n=2$ biological replicates with unadjusted LSD tests.

### 4. Reproducibility & Data Completeness
- **Gene Identifiers & Coordinates:** Phytozome locus tags (`Phvul.005G066600`, etc.), exact chromosomal coordinates, and NCBI EST accessions are fully tabulated in Table 1.
- **Primers & Supporting Data:** Gene-specific RT-PCR, qRT-PCR, and Y2H cloning primers, pairwise identity/Ka-Ks matrices, and tissue FPKM tables are provided in Supporting Information (`S1`–`S7 Tables`).
</Blinded Review: TIME_ANON_0636>
