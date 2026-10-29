# Forensic Peer Review: FEXP_ANON_156

**Overall Score:** **1.4 / 10.0** (Fundamentally Invalid) | **Scientific Core Score:** **1.0 / 8.0**
* **Score Breakdown:** Rigor: 0.2/3.5 | Claims: 0.3/2.5 | Biology: 0.5/2.0 | Reproducibility: 0.4/2.0

---

## 1. Blinded Metadata Perception
* **Perceived Tier:** Low Tier (Predatory/Megajournal)
* **Perceived Impact Factor Range:** < 2.0
* **Subfield:** Medicinal Chemistry / Anticancer Natural Product Derivatives (Chromones)
* **Rationale:** A forensic audit uncovers verbatim copy-paste artifacts from unrelated studies in the Materials and Methods (describing treatment of `HepG2` cells with `naringin` and `NDN` at `188.26` and `214.57 µg/mL`, and collecting `MCF7` and `HCT116` samples `"immediately after sacrificing the animals"` in an exclusively *in vitro* cell-culture paper), duplicated $^{13}\text{C}$ NMR peak lists shared across structurally unrelated compounds (`3`, `5`, `6b`, `10`, `15a`, `17`), concentration unit contradictions (`100 µM` vs. `100 µg/mL`), flow cytometry cell-cycle distributions that fail to sum to $100\%$ (missing up to $25.6\%$ of cells), and positive-control Doxorubicin apoptosis assays showing $>99.5\%$ necrosis and $0\%$ apoptosis.

---

## 2. Executive Summary & Editorial Verdict

This manuscript reports the synthesis of 20 visnagin-derived chromone congeners (`3–20`), their MTT cytotoxicity against MCF-7, HCT-116, HepG2, and normal BJ-1 cells, diphenylamine DNA fragmentation and agarose gel laddering, RT-qPCR of *CDK4*, *p53*, *Bax*, and *Bcl-2*, Annexin V-FITC/PI apoptosis and cell-cycle flow cytometry, AutoDock Vina docking into CDK4 (PDB: `7SJ3`), and SwissADME/admetSAR profiling. A forensic examination of the Experimental section, spectral data, and biological tables reveals severe data integrity and fabrication/copy-paste failures across every section of the study:

1. **Unrelated Study Protocols Copied into Materials and Methods (`naringin`/`NDN` and `"sacrificing the animals"`):**
   * In Section "Cell cycle arrest and apoptosis detection" (second half, line 255), the protocol states: *"After 24 h of the culture of HepG2 and treated with naringin and NDN at concentrations of 188.26 and 214.57 µg/mL, respectively, DNA was stained with propidium iodide (PI)..."* Neither `naringin`, `NDN`, nor `HepG2` cell cycle flow cytometry exists anywhere in this study (which tested chromones `14b` and `14c` on `MCF-7` and `HCT-116` cells).
   * In Section "Diphenylamine reaction procedure" (second half, line 231), the protocol states: *"MCF7 and HCT116 samples were collected immediately after sacrificing the animals."* This manuscript is an exclusively *in vitro* cell-culture study with no animals, no xenografts, and no animal ethics approval; furthermore, the same paragraph specifies suspending Eppendorf tube cell pellets in `"80 mL of 5% TCA"` and adding `"160 mL of Diphenyl Amine (DPA) solution [150 mg DPA in 10 mL glacial acetic acid, 150 mL of sulfuric acid and 50 mL acetaldehyde]"` (`mL` substituted for `µL`).
   * In Section "Cell proliferation and viability" (second half, line 213), the protocol describes seeding `PC3` and `A549` cell lines (neither of which is studied in the paper) and testing at `100 µM` (and `100, 50, 25, 12.5, 6.25 µM` in line 218), contradicting Tables 1 and 2 which report single-dose screening at `100 µg/mL` and $\text{IC}_{50}$ values in `µg/mL`.
