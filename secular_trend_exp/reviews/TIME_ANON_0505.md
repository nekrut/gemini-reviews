<Blinded Review: TIME_ANON_0505>
**Composite Score:** 5.6 / 10.0 (Rigor: 1.9/3.5 | Claims: 1.4/2.5 | Biology: 1.3/2.0 | Reproducibility: 1.0/2.0)
**Bias Category:** Statistical/Design
**Verdict:** Major Revision
**Study Modality:** Wet-Lab Primary Experimental
**Technology Maturity:** Mature/Classical
**Epistemic Stage:** Basic/Mechanistic Discovery

OVERALL_SCORE: 5.6/10
VERDICT: CAVEATS
ESTIMATED_DECADE: 2010s

---

### 1. Executive Summary / SUMMARY
This study characterizes the Porcine deltacoronavirus (PDCoV) nucleocapsid (N) protein by establishing a stable porcine kidney (PK-15) cell line constitutively expressing a C-terminally myc/His-tagged PDCoV N construct (with the overlapping internal NS7 ORF knocked out via synonymous point mutations). The authors examine N protein oligomerization (via non-reducing SDS-PAGE and DSP chemical cross-linking), subcellular localization (via immunofluorescence and nuclear/cytosolic fractionation), cell growth (MTT assay), and host proteomic changes using 2D gel electrophoresis (2DE) coupled with MALDI-TOF peptide mass fingerprinting (PMF), followed by qRT-PCR and Western blot validation of GRP78 and HSC70. While the basic biochemical characterization of N non-covalent oligomerization and transient nucleolar localization is straightforward, the proteomic screen and host-response inferences are undermined by reliance on a single clonal integrant selected for maximum expression, unadjusted multiple hypothesis testing across ~1,090 2DE spots, use of a Posterior-Probability >0.50/uncorrected t-test selection threshold, and absence of authentic viral infection validation.

### 2. STRENGTHS
- **Thoughtful Plasmid Engineering for Overlapping ORFs:** The authors recognized that PDCoV N contains an internal overlapping reading frame encoding the accessory protein NS7 and introduced two synonymous mutations into the N frame (`T24097C/T24109A`) to disrupt the start and fifth codons of NS7 (`pBud-PDCoV-N w/oNS7`), preventing confounding expression of NS7.
- **Orthogonal Biochemical Confirmation of Oligomerization and Localization:** Non-reducing SDS-PAGE alongside a PRRSV N positive control confirms the absence of disulfide-linked dimers (consistent with zero cysteines in the 342-aa sequence), while DSP cross-linking demonstrates higher-order non-covalent multimers. Nucleolar localization is cross-checked across stable PK-15 cells, transiently transfected BHK-21/ST cells, and Sp1/α-tubulin-controlled subcellular fractionation.

### 3. Methodological & Statistical Audit / WEAKNESSES & METHODOLOGICAL AUDIT
- **Single-Clone Selection Bias and Retroviral Integration Confounding:** Out of 10 antibiotic-resistant retroviral clones, the authors selected a single clone ("one PK-PDCoV-N cell clone that constitutively expressed the highest levels of N") and compared it against `PK-Neo`. Retroviral integration is semi-random, and single-cell cloning captures pre-existing clonal heterogeneity in PK-15 cells. Comparing $n=3$ technical/culture replicates of a single high-expressing clone against a control line conflates clonal/integration effects and supraphysiological overexpression stress with specific biological functions of PDCoV N.
- **Uncorrected Multiple Testing in 2DE Proteomics:** The 2DE analysis resolved $1,090 \pm 63$ protein spots across triplicate gels and applied uncorrected Student's $t$-tests ($p < 0.05$) with a 2-fold cutoff, initially flagging 43 spots and excising 10 for MALDI-TOF PMF. With ~1,090 parallel comparisons on $n=3$ gels per group, the expected number of false positives at $\alpha = 0.05$ is ~54 spots—exceeding the 43 spots initially observed. No false discovery rate (Benjamini-Hochberg) correction was applied.
- **Over-interpretation of Chaperone Up-regulation (GRP78 / HSC70):** Constitutive high-level overexpression of a foreign tagged viral protein from a retroviral LTR promoter naturally burdens cellular protein folding machinery. Attributing the ~2-fold induction of general chaperones GRP78 and HSC70 to a specific evolved viral immune/apoptosis-evasion strategy—rather than generic overexpression-induced proteotoxic/ER stress—lacks an irrelevant-protein overexpression control (e.g., GFP-myc/His expressed at comparable levels).
- **Subcellular Fractionation Loading Control Anomaly:** In Figure 3C, $\beta$-actin is used as an "equal protein loading" control across cytosolic and nuclear fractions, showing nearly identical intense bands in both fractions at all time points (24–72 h), even though Sp1 and $\alpha$-tubulin partition cleanly. Moreover, the manuscript notes in the Discussion that authentic PDCoV infection was not tested because the authors did not yet have a cell-culture-adapted isolate.

### 4. Biological / Experimental Grounding & Claim Proportionality
- **PDCoV N forms non-covalently linked oligomers and lacks disulfide bridges:** `[Well Supported]` — Directly supported by primary sequence (0 Cys residues), non-reducing SDS-PAGE, and DSP chemical cross-linking against a PRRSV N positive control.
- **PDCoV N localizes to both the cytoplasm and the nucleolus:** `[Moderately Supported]` — Supported by IFA in stable and transient transfections and cell fractionation, though nucleolar marker co-staining (e.g., fibrillarin/nucleolin) was not performed, relying instead on phase/DAPI morphology.
- **PDCoV N specifically regulates 10 host proteins (including GRP78 and HSC70) to remodel the host cell for viral replication:** `[Overstated]` — Based on unadjusted $t$-tests in a single retroviral clone without an irrelevant-protein overexpression control or viral infection validation.

### 5. Reproducibility & Data Completeness
- **Missing Primer Sequences and Raw Proteomic Spectra:** While cloning and mutagenesis primers (`KNU14-04-N-Fwd/Rev`, `NS7-KO-Fwd/Rev`) and NCBI GI accessions for the 10 identified spots (Table 1) are reported, all qRT-PCR primer sequences for the 10 host genes and porcine $\beta$-actin are withheld ("available upon request"). Raw 2DE spot intensity matrices and MALDI-TOF mass spectra / MASCOT peptide match tables (number of matched peptides per spot) are not deposited.
</Blinded Review: TIME_ANON_0505>
