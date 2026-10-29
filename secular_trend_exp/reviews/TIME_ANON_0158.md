</Agent System Instructions>
<Blinded Review: TIME_ANON_0158>
**Composite Score:** 4.5 / 10.0 (Rigor: 1.3/3.5 | Claims: 1.1/2.5 | Biology: 1.1/2.0 | Reproducibility: 1.0/2.0)
**Bias Category:** Statistical/Design
**Verdict:** Major Revision
**Study Modality:** Wet-Lab Primary Experimental
**Technology Maturity:** Mature/Classical
**Epistemic Stage:** Basic/Mechanistic Discovery

---

### 1. Executive Summary
This study investigates the role of nitric oxide ($\bullet\text{NO}$) in porcine respiratory viral infections by measuring total nitrite/nitrate ($\text{NO}_2^- + \text{NO}_3^-$) via the Griess assay in archival bronchoalveolar lavage (BAL) fluids from 92 weaned pigs across four retrospective animal trials (PRCV single-infection $n=26$, PRRSV single-infection $n=20$, PRRSV/PRCV dual-infection $n=26$, and mock control $n=20$ across post-inoculation days 2, 4, 8, 10, and 14), alongside *in vitro* antiviral assays using the $\bullet\text{NO}$ donor *S*-nitroso-*N*-acetylpenicillamine (`SNAP`) against PRCV in ST cells and PRRSV in MARC145 cells. While the *in vitro* finding that SNAP inhibits PRCV replication in ST cells ($P < 0.05$ at 24 h, $P < 0.01$ at 48 h) but does not inhibit PRRSV in MARC145 cells is straightforward, the manuscript's central *in vivo* claim—that PRCV induces a large increase in BAL $\bullet\text{NO}$—is statistically unsupported ($P > 0.05$ across all treatment groups), and the reported *in vitro* $\bullet\text{NO}$ concentrations use dimensionally invalid units (`mM/ml`) and exceed the molar stoichiometry of the added SNAP donor by up to $3.5\times$.

### 2. Methodological & Statistical Audit
- **Statistically Non-Significant *In Vivo* BAL $\bullet\text{NO}$ Data Presented as a Positive Finding:**
  - Both the Abstract (*"We detected a large increase in •NO levels in BAL fluids of PRCV-infected pigs"*) and the title of Figure 1 (*"PRCV, but not PRRSV, induced increased •NO levels in BAL during the early and middle stages of infection"*) assert a positive *in vivo* induction of $\bullet\text{NO}$ by PRCV.
  - Yet in the Results text (line 50), the authors explicitly admit: ***"there were no significant differences in mean •NO levels among treatment groups due to high variability among pigs... For this reason, no significant differences were detected in mean BAL •NO levels among the four experimental groups in our study."***
  - Even in mock-infected control pigs, mean BAL $\bullet\text{NO}$ varied nearly 7-fold across the four archival trials ($2.5$ to $16.63\text{ }\mu\text{M}$), which the authors attribute to outbred animals and different storage durations at $-70^\circ\text{C}$ between retrospective trials. Claiming a reproducible *in vivo* biological effect when the Kruskal-Wallis test is non-significant at every time point ($n = 4\text{--}6$ pigs/group/PID pooled across 4 trials) is statistically invalid.
- **Reporting "Means $\pm$ SDM" for Sample Sizes of $n = 1$ (Figure 1A–B):**
  - The caption to Figure 1A–B (line 53) states: *"BAL samples were collected from each pig (n = 1 at all PIDs for mock and PRRSV single-infected pigs, n = 1–2 at each PID for PRRSV/PRCV dual- and PRCV single-infected pigs). All data are expressed as the means ± SDM."* A standard deviation (`SDM`) is mathematically undefined for $n = 1$ biological replicate per time point per trial.
- **Dimensionally Nonsensical Concentration Units (`μM/ml` and `mM/ml`) and Impossible Molar Stoichiometry of SNAP:**
  - Throughout the Results (lines 50 and 61), $\bullet\text{NO}$ concentrations are written as **`μM/ml`** and **`mM/ml`** (e.g., `2.5 to 16.63 μM/ml` and `1.07 and 1.51 mM/ml`). Molarity ($\text{M} = \text{mol/L}$) is already a volume concentration; dividing $\mu\text{M}$ or $\text{mM}$ by $\text{mL}$ (`mM/ml`) is dimensionally incorrect.
  - More seriously, in line 61 and Figure 2A/C, the authors report that treating ST cells with **$800\text{ }\mu\text{M}$ ($0.80\text{ mM}$) SNAP** produced **$1.07\text{ and }1.51\text{ mM}$** $\bullet\text{NO}$, and treating MARC145 cells with **$400\text{ }\mu\text{M}$ ($0.40\text{ mM}$) SNAP** produced **$1.31\text{ and }1.41\text{ mM}$** $\bullet\text{NO}$. Because each molecule of *S*-nitroso-*N*-acetylpenicillamine (`SNAP`) contains exactly **one** nitroso ($\text{-NO}$) group ($1:1$ molar stoichiometry), $400\text{ }\mu\text{M}$ SNAP can release at most $400\text{ }\mu\text{M}$ ($0.40\text{ mM}$) of nitrite/nitrate! Reporting $1.31\text{--}1.41\text{ mM}$ $\bullet\text{NO}$ from $0.40\text{ mM}$ SNAP ($350\%$ molar yield) indicates either unsubtracted background nitrate in the culture medium/serum or a Griess calibration/calculation error.
- **Missing Thiol Backbone Control (`NAP`) in Antiviral Assays:**
  - The *in vitro* antiviral experiments compare $400\text{--}800\text{ }\mu\text{M}$ SNAP against untreated media without including the non-nitrosylated parent compound *N*-acetylpenicillamine (`NAP`) or light-inactivated/spent SNAP as a control to rule out non-$\bullet\text{NO}$ thiol effects on cell physiology or viral replication.

### 3. Biological / Experimental Grounding & Claim Proportionality
- **[Moderately Supported]** *In vitro* treatment of ST cells with $800\text{ }\mu\text{M}$ SNAP reduces PRCV infectious titers ($\text{TCID}_{50}/\text{mL}$) at 24 h ($P < 0.05$) and 48 h ($P < 0.01$), whereas $400\text{ }\mu\text{M}$ SNAP does not significantly reduce PRRSV titers in MARC145 cells.
- **[Moderately Supported]** PRRSV infection of primary gnotobiotic porcine alveolar macrophages (*in vitro*) does not induce detectable $\bullet\text{NO}$ accumulation over mock-infected macrophages.
- **[Overstated]** The claim in the Abstract and Figure 1 title that PRCV infection induces a large increase in BAL $\bullet\text{NO}$ *in vivo* is overstated because between-trial and inter-animal variance rendered all group differences statistically non-significant.

### 4. Reproducibility & Data Completeness
- **Reagents & Strains:** Virus strains (`PRRSV SD23983`, `VR2332`, `MN184`; `PRCV ISU-1`), cell lines (`ST`, `MARC145`), monoclonal antibodies (`SDOW-17`, `25H7/14E3`), and the Cayman Griess assay kit are clearly identified.
- **Data Reporting:** Raw animal-level BAL Griess measurements and standard curve parameters are not tabulated, and the alveolar macrophage *in vitro* experiment (line 59) is reported as "data not shown" from a single 5-day-old gnotobiotic pig.
</Blinded Review: TIME_ANON_0158>