2. **Duplicated and Fabricated $^{13}\text{C}$ / $^1\text{H}$ NMR Spectral Peak Lists Across Unrelated Chemical Structures:**
   * **Compound `3` vs. Compound `5` (second half, lines 46 and 60):** Compound `3` (`C15H14O6`, a tricyclic dioxocino-chromenone lacking any nitrogen, chlorine, or aromatic Schiff base) has $^{13}\text{C}$ NMR peaks at `175.66, 164.96, 161.79, 158.41, 158.00, 125.11, 113.29, 111.75, 106.34, 98.15, 75.42, 75.31, 66.27, 63.89, 19.80` and $^1\text{H}$ NMR peaks at `6.92, 6.51, 6.02, 4.76, 4.42, 4.12, 3.94, 3.78, 3.70, 2.25`. Compound `5` (`C21H17ClN2O7`, a chloronitrophenyl-imine bearing an oxiranylmethoxy chain) reports the exact same 15 $^{13}\text{C}$ peaks shifted by $+0.01\text{ to }+0.04\text{ ppm}$ (`175.67, 164.98, 161.83, 158.45, 158.03, [128.11], 125.14, [118.19, 116.09], 113.33, 111.78, 106.37, 98.16, 75.44, 75.30, 66.28, 63.91, 19.83`) and the exact same 10 $^1\text{H}$ peaks shifted by $+0.01\text{ ppm}$ (`6.93, 6.52, 6.04, 4.77, 4.42, 4.13, 3.94, 3.79, 3.71, 2.26`), with no imine `CH=N` proton peak at all! Moreover, in precursor `4` (line 53), an aromatic proton doublet-of-doublets is reported with an impossible $\text{H–H}$ coupling constant of $J = 45.5, 12.3\text{ Hz}$, and the chloro/nitro positions flip from `5-chloro-2-nitrophenyl` in `4` to `2-chloro-5-nitrophenyl` in `5`.
   * **Compound `10` vs. Compound `17` vs. Compound `3` (second half, lines 97 and 174):** Compound `10` (an acyclic cyanoacetylhydrazone, `C19H19N3O7`) and Compound `17` (a cyclic 4-oxothiazolidin-2-ylidenehydrazone, `C19H19N3O7S`) share **11 identical $^{13}\text{C}$ NMR peaks to two decimal places** (`168.33, 160.30, 159.80, 159.57, 142.10, 138.94, 116.56, 98.33, 61.47, 24.79, 14.53`), while the remaining peaks of `17` (`164.96, 113.29, 111.75, 66.27, 63.89, 19.80`) are copied verbatim to two decimal places from Compound `3`!
   * **Compound `6b` vs. Compound `15a` (second half, lines 69 and 150):** Compound `6b` (a 4-bromobenzoyl furochromone, `C20H13BrO5`) and Compound `15a` (a bis-*N*-methylthiosemicarbazone, `C18H22N6O5S2`) share **7 identical $^{13}\text{C}$ NMR peaks to two decimal places** (`164.68, 158.27, 158.21, 156.40, 116.98, 116.88, 111.01`).
3. **Flow Cytometry Cell-Cycle Percentages Fail to Sum to $100\%$ and Doxorubicin Positive Control Shows $>99.5\%$ Necrosis (First half, lines 186–215):**
   * In the MCF-7 cell-cycle analysis (first half, line 205), the reported G0/G1, S, and G2/M percentages sum to $81.94\% + 5.84\% + 0.81\% = 88.59\%$ for Control and $32.53\% + 44.1\% + 4.53\% = 81.16\%$ for `14b`. In the HCT-116 cell-cycle analysis (line 213), they sum to $73.64\% + 0.78\% + 0.00\% = 74.42\%$ for Control and $56.18\% + 24.43\% + 2.92\% = 83.53\%$ for `14c` (leaving $11.4\%$ to $25.6\%$ of cells unaccounted for).
   * In the Annexin V-FITC/PI apoptosis assay (lines 189 and 197), the positive control Doxorubicin produced **99.83% necrosis** ($0.17\%$ late apoptosis, $0\%$ early apoptosis) in MCF-7 and **99.53% necrosis** ($0.47\%$ late apoptosis, $0\%$ early apoptosis) in HCT-116, demonstrating that the positive-control cells were lysed/dead rather than undergoing apoptosis.

**Editorial Verdict:** **Reject.** The presence of fabricated/duplicated $^{13}\text{C}$ NMR spectra across distinct chemical classes and verbatim copy-paste of unrelated animal/plant-flavonoid experimental protocols invalidates the manuscript.

