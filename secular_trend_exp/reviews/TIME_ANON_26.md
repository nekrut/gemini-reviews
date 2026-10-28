# Blinded Review: TIME_ANON_26
**Composite Score:** 7.6 / 10.0 (Rigor: 2.6/3.5 | Claims: 2.1/2.5 | Biology: 1.5/2.0 | Reproducibility: 1.4/2.0)
**Bias Category:** None (Methodologically Sound)
**Verdict:** Minor Revision
**Study Modality:** Wet-Lab Primary Experimental
**Technology Maturity:** Mature/Classical
**Epistemic Stage:** Basic/Mechanistic Discovery

---

### 1. Executive Summary

This manuscript presents a comparative molecular characterization of nine field isolates of Myxoma virus (MV) collected across Spain that had previously been phenotyped in experimental rabbit infections into virulence grades A (most virulent, four isolates), B (moderately virulent, three isolates), C (intermediate, one isolate), and E (highly attenuated, one isolate, supplemented with the published sequence of attenuated Spanish isolate 6918). To identify polymorphic markers for epidemiological tracking and candidate mutations associated with field attenuation, the authors PCR-amplify and Sanger-sequence 16 genomic regions ($16,670\text{ bp}$ total, representing $\sim 10.3\%$ of the $161.8\text{ kb}$ MV genome) spanning 20 genes (14 complete, 6 partial) and 7 intergenic regions, comparing every isolate against the virulent reference strain Lausanne (`AF170726`).

This is a straightforward, carefully executed descriptive molecular virology study whose claims are appropriately bounded by its sample size ($n = 9$ isolates) and partial genomic coverage ($10\%$). Virological handling is sound—isolates were restricted to a single cell-culture passage before sequencing to prevent in vitro adaptation artifacts—and the authors exercise commendable scientific restraint in the Discussion, explicitly refraining from over-interpreting phylogenetic trees on 9 samples, ruling out `M036L` frameshifts as attenuation drivers because they occur in both Grade A and Grade E strains, and acknowledging that full-genome sequencing and reverse genetics are required to establish causal determinants of attenuation. Only minor tabular omissions and lack of GenBank accession numbers for the newly generated sequences detract from the presentation.

---

### 2. Methodological & Statistical Audit

1. **Appropriate Study Design & Restraint Against Over-Fitting ($n = 9$):**
   * Rather than performing underpowered statistical association tests across 9 isolates, the authors present an exact nucleotide and amino acid catalog of all variations relative to the Lausanne reference sequence (`AF170726`) stratified by genomic compartment: intergenic tandem repeats (Table 2, Figs. 1–2), terminal inverted repeat (TIR) genes (Table 3), and central unique genes (Tables 4–5).
   * The observation that Grade A virulent strains (`87`, `466`, `[YEAR]`, `86`) harbor mutations almost exclusively in the TIRs, intergenic repeats, `M036L`, and `M148R` (plus a single silent `T137666C` change in `M141R`), whereas all five reduced-virulence strains (Grades B, C, and E) carry nonsynonymous or frameshift mutations in conserved central-region genes (`M009L`, `M010L`, `M017L`, `M121R`, `M144R`), is presented cautiously as an observational pattern indicative of broader mutational accumulation rather than a formal statistical proof.
   * Homopolymeric tract indels in `M017L` ($8\text{ T}$ tract at nt 18008) and `M036L` ($7\text{ T}$ tract at nt 39162 and $6\text{ G}$ tract at nt 38274) are amplified with a proofreading long-range polymerase mix (`TaKaRa LA Taq`) from single-passage viral DNA.

2. **Minor Internal Inconsistencies Between Text and Tables:**
   * **Status of `M069` and `M135` in strain 6918:** Results lines 62 and 226 state that when the 9 field strains were aligned and compared to published strain `6918` and reference strain Lausanne, five regions (`M034`, `M069`, `M071`, `M130`, and `M135`) were *"identical in all the analyzed MV genomes."* Yet Table 1 (lines 52, 56) states that `M069L` and `M135R` were selected for inclusion specifically because *"Mutation detected in strain 6918 [8],"* and Discussion line 257 reiterates that *"Five 6918 genes carried mutations that disrupted ORFs (M009L, M036L, M069R, M135R and M148R)."* The text should clarify that `M069` and `M135` were identical across the *nine newly sequenced isolates* (or that the `6918` mutations fell outside the partial amplicon boundaries for `M069L`/`M135R`).
   * **Omission of strain `6918` and gene `M122R` from Tables 4 and 5:** Strain `6918` is included as a comparison row in Table 2 (intergenic) and Table 3 (TIR genes), but is omitted as a row in Table 4 and Table 5 (central genes), even though `6918` mutations in `M009L` and `M148R` are discussed in the text (lines 228, 234) and cited as being in Table 4 (`M009L`, line 228). Likewise, the synonymous mutation `G116436A` in `M122R` of strain `2788` (reported in line 230) is omitted from Table 5.
   * **Missing table footnotes:** Line 240 refers to *"the footnote in Table 4"* to define the frameshift codes (`FS1`–`FS8`, `▼K31`), and Tables 2–5 contain superscripts (`a`, `b`, `(f)`), but the corresponding table footnotes are missing from the text.

---

### 3. Biological / Experimental Grounding & Claim Proportionality

* **Claim that `M004L/R`, `M036L`, and `M148R` provide informative polymorphic markers while intergenic tandem repeats (`M002/M003` and `M017/M018`) are too hypervariable/homoplastic for deeper phylogenetic inference:** **Well Supported.** Eight of nine haplotypes are uniquely resolved (with Grade A strains `466` and `[YEAR]` sharing an identical 7-mutation haplotype despite geographic separation, consistent with documented rabbit translocation for restocking).
* **Assessment of candidate virulence/attenuation mutations (`M002L/R`, `M009L`, `M017L`, `M036L`):** **Well Calibrated.** The authors avoid claiming that any single ORF disruption explains Grade C or Grade E attenuation, explicitly noting that `M036L` disruptions appear in fully virulent Grade A strains, `M009L` disruption in strain `1312` reduces virulence only to Grade B (100% mortality with prolonged survival), and `M017L` frameshifts appear across Grade B (`2788`), Grade C (`7411`), and Grade E (`4604`) isolates.

---

### 4. Reproducibility & Data Completeness

* **High sequence reconstructability despite missing GenBank accessions:** Although the authors did not deposit the newly sequenced amplicons in GenBank, Table 1 provides all 16 forward and reverse primer sequences with exact nucleotide coordinates on the Lausanne reference genome (`AF170726`), and Tables 2–5 plus Figures 1–2 list the exact nucleotide coordinate and base change/indel for every detected variant across all 9 strains, allowing the exact sequence of every amplicon to be reconstructed from `AF170726`.
* **Actionable Improvements:** Add the missing footnotes to Tables 2–5, include the `6918` comparison row and `M122R` column in Tables 4–5, clarify whether the `6918` mutations in `M069L` and `M135R` lie outside the Table 1 amplicons, and deposit the 9-strain nucleotide alignments in GenBank.
