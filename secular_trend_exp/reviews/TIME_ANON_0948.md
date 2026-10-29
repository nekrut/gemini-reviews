<Blinded Review: TIME_ANON_0948>
**Composite Score:** 8.2 / 10.0 (Rigor: 3.0/3.5 | Claims: 2.0/2.5 | Biology: 1.8/2.0 | Reproducibility: 1.4/2.0)
**Bias Category:** None (Methodologically Sound)
**Verdict:** Minor Revision
**Study Modality:** Hybrid Computational + Wet-Lab
**Technology Maturity:** Mid-Stage High-Throughput
**Epistemic Stage:** Basic/Mechanistic Discovery

OVERALL_SCORE: 8.2/10
VERDICT: PASS
ESTIMATED_DECADE: 2020s

---

### 1. Executive Summary / SUMMARY
This comprehensive virology and proteomics study demonstrates that influenza A virus (IAV; strains WSN and PR8) infection triggers a rapid, replication-dependent upregulation of host and viral poly(ADP-ribosyl)ation (PARylation) across human (A549), chicken (DF-1), pig (PK15), and bat (Tb1Lu) cells. Using enzymatic labeling of terminal ADP-ribose coupled to mass spectrometry (`ELTA-MS`, utilizing OAS1-mediated $N^6$-(6-azido)hexyl-dATP tagging, DBCO-agarose click capture, and NudT16 phosphodiesterase cleavage across 3 independent experiments in biological duplicate $\times$ technical triplicate), the authors map 4,542 unique ADP-ribosylation sites on 1,135 host proteins and >100 sites across 8 viral proteins (with viral nucleoprotein `NP` most heavily modified, containing 27 total and 18 high-confidence sites). Combining `ELTA-MS` with direct $^{32}\text{P}$-dATP OAS1 polymer-length urea-PAGE assays reveals a striking mechanistic insight: IAV infection does not substantially alter *which* protein sites carry ADP-ribose (~75% site overlap between mock, infected, and $\text{H}_2\text{O}_2$-treated cells), but converts pre-existing mono(ADP-ribosyl)ated (MARylated) or low-occupancy sites into long PAR chains. Alanine scanning of 18 ADPr sites on `NP` shows that ablating modification at RNA-binding groove / functional residues (`D34A`, `S69A`, `E294A`) significantly increases viral polymerase minigenome activity. Furthermore, the authors show that viral `NS1` suppresses global and RNP-associated PARylation in a strain-specific (`PR8 NS1` > `WSN NS1`), dsRNA-binding-dependent (`NS1 R38A/K41A` loses suppression) manner, and use selective PARP inhibitors (`Olaparib`, `Rucaparib`, `AG14361` vs tankyrase inhibitor `XAV939`), two clonal CRISPR-Cas9 `PARP1` knockout A549 lines, and Sleeping Beauty transposon complementation (`WT PARP1`, catalytically dead `E988A`, MAR-only `E988K`, and caspase-uncleavable `D214A`) to prove that `PARP1` generates the infection-induced PARylation and restricts single- and multi-cycle IAV replication by ~5-fold.

### 2. Methodological & Statistical Audit / STRENGTHS & WEAKNESSES & METHODOLOGICAL AUDIT

#### STRENGTHS
- **Resolution of the Blotting vs. Mass Spectrometry Paradox via Polymer-Length Gel Analysis:** Observing massive PAR upregulation by Western blot alongside nearly invariant site counts by `ELTA-MS` (which cleaves PAR down to phosphoribose with NudT16) could easily have been misinterpreted; the authors resolve this cleanly by isolating total ADPr chains with KOH/proteinase K and end-labeling with OAS1 + $\alpha\text{-}^{32}\text{P}$-dATP on 15% urea-PAGE (Figs. 2F, 3C), proving that infection drives PAR chain extension rather than de novo target recruitment.
- **Rigorous Genetic & Chemical Dissection on Both Host (`PARP1`) and Virus (`NS1`, `NP`):**
  1. Two independent clonal `PARP1-/-` A549 lines complemented with WT, catalytic-dead (`E988A`), and mono-ADP-ribosylating (`E988K`) `PARP1` alleles establish `PARP1` chain elongation as the causal host mechanism.
  2. Reciprocal chimeric viruses (`WSN-NS1(PR8)` and `PR8-NS1(WSN)`), $\Delta\text{NS1}$ deletion mutants, and the RNA-binding mutant `NS1 R38A/K41A` (note: written as `K38A/R41A` in Fig. 4B legend and Methods line 36, and `R38A/K41A` in main text line 64) cleanly map viral antagonism to `NS1`.
