# Blinded Review: TIME_ANON_50
**Composite Score:** 4.6 / 10.0 (Rigor: 1.2/3.5 | Claims: 1.2/2.5 | Biology: 1.2/2.0 | Reproducibility: 1.0/2.0)
**Bias Category:** Uncorrected High-Dimensional Multiple Testing, Panel-Biased Pathway Circularity & Missing Raw Omics Data
**Verdict:** Reject
**Study Modality:** Wet-Lab Primary Experimental
**Technology Maturity:** Mid-Stage High-Throughput
**Epistemic Stage:** Translational/Preclinical/Biomarker

---

### 1. Executive Summary

This manuscript performs retrospective multi-omics profiling on archival formalin-fixed, paraffin-embedded (FFPE) pre-treatment tumor biopsies from stage III/IV melanoma patients treated with anti-PD-1 immune checkpoint blockade, stratified into "good responders" ($\text{PFS} > 365\ \text{days}$ or prolonged stable disease after pseudo-progression) and "poor responders" ($\text{PFS} < 180\ \text{days}$). The authors analyze $n = 19$ FFPE specimens (9 good vs 10 poor responders) by label-free LC–MS/MS proteomics with pooled fractionated spectral library matching (quantifying 4,958 proteins) and $n = 25$ FFPE specimens (14 good vs 11 poor responders) using the 549-gene HTG EdgeSeq Precision Immuno-Oncology targeted mRNA assay. Using an unadjusted $t$-test cutoff of $p < 0.05$, $\lvert\log_2\text{FC}\rvert \ge \log_2(1.5)$, and Hellinger distance $> 0.25$, they report 223 differentially expressed proteins and 40 upregulated transcripts, which are fed into Clarivate MetaCore for pathway/network enrichment and TIMER2.0 for in silico immune deconvolution. They conclude that IFN-$\gamma$-driven JAK/STAT and NF-$\kappa$B signaling and MHC class I/II antigen presentation predispose melanoma patients to respond to anti-PD-1 therapy.

While the biological conclusion—that pre-existing T-cell inflammation, IFN-$\gamma$ signaling, and MHC class I/II antigen presentation correlate with anti-PD-1 response in melanoma—is well established in the clinical immuno-oncology literature, the quantitative and statistical execution of this study suffers from three major methodological flaws: (1) complete absence of false discovery rate (FDR) correction when screening 4,958 proteins in $n = 19$ samples and 549 mRNAs in $n = 25$ samples, where the number of expected false positives at unadjusted $p < 0.05$ ($\sim 248$ proteins and $\sim 27$ mRNAs) equals or exceeds the number of "discoveries" (223 proteins and 40 mRNAs); (2) circular pathway enrichment and manual node injection in MetaCore (computing whole-genome hypergeometric $p$-values as extreme as $1.41 \times 10^{-104}$ and enriching for "immune processes" from a pre-selected 549-gene immuno-oncology panel, plus manually inserting unmeasured `IFN-γ` and `iNOS` nodes into the network); and (3) invalid application of whole-transcriptome bulk deconvolution algorithms (`TIMER2.0`, `xCell`, `EPIC`) to a 549-gene targeted panel.

---

### 2. Methodological & Statistical Audit

* **Uncorrected Multiple Hypothesis Testing Where Expected False Positives Exceed Reported Hits:**
  In Section 2.2 and Section 4.5, differential expression across the 4,958 quantified proteins ($n = 9$ vs $10$, $df = 17$) and 549 targeted mRNAs ($n = 14$ vs $11$, $df = 23$) is defined using an **unadjusted two-sample $t$-test $p < 0.05$** combined with a 1.5-fold change and Hellinger distance $> 0.25$.
  - Under the global null hypothesis across $M = 4,958$ proteins, an unadjusted $\alpha = 0.05$ threshold produces $4,958 \times 0.05 = 247.9$ false positives by random chance alone—more than the **223 differentially expressed proteins** reported in the study!
  - Similarly, across $M = 549$ mRNA transcripts on the HTG EdgeSeq panel, an unadjusted $\alpha = 0.05$ threshold produces $549 \times 0.05 = 27.5$ false positives by chance, accounting fornearly 70% of the **40 transcripts** reported!
  Furthermore, in Section 2.2 and Figure 1E, only **40 upregulated transcripts** (higher in good responders) are reported from the mRNA panel, with no accounting of downregulated transcripts in good responders. Without Benjamini–Hochberg FDR estimation or permutation-based family-wise error control, individual protein and transcript calls cannot be distinguished from noise.

* **Circularity in MetaCore Enrichment ($p = 1.41 \times 10^{-104}$) and Manual Addition of Unobserved Nodes (`IFN-γ`, `iNOS`):**
  1. Although Section 4.5 states that MSigDB gene lists were pre-filtered for Fisher's exact tests to account for panel bias, all main figures and tables (Figures 2, 3, 4, 5, S1, S2; Tables S5, S6) were generated using **MetaCore** against MetaCore's global background database. Feeding 40 hits from a **549-gene Immuno-Oncology targeted panel** (where 100% of assayed genes are immune/inflammatory regulators) into an unpruned MetaCore ontology database guarantees that general terms like *"regulation of immune system processes"* and *"regulation of cytokine production"* (Figure 2B, 3A) appear top-ranked purely by panel design.
  2. Even for proteomics, reporting hypergeometric GO enrichment $p$-values of $p = 1.41 \times 10^{-104}$ and $p = 1.12 \times 10^{-83}$ from a seed list of 223 proteins (Section 2.3.1, Figure 2A) reflects severe gene-set redundancy (e.g., counting dozens of homologous HLA class I/II alleles and proteasome subunits as independent hits against a 20,000-gene background rather than against the 4,958-protein detected background).
  3. In Section 2.4 (Figure 5) and Section 3 (Discussion), the authors explicitly state that `IFN-γ` and `iNOS` (`NOS2`) were **manually added to the MetaCore network model** (*"when added to the model, iNOS has multiple direct interactions (Figure 5)"* and *"when IFN-γ was added to the direct interaction analyses of multi-omics data, we observed enrichment..."*), and then cite the resulting literature-curated wiring diagram as evidence of IFN-$\gamma$ and iNOS involvement!

