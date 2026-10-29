# Forensic Peer Review: FEXP_ANON_158

**Overall Score:** **3.4 / 10.0** (Flawed / Overstated) | **Scientific Core Score:** **2.5 / 8.0**
* **Score Breakdown:** Rigor: 0.9/3.5 | Claims: 0.7/2.5 | Biology: 0.9/2.0 | Reproducibility: 0.9/2.0

---

## 1. Blinded Metadata Perception
* **Perceived Tier:** Mid-to-Low Tier Open-Access Virology / Biomolecules Journal
* **Perceived Impact Factor Range:** 2.5 – 4.0
* **Subfield:** Antiviral Drug Discovery / Norovirus $\text{3CL}^{\text{pro}}$ Protease Screening
* **Rationale:** The manuscript combines AutoDock Vina virtual screening of 58,836 compounds against Norovirus GII.4 $\text{3CL}^{\text{pro}}$ (PDB: `8U1V`) with a cellular FlipGFP reporter assay and Western blot cleavage readout. However, it mislabels *in silico* docked poses as *"Crystal Structures of Norovirus $\text{3CL}^{\text{pro}}$ in Complex with Hit Inhibitors"* and *"co-crystal structures"*, lacks cell-viability ($\text{CC}_{50}$) or translation controls to rule out false-positive fluorescence suppression by cytotoxic PI3K/mTOR/kinase inhibitors (such as Gedatolisib), misinterprets Chain B of the crystallographic dimer as "residues 345–355" in the MD RMSF analysis, and omits Tables 1 and 2 from the main text.

---

## 2. Executive Summary & Editorial Verdict

This study screens a 58,836-compound library against the crystal structure of Norovirus GII.4 3C-like cysteine protease ($\text{3CL}^{\text{pro}}$, PDB: `8U1V`) using a three-tier AutoDock Vina workflow (`exhaustiveness = 1, 8, 16`), tests 17 top-scoring commercial hits in a HEK293T cell-based FlipGFP reporter assay, and performs 100 ns GROMACS molecular dynamics (MD) simulations on eight active hits (`Gedatolisib`, `EGFR-IN-8`, `Akt inhibitor VIII`, `Bavdegalutamide`, `Lifirafenib`, `TAM-IN-2`, `GSK1904529A`, and `IKK 16`). A forensic audit identifies four major scientific and methodological defects:

1. **In Silico Docked Poses Misrepresented as Experimental "Co-Crystal Structures" (Section 3.4, lines 87–90):** Section 3.4 is titled *"3.4. Crystal Structures of Norovirus $\text{3CL}^{\text{pro}}$ in Complex with Hit Inhibitors"* and states: *"To elucidate the inhibitory mechanisms of the eight candidate compounds, we analyzed their co-crystal structures with $\text{3CL}^{\text{pro}}$, focusing on the interactions between the compounds and key protease residues... with Max Affinity scores of $-11.41, -12.41,$ and $-11.15\text{ kcal/mol}$."* No X-ray crystallography was performed in this study; Figure 4A–H depicts AutoDock Vina docked poses inside apo PDB `8U1V`, not experimental co-crystal structures.
2. **Uncontrolled Confounding of the Cell-Based FlipGFP Assay by mTOR/PI3K Translation Inhibition and Cytotoxicity:** All eight active hits are potent mammalian kinase or signaling inhibitors (`Gedatolisib`: dual PI3K/mTORC1/2 inhibitor with $\text{IC}_{50} \sim 0.4\text{–}10\text{ nM}$; `Akt inhibitor VIII`; `EGFR-IN-8`; `Lifirafenib`: RAF/EGFR inhibitor; `GSK1904529A`: IGF-1R/IR inhibitor; `TAM-IN-2`: AXL/TAM inhibitor; `IKK 16`: IKK inhibitor; `Bavdegalutamide`: AR PROTAC). In the FlipGFP assay, HEK293T cells are treated with compound 6 hours after plasmid transfection and green fluorescence is read at 24 hours. Because mTORC1/PI3K/AKT/IGF-1R inhibitors directly suppress cap-dependent mRNA translation and cell viability in HEK293T cells, any compound that blocks *de novo* FlipGFP protein synthesis or kills HEK293T cells will reduce fluorescence intensity and mimic protease inhibition. No $\text{CC}_{50}$ cytotoxicity assay (e.g., MTT/CCK-8/ATP), no constitutively fluorescent transfection control (e.g., mCherry/Renilla), and no purified biochemical $\text{3CL}^{\text{pro}}$ FRET enzymatic assay were performed. Moreover, for `Lifirafenib`, the reported $\text{IC}_{50} = 1.02 \pm 1.23\text{ }\mu\text{M}$ (line 80) has a standard deviation exceeding the mean (`SD = 121%` of the mean).
3. **Dimer Indexing Error in MD RMSF Analysis (`Residues 345–355` in a 181-Residue Protease, Section 3.5, line 98):** Line 98 states: *"Large fluctuations were primarily observed in residues 165–180 and 345–355, regions likely associated with loop flexibility."* Mature Norovirus $\text{3CL}^{\text{pro}}$ (`NS6`) is only **181 amino acids long**! PDB `8U1V` contains a homodimer (Chains A and B, $2 \times 181 = 362$ residues) in the asymmetric unit; "residues 345–355" are simply residues 164–174 of the second monomer (Chain B) after continuous 1-to-362 renumbering, not a separate domain or loop at position 350.
4. **Excessive Blind-Docking Grid Box ($88.94 \times 83.85 \times 84.82\text{ \AA}$) and Missing Tables 1 and 2:** In Section 2.5 (line 46), the AutoDock Vina grid box is specified as `88.94 Å × 83.847 Å × 84.821 Å`, which is larger than the entire $\text{3CL}^{\text{pro}}$ dimer and contradicts Section 3.2 (line 71: *"with a defined docking box set around the active site of $\text{3CL}^{\text{pro}}$"*). Furthermore, `Table 1` (cited at line 71) and `Table 2` (cited at line 80) are missing from the manuscript body.

