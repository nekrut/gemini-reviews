# Review of FEXP_ANON_134

**Overall Score:** **3.0 / 10.0** (Flawed / Overstated)
* **Score Breakdown:** Rigor: 0.8/3.5 | Claims: 0.7/2.5 | Biology: 0.9/2.0 | Reproducibility: 0.6/2.0
* **Scientific Core Score:** **2.4 / 8.0**

---

## 1. Blinded Metadata Perception

* **Manuscript ID:** `FEXP_ANON_134`
* **Perceived Study Type:** Case-control resting-state fMRI study ($n = 20$ patients with primary intravaginal anejaculation [PIAJ] vs. $n = 16$ healthy controls [HCs]).
* **Domain & Focus:** Andrological neuroimaging (fractional amplitude of low-frequency fluctuation [fALFF], regional homogeneity [ReHo], and seed-based functional connectivity [FC] processed in `DPARSF` and `REST`).

---

## 2. Executive Summary & Editorial Verdict

This study compares resting-state fMRI metrics (fALFF, ReHo, and post-hoc seed-based FC) between 20 patients with primary intravaginal anejaculation (PIAJ) and 16 healthy controls. The authors claim that PIAJ patients exhibit increased fALFF in the left precuneus, increased ReHo in six cortical clusters (including bilateral precuneus and left postcentral gyrus), and widespread increases in seed-based FC that reflect heightened top-down cortical inhibition over ejaculation.

**Editorial Verdict:** **Reject (Severe Internal Contradictions and Methodological Flaws).** A forensic audit of the text, tables, MNI coordinates, and statistical thresholds reveals pervasive, irreconcilable contradictions:
1. **Sign Reversal on the Primary fALFF Finding:** While the `Abstract`, `Results` text, `Discussion`, and `Conclusion` repeatedly claim that PIAJ patients showed **increased** fALFF in the left precuneus, **`Table 2` reports a negative $t$-statistic (`Peak t value = −6.14`)** and the **`Figure 1b` caption explicitly states *"Brain regions exhibiting decreased fractional amplitude of low-frequency fluctuation (fALFF) between PIAJ and HCs groups"*!**
2. **Gross Anatomical Mislabeling of MNI Coordinates (`Precuneus` vs. `Postcentral Gyrus`):** In `Table 2`, the clusters labeled `Left precuneus` (`−51, −6, 30`) and `Right precuneus` (`54, 0, 27`) have lateral MNI $X$-coordinates of $-51\text{ mm}$ and $+54\text{ mm}$ near the central sulcus ($Y = -6\text{ to }0\text{ mm}$), which lie in the **lateral precentral/postcentral sensorimotor cortex**, NOT the medial parietal precuneus ($|X| < 15\text{ mm}, Y \approx -50\text{ to }-70\text{ mm}$). Confirming this mix-up, the `Results` text (line 145) refers to the seed as **`right postcentral gyrus (altered ReHo)`**, whereas `Table 3` (line 137) labels the exact same ROI as **`Right precuneus as ROI`** (and omits three of the seven target regions claimed in the prose, as well as the entire `Right middle temporal gyrus as ROI` section claimed in line 147).
3. **Ad-Hoc Switching of Legacy Multiple-Comparison Thresholds:** The authors switch arbitrarily across three different correction schemes in the legacy `REST` toolkit—GRF ($p < 0.001$, cluster $p < 0.05$), `AlphaSim` ($p < 0.001$, cluster $\ge 6$ voxels), and a relaxed `AlphaSim` ($p < 0.005$, cluster $\ge 12$ voxels)—across 8 post-hoc seeds selected from the same 36 subjects without correcting for multiple seeds.

### Assessment of Specific Conclusions & Support

* **PIAJ patients show increased fALFF values in the left precuneus compared with HCs: [Methodologically Flawed].**  
  Directly contradicted by `Table 2` (`Left precuneus`, MNI `−21, −54, 27`, `Peak t value = −6.14`) and `Figure 1b` (*"Brain regions exhibiting decreased fractional amplitude of low-frequency fluctuation (fALFF)"*). The entire biological narrative in the `Discussion` arguing that "increased fALFF in the left precuneus increases top-down inhibition" is built on a sign-inverted reading of their own $t$-map.

* **PIAJ patients show increased ReHo in the bilateral precuneus and widespread cortical regions: [Methodologically Flawed].**  
  The MNI coordinates reported in `Table 2` for `Left precuneus` (`−51, −6, 30`) and `Right precuneus` (`54, 0, 27`) are anatomically located in the lateral pericentral (precentral/postcentral) cortex, not the precuneus. Furthermore, thresholding via legacy `REST AlphaSim` with a minimum cluster size of 6 voxels yields uncalibrated family-wise false-positive rates.

