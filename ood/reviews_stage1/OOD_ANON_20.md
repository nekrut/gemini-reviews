# Review of OOD_ANON_20

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **5.0 / 10.0** (Mixed / Salvageable)  
* **Score Breakdown:** Rigor: 1.5/3.5 | Claims: 1.2/2.5 | Biology: 1.3/2.0 | Reproducibility: 1.0/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This medicinal chemistry and cellular pharmacology study screens an in-house library of 1,000 compounds against the substrate-binding pocket of the PRMT5:MEP50 complex (PDB: `4X61`) using Schrödinger Glide XP molecular docking, tests 50 top hits in a radioactive $[\text{^3H}]$-SAM enzymatic methylation assay, and identifies compound `SJL2-1` ($\text{C}_{22}\text{H}_{26}\text{N}_2\text{O}$, MW $334.46$, Glide XP G-score $= -11.215$, enzymatic $\text{IC}_{50} = 1.56\ \mu\text{M}$ vs. $0.047\ \mu\text{M}$ for positive control EPZ015666). The authors evaluate `SJL2-1` across three human prostate cancer cell lines—androgen-sensitive LNCaP ($\text{IC}_{50} = 4.29\ \mu\text{M}$), AR-V7-positive castration-resistant 22RV1 ($\text{IC}_{50} = 40.07\ \mu\text{M}$), and AR-negative castration-resistant PC3 ($\text{IC}_{50} = 37.29\ \mu\text{M}$)—as well as normal prostate epithelial cells (RWPE-1) using CCK-8 viability, EdU incorporation, Transwell migration/invasion, PI cell-cycle flow cytometry, and Western blotting for Bax, Bcl-2, pro-caspase-3/caspase-3, PRMT5, symmetric dimethylarginine (SDMA/SmD3me2s), and AR/AR-V7. Neither raw screening tables nor uncropped Western blots are publicly deposited ("available on reasonable request").

While the study combines direct biochemical target validation ($[\text{^3H}]$-SAM assay), full chemical characterization ($^1\text{H}$/$^{13}\text{C}$ NMR, ESI-MS, elemental analysis), and multi-line phenotypic assays with a normal-cell toxicity control (RWPE-1), several major experimental design mismatches and mechanistic contradictions weaken the primary conclusions:
1. LNCaP has a 48-h cellular $\text{IC}_{50}$ of $4.29\ \mu\text{M}$, yet the cell-cycle flow cytometry (Figure 5) and Western blot assays (Figures 4 and 6) treat all three cell lines with $15, 30,$ and $45\ \mu\text{M}$ `SJL2-1`—concentrations that are **$3.5\times$ to $10.5\times$ above LNCaP's $\text{IC}_{50}$**, where severe overt cytotoxicity confounds cell-cycle and protein expression readouts.
2. In the apoptosis Western blot (Section 3.3, line 107; Figure 4), the authors report that *both* pro-caspase-3 and cleaved caspase-3 increase with `SJL2-1` concentration, whereas canonical caspase-3 activation via proteolytic cleavage of pro-caspase-3 decreases pro-caspase-3 levels.
3. `SJL2-1` was designed as a catalytic inhibitor binding the substrate pocket of PRMT5 (like EPZ015666), yet Western blotting (Figure 6) shows that `SJL2-1` strongly reduces total PRMT5 protein abundance alongside SDMA, without testing whether `SJL2-1` triggers proteasomal degradation or transcriptional repression of *PRMT5*.
4. The chemical synthesis route and the explicit IUPAC name/SMILES of `SJL2-1` are omitted from the text, and the NMR coupling constants in Section 2.3 ($J = 49.8\text{ Hz}$ and $J = 58.9\text{ Hz}$ in $^1\text{H}$ NMR for a $\text{C}_{22}\text{H}_{26}\text{N}_2\text{O}$ molecule lacking fluorine or phosphorus) are physically impossible proton–proton couplings.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **`SJL2-1` is a direct, sub-2 $\mu\text{M}$ enzymatic inhibitor of PRMT5 ($\text{IC}_{50} = 1.56\ \mu\text{M}$) identified via Glide XP docking: [Moderately Supported].**  
  The radioactive $[\text{^3H}]$-SAM assay includes appropriate positivecontrols (`EPZ015666`, $\text{IC}_{50} = 0.047\ \mu\text{M}$, matching literature values; and `SAH`) across 3-fold serial dilutions in triplicate. However, `SJL2-1` is $>30$-fold less potent than `EPZ015666`, no counter-screening against other arginine/lysine methyltransferases (e.g., PRMT1, PRMT4/CARM1, PRMT7, EZH2) is performed to establish selectivity, and neither the chemical synthesis procedure nor the chemical structure in SMILES/IUPAC format is provided in the text. Moreover, the $^1\text{H}$ NMR peak list in Section 2.3 (line 39) reports $J = 49.8\text{ Hz}$ (`3.84 (dq, J = 49.8, 6.9 Hz, 1H)`) and $J = 58.9\text{ Hz}$ (`2.45 (ddd, J = 58.9, 12.5, 10.1 Hz, 1H)`), which are impossible $^1\text{H}\text{--}^1\text{H}$ scalar coupling constants (typical $^2J_{\text{HH}}$ and $^3J_{\text{HH}}$ are $0\text{--}18\text{ Hz}$; $50\text{--}60\text{ Hz}$ occurs only when two separate chemical shift multiplets are erroneously integrated as a single split multiplet).

