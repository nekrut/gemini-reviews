# Review of OOD_ANON_28

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **4.6 / 10.0** (Flawed / Overstated)  
* **Score Breakdown:** Rigor: 1.2/3.5 | Claims: 1.0/2.5 | Biology: 1.3/2.0 | Reproducibility: 1.1/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This study investigates changes in glymphatic system proxies—specifically the diffusion tensor imaging along the perivascular space (DTI-ALPS) index and dilated perivascular space (pPVS) volume—alongside seed-based resting-state functional connectivity (FC) across four brain networks and cognitive performance (MCCB battery) in unmedicated Major Depressive Disorder (MDD) patients treated with open-label vortioxetine ($20\text{ mg/day}$ for 8 weeks; $n = 34$ clinical/cognitive, $n = 25$ MRI completers) compared against 41 healthy controls (HCs). The authors report reduced baseline DTI-ALPS and elevated left posterior cingulate cortex (PCC)–precuneus FC in MDD compared to HCs, followed after 8 weeks of vortioxetine by increased DTI-ALPS, reduced right PCC–precuneus FC, improved mood and cognitive scores, and positive correlations ($r = 0.40–0.52$) between $\Delta\text{DTI-ALPS}$ and $\Delta\text{global cognition}$.

While longitudinal multimodal imaging of antidepressant treatment is clinically relevant, the manuscript's causal claims and statistical reporting suffer from major design flaws and direct text-table contradictions: (1) **Healthy controls were never rescanned or retested at 8 weeks**, despite explicit claims in the Abstract (line 10: *"All participants underwent mood and cognitive assessment, and diffusion tensor imaging (DTI) and resting-state functional MRI scans at baseline and 8-week follow-up"*) and Results (line 100: *"41 HCs completed baseline and follow-up assessment"*). Inspection of Table 1 and Table 3 reveals that every single "Posttreatment" / "8-week follow-up" mean and SD for HCs is identical to their Baseline value to the second decimal place; (2) without a placebo control group or retested HCs, 8-week gains on the MCCB cognitive battery cannot be separated from test-retest practice effects; (3) the Abstract (line 12) and Results text (line 157) claim significant improvements in visual learning ($p = 0.049$) and social cognition, whereas Table 2 shows neither is statistically significant (`Visual learning`: $p = 0.051$; `Social cognition`: $42.03 \to 42.61, p = 0.788$), and none of the individual cognitive subscales survive the FDR correction promised in Methods Section 2.9; (4) the DMN connectivity analysis switches seeds mid-analysis—reporting baseline hyperconnectivity from the **left PCC** seed, but post-treatment decreases from the **right PCC** seed (which actually drops significantly *below* HCs at 8 weeks rather than normalizing); and (5) the headline correlations between $\Delta\text{DTI-ALPS}$, $\Delta\text{FC}$, and $\Delta\text{cognition}$ did not survive multiple-testing correction, as acknowledged only in the final sentence of the Discussion. Correcting the misrepresentation of HC follow-up data, applying consistent FDR thresholds, and reframing the single-arm findings as preliminary observational associations are essential.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Unmedicated patients with acute MDD exhibit reduced baseline DTI-ALPS indexes compared to healthy controls, without structural enlargement of white-matter or subcortical PVS volume: [Moderately Supported].**  
  The baseline cross-sectional comparison ($n = 25$ MDD vs. $n = 41$ HCs; Table 3) shows a lower mean DTI-ALPS index in MDD ($1.66 \pm 0.09$ vs. $1.76 \pm 0.18$, $p = 0.003$, $\text{FDR-}p = 0.033$), with good inter-observer reliability ($\text{ICC} = 0.83–0.88$) and robustness to corpus callosum $D_{xx}$ adjustment (Table S5). However, DTI-ALPS reflects local water diffusivity ratios ($D_{xx}/D_{yy}$ and $D_{xx}/D_{zz}$) in periventricular association and projection fibers rather than a direct measurement of whole-brain glymphatic clearance.

* **Eight-week vortioxetine treatment restores glymphatic function (DTI-ALPS) and improves attention/vigilance, verbal learning, visual learning, social cognition, and global cognition in MDD: [Overstated].**  
  First, because the study is an open-label single-arm design without a placebo MDD arm and because HCs were only assessed once at baseline (their baseline values were simply copied into the "Posttreatment" rows of Table 1 and Table 3), cognitive score increases over 8 weeks are confounded by standard MCCB test-retest practice effects. Second, the Abstract (line 12) claims vortioxetine improved "social cognition" and "visual learning," and Section 3.2 (line 157) reports $p = 0.049$ for visual learning—both directly contradicted by Table 2, where social cognition is completely unchanged ($42.03 \to 42.61$, $p = 0.788$) and visual learning has $p = 0.051$. Third, although Methods Section 2.9 states that FDR correction was applied to paired $t$-tests of cognitive functions, Table 2 reports raw uncorrected $p$-values ($0.022, 0.040, 0.051, 0.012$ across 8 MCCB measures); under Benjamini-Hochberg FDR across the 7 cognitive domains, none reach $\text{FDR-}p < 0.05$.

* **Vortioxetine normalizes elevated DMN functional connectivity between the PCC and precuneus in MDD: [Fragile].**  
  The baseline group comparison (Figure 2A) found elevated FC between the **left PCC** seed and bilateral precuneus in MDD vs. HCs, with no significant baseline difference for the right PCC seed. However, the longitudinal pre- vs. post-treatment comparison (Figure 2B) and the post-treatment MDD vs. HC comparison (Figure 2C) report changes only for the **right PCC** seed—and at post-treatment, right PCC–precuneus FC in MDD is significantly *lower* than in HCs (Figure 2C, line 314), indicating an overshoot on the contralateral seed rather than normalization of the baseline left PCC abnormality.

