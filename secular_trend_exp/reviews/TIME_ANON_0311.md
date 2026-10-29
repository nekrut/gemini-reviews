<Blinded Review: TIME_ANON_0311>
**Composite Score:** 6.5 / 10.0 (Rigor: 2.1/3.5 | Claims: 1.5/2.5 | Biology: 1.5/2.0 | Reproducibility: 1.4/2.0)
**Bias Category:** Technical/Assay
**Verdict:** Major Revision
**Study Modality:** Hybrid Computational + Wet-Lab
**Technology Maturity:** Mature/Classical
**Epistemic Stage:** Clinical/Observational

---

### 1. Executive Summary
This molecular epidemiological surveillance study investigates coronavirus (CoV) prevalence, co-infection, genetic diversity, and recombination among companion animals at a veterinary hospital in Chengdu, Sichuan Province, China. Between July 2022 and June 2023, the authors collected 309 clinical samples (fecal, ascitic fluid, blood, nasal, and throat swabs) from 263 companion animals (142 cats and 121 dogs) and screened them using a pan-coronavirus semi-nested RT-PCR targeting a 242-bp fragment of the *RdRp* gene, alongside PCR/RT-PCR screening for common co-infecting viral pathogens (`FPV`, `FCV`, `FHV-1`, `CPV`, `CDV`, `CAdV-2`, `CPIV`). Overall CoV positivity was 21.7% (57/263): in cats, `FCoV` was detected in 25.4% (36/142, all typed as `FCoV-I`); in dogs, `CCoV` was detected in 14.0% (17/121, all `CCoV-IIa`), `CRCoV` in 3.3% (4/121), and `SARS-CoV-2` in 0.8% (1/121). From positive samples, the authors amplified and Sanger-sequenced full-length *S*, *N*, *ORF3abc*, and *ORF7ab* genes (`GenBank PV246283–PV246328`, `PV983458`), performing phylogenetic (`MEGA 7.0`, NJ with 1,000 bootstraps), recombination (`RDP4` across 7 algorithms + `SimPlot`), and selective pressure (`Datamonkey`: `SLAC`, `FEL`, `MEME`, `FUBAR`) analyses.

The surveillance dataset and full-length gene characterizations of local `FCoV-I` and `CCoV-IIa` strains (including identification of a 145-nt deletion truncating *ORF3c* in `FCoV-3abc-14`, a 21-nt deletion in two `FCoV-I` *S* genes, and recombinant `FCoV-I` *S* mosaic breakpoints at nt 919 and 1639) provide useful regional veterinary virology data. However, the manuscript has three significant weaknesses:
1. **Unconfirmed single-amplicon claim of the "first reported case of SARS-CoV-2 in a dog in mainland China":** This headline claim rests solely on a single short (~242 bp) pan-CoV semi-nested *RdRp* Sanger amplicon (`PV983458`, 99.6% identity to reference `WIV04`). When the sample (`20221208dog7`) was sent to the Chengdu CDC for whole-genome sequencing, NGS failed completely (`"the complete genomic sequence of SARS-CoV-2 was not obtained due to the poor sample quality"`), and no confirmatory second target (`N`, `S`, or `E` gene qRT-PCR), Ct value, or serological neutralization assay was performed to rule out laboratory or environmental amplicon cross-contamination.
2. **Internal text contradiction on the amino acid insertion size in `FCoV-S-5-9`:** In Results Section 3.3 (line 87), the authors state *"there was an insertion at positions 514–525 in FCoV-S-5-9 resulting in a 4-aa insertion"*, whereas in the Discussion (line 115), they state *"Moreover, FCoV-S-5-9 had a 5-aa insertion."*
3. **Missing tables and selection site coordinates in the manuscript body:** None of the five referenced tables (`Tables 1–5`) or figure legends (`Figures 1–6`) are embedded in the manuscript text, and the `Datamonkey` selection analysis (Section 2.4) is never reported in the Results section.

### 2. Methodological & Statistical Audit
- **Diagnostic Screening and Confirmatory Standards for `SARS-CoV-2` in Animals:**
  - Semi-nested RT-PCR involves opening first-round PCR tubes to transfer template into a second PCR reaction, carrying a well-known risk of carryover amplicon contamination—especially in December 2022 (`20221208dog7`) when human `SARS-CoV-2` circulation was at its peak.
  - Because `PV983458` has 99.6% nucleotide identity to the ancestral `WIV04` reference (differing by at most 1 nt across ~242 bp) and CDC whole-genome NGS failed to recover SARS-CoV-2 reads from the clinical specimen, WHO/WOAH standards for confirming a novel animal host infection in a new geographic region require amplification of at least two independent genomic targets (e.g., `RdRp` + `N` or `S`) or serological confirmation.
- **Internal Contradiction on `FCoV-S-5-9` Insertion Length:**
  - Nucleotide positions `514–525` span $525 - 514 + 1 = 12\text{ nucleotides}$, which encodes $12 / 3 = 4\text{ amino acids}$ (consistent with line 87: `"resulting in a 4-aa insertion"`). The statement in Discussion line 115 (`"FCoV-S-5-9 had a 5-aa insertion"`) is an arithmetic/reporting error that must be corrected.
