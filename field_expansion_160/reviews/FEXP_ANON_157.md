# Forensic Peer Review: FEXP_ANON_157

**Overall Score:** **1.3 / 10.0** (Fundamentally Invalid) | **Scientific Core Score:** **0.9 / 8.0**
* **Score Breakdown:** Rigor: 0.2/3.5 | Claims: 0.2/2.5 | Biology: 0.5/2.0 | Reproducibility: 0.4/2.0

---

## 1. Blinded Metadata Perception
* **Perceived Tier:** Low Tier (Predatory/Megajournal)
* **Perceived Impact Factor Range:** < 2.0
* **Subfield:** Computational Phytochemistry / In Silico Antidiabetic Screening (PPAR$\gamma$)
* **Rationale:** The manuscript commits multiple foundational errors that invalidate its results: (1) it leaves the synthetic pyrene-containing co-crystallized ligand `13M` (`CID_25112371`) from PDB `3VI8` in the screening list and claims it is a natural phytoconstituent of *Trigonella foenum-graecum* (Fenugreek); (2) it misidentifies saturated arachidic acid (`CID_10467`, $\text{MW} = 312.53\text{ g/mol}$) as polyunsaturated "arachidonic acid" and misidentifies a quercetin diglucoside (`CID_10121947`, $\text{MW} = 626.52\text{ g/mol}$) as "quercetin"; (3) it scrambles every MM/GBSA binding free energy between the text/Abstract and Table 2; and (4) Tables 1 and 2 contain dozens of duplicate PubChem IDs with different docking and MM/GBSA scores.

---

## 2. Executive Summary & Editorial Verdict

This study screens 140 compounds attributed to Fenugreek (*Trigonella foenum-graecum*) against the peroxisome proliferator-activated receptor gamma (PPAR$\gamma$) ligand-binding domain (PDB ID: `3VI8`) using Schrödinger Glide docking, Prime MM/GBSA binding free energy estimation, PHASE E-pharmacophore generation, and SwissADME/ProTox-II profiling. A forensic audit reveals that the compound identities, numerical tables, and biological interpretations are fundamentally erroneous:

1. **Synthetic Co-Crystallized Pyrene Ligand (`13M` / `CID_25112371`) Misreported as a Fenugreek Phytochemical:** In Section 2.3 (line 36), the authors note that the PDB `3VI8` receptor grid was centered on its co-crystallized ligand `(2S)-2-(4-methoxy-3-{[(pyren-1-ylcarbonyl)amino]methyl}benzyl)butanoic acid` (PDB ligand ID `13M`, PubChem `CID_25112371`), a synthetic pyrene-carboxamide PPAR$\gamma$ partial agonist. Yet throughout the Abstract (line 5), Results (line 59), Tables 1–6, Figure 6, and Discussion (line 220), `CID_25112371` is reported as one of the five top natural phytoconstituents isolated from *Trigonella foenum-graecum*!
2. **Misidentification of `CID_10467` (Arachidic Acid vs. "Arachidonic Acid") and `CID_10121947` (Quercetin Diglucoside vs. "Quercetin"):**
   * The manuscript's top-recommended lead compound, `CID_10467`, is repeatedly named **"arachidonic acid"** in the Abstract, Results, Tables 3–6, and Discussion (where line 220 discusses it in the context of polyunsaturated fatty acids, PUFAs). However, PubChem `CID_10467` (with `Mol. wt. = 312.53 g/mol` in Table 4 and pharmacophore `HHHHN` in Table 3) is **arachidic acid** (eicosanoic acid, $\text{C}_{20}\text{H}_{40}\text{O}_2$), a fully saturated 20-carbon fatty acid (as inadvertently shown in the caption of Figure 2, line 138: *"2D configuration of arachidic acid complex"*), whereas arachidonic acid ($\text{C}_{20}\text{H}_{32}\text{O}_2$, `CID_444899`) has $\text{MW} = 304.47\text{ g/mol}$ and four *cis*-double bonds.
   * Similarly, `CID_10121947` is labeled **"Quercetin"** across the Abstract, Results, Tables 3–6, and Discussion. However, Table 4 (line 175) lists `CID_10121947` with `Mol. wt. = 626.52 g/mol`, `HBD = 11`, `HBA = 17`, and `Lipinski Violation = 3`. True quercetin (`CID_5280343`, which appears separately in Table 1 at line 74 with a docking score of `-8.553`) has $\text{MW} = 302.24\text{ g/mol}$, $\text{HBD} = 5$, $\text{HBA} = 7$, and $0$ Lipinski violations; `CID_10121947` ($\text{C}_{27}\text{H}_{30}\text{O}_{17}$, $\text{MW} = 626.52\text{ g/mol}$) is a quercetin diglucoside.
