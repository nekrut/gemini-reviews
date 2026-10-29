# Review of FEXP_ANON_136

**Overall Score:** **3.8 / 10.0** (Flawed / Overstated)
* **Score Breakdown:** Rigor: 0.9/3.5 | Claims: 0.8/2.5 | Biology: 0.9/2.0 | Reproducibility: 1.2/2.0
* **Scientific Core Score:** **2.6 / 8.0**

---

## 1. Blinded Metadata Perception

* **Manuscript ID:** `FEXP_ANON_136`
* **Perceived Study Type:** Secondary analysis of a public resting-state fMRI repository (UCLA Consortium for Neuropsychiatric Phenomics [CNP], OpenNeuro `ds000030`; $N = 189$: 40 ADHD, 49 BD, 50 SZ, 50 HCs).
* **Domain & Focus:** Transdiagnostic psychiatric neuroimaging (ROI-to-ROI resting-state functional connectivity [rs-FC] across 34 subcortical, cerebellar, and supplementary motor ROIs termed the "procedural memory network", analyzed in `CONN` v21.a).

---

## 2. Executive Summary & Editorial Verdict

This study analyzes resting-state fMRI scans from 189 participants in the public UCLA CNP dataset (40 ADHD, 49 bipolar disorder [BD], 50 schizophrenia [SZ], and 50 healthy controls [HCs]) using `CONN` v21.a across 34 ROIs (basal ganglia, subthalamic nucleus, substantia nigra, claustrum, SMA, and cerebellar lobules I–X) defined as the "procedural memory network". The authors report pairwise $t$-tests between each patient group and HCs at $p < 0.001$ alongside effect sizes ($\eta^2$), concluding that disorder-specific disruptions in the procedural memory network underlie cognitive network impairments in ADHD, BD, and SZ.

**Editorial Verdict:** **Reject (Mathematically Impossible Statistical Tables and Uncorrected Multiple Comparisons).** Although the raw dataset (`OpenNeuro ds000030`) and `CONN` v21.a preprocessing pipeline are standard, the statistical reporting and scientific claims suffer from fatal defects:
1. **Mathematically Impossible Effect Sizes ($\eta^2$) in `Tables 3, 4, and 5`:** For an independent-samples $t$-test with degrees of freedom $df = n_1 + n_2 - 2$, eta-squared is strictly determined by $\eta^2 = \frac{t^2}{t^2 + df}$. In `Table 3` ($n_1 = 40, n_2 = 50, df = 88$), $t = 4.00$ yields $\eta^2 = \frac{16}{104} = \mathbf{0.154}$, and $t = -3.13$ yields $\eta^2 = \mathbf{0.100}$; yet `Table 3` reports **`η² = 0.53`** and **`η² = 0.49`** (inflated by nearly $4\times$ to $5\times$)! Even more glaringly, in `Table 4` ($df = 97$), five positive $t$-values between $3.20$ and $3.35$ (which must all have $\eta^2 \in [0.095, 0.104]$) are assigned wildly disparate $\eta^2$ values (`0.28, 0.21, 0.16, 0.12, 0.14`), while negative $t$-values ($-3.80$ and $-3.52$, true $\eta^2 = 0.130$ and $0.113$) are reported as `0.52` and `0.32`, and `Table 5` prints a malformed string **`0.0.19`**!
2. **Uncorrected One-Tailed $p$-Values Misrepresented as FDR-Corrected:** The `Statistical analysis` section claims that False Discovery Rate (FDR) correction was applied across all connections. However, every $p$-value reported in `Tables 3–5` (e.g., $t = 4.00 \implies p = 0.000067$; $t = 3.35 \implies p = 0.00058$; $t = 3.20 \implies p = 0.00093$) is the **uncorrected one-tailed $p$-value** from Student's $t$-distribution! Across $\binom{34}{2} = 561$ unique undirected ROI pairs (miscounted by the authors as "992 functional connections", which is $32 \times 31$), a two-tailed threshold of $q_{\text{FDR}} < 0.05$ requires uncorrected two-tailed $p \lesssim 0.00018$ ($|t| \gtrsim 3.90$). Thus, virtually all reported connections in BD and SZ fail to survive genuine FDR correction across the $34 \times 34$ matrix.
3. **Zero Behavioral or Procedural Memory Data Analyzed:** Despite the UCLA CNP dataset containing extensive neuropsychological batteries, no cognitive or procedural memory task measures were analyzed or correlated with rs-FC.

### Assessment of Specific Conclusions & Support

* **ADHD, BD, and SZ patients exhibit FDR-significant alterations in procedural memory network rs-FC with large effect sizes ($\eta^2$ up to $0.53$): [Methodologically Flawed].**  
  The reported $p$-values in `Tables 3–5` are uncorrected one-tailed $p$-values thresholded at $p_{\text{one-tailed}} < 0.001$ rather than FDR-corrected $q$-values across the 561 unique ROI pairs ($\binom{34}{2} = 561$). When two-tailed $p$-values are computed and Benjamini–Hochberg FDR correction is applied across the 561 pairs per group comparison, the majority of reported edges ($|t| \in [3.13, 3.52]$) do not survive at $q_{\text{FDR}} < 0.05$. Moreover, the reported $\eta^2$ values (`0.49`, `0.51`, `0.52`, `0.53`) are mathematically incompatible with the reported $t$-statistics and sample sizes.