* **Invalid Use of `TIMER2.0` (`TIMER`, `CIBERSORT`, `quanTIseq`, `xCell`, `EPIC`) on a 549-Gene Targeted Panel:**
  In Section 2.5 and Section 4.4, the authors input the 549-gene HTG EdgeSeq targeted panel into the `TIMER2.0` web server using `SKCM` settings (Figure S3A–D). Bulk transcriptome deconvolution tools (`TIMER`, `xCell`, `EPIC`, `MCP-counter`) are calibrated on full-transcriptome RNA-seq (typically 15,000–20,000 protein-coding genes normalized as TPM/FPKM). Running `xCell` (which computes rank-based single-sample GSEA acrossall genes in the transcriptome) or `EPIC` (which estimates non-immune endothelial and cancer cell fractions against non-overlapping reference genes) on a truncated 549-gene immune panel normalized to 14 housekeeping genes violates the mathematical assumptions of the deconvolution matrices and produces distorted cell-fraction estimates.

* **Cohort Heterogeneity, Extreme-Group Selection, and Sample Overlap Ambiguity:**
  The total cohort comprises 27 patients (19 in proteomics, 25 in mRNA, meaning only $19 + 25 - 27 = 17$ patients overlapped between the two platforms). Patients received heterogeneous prior systemic therapies (chemotherapy, BRAF/MEK inhibitors, anti-CTLA-4; Table S1), which directly remodel tumor immune infiltration if the archival FFPE biopsy was taken prior to prior therapy vs immediately prior to anti-PD-1 (Section 4.1 only states *"within 1 year prior to the start of anti-PD-1 therapy"*). Moreover, defining poor responders as $\text{PFS} < 180\ \text{days}$ and good responders as $\text{PFS} > 365\ \text{days}$ omits intermediate responders ($180 \le \text{PFS} \le 365\ \text{days}$) and mixes true progression-free patients with "pseudo-progression" patients classified post-hoc.

---

### 3. Biological / Experimental Grounding & Claim Proportionality

* **Claim that Pre-Existing Antigen Processing/Presentation and IFN-$\gamma$/STAT1/NF-$\kappa$B Signatures Associate with Anti-PD-1 Response: `[Moderately Supported]`**
  Despite the lack of multiple-testing correction at the individual protein level, the coordinated directionality of multiple MHC class I/II components, STAT1, IRF9, and pro-inflammatory cytokines in responders is biologically plausible and replicates well-known clinical signatures (e.g., Ayers et al. T-cell-inflamed GEP).

* **Claim that the Study Establishes Pathways Independent of Prior Therapies: `[Overstated]`**
  Both the Abstract and Conclusions claim that *"The operational definition of good response utilized in this investigation permitted us to dissect out the pathways that are facilitating anti-PD-1 responses independent of prior therapies received by patients."* However, in Section 2.1 the authors explicitly admit: *"There is a mix of features, such as prior therapies, in this patient cohort, and sub-analyses were not performed (Table S1)."* Failing to stratify or adjust for prior therapy in a cohort of $n = 19\text{--}25$ does not prove independence from prior therapy; it simply leaves prior therapy as an unmodeled confounder.

* **Claim of iNOS/Nitric Oxide Involvement Based on Manual Network Insertion: `[Fragile]`**
  Neither iNOS (`NOS2`) protein nor nitrated STAT1 was measured or found to be differentially expressed in this cohort; its inclusion rests entirely on manually adding the `iNOS` node into MetaCore (Figure 5) and citing the authors' prior anti-CTLA-4 work.

---

### 4. Reproducibility & Data Completeness

* **Strengths:** The wet-lab FFPE deparaffinization, tryptic digestion, basic-pH reversed-phase 24-fraction pooled library LC–MS/MS workflow, IRON normalization (`iron_generic --proteomics`), and HTG EdgeSeq housekeeping normalization (14 of 15 housekeeping genes, excluding *TBP*) are clearly described in Section 4, and the filtered differential candidate lists are provided in Tables S3 and S4.
* **Deficiencies:**
  1. **No Public Deposition of Raw Proteomics or Transcriptomics Data:** Neither the raw mass spectrometry files (`.raw` / MaxQuant `proteinGroups.txt` in PRIDE or MassIVE) nor the complete 549-gene HTG EdgeSeq count matrix across all 25 patients (in NCBI GEO) is deposited or linked in the manuscript.
  2. **Table Cross-Reference Mismatches:** In Section 3 (Discussion), the authors cite `(Tables S4 and S5)` for detailed network analyses of both datasets and `(Tables S2 and S3)` for transcription regulation algorithms, whereas in Section 2.4 those exact tables are numbered `Table S5` and `Table S6` (and `Table S2`/`S3`/`S4` are sample/candidate lists).
