# Forensic Peer Review: FEXP_ANON_121

**Overall Score:** **3.7 / 10.0** (Flawed / Overstated) | **Scientific Core Score:** **2.7 / 8.0**  
* **Score Breakdown:** Rigor: 0.9/3.5 | Claims: 0.9/2.5 | Biology: 0.9/2.0 | Reproducibility: 1.0/2.0

---

## 1. Blinded Metadata Perception

* **Manuscript ID:** `FEXP_ANON_121`
* **Perceived Domain & Topic:** Clinical Neuroimaging / Neuroendocrinology / Cognitive Neuroscience; hippocampal subregion resting-state functional connectivity (RSFC) and peripheral serum cytokines in Type 2 diabetes mellitus-associated cognitive decline (T2DACD).
* **Perceived Empirical Scope:** $N = 57$ human participants ($n = 16$ T2DM without cognitive decline, $n = 16$ T2DACD defined by $\text{MoCA} < 26$, and $n = 25$ healthy controls [HCs]); ELISA serum cytokines (IL-6, IL-10, TNF-$\alpha$) measured on a subset of $n = 28$ participants ($10$ HC, $8$ T2DM, $10$ T2DACD); cognitive battery (MoCA, Flanker, Stroop, 1-back, 2-back); 3T resting-state fMRI analyzed in FSL/SPM12 using 6 hippocampal subregion seeds, MetaboAnalyst OPLS-DA, and GraphPad Prism ROC curves.

---

## 2. Executive Summary & Editorial Verdict

This cross-sectional clinical study compares 16 patients with T2DM, 16 patients with T2DM-associated cognitive decline (`T2DACD`, defined by $\text{MoCA} < 26$), and 25 healthy controls across cognitive tasks (Flanker, Stroop, N-back), peripheral serum cytokines (IL-6, IL-10, TNF-$\alpha$), and seed-based resting-state fMRI functional connectivity (RSFC) of six hippocampal subregions (bilateral anterior, middle, posterior). The authors report elevated serum IL-6 in both T2DM and T2DACD ($p < 0.001$), altered hippocampal RSFC with default mode network (precuneus, angular gyrus, medial frontal gyrus, middle temporal gyrus) and sensorimotor regions (precentral gyrus), a positive partial correlation between left posterior hippocampus–left precuneus RSFC and Flanker conflict reaction time in T2DACD ($r = 0.766, p = 0.002$), and high diagnostic classification accuracy in ROC analysis ($\text{AUC} = 0.870\text{–}0.918, p < 0.0001$).

**Editorial Verdict: Reject / Severe Circular Analysis (Double-Dipping) and Statistical/Biochemical Artifacts (3.7 / 10.0).** While investigating hippocampal long-axis specialization in diabetic cognitive impairment is clinically motivated, the study's main conclusions rest on textbook circular statistics, unacknowledged glycemic confounding, and implausible ELISA data:
1. **Textbook double-dipping (circularity) in the neuroimaging ROC analysis and cognitive OPLS-DA:** In the fMRI analysis, the authors performed whole-brain voxelwise searches across 6 hippocampal seeds and 3 pairwise group contrasts, extracted the mean zFC values from the peak significant clusters (`Table 5`) on the *same* $n = 16$ vs. $16$ (or $25$) subjects, and fed those exact values into an in-sample ROC analysis (`Table 6`, `Figure 6`), claiming $\text{AUC} = 0.870\text{–}0.918$ ($p < 0.0001$). Selecting features via whole-brain $t$-tests and evaluating ROC AUC on the discovery sample without independent validation is circular (Kriegeskorte et al. 2009). Similarly, `T2DACD` vs. `T2DM` was defined by thresholding $\text{MoCA} < 26$ (line 32), and the authors then included MoCA in a supervised OPLS-DA model (`Figure 2`, $R^2Y = 0.968, Q^2 = 0.901$) to claim that cognitive indicators separate the groups.
2. **Mathematically inconsistent and biochemically implausible ELISA values in Table 2:** Table 2 (conducted on an unexplained subset of only $n = 10, 8, 10$ subjects) reports IL-6 concentrations of $0.160 \pm 0.047\text{ pg/mL}$ (HCs), $0.166 \pm 0.003\text{ pg/mL}$ (T2DM), and $0.168 \pm 0.003\text{ pg/mL}$ (T2DACD) with ANOVA $p < 0.001$. For those numbers as printed, the exact one-way ANOVA is $F_{2,25} = 0.214, p = 0.809$ (not $< 0.001$, indicating a decimal-point error in $\pm 0.047 \to \pm 0.0047$). More fundamentally, nearly invariant values of $0.160\text{–}0.168$, $0.087 \pm 0.001$, and $0.237 \pm 0.003$ with ~1% inter-individual coefficient of variation resemble raw microplate optical density (OD) background absorbance values rather than calibrated human serum cytokine concentrations in $\text{pg/mL}$.
3. **Uncontrolled glycemic confounding (`HbA1c`, $p = 0.008$) and whole-brain multiple-testing inflation:** Table 1 shows that `HbA1c` is significantly higher in `T2DACD` ($7.68 \pm 1.84\%$) than in `T2DM` ($6.68 \pm 0.58\%, p = 0.008$), yet this difference is omitted from the Results narrative and never controlled for in the `T2DACD vs. T2DM` RSFC comparison.

