# Review of FEXP_ANON_133

**Overall Score:** **4.7 / 10.0** (Flawed / Overstated)
* **Score Breakdown:** Rigor: 1.5/3.5 | Claims: 1.0/2.5 | Biology: 1.1/2.0 | Reproducibility: 1.1/2.0
* **Scientific Core Score:** **3.6 / 8.0**

---

## 1. Blinded Metadata Perception

* **Manuscript ID:** `FEXP_ANON_133`
* **Perceived Study Type:** Case-control resting-state fMRI study ($N = 105$: $n = 42$ medicated chronic schizophrenia patients with auditory verbal hallucinations [AVH; PANSS P3 $> 3$] vs. $n = 63$ healthy controls [HC]).
* **Domain & Focus:** Clinical psychiatric neuroimaging (seed-based resting-state functional connectivity [rsFC] of the left and right precentral gyrus [PCG] processed via `CONN` 21.a and `SPM12`).

---

## 2. Executive Summary & Editorial Verdict

This study examines seed-based resting-state functional connectivity of the bilateral precentral gyrus (PCG) in 42 medicated chronic schizophrenia patients experiencing auditory verbal hallucinations (`PANSS P3 > 3`, mean illness duration $117.8 \pm 102.1$ months) compared with 63 age- and sex-matched healthy controls (`CONN` v21.a default pipeline, voxel threshold $p < 0.001$, cluster-level $p_{\text{FWE}} < 0.05$). The authors report increased rsFC between bilateral PCG seeds and frontal/cingulate/motor clusters (SFG, SMA, ACC, paracingulate gyrus, precuneus) and decreased rsFC with occipital/visual and right cerebellar crus I clusters, attributing these alterations to the neurobiology of auditory verbal hallucinations (AVH).

**Editorial Verdict:** **Reject / Major Re-Framing and Re-Analysis Required.** While the standard `CONN` 21.a preprocessing and cluster-level FWE statistical thresholding ($p < 0.001$ voxel, $p_{\text{FWE}} < 0.05$ cluster) are appropriately executed for a two-group comparison, the study's central scientific claim—that these PCG connectivity alterations are associated with auditory verbal hallucinations ("higher hallucination proneness" and "involvement of the sensorimotor network in the mechanism of AVH")—is **unsupported by the experimental design**. Because the study lacks a non-hallucinating schizophrenia control group (`SZ-NAVH`), fails to control for antipsychotic medication dosage (dopamine $D_2$ receptor blockade directly alters primary motor cortex [PCG] and supplementary motor area [SMA] connectivity), and performs zero correlation or regression analyses against `PANSS P3` (hallucination severity) or `PANSS` subscale scores, the observed differences between chronic medicated patients and healthy controls cannot be attributed to AVH rather than general schizophrenia pathology or antipsychotic drug effects. Furthermore, `Table 1` contains a psychometric impossibility in the healthy control PANSS scores (`PANSS N = 6.0 ± 0.0`, below the minimum possible 7-item score of $7.0$).

### Assessment of Specific Conclusions & Support

* **Medicated patients with chronic schizophrenia show hyperconnectivity between bilateral precentral gyrus (PCG) and frontal-cingulate/SMA regions and hypoconnectivity with occipital/visual regions relative to healthy controls: [Moderately Supported].**  
  The two-group GLM in `CONN` 21.a uses a standard cluster-forming threshold ($p < 0.001$) and FWE cluster-size correction ($p_{\text{FWE}} < 0.05$), and repeating the model with education as a covariate confirmed cluster stability. However, because all 42 patients were receiving typical and/or atypical antipsychotics and chlorpromazine equivalents were not included as covariates, motor-cortex (`PCG`/`SMA`) dysconnectivity is confounded by pharmacological dopamine blockade.

* **Observed PCG connectivity alterations reflect the mechanism of auditory verbal hallucinations (AVH) and higher hallucination proneness: [Methodologically Flawed].**  
  Comparing `SZ + AVH` ($n = 42$) solely against `HC` ($n = 63$) confounds AVH status completely with schizophrenia diagnosis, chronicity ($\sim 10$ years), and antipsychotic exposure. Moreover, the authors did not test whether PCG rsFC correlates with `PANSS P3` ($5.1 \pm 0.6$) or `PANSS Positive` ($21.0 \pm 3.6$) within the patient group.

* **Lateralized right-hemisphere dysconnectivity reflects diminished left-greater-than-right language asymmetry in AVH: [Overstated].**  
  No formal statistical test of hemispheric laterality (e.g., $\text{Left Seed} - \text{Right Seed}$ interaction or Laterality Index) or handedness verification (handedness is never reported in `Participants` or `Table 1`) was conducted; visual inspection of thresholded cluster maps does not establish a statistically significant lateralization deficit.

---

## 3. Forensic Defect Inventory

