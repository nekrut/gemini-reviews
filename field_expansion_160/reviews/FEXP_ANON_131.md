# Review of FEXP_ANON_131

**Overall Score:** **7.5 / 10.0** (Strong / Sound)
* **Score Breakdown:** Rigor: 2.3/3.5 | Claims: 1.7/2.5 | Biology: 1.7/2.0 | Reproducibility: 1.8/2.0
* **Scientific Core Score:** **5.7 / 8.0**

---

## 1. Blinded Metadata Perception

* **Manuscript ID:** `FEXP_ANON_131`
* **Perceived Study Type:** Double-blind, randomized, placebo-controlled mixed-design pharmaco-fMRI clinical trial (NCT05780216; $N = 40$ enrolled, $n = 39$ analyzed: 19 buccal DMT–harmine [120 mg each], 20 placebo).
* **Domain & Focus:** Systems neuroscience and psychedelic neuroimaging (subacute resting-state functional connectivity [seed-to-voxel, within/between Yeo 6 networks, surface-based global FC across 400 Schaefer parcels, and diffusion-map cortical gradients] 2 days before and 2 days after dosing during a 3-day mindfulness meditation retreat).

---

## 2. Executive Summary & Editorial Verdict

This study investigates the subacute neural effects of a standardized buccal DMT–harmine formulation (120 mg each, administered in four split doses over 90 min on Day 2) versus taste-matched placebo in 39 experienced meditation practitioners participating in a 3-day meditation retreat. Resting-state fMRI scans were acquired 1 day before and 1 day after the retreat (2 days post-dosing) and processed via `fMRIPrep` 23.0.2, `CONN` 22.a, `BrainSpace` 0.1.10, and `BrainStat` 0.4.2, with sensitivity analyses performed both with and without Global Signal Regression (GSR). Raw imaging data are publicly deposited in OpenNeuro (`ds006644`).

**Editorial Verdict:** **Accept with Minor-to-Moderate Revisions.** The preprocessing pipeline, multimodal surface/volumetric analyses, transparent reporting of null results across cortical gradients and FDR-corrected ROI-to-ROI matrices, and open data sharing are commendable. However, three methodological and reporting issues require correction: (1) the Abstract claims that the DMT–harmine group showed increased within-network visual (VIS) connectivity and VIS–attention network connectivity without disclosing that all within- and between-network ROI-to-ROI effects failed FDR correction ($q_{\text{FDR}} < 0.05$) and were only uncorrected trends; (2) the `Statistical analyses` description of the within-group ANCOVAs and the degrees of freedom ($F(1, 74)$) reported in `Figure 3` indicate either an error in how repeated measures were modeled (treating 78 scans from 39 subjects as independent observations in a $2 \times 2$ factorial ANOVA) or a misstatement of the design matrix; and (3) because there was no non-meditation drug arm, the group-by-time interaction contrasts drug vs. placebo *within* a meditation retreat rather than formal pharmacological-by-meditation synergy.

### Assessment of Specific Conclusions & Support

* **No prolonged disruption of cortical gradient hierarchy or 3D gradient dispersion 2 days post-DMT–harmine administration: [Well Supported].**  
  Surface-based linear models (`BrainStat` SLM) across the first three diffusion-map embedding gradients ($\sim 70\%$ variance explained) and 3D within-/between-network dispersion metrics consistently showed no subacute differences between groups or timepoints, with or without GSR, supporting the reversibility of acute psychedelic gradient collapse.

* **Increased seed-to-voxel functional connectivity between the salience network (SAL) and visual cortex (VIS: bilateral calcarine sulcus/cuneus/occipital poles) in the DMT–harmine group vs. placebo post-retreat: [Moderately Supported].**  
  In the voxel-wise `CONN` analysis (cluster-forming $p < 0.001$, cluster-level $q_{\text{FDR}} < 0.05$), both the group-by-time interaction (`Synergy`) and the post-retreat ANCOVA (`DMT–harmine > Placebo: Post`) identified reciprocating SAL–VIS clusters that replicated with and without GSR. Caveats include substantial unblinding ($>80\%$ of participants correctly identified drug allocation) and the relatively small sample size ($n = 19$ vs. $20$).

* **Meditation alone (placebo arm) decouples resting-state networks and reduces global FC in SAL/FPN parcels post-retreat: [Moderately Supported].**  
  Seed-to-voxel FC decreases (VIS–right insula, DAN–precuneus, FPN–visual cortex) survived cluster-level FDR correction with and without GSR. However, the surface-based global FC reductions in three SAL/FPN clusters (`Figure 4`) survived FDR correction *only* without GSR and disappeared when GSR was applied, indicating sensitivity to global physiological signal fluctuations.

* **Increased within-network VIS connectivity and ROI-to-ROI between-network connectivity in the DMT–harmine group: [Overstated].**  
  The Abstract states without qualification that *"the DMT–harmine group showed increased FC within the visual network (VIS)"*, whereas Section `Within- and between-network connectivity` and `Figure 3` explicitly report that **no within- or between-network ROI-to-ROI comparisons survived multiple-testing correction ($q_{\text{FDR}} < 0.05$)**; the within-VIS effect was merely an uncorrected trend ($t = 2.29, p_{\text{uncorrected}} = 0.025$).

* **Association between post-retreat SAL–VIS connectivity change and Day 2 Mystical Experience Questionnaire (MEQ) and Toronto Mindfulness Scale (TMS) scores: [Fragile].**  
  The SAL–VIS cluster was selected because it showed a significant group difference (`DMT–harmine > Placebo`), and Day 2 MEQ/TMS scores also differed strongly by group. Within the DMT–harmine group itself, SAL–VIS FC did not correlate with MEQ, and when baseline-adjusted change scores ($\Delta\text{MEQ}$, $\Delta\text{TMS}$) were analyzed, the group $\times$ questionnaire interactions were non-significant.

