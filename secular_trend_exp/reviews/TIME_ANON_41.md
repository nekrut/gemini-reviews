# Blinded Review: TIME_ANON_41
**Composite Score:** 5.6 / 10.0 (Rigor: 1.7/3.5 | Claims: 1.3/2.5 | Biology: 1.2/2.0 | Reproducibility: 1.4/2.0)
**Bias Category:** Uncontrolled Multiple Testing & Mechanistic Overclaiming (ChIP-Free Direct Binding Claims / Formulaic Signaling Cascade)
**Verdict:** Major Revision
**Study Modality:** Hybrid Computational + Wet-Lab Functional Validation
**Technology Maturity:** Commodity/Hype-Cycle Template
**Epistemic Stage:** Basic/Mechanistic Discovery

---

### 1. Executive Summary

This manuscript proposes a six-step mechanotransduction cascade (`Piezo1 -> Ca2+ -> calcineurin -> NFAT2/HDAC1 -> BHLHE40 -> SLC7A11`) in vascular endothelial cells that suppresses Erastin-induced ferroptosis in vitro and attenuates lipopolysaccharide (LPS)-induced pulmonary vascular injury in mice. The authors combine bulk RNA sequencing in Yoda1-stimulated mouse brain microvascular endothelial cells (MBMECs) and *BHLHE40*-perturbed human umbilical vein endothelial cells (HUVECs) with pharmacological inhibitor screens, shRNA knockdowns, HeLa luciferase reporter assays, and adeno-associated virus (AAV9-TIE)-mediated endothelial *Bhlhe40* overexpression in an acute endotoxemia mouse model. Raw RNA-seq datasets are deposited under NCBI BioProject `PRJNA1297692` and CNCB GSA `CRA006427`.

While the multi-tiered experimental effort is extensive, the manuscript exhibits several methodological, pharmacological, and inferential flaws typical of formulaic multi-node signaling papers. First, the statistical analysis section contradicts every figure legend in the paper, and multi-group experiments ($n = 3$ biological replicates across 4–8 conditions) are analyzed with unadjusted two-group Student's $t$-tests. Second, the Abstract and main text claim direct promoter binding by NFAT2–HDAC1 to *BHLHE40* and by BHLHE40 to *SLC7A11* without a single chromatin immunoprecipitation (ChIP) or electrophoretic mobility shift assay (EMSA) in endothelial cells, relying exclusively on truncated plasmid luciferase assays in non-endothelial HeLa cells. Third, several pharmacological and cell-identity descriptions are internally contradictory or biologically inaccurate (e.g., misclassifying Ruthenium Red as an L-type $\text{Ca}^{2+}$ channel blocker, classifying ERK1/2 and HDACs as transcription factors, using suprapharmacological $20\ \mu\text{M}$ abexinostat for 12 h, and contradicting whether HDAC1-H141A experiments were conducted in HeLa cells or HUVECs).

---

### 2. Methodological & Statistical Audit

* **Contradiction Between Stated Statistical Methods and Figure Execution (Unadjusted Multiple Comparisons at $n = 3$):**
  In the *Statistical analysis* section, the authors state that two-group comparisons used unpaired Welch's $t$-tests and multigroup comparisons used one-way ANOVA followed by Tukey's post-hoc test. However, every figure legend (Figs. 1–7) explicitly states: *"Statistical significance was determined by unpaired Student's t-test."* Nearly all quantitative panels involve multi-group or factorial designs—including 5-timepoint kinetics (Figs. 1C, 2F), 8-group kinase/phosphatase inhibitor screens (Fig. 2D), 5-group NFAT isoform knockdowns (Fig. 2H), and 4-to-6-group combinatorial genetic/pharmacological rescue experiments (Figs. 5D–H, 6G, 7B–I)—with only $n = 3$ independent biological replicates per group in vitro ($df = 4$ per pairwise test). Applying unadjusted pairwise Student's $t$-tests across multi-group designs severely inflates the family-wise Type I error rate and fails to test the interaction terms required for epistatic rescue claims.

* **Undocumented Spatial Separation in Orbital Shaker Shear Stress Assays:**
  In the *Shear stress application* section, HUVECs are seeded as a confluent monolayer into standard $3.5\ \text{cm}$ 6-well plates and shaken at 210 rpm for 5 days, which generates disturbed flow ($4.8\ \text{dyn/cm}^2$) in the center of the well and laminar flow ($11.1\ \text{dyn/cm}^2$) in the $8\ \text{mm}$ peripheral annulus of the same well. Yet the Methods state *"Static controls were cultured identically in the absence of shear stress"* and never describe any physical microdissection, regional scraping, or concentric ring barrier used to isolate peripheral (UF) from central (DF) cells within the same well prior to TRIzol or RIPA lysis (Figs. 1D, 1E, 1H, 1I, 4E, 4F).

* **Internal Contradictions in Cell Line Identity and Dominant-Negative Assumptions:**
  In the Results text (Section *HDAC1 facilitates Piezo1/NFAT2-mediated transactivation...*), the authors state that they *"co-expressed NFAT2 with the H141A deacetylase-deficient HDAC1 mutant in HeLa cells [39]"* (Fig. 3I, J). Conversely, the Fig. 3I, J legend states that *"WT and HDAC-H141A mutant Huvecs were treated with 5 μM Yoda1."* Furthermore, neither the text nor the Methods explain how overexpressing a catalytically inactive HDAC1-H141A point mutant in cells that retain endogenous wild-type *HDAC1* expression completely abolishes Yoda1-induced *BHLHE40* transcription without endogenous *HDAC1* knockout or knockdown.