### 1. Missing Clinical Comparator Group (`SZ-NAVH`) and Absence of Symptom Correlation Analysis (Pillar 1 & Pillar 5)
* **Defect:** Throughout the `Abstract`, `Introduction`, and `Discussion`, the study frames its findings around auditory verbal hallucinations (AVH). However, without a non-hallucinating schizophrenia control group (`SZ-NAVH`) or within-patient regression against hallucination severity (`PANSS P3`), a `SZ-AVH vs. HC` contrast measures the composite effect of chronic schizophrenia + antipsychotic medication + AVH.
* **Actionable Fix:** Compute voxel-wise and cluster-level regressions between PCG rsFC and `PANSS P3` (controlling for `PANSS Total - P3`, illness duration, and antipsychotic chlorpromazine-equivalent dose) within the $n = 42$ patient cohort, and reframe all `SZ vs. HC` findings as general schizophrenia-associated sensorimotor alterations rather than AVH-specific mechanisms.

### 2. Psychometrically Impossible Healthy Control `PANSS` Scores in `Table 1` (Pillar 7)
* **Defect:** In `Table 1` (lines 94–103), the Healthy Control (`HC`, $N = 63$) group is reported as having:
  * `PANSS P score`: $7.1 \pm 0.3$
  * `PANSS G score`: $16.8 \pm 1.0$
  * `PANSS N score`: **$6.0 \pm 0.0$**
  * `PANSS score Total`: **$29.8 \pm 1.1$**
  The standard Positive and Negative Syndrome Scale (PANSS) comprises 7 Positive items (minimum score $= 7$), **7 Negative items (minimum score $= 7$, since each item is rated $1 = \text{absent}$ to $7 = \text{extreme}$)**, and 16 General Psychopathology items (minimum score $= 16$), yielding a minimum possible Total score of **$30.0$**. A mean `PANSS N` score of $6.0 \pm 0.0$ and a `PANSS Total` score of $29.8 \pm 1.1$ are mathematically impossible under standard 1–7 PANSS scoring and indicate that one Negative subscale item was systematically omitted or scored as $0$ in the control group.
  Additionally, in `Table 1` Row 1 (`Education: primary/secondary/higher`), the patient counts are `8 / 26 / 6`, which sum to **$40$**, not $N = 42$ (2 patients have missing education data despite Section `2.1` stating that 5 cases were already excluded due to missing demographic or clinical data).
* **Actionable Fix:** Audit the raw PANSS item spreadsheets to identify which Negative subscale item was omitted or mis-coded in the HC group, and account for the 2 patients missing from the `Table 1` education row (`8 + 26 + 6 = 40` vs. $N = 42$).

### 3. Uncontrolled Antipsychotic Medication Confounding on Primary Motor Cortex (`PCG`) Connectivity and Missing Handedness Data (Pillar 2 & Pillar 6)
* **Defect:** The precentral gyrus (`PCG`) and supplementary motor area (`SMA`) are primary targets of nigrostriatal/thalamocortical dopamine $D_2$ antagonism by typical and atypical antipsychotics. Comparing medicated patients against unmedicated controls on motor-cortex connectivity without recording or adjusting for chlorpromazine (CPZ) equivalent doses or extrapyramidal motor symptoms leaves the primary `PCG–SMA` hyperconnectivity finding heavily confounded. Furthermore, neither participant handedness nor head-motion group comparisons (mean framewise displacement in `SZ` vs. `HC`) are reported.
* **Actionable Fix:** Report participant handedness, compare mean framewise displacement (FD) and scrubbed outlier volume counts between `SZ` and `HC`, and include CPZ-equivalent antipsychotic dosage and mean FD as covariates in the group-level GLM.

---

## 4. Quantitative Rubric Scoring

| Rubric Dimension | Score | Max | Forensic Justification |
| :--- | :---: :---: | :---: | :--- |
| **1. Methodological & Statistical Rigor** | **1.5** | **3.5** | Standard `CONN` 21.a FWE cluster correction ($p < 0.001$ voxel, $p_{\text{FWE}} < 0.05$ cluster) and education covariate check, but lacks a `SZ-NAVH` control group, omits within-patient `PANSS P3` regressions, and fails to test hemispheric laterality statistically. |
| **2. Claim-to-Evidence Alignment** | **1.0** | **2.5** | Overstates `SZ vs. HC` differences in medicated chronic patients as revealing the neurobiology of AVH and language lateralization without testing hallucination severity or non-AVH schizophrenia controls. |
| **3. Data Integrity & Biological Plausibility** | **1.1** | **2.0** | Motor cortex (`PCG`/`SMA`) connectivity in medicated schizophrenia is severely confounded by unmodeled antipsychotic dopamine blockade; handedness and group head-motion statistics are omitted. |
| **4. Reproducibility & Data Integrity** | **1.1** | **2.0** | `Table 1` reports an impossible `PANSS N` score ($6.0 \pm 0.0$, minimum possible is $7.0$) and `PANSS Total` ($29.8 < 30.0$), and patient education counts (`8/26/6 = 40`) do not sum to $N = 42$. |
| **Scientific Core Score** | **3.6** | **8.0** | Sum of Rigor + Claims + Biology (`1.5 + 1.0 + 1.1`). |
| **Overall Composite Score** | **4.7** | **10.0** | **Flawed / Overstated** (`1.5 + 1.0 + 1.1 + 1.1`). |
