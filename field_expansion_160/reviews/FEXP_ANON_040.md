# Forensic Review of FEXP_ANON_040

**Manuscript ID:** `FEXP_ANON_040`  
**Overall Score:** **6.6 / 10.0** (Mixed / Salvageable) | **Scientific Core Score:** **5.1 / 8.0**  
* **Score Breakdown:** Rigor: 2.1/3.5 | Claims: 1.6/2.5 | Biology: 1.4/2.0 | Reproducibility: 1.5/2.0

---

## 1. Blinded Metadata Perception

* **Perceived Subfield:** Plant Molecular Evolution & Structural Bioinformatics / Developmental Transcription Factors (Poaceae: *RAMOSA1* / *SUPERMAN* C2H2 Zinc Finger Family).
* **Study Design:** Comparative phylogenetic, syntenic, motif, promoter, subcellular localization, and molecular dynamics (MD) study of *SUPERMAN* (*SUP*), *RAMOSA1* (*RA1*), and *RA1-like A/B* across 48–50 embryophyte genomes (73 protein sequences; 35 grass sequences across 16 Poaceae species), with transient GFP-fusion confocal microscopy in *Nicotiana benthamiana*.
* **Primary Methods:** BLASTp + MEME v5.5 + MAFFT E-INS-i alignment, MrBayes 3.2.6 Bayesian phylogenetics, Phytozome GENESPACE chromosomal collinearity, *Agrobacterium* transient expression (`35S:GFP:RA1` / `SvRA1-like A/B`) with DAPI confocal microscopy, PsiPred 4.0 / DisoPred 3.1 secondary structure/disorder prediction, 1 $\mu$s GROMACS 2021.5 MD simulation (`AMBER99SB-ILDN`), and XSTREME / JASPAR CORE 2022 promoter motif scanning.

---

## 2. Executive Summary & Editorial Verdict

This study investigates the evolutionary origin and structural/regulatory diversification of the maize meristem-determinacy C2H2 zinc finger transcription factor RAMOSA1 (RA1) across land plants. Using 73 amino acid sequences from 48 embryophyte species, Bayesian phylogenetic inference, and grass chromosomal synteny (GENESPACE across maize, *Setaria viridis*, and rice), the authors show that *RA1* originated from two successive duplications of a *SUPERMAN* (*SUP*)-like ancestor near the divergence of the BOP and PACMAD grass clades, yielding three syntenic paralogous lineages (`RA1-like A`, `RA1-like B`, and PACMAD-retained `RA1`). Using transient agro-infiltration of GFP fusions in *Nicotiana benthamiana* leaves, they experimentally demonstrate that maize RA1 and *S. viridis* RA1, RA1-like A, and RA1-like B all localize to the nucleus despite lacking a canonical NLS. They further compare conserved C-terminal EAR-like motifs (Motif 2), run 1 $\mu$s GROMACS molecular dynamics simulations on the zinc finger domain of SUP (`QALGGH`) and RA1 (`QGLGGH`) showing that the Ala $\to$ Gly substitution does not increase local backbone flexibility, and catalog putative TF binding motifs in 2-kb upstream promoter regions across 16 grass species.

**Editorial Verdict: Minor-to-Moderate Revision (Mixed / Salvageable).** The combination of Bayesian phylogenetics, grass microsynteny, and in vivo confocal nuclear localization of the previously uncharacterized `RA1-like A` and `RA1-like B` paralogs provides solid support for the two-step duplication model and nuclear function of these proteins. However, three methodological issues in the computational sections require correction or qualification: (1) the GROMACS molecular dynamics protocol for the C2H2 zinc finger peptide (Section 2.6) takes the apo AlphaFold model of RA1 without documenting how the structural $\text{Zn}^{2+}$ ion and its four coordinating Cys2-His2 residues were parameterized, uses the legacy Berendsen thermostat/barostat ($n=1$ trajectory), and likely misstates the backbone RMSD unit as $<0.5\text{ \AA}$ instead of $<0.5\text{ nm}$ (or left position restraints active); (2) pre-filtering BLASTp hits to discard sequences with truncated C-terminal EAR motifs (Section 2.1) introduces ascertainment bias against detecting motif loss or pseudogenization; and (3) XSTREME promoter motif scanning across tiny clades of 3–5 closely related species without a phylogenetic conservation null model conflates passive sequence identity with selective retention of TF binding sites.

### Specific Conclusions and Assessment of Support

* ***RA1* originated from two consecutive grass-specific gene duplications of a *SUPERMAN*-like ancestor around the BOP/PACMAD split, producing three syntenic paralogous lineages (*RA1-like A*, *RA1-like B*, and PACMAD-restricted *RA1*): [Well Supported].**  
  The MrBayes consensus phylogeny (Figs. 1 and 2a, $\text{PP} \ge 0.9$ on key grass nodes) is independently corroborated by conserved chromosomal collinearity across *Oryza sativa*, *Setaria viridis*, and *Zea mays* (Fig. S6).