- **Unreported Positive Selection Analysis (`SLAC`, `FEL`, `MEME`, `FUBAR`):**
  - Section 2.4 (`line 52`) details a complete codon-level selection pipeline on `Datamonkey` (`http://www.datamonkey.org`) using four methods (`SLAC`, `FEL`, `MEME`, `FUBAR`) with significance thresholds `$p$-value < 0.1` (`SLAC`, `FEL`, `MEME`) and `posterior probability > 0.9` (`FUBAR`). However, **zero selection results ($d_N/d_S$, positively selected sites, or purifying selection statistics) are presented anywhere in the Results or Discussion**.
- **Phylogenetic Model Selection:**
  - All phylogenetic trees (*RdRp*, *S*, *N*, *ORF3abc*, *ORF7ab*) were reconstructed using neighbor-joining (NJ) with the Kimura 2-parameter (K2P) model in `MEGA 7.0` rather than maximum likelihood (ML, e.g., `IQ-TREE` or `RAxML` with best-fit substitution models). While adequate for broad genotype assignment (`FCoV-I` vs. `FCoV-II`, `CCoV-IIa` vs. `CCoV-IIb`), ML trees are preferred for full-length *S* gene phylogenetics (`~4.4 kb`).
  - The recombination analysis in `RDP4` (requiring support from all 7 methods—`RDP`, `GENECONV`, `BootScan`, `MaxChi`, `Chimaera`, `SiScan`, `3Seq`—at Bonferroni $p \le 0.05$, followed by `SimPlot` verification) is stringent and methodologically sound.

### 3. Biological / Experimental Grounding & Claim Proportionality
- **Claim 1:** *"This study discovered the first case of a dog infected with SARS-CoV-2 in the Chinese mainland."* `[Overstated]`
  - A single ~242-bp semi-nested *RdRp* amplicon from a specimen that failed NGS confirmation at the local CDC and lacks a second PCR target or serology is insufficient to prove active `SARS-CoV-2` infection in a dog (as opposed to transient environmental/owner contamination of the swab or PCR carryover). This finding should be reported cautiously as an unconfirmed *RdRp*-reactive swab rather than a definitive infection.
- **Claim 2:** *"All 36 FCoV strains identified belonged to FCoV I, and 17 CCoV strains were subtyped as CCoV IIa... Co-infections of CCoV with CPV and FCoV with FPV were the most frequent, accounting for 55.6% (10/18) and 11.4% (4/35), respectively."* `[Well Supported]`
  - Supported by *RdRp* and full-length *S*/*N*/*ORF3abc*/*ORF7ab* sequencing (`PV246283–PV246328`) and multi-pathogen PCR screening across the 263 clinical cases. (Note a minor denominator discrepancy: 36 FCoV-positive cats on line 60 vs. `4/35` on lines 16 and 69, and 17 CCoV-positive dogs on line 61 vs. `10/18` on lines 16 and 69).
- **Claim 3:** *"FCoV-S-5-9 and FCoV-S-7-10 were proven to be recombinants of FCoV-S-5-23 and FCoV-S-1-2, with distinct breakpoints [nt 919 and nt 1639]."* `[Well Supported]`
  - Supported by full-length *S* gene sequencing and 7-algorithm consensus detection in `RDP4` ($p \le 0.05$) plus `SimPlot` bootscanning.
- **Claim 4:** *"A 145-nt deletion at positions 942 to 1086 in the ORF3abc gene of FCoV-3abc-14... caused a severe truncation of the encoded protein, which is fixed in the virulent pathotype (FIPV)."* `[Moderately Supported]`
  - While the 145-nt deletion truncating *ORF3c* is clearly documented by Sanger sequencing, the clinical status of cat `#14` (whether it had histopathologically confirmed feline infectious peritonitis [FIP] vs. enteric FCoV) is not explicitly linked to the `FCoV-3abc-14` isolate in the text.

### 4. Reproducibility & Data Completeness
- **Data Availability:** All 47 newly generated sequences (`FCoV`, `CCoV`, `CRCoV` *RdRp*, *S*, *N*, *ORF3abc*, *ORF7ab*, and the canine `SARS-CoV-2` *RdRp* sequence) are deposited in NCBI GenBank under accessions `PV246283–PV246328` and `PV983458`.
- **Missing Elements Requiring Revision:** `Tables 1–5` (clinical primers, sampling breakdown, sequence identity matrices, amino acid variations, and `RDP4` $p$-values) must be included in the main text, the `Datamonkey` selection results (`Section 2.4`) must either be reported or removed from Methods, and the `4-aa` vs. `5-aa` insertion discrepancy in `FCoV-S-5-9` and `35 vs. 36` / `17 vs. 18` co-infection denominators must be reconciled.
</Blinded Review: TIME_ANON_0311>
