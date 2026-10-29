# Forensic Review of FEXP_ANON_038

**Manuscript ID:** `FEXP_ANON_038`  
**Overall Score:** **8.6 / 10.0** (Strong / Sound) | **Scientific Core Score:** **7.1 / 8.0**  
* **Score Breakdown:** Rigor: 3.0/3.5 | Claims: 2.3/2.5 | Biology: 1.8/2.0 | Reproducibility: 1.5/2.0

---

## 1. Blinded Metadata Perception

* **Perceived Subfield:** Synthetic Biology / Genetic Code Expansion & Bioorthogonal Protein Labeling in Mammalian Cells.
* **Study Design:** Systematic experimental evaluation of piggyBac (PB) transposon-mediated genomic integration of archaeal ($\text{tRNA}^{\text{Pyl}}/\text{PylRS}$) and bacterial ($\text{tRNA}^{\text{Tyr}}_{\text{CUA}}/\text{AzFRS}$, $\text{tRNA}^{\text{Leu}}_{\text{CUA}}/\text{AnapRS}$) stop-codon suppression machineries across six mammalian cell lines (HEK293T, HEK293, HCT116, A375, U-2 OS, COS-7), encompassing amber (TAG), ochre (TAA), and opal (TGA) single and dual stop-codon suppression and live-cell bioorthogonal click labeling.
* **Primary Methods:** Modular 4x7SK PolIII tRNA / EF1$\alpha$-aaRS-IRES-antibiotic PB transposon plasmids, flow cytometry and FACS clonal isolation, in-gel SPIEDAC/SPAAC/CuAAC fluorescence, anti-GFP/HA/FLAG immunoblotting, ESI-TOF intact protein mass spectrometry, and widefield fluorescence microscopy.

---

## 2. Executive Summary & Editorial Verdict

This study systematically characterizes stable genetic code expansion (GCE) in mammalian cell lines via piggyBac (PB) transposon integration of modular two-plasmid constructs bearing four tandem 7SK PolIII-driven suppressor tRNA repeats and EF1$\alpha$-driven aminoacyl-tRNA synthetase (aaRS) or target reporter genes. Comparing six mammalian cell lines, the authors show that stable amber suppression is highly cell-line dependent—with HCT116 outperforming HEK293T and yielding ~47–50% of wild-type `GFP150AAG` fluorescence—and prove via add-back complementation that suppressor $\text{tRNA}^{\text{Pyl}}$ gene dosage, rather than PylRS protein abundance or catalytic activity, limits suppression efficiency in stable integrants. They extend PB integration to *E. coli*-derived $\text{tRNA}^{\text{Tyr}}_{\text{CUA}}/\text{AzFRS}$ and $\text{tRNA}^{\text{Leu}}_{\text{CUA}}/\text{AnapRS}$ pairs, isolate clonal HCT116 lines suppressing ochre (TAA) and opal (TGA) codons, and achieve dual amber+ochre suppression (`GFP102AzF150CpK`, verified by intact mass spectrometry, and `SynNotch204CpK442AzF-GFP`) with mutually orthogonal SPIEDAC and CuAAC/SPAAC click labeling on live cell surfaces. Crucially, the authors also evaluate five intracellular target proteins and no-reporter controls, transparently demonstrating that off-target suppression of endogenous stop codons and intracellularly retained ncAA/tRNA complexes preclude selective intracellular imaging in stable integrants, confining practical bioorthogonal imaging to extracellular surface receptors labeled with membrane-impermeable dyes.

