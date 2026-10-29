# Review of FEXP_ANON_138

**Overall Score:** **6.0 / 10.0** (Mixed / Salvageable)
* **Score Breakdown:** Rigor: 1.8/3.5 | Claims: 1.5/2.5 | Biology: 1.4/2.0 | Reproducibility: 1.3/2.0
* **Scientific Core Score:** **4.7 / 8.0**

---

## 1. Blinded Metadata Perception

* **Manuscript ID:** `FEXP_ANON_138`
* **Perceived Study Type:** Cross-sectional clinical resting-state fMRI study ($N = 195$ analyzed: $n = 78$ MDD with suicidal ideation [MDD-SI], $n = 44$ MDD without suicidal ideation [MDD-NSI], and $n = 73$ healthy controls [HCs]), with external validation of ALFF in the multi-site REST-meta-MDD consortium dataset ($N = 1,596$: 396 MDD-SI, 142 MDD-NSI, 1,058 HCs).
* **Domain & Focus:** Psychiatric neuroimaging of suicidality in Major Depressive Disorder (amplitude of low-frequency fluctuations [ALFF], seed-based functional connectivity [FC], and voxel-wise Granger Causality effective connectivity [EC] of the right anterior cingulate cortex [ACC]).

---

## 2. Executive Summary & Editorial Verdict

This study compares resting-state fMRI ALFF, seed-based FC, and bivariate autoregressive Granger Causality effective connectivity (EC) across patients with MDD with suicidal ideation (MDD-SI), MDD without suicidal ideation (MDD-NSI), and healthy controls (HCs), and validates the primary right anterior cingulate cortex (ACC) ALFF elevation using the large multi-center REST-meta-MDD consortium cohort ($N = 1,596$).

**Editorial Verdict:** **Major Revision Required.** The inclusion of a depressed non-suicidal comparator group (`MDD-NSI`, $n = 44$) matched to `MDD-SI` ($n = 78$) on non-suicidal depression severity (`HAMD-except suicidality`: $20.29 \pm 4.22$ vs. $20.20 \pm 3.75, p = 0.906$) and the external replication of the right ACC ALFF finding in REST-meta-MDD ($N = 1,596$) are notable methodological strengths. However, a forensic audit reveals three critical defects:
1. **Incompatible Operational Definitions of Suicidal Ideation (`BSI-CV` vs. `HAMD Item 3`) and Non-Zero Suicidality in the `MDD-NSI` Group:** In the primary cohort, `MDD-SI` vs. `MDD-NSI` was defined using items 4 and 5 of the Beck Scale for Suicide Ideation (`BSI-CV`). Yet in `Table 1`, the `MDD-NSI` ("without suicidal ideation") group has a mean `HAMD-suicidality` (Item 3) score of **$1.00 \pm 1.01$**! Conversely, in the REST-meta-MDD validation cohort, `MDD-NSI` was defined as `HAMD Item 3 = 0` and `MDD-SI` as `HAMD Item 3 > 0`. Critically, the authors disclose in the `Limitations` (line 223) that when they applied the `HAMD Item 3` grouping criterion to their own primary cohort, **it failed to replicate the main FC and EC findings (`Supplementary Table S6`)**!
2. **Group-Driven Pseudocorrelations with `HAMD-Suicidality` Instead of `BSI-CV`:** Although `BSI-CV` was collected specifically to quantify suicidal ideation severity ($34.37 \pm 5.93$ in `MDD-SI`), the authors did not report correlations with `BSI-CV`; instead, they correlated FC and EC values (extracted from clusters already selected for differing between `MDD-SI` and `MDD-NSI`) against `HAMD-suicidality` (a 0–4 ordinal item that also differs strongly between `MDD-SI` and `MDD-NSI`, $t = 8.18, p < 0.001$) across *all* MDD patients pooled together ($n = 122$), inducing a group-driven correlation ($r = -0.26$ and $r = -0.28$).
3. **Sample Size Swap Between `Abstract` and `Table 1`, Plus Fragile 5-Voxel EC Clusters:** The `Abstract` reports `73 MDD-SI` and `78 HCs`, whereas `Table 1` reports `78 MDD-SI` and `73 HCs`. Moreover, the voxel-wise Granger Causality (EC) clusters (`right fusiform gyrus`, $k = 5$ voxels; `left VPM thalamus`, $k = 6$ voxels; `right MFG`, $k = 7$ voxels; `right cerebellar tonsil`, $k = 8$ voxels) rely on an arbitrary cluster-extent cutoff of $k > 5$ voxels inside an ANCOVA mask and are vulnerable to regional hemodynamic lag differences.

### Assessment of Specific Conclusions & Support