### Specific Conclusions and Assessment of Support
* **Claim 1:** Twenty novel visnagin-derived chromone derivatives (`3–20`) were synthesized and structurally characterized by IR, $^1\text{H}$/$^{13}\text{C}$ NMR, and MS. `[Methodologically Flawed]` — Compounds `3`, `5`, `6b`, `10`, `15a`, and `17` share verbatim copied-and-pasted $^{13}\text{C}$ NMR chemical shift lists; compound `4` reports an impossible $J = 45.5\text{ Hz}$ proton coupling; and compound `9` is titled as the `6-(methoxymethyl)` ether (`C16H18O7`, $m/z = 322$) while its procedure, IR (`3195 cm-1 OH`), and $^1\text{H}$ NMR (`2.25 ppm, 1H, OH exchangeable with D2O`) describe the `6-(hydroxymethyl)` alcohol (`C15H16O7`, MW $308.28$).
* **Claim 2:** Compounds `14b`, `17`, and `19` show selective cytotoxicity against MCF-7, while `6a`, `6b`, `11`, and `14c` are potent against HCT-116. `[Methodologically Flawed]` — The concentration units contradict between `100 µM` (Methods lines 213, 218; Results line 62) and `100 µg/mL` (Tables 1 and 2). Moreover, in Table 1, compound `14c` induces `100%` growth inhibition of MCF-7 at $100\text{ }\mu\text{g/mL}$ (exceeding the $\ge 60\%$ threshold stated in line 218), yet in Table 2 its $\text{IC}_{50}$ against MCF-7 is omitted (`–`), while compounds `17` and `19` report identical MCF-7 $\text{IC}_{50}$ values (`54.8 µg/mL`) and compounds `14b` and `17` report identical HCT-116 inhibition (`76.3%`) and $\text{IC}_{50}$ values (`33.3 µg/mL`).
* **Claim 3:** Compounds `14b` and `14c` induce apoptosis and S-phase cell cycle arrest in MCF-7 and HCT-116 cells. `[Methodologically Flawed]` — Flow cytometry cell-cycle distributions sum to $74.42\%–88.59\%$, the positive control Doxorubicin shows $99.53\%–99.83\%$ necrosis with $0\%$ early apoptosis, the Methods section describes treating `HepG2` cells with `naringin` and `NDN`, and line 215 of the Results states the exact opposite of its conclusion (*"there is an inverse relationship between the potency of anticancer activities and the number of cells in the S and G2 phases"*).
* **Claim 4:** SwissADME bioavailability radar shows that compound `14c` falls entirely within the optimal range for oral bioavailability whereas `6a` and `6b` are not orally bioavailable. `[Methodologically Flawed]` — Directly contradicted by Table 6 (first half, lines 281–291), which shows that `6a` ($\text{MW} = 334.32$) and `6b` ($\text{MW} = 413.22$) have **0 Lipinski violations and 0 Veber violations**, whereas `14c` ($\text{MW} = 513.76 > 500$, `MlogP = 3.24`) has **1 Lipinski violation**, and Table 7 reports impossible plasma protein binding values exceeding $100\%$ (`1.06` $= 106\%$ for `6b` and `1.004` $= 100.4\%$ for `14b`).

---

## 3. Forensic Defect Inventory

### 3.1 Major Methodological and Statistical Defects

* **Defect 1: Verbatim Copy-Paste of Unrelated Animal and Flavonoid Protocols in Materials and Methods.**
  * *Location:* Second half, lines 213, 231, and 255.
  * *Forensic Evidence:*
    1. Line 255 ("Cell cycle arrest and apoptosis detection"): *"After 24 h of the culture of HepG2 and treated with naringin and NDN at concentrations of 188.26 and 214.57 µg/mL, respectively, DNA was stained with propidium iodide (PI)..."*
    2. Line 231 ("Diphenylamine reaction procedure"): *"MCF7 and HCT116 samples were collected immediately after sacrificing the animals... the pellets were suspended in 80 mL of 5% TCA... Subsequently, to each sample, 160 mL of Diphenyl Amine (DPA) solution... was added."*
    3. Line 213 ("Cell proliferation and viability"): *"at a concentration of 20,000 cells/well for HCT-116 and PC3 cell lines and 10,000 cells/well for HepG2, A549 and MCF-7 cell lines... containing the tested compounds (100 μM)."*

* **Defect 2: Cross-Compound Duplication of $^{13}\text{C}$ and $^1\text{H}$ NMR Peak Lists.**
  * *Location:* Second half, lines 46 (`3`), 53 (`4`), 60 (`5`), 69 (`6b`), 90 (`9`), 97 (`10`), 150 (`15a`), and 174 (`17`).
  * *Forensic Evidence:*
    * **Pair A (`3` vs. `5`):** Every $^{13}\text{C}$ shift of `3` (`175.66, 164.96, 161.79, 158.41, 158.00, 125.11, 113.29, 111.75, 106.34, 98.15, 75.42, 75.31, 66.27, 63.89, 19.80`) reappears in `5` incremented by $0.01\text{–}0.04\text{ ppm}$ (`175.67, 164.98, 161.83, 158.45, 158.03, ..., 125.14, ..., 113.33, 111.78, 106.37, 98.16, 75.44, 75.30, 66.28, 63.91, 19.83`).
    * **Triplet B (`10` vs. `17` vs. `3`):** Compound `17` is a composite splice of 11 $^{13}\text{C}$ shifts copied exactly from `10` (`168.33, 160.30, 159.80, 159.57, 142.10, 138.94, 116.56, 98.33, 61.47, 24.79, 14.53`) and 6 $^{13}\text{C}$ shifts copied from `3` (`164.96, 113.29, 111.75, 66.27, 63.89, 19.80`). Notice that `24.79 ppm` in `10` corresponds to the acyclic $-\text{CH}_2\text{CN}$ carbon, which no longer exists after cyclization to the thiazolidinone ring in `17`!
    * **Pair C (`6b` vs. `15a`):** Seven aromatic/chromone $^{13}\text{C}$ shifts of bromobenzoyl furochromone `6b` (`164.68, 158.27, 158.21, 156.40, 116.98, 116.88, 111.01`) are copied identically into bis-thiosemicarbazone `15a`, which also lists two impossible thiocarbonyl peaks above $210\text{ ppm}$ (`211.23, 210.63 ppm`; thiosemicarbazone $\text{C=S}$ carbons resonate at $175\text{–}185\text{ ppm}$, as seen in `16` at `178.61 ppm`).