### Assessment of Specific Claims

* **Claim 1 (T2DACD patients exhibit slower reaction times on Flanker conflict, Stroop neutrality/conflict, and 1-back tasks compared to T2DM and HCs): `[Moderately Supported]`.**  
  Unlike MoCA (which was used to define the groups), the computerized executive/working-memory reaction-time deficits in Table 3 provide independent behavioral evidence of slower conflict resolution in the $\text{MoCA} < 26$ group, although OPLS-DA separation in Figure 2 is circular due to the inclusion of MoCA.
* **Claim 2 (Peripheral serum IL-6 is significantly elevated in T2DM and T2DACD compared to HCs, whereas IL-10 and TNF-$\alpha$ are unchanged): `[Methodologically Flawed]`.**  
  First, 29 of the 57 participants are missing from Table 2 without explanation. Second, the reported means and SDs in Table 2 ($0.160 \pm 0.047$ vs. $0.166 \pm 0.003$ vs. $0.168 \pm 0.003$) yield $F_{2,25} = 0.214, p = 0.809$, contradicting the reported $p < 0.001$. Third, a $0.006\text{ pg/mL}$ shift at $0.16\text{ pg/mL}$ with $\text{SD} = 0.003$ (~1.8% CV) is consistent with uncalibrated plate-reader optical density noise at the assay blank floor rather than biological cytokine variation.
* **Claim 3 (T2DACD and T2DM show distinct hippocampal subregion RSFC alterations with the left precuneus, angular gyrus, precentral gyrus, medial frontal gyrus, and posterior middle temporal gyrus): `[Fragile]`.**  
  Five of the seven region-to-region differences reported in the pairwise $t$-tests (Table 5)—including `Left pHPC – Left precuneus` (`T2DACD > T2DM`) and `Left aHPC – Left precentral gyrus` (`T2DACD > HCs`)—were **not significant in the 3-group omnibus ANOVA (Table 4)**, indicating that unconstrained whole-brain pairwise $t$-tests were run across 6 seeds $\times$ 3 contrasts (18 whole-brain maps) without family-wise error correction across seeds or contrasts, and without controlling for the significant difference in `HbA1c` ($p = 0.008$) between `T2DACD` and `T2DM`.
* **Claim 4 (Altered hippocampal subregion RSFC values achieve high diagnostic accuracy [$\text{AUC} = 0.870\text{–}0.918, p < 0.0001$] for distinguishing T2DACD from HCs and T2DM): `[Methodologically Flawed]`.**  
  The ROC curves in Table 6 and Figure 6 were computed on the exact same small sample ($n = 16$ vs. $16$ or $25$) used to select the peak clusters out of whole-brain voxelwise $t$-maps, resulting in severe selection-bias circularity.

---

## 3. Forensic Defect Inventory

