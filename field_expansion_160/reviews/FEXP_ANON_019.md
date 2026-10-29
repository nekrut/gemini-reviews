# Review of FEXP_ANON_019

**Overall Score:** **6.3 / 10.0** (Mixed / Salvageable) | **Scientific Core Score:** **4.7 / 8.0**  
* **Score Breakdown:** Rigor: 1.7/3.5 | Claims: 1.5/2.5 | Biology: 1.5/2.0 | Reproducibility: 1.6/2.0

---

## 1. Blinded Metadata Perception

* **Manuscript ID:** `FEXP_ANON_019`
* **Perceived Research Domain:** Behavioral epidemiology, public health psychology, and longitudinal survey methodology (vaccine attitudes and pandemic spillover effects).
* **Study Design:** Two-wave longitudinal panel survey across two independent adult cohorts in Finland comparing pre-pandemic baseline to pandemic follow-up: Study 1 ($N = 205$, Pietarsaari region; Wave 1 in April 2019, Wave 2 in March–April 2020 prior to COVID-19 vaccine availability) and Study 2 ($N = 197$, FinnBrain Birth Cohort parents; Wave 1 in May–December 2018, Wave 2 in June–July 2021 after COVID-19 vaccine rollout).
* **Primary Methods:** Scale reliability estimation (McDonald's $\omega$ and Spearman-Brown coefficient), paired-samples $t$-tests with Cohen's $d$ and within-subjects probability of superiority (`RProbSup`), and categorical repeated-measures tests (McNemar-Bowker test of symmetry in Study 1; McNemar's test in Study 2) conducted in IBM SPSS Statistics 27.

---

## 2. Executive Summary & Editorial Verdict

This manuscript investigates whether the COVID-19 pandemic produced psychological "spillover" effects on public attitudes toward non-COVID-19 vaccines (seasonal influenza and childhood vaccines), perceived severity of measles and influenza, and trust in healthcare professionals. Using two longitudinal panel samples of Finnish adults surveyed before and during the pandemic—Study 1 ($N = 205$, surveyed in April 2019 and April 2020) and Study 2 ($N = 197$ parents from the FinnBrain Birth Cohort, surveyed in 2018 and June–July 2021)—the authors report consistent increases in the perceived benefit ($d = -0.46$ in Study 1; $d = -0.19$ and $-0.33$ in Study 2) and perceived safety ($d = -0.15$ in Study 1; $d = -0.49$ in Study 2) of influenza vaccines, alongside smaller, study-specific changes in childhood vaccine safety ($d = -0.44$ in Study 2 only), trust in healthcare professionals ($d = -0.31$ in Study 1 only), and self-reported influenza vaccination uptake/demand in Study 2 ($p = 0.007$). Data access is governed by Finnish participant consent and FinnBrain Material Transfer Agreement (MTA) procedures, which are appropriately documented.

The longitudinal within-subject design is an important improvement over purely cross-sectional or retrospective post-hoc surveys of pandemic vaccine attitudes. However, several methodological and statistical flaws weaken the reliability of the secondary and subgroup conclusions: (1) in Study 2, the response options for past influenza vaccination were changed between waves by adding *"I wanted to get vaccinated, but there were no vaccines available"* at Wave 2 and collapsing it into *"yes"*, creating an asymmetric measurement artifact; (2) across both studies, 42 paired/categorical tests (including gender-stratified tests with only $n = 43\text{–}62$ men) are run without multiple-testing correction, and gender differences are claimed by comparing subgroup $p$-values rather than testing a formal $\text{Time} \times \text{Gender}$ interaction; (3) the single item used to measure "perceived severity of influenza" is a double-barreled question that conflates symptom severity with vaccination worth; and (4) despite $>74\%\text{–}82\%$ attrition between Wave 1 and Wave 2, no baseline comparison between retained participants and Wave 1 dropouts (or inverse probability of attrition weighting) is reported. All of these issues can be resolved through computational reanalysis of the existing survey dataset.

### Specific Assessment of Core Claims

* **Perceived benefit and safety of seasonal influenza vaccines increased from before to during the COVID-19 pandemic:** **[Well Supported].**  
  The increase in perceived benefit of influenza vaccination in Study 1 ($t(200) = -6.56, p < 0.001, d = -0.46$) and perceived efficacy in Study 2 ($t(189) = -4.61, p < 0.001, d = -0.33$), as well as perceived safety of influenza vaccination in Study 2 ($t(185) = -6.70, p < 0.001, d = -0.49$), show moderate effect sizes that remain highly significant even under strict Bonferroni correction across all conducted tests. By contrast, the Study 1 influenza safety increase ($t(192) = -2.08, p = 0.039, d = -0.15$) is marginal and does not survive multiple-testing correction.

* **More people received or wanted to receive the influenza vaccine during the pandemic than before:** **[Fragile].**  
  In Study 1, future intention to take the influenza vaccine did not change ($\chi^2(3, N=201) = 2.80, p = 0.423$). The positive claim in the Abstract rests entirely on Study 2 ($\chi^2(1, N=191) = 7.20, p = 0.007$), where the Wave 1 question had binary options (*"no"*, *"yes"*) for 2017–2018 uptake, whereas the Wave 2 question added a third option (*"I wanted to get vaccinated, but there were no vaccines available"*) and coded both *"yes"* and the unfulfilled-intention option as *"yes"* (Section "Past influenza vaccination behavior", line 176). Conflating actual vaccination behavior at Wave 1 with behavior plus stated unfulfilled intention at Wave 2 biases the McNemar test toward finding an increase, and the manuscript fails to report how many Wave 2 respondents actually received the vaccine versus chose the third option.

* **Perceived severity of influenza increased during the pandemic, whereas perceived severity of measles did not change:** **[Methodologically Flawed].**  
  While the measles item directly asked about disease severity (*"Measles is a very serious disease"*), the item used to measure "perceived severity of influenza" was *"It is not worth getting the influenza vaccine, as the influenza symptoms are not serious"* (reversed; line 85). This is a double-barreled item that directly embeds the value of getting the influenza vaccine (*"not worth getting the influenza vaccine"*). Consequently, changes in this item ($d = -0.22$ in Study 1; $d = -0.19$ in Study 2) cannot be isolated as changes in perceived disease severity rather than perceived vaccine utility.

* **Perceived safety of childhood vaccines increased in Study 2 ($d = -0.44$), while perceived benefit slightly decreased in Study 1 ($p = 0.045, d = 0.14$):** **[Moderately Supported].**  
  The Study 2 increase in perceived safety ($t(176) = -5.85, p < 0.001, d = -0.44$) is statistically robust, although two of the three retained items in Study 2 asked about *"vaccines in general"* rather than *"childhood vaccines"* specifically (line 186, 209), confounding general COVID-19/adult vaccine safety perceptions with childhood vaccine perceptions. Conversely, the Study 1 decrease in childhood vaccine benefit ($t(200) = 2.02, p = 0.045, d = 0.14$) coincides with a sharp drop in scale internal consistency (McDonald's $\omega$ dropping from $0.823$ at Wave 1 to $0.657$ at Wave 2; Table 2) and does not survive correction for multiple comparisons.

* **Gender-specific differences in attitude changes (e.g., changes occurring "only in men" in Study 1 and "only in women" in Study 2):** **[Methodologically Flawed].**  
  In both studies, the authors infer gender differences by running separate paired $t$-tests in men ($n = 63$ in Study 1; $n = 44$ in Study 2) and women ($n = 141$ in Study 1; $n = 153$ in Study 2) and contrasting $p < 0.05$ in one subgroup against $p > 0.05$ in the other (lines 131, 136, 138, 214, 219, 229). Because female sample sizes are $2.2\times$ to $3.5\times$ larger than male sample sizes, statistical power differs substantially between subgroups. No $\text{Time} \times \text{Gender}$ interaction test was performed.

---

## 3. Forensic Defect Inventory

### Defect 1: Asymmetric Coding of Wave 1 vs. Wave 2 Influenza Vaccination Behavior in Study 2 (Pillar 3 & Pillar 5)
* **Location:** Study 2 Methods ("Past influenza vaccination behavior", line 176) and Results (line 214).
* **Diagnostic Finding:** At Wave 1 (2018), respondents answered *"yes"* or *"no"* to whether they took the influenza vaccine. At Wave 2 (2021), respondents were offered *"no"*, *"yes"*, and *"I wanted to get vaccinated, but there were no vaccines available"*, and the authors collapsed the second and third options into *"yes"*. At Wave 1, individuals who intended to get vaccinated in 2017–2018 but did not (due to stockouts, scheduling, or inconvenience) were forced to answer *"no"*. Merging unfulfilled intention with realized behavior only at Wave 2 breaks measurement symmetry. Furthermore, the raw contingency table counts (how many respondents chose each option at Wave 1 and Wave 2) are omitted from the text.
* **Remediation:** Report the full $2 \times 3$ cross-tabulation of Wave 1 (`yes`, `no`) by Wave 2 (`yes`, `wanted to but unavailable`, `no`), and conduct a sensitivity McNemar test restricting Wave 2 `"yes"` strictly to actual vaccine recipients.

### Defect 2: Uncorrected Multiple Hypothesis Testing and Invalid Subgroup Inference by Separate $p$-Values (Pillar 3 & Pillar 4)
* **Location:** Study 1 Statistical analyses & Results (lines 95, 126–148) and Study 2 Statistical analyses & Results (lines 201, 214–234).
* **Diagnostic Finding:**
  1. **Multiple comparisons:** Each study evaluates 7 primary outcomes across 3 analytical strata (full cohort, men, women), yielding 42 hypothesis tests without any family-wise error rate (FWER) or false discovery rate (FDR) control. Marginal findings such as Study 1 childhood vaccine benefit ($p = 0.045$) and Study 1 influenza vaccine safety ($p = 0.039$) are likely Type I errors.
  2. **Subgroup fallacy:** Claiming that an effect occurred "only in men" or "only in women" based on separate subgroup $t$-tests without testing the $\text{Time} \times \text{Gender}$ interaction term violates standard biostatistical practice, especially given the severe sample-size imbalance ($77.7\%$ female vs. $22.3\%$ male in Study 2).
* **Remediation:** Apply Benjamini–Hochberg FDR or Holm–Bonferroni correction across the primary outcome family in each study, and replace separate gender $t$-tests with repeated-measures linear mixed models testing the $\text{Time} \times \text{Gender}$ interaction directly.

### Defect 3: Unassessed Attrition Bias Between Wave 1 Respondents and Wave 2 Panel Completers (Pillar 2)
* **Location:** Study 1 Participants (line 35) and Study 2 Participants (line 168).
* **Diagnostic Finding:** In Study 1, only 205 of 1,139 Wave 1 respondents (18.0%) completed Wave 2. In Study 2, only 197 of 770 valid Wave 1 respondents (25.6%) completed Wave 2 (after first conditioning on participation in a May 2020 COVID-19 survey). Although the authors have complete Wave 1 baseline attitude and demographic data for all 1,139 (Study 1) and 770 (Study 2) initial respondents, they never test whether panel completers differed systematically at baseline from dropouts, nor do they check whether inverse probability weights alter the longitudinal estimates.
* **Remediation:** Add a baseline attrition balance table comparing Wave 1 vaccine benefit, safety, severity, trust, and demographics between longitudinal completers ($n=205$ / $n=197$) and Wave 1 non-completers ($n=934$ / $n=573$), and perform a sensitivity analysis weighted by inverse probability of retention or post-stratified to regional gender/age margins.

### Defect 4: Construct Validity and Longitudinal Measurement Invariance Issues (Pillar 3)
* **Location:** Measures (lines 85, 181, 186) and Table 2 (lines 108–122).
* **Diagnostic Finding:**
  1. The single item measuring "perceived severity of influenza" (*"It is not worth getting the influenza vaccine, as the influenza symptoms are not serious"*) directly asks whether it is worth getting the vaccine, confounding vaccine utility with disease severity.
  2. In Study 2, two of the items in the "childhood vaccine safety" composite actually asked about *"vaccines in general"* rather than childhood vaccines (line 186, 209). During the June–July 2021 mass COVID-19 vaccination campaign, "vaccines in general" was inevitably interpreted by respondents in light of COVID-19 vaccines, explaining why childhood vaccine safety appeared to jump in Study 2 ($d = -0.44$) whereas no change occurred in Study 1 ($d = -0.12, p = 0.109$) where items specifically named childhood vaccines.
* **Remediation:** Analyze the single specific childhood-vaccine safety item in Study 2 separately from the two "vaccines in general" items to verify whether childhood vaccine safety perception truly increased, and rename the influenza severity item to accurately reflect "perceived necessity of vaccination given influenza severity."

---

## 4. Quantitative Rubric Scoring

| Rubric Dimension | Score | Max | Diagnostic Justification |
| :--- | :---: | :---: | :--- |
| **1. Methodological & Statistical Rigor** | **1.7** | **3.5** | Asymmetric Wave 1 vs. Wave 2 coding of influenza vaccination behavior in Study 2; 42 tests run without multiple-testing correction; invalid subgroup inference without $\text{Time} \times \text{Gender}$ interaction tests; unassessed attrition bias across $>74\%$ Wave 1 dropouts. |
| **2. Claim-to-Evidence Alignment** | **1.5** | **2.5** | Primary findings on influenza vaccine benefit/safety are well supported, but claims regarding actual influenza vaccine uptake, influenza disease severity (double-barreled item), childhood vaccine safety (confounded by general vaccine wording in Study 2), and gender differences are overstated. |
| **3. Data Integrity & Biological Plausibility** | **1.5** | **2.0** | Two-wave longitudinal panel design within the same individuals eliminates retrospective recall bias, and limitations regarding regional/cohort representativeness are transparently discussed, though attrition selection from Wave 1 to Wave 2 is left unquantified. |
| **4. Reproducibility & Data Integrity** | **1.6** | **2.0** | Ethical/legal data access procedures (Finnish privacy law / FinnBrain MTA and author contact) receive full credit under controlled-access rules, and full item means/SDs and wording are provided in Tables S1–S6; minor deductions for missing raw cell counts in categorical McNemar tables. |
| **Total Composite Score** | **6.3** | **10.0** | **Mixed / Salvageable** (Scientific Core Score: **4.7 / 8.0**) |