* **Altered rs-FC within the procedural memory network is associated with cognitive network impairments in ADHD, BD, and SZ: [Overstated].**  
  No cognitive, behavioral, or clinical symptom measures were included anywhere in the analysis; the claimed link to cognitive network impairment is purely speculative reverse inference in the `Discussion`.

* **The claustrum and caudate are situated within the frontal region of the Default Mode Network (DMN): [Methodologically Flawed].**  
  In Section `BD` (line 201), the authors write: *"Given that the claustrum and caudate are both situated within the frontal region of the DMN, the findings of this study corroborate the potential involvement of these structures in BD."* Anatomically and functionally, the claustrum and caudate nucleus are deep subcortical/telencephalic structures primarily coupled to the salience, frontoparietal, and basal ganglia networks—not the frontal cortex of the DMN. Similarly, the `Abstract` erroneously states that the 34 subcortical and cerebellar ROIs were defined from the *"Harvard-Oxford Cortical Structural Atlas"*.

---

## 3. Forensic Defect Inventory

### 1. Mathematically Impossible $\eta^2$ Values and Malformed Entries in `Tables 3, 4, and 5` (Pillar 4 & Pillar 7)
* **Defect:** In a two-sample $t$-test with $df = n_1 + n_2 - 2$, the proportion of variance explained is $\eta^2 = \frac{t^2}{t^2 + df}$:
  * **`Table 3` (ADHD $n = 40$ vs. HC $n = 50$, $df = 88$):**
    * `Cereb45 l – Cereb3 r`: $t = 4.00 \implies \eta^2_{\text{true}} = \frac{16.00}{104.00} = \mathbf{0.154}$ (Reported: **`0.53`**).
    * `Cereb1 l – Cereb6 l`: $t = -3.13 \implies \eta^2_{\text{true}} = \frac{9.797}{97.797} = \mathbf{0.100}$ (Reported: **`0.49`**).
  * **`Table 4` (BD $n = 49$ vs. HC $n = 50$, $df = 97$):**
    * Five edges with $t = 3.35, 3.34, 3.24, 3.22, 3.20$ have $\eta^2_{\text{true}} = \mathbf{0.104, 0.103, 0.098, 0.097, 0.096}$, yet `Table 4` reports **`0.28, 0.21, 0.16, 0.12, 0.14`**.
    * `subthalamic nucleus r – Cereb6 l`: $t = -3.80 \implies \eta^2_{\text{true}} = \mathbf{0.130}$ (Reported: **`0.52`**).
    * `Cereb9 r – Cereb9 l`: $t = -3.52 \implies \eta^2_{\text{true}} = \mathbf{0.113}$ (Reported: **`0.32`**).
  * **`Table 5` (SZ $n = 50$ vs. HC $n = 50$, $df = 98$):**
    * `Caudate r – putamen l`: $t = 3.35 \implies \eta^2_{\text{true}} = \mathbf{0.103}$ (Reported: **`0.25`**).
    * `subthalamic nucleus r – Cereb6 l`: $t = -3.99 \implies \eta^2_{\text{true}} = \mathbf{0.140}$ (Reported: **`0.51`**).
    * `Cereb1 r – subthalamic nucleus r`: $t = -3.32 \implies \eta^2_{\text{true}} = \mathbf{0.101}$ (Reported: **`0.0.19`**, a corrupted string!).