* **Restoration of glymphatic function ($\Delta\text{DTI-ALPS}$) drives the improvements in global cognition and DMN connectivity: [Overstated].**  
  As the authors acknowledge at the end of the Discussion (line 340), the exploratory correlations in $n = 25$ patients ($r = 0.404, p = 0.045$; $r = 0.484, p = 0.014$; $r = 0.520, p = 0.008$; $r = -0.429, p = 0.033$) did not survive multiple-comparison correction across the tested mood, cognitive, DTI, and FC variables. Furthermore, Figure 3A–C tests three collinear versions of the exact same variable (Left, Right, and Mean DTI-ALPS) against the MCCB composite score, and the sample size ($n = 25$ after excluding 9 of 34 MDD patients for MRI dropout/motion) is small.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Correct the False Statement That Healthy Controls Completed 8-Week Follow-Up MRI and Cognitive Testing
* **WHY:** Abstract line 10 and Results line 100 explicitly state that all 41 HCs underwent both baseline and 8-week follow-up mood, cognitive, and MRI assessments. However, Tables 1 and 3 show identical numbers for HCs at baseline and follow-up across all 22 variables, proving that HCs were assessed only at baseline and their baseline data were reused in the follow-up comparison.
* **WHAT:** Revise the Abstract (line 10), Methods Section 2.2 (line 42), and Results Section 3.1 (line 100) to state transparently that HCs were assessed only once at baseline, and label the post-treatment vs. HC comparisons in Tables 1 and 3 as "Posttreatment MDD vs. Baseline HCs."
* **HOW:** Remove the duplicate "Posttreatment" HC rows in Table 1 and "8-week follow-up" HC column in Table 3 (Instead, add a column in Table 1 and Table 3 for `Posttreatment MDD vs. Baseline HCs p-value`), and explicitly discuss MCCB practice/retest effects as a key limitation when interpreting cognitive changes in the unblinded MDD cohort.

#### 2. Reconcile Text-Table Discrepancies for Visual Learning and Social Cognition and Report FDR-Adjusted $p$-Values in Tables 1 and 2
* **WHY:** Claiming in the Abstract (line 12) that vortioxetine improved social cognition when $p = 0.788$ in Table 2, and reporting $p = 0.049$ in the text (line 157) when Table 2 prints $p = 0.051$ for visual learning, directly misrepresents the statistical results. Moreover, Methods line 85 states FDR correction was applied to cognitive comparisons, but FDR-adjusted $p$-values are missing from Tables 1 and 2.
* **WHAT & HOW:**
  1. Remove "social cognition" and "visual learning" from the list of significantly improved cognitive domains in the Abstract (line 12), Results (line 157), and Discussion (line 338).
  2. Add an `FDR-p` column to Table 1 and Table 2 (matching the format of Tables 3 and 4) computed via `p.adjust(p, method = "BH")` across the MCCB domains, and clarify which cognitive improvements survive FDR correction.
  3. In Table 1, verify why the MDD sample size for MCCB is $n = 34$ (`df` not shown, but means such as `46.88`, `46.64`, `48.33`, `48.00` are exact multiples of $1/33 = 0.030303...$, indicating $n = 33$, not $n = 34$!). State the exact number of MDD participants with complete MCCB data.

#### 3. Report Both Left and Right PCC Seed Trajectories Symmetrically
* **WHY:** Finding baseline hyperconnectivity in the **left PCC** seed (Figure 2A) but reporting post-treatment reductions only in the **right PCC** seed (Figures 2B–C) leaves unanswered what happened to the left PCC cluster after treatment and why right PCC dropped below baseline HC levels.
* **WHAT:** Extract the mean Fisher-$z$ FC values from the baseline left PCC–precuneus cluster at both baseline and 8-week follow-up in MDD (and from the right PCC–precuneus cluster at baseline in MDD vs. HCs) and report both trajectories in a supplementary table or figure.
* **HOW:** Using the cluster masks from Figure 2A and 2B, compute ROI-averaged $z$-scores for all 25 MDD patients (pre and post) and 41 HCs, run paired and two-sample $t$-tests on both seeds, and clarify in the Discussion that right PCC–precuneus FC decreased below HC baseline levels rather than simply normalizing.

#### 4. Temper Causal Language Around Uncorrected Exploratory Correlations
* **WHY:** In an unblinded single-arm cohort of $n = 25$ patients, uncorrected correlations ($p = 0.008–0.045$) that fail FDR correction cannot establish that glymphatic changes causally drive DMN or cognitive recovery.
* **WHAT:** Temper the Abstract Conclusion (line 14) and Discussion Summary (lines 332, 345) to frame the correlation between $\Delta\text{DTI-ALPS}$, $\Delta\text{DMN FC}$, and $\Delta\text{MCCB}$ as an exploratory, hypothesis-generating association that requires replication in a placebo-controlled trial.
* **HOW:** Also report partial correlations controlling for $\Delta\text{HDRS-24}$ (change in depression severity) to test whether the correlation between $\Delta\text{DTI-ALPS}$ and $\Delta\text{global cognition}$ is independent of symptom remission, which is a central hypothesis raised in the Introduction (line 23).
