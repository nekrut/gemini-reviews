# Review of PMC8264168 (PMID:34236606)

**Manuscript Title:** SARS-CoV-2 in Human Sewage and River Water from a Remote and Vulnerable Area as a Surveillance Tool in Brazil  
**Authors:** Fongaro G, Rogovski P, Savi BP, Cadamuro RD, Pereira JVF, Anna IHS, Rodrigues IH, Souza DSM, Saravia EGT, Rodríguez-Lázaro D, da Silva Lanna MC.  
**Journal / Preprint:** *Food Environ Virol* (2022; `PMC8264168` / `PMID:34236606` / `10.1007/s12560-021-09487-9`)  
**Calibration Study Cohort:** Cohort A — Known Invalid / Refuted (`A32` | Double-Blinded as `ANON_193`)  
**Overall Score:** **6.0 / 10.0** (Mixed / Salvageable)  
* **Score Breakdown:** Rigor: 1.8/3.5 | Claims: 1.7/2.5 | Biology: 1.5/2.0 | Reproducibility: 1.0/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This brief surveillance report describes the RT-qPCR detection of SARS-CoV-2 RNA (CDC N1 and N2 targets) in raw sewage and river water samples collected in August 2020 from rural, low-sanitation areas of Minas Gerais State, Brazil, more than one week prior to the first officially notified COVID-19 clinical cases in those localities (August 29, 2020). Five 2-L samples were collected at each of five sites: raw sewage from a regional prison (150 inmates) and miner accommodation units (100 residents), and river water at one site upstream and two sites downstream (6 km apart) of a rural community (~1,500 inhabitants) lacking basic sewage treatment. Using spiked Murine coronavirus (MHV-3) as a whole-process control, the authors report viral recovery efficiencies of $6 \pm 2\%$ in sewage (glycine/PEG precipitation) and $39 \pm 2\%$ in river water (electronegative membrane adsorption). SARS-CoV-2 RNA was detected in prison and worker accommodation sewage and in both downstream river sites, while remaining undetected upstream. Raw RT-qPCR data are not deposited in a public repository and are listed only as available on reasonable request.

The study provides a useful field demonstration of wastewater and surface-water surveillance in under-resourced rural settings prior to clinical case reporting. However, the technical execution and reporting suffer from: (1) a direct numerical contradiction between the Abstract and main text regarding the viral load in prison sewage ($3.0 \times 10^4$ vs. $1.3 \times 10^4\text{ GC/mL}$) and incomplete reporting of the second downstream river site in the Abstract; (2) ambiguity as to whether reported SARS-CoV-2 concentrations are raw measured values or adjusted for the 6.5-fold difference in MHV-3 process recovery efficiency between sewage ($6\%$) and river water ($39\%$); (3) omission of sample-level positivity rates (how many of the 5 replicate samples per site were positive), individual N1 vs. N2 $C_t$ values, limit of detection/quantification (LOD/LOQ), and negative extraction/PCR controls; and (4) lack of open raw data. All of these issues can be resolved through textual corrections and a supplementary table of raw RT-qPCR measurements.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **SARS-CoV-2 RNA was present in raw sewage from the prison and worker accommodations and in river water downstream (but not upstream) of the rural community prior to official case notification (Fig. 2): [Moderately Supported].**  
  The upstream-negative vs. downstream-positive spatial contrast along the rural river and detection in institutional sewage prior to August 29, 2020, are consistent with unrecognized community shedding. However, because individual $C_t$ values, N1/N2 concordance across the 5 replicate grab samples per site, and negative extraction/no-template control results are not reported, the exact false-positive safeguards near the assay limit of detection cannot be independently verified.

* **Quantitative viral loads in presidio sewage ($3.0 \times 10^4$ vs. $1.3 \times 10^4\text{ GC/mL}$), worker sewage ($4.3 \times 10^4\text{ GC/mL}$), and downstream river water ($1.1 \times 10^2$ and $1.7 \times 10^3\text{ GC/mL}$): [Fragile].**  
  First, the Abstract states $3.0 \times 10^4\text{ GC/mL}$ for the presidio, whereas line 28 of *The Study* reports $1.3 \times 10^4\text{ GC/mL}$. Second, line 20 describes spiking MHV-3 to calculate recovery efficiency ($6 \pm 2\%$ for sewage vs. $39 \pm 2\%$ for river water), but the manuscript never states whether the reported SARS-CoV-2 $\text{GC/mL}$ numbers are raw (unadjusted) concentrations or recovery-corrected concentrations, nor does it report the standard deviation or range across the 5 samples per site.