* **Actionable Fix:** Recompute all $\eta^2$ (and Cohen's $d$) values directly from the $t$-statistics and degrees of freedom using $\eta^2 = \frac{t^2}{t^2 + df}$, and fix the typographical corruption `0.0.19` in `Table 5`.

### 2. Uncorrected One-Tailed $p$-Values Reported Instead of Two-Tailed FDR-Adjusted $q$-Values, and Incorrect Connection Count (`992` vs. `561` / `1122`) (Pillar 3 & Pillar 4)
* **Defect:**
  1. In `Statistical analysis` (line 104), the authors state: *"Among the 992 functional connections between 34 ROIs of the procedural memory network..."* However, 34 ROIs yield $34 \times 33 = \mathbf{1,122}$ directed pairs or $\frac{34 \times 33}{2} = \mathbf{561}$ unique undirected pairs (note that $32 \times 31 = 992$, indicating that 2 of the 34 ROIs listed in `Table 2` were either missing from the `CONN` matrix or miscounted).
  2. The $p$-values in `Tables 3, 4, and 5` are **uncorrected one-tailed $p$-values** (for example, at $df = 97$, $\Pr(T > 3.35) = 0.000575$, matching `0.00058` in `Table 4`, whereas the two-tailed $p$-value is $0.00115$ and the Benjamini–Hochberg FDR-adjusted $q$-value across 561 pairs is $q_{\text{FDR}} \approx 0.11 > 0.05$).
* **Actionable Fix:** Report two-tailed uncorrected $p$-values alongside exact Benjamini–Hochberg FDR-adjusted $q$-values across all $\binom{34}{2} = 561$ unique ROI pairs, and clarify whether 32 or 34 ROIs were entered into the connectivity matrix.

### 3. Inconsistent Demographic Percentages in `Table 1` and Uncontrolled Sex Confounding (Pillar 2 & Pillar 7)
* **Defect:** In `Table 1` (lines 33–37), the sample sizes are listed as `ADHD (n = 40)`, `BD (n = 49)`, `SZ (n = 50)`, and `HCs (n = 50)` ($N = 189$). However, the `Gender (%)` rows list:
  * `Male (%)`: `7.7` (ADHD), `10.3` (BD), `14` (SZ), `25` (HCs) $\implies \text{Sum} = 57.0\%$
  * `Female (%)`: `8.1` (ADHD), `7.7` (BD), `4.4` (SZ), `22.8` (HCs) $\implies \text{Sum} = 43.0\%$
  Notice that for ADHD, $7.7\% + 8.1\% = 15.8\%$ of total ($0.158 \times 189 = 29.9 \ne 40$), while for HCs, $25\% + 22.8\% = 47.8\%$ of total ($0.478 \times 189 = 90.3 \ne 50$)! These percentages appear to have been copied from a larger baseline CNP cohort table ($N \approx 272$ where $HCs = 130$) without recalculating for the $N = 189$ subsample analyzed here! Furthermore, the SZ group is $>75\%$ male (`14%` vs. `4.4%`), yet sex (and age and mean framewise displacement) was not included as a covariate in the `CONN` group comparisons.
* **Actionable Fix:** Recalculate `Table 1` gender counts and within-group percentages for the exact $N = 189$ analyzed participants, and include age, sex, and mean framewise displacement (FD) as covariates in the group-level GLMs.

### 4. Tiny Subcortical Nuclei (`STN`, `SN`, `Claustrum`) Sampled at $4\text{ mm}$ Slice Thickness with Spherical Coordinates (Pillar 6)
* **Defect:** The fMRI acquisition has $3 \times 3 \times 4\text{ mm}$ voxels smoothed in MNI space, yet `Table 2` defines point coordinates for the subthalamic nucleus (`12, −18, −7`), substantia nigra (`13, −17, −16`), and claustrum (`33, −19, 10`, which is actually in the posterior insula/putamen border). At $4\text{ mm}$ slice thickness, the subthalamic nucleus and claustrum suffer severe partial-volume contamination from adjacent white matter, globus pallidus, and insula.
* **Actionable Fix:** Specify the exact ROI mask geometry (spherical radius vs. probabilistic subcortical atlas mask) used in `CONN` for `Table 2`, and discuss partial-volume limitations for subthalamic and claustral seeds at $4\text{ mm}$ slice resolution.

---

## 4. Quantitative Rubric Scoring

| Rubric Dimension | Score | Max | Forensic Justification |
| :--- | :---: :---: | :---: | :--- |
| **1. Methodological & Statistical Rigor** | **0.9** | **3.5** | Mathematically impossible $\eta^2$ values (`0.53`, `0.52`, `0.51`, `0.0.19`) in `Tables 3–5`; uncorrected one-tailed $p$-values reported as FDR-corrected; miscounted ROI pairs (`992` vs. `561`); no sex or motion covariates in group $t$-tests despite severe sex imbalance in SZ. |
| **2. Claim-to-Evidence Alignment** | **0.8** | **2.5** | Claims that procedural memory network rs-FC alterations underlie cognitive network impairments in ADHD, BD, and SZ without analyzing any cognitive or procedural memory task data; misclassifies claustrum and caudate as frontal DMN structures. |
| **3. Data Integrity & Biological Plausibility** | **0.9** | **2.0** | Uses a high-quality public cohort (`ds000030`), but attributes $4\text{ mm}$ EPI signals at single coordinates to tiny nuclei (subthalamic nucleus, claustrum) without addressing partial voluming or antipsychotic/stimulant medication confounds. |
| **4. Reproducibility & Data Integrity** | **1.2** | **2.0** | Raw data are publicly available on OpenNeuro (`ds000030`), but `Table 1` gender percentages do not match the $N = 189$ sample sizes, `Tables 3–5` contain corrupted/impossible statistics, and the `Abstract` misidentifies the ROI atlas. |
| **Scientific Core Score** | **2.6** | **8.0** | Sum of Rigor + Claims + Biology (`0.9 + 0.8 + 0.9`). |
| **Overall Composite Score** | **3.8** | **10.0** | **Flawed / Overstated** (`0.9 + 0.8 + 0.9 + 1.2`). |
