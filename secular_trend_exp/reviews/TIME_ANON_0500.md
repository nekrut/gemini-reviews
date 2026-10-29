<Blinded Review: TIME_ANON_0500>
**Composite Score:** 7.6 / 10.0 (Rigor: 2.6/3.5 | Claims: 2.1/2.5 | Biology: 1.6/2.0 | Reproducibility: 1.3/2.0)
**Bias Category:** None (Methodologically Sound)
**Verdict:** Minor Revision
**Study Modality:** Wet-Lab Primary Experimental
**Technology Maturity:** Mature/Classical
**Epistemic Stage:** Translational/Preclinical/Biomarker

---

OVERALL_SCORE: 7.6/10
VERDICT: PASS
ESTIMATED_DECADE: 2000s

### 1. Executive Summary / SUMMARY
This large-scale biosafety and quality-control study screens 465 continuous human and non-human primate cell lines held at a biological resource center (authenticated by DNA profiling and confirmed free of mycoplasma and bacterial/fungal contamination) for latent and productive infections with human pathogenic viruses—Epstein-Barr virus (EBV), hepatitis B virus (HBV), hepatitis C virus (HCV), human immunodeficiency virus type 1 (HIV-1), human T-cell leukemia/lymphoma virus types I and II (HTLV-I/-II)—as well as xenotropic squirrel monkey retrovirus (SMRV) and general reverse transcriptase (RT) activity. Using PCR/RT-PCR assays equipped with custom-engineered competitive internal control templates, ultracentrifuged supernatant RT-ELISA (293 cell lines), anti-ZEBRA (`BZLF1`) Western blotting ($\pm$ TPA/Na-butyrate lytic induction), Gardella *in situ* lysing gel electrophoresis (separating circular episomes from linear virion DNA), *XhoI* Southern blot genotyping across EBV terminal repeats, and interphase FISH, the authors find: (1) zero cell lines infected with HCV, HIV-1, or HTLV-I/-II; (2) one acute myeloid leukemia line (`KASUMI-1`) with unexplained supernatant RT activity negative for HIV/HTLV/SMRV; (3) one hepatoma line (`HEP-3B`) carrying a known integrated 2.3-kb *HBsAg* fragment (core-deleted) with no active HBV virion production; (4) six cell lines positive for SMRV (`NAMALWA` and four subclones, plus the B-LCL `LCL-HO` likely co-transduced via `B95-8` supernatant); and (5) 39 lymphoid/NK cell lines positive for EBV DNA (including 3 lines—`CI-1`, `NK-92`, and `TMM`—previously misclassified as EBV-negative), of which 5 constitutively express weak `BZLF1` (`B95-8`, `BD-215`, `L-591`, `NC-NC`, `YT`) and 6 more express `BZLF1` upon TPA/Na-butyrate stimulation, with Southern blot RFLP proving each line carries a distinct patient- or `B95-8`-derived EBV strain rather than laboratory cross-contamination.

### 2. Methodological & Statistical Audit / WEAKNESSES & METHODOLOGICAL AUDIT
- **Incomplete Primer Table (Table 1) and Truncated Summary Tables (Tables 2 and 3) in the Manuscript Text:**
  - In Section `2.6 PCR Assays` (line 53), the text states that `Table 1` lists the primer sequences and annealing temperatures for HIV-1 (`SK 38`/`SK 39`), HTLV-I/-II (`SK 110`/`SK 111`), SMRV (`F/R-SMRV-env`, `F/R-SMRV-gag`), EBV (`TC 70`/`TC 72`), and HHV-8 (`F/R-HHV-8`). However, the rendered `Table 1` (lines 56–92) contains only four targets (`ABL`, `EBV`, `HBV`, and `HCV`), completely omitting the primer sequences, annealing temperatures, reference accessions, and wild-type/internal-control amplicon sizes for HIV-1, HTLV-I/-II, SMRV, and HHV-8 (and HHV-8 screening results are never mentioned in the Results section).
  - Similarly, `Table 2` (lines 127–163) is truncated alphabetically at `RAJI` (listing 33 of the 39 EBV-positive cell lines and omitting `SD-1`, `TMM`, `VAL`, and `YT` discussed in the text on lines 205–232), and `Table 3` (lines 165–201) is truncated alphabetically at `BE-13` (listing only 34 of the 465 screened cell lines, with a German column header `Zelltyp` left untranslated on line 167).