* **Wastewater and river monitoring serves as a non-invasive early warning tool in vulnerable rural communities with poor sanitation: [Well Supported].**  
  As a qualitative public health surveillance proof-of-concept, detecting viral shedding in shared sewage tanks and receiving surface waters ahead of delayed rural clinical testing aligns with established wastewater epidemiology principles.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Provide Complete Sample-Level RT-qPCR Data (N1, N2, MHV-3, and Negative Controls) in a Table
* **WHY:** The manuscript states that 5 samples (2 L each) were collected per site and assayed in duplicate for N1 and N2, and Fig. 2 averages N1 and N2 together without reporting how many of the 5 samples per site tested positive, what the individual $C_t$ values were, or how negative controls performed. Averaging N1 and N2 across replicates without reporting variance or non-detects obscures assay reliability, especially in river water at $1.1 \times 10^2\text{ GC/mL}$.
* **WHAT:** Add a table listing all 25 environmental samples (5 sites $\times$ 5 samples) plus extraction/PCR negative controls, showing N1 $C_t$ and $\text{GC/mL}$, N2 $C_t$ and $\text{GC/mL}$, MHV-3 recovery (%), and assay LOD/LOQ.
* **HOW:** Compile the raw duplicate RT-qPCR outputs already generated for Fig. 2 into Table 1 in the main text (which directly fulfills the Data Availability requirement without compromising site confidentiality).

#### 2. Clarify Concentration Math and Recovery Efficiency Adjustment
* **WHY:** Sewage samples were concentrated via PEG precipitation ($6 \pm 2\%$ MHV-3 recovery), whereas river water was concentrated via electronegative filtration ($39 \pm 2\%$ recovery). If the reported SARS-CoV-2 $\text{GC/mL}$ values are unadjusted for recovery and concentrator volume factor, direct quantitative comparison between sewage and river water is biased by more than 6-fold; conversely, if they were divided by MHV-3 recovery, propagating a $6 \pm 2\%$ denominator introduces large variance.
* **WHAT:** Explicitly state the concentration factor (initial 2 L volume to final concentrated eluate volume and RNA template volume per reaction) and specify whether SARS-CoV-2 $\text{GC/mL}$ values are raw or recovery-adjusted.
* **HOW:** Add the exact formula used to convert copies/reaction (from the IDT standard curve, 10 to $3.0 \times 10^6\text{ copies/reaction}$) to $\text{GC/mL}$ of original water/sewage in *The Study* (line 20). Note that $1.1 \times 10^2\text{ GC/mL}$ in original river water corresponds to $2.2 \times 10^5\text{ GC}$ in a 2-L sample, and verify that the unit conversion ($\text{GC/mL}$ vs. $\text{GC/L}$) is arithmetically exact.

#### 3. Reconcile Numerical Discrepancies Between the Abstract and Main Text
* **WHY:** Contradictory concentrations between the Abstract and main text undermine reader confidence.
* **WHAT & HOW:**
  * **Line 8 vs. Line 28:** Reconcile the presidio sewage concentration between the Abstract ($3.0 \times 10^4\text{ GC/mL}$) and line 28 ($1.3 \times 10^4\text{ GC/mL}$), and include both downstream river sites ($1.1 \times 10^2$ and $1.7 \times 10^3\text{ GC/mL}$) in the Abstract alongside their standard deviations ($\pm\text{SD}$ across the $n = 5$ samples).
  * **Line 15 vs. Line 8:** Standardize the geographical description of Minas Gerais State (referred to as *"Southern Brazil"* in the Abstract, line 8, and *"South-eastern Brazil"* in the Introduction, line 15; Minas Gerais is in Southeastern Brazil).
  * **Line 20:** Fix the typo *"just with the first COVID-19 wave pick"* to *"during the first COVID-19 wave peak"*, and in line 48 change *"available from the corresponding on reasonable request"* to *"included in Table 1 of this article"*.