* **`SJL2-1` inhibits proliferation, migration, and invasion across AR-positive (LNCaP), AR-V7-positive (22RV1), and AR-negative (PC3) prostate cancer cells at cellularly relevant concentrations: [Fragile].**  
  In LNCaP cells, the 48-h $\text{IC}_{50}$ ($4.29\ \mu\text{M}$) is within $2.7$-fold of the biochemical PRMT5 $\text{IC}_{50}$ ($1.56\ \mu\text{M}$), which is pharmacologically plausible. In contrast, in 22RV1 ($\text{IC}_{50} = 40.07\ \mu\text{M}$) and AR-negative PC3 ($\text{IC}_{50} = 37.29\ \mu\text{M}$), cellular antiproliferative activity requires $\sim 40\ \mu\text{M}$—nearly $25\times$ higher than the enzymatic $\text{IC}_{50}$. As the authors note in the Discussion (line 141), genetic knockdown of *PRMT5* has no effect on AR-negative PC3 cells (Deng et al. 2017; Beketova et al. 2020). The fact that `SJL2-1` kills PC3 and 22RV1 only at $\sim 40\ \mu\text{M}$ while *PRMT5* knockdown leaves PC3 unaffected strongly suggests that the cytotoxicity in PC3 at $30\text{--}45\ \mu\text{M}$ is driven by off-target toxicity rather than on-target PRMT5 inhibition. Furthermore, the Transwell migration and invasion assays (Section 2.7, line 59) pre-treat cells for 48 h at $0.5 \times \text{IC}_{50}$ and then incubate them in the Transwell chamber for *another* 48 h (96 h total), where reduced cell counts on the lower membrane can be confounded by ongoing proliferation arrest and apoptosis.

* **`SJL2-1` induces G0/G1 cell-cycle arrest and caspase-3-mediated apoptosis across all three cell lines at 15, 30, and 45 $\mu\text{M}$: [Methodologically Flawed].**  
  1. **Severe overdosing of LNCaP cells:** Using 15, 30, and 45 $\mu\text{M}$ `SJL2-1` for 48 h in LNCaP cells ($\text{IC}_{50} = 4.29\ \mu\text{M}$) exposes LNCaP to $3.5\times\text{--}10.5\times$ its $\text{IC}_{50}$. Comparing LNCaP, 22RV1, and PC3 at identical 15–45 $\mu\text{M}$ doses (Figures 4, 5, and 6) while using cell-line-specific $0.5 \times \text{IC}_{50}$ doses in the EdU and Transwell assays (Section 2.6–2.7) is internally inconsistent.  
  2. **Contradictory pro-caspase-3 / caspase-3 Western blot:** Section 3.3 (line 107) states that `SJL2-1` induced *"elevated levels of both pro-caspase-3 and its activated form (caspase-3)"*, which contradicts canonical apoptosis biochemistry where cleavage of the 32 kDa zymogen (pro-caspase-3) into the active 17/12 kDa subunits depletes pro-caspase-3. Also, Section 2.4 (line 44) lists `GAPDH` as the only loading control antibody purchased, whereas the Figure 4B caption states that protein expression was *"normalized to $\beta$-Actin."*  
  3. **Lack of Annexin V/PI flow cytometry:** Apoptosis was inferred solely from Western blots without Annexin V/PI flow cytometric quantification, and multiple-group comparisons in Figure 3C,E,G were analyzed with pairwise $t$-tests rather than ANOVA with post-hoc correction.

