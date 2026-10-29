# Review of FEXP_ANON_001

**Overall Score:** **6.5 / 10.0** (Mixed / Salvageable) | **Scientific Core Score:** **5.3 / 8.0**  
* **Score Breakdown:** Rigor: 2.1/3.5 | Claims: 1.5/2.5 | Biology: 1.7/2.0 | Reproducibility: 1.2/2.0

---

## 1. Blinded Metadata Perception
* **Anonymized Manuscript ID:** `FEXP_ANON_001`
* **Perceived Domain & Design:** Public health / social epidemiology; cluster-randomized controlled trial (cRCT) with a double-randomized household sampling design evaluating within-village spillover effects of a 14-session gender-transformative coffee ceremony intervention (Unite for a Better Life, UBL) on intimate partner violence (IPV), HIV risk behaviors, and gender norms in rural Ethiopia (64 clusters, 2,516 baseline households in the control + indirect beneficiary subsample; 4,379 endline individuals).
* **Blinding Integrity:** Double-blind review maintained; evaluated strictly on internal design, statistical modeling, and tabular consistency at $t_0$.

---

## 2. Executive Summary & Editorial Verdict

This study analyzes the within-cluster spillover effects of the Unite for a Better Life (UBL) intervention in 64 rural Ethiopian villages (kebeles/gottes) randomized equally (16 clusters per arm) to control, women's UBL, men's UBL, or couples' UBL. Within the 48 treated clusters, 80% of sampled households were randomized to participate directly (`direct beneficiaries`) and 20% were not invited (`indirect beneficiaries`, surveyed at baseline in 2014–2015 and 24 months post-intervention in 2017–2018). Comparing indirect beneficiaries against control clusters using generalized estimating equations (GEE) with logistic link and village-clustered robust standard errors, the authors find null effects on both prespecified primary outcomes (women's past-year experience of physical IPV and sexual IPV across all three arms), a reduction in men's self-reported perpetration of sexual IPV in the men's UBL arm ($\text{AOR} = 0.55$, $95\%\text{ CI } [0.38, 0.80]$, $p = 0.002$), an unexpected harmful increase in men's self-reported perpetration of physical IPV in the couples' UBL arm ($\text{AOR} = 1.49$, $95\%\text{ CI } [1.08, 2.05]$, $p = 0.016$), and heterogeneous shifts across secondary knowledge/attitude indicators.

**Editorial Verdict: Major Revision (Mixed / Salvageable).** The double-randomized design is a genuine methodological strength for isolating within-village spillover effects without selection bias into non-participation. However, the manuscript's headline conclusions are undermined by four serious methodological and interpretive defects: (1) conflating underpowered non-significant interaction terms ($p > 0.05$) with proof of equivalence between direct and indirect beneficiaries ("benefited as much as direct participants"), (2) unadjusted multiple hypothesis testing across 19 outcomes $\times$ 3 arms $\times$ 2 sexes (>100 tests) while elevating secondary self-reported male perpetration results over null primary female-reported experience outcomes, (3) non-random cluster-level record-keeping loss that eliminated all indirect beneficiaries in 3 of 16 clusters in the couples' arm and reclassified 222 baseline respondents into the direct beneficiary arm, and (4) asymptotic GEE sandwich variance estimation with only 13 to 16 clusters per arm without small-sample bias correction, alongside severe sparse-cell instability (e.g., condom use at last intercourse with 0 to 5 events per arm). All four issues can be resolved through computational re-analysis and textual reframing without new data collection.

