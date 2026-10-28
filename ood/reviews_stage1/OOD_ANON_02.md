# Review of OOD_ANON_02

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **3.3 / 10.0** (Flawed / Overstated)  
* **Score Breakdown:** Rigor: 0.9/3.5 | Claims: 0.8/2.5 | Biology: 1.0/2.0 | Reproducibility: 0.6/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This cross-sectional case-control study investigates global graph-theoretical topological properties of white matter (WM) structural networks (derived from deterministic DTI tractography across the 90-node AAL atlas) and resting-state functional networks (derived from BOLD fMRI correlations across the 116-node AAL atlas) in 45 patients with amnestic mild cognitive impairment (aMCI) and 42 healthy controls (HC). Using PANDA, DPARSFA, and GRETNA, the authors compute small-worldness ($C_p, L_p, \gamma, \lambda, \sigma$), rich-club organization, global and local efficiency ($E_g, E_{loc}$), assortativity ($r$), hierarchy ($b$), and synchronization ($s$) across sparsity thresholds. They conclude that aMCI is characterized by a "structure-function dissociation" in which the WM structural network undergoes fragmentation and hub disruption while the functional network exhibits hyper-localized compensatory reorganization.

While multimodal characterization of structural and functional connectomes in aMCI is clinically relevant, the manuscript's primary conclusions are compromised by extensive internal contradictions between the Abstract/Discussion and the Results, a fatal statistical over-controlling error, and unaddressed confounding from mismatched parcellations and binary thresholding. Most notably, the Abstract and Discussion claim significant group differences in structural synchronization ($s$), structural assortativity ($r$), rich-club coefficients, and functional local efficiency that the Results section explicitly reports as statistically non-significant ($P > 0.05$). Furthermore, the authors state in Figure 10 and Section 4 that group comparisons between aMCI and HC were statistically controlled for MMSE and MoCA scores as covariates—the very cognitive scales used to define the aMCI and HC groups—which removes the disease variance of interest. Finally, residual text from an undisclosed acupuncture intervention ("before and after acupuncture" in Section 3.2.1; "skin at the acupuncture site is intact" in Section 2.1.1) and missing repository accession numbers undermine data provenance.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Claim of decreased structural synchronization ($s$), altered structural assortativity ($r$), and altered rich-club coefficients in aMCI (Abstract, Sections 3.2.2, 3.2.4, 3.2.6, and Discussion 4.2, 4.4, 4.6): [Methodologically Flawed].**  
  The Abstract and Discussion assert significant group differences that directly contradict the Results section:
  1. *Synchronization ($s$):* The Abstract states "the synchronization coefficient ($s$) was significantly reduced at sparsity levels ranging from 0.28 to 0.30," and Discussion 4.6 states "significantly decreased $s$ values in white matter structural networks directly reflected reduced fiber connection density." However, Section 3.2.6 explicitly states: "within the sparsity range of 0.28~0.30, intergroup differences in global white matter connection strength $s$ values were no statistically significant ($P < 0.05$). No significant differences were observed in $as$ or $aszscore$."
  2. *Assortativity ($r$):* Discussion 4.4 states "In this study, the Assortativity index of white matter structural networks showed significant intergroup differences," whereas Section 3.2.4 states "Within the sparsity range of 0.21~0.41, there were no statistically significant differences in assortativity coefficients ($r$ and $rzscore$) between the two groups ($P > 0.05$)."
  3. *Rich-club coefficient:* The Abstract claims "the Rich-club coefficient was decreased" in the WM network and "increased within a certain Degree range" in the functional network, but Sections 3.2.2(1) and 3.2.2(2) explicitly report that for both structural and functional networks, "Both $\phi_{norm}$ and $\phi_{real}$ showed no significant difference between the two groups, as shown in Figure 6 [and Figure 8]."
  4. *Hierarchy ($b$):* The Abstract claims "a significant decrease in $b$ within the sparsity range of 0.39~0.4," whereas Section 3.2.5 reports significance only at "0.4~0.41" and no significant difference in normalized $b_{zscore}$ or AUC ($ab$).

* **Core conclusion of "structure-function dissociation" driven by elevated functional local efficiency (Abstract, Conclusion, Section 3.2.3): [Overstated].**  
  The Abstract and Conclusion claim that "the functional network compensates through rigid, hyper-localized reorganization with elevated local efficiency." However, Section 3.2.3(2) and Discussion 4.3 show that the AUC of functional local efficiency ($aE_{loc}$) was not significantly different between groups ("At the functional network level, aMCI patients exhibited an advantage in global efficiency, while the change in $E_{loc}$ was not significant"). Conversely, $aE_{loc}$ and $aC_p$ were significantly *higher* in the WM structural network of aMCI patients (Section 3.2.3(1)), which is the exact opposite of structural fragmentation. Moreover, structural networks were built on 90 cerebral nodes (excluding the cerebellum) with sparsity $0.21$–$0.41$, whereas functional networks were built on 116 nodes (including 26 cerebellar regions, where 3 of the top 7 HC functional rich-club hubs reside; Table 3) with sparsity $0.05$–$0.50$, confounding modality differences with anatomical coverage and graph density.

