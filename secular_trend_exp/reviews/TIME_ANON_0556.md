<Blinded Review: TIME_ANON_0556>
OVERALL_SCORE: 7.5/10
VERDICT: PASS
ESTIMATED_DECADE: 2020s
**Composite Score:** 7.5 / 10.0 (Rigor: 2.4/3.5 | Claims: 1.9/2.5 | Biology: 1.5/2.0 | Reproducibility: 1.7/2.0)
**Bias Category:** Technical/Assay
**Verdict:** Minor Revision
**Study Modality:** Hybrid Computational + Wet-Lab
**Technology Maturity:** Mid-Stage High-Throughput
**Epistemic Stage:** Basic/Mechanistic Discovery

---

### 1. Executive Summary / SUMMARY
This experimental dermatology and innate immunology study investigates the transcriptional regulation and alternative splicing of chemokines—specifically *CCL2*, *CXCL10*, and *CX3CL1* (fractalkine)—in primary normal human epidermal keratinocytes (NHEKs isolated from breast reduction skin specimens) following transfection with synthetic cytosolic nucleic acid analogs (`poly(I:C)` dsRNA at `0.666 μg/mL` and `poly(dA:dT)` dsDNA at `1 μg/mL`) or stimulation with inflammatory cytokines and TLR ligands. Combining a 10-chemokine qPCR screen ($n=4$ donors), time-course TaqMan qRT-PCR validation ($n=7$ donors), siRNA knockdown of nine pattern recognition receptors (PRRs: *TLR3, IFIH1/MDA5, DDX58/RIG-I, EIF2AK2/PKR, CGAS, IFI16, AIM2, ZBP1/DAI, POLR3A*; $n=3$ donors), small-molecule signaling inhibitor assays (NF-$\kappa$B [`Bay 11-7085`], STING [`H151`], STAT1 [`Fludarabine`], STAT3 [`Stattic`], ERK1/2 [`PD98059`], JNK [`SP600125`], and p38 MAPK [`SB203580`]; $n=3$ donors), and isoform-specific RT-PCR/Sanger sequencing paired with re-analysis of two public bulk RNA-seq datasets (`E-MTAB-9019` and `GSE216511`), the authors show that: (1) both `poly(I:C)` and `poly(dA:dT)` strongly induce *CCL2*, *CXCL10*, and *CX3CL1* mRNA in NHEKs with distinct kinetics (peaking at `12 h` for `poly(dA:dT)` vs. `24 h` for `poly(I:C)`); (2) single-PRR siRNA knockdowns fail to abrogate chemokine induction, indicating sensor redundancy; (3) pharmacological inhibition implicates NF-$\kappa$B and STAT3 in the induction of all three chemokines, plus STING/STAT1/p38 in specific stimulus-gene combinations; and (4) a database-annotated alternative splice variant of *CX3CL1* lacking part of exon 1 (`NM_001304392.3` / `ENST00000564948.1`) is undetectable in human keratinocytes and supported by only a single choroid EST (`CA396869.1`) in GenBank, whereas the canonical transcript (`NM_002996.6`) accounts for all *CX3CL1* expression.

### 2. STRENGTHS
- **Appropriate Mixed-Effects Statistical Modeling of Multi-Donor Primary Human Cells:** Rather than treating technical replicates from a single immortalized cell line as independent or using unadjusted $t$-tests across time points, the authors use primary human keratinocytes from multiple independent donors ($n=4$ for array, $n=7$ for time-course qPCR, $n=3$ for siRNA/inhibitors) and analyze $\Delta C_t$ values with linear mixed-effects models (`lme4` in R with donor as a random intercept) and Holm or Benjamini-Hochberg multiplicity corrections.
- **Rigorous Debunking of an Annotated Database Splice Variant (`NM_001304392.3`):** When a commercial TaqMan assay spanning the exon 1–2 junction unexpectedly failed to detect *CX3CL1* induction, the authors designed flanking RT-PCR primers (`F1`/`F2`/`R`), sequenced the single `265-bp` amplicon by Sanger sequencing, audited the underlying GenBank EST evidence (`CA396869.1`), and checked splice junctions in two public keratinocyte RNA-seq cohorts (`E-MTAB-9019`, `GSE216511`), demonstrating that `NM_001304392.3` is not expressed in human keratinocytes and likely represents an annotation artifact or rare tissue-restricted transcript.
- **Full Open Data Availability:** Raw Cq values, processed tables, and scripts are deposited in an open institutional repository (`10.82570/SZTE_Datarepo_detfw-gx013`).