* **Regions with altered fALFF and ReHo show increased seed-based FC with widespread cortical regions driving top-down inhibition of ejaculation: [Methodologically Flawed].**  
  Seeds were defined from group differences in the same $20\text{ vs. }16$ dataset, tested across 8 separate seed-to-whole-brain maps without correction for the number of seeds, thresholded with ad-hoc switching between GRF, `AlphaSim` ($p < 0.001, k \ge 6$), and `AlphaSim` ($p < 0.005, k \ge 12$), and `Table 3` does not match the regions described in the `Results` text.

---

## 3. Forensic Defect Inventory

### 1. Direct Contradiction Between Text (`Increased fALFF`) and `Table 2` / `Figure 1b` (`Decreased fALFF`, $t = -6.14$) (Pillar 3 & Pillar 7)
* **Defect:** In `Table 2` (line 82), the only significant fALFF cluster (`Left precuneus`, `−21, −54, 27`, $k = 232$) has `Peak t value = −6.14`, while positive `Peak t values` (`+4.12` to `+4.77`) denote `PIAJ > HCs` in the ReHo rows immediately below it. Consistently, `Figure 1b` is colored blue and its legend reads: *"(b) Brain regions exhibiting decreased fractional amplitude of low-frequency fluctuation (fALFF) between PIAJ and HCs groups... Red: increased values; blue: decreased values."* Yet the `Abstract`, `Results` (line 73), `Discussion` (lines 152, 156), and `Conclusion` all state that left precuneus fALFF was **increased** in PIAJ patients.
* **Actionable Fix:** Reconcile the sign of the left precuneus fALFF difference ($t = -6.14$, i.e., decreased in PIAJ relative to HCs) across the entire manuscript and revise the biological interpretation accordingly.

### 2. Anatomical Coordinate Mislabeling (`Precuneus` at $X = \pm 51\text{--}54\text{ mm}$) and Text–Table Discrepancies in `Table 3` (Pillar 6 & Pillar 7)
* **Defect:**
  1. In MNI152 space, the precuneus is a medial parietal structure near the interhemispheric fissure ($|X| < 18\text{ mm}, Y \in [-45, -75]\text{ mm}$). In `Table 2` (ReHo), `Left precuneus` is listed at `(-51, -6, 30)` and `Right precuneus` at `(54, 0, 27)`—coordinates that lie in the lateral precentral/postcentral gyrus!
  2. In `Results` (line 145), the authors describe FC results for the **`right postcentral gyrus (altered ReHo)`** with seven target regions (*"left middle temporal gyrus, right rolandic operculum, right postcentral gyrus, right supplementary motor area, right middle temporal gyrus, right calcarine fissure, and right angular gyrus"*). However, `Table 2` has **no** `right postcentral gyrus` ReHo cluster, and `Table 3` (line 137) instead lists **`Right precuneus as ROI`** with only four clusters (two of which are labeled `Left middle temporal gyrus d` and `Left middle temporal gyrus e` with unexplained footnotes `d` and `e`), omitting the right rolandic operculum, right postcentral gyrus, right SMA, and right angular gyrus!
  3. In `Results` (line 147), the authors state: *"Finally, when the right middle temporal gyrus (altered ReHo) was selected as an ROI, PIAJ patients showed increased FC values in the right lingual gyrus (GRF correction... Table 3 and Figure 2)."* Yet **`Table 3` completely omits the `Right middle temporal gyrus as ROI` row!**
  4. In `Table 3` (lines 114–115), `Left middle temporal gyrus` (`−45, −45, 9`, $k = 506$) and `Left postcentral gyrus` (`−45, −3, 30`, $k = 243$) have the exact same peak $t$-value (`5.89` and `5.89`), and `Left postcentral gyrus as ROI` includes a self-connectivity cluster in `Left postcentral gyrus` (`−45, −24, 48`, abutting the seed `−48, −21, 48`).
* **Actionable Fix:** Re-map all MNI peak coordinates against the AAL/Harvard-Oxford atlas to correct the `Precuneus` vs. `Postcentral/Precentral gyrus` mislabeling, and regenerate `Table 3` so that every seed and target cluster matches the statistical maps and text.