3. **Complete Scrambling of MM/GBSA Binding Free Energies Between Text/Abstract and Table 2 (Lines 5, 93, 99–103, 220):** In Table 2 (lines 99–103), the five asterisked MM/GBSA binding free energies (`BFE`) are: `10121947 = -58.9`, `25112371 = -56.33`, `10467 = -41.8`, `5280804 = -45.89`, and `5280805 = -45.73` (while an unstarred compound, `135398658` at line 116, actually has the lowest BFE in the table at `-60.85`). Yet in the Abstract (line 5), Results Section 3.2 (line 93), and Discussion (line 220), these values are completely misassigned: `-58.9` is attributed to `CID_10467` (arachidonic acid), `-56.33` is attributed simultaneously to both `CID_5280804` (isoquercetin) and `CID_5280805` (rutin), `-45.89` is attributed to `CID_10121947` (quercetin), and `-45.73` is attributed to `CID_25112371`.
4. **Extensive Duplication of PubChem IDs in Tables 1 and 2 and Contradictions Between Text and ADMET Tables:** Dozens of PubChem IDs appear two or three times in Tables 1 and 2 with conflicting docking and MM/GBSA scores (e.g., `5280804`, `5280805`, `114776`, `11349`, `318040061`, `13644663`, `5280961`, `162350`, `5281675`, `5280378`, `5280445`, `5280441`, `135398658`, `6274`, `1054`, `131752196`, `133082395`). Furthermore, Discussion line 220 claims that `CID_10467` shows *"strong compliance to Lipinski, Ghose, and Verber's rules"*, whereas Table 4 (line 177) reports that `CID_10467` violates all three rules (`1` Lipinski violation, `1` Ghose violation, `1` Veber violation) and Table 7 (line 207) predicts all three leads to be **Inactive** at `PPAR-Gamma`.

**Editorial Verdict:** **Reject.** The manuscript misidentifies its chemical structures, mistakes the synthetic PDB co-crystal ligand for a plant metabolite, and misassigns every MM/GBSA value between its text and tables.

### Specific Conclusions and Assessment of Support
* **Claim 1:** Five phytoconstituents from *Trigonella foenum-graecum*—arachidonic acid (`CID_10467`), isoquercetin (`CID_5280804`), rutin (`CID_5280805`), quercetin (`CID_10121947`), and `(2S)-2-[[4-methoxy-3-[(pyrene-1-carbonylamino)methyl]phenyl]methyl]butanoic acid` (`CID_25112371`)—are top PPAR$\gamma$ binders superior to Rosiglitazone (`-7.672`). `[Methodologically Flawed]` — `CID_25112371` is the synthetic co-crystallized ligand `13M` from PDB `3VI8`, not a Fenugreek phytoconstituent; `CID_10467` is saturated arachidic acid, not arachidonic acid; `CID_10121947` ($\text{MW} = 626.52$) is a quercetin diglucoside, not quercetin (`CID_5280343`); and Rosiglitazone is never included in Table 1 or Table 2.
* **Claim 2:** Arachidonic acid (`CID_10467`) has the lowest MM/GBSA binding free energy (`-58.9 kcal/mol`), followed by isoquercetin (`-56.33`), rutin (`-56.33`), quercetin (`-45.89`), and `CID_25112371` (`-45.73`). `[Methodologically Flawed]` — Directly contradicted by Table 2 (lines 99–103), where `-58.9` belongs to `10121947`, `-56.33` belongs to `25112371`, `-41.8` belongs to `10467`, `-45.89` belongs to `5280804`, `-45.73` belongs to `5280805`, and `-60.85` belongs to `135398658` (line 116).
* **Claim 3:** `CID_10467` exhibits the most favorable drug-like and ADMET characteristics with strong compliance to Lipinski, Ghose, and Veber rules. `[Methodologically Flawed]` — Contradicted by Table 4 (which shows `CID_10467` violates Lipinski, Ghose, and Veber rules), Table 5 (which shows `Low` human gastrointestinal absorption for `CID_10467`), and Table 7 (which predicts `CID_10467` has the lowest $\text{LD}_{50}$ of the three leads at `900 mg/kg` and is `Inactive` at PPAR$\gamma$).

---

## 3. Forensic Defect Inventory

### 3.1 Major Methodological and Statistical Defects

* **Defect 1: Inclusion of Synthetic PDB Co-Crystal Ligand `13M` (`CID_25112371`) as a Natural Plant Compound from Fenugreek.**
  * *Location:* Abstract (line 5), Section 2.3 (line 36), Section 3.1 (line 59), Tables 1–7, Figure 6, and Discussion (line 220).
  * *Forensic Evidence:* PDB entry `3VI8` is the crystal structure of human PPAR$\gamma$ LBD bound to the synthetic pyrene derivative `13M` (`(2S)-2-(4-methoxy-3-{[(pyren-1-ylcarbonyl)amino]methyl}benzyl)butanoic acid`, PubChem `CID_25112371`). After using `13M` to define the receptor grid in Section 2.3, the authors failed to remove it from the ligand set and reported it throughout the paper as a natural antidiabetic phytochemical from *Trigonella foenum-graecum*.

