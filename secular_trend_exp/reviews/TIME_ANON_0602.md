<Blinded Review: TIME_ANON_0602>
OVERALL_SCORE: 8.0/10
VERDICT: PASS
ESTIMATED_DECADE: 2010s
**Composite Score:** 8.0 / 10.0 (Rigor: 2.7/3.5 | Claims: 2.0/2.5 | Biology: 1.8/2.0 | Reproducibility: 1.5/2.0)
**Scientific Core Score:** 6.5 / 8.0
**Bias Category:** None (Methodologically Sound)
**Verdict:** Minor Revision
**Study Modality:** Wet-Lab Primary Experimental
**Technology Maturity:** Mature/Classical
**Epistemic Stage:** Translational/Preclinical/Biomarker

---

### 1. Executive Summary (SUMMARY)
This preclinical translational study investigates the in vitro and in vivo transcriptional silencing and epigenetic regulation of the conditional immortalizing transgene `c-mycERTAM` (driven by the viral CMV promoter) in the clinical-grade human neural stem cell line CTX0E03. Using sequential gDNA/RNA extraction from the same brain tissue homogenates, human-specific *Alu-Sq* probe qPCR (to quantify surviving human cells down to 1 cell/reaction), and junction-specific *c-mycERTAM* SYBR Green qRT-PCR (down to 10 copies/reaction), the authors demonstrate that *c-mycERTAM* expression drops from $215.7 \pm 13.2$ copies/cell pre-implantation to $6.9 \pm 3.4$ copies/cell at 1 week and $7.7 \pm 2.5$ copies/cell at 4 weeks after intracerebral grafting into middle cerebral artery occluded (MCAo) rat brains ($96–97\%$ reduction). Bisulfite sequencing of 99 clones across 10 grafted brains confirms extensive CpG methylation of the CMV promoter in vivo ($86.8\%$ at 1 week and $75.0\%$ at 4 weeks vs. $2\%$ pre-implantation), while in vitro growth-factor and 4-hydroxytamoxifen (4-OHT) withdrawal confirms parallel reductions in transcript and c-MycERTAM protein levels by Western blot and immunocytochemistry. The assay validation is well controlled, with only minor technical caveats in qPCR efficiency calibration and incomplete table display.

### 2. Methodological & Statistical Audit (STRENGTHS, WEAKNESSES & METHODOLOGICAL AUDIT)
**Strengths:**
* **Rigorous Spike-In and Immediate-Harvest Positive Controls (Figure 1C–F):** Standard curves were generated in the presence of background rat brain gDNA/cDNA, and an in vivo zero-hour positive control (brains harvested immediately after injecting 279,600 cells) recovered $241,116 \pm 15,487$ cells by *Alu* qPCR and $236.9 \pm 7.8$ *c-mycERTAM* copies/cell (matching $242.3 \pm 47.8$ copies/cell in culture), proving that rat brain tissue lysis does not inhibit human cell or transcript quantification.
* **Paired gDNA/RNA Co-Extraction from Identical Tissue Pieces:** Extracting DNA and RNA sequentially from the same homogenate via the AllPrep kit avoids spatial sampling bias between adjacent brain sections.
* **Orthogonal Epigenetic and Protein Validation:** Pairs in vivo transcript knockdown with bisulfite sequencing of the CMV promoter CpG island (10 clones/animal × 5 animals/timepoint) and in vitro protein-level confirmation via dual-epitope (c-Myc and ERα) Western blot and ICC.

**Weaknesses & Methodological Audit:**
* **Supra-Optimal qRT-PCR Amplification Efficiency (`E = 2.131`):** In Figure 1D, the *c-mycERTAM* qRT-PCR standard curve reports an efficiency of `2.131` (i.e., $113.1\%$ per cycle, above the standard MIQE acceptable range of $1.90–2.10$ / $90–110\%$), likely reflecting mild primer-dimer formation or polymerase inhibition at high template concentrations in the SYBR Green assay.
* **Incomplete Animal Rows in Table 1 vs. Methods Sample Size:** The Methods section ("MCAo and cell grafting") states that animal brains were collected from **6 grafted** (+ 2 vehicle control) rats at 1 week and **6 grafted** (+ 3 vehicle control) rats at 4 weeks, which matches the 6 bars per timepoint in Figure 2A–B (`201, 301, 302, 501, 502, 601` at Week 1; `203, 204, 403, 404, 602, 604` at Week 4). However, Table 1 is truncated at the bottom, displaying only 4 animals per timepoint (`201, 301, 302, 501` for Week 1; `203, 204, 403, 404` for Week 4) and omitting `502, 601, 602, 604` as well as the `404` summary row and footnotes `1, 2`.
* **Lack of Reverse-Transcription Efficiency Normalization in "Absolute" Copy Numbers per Cell:** The *c-mycERTAM* copy number standard curve (Methods, line 145) was constructed using serial dilutions of CTX0E03 genomic DNA (assuming 1 genomic copy per cell) spiked into rat cDNA, rather than an in vitro transcribed RNA standard subjected to reverse transcription alongside the samples. Because reverse transcription efficiency is typically $<100\%$, gDNA-calibrated qRT-PCR measures cDNA copies rather than absolute mRNA copies (though the relative ~30-fold reduction between pre-implantation and post-implantation cells using the same protocol remains completely valid).
* **Figure Cross-Reference Typo in Results:** In Results ("Validation of Alu and c-mycERTAM assays", line 40), the text cites `Figure 1F` and `Figure 1G` for the positive control cell counts and transcript copies, which actually correspond to `Figure 1E` and `Figure 1F`.

### 3. Biological / Experimental Grounding & Claim Proportionality
* **Rapid (~96%) downregulation of *c-mycERTAM* transcription per surviving CTX0E03 cell within 1–4 weeks after grafting into MCAo rat brain: [Well Supported].** Demonstrated across all grafted animals with immediate-harvest positive controls and vehicle negative controls.
* **In vivo silencing of the *c-mycERTAM* transgene is mediated by CpG methylation of the viral CMV promoter: [Well Supported].** Bisulfite sequencing shows a shift from 2% CpG methylation in proliferating culture to 75–87% methylation at 1 and 4 weeks in vivo across 99 sequenced clones.
* **Reduction in *c-mycERTAM* mRNA is accompanied by a proportional reduction in c-MycERTAM fusion protein upon growth arrest: [Well Supported].** Confirmed in vitro over 4 weeks of EGF/bFGF/4-OHT withdrawal via Western blot densitometry (~73% drop matching the ~73.4% mRNA drop).
* **Average silencing across bulk tissue sections precludes tumourigenicity risk: [Moderately Supported].** As the authors appropriately caveat in the Discussion, bulk qRT-PCR averages across all surviving cells in a section (and one section, `403 F2` at Week 4, showed 48.0 copies/cell), so single-cell heterogeneity cannot be fully excluded by homogenate qRT-PCR alone, though it is mitigated by the absence of the 4-OHT ligand in vivo.

### 4. Reproducibility & Data Completeness
* **Primer & Assay Transparency:** Exact primer sequences, fluorogenic probe sequences, GenBank accession (`U14573` for *Alu-Sq*), cycling conditions, stereotaxic coordinates, immunosuppression regimens, and antibody dilutions are clearly documented (except for two secondary antibody dilutions where a year-scrubbing regex replaced `1:2000` with `1:[YEAR]`).
* **Data Completeness:** Individual section-level cell counts and transcript numbers are tabulated in Table 1 (subject to restoring the truncated final rows for rats 502, 601, 602, and 604), and individual clone methylation maps are plotted in Figure 3B.
</Blinded Review: TIME_ANON_0602>