### 3. Arbitrary Switching of Multiple-Testing Corrections in Legacy `REST` Software (Pillar 4 & Pillar 5)
* **Defect:** Across `Table 2` and `Table 3`, the authors cherry-pick three different multiple-comparison thresholds depending on the seed:
  * GRF (`voxel P < 0.001, cluster P < 0.05`) for fALFF and 3 FC seeds;
  * `AlphaSim` (`P < 0.001, minimum cluster size = 6 voxels`) for ReHo and 4 FC seeds;
  * `AlphaSim` (`P < 0.005, minimum cluster size = 12 voxels`) for the `Left precuneus (altered fALFF)` FC seed!
  Using legacy `REST AlphaSim` (which underestimates spatial smoothness and fails to control FWE) with a 6-voxel cluster threshold, and relaxing the voxel threshold to $p < 0.005$ ($k \ge 12$) when a seed fails to yield results at $p < 0.001$, constitutes severe $p$-hacking across 8 unadjusted seed maps.
* **Actionable Fix:** Apply a single, uniform non-parametric permutation test (e.g., `DPABI`/`PALM` with 5,000 permutations, cluster-forming $p < 0.001$, and FWE cluster correction $p_{\text{FWE}} < 0.05/8$ Bonferroni-adjusted across all seeds).

### 4. Mathematical & Physical Reporting Errors in `Methods` (Pillar 3 & Pillar 7)
* **Defect:**
  1. `MRI data acquisition` (line 31): Reports $T_1$-weighted structural parameters as `repetition time = 7600 ms, echo time = 3400 ms`. A $3.4\text{ s}$ echo time for a $T_1$ structural scan is physically impossible (the actual Philips 3D TFE parameters are $TR = 7.6\text{ ms}, TE = 3.4\text{ ms}$, mismultiplied by $10^3$).
  2. `Calculation of fALFF, ReHo, and FC` (lines 41, 43): States that fALFF and ReHo (Kendall's $W$) values were normalized to $z$-values *"using the Fisher's r-to-z transformation"*. Fisher's $r$-to-$z$ transformation ($\frac{1}{2}\ln\frac{1+r}{1-r}$) applies to Pearson correlation coefficients (`FC`), whereas `DPARSF`/`REST` computes `zfALFF` and `zReHo` via spatial $z$-standardization ($\frac{x - \bar{x}}{s}$).
  3. `MRI data preprocessing` (line 36): Lists spatialsmoothing *before* linear detrending and bandpass filtering for fALFF/FC, but omits spatial smoothing from the ReHo description (`line 43`) without stating when post-ReHo spatial smoothing was performed.
* **Actionable Fix:** Correct the $T_1$ scan parameters to $TR = 7.6\text{ ms}, TE = 3.4\text{ ms}$, replace "Fisher's $r$-to-$z$ transformation" with "$z$-score standardization across the brain mask" for `zfALFF` and `zReHo`, and document post-ReHo spatial smoothing.

---

## 4. Quantitative Rubric Scoring

| Rubric Dimension | Score | Max | Forensic Justification |
| :--- | :---: :---: | :---: | :--- |
| **1. Methodological & Statistical Rigor** | **0.8** | **3.5** | Ad-hoc switching between GRF, `AlphaSim` ($p < 0.001, k \ge 6$), and `AlphaSim` ($p < 0.005, k \ge 12$) across 8 post-hoc seeds selected in-sample ($n = 20$ vs. $16$); incorrect Fisher $r$-to-$z$ description for fALFF/ReHo. |
| **2. Claim-to-Evidence Alignment** | **0.7** | **2.5** | Headline claim of "increased fALFF in the left precuneus" is directly contradicted by `Table 2` ($t = -6.14$) and `Figure 1b` ("decreased fALFF"). |
| **3. Data Integrity & Biological Plausibility** | **0.9** | **2.0** | Lateral sensorimotor coordinates ($\pm 51\text{ to }54, -6\text{ to }0, 27\text{ to }30$) are misidentified as the medial parietal "precuneus", invalidating the anatomical and physiological interpretation. |
| **4. Reproducibility & Data Integrity** | **0.6** | **2.0** | Severe text–table–figure contradictions (`Table 2` vs. text on fALFF sign; `Table 3` missing seeds/clusters described in text; physically impossible $T_1$ $TR = 7600\text{ ms}, TE = 3400\text{ ms}$). |
| **Scientific Core Score** | **2.4** | **8.0** | Sum of Rigor + Claims + Biology (`0.8 + 0.7 + 0.9`). |
| **Overall Composite Score** | **3.0** | **10.0** | **Flawed / Overstated** (`0.8 + 0.7 + 0.9 + 0.6`). |