* **Defect 3: Defective Flow Cytometry Gating and Contradictory ADME Tables.**
  * *Location:* First half, lines 186–215 (Flow cytometry) and lines 269–302 (Tables 6 and 7).
  * *Forensic Evidence:*
    1. Cell cycle phase percentages (`G0/G1 + S + G2/M`) sum to $88.59\%$ (MCF-7 Control), $81.16\%$ (`14b`), $74.42\%$ (HCT-116 Control), and $83.53\%$ (`14c`).
    2. Doxorubicin positive control in the Annexin V assay shows $99.83\%$ and $99.53\%$ necrotic cells (quadrant Q2-1) and $0.17\%–0.47\%$ apoptotic cells.
    3. Line 277 claims `6a` and `6b` are not orally bioavailable while `14c` is inside the optimal radar pink area, directly contradicting Table 6 (`0` Lipinski/Veber violations for `6a` and `6b`; $\text{MW} = 513.76$ and `1` Lipinski violation for `14c`) and second half line 19 (*"the tested compounds were found to be absorbed in the human intestine, water-soluble and showed oral bioavailability except for compounds 11 and 19"*).
    4. Table 7 reports `Plasma protein binding (100%)` values of `1.06` ($106\%$) for `6b` and `1.004` ($100.4\%$) for `14b`, exceeding the physical upper bound of $1.00$ ($100\%$).

### 3.2 Minor Presentation, Structural, and Editorial Issues
* **Bogus IR Wavenumbers (Second half, lines 140 and 188):** Compound `14c` reports an IR peak at `15,602 (C=C)` $\text{cm}^{-1}$ and compound `19` reports an IR peak at `11,903` $\text{cm}^{-1}$ (outside the mid-IR spectrum `4000–400 cm-1`).
* **Misstatement of AutoDock Vina RMSD (Second half, line 260):** Line 260 states that the first docking pose of every synthesized ligand was selected because it had *"zero Å root-mean-square deviation (RMSD)"*; in AutoDock Vina, `RMSD l.b. = 0.000` and `RMSD u.b. = 0.000` for Mode 1 simply denote the distance of Mode 1 from itself, not validation accuracy against a crystal pose.

---

## 4. Quantitative Rubric Scoring

* **Methodological & Statistical Rigor (0.2 / 3.5):** Copy-pasted unrelated experimental protocols, spliced/duplicated $^{13}\text{C}$ NMR peak lists across unrelated molecules, inconsistent concentration units (`µM` vs. `µg/mL`), and unnormalized flow cytometry distributions render the methodology invalid.
* **Claim-Evidence Alignment (0.3 / 2.5):** Multiple claims directly contradict the manuscript's own tables (e.g., oral bioavailability of `6a`/`6b` vs. `14c`, inverse relationship between S/G2 arrest and potency, omission of `14c` MCF-7 $\text{IC}_{50}$).
* **Biological & Domain Validity (0.5 / 2.0):** Using a positive control (Doxorubicin) that yields $99.8\%$ necrosis and $0\%$ apoptosis invalidates the apoptosis flow cytometry comparison.
* **Reproducibility & Transparency (0.4 / 2.0):** The experimental protocols cannot be reproduced because key sections (cell cycle, diphenylamine DNA fragmentation, MTT concentrations) were copied from other studies with different compounds (`naringin`, `NDN`) and animal tissues.
* **Scientific Core Score:** **1.0 / 8.0** (`0.2 + 0.3 + 0.5`)
* **Overall Score:** **1.4 / 10.0** (`0.2 + 0.3 + 0.5 + 0.4`)