### Defect 1: Double-Dipping (Circular Feature Selection) in Neuroimaging ROC Analysis and Cognitive OPLS-DA [ Pillar 1, Pillar 2, Pillar 4 — Critical ]
* **Location:** Section "Participants" (line 32), Section "Receiver operating characteristic analysis" (line 80), Results (lines 88, 193–205), Figure 2, Figure 6, and Table 6.
* **Forensic Evidence:**
  1. **Neuroimaging ROC circularity:** In Table 5, whole-brain voxelwise $t$-tests ($n = 16$ T2DACD vs. $n = 25$ HCs; $n = 16$ T2DACD vs. $n = 16$ T2DM) identified peak clusters at $T = 4.92$, $T = -4.67$, and $T = 4.24$. The authors then extracted the mean zFC values of those exact peak clusters from the same subjects and evaluated in-sample ROC curves (Table 6: $\text{AUC} = 0.870, 0.880, 0.918$, all $p < 0.0001$). Because the clusters were selected specifically for having maximal $T$-statistics between those groups in that sample, in-sample ROC AUCs and $p$-values are guaranteed to be artificially high and cannot be interpreted as diagnostic performance.
  2. **OPLS-DA group-definition circularity:** In Section "Participants" (line 32), `T2DACD` was defined by $\text{MoCA} < 26$. In Results (line 88, Figure 2), the authors fitted supervised PLS-DA and OPLS-DA models on *"all cognitive assessment indicators"* (which includes MoCA) to classify `T2DACD vs. T2DM` ($R^2Y = 0.968, Q^2 = 0.901$) and `T2DACD vs. HCs` ($R^2Y = 0.985, Q^2 = 0.937$). Including the group-defining threshold variable (`MoCA`) inside a supervised multivariate classifier makes the separation tautological.
* **Fix:** Remove the circular in-sample ROC analysis (or re-evaluate classification using nested leave-one-out / $k$-fold cross-validation where whole-brain cluster selection is performed strictly inside each training fold), and exclude `MoCA` from the cognitive PLS-DA/OPLS-DA models in Figure 2.

### Defect 2: Arithmetic Contradiction and Biochemical Implausibility in Serum Cytokine Data (Table 2) [ Pillar 3, Pillar 4, Pillar 6 — Critical ]
* **Location:** Section "Glycolipid metabolism indicators and inflammation factors measures" (line 39), Results (line 88), and Table 2 (lines 108–114).
* **Forensic Evidence:**
  1. **Unexplained missing data ($N = 28$ vs. $N = 57$):** Table 1 and Table 3 include $n = 25$ HCs, $n = 16$ T2DM, and $n = 16$ T2DACD ($N = 57$), whereas Table 2 includes only $n = 10$ HCs, $n = 8$ T2DM, and $n = 10$ T2DACD ($N = 28$), with no explanation in the Methods or Results for why 51% of the cohort lacks blood cytokine data.
  2. **ANOVA mathematical impossibility as printed:** For `IL-6` in Table 2 ($0.160 \pm 0.047$, $0.166 \pm 0.003$, $0.168 \pm 0.003$), the between-group mean square is $\text{MS}_{\text{between}} = 0.0001714$ and the within-group mean square is $\text{MS}_{\text{within}} = 0.000801$, yielding $F_{2,25} = 0.214$ ($p = 0.809$), contradicting the reported $p < 0.001$ (which would only arise if the HC standard deviation were $0.0047$ instead of $0.047$).
  3. **Biochemical implausibility of values and variances:** Across all three groups in Table 2, `IL-6` is $0.160\text{–}0.168$, `IL-10` is $0.087 \pm 0.001$ to $0.087 \pm 0.003$, and `TNF-α` is $0.237 \pm 0.003$ to $0.238 \pm 0.009$. Human serum cytokines measured by ELISA do not exhibit $1\%$ biological coefficients of variation ($\text{SD} = 0.001\text{ pg/mL}$) across unrelated adults; these numbers match raw, unconverted microplate absorbance (optical density, OD450) readings near the blank floor rather than standard-curve-interpolated concentrations in $\text{pg/mL}$.
* **Fix:** Audit the raw ELISA standard curves and optical density spreadsheets, clarify why 29 subjects were omitted from Table 2, convert raw OD readings properly using the standard curve (or report if samples fell below the lower limit of detection), and correct the SD/ANOVA values in Table 2.