* **Maize RA1 and *Setaria viridis* RA1, RA1-like A, and RA1-like B localize to the nucleus in planta despite lacking a classical nuclear localization signal: [Well Supported].**  
  Transient expression of `35S:GFP` translational fusions in *N. benthamiana* epidermal cells with DAPI counterstaining across independent biological replicates (Fig. 3) clearly confirms nuclear localization for all four proteins, though inclusion of a free `35S:GFP` control image in Fig. 3 would help visually distinguish active nuclear accumulation from passive diffusion of ~47 kDa GFP fusions through nuclear pores.
* **The `A -> G` substitution in the `QGLGGH` zinc finger motif of RA1 does not increase local $\alpha$-helix backbone flexibility compared to the `QALGGH` motif of SUP: [Fragile].**  
  While testing this long-standing structural hypothesis via MD is well motivated, Section 2.6 does not state whether the essential tetrahedral $\text{Zn}^{2+}$ cofactor ion (absent from standard AlphaFold coordinate outputs) and deprotonated `CYM` thiolates were included in the GROMACS topology, relies on a single 1 $\mu$s trajectory coupled with the non-canonical Berendsen thermostat/barostat, and reports an implausibly small backbone RMSD ($<0.5\text{ \AA}$ over 1 $\mu$s for a 52-residue peptide, suggesting either a $\text{nm} \to \text{\AA}$ unit conversion error from GROMACS output or residual position restraints).
* **Divergence of C-terminal EAR-like motifs and upstream promoter cis-regulatory elements reflects subfunctionalization and neofunctionalization across the three grass paralogs: [Moderately Supported].**  
  Lineage-specific differences in the copy number (2 vs. 3) and leucine spacing of the C-terminal EAR-like Motif 2 (Fig. 2b) are clear and biologically relevant to REL2/TOPLESS co-repressor binding. However, promoter motif claims from XSTREME on subsets of only $n=3\text{--}6$ orthologous 2-kb sequences lack controls for background phylogenetic sequence conservation, and no expression data across grass tissues are analyzed to confirm regulatory divergence.

---

## 3. Forensic Defect Inventory

### 1. Missing $\text{Zn}^{2+}$ Coordination Details, Unit Error ($<0.5\text{ \AA}$), and Berendsen Coupling in Zinc Finger MD Simulations (Pillars 3, 6 & 7)
* **WHY:** In Sections 2.6 and 3.4.2, the authors simulate the C2H2 zinc finger fragments of SUP (PDB `1NJQ`, aa 42–78) and RA1 (AlphaFold model, aa 32–83) in GROMACS 2021.5. Three technical issues affect this simulation:
  1. Standard AlphaFold models do not contain the $\text{Zn}^{2+}$ cofactor ion required to maintain the C2H2 fold, and Section 2.6 never states whether a $\text{Zn}^{2+}$ ion was grafted into the RA1 model or how the $\text{Zn}^{2+}$–Cys2His2 coordination sphere was parameterized in `AMBER99SB-ILDN`.
  2. Line 132 reports *"average RMSD values lower than 0.5 Å"* across 1 $\mu$s at 300 K. Because GROMACS outputs distances in **nanometers (nm)** by default, an unrestrained 52-residue peptide with disordered terminal tails cannot maintain an average RMSD $< 0.05\text{ nm}$ ($0.5\text{ \AA}$); either $0.5\text{ nm}$ ($5.0\text{ \AA}$) was misread as $0.5\text{ \AA}$, or the heavy-atom position restraints applied during the simulated annealing step (Section 2.6, step 3, line 74) were inadvertently retained during the 1 $\mu$s production run.
  3. The Berendsen thermostat and barostat used in step 4 do not generate a true canonical ensemble and suppress structural fluctuations (directly impacting RMSF comparisons in Fig. 5b), and only $n=1$ trajectory was run per peptide.
* **WHAT:** Clarify the $\text{Zn}^{2+}$ coordination parameterization, check whether position restraints were released during the production run, and verify the RMSD units ($\text{\AA}$ vs. $\text{nm}$) in Section 3.4.2 and Fig. S11b.
* **HOW:** Document the exact protonation states of the coordinating Cys/His residues and $\text{Zn}^{2+}$ force-field parameters in Section 2.6, confirm that `define = -DPOSRES` was removed in step 4, correct the RMSD unit if GROMACS `nm` output was mislabeled as `Å`, and ideally run 3 independent velocity replicates using the velocity-rescaling (`v-rescale`) thermostat and Parrinello-Rahman barostat.

