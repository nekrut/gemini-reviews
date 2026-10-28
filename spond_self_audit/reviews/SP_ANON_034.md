# Blinded Review: SP_ANON_034
**Composite Score:** 3.8 / 10.0 (Rigor: 1.0/3.5 | Claims: 0.8/2.5 | Biology: 1.0/2.0 | Reproducibility: 1.0/2.0)
**Bias Category:** Censoring/Truncation Bias (Excluding Zero-Droplet CSF Samples), Detection-Limit Contamination & Denominator Mismatch
**Verdict:** Reject
**Study Modality:** Wet-Lab Primary Experimental
**Technology Maturity:** Mid-Stage High-Throughput
**Epistemic Stage:** Translational/Preclinical/Biomarker

---

### 1. Executive Summary
This study applies droplet digital PCR (ddPCR) targeting HIV-1 *pol* (and human *RPP30* to quantify cellular input) to paired cerebrospinal fluid (CSF) cellular pellets and peripheral blood mononuclear cells (PBMCs) from 28 HIV-infected participants (19 with suppressed plasma HIV RNA $<50\text{ copies/mL}$ and 9 unsuppressed) and 20 HIV-seronegative controls. The authors report detecting HIV DNA in 18/28 (64%) CSF cell pellets (and 3/20 [15%] HIV-negative controls), find no difference in CSF HIV DNA levels between suppressed and unsuppressed individuals ($p=0.14$), and claim as their headline finding that HIV DNA concentrations are ~10-fold higher in CSF leukocytes than in PBMCs ($3.3$ vs. $2.4 \log_{10}\text{ copies}/10^6\text{ cells}$, $p<0.001$) among the subset of 18 subjects with detectable CSF HIV DNA. A forensic audit reveals that this headline claim is a mathematical artifact caused by discarding the 10 zero-droplet CSF samples in a paucicellular assay where a single positive droplet equals $\sim 3.0 \log_{10}\text{ copies}/10^6\text{ cells}$, compounded by a 15% false-positive background rate in HIV-negative controls and inconsistent cellular normalization denominators.

---

### 2. Methodological & Statistical Audit
* **Truncation Bias + Small-Denominator Floor Artifact in the Headline CSF vs. PBMC Comparison:** Across all 28 HIV-positive participants, the authors admit on page 44 that HIV DNA levels did **not** differ significantly between CSF cell pellets and PBMCs ($2.7$ vs. $2.3 \log_{10}$, $p=0.41$). To obtain their headline result ($3.3$ vs. $2.4 \log_{10}$, $p<0.001$, Abstract and Figure 1B), the authors **excluded the 10 participants (36%) who had 0 positive HIV DNA droplets in CSF**. Consider the arithmetic of normalizing by *RPP30* in paucicellular CSF pellets:
  * The median cellular input per CSF ddPCR reaction was only **2,590 cells** (IQR 827–3,309; minimum 212 cells), compared to **147,000 cells** for PBMCs (a 57-fold smaller denominator in CSF).
  * In a CSF sample containing 1,000 cells ($10^{-3} \times 10^6$ cells), observing **0 positive droplets** yields $0\text{ copies}/10^6\text{ cells}$, whereas observing **just 1 single positive droplet** automatically translates to $1 / 10^{-3} = \mathbf{1,000\text{ copies}/10^6\text{ cells}}$ ($3.0 \log_{10}$)! In a CSF sample with 212 cells, 1 positive droplet equals **$4,717\text{ copies}/10^6\text{ cells}$ ($3.67 \log_{10}$)**!
  * By discarding all CSF samples with 0 droplets and taking the average of the remaining 18 samples (which by mathematical necessity of having $\ge 1$ droplet in $\sim 10^3$ cells are bounded below by $\sim 2.5\text{–}3.6 \log_{10}$), the authors manufacture an artificial 10-fold "enrichment" in CSF over PBMCs (where 147,000 cells allow detection down to $0.8 \log_{10}$).
* **False-Positive Background Indistinguishable from "Positive" Paucicellular CSF Samples:** Among the 20 HIV-seronegative control CSF samples, **3/20 (15%) registered 1 positive HIV DNA droplet** (false-positive rate of 0.15 per reaction). Among the 18 HIV-positive CSF samples declared "detectable," **6 samples (33%) had only a single positive droplet**! Under a Poisson/binomial background model where 15% of negative controls produce 1 false-positive droplet, a single-droplet call in an HIV+ CSF pellet cannot be distinguished from background noise, yet these single-droplet samples were retained and scaled by $10^6 / N_{\text{cells}}$ to produce high log-transformed copy numbers.
* **Contradictory Cellular Normalization Denominators (CD4+ T cells vs. Total RPP30 Cells):** In the Methods and Table 1, HIV DNA is described as normalized per $10^6$ total cells via *RPP30* in both CSF and PBMC. However, in the Discussion (page 57), the authors state: *"we normalized HIV DNA content by CD4+ T-cells in PBMC and by total cells in CSF cell pellets."* Because CD4+ T cells represent only ~15–40% of PBMCs (and CSF leukocytes are predominantly T cells and monocytes), normalizing one compartment by CD4+ T cells and the other by total *RPP30* cells—or contradicting the Methods inside the Discussion—invalidates direct numerical comparisons.
* **Differential DNA Extraction Protocols Between Compartments:** PBMCs were extracted via Qiagen silica spin columns (which lose 30–50% of input DNA during binding/elution, though normalizing to *RPP30* partially compensates), whereas CSF cell pellets underwent direct heat/proteinase lysis without column purification.
* **Sample Size Discrepancy in Text:** The Methods ("Study population and samples", line 17) states *"We evaluated 29 HIV infected subjects"*, whereas the Abstract, Results, and Table 1 report $N=28$ ($19$ suppressed $+ 9$ unsuppressed).

---

### 3. Biological / Experimental Grounding & Claim Proportionality
* **Claim:** *CSF leukocytes harbor significantly higher concentrations of HIV DNA per million cells than PBMCs ($3.3$ vs. $2.4 \log_{10}$, $p<0.001$).* **[Methodologically Flawed]** — Entirely an artifact of conditioning on $\ge 1$ positive droplet in paucicellular CSF reactions ($N_{\text{cells}} \sim 10^3$) while discarding the 36% of samples with 0 droplets; across all 28 paired samples, $p=0.41$.
* **Claim:** *ddPCR reliably quantifies the HIV DNA reservoir in paucicellular CSF samples.* **[Overstated]** — With a median of 2,590 cells per CSF pellet and a 15% single-droplet false-positive rate in HIV-negative controls, the assay operates at or below a single copy per reaction in most suppressed CSF samples.

---

### 4. Reproducibility & Data Completeness
* **Raw Data Reporting:** Individual subject-level droplet counts (positive HIV droplets, total droplets, *RPP30* cell equivalents, and uncensored zeros) are not tabulated, preventing independent Poisson mixture or left-censored Tobit re-analysis.