**Editorial Verdict:** **Reject / Major Resubmission Required.** To support the claim of direct Norovirus $\text{3CL}^{\text{pro}}$ inhibition, the authors must perform cell-free enzymatic cleavage assays alongside HEK293T $\text{CC}_{50}$ viability and constitutive reporter controls, remove all claims of "co-crystal structures," and fix the dimer residue numbering and missing tables.

### Specific Conclusions and Assessment of Support
* **Claim 1:** A HEK293T cell-based FlipGFP assay validated with wild-type vs. C139A mutant Norovirus GII.4 $\text{3CL}^{\text{pro}}$ and positive control GC376 ($\text{IC}_{50} = 2.28 \pm 0.17\text{ }\mu\text{M}$) reliably measures intracellular protease activity. `[Moderately Supported]` — The WT vs. C139A and GC376 controls confirm assay responsiveness, though the Western blot (`Figure S3`, line 82) unexpectedly shows two uncleaved bands (~35 and ~25 kDa) that disappear upon WT $\text{3CL}^{\text{pro}}$ expression without showing the expected accumulating cleaved fragment band, and lacks a constitutive expression control for compound toxicity.
* **Claim 2:** Eight oncology/immunology drugs—led by Gedatolisib ($\text{IC}_{50} = 0.06 \pm 0.01\text{ }\mu\text{M}$)—are potent, direct inhibitors of Norovirus $\text{3CL}^{\text{pro}}$. `[Fragile]` — Without a purified enzymatic FRET assay or HEK293T $\text{CC}_{50}$ / translation control, nanomolar inhibition of FlipGFP fluorescence in HEK293T cells by a nanomolar mTORC1/2 and PI3K inhibitor (`Gedatolisib`) is severely confounded by suppression of plasmid-driven protein translation and cytotoxicity.
* **Claim 3:** Analysis of the "co-crystal structures" of the eight compounds with $\text{3CL}^{\text{pro}}$ identifies Val82, Asn165, Arg100, Ser125, and Met130 as key inhibitor-binding residues. `[Methodologically Flawed]` — No co-crystal structures exist; these are unvalidated AutoDock Vina poses generated using an $88.9 \times 83.8 \times 84.8\text{ \AA}$ grid box.
* **Claim 4:** 100 ns MD simulations show stable complex formation with primary loop flexibility in residues `165–180` and `345–355`. `[Methodologically Flawed]` — Norovirus $\text{3CL}^{\text{pro}}$ has only 181 residues; `345–355` is an indexing artifact of concatenating the two chains of the PDB `8U1V` homodimer ($164+181=345$).

---

## 3. Forensic Defect Inventory

### 3.1 Major Methodological and Statistical Defects

* **Defect 1: Misrepresentation of AutoDock Vina Poses as Experimental "Crystal Structures" and "Co-Crystal Structures".**
  * *Location:* Section 3.4 header and text (lines 87–90).
  * *Forensic Evidence:* Line 87 titles the section *"3.4. Crystal Structures of Norovirus $\text{3CL}^{\text{pro}}$ in Complex with Hit Inhibitors"* and line 89 states *"we analyzed their co-crystal structures with $\text{3CL}^{\text{pro}}$."* No crystallization, X-ray diffraction data collection, or structure refinement was conducted.

