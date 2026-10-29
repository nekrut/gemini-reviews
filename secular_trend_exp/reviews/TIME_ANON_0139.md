</Agent System Instructions>
<Blinded Review: TIME_ANON_0139>
**Composite Score:** 8.2 / 10.0 (Rigor: 2.9/3.5 | Claims: 2.1/2.5 | Biology: 1.7/2.0 | Reproducibility: 1.5/2.0)
**Bias Category:** None (Methodologically Sound)
**Verdict:** Minor Revision
**Study Modality:** Wet-Lab Primary Experimental
**Technology Maturity:** Mid-Stage High-Throughput
**Epistemic Stage:** Basic/Mechanistic Discovery

---

### 1. Executive Summary
This molecular virology study demonstrates that a parallel G-quadruplex (G4) structure located at $-61$ to $-19\text{ bp}$ in the human cytomegalovirus (HCMV) *UL146* promoter acts as a positive cis-regulatory element bound directly by the viral immediate-early 2 (IE2) transactivator. Following an initial RNA-seq screen in N-methyl mesoporphyrin IX (NMM)-treated HCMV-infected fibroblasts that identified the *UL146–UL132* polycistronic locus as strongly downregulated, the authors characterize four overlapping putative G4-forming sequences (`PQS1`–`PQS4`) and their G-to-A mutant controls using circular dichroism (CD), NMM fluorescence turn-on in $\text{K}^+$ vs. $\text{Li}^+$, and native PAGE ($\pm 40\%$ PEG200). They show via biotin-oligo pull-down that purified recombinant $\text{His}_6\text{-IE2(87–579)}$ binds wild-type `PQS1`–`PQS4` G4s (inhibited by the G-quartet ligand NMM but not by the groove binder Peimine), validate G4-dependent transactivation in luciferase reporter assays, and construct both a G4-mutant HCMV Toledo BAC (`UL146(G4m)`) and its revertant virus, confirming reduced BG4 and IE1/IE2 ChIP occupancy and dramatic reductions in *UL146* and *UL132* transcription (especially at low MOI of 0.2). The experimental design is thorough and multi-layered, with only minor methodological and reporting caveats.

### 2. Methodological & Statistical Audit
- **Orthogonal Biophysical and Genetic Controls:** The study pairs every wild-type G4 assay with well-designed point-mutant controls (`PQS1m`–`PQS4m`), ionic controls ($\text{KCl}$ vs. $\text{LiCl}$), ligand-mode controls (NMM $\pi$-stacking vs. Peimine groove-binding), and—most importantly—a full BAC-engineered revertant virus alongside the `UL146(G4m)` mutant virus in primary human fibroblasts (Fig. 7). This rules out off-target BAC mutagenesis artifacts.
- **Discrepancy in MOI and Unreplicated RNA-Seq Screen:** In the Results text (line 34), the authors state that HF cells were infected at an **MOI of 5** for the 96 h RNA-seq experiment, whereas the Figure 1B caption (line 37) states **MOI of 2**. The authors transparently note that the RNA-seq screen was performed as a single replicate ($n = 1$), and appropriately validate the top hit (*UL146*) and control (*UL112*) with replicated dose-response RT-qPCR (Fig. 1D).
- **ChIP Antibody Specificity Caveat:** In Figure 7E, the authors transparently note that because their IE2-specific antibody failed in ChIP, they used an antibody recognizing the shared N-terminal exon 2/3 region of both IE1 and IE2. While IE1 is not known to bind G4s directly, the ChIP readout technically measures combined IE1/IE2 occupancy at the *UL146* promoter. Also, in the text (line 85), the ChIP results are misreferenced as `(Fig. 7D)` instead of `(Fig. 7E)`.
- **Statistical Testing:** All multi-group comparisons (e.g., dose-response curves in Fig. 1D, 5C, 6C and multi-virus/multi-timepoint comparisons in Fig. 7C–E) are analyzed via pairwise Student's $t$-tests without correction for multiple comparisons (e.g., Dunnett's or Tukey's post-hoc tests), though the primary biological effect sizes (6-fold to 3,000-fold reduction in *UL146* mRNA in the mutant virus relative to both WT and revertant) are large and unambiguous.

### 3. Biological / Experimental Grounding & Claim Proportionality
- **Claim 1:** *"A parallel intramolecular G4 is formed in the UL146 promoter and is directly targeted by IE2."* — `[Well Supported]`. CD spectra (265 nm positive / 240 nm negative peaks), $\text{K}^+$-dependent NMM fluorescence turn-on, native PAGE under PEG200 molecular crowding (`PQS4`), BG4 ChIP in infected cells, and direct pull-down of purified $\text{IE2(87–579)}$ provide convergent biophysical and in-cell evidence.
- **Claim 2:** *"IE2 binding to G4 is necessary for efficient UL146 transcription during virus infection, especially at low multiplicity of infection."* — `[Well Supported]`. Demonstrated both in transient co-transfection reporters (where `UL146(G4m)` abolishes IE2 transactivation) and in the context of the complete viral genome via `UL146(G4m)` vs. WT and revertant BAC viruses. The authors also thoughtfully discuss why residual transcription occurs at high MOI (potential contribution of upstream *crs*-like, AP-1, AP-2, and CREB sites).

### 4. Reproducibility & Data Completeness
- Oligonucleotide sequences (`PQS1`–`PQS4` and mutants, `cMyc-G4`, scrambled), GenBank strain accessions, RT-qPCR and ChIP-qPCR primer sequences, buffer compositions, and BAC recombineering steps are clearly documented in the figures and Methods.
- However, the raw/processed RNA-seq dataset (referenced only as File S1) does not have a public repository accession (e.g., NCBI GEO/SRA) listed in the Data Availability statement, and the RT-qPCR primers for *UL132* and *UL112* (shown in Fig. 1D and 7D) are omitted from the "Real-time qPCR" Methods section (which only lists primers for *UL146* and *GAPDH*).
</Blinded Review: TIME_ANON_0139>