- **Stringent Proteomic Filtering & Artifact Control:** Inclusion of `PJ-34` and `ADP-HPD` in lysis buffers prevents post-lysis PARP/PARG artifacts; FragPipe/PTMProphet localization $\ge 0.9$, removal of misassigned carbamidomethyl-Cys sites, and requiring $\text{score} \ge 4$ across technical replicates ensure high-confidence site calls.

#### WEAKNESSES & METHODOLOGICAL AUDIT
- **Missing Proteomics Repository Accession (PRIDE/MassIVE) and Incomplete LC Column Text:** While the paper references Supplementary Data 1–5 and a Source Data file, no public mass spectrometry repository accession (e.g., ProteomeXchange/PRIDE or MassIVE ID) is provided in the text for the raw `.RAW`/`.mzML` files. Additionally, Methods line 82 contains an unedited template placeholder: *"coupled to an EASY-nLC 1200 system (Thermo) with a column type and stationary phase."*
- **Unresolved Apoptosis / Caspase-Cleavage Coupling (`PARP1 D214A`):** As the authors candidly note, `WSN` and `PR8\Delta NS1` induce both stronger PARylation and stronger apoptotic caspase cleavage of `PARP1` and `NP` (Figs. 3A, 4A), and complementing `PARP1` KO cells with the caspase-uncleavable mutant `PARP1 D214A` *failed* to restore PARylation (`Fig. S6B`). While PARP inhibitors did not block `NP` cleavage (Fig. 6A), the possibility that DNA fragmentation/chromatin nicking during virus-induced apoptosis is the proximal trigger activating nuclear `PARP1` (which is suppressed by `NS1`'s anti-apoptotic activity) is not directly tested (e.g., via pan-caspase inhibition with Z-VAD-FMK).
- **Modest Antiviral Effect Size in `PARP1` KO Cells:** In both multi-cycle (`MOI 0.01`) and single-cycle (`MOI 5`) replication assays in A549 cells, `PARP1` knockout increases viral titers by ~5-fold at early time points (8–24 hpi) before converging to identical plateau titers at 48–72 hpi (Fig. 7B–C), and viral growth was not tested in `PARP1` KO cells using `PR8\Delta NS1` (where NS1 antagonism of PARP1 is removed).

### 3. Biological / Experimental Grounding & Claim Proportionality
- **Claim 1:** IAV infection induces global PARylation and modification of viral proteins (especially `NP`), reflecting extension of PAR chains on a largely conserved core ADP-ribosylome rather than modification of novel protein targets. `[Well Supported]`
- **Claim 2:** `PARP1` is the primary enzyme responsible for IAV-induced PARylation and slows early viral replication (~5-fold), while an unknown PARP mediates baseline MARylation. `[Well Supported]`
- **Claim 3:** Viral `NS1` antagonizes host PARylation in a strain-dependent manner requiring its dsRNA-binding residues (`R38/K41`). `[Well Supported]`

### 4. Reproducibility & Data Completeness
- **Reagents & Software:** Exceptional detail on CRISPR sgRNA sequences, chemical inhibitor catalog numbers and concentrations, FragPipe (`v20.0`)/MSFragger (`v3.8`)/PTMProphet parameters, and R (`v4.3.2`) filtering logic.
- **Minor Omissions:** Placeholder text in LC-MS/MS column description (`"with a column type and stationary phase"`) and absence of a ProteomeXchange/PRIDE accession number in the main text.
</Blinded Review: TIME_ANON_0948>