* **Defect 2: Misidentification of Chemical Entities (`CID_10467` and `CID_10121947`).**
  * *Location:* Abstract (line 5), Section 3.1 (line 59), Figure 2 (line 138), Tables 3–6 (lines 158–192), and Discussion (line 220).
  * *Forensic Evidence:*
    1. `CID_10467` has molecular formula $\text{C}_{20}\text{H}_{40}\text{O}_2$ and $\text{MW} = 312.53\text{ g/mol}$ (Table 4, line 177), which is **arachidic acid** (a saturated fatty acid), not **arachidonic acid** ($\text{C}_{20}\text{H}_{32}\text{O}_2$, $\text{MW} = 304.47\text{ g/mol}$).
    2. `CID_10121947` has $\text{MW} = 626.52\text{ g/mol}$, $\text{HBD} = 11$, $\text{HBA} = 17$ (Table 4, line 175), which is a **quercetin diglucoside**, whereas aglycone quercetin (`CID_5280343`, $\text{MW} = 302.24\text{ g/mol}$) is listed separately at line 74 of Table 1.

* **Defect 3: Complete Misassignment of MM/GBSA Energies Between Text and Table 2.**
  * *Location:* Abstract (line 5), Section 3.2 (line 93), Table 2 (lines 99–103), and Discussion (line 220).
  * *Forensic Evidence:* Table 2 lists `10121947 (-58.9)`, `25112371 (-56.33)`, `10467 (-41.8)`, `5280804 (-45.89)`, and `5280805 (-45.73)`. The text in Section 3.2, Abstract, and Discussion shifts the values across rows, assigning `-58.9` to `10467`, `-56.33` to both `5280804` and `5280805`, `-45.89` to `10121947`, and `-45.73` to `25112371`, while ignoring `-41.8` and ignoring compound `135398658` (`BFE = -60.85` in Table 2, line 116).

* **Defect 4: Extensive Unexplained Duplication of Ligands in Tables 1 and 2.**
  * *Location:* Table 1 (lines 62–89) and Table 2 (lines 96–123).
  * *Forensic Evidence:* Out of 144 cells in Table 1 (and 145 cells in Table 2, where `14257` with `BFE = -30.63` appears at the bottom of column 6 in Table 2 despite being absent from Table 1, while `114776` is dropped from row 1 col 2 of Table 2, shifting the entire second column of Table 2 up by one row relative to Table 1!), at least 17 PubChem IDs are duplicated 2–3 times with different scores (e.g., `5280804` has BFEs of `-45.89` and `-54.99`; `5280805` has BFEs of `-45.73` and `-42.53`; `135398658` has BFEs of `-43.93`, `-60.85`, and `-32.4`).

* **Defect 5: Scrambled Figure Citations and Residue Numbers in Section 3.4.**
  * *Location:* Section 3.4 (line 135), Figures 2–6 (lines 138–150), and Discussion (line 220).
  * *Forensic Evidence:* Line 135 cites `Fig 3A and 3B` for `CID_25112371` (when Fig 3 is isoquercitrin and Fig 6 is `CID_25112371`), cites `Fig 4A and 4B` for `CID_10121947` (when Fig 4 is rutin and Fig 5 is quercetin), and cites `Figs 5A/5B and 6A/6B` for `CID_5280804` and `CID_5280805`. Furthermore, `Serine-280` and `Glutamine-277` in line 135 become `Ser 240` and `Glu 277` in Discussion line 220.

### 3.2 Minor Presentation, Structural, and Editorial Issues
* **Self-Contradictory Docking Parameter Description (Section 2.4, line 41):** *"setting ligand sampling to flexible, with the ligand sampling set to none (refine only)"*.
* **Inconsistent Spelling of Plant Binomial:** Spelled variously as `Trigonellafeonumgraecum` (lines 5, 31, 220), `Trigonellafoenum-graecum` (lines 12, 14, 18), `Trignonella foenum graecum` (lines 59, 62, 96, 172), and `Trigonellafoecumgraecum` (line 220).

---

## 4. Quantitative Rubric Scoring

* **Methodological & Statistical Rigor (0.2 / 3.5):** Contaminating the natural product library with the synthetic PDB co-crystallized ligand, duplicating compounds across Tables 1 and 2, shifting column 2 of Table 2 by omitting `114776`, and scrambling all MM/GBSA numbers between text and tables represent fatal methodological failures.
* **Claim-Evidence Alignment (0.2 / 2.5):** Every major claim (compound identities, MM/GBSA rankings, Lipinski/Ghose/Veber compliance of `CID_10467`, and ProTox-II PPAR$\gamma$ activity) is contradicted by the manuscript's own tables.
* **Biological & Domain Validity (0.5 / 2.0):** Confusing saturated arachidic acid (`20:0`) with polyunsaturated arachidonic acid (`20:4`) and mistaking a synthetic pyrene derivative for a Fenugreek metabolite invalidate the biological discussion.
* **Reproducibility & Transparency (0.4 / 2.0):** Although PubChem CIDs and PDB `3VI8` are listed, the tables are internally inconsistent and the Supporting Information links are non-functional placeholders.
* **Scientific Core Score:** **0.9 / 8.0** (`0.2 + 0.2 + 0.5`)
* **Overall Score:** **1.3 / 10.0** (`0.2 + 0.2 + 0.5 + 0.4`)