* **Group comparisons controlling for MMSE and MoCA scores as covariates (Figure 10 caption, Section 4 Discussion): [Methodologically Flawed].**  
  The caption to Figure 10 and Section 4 state that intergroup comparisons between HC and aMCI "statistically controlled for covariates such as age, sex, years of education, MMSE, and MoCA scores." Because inclusion in the aMCI group was defined by MMSE $\ge 17\text{–}24$ and MoCA $\le 26$ while HC required MMSE $> 26$ (Section 2.1, Table 2: MMSE $25.20 \pm 1.21$ vs. $28.26 \pm 1.06$, $P = 0.000$), controlling for MMSE and MoCA in an ANCOVA testing for group differences between aMCI and HC introduces severe collinearity with the group indicator and conditions on the defining clinical outcome. Furthermore, Section 1 claims the study "revealed significant correlations between multimodal topological indices and clinical cognitive scores," yet no correlation analysis with cognitive scores appears anywhere in the Results.

* **Undisclosed acupuncture trial provenance and asymmetric head-motion exclusion criteria (Sections 2.1.1, 2.3, 2.5, 3.2.1): [Fragile].**  
  The manuscript frames the study as an observational case-control study of aMCI vs. HC, but contains unedited text from an acupuncture clinical trial: Section 2.1.1 requires "the skin at the acupuncture site is intact without scars"; Section 2.5 states "Most of the subjects have not experienced acupuncture"; and Section 3.2.1 states "both groups exhibited small-world properties before and after acupuncture." In addition, Section 2.3 specifies head-motion exclusion criteria (displacement $> 2.0\text{ mm}$ or rotation $> 2^\circ$) exclusively for "any frame of images in the HC group" without stating whether identical motion quality control was enforced for the aMCI group.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Remove Conditioning on Diagnostic Cognitive Scores (MMSE/MoCA) in Group ANCOVAs
* **WHY:** Including MMSE and MoCA as covariates when comparing groups defined by MMSE and MoCA thresholds partials out the disease effect itself and distorts parameter estimates.
* **WHAT:** Re-run all intergroup topological comparisons controlling only for demographic and technical confounders (age, sex, education years, and mean framewise displacement).
* **HOW:** In GRETNA / SPSS, specify the general linear model for each AUC topological metric ($aC_p, aL_p, a\gamma, a\lambda, a\sigma, aE_g, aE_{loc}, ar, ab, as$) with Group (aMCI vs. HC) as the fixed factor and Age, Sex, Education, and Mean FD as covariates. Separately, within the aMCI group, compute partial correlations between the topological AUC metrics and MMSE/MoCA scores (controlling for Age, Sex, and Education) to fulfill the correlation analysis promised in the Introduction.

#### 2. Harmonize Parcellation Atlases Across Structural and Functional Modalities
* **WHY:** Comparing a 90-node cerebral structural graph against a 116-node cerebro-cerebellar functional graph confounds modality differences ("structure-function dissociation") with the inclusion of 26 cerebellar nodes that act as major functional hubs (Table 3).
* **WHAT:** Recompute the functional network graph metrics restricted to the identical 90-node AAL cerebral parcellation used for the DTI structural network.
* **HOW:** Slice the $116 \times 116$ Fisher-$Z$ functional connectivity matrices to the first $90 \times 90$ cortical/subcortical AAL regions prior to sparsity thresholding in GRETNA, and verify whether the rich-club redistribution and $aL_p / aE_g$ differences persist when the cerebellum is excluded.

#### 3. Reconcile Contradictions Between Abstract/Discussion and Statistical Results
* **WHY:** Claiming significant alterations in Rich-club coefficients ($\phi_{norm}$), assortativity ($r$), structural synchronization ($s$), and functional local efficiency ($E_{loc}$) when $P > 0.05$ violates basic scientific reporting standards.
* **WHAT:** Revise the Abstract, Results, Discussion, and Conclusion to strictly reflect the Bonferroni/FDR-corrected AUC and sparsity-level statistical tests.
* **HOW:** Remove claims of significant group differences in $\phi_{norm}$, assortativity $r$, functional $aE_{loc}$, and hierarchy $b_{zscore}$; base primary inferences on the integrated AUC metrics ($aC_p, aE_{loc}$ in WM; $aL_p, aE_g$ in fMRI) rather than isolated single-sparsity $t$-tests; and correct the typo in Section 3.2.6 ("were no statistically significant ($P < 0.05$)").

#### 4. Clarify Study Provenance, Motion Exclusion, and Binarization vs. Weighted Definitions
* **WHY:** References to "before and after acupuncture" (Section 3.2.1), HC-only motion exclusion (Section 2.3), contradictory edge definitions (binary FA matrices in Section 2.8 vs. weighted synchronization/strength in Section 2.9), and placeholder Data Availability statements ("can be found in the article/supplementary material" with no accession numbers) prevent independent verification.
* **WHAT & HOW:** Clarify in Section 2 whether these scans represent baseline pre-intervention data from an acupuncture trial (and provide the clinical trial registration number); confirm that the $>2.0\text{ mm} / 2^\circ$ motion exclusion criterion was applied symmetrically to both aMCI and HC participants (reporting mean FD per group in Table 2); clarify how negative functional correlations were handled when taking absolute values during binarization (Section 2.8); and deposit the $90 \times 90$ DTI and $116 \times 116$ fMRI connectivity matrices in a public repository with a valid accession link.