* **Defect 2: Lack of Cell Viability ($\text{CC}_{50}$), Translation Control, and Cell-Free Enzymatic Assay for Cytotoxic Kinase/mTOR Inhibitors.**
  * *Location:* Sections 2.4, 3.3, and 4 (lines 41, 80–84, 109).
  * *Forensic Evidence:* In the FlipGFP assay, fluorescence requires active transcription and cap-dependent translation of two co-transfected plasmids in HEK293T cells between 6 h and 24 h post-transfection. `Gedatolisib` is a clinical dual PI3K/mTOR inhibitor ($\text{IC}_{50} = 0.4\text{–}10\text{ nM}$ against PI3K$\alpha/\gamma$ and mTOR), `Akt inhibitor VIII` inhibits AKT1/2/3, and `GSK1904529A` inhibits IGF-1R/IR. Inhibiting the PI3K–AKT–mTOR axis directly shuts down cap-dependent translation (via 4E-BP1 dephosphorylation and S6K inhibition) and induces cell-cycle arrest/apoptosis in HEK293T cells, which lowers GFP fluorescence independientemente of $\text{3CL}^{\text{pro}}$ catalytic inhibition. Neither $\text{CC}_{50}$ values nor cell-free enzymatic $\text{IC}_{50}$ values are provided. Furthermore, `Lifirafenib` is reported with $\text{IC}_{50} = 1.02 \pm 1.23\text{ }\mu\text{M}$ ($\text{CV} = 120.6\%$), indicating an unconstrained curve fit.

* **Defect 3: Homodimer Chain-Concatenation Artifact (`Residues 345–355`) and Unphysiological MD Temperature ($290\text{ K}$).**
  * *Location:* Section 2.6 (line 51) and Section 3.5 (line 98).
  * *Forensic Evidence:*
    1. Line 98 reports RMSF peaks at *"residues 165–180 and 345–355."* Since Norovirus $\text{3CL}^{\text{pro}}$ is 181 residues long, residues `345–355` correspond to residues `164–174` of the second subunit (Chain B) of the PDB `8U1V` dimer.
    2. Line 51 states that MD simulations were performed at `290 K` ($16.85\text{ }^\circ\text{C}$, below room temperature and far below human physiological temperature of $310\text{ K}$ / $37\text{ }^\circ\text{C}$) using `"GRAFF2"` (a misspelling of `GAFF2`), and states *"initial velocities were not generated to ensure system stability."*

* **Defect 4: Contradictory Docking Grid Box Dimensions and Omitted Main-Text Tables 1 and 2.**
  * *Location:* Section 2.5 (line 46) and Sections 3.2–3.3 (lines 71 and 80).
  * *Forensic Evidence:* Line 46 specifies a grid box of `88.94 Å × 83.847 Å × 84.821 Å`, which encompasses the entire crystal unit cell rather than the catalytic cleft around His30/Glu54/Cys139, and `Table 1` and `Table 2` are referenced in the text but omitted from the article.

### 3.2 Minor Presentation, Structural, and Editorial Issues
* **Protocol Discrepancy in Section 2.4 (Line 41) vs. Section 2.2 (Line 31):** Line 41 states *"For the assay, $\text{3CL}^{\text{pro}}$ was incubated with FlipGFP in $50\text{ }\mu\text{L}$ of DMEM for $30\text{ min}$"* before PEI addition, whereas line 31 states the two plasmids ($250\text{ ng}$ each) were mixed in $50\text{ }\mu\text{L}$ DMEM with $1500\text{ ng}$ PEI and incubated for $20\text{ min}$.
* **Typographical Error in Section 3.1 (Line 64):** *"we co-transfected of $\text{3CL}^{\text{pro}}$-FlipGFP"*.

---

## 4. Quantitative Rubric Scoring

* **Methodological & Statistical Rigor (0.9 / 3.5):** The FlipGFP WT/C139A/GC376 assay setup is valid, but the screen lacks cytotoxicity ($\text{CC}_{50}$) and cell-free enzymatic counter-screens to filter out translation-inhibiting kinase/mTOR blockers, uses an oversized $89\text{ \AA}$ docking box, and misindexes the dimeric PDB structure in MD analysis.
* **Claim-Evidence Alignment (0.7 / 2.5):** Calling AutoDock Vina models "co-crystal structures" and claiming nanomolar direct $\text{3CL}^{\text{pro}}$ inhibition by Gedatolisib without ruling out mTOR-mediated translation shutdown overstates the experimental evidence.
* **Biological & Domain Validity (0.9 / 2.0):** The authors candidly acknowledge in the Discussion (line 109) that live-virus and *in vitro* antiviral validations are still required, but overlook the direct confounding effect of PI3K/AKT/mTOR inhibition on plasmid reporter expression in HEK293T cells.
* **Reproducibility & Transparency (0.9 / 2.0):** GenBank (`PQ213805.1`) and PDB (`8U1V`) IDs and experimental reagent sources are documented, but Tables 1 and 2 are missing from the manuscript text.
* **Scientific Core Score:** **2.5 / 8.0** (`0.9 + 0.7 + 0.9`)
* **Overall Score:** **3.4 / 10.0** (`0.9 + 0.7 + 0.9 + 0.9`)