**Editorial Verdict: Accept with Minor Revisions (Strong / Sound, bordering Exemplary).** This is a rigorously controlled, refreshingly candid experimental study that directly tests both the capabilities and the failure modes of stable mammalian genetic code expansion. The claims are tightly bounded by orthogonal biochemical, mass spectrometric, flow cytometric, and imaging evidence, including a clear "Limitations of the study" section. Only minor editorial and statistical fixes are needed: resolving a lane-numbering swap between the main text and the Figure 1C legend, fixing two typographical errors in construct/dye names, and applying a multiple-testing correction (Dunnett's test) to the multi-group plate-reader comparison in Figure 1C.

### Specific Conclusions and Assessment of Support

* **Suppressor $\text{tRNA}^{\text{Pyl}}$ gene copy number, rather than PylRS expression level or catalytic rate, is the primary bottleneck limiting amber suppression in stable PB integrants: [Well Supported].**  
  Complementation of a low-efficiency stable HEK293T integrant line (Fig. 1C–D, Fig. S1A) demonstrates that overexpressing wild-type PylRS or the catalytically enhanced `IPYE` chimeric PylRS increases synthetase protein levels without improving $\text{GFP}^{150\text{CpK}}$ yield, whereas supplying additional `4xPylT` copies increases GFP yield 2.5- to 3-fold.
* **Stable PB integration in HCT116 cells supports homogeneous single-codon (amber, ochre, opal) and dual-codon (amber + ochre) ncAA incorporation across archaeal and bacterial tRNA/aaRS pairs: [Well Supported].**  
  Flow cytometry against wild-type `GFP150AAG` controls, FACS clonal isolation, orthogonal SPIEDAC/SPAAC in-gel fluorescence, and intact ESI-MS of affinity-purified `GFP102AzF150CpK` (Fig. 4D) unambiguously confirm site-specific dual incorporation without single-ncAA readthrough or cross-incorporation.
* **In stable integrant lines, off-target ncAA incorporation at endogenous stop codons and unincorporated/tRNA-bound ncAAs create high intracellular background, restricting selective bioorthogonal imaging to cell-surface proteins labeled with membrane-impermeable dyes: [Well Supported].**  
  The authors rigorously test an `AnapRS`-only reporter-free cell line (Fig. S2C–E) and five intracellular HA-tagged proteins (tubulin, DAXX, CENP-A, PIGBOS, SARS-CoV-2 M; Fig. S5), showing strong intracellular background in lysates and fixed cells, and then demonstrate clean, selective live-cell surface labeling of `CRFR1` and `SynNotch` using membrane-impermeable `tet488`/`tetCy3` (Fig. 5C).
* **Live-cell dual-color bioorthogonal labeling of `SynNotch204CpK442AzF-GFP` in stable HCT116 clones is achievable via combined SPIEDAC and CuAAC, whereas SPAAC with DBCO-AF647 suffers from non-specific background and CuAAC partially quenches GFP/Cy3 fluorescence: [Well Supported].**  
  In-gel fluorescence of proteolytically processed N-terminal (43 kDa, CpK-tet488/tetCy3) and C-terminal (38 kDa, AzF-alk647/DBCO-647) SynNotch fragments and live-cell microscopy controls (Fig. 6B–D, Fig. S6E–G) directly substantiate both the specific dual-domain labeling and the chemical trade-offs of CuAAC vs. SPAAC.

---

## 3. Forensic Defect Inventory

### 1. Contradictory Lane Assignments Between Main Text and Figure 1C/1D Legend (Pillar 7)
* **WHY:** In the Figure 1C legend (line 29), the transfected plasmids are listed as: *"lane 2: no transfection; lane 3: pAS control plasmid; lane 4: pAS (4xPylT); lane 5: pAS_MmaPylRS (PylRS); and lane 6: pAS_4xMmaPylT/RS (4xPylT and PylRS)."* However, in the main text (Section "PylT gene copy number is limiting...", line 36), lanes 4 and 5 are reversed: *"Transfection with pAS expressing PylRS led to a strongly increased PylRS protein level but no increased amber suppression efficiency (lane 4, Figures 1C and 1D). Addition of pAS with either 4xPylT or 4xPylT/PylRS enhanced GFP 150CpK expression (lanes 5 and 6, Figures 1C and 1D)."*
* **WHAT & HOW:** Verify the gel/bar-chart order in Figures 1C and 1D and harmonize the lane numbering for `pAS (4xPylT)` and `pAS_MmaPylRS` between the main text (line 36) and the Figure 1C legend (line 29).

### 2. Uncorrected Pairwise *t*-Tests and Biological vs. Technical Replicate Ambiguity in Figure 1C (Pillar 4)
* **WHY:** In Figure 1C and STAR Methods ("Quantification of GFP expression" and "Quantification and statistical analysis", lines 110 and 144), the authors state that transfections were performed in quadruplicate with 0.2 mM CpK addition in triplicate, that error bars show the SD of $+{\text{CpK}}$ triplicates, and that multiple treatment lanes were compared using uncorrected two-sided homoscedastic *t*-tests. Computing *t*-tests across technical plate-reader triplicates rather than the $n=4$ independent biological transfections underestimates variance, and running multiple pairwise comparisons against the control without Dunnett's or Holm-Bonferroni correction inflates the family-wise Type I error rate.
* **WHAT:** Compute summary statistics and hypothesis tests in Figure 1C across the $n=4$ biological transfection replicates and apply a multiple-comparison correction.
* **HOW:** Average the technical triplicates within each of the 4 independent transfections first, plot the mean $\pm$ SD across the $n=4$ biological replicates, and report one-way ANOVA with Dunnett's post-hoc test against the untransfected control (lane 2).

### 3. Minor Nomenclature Typos in the Results Text (Pillar 7)
* **WHY:**
  1. In Section "PB transgenesis with E. coli-derived tRNA/aaRS amber suppression pairs in HCT116 cells" (line 57), the reporter construct for `AnapRS` is written as `tRNA Leu CUA /GFP 150CpK integrants` instead of `tRNA Leu CUA /GFP 150TAG integrants` (since CpK is a PylRS substrate, not an AnapRS substrate).
  2. In Section "Live-cell dual-color bioorthogonal labeling..." (line 108), `DBCO-647` is mistyped as `DBCO-467`.
* **WHAT & HOW:** Replace `GFP 150CpK` with `GFP 150TAG` on line 57 and `DBCO-467` with `DBCO-647` on line 108.

---

## 4. Quantitative Rubric Scoring

| Rubric Dimension | Score | Max | Forensic Justification |
| :--- | :---: | :---: | :--- |
| **1. Methodological & Statistical Rigor** | **3.0** | **3.5** | Thorough experimental controls (wild-type `GFP150AAG` benchmark, single-ncAA dropout controls in dual suppression, intact mass spectrometry confirmation, `AnapRS`-only no-reporter off-target control, and side-by-side lysate vs. live-surface labeling). Minor deduction (0.5 pts) for using uncorrected *t*-tests on technical triplicates in Fig. 1C and absence of qPCR transgene copy-number quantification (transparently noted in Limitations). |
| **2. Claim-to-Evidence Alignment** | **2.3** | **2.5** | Claims are exceptionally well-calibrated; the authors explicitly highlight where stable PB integration fails (intracellular protein labeling and SPAAC DBCO background) rather than overstating the generality of the GFP reporter results. |
| **3. Data Integrity & Biological Plausibility** | **1.8** | **2.0** | Orthogonal biochemical (SDS-PAGE in-gel fluorescence, Western blot, ESI-MS) and cellular (flow cytometry, microscopy) validation across 6 mammalian cell lines and 8 target proteins. |
| **4. Reproducibility & Data Integrity** | **1.5** | **2.0** | Plasmids deposited in Addgene, raw uncropped blots/images and cell line tables deposited in Mendeley Data (`doi:10.17632/tgc7mbv5xp`), and full reagent identifiers provided. Deducted 0.5 pts for the lane 4/5 swap between the main text and Fig. 1C legend and minor construct/dye typos (`GFP 150CpK` in line 57, `DBCO-467` in line 108). |
| **Scientific Core Score** | **7.1** | **8.0** | Sum of Rigor + Claims + Biology (`3.0 + 2.3 + 1.8`). |
| **Total Composite Score** | **8.6** | **10.0** | **Strong / Sound** (`3.0 + 2.3 + 1.8 + 1.5`). |