* **`SJL2-1` inhibits PRMT5 expression, symmetric dimethylarginine (SDMA), and AR/AR-V7 expression: [Fragile].**  
  A competitive small-molecule enzyme inhibitor occupying the substrate pocket (like `EPZ015666`) inhibits catalytic methyltransferase activity (reducing SDMA and SmD3me2s) without decreasing total PRMT5 protein abundance. Figure 6A,B shows a sharp dose-dependent reduction in total PRMT5 protein itself. Consequently, the decrease in SDMA and SmD3me2s could simply reflect loss of PRMT5 protein (or general protein degradation in dying cells at $30\text{--}45\ \mu\text{M}$) rather than catalytic pocket inhibition.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Include `EPZ015666` as a Benchmark Control in Cellular Assays and Match Doses to Each Cell Line's $\text{IC}_{50}$
* **WHY:** Testing LNCaP ($\text{IC}_{50} = 4.29\ \mu\text{M}$) at $15\text{--}45\ \mu\text{M}$ measures non-specific cell death at $10\times\ \text{IC}_{50}$, and because *PRMT5* knockdown is known not to inhibit AR-negative PC3 cells, the $\sim 40\ \mu\text{M}$ activity of `SJL2-1` in PC3 may be an off-target effect.
* **WHAT:** Repeat the LNCaP Western blot and cell-cycle experiments at concentrations spanning its actual $\text{IC}_{50}$ ($1, 2.5, 5, 10\ \mu\text{M}$), and include the selective nanomolar PRMT5 inhibitor `EPZ015666` (which the authors already purchased for the biochemical assay) as a positive control in LNCaP, 22RV1, and PC3 viability and Western blot assays.
* **HOW:** Treat LNCaP, 22RV1, and PC3 with `EPZ015666` ($0.5\text{--}20\ \mu\text{M}$) alongside `SJL2-1` to test whether selective catalytic inhibition of PRMT5 phenocopies `SJL2-1` in PC3 or confirms that PC3 cytotoxicity at $40\ \mu\text{M}$ involves additional targets.

#### 2. Clarify the Mechanism of Total PRMT5 Protein Downregulation and Pro-Caspase-3 Elevation
* **WHY:** Small-molecule substrate-pocket inhibitors do not ordinarily reduce total PRMT5 protein levels (Figure 6A), and pro-caspase-3 typically decreases upon cleavage into active caspase-3 (Figure 4A).
* **WHAT:** Measure *PRMT5* and *AR* mRNA levels by RT-qPCR (or co-treat with the proteasome inhibitor MG132) to determine whether `SJL2-1` reduces PRMT5 transcription or induces PRMT5 proteasomal degradation, and report the cleaved-caspase-3 / pro-caspase-3 ratio alongside Annexin V-FITC/PI apoptosis flow cytometry.
* **HOW:** Treat LNCaP and 22RV1 cells with `SJL2-1` in the presence or absence of $10\ \mu\text{M}$ MG132 for 6 h before lysis to test whether PRMT5 protein levels are rescued, and reconcile the discrepancy between Section 2.4 (`GAPDH` antibody) and Figure 4B (`β-Actin` normalization).

#### 3. Provide the Synthesis Scheme, IUPAC Name/SMILES, and Corrected $^1\text{H}$ NMR Peak Assignments for `SJL2-1`
* **WHY:** Although the Abstract and Conclusion state that `SJL2-1` was "designed and synthesized," Section 2.3 ("Chemistry") provides no synthetic procedure, starting materials, or IUPAC name, and reports physically impossible $^1\text{H}\text{--}^1\text{H}$ coupling constants of $J = 49.8\text{ Hz}$ and $J = 58.9\text{ Hz}$ (which occur when two separate multiplets separated by $\sim 0.08\text{--}0.10\text{ ppm}$ on a 600 MHz spectrometer are mis-picked as a single multiplet).
* **WHAT & HOW:**
  1. Add the step-by-step synthetic scheme, reaction conditions, yield, HPLC purity, and full IUPAC name / SMILES string of `SJL2-1` to Section 2.3.
  2. Re-inspect the 600 MHz $^1\text{H}$ NMR spectrum (Figure S3) around $\delta\ 3.84$ and $\delta\ 2.45\text{ ppm}$ and report the two separate chemical shifts (or diastereomeric/rotameric peaks) rather than artificial $49.8\text{ Hz}$ and $58.9\text{ Hz}$ coupling constants.
  3. Remove the duplicated sentence in the Abstract (lines 8: *"In prostate cancer, gene knockout has been shown to inhibit cancer cells by regulating the AR..."* appears twice word-for-word) and fix the typo `SJ2-1` $\to$ `SJL2-1` in Section 3.1 (line 85).