* **MDD-SI patients exhibit increased ALFF in the right ventral/subgenual ACC (`9, 21, −12`) compared to MDD-NSI and HCs: [Well Supported].**  
  The right ACC ALFF increase ($k = 36, F = 12.09, t = 3.71, p_{\text{FDR}} = 0.024$) survived 3-group ANCOVA and post-hoc FDR correction in the primary cohort (where `MDD-SI` and `MDD-NSI` had identical non-suicidal HAMD and HAMA scores), held across both `BSI-CV` and `HAMD Item 3` grouping definitions (`Supplementary Table S6`), and replicated externally in the REST-meta-MDD consortium dataset ($N = 1,596; t = 2.77, p_{\text{Bonf}} = 0.017$).

* **MDD-SI patients exhibit reduced FC between right ACC and left IFG and altered Granger Causality (EC) with right fusiform gyrus, right cerebellar tonsil, and left IPL: [Fragile].**  
  First, the authors admit (`Limitations`, line 223) that these FC and EC group differences **disappeared** when patients in the primary cohort were classified using `HAMD Item 3` (the criterion used for REST-meta-MDD validation) instead of `BSI-CV`. Second, the target clusters are extremely small ($k = 5$ to $8$ voxels for left IFG, right fusiform gyrus, and right cerebellar tonsil), and time-domain Granger Causality onresting-state BOLD fMRI is confounded by variable neurovascular delays between limbic ACC, cerebellum, and ventral occipitotemporal cortex.

* **Right ACC–left IFG FC and right ACC–right fusiform EC negatively correlate with suicidal ideation severity: [Methodologically Flawed].**  
  Connectivity values were extracted from clusters pre-selected for significant `MDD-SI < MDD-NSI` differences ($t = -4.42$ and $t = -3.85$) and then correlated across the pooled `MDD-SI + MDD-NSI` sample against the 5-level ordinal `HAMD-suicidality` item (which was $2.50 \pm 0.95$ in `MDD-SI` vs. $1.00 \pm 1.01$ in `MDD-NSI`, $t = 8.18$). Pooling two groups that differ on both $X$ and $Y$ guarantees a negative correlation ($r = -0.26$ and $r = -0.28$) even if there is zero within-group association with suicidal ideation severity (`BSI-CV`).

* **Progressive EC increase across the continuum `HC < MDD-NSI < MDD-SI without SB < MDD-SI with SB`: [Overstated].**  
  While the `Results` text properly notes that this 4-group ordering was an untested exploratory visual trend due to the tiny sample size of the `HAMD Item 3 = 4` (`MDD-SI with SB`) subgroup, the `Abstract` presents this "progressive increase pattern" as a headline finding without disclosing that no statistical test was performed.

---

## 3. Forensic Defect Inventory

### 1. Contradictory Sample Sizes Across `Abstract`, `Methods`, and `Table 1`, and Identical Post-Hoc $t$-Values in Text vs. `Table 2` (Pillar 7)
* **Defect:**
  1. **Swapped Group Sample Sizes:** The `Abstract` (line 7) states: *"We included **73** MDD patients with SI (MDD-SI), 44 MDD patients without SI (MDD-NSI) and **78** healthy controls (HCs)"*. However, `Table 1` (line 81/86) reports **`MDD-SI (n = 78)`**, **`MDD-NSI (n = 44)`**, and **`HCs (n = 73)`**, while `Methods` (line 34) states that `127 MDD (83 MDD-SI, 44 MDD-NSI)` and `88 HCs` were initially enrolled (without explaining in the main text that 5 MDD-SI and 15 HCs were excluded during quality control).
  2. **Mismatched $t$-Statistic in Text vs. `Table 2`:** In Section `EC from the right ACC to the whole brain` (line 168), the text reports: *"MDD-SI exhibited increased EC from the right ACC to the right cerebellar tonsil (**NSI: t = 3.38; HCs: t = 3.38**)."* In `Table 2` (line 141–142), the values are `MDD-SI > MDD-NSI: t = 3.38` and **`MDD-SI > HCs: t = 3.75`** (`3.38` was duplicated by mistake in the prose).
  3. **Medication Acronym Error:** In `Correlation analysis` (line 187), `FLU` is expanded in the text as **`fluphenazine (FLU) equivalents`** (an antipsychotic), whereas `Table 1` note (line 81) correctly defines `FLU` as **`Fluoxetine`** (an SSRI antidepressant, alongside `CPZ = Chlorpromazine` for antipsychotics)!
* **Actionable Fix:** Correct the `Abstract` sample sizes to match `Table 1` (`78 MDD-SI, 44 MDD-NSI, 73 HCs`), state the QC exclusion numbers ($83 \to 78$ MDD-SI; $88 \to 73$ HCs) in the main `Participants` section, fix `HCs: t = 3.38` to `t = 3.75` in line 168, and change "fluphenazine (FLU)" to "fluoxetine (FLU)" in line 187.