* **Bioinformatics Pipeline Version Inaccuracies:**
  In *RNA sequencing and data analysis*, the authors state that raw reads *"underwent FastQC-based quality control and Trimmomatic filtering"* and later state *"Raw sequencing data underwent FastQC v0.20.1 with default parameters. This process involved the removal of adapter sequences..."* FastQC is a read-quality visualization tool (whose versions are `0.11.x` / `0.12.x`) and cannot trim adapters; `v0.20.1` is a version of `fastp`. Similarly, the authors cite *"Limma (v4.4)"* running in *"R (v4.1.2)"*, whereas Bioconductor `limma` in R 4.1.2 is version `3.50.x` (no `v4.4` of `limma` exists).

---

### 3. Biological / Experimental Grounding & Claim Proportionality

* **Claim that NFAT2–HDAC1 Directly Binds the *BHLHE40* Promoter and BHLHE40 Directly Binds the *SLC7A11* Promoter: `[Overstated]`**
  The Abstract states that *"NFAT2 recruits HDAC1 to form a transcriptional complex that directly drives BHLHE40 expression. BHLHE40 then binds the SLC7A11 promoter."* In reality, the authors only performed JASPAR motif scanning and dual-luciferase reporter assays in heterologous HeLa cells using plasmid promoters with binding-site deletions (Figs. 2K–M, 3H, 4N–O). As acknowledged only at the end of the Discussion, no ChIP-qPCR, ChIP-seq, CUT&Tag, or EMSA was performed in HUVECs or primary endothelial cells to demonstrate endogenous physical occupancy of NFAT2, HDAC1, or BHLHE40 at the native *BHLHE40* or *SLC7A11* chromatin loci under shear stress.

* **Pharmacological Specificity and Misclassification Errors: `[Methodologically Flawed]`**
  1. In Results (Section 2), Ruthenium Red is described as *"the L-type calcium channel blocker ruthenium red (RR)."* Ruthenium Red is not an L-type voltage-gated $\text{Ca}^{2+}$ channel blocker; it is a non-selective polycationic inhibitor of ryanodine receptors, TRP channels, the mitochondrial calcium uniporter, and mechanically activated channels including Piezo1/2.
  2. In Results (Section 3), ERK1/2, ERK5, and HDACs are referred to as *"other Piezo1 downstream transcription factors, including extracellular signal-regulated kinases 1/2 (ERK1/2), activator protein-1 (AP-1), histone deacetylases (HDAC), and extracellular signal-regulated kinase 5 (ERK5)."* Kinases and histone deacetylases are enzymatic signaling modifiers, not transcription factors.
  3. The pan-HDAC inhibitor abexinostat (which has nanomolar potency against HDAC1/2/3/6/8/10, $\text{IC}_{50} < 100\ \text{nM}$) was applied to HUVECs at $20\ \mu\text{M}$ for 12 hours (Fig. 3A–E). At $>200$-fold above its $\text{IC}_{50}$, a 12-hour exposure to a hydroxamic acid pan-HDAC inhibitor causes broad transcriptional repression and apoptosis; moreover, abexinostat inhibits all class I and II HDACs and cannot by itself isolate HDAC1 specificity.

* **Claim that Endothelial BHLHE40 Overexpression Protects Against Sepsis via SLC7A11-Mediated Ferroptosis Suppression In Vivo: `[Fragile]`**
  In Fig. 7, mice transduced with `AAV9-TIE-mCherry-Bhlhe40-Flag` show reduced Evans Blue lung extravasation, neutrophil infiltration, cytokine levels, and plasma MDA at 48 h post-LPS. However, (i) systemic AAV9 has strong tropism for myocardium, hepatocytes, and skeletal muscle and poor specificity for pulmonary microvascular endothelium even with a TIE promoter (and no co-staining quantifying percentage of CD31+ vs CD31- cells expressing Flag in lung/liver/heart is provided in the main figures), (ii) plasma MDA is a non-specific systemic lipid peroxidation byproduct rather than a specific marker of endothelial ferroptosis, and (iii) no in vivo epistasis experiment (such as *Slc7a11* knockdown/inhibition or *Bhlhe40* loss-of-function under shear/sepsis) was performed to demonstrate that the in vivo anti-inflammatory protection requires SLC7A11 or ferroptosis inhibition.

---

### 4. Reproducibility & Data Completeness

* **Strengths:** Raw bulk RNA-seq datasets for HUVECs (`PRJNA1297692`) and MBMECs (`CRA006427`) are deposited in public repositories. Vendor catalog numbers and CAS numbers for small-molecule inhibitors and antibodies are listed in the Methods, and shRNA/siRNA/primer sequences are referenced in Supplementary Tables S1–S4.
* **Deficiencies Requiring Correction:**
  1. The physical protocol for separating UF (peripheral annulus) from DF (central core) HUVECs inside 6-well plates on the orbital shaker is omitted and must be specified.
  2. The plasmid construction, delivery method (lentivirus vs transient transfection), and cell type (HeLa vs HUVEC) for the `HDAC1-H141A` experiment (Fig. 3I, J) are missing from the Materials and Methods and contradictory between text and legend.
  3. All multi-group comparisons across Figs. 1–7 must be re-analyzed using one-way or two-way ANOVA with appropriate post-hoc multiple-testing corrections (Tukey's or Dunnett's test), and exact $p$-values and $F$-statistics should be reported.