### 3. WEAKNESSES & METHODOLOGICAL AUDIT (Methodological & Statistical Audit)
- **1,000-Fold Cytokine Concentration Discrepancy Between Methods and Figure 2 Legend:**
  - In Section "Experimental procedures" (Line 41), the text states: *"24 hours after the shifting of the medium to serum-free, cells were treated with 100 ng/mL IFN-γ, 50 ng/mL TNF-α, **100 μg/mL IL-17A**, **100 μg/mL IL-23**, **100 μg/mL IL-12** (PeproTech)..."*
  - In the Figure 2 legend (Line 89), the concentrations are stated as: *"IL-12 (`100 ng/mL`), IL-17A (`100 ng/mL`), IL-23 (`100 ng/mL`)..."*
  - `100 μg/mL` of recombinant human IL-17A, IL-23, or IL-12 would be a massive, non-physiological concentration (the entire PeproTech vial per mL of medium); this is clearly a `μg/mL` vs. `ng/mL` unit error in the Methods section that must be corrected.
- **Exclusive Reliance on mRNA (qRT-PCR) Without Protein Secretion / Shedding Validation:**
  - Every functional readout in the manuscript (`CCL2`, `CXCL10`, `CX3CL1`, and PRR knockdowns) is measured solely at the mRNA level by qRT-PCR normalized to a single housekeeping gene (*GAPDH*). Because CX3CL1 is synthesized as a membrane-anchored chemokine that requires metalloprotease shedding (`ADAM10`/`ADAM17`) to act as a soluble chemoattractant, and CXCL10/CCL2 secretion can be post-transcriptionally regulated, the absence of ELISA or Western blot confirmation is a notable biological limitation.
- **Inhibitor Specificity and Cytotoxicity Controls Missing (`Bay 11-7085` and `Stattic`):**
  - Pharmacological inhibitors (`10 μM Bay 11-7085`, `5 μM Stattic`, `100 μM Fludarabine`, `0.5 μg/mL H151`, `20 μM PD98059`, `25 μM SP600125`, `10 μM SB203580`) were applied for up to `24 h` alongside `LyoVec` nucleic acid transfection. Both `Bay 11-7085` (`10 μM`) and `Stattic` (`5 μM`) are irreversible electrophilic modifiers known to induce significant cell death and off-target translational arrest in primary keratinocytes over 24 hours, yet no cell viability/cytotoxicity data (e.g., MTT/LDH) or target phosphorylation Western blots (`p-p65`, `p-STAT3`, `p-STING`, `p-p38`) are shown to verify that the drop in relative chemokine mRNA reflects specific pathway blockade rather than toxicity.
- **Negative Single-PRR siRNA Knockdowns Leave Upstream Sensing Unresolved:**
  - Individual siRNA knockdowns achieved only ~50–75% mRNA reduction (Figure S3) and produced zero statistically significant reduction in *CCL2*, *CXCL10*, or *CX3CL1* induction (Figure 3). While the authors reasonably attribute this to redundancy among cytosolic dsRNA and dsDNA sensors, combined knockdowns (e.g., `RIG-I + MDA5` or `cGAS + IFI16`) were not performed.

### 4. Biological / Experimental Grounding & Claim Proportionality
- **Claim 1:** *Cytosolic dsRNA (`poly(I:C)`) and dsDNA (`poly(dA:dT)`) strongly induce CCL2, CXCL10, and CX3CL1 transcription in primary human keratinocytes, with `poly(dA:dT)` eliciting faster peak kinetics (12 h) than `poly(I:C)` (24 h).* — `[Well Supported]` by multi-donor qPCR array ($n=4$) and time-course TaqMan assays ($n=7$, Figure 1).
- **Claim 2:** *Only the full-length canonical CX3CL1 transcript (`NM_002996.6`), and not the database-predicted exon-1-truncated splice variant (`NM_001304392.3`), is expressed in unstimulated and nucleic-acid-stimulated human keratinocytes.* — `[Well Supported]` by flanking RT-PCR, Sanger sequencing, and independent public RNA-seq re-analysis (Figure 5).
- **Claim 3:** *NF-$\kappa$B, STAT1/STAT3, STING, and MAPK pathways differentially mediate nucleic-acid-induced CCL2, CXCL10, and CX3CL1 expression.* — `[Moderately Supported]`; based solely on single-dose small-molecule inhibitors ($n=3$) at the mRNA level without viability or phosphorylation controls.

### 5. Reproducibility & Data Completeness
- **Data & Code:** Raw data and statistical scripts are publicly accessible via DOI `10.82570/SZTE_Datarepo_detfw-gx013`; public RNA-seq accessions (`E-MTAB-9019`, `GSE216511`) and RefSeq/Ensembl transcript IDs (`NM_002996.6`, `NM_001304392.3`) are explicitly cited.
- **Reagent Details:** Primer sequences (`F1`, `F2`, `R`), TaqMan assay IDs, siRNA catalog numbers, and statistical model specifications (`lme4`, `emmeans`) are thoroughly reported (subject to fixing the `100 μg/mL` vs. `100 ng/mL` typo in Line 41).
</Blinded Review: TIME_ANON_0556>