### Assessment of Specific Claims
* **Claim 1 (Men's UBL reduced male self-reported past-year sexual IPV perpetration among indirect beneficiaries: $\text{AOR} = 0.55$, $p = 0.002$): [Moderately Supported].**  
  The effect size in Table 4 is large enough to survive Bonferroni correction across the three treatment arms for this secondary outcome, and information diffusion among men in the men's arm was high (93.2% shared, 67.6% remembered). However, it is not corroborated by female indirect beneficiaries' reports of sexual IPV experience in the same arm ($\text{AOR} = 0.80$, $95\%\text{ CI } [0.61, 1.05]$, $p = 0.106$) and remains susceptible to differential social desirability reporting among men in communities where male peers underwent norm-transformation training.
* **Claim 2 (Intervention effects among indirect beneficiaries were comparable to those of direct beneficiaries; "indirect beneficiaries who did not participate in the programme benefited as much as direct participants"): [Methodologically Flawed].**  
  The authors base this claim on failing to reject the null hypothesis of zero interaction ($\text{Treatment} \times \text{Indirect}$) in Table 7. The Methods explicitly acknowledge that no power calculation was performed for the 20% indirect beneficiary subsample ($n \approx 125\text{–}162$ baseline households per arm). Wide confidence intervals on the interaction terms (e.g., $\text{AOR} \in [0.60, 1.74]$ for physical IPV) reflect low statistical power to detect differential effects, not equivalence. Furthermore, for male physical IPV perpetration in the couples' arm, the interaction term is highly significant ($\text{AOR} = 1.53$, $p < 0.001$) in the direction of harm for indirect beneficiaries.
* **Claim 3 (Women's UBL significantly increased condom use at last intercourse among female indirect beneficiaries: $\text{AOR} = 5.93$, $p = 0.015$): [Fragile].**  
  Table 5 shows that this odds ratio is driven by 4/146 (2.7%) events in the women's UBL arm versus 5/769 (0.7%) in the control group and 0/120 (0.0%) in the couples' UBL arm (where the model failed to converge, reporting $\text{OR} = 1.00$ with missing CI). Fitting a covariate-adjusted GEE logistic regression with 7 baseline covariates and district fixed effects on 4 events in 16 clusters violates events-per-variable requirements and produces severe small-sample bias.
* **Claim 4 (UBL shifts gender norms, decision-making, and HIV behaviors broadly across all three arms among indirect beneficiaries): [Overstated].**  
  Tables 5 and 6 evaluate 11 non-IPV outcomes across 3 arms for both women and men (66 tests) without false discovery rate (FDR) or family-wise error rate control. Several highlighted effects have marginal nominal $p$-values ($p = 0.030$ to $0.042$) that do not survive multiple-testing adjustment.

---

## 3. Forensic Defect Inventory

1. **Pillar 4 Violation — Equivalence Claimed from Underpowered Null Interaction Tests (Table 7, Abstract, Discussion p. 57):**  
   In the Abstract ("The intervention effects among indirect beneficiaries were statistically similar to those reported for the direct beneficiaries. In general, the hypothesis of equal effects cannot be rejected") and Discussion ("indicating that indirect beneficiaries who did not participate in the programme benefited as much as direct participants"), the authors treat non-significant interaction $p$-values in Table 7 as proof of equal treatment efficacy. Because only ~21 households per cluster were assigned to the indirect sample, the standard errors of the interaction log-odds ratios are ~0.20–0.28, meaning the test cannot rule out a 35%–50% attenuation or reversal of treatment effects. Formal equivalence requires Two One-Sided Tests (TOST) against prespecified equivalence margins, not failing to reject a point-null interaction.
2. **Pillar 2 & 3 Violation — Non-Random Cluster Attrition and Misclassification of 222 Households (Results, line 146):**  
   Second-level randomization status (direct vs. indirect) was lost for 222 baseline respondents due to record-keeping errors, including *all* indirect beneficiaries in 3 of the 16 clusters in the couples' UBL arm. Coding these 222 respondents as "direct beneficiaries" completely removes 3 clusters from the couples' arm in the indirect-beneficiary analysis (leaving only $K = 13$ clusters vs. $K = 16$ in other arms) and contaminates the direct-beneficiary reference group in Table 7 with unrecorded indirect beneficiaries, biasing the $\text{Treatment} \times \text{Indirect}$ interaction toward the null.
3. **Pillar 3 & 4 Violation — Uncorrected GEE Sandwich Standard Errors with Small Number of Clusters ($K = 13\text{–}16$ per arm):**  
   Standard Liang-Zeger robust sandwich variance estimators in GEE underestimate true variance when the number of clusters per treatment arm is below 30–40. With 16 clusters per arm (and only 13 in the couples' arm), nominal $p$-values are anti-conservative without Mancl-DeRouen, Kauermann-Carroll, or wild cluster bootstrap corrections.
4. **Pillar 4 & 5 Violation — Uncorrected Multiple Testing and Elevation of Secondary Outcomes Over Null Primary Outcomes:**  
   Both prespecified primary outcomes (women's experience of past-year physical IPV and sexual IPV) are null across all three arms in Table 4 ($p = 0.106$ to $0.923$). The manuscript's abstract and headline conclusions pivot to a secondary outcome (men's self-reported sexual IPV perpetration in one of three arms) and highlight nominal $p < 0.05$ hits across 90+ unadjusted secondary/additional tests in Tables 4–6, while downplaying the statistically significant *increase* in male physical IPV perpetration in the couples' arm ($\text{AOR} = 1.49$, $p = 0.016$; interaction $\text{AOR} = 1.53$, $p < 0.001$).
5. **Pillar 7 Violation — Table, Text, and Questionnaire Item Discrepancies:**  
   * **Text vs. Table 4 CI mismatch:** Line 219 reports men's UBL sexual IPV perpetration AOR as `0.55, 95% CI 0.38 to 0.81, p=0.002`, whereas Abstract (line 9) and Table 4 (line 211) report `95% CI 0.38 to 0.80`. Similarly, line 221 reports women's comprehensive HIV knowledge AOR CI as `1.03 to 3.81`, whereas Table 5 (line 230) reports `1.03–3.18`.
   * **Table 1 internal coding mismatches:** For emotional violence (rows 4 and 8 of Table 1, lines 100 and 105), the Indicator column states *"asked five items"* but lists only four numbered items `(1)`–`(4)`, and the Coding column states *"responded yes to any of the four items"*. For Support for gender equitable norms (Table 1, line 115), the Indicator column states *"agreed with 13 statements"* but lists 12 numbered statements `(1)`–`(12)`, and the Coding column states *"summing the responses to all 12 questions"*.
   * **Sample size drop in Tables 5 & 6:** In Table 4 and the household decision-making rows of Tables 5–6, the endline sample size is $N \approx 2,173$ women and $N \approx 2,186$ men (both baseline respondents and spouses), whereas the HIV and IPV knowledge/norms rows of Tables 5–6 have roughly half the sample size ($N = 1,173$ women and $N = 1,040$ men) because those modules were only administered in the full questionnaire—a distinction indicated only by a table dagger (`†`) without explanation in the main text.
   * **Data and code availability:** Neither a Data Availability statement nor replication code is provided in the manuscript text.

---

## 4. Quantitative Rubric Scoring

| Rubric Dimension | Score | Max | Forensic Justification |
| :--- | :---: | :---: | :--- |
| **1. Methodological & Statistical Rigor** | **2.1** | **3.5** | Strong double-randomized cluster design, but compromised by uncorrected small-sample GEE sandwich SEs ($K=13\text{–}16$), sparse-data logistic overfitting (4 events in Table 5 condom use), and invalid inference of equivalence from null interaction tests. |
| **2. Claim-to-Evidence Alignment** | **1.5** | **2.5** | Both primary outcomes (female-reported physical and sexual IPV) are null; abstract and discussion overstate equivalence with direct beneficiaries and selectively emphasize secondary male self-reports without multiple-testing correction. |
| **3. Data Integrity & Biological/Behavioral Plausibility** | **1.7** | **2.0** | Loss of second-level randomization records for 222 households (including 3 entire clusters in the couples' arm) and uncorroborated divergence between male self-reported sexual IPV perpetration and female-reported experience. |
| **4. Reproducibility & Data Integrity** | **1.2** | **2.0** | Numerical discrepancies between text and tables (`0.81` vs `0.80`; `3.81` vs `3.18`), item-count mismatches in Table 1 (5 vs 4 items; 13 vs 12 items), and absence of replication code/data availability statement. |
| **Total Composite Score** | **6.5** | **10.0** | **Mixed / Salvageable** (Scientific Core Score: **5.3 / 8.0**) |

---

### Constructive and Doable Suggestions for Improvement

1. **Replace Invalid Equivalence Claims with Formal Equivalence Bounds or Tempered Language:**  
   * **WHY:** Failing to reject $H_0: \beta_{\text{interaction}} = 0$ in an underpowered 20% subsample does not prove that indirect beneficiaries benefited as much as direct beneficiaries.  
   * **WHAT & HOW:** Report the minimum detectable effect size (MDE) for the interaction terms in Table 7, perform Two One-Sided Tests (TOST) against a prespecified equivalence margin (e.g., $\Delta \log\text{OR} = \pm 0.25$), and remove the claim that indirect beneficiaries "benefited as much as direct participants."
2. **Apply Small-Sample Cluster Corrections and Multiple-Testing Adjustments:**  
   * **WHY:** With 13–16 clusters per arm and >90 secondary tests, asymptotic GEE SEs and unadjusted $p$-values inflate Type I error.  
   * **WHAT & HOW:** Re-estimate Table 4–7 $p$-values using a Mancl-DeRouen / Kauermann-Carroll finite-sample GEE variance correction or cluster wild bootstrap, and report Benjamini-Hochberg FDR $q$-values alongside nominal $p$-values within each prespecified outcome family. For condom use at last intercourse (0–5 events per arm), use exact logistic regression or Fisher's exact permutation test at the cluster level.
3. **Conduct Sensitivity Analysis for the 222 Misclassified Households and 3 Missing Couples' Arm Clusters:**  
   * **WHY:** Reclassifying 222 baseline respondents with missing second-level randomization status as direct beneficiaries attenuates the direct-vs-indirect contrast in Table 7.  
   * **WHAT & HOW:** Re-estimate Table 7 excluding the 3 clusters in the couples' arm where indirect status was lost (rather than pooling their indirect beneficiaries into the direct group), and verify robustness under inverse-probability weighting for missing randomization records.
4. **Correct Numerical and Tabular Typos:**  
   * **WHAT & HOW:** Fix line 219 (`0.81` $\to$ `0.80`), line 221 (`3.81` $\to$ `3.18`), and Table 1 item counts (`five items` $\to$ `four items` in emotional IPV; `13 statements` $\to$ `12 statements` in GEMS).