### Defect 3: Unconstrained Pairwise Whole-Brain Testing Outside the Omnibus ANOVA Mask and Uncontrolled `HbA1c` Confounding [ Pillar 3, Pillar 4, Pillar 5 — Major ]
* **Location:** Section "Functional connectivity analysis" (line 70), Table 1 (line 102), Table 4 (lines 160–167), and Table 5 (lines 169–181).
* **Forensic Evidence:**
  1. **Pairwise clusters outside the 3-group omnibus ANOVA:** Table 4 reports the significant clusters from the 3-group ANOVA (`Left aHPC` with bilateral angular gyrus; `Right mHPC` and `Right aHPC` with left precuneus). However, Table 5 ("post hoc test") reports pairwise clusters for `Left aHPC – Left precentral gyrus`, `Left mHPC – Right medial frontal gyrus`, `Left aHPC – Right precuneus`, `Left aHPC – Right posterior middle temporal gyrus`, and `Left pHPC – Left precuneus`—none of which were significant in the 3-group ANOVA in Table 4. Performing 18 separate unconstrained whole-brain searches (6 seeds $\times$ 3 pairwise contrasts) at primary threshold $p < 0.001$ without Bonferroni/Šidák adjustment across the 6 seeds and 3 contrasts inflates the family-wise false positive rate.
  2. **Unacknowledged `HbA1c` difference between `T2DACD` and `T2DM`:** Table 1 (line 102) shows that `HbA1c` is significantly higher in `T2DACD` ($7.68 \pm 1.84\%$) than in `T2DM` ($6.68 \pm 0.58\%$, $p = 0.008$). However, Results line 88 omits this significant difference, and the `T2DACD vs. T2DM` neuroimaging comparison (line 70) only covaries for age and gender, leaving acute/chronic glycemic severity (`HbA1c`) and insulin usage imbalance (10/16 on insulin/multi-drug therapy in T2DACD vs. 4/16 in T2DM; line 32) unadjusted.
* **Fix:** Restrict post-hoc pairwise comparisons strictly to clusters surviving the 3-group omnibus ANOVA (Table 4) or apply a Bonferroni-adjusted cluster FWE threshold ($\alpha = 0.05 / 18 = 0.0028$) across the 6 seeds and 3 contrasts, and include `HbA1c` and education as covariates in the group RSFC models.

### Defect 4: Text–Table Inconsistencies and Missing Gender Test Statistic [ Pillar 7 — Minor ]
* **Location:** Abstract (line 9) vs. Results (line 185), and Table 1 (line 96).
* **Forensic Evidence:**
  1. The partial correlation $p$-value between `Left pHPC – Left precuneus` RSFC and Flanker conflict RT in T2DACD is reported as $P = 0.001$ in the Abstract (line 9) but as $p = 0.002$ in Results (line 185; exact two-tailed $p = 0.0023$ for $r = 0.766, n = 16, 3\text{ covariates}, \text{df} = 11$).
  2. In Table 1 (line 96), `Gender (male/female)*` ($7/18$ in HCs, $5/11$ in T2DM, $9/7$ in T2DACD) has `—` in the $p$-value column and an unexplained asterisk `*` with no footnote (exact $\chi^2 = 3.59, p = 0.166$).
  3. In the Introduction (line 24) and Discussion (line 216), `T2DACD` is inconsistently abbreviated as `T2ACD`, `T2DCD`, and `T2DCAD`.

---

## 4. Quantitative Rubric Scoring

| Rubric Dimension | Score | Max | Diagnostic Justification |
| :--- | :---: :---: | :---: | :--- |
| **1. Methodological & Statistical Rigor** | **0.9** | **3.5** | Circular in-sample ROC analysis on whole-brain-selected peak clusters; circular OPLS-DA including the group-defining MoCA score; mathematically impossible ANOVA $p < 0.001$ on Table 2 IL-6 numbers as printed; unconstrained whole-brain pairwise $t$-tests outside the omnibus ANOVA mask. |
| **2. Claim-to-Evidence Alignment** | **0.9** | **2.5** | Claims of diagnostic biomarker performance ($\text{AUC} = 0.918$) and elevated serum IL-6 are artifacts of circular feature selection and uncalibrated/erroneous ELISA reporting; fails to acknowledge or adjust for significantly higher `HbA1c` ($p=0.008$) in T2DACD vs. T2DM. |
| **3. Data Integrity & Biological Plausibility** | **0.9** | **2.0** | Serum cytokine values in Table 2 ($0.087 \pm 0.001$, $0.166 \pm 0.003$, $0.237 \pm 0.003\text{ pg/mL}$ on an unexplained subset of $28/57$ subjects) are biochemically implausible as calibrated $\text{pg/mL}$ concentrations and resemble raw plate-reader optical density readings. |
| **4. Reproducibility & Data Integrity** | **1.0** | **2.0** | Standard MRI acquisition parameters and MNI coordinates are tabulated, but raw data/code are not deposited, 29 subjects are missing from Table 2 without explanation, and Table 2 SDs contradict the reported $F$-test $p$-value. |
| **Total Composite Score** | **3.7** | **10.0** | **Flawed / Overstated** (Scientific Core Score: **2.7 / 8.0**) |