- **100-Fold Discrepancy in Sodium Butyrate Concentration Between Methods and Figure 5 Legend:**
  - In Section `2.1 Culture of Cell Lines` (line 28), lytic cycle induction of EBV-positive lines is specified as treatment *"for 3 days with $10^{-7}\text{ M}$ TPA (Sigma) and $3\text{ mM}$ Na-butyrate (Sigma)."* However, the legend to Figure 5 (line 235) states: *"Cells were stimulated for 72 hours with $10^{-7}\text{ M}$ TPA and $0.3\text{ M}$ Na-butyrate"* ($300\text{ mM}$, a 100-fold higher concentration that is hyperosmolar/cytotoxic to lymphoid cells).
- **Indirect Assessment of Infectious EBV Virion Production:**
  - To classify EBV-positive cell lines into biosafety risk groups, the authors measure immediate-early `BZLF1` (ZEBRA) protein induction by Western blot and linear EBV DNA bands on Gardella *in situ* lysing gels. However, as the authors themselves document on line 232, linear EBV DNA and `BZLF1` expression did not consistently correlate (`IM-9` induced `BZLF1` after TPA without producing linear DNA, whereas several `BZLF1`-negative cell lines exhibited significant linear EBV DNA bands on Gardella gels). Direct quantification of DNase-resistant encapsidated viral genomes in filtered cell-free supernatants or functional B-cell transformation bioassays was not performed.

### 3. Biological / Experimental Grounding & Claim Proportionality / STRENGTHS
- **Strengths:**
  - **Exemplary Molecular Assay Design with Spiked Competitive Internal Controls:** Every diagnostic PCR/RT-PCR reaction was run in paired duplicate (unspiked vs spiked near the limit of detection with custom-cloned size-shifted internal control templates sharing identical primer binding sites, plus exon-spanning `ABL` RT-PCR to verify RNA integrity and cDNA synthesis), rigorously eliminating false negatives due to PCR inhibition or nucleic acid degradation.
  - **Orthogonal Multi-Assay Verification of EBV Status and Clonality:** Discrepant cell lines previously reported as EBV-negative in the literature (`CI-1`, `NK-92`, `TMM`, `DOHH-2`) were cross-verified by PCR, Gardella *in situ* lysing gels, *XhoI* Southern blotting, and single-cell interphase FISH (demonstrating why focal/low-copy episomal carriage in `DOHH-2`, `CI-1`, and `TMM` escaped earlier insensitive EBNA immunofluorescence assays).
  - **Important Practical Biosafety Insight on SMRV Co-Transmission via `B95-8`:** Demonstrating that SMRV-contaminated `B95-8` marmoset stocks can co-transmit xenotropic SMRV during routine EBV immortalization of human B-LCLs (`LCL-HO`) and confirming that all tested `NAMALWA` subclones harbor integrated SMRV provides actionable guidance for cell repositories.
- **Claim Proportionality:**
  - `[Well Supported]` Continuous primate cell lines curated in major biological resource centers are free of active HIV-1, HTLV-I/-II, HCV, and productive HBV, and neither EBV nor SMRV spreads horizontally across unrelated cell lines during routine culture.
  - `[Well Supported]` 39 of 465 tested primate cell lines (all of B-cell or NK-cell lineage) harbor EBV DNA (episomal, linear, or integrated), and `B95-8`-derived B-LCLs require screening for SMRV co-infection.

### 4. Reproducibility & Data Completeness
- Experimental protocols for Gardella *in situ* lysing gels, Southern blotting, interphase FISH, RT-ELISA, and internal-control plasmid construction are described in thorough, step-by-step detail.
- Completion of the truncated portions of Table 1 (primers for HIV-1, HTLV-I/-II, SMRV, HHV-8), Table 2 (remaining 6 EBV+ cell lines from S–Y), and Table 3 (remaining ~430 negative cell lines) is needed for full archival completeness.
</Blinded Review: TIME_ANON_0500>