### 2. Ascertainment Bias from Pre-Filtering Sequences Without Complete C-Terminal EAR Motifs (Pillars 2 & 3)
* **WHY:** Section 2.1 (line 24) states: *"Based on MEME exploratory scans, sequences containing an incomplete zinc finger motif and/or truncated C-terminal EAR motif were discarded."* Discarding homologs with truncated C-terminal EAR motifs *before* phylogenetic analysis creates circularity when Section 3.2 and the Discussion subsequently conclude that all retained grass homologs conserve two to three C-terminal EAR motifs, and may also cause genuine diverged *RA1* orthologs in the BOP clade to be misclassified as "lost."
* **WHAT:** Separate structural quality filtering (removing fragmented genome annotation artifacts) from evolutionary motif filtering (removing full-length genes that have lost the C-terminal EAR motif).
* **HOW:** List all BLASTp hits discarded by the MEME filter in Table S1, verify whether any discarded sequence in the BOP clade is located in the syntenic *RA1* chromosomal block, and state explicitly in Section 3.2 that conservation of the C-terminal EAR motif was partially enforced as an inclusion criterion in Section 2.1.

### 3. Uncontrolled Phylogenetic Conservation in Small-Sample Promoter Motif Scans (Pillars 4 & 5)
* **WHY:** In Section 2.7 (line 79), the 35 grass promoters are split into 8 sub-datasets containing only $n=3$ to $n=6$ sequences each (e.g., 3 Andropogoneae sequences for `RA1-like A` and `RA1-like B`). Running XSTREME ($E < 0.05$) on 3–4 closely related grass promoters (2 kb each) detects any conserved sequence block that happens to match one of hundreds of short degenerate plant JASPAR PWMs.
* **WHAT:** Temper the functional conclusions drawn from the 33 putative JASPAR TF motif families in Section 3.5 and 4.1.3.
* **HOW:** Emphasize motifs that are either experimentally validated by ChIP-seq/genetics in the literature (such as the Andropogoneae ARF motifs reported by Strable et al.) or conserved across both PACMAD and BOP clades ($n \ge 10$ species), and frame the clade-restricted 3-species XSTREME hits as preliminary bioinformatic candidates requiring experimental validation.

### 4. Minor Numerical Inconsistency Between Abstract and Methods (Pillar 7)
* **WHY:** The Abstract (line 5) and Figure S1 legend state that the phylogeny is based on 73 amino acid sequences from **48 embryophyte species**, whereas Section 2.1 (line 24) lists **50 studied embryophyte genomes** (2 of which, *Marchantia polymorpha* and *Selaginella moellendorffii*, lacked recoverable SUP hits as noted in Section 3.1.1, line 90).
* **WHAT & HOW:** Clarify in Section 2.1 (line 24) that 50 embryophyte genomes were screened and 48 species yielded the 73 retained protein sequences.

---

## 4. Quantitative Rubric Scoring

| Rubric Dimension | Score | Max | Forensic Justification |
| :--- | :---: | :---: | :--- |
| **1. Methodological & Statistical Rigor** | **2.1** | **3.5** | Solid Bayesian phylogenetic inference, GENESPACE synteny validation, and in vivo confocal localization; deducted 1.4 pts for undocumented $\text{Zn}^{2+}$ parameterization, Berendsen coupling, and suspected $\text{nm}/\text{\AA}$ unit or restraint error ($<0.5\text{ \AA}$ RMSD) in the MD simulation, pre-filtering of truncated EAR motifs, and small-sample ($n=3\text{--}6$) promoter motif scans without a phylogenetic null. |
| **2. Claim-to-Evidence Alignment** | **1.6** | **2.5** | Evolutionary origin of *RA1* via two grass duplications and nuclear localization of RA1-like paralogs are well supported; claims of subfunctionalization/neofunctionalization in DNA binding, protein-protein interactions, and upstream regulation rely on in silico predictions without expression or binding assays. |
| **3. Data Integrity & Biological Plausibility** | **1.4** | **2.0** | Broad taxon sampling across 50 embryophyte genomes with authentic experimental localization in *N. benthamiana*; omitting a free `35S:GFP` diffusion control and omitting $\text{Zn}^{2+}$ cofactor details in the C2H2 zinc finger MD simulation weaken biophysical completeness. |
| **4. Reproducibility & Data Integrity** | **1.5** | **2.0** | Sequence datasets, alignments, primer tables, and supplementary trees are openly deposited in Mendeley Data (`doi:10.17632/m45fk8hxs4.1`) and biological materials in CRBIAL; minor deduction for the $<0.5\text{ \AA}$ vs. $\text{nm}$ RMSD discrepancy and missing GROMACS $\text{Zn}^{2+}$ topology details. |
| **Scientific Core Score** | **5.1** | **8.0** | Sum of Rigor + Claims + Biology (`2.1 + 1.6 + 1.4`). |
| **Total Composite Score** | **6.6** | **10.0** | **Mixed / Salvageable** (`2.1 + 1.6 + 1.4 + 1.5`). |