### 2. Discordant Suicidal Ideation Definitions (`BSI-CV` vs. `HAMD Item 3`) and Pooled Group-Driven Correlations (Pillar 2, Pillar 3 & Pillar 4)
* **Defect:**
  1. In `Table 1`, the `MDD-NSI` group (defined via `BSI-CV` items 4 and 5 $\le 1$) has a `HAMD-suicidality` (Item 3) score of $1.00 \pm 1.01$, indicating that many patients classified as "non-suicidal ideation" endorsed passive death wishes or suicidal thoughts on the clinician-rated HAMD. Furthermore, when the authors re-classified their own cohort using `HAMD Item 3` (matching their REST-meta-MDD validation definition), the FC and EC group differences failed to replicate (`Limitations`, line 223).
  2. Correlating FC and EC from clusters defined by `MDD-SI vs. MDD-NSI` against `HAMD Item 3` across the combined MDD cohort ($n = 122$) confounds within-group symptom severity with the between-group step difference already used to select the clusters.
* **Actionable Fix:** Report the within-group Spearman correlation between ALFF/FC/EC and continuous `BSI-CV` total scores ($34.37 \pm 5.93$) strictly within the `MDD-SI` group ($n = 78$), and perform a sensitivity analysis restricting `MDD-NSI` to patients who scored $0$ on *both* `BSI-CV` items 4/5 and `HAMD Item 3`.

### 3. Tiny Cluster Extents ($k = 5\text{--}8$ Voxels) and Untested Continuum Claims in the `Abstract` (Pillar 1 & Pillar 4)
* **Defect:** In `Table 2`, several reported clusters consist of only 5 to 8 voxels (`R fusiform gyrus` $k = 5$; `L VLN thalamus` $k = 5$; `L pyramis` $k = 6$; `Vermis` $k = 6$; `L VPM` $k = 6$; `R MFG` $k = 7$; `L IFG` $k = 8$; `R cerebellar tonsil` $k = 8$). Voxel-wise FDR ($p_{\text{FDR}} < 0.05$, $k > 5$) masked inside a 3-group ANCOVA map allows tiny 5-voxel slivers to be reported as regional connectivity hubs. Additionally, the `Abstract` highlights the 4-group progression (`HC < MDD-NSI < MDD-SI without SB < MDD-SI with SB`) without noting that it was an untested visual trend (`Figure 3c`).
* **Actionable Fix:** Apply a formal Jonckheere–Terpstra non-parametric trend test (with exact permutation $p$-values) to evaluate the ordered 4-group hypothesis (`HC < MDD-NSI < MDD-SI without SB < MDD-SI with SB`) or remove the un-tested progression claim from the `Abstract`.

---

## 4. Quantitative Rubric Scoring

| Rubric Dimension | Score | Max | Forensic Justification |
| :--- | :---: :---: | :---: | :--- |
| **1. Methodological & Statistical Rigor** | **1.8** | **3.5** | Strong clinical matching (`MDD-SI` vs. `MDD-NSI` on non-suicidal HAMD/HAMA) and external ALFF validation ($N = 1,596$), but undermined by pooled group-driven correlations on pre-selected clusters, failure of FC/EC to replicate under `HAMD Item 3` grouping, and tiny 5–8 voxel EC clusters. |
| **2. Claim-to-Evidence Alignment** | **1.5** | **2.5** | Candid `Limitations` section disclosing the non-replication of FC/EC under HAMD grouping and the untested nature of the 4-group SB trend, though the `Abstract` omits these caveats. |
| **3. Data Integrity & Biological Plausibility** | **1.4** | **2.0** | Right subgenual/ventral ACC (`9, 21, −12`) hyperactivity in suicidal depression is biologically well-grounded and externally replicated, whereas 5-voxel Granger causality on slow BOLD fMRI is physiologically fragile. |
| **4. Reproducibility & Data Integrity** | **1.3** | **2.0** | Uses public REST-meta-MDD validation data, but swaps `MDD-SI` ($n=78$) and `HC` ($n=73$) sample sizes in the `Abstract`, duplicates $t = 3.38$ in the text, and mislabels `FLU` as "fluphenazine" instead of "fluoxetine" in line 187. |
| **Scientific Core Score** | **4.7** | **8.0** | Sum of Rigor + Claims + Biology (`1.8 + 1.5 + 1.4`). |
| **Overall Composite Score** | **6.0** | **10.0** | **Mixed / Salvageable** (`1.8 + 1.5 + 1.4 + 1.3`). |