---

## 3. Forensic Defect Inventory

### 1. Degrees of Freedom ($F(1, 74)$) and Within-Group ANCOVA Misspecification in Repeated-Measures Analyses (Pillar 3 & Pillar 4)
* **Defect:**
  1. In `Figure 3` (lines 120, 123, 125), the two-way repeated-measures ANOVA (`Synergy` contrast: Group $\times$ Time) on $N = 39$ participants (19 DMT–harmine, 20 placebo; 78 total scans) reports degrees of freedom as **$F(1, 74)$** (e.g., $F(1, 74) = 6.16, p = 0.015$; $F(1, 74) = 5.31, p = 0.024$). In a two-group $\times$ two-timepoint design with $N = 39$ subjects, $df_{\text{error}} = 78 - 4 = 74$ occurs only if the 78 scans are entered into an ordinary between-subjects $2 \times 2$ ANOVA **without subject-level random intercepts / repeated-measures pairing**! In a properly paired $2 \times 2$ mixed ANOVA (equivalent to an independent $t$-test on $\text{Post} - \text{Pre}$ difference scores across 39 subjects), the denominator degrees of freedom must be $df = N - 2 = \mathbf{37}$, not $74$.
  2. In Section `Statistical analyses` (line 82), the authors state that contrasts (iii) `Meditation (Placebo: Post > Pre)` and (iv) `Psychedelic-augmented meditation (DMT–harmine: Post > Pre)` were implemented *"as ANCOVAs restricted to the corresponding group, with baseline values of the other group included as covariates."* Conditioning a within-group change test for the Placebo group ($n = 20$) on the baseline values of the independent DMT–harmine group ($n = 19$) is either a severe design-matrix error in `CONN` or a garbled description of a pooled ANCOVA model.
* **Actionable Fix:** Audit the second-level design matrix for `Figure 3` (`Supplementary Table S6`) to ensure subject-specific intercepts were included (yielding $df = 1, 37$ for the Group $\times$ Time interaction and main effect of Time), and clarify or re-compute the within-group `Post > Pre` contrasts as paired $t$-tests within each group ($df = 18$ for DMT–harmine, $df = 19$ for placebo).

### 2. Abstract and Conclusion Overstatement of Uncorrected Null ROI-to-ROI Results (Pillar 1 & Pillar 5)
* **Defect:** All ROI-to-ROI within-network (6 tests) and between-network (15 pairs) comparisons failed to survive FDR correction ($q_{\text{FDR}} < 0.05$). Nevertheless, the `Abstract`, `Discussion`, and `Conclusion` present the uncorrected within-VIS trend ($p_{\text{uncorrected}} = 0.025$) as a primary positive finding alongside the FDR-corrected seed-to-voxel clusters.
* **Actionable Fix:** Explicitly qualify all within-network VIS findings in the `Abstract` and `Conclusion` as exploratory uncorrected trends that did not survive FDR correction, or restrict headline claims to the cluster-FDR-corrected seed-to-voxel SAL–VIS and DAN–VIS findings.

### 3. Terminology of "Synergy" Without a Drug-Only Control Arm (Pillar 1 & Pillar 5)
* **Defect:** Labelling the $2 \times 2$ interaction contrast (`DMT–harmine > Placebo: Post > Pre`) as *"Synergy"* implies a super-additive interaction between meditation and DMT–harmine ($\text{Drug} \times \text{Meditation} \times \text{Time}$). Because both arms participated in the 3-day meditation retreat and no non-meditating DMT–harmine group was included, this contrast estimates the subacute pharmacological effect of DMT–harmine in a retreat context, not formal synergy.
* **Actionable Fix:** Rename Contrast (i) from `Synergy` to `Group × Time Interaction (Drug vs. Placebo)` throughout the text and figures.

---

## 4. Quantitative Rubric Scoring

| Rubric Dimension | Score | Max | Forensic Justification |
| :--- | :---: | :---: | :--- |
| **1. Methodological & Statistical Rigor** | **2.3** | **3.5** | Rigorous `fMRIPrep`/`CONN`/`BrainSpace` pipeline with GSR sensitivity analyses, but marred by $F(1, 74)$ un-paired degrees of freedom in the 39-subject $2 \times 2$ ANOVA and unclear within-group ANCOVA specification. |
| **2. Claim-to-Evidence Alignment** | **1.7** | **2.5** | Transparent reporting of null gradient and FDR-corrected ROI results in the body text, but the Abstract presents uncorrected within-VIS trends ($p = 0.025$) as positive findings and labels the $2 \times 2$ contrast "Synergy" without a drug-only arm. |
| **3. Data Integrity & Biological Plausibility** | **1.7** | **2.0** | Biologically plausible subacute normalization of cortical gradients 48 h post-DMT–harmine; candid acknowledgment of $>80\%$ participant unblinding and group-retreat setting effects. |
| **4. Reproducibility & Data Integrity** | **1.8** | **2.0** | Exemplary open data availability on OpenNeuro (`ds006644`), pre-registration (`NCT05780216`), and complete software version reporting (`fMRIPrep` 23.0.2, `CONN` 22.a, `BrainSpace` 0.1.10, `BrainStat` 0.4.2). |
| **Scientific Core Score** | **5.7** | **8.0** | Sum of Rigor + Claims + Biology (`2.3 + 1.7 + 1.7`). |
| **Overall Composite Score** | **7.5** | **10.0** | **Strong / Sound** (`2.3 + 1.7 + 1.7 + 1.8`). |
