# Forensic Peer Review: FEXP_ANON_116

**Overall Score:** **4.4 / 10.0** (Flawed / Overstated) | **Scientific Core Score:** **3.5 / 8.0**  
* **Score Breakdown:** Rigor: 1.1/3.5 | Claims: 1.1/2.5 | Biology: 1.3/2.0 | Reproducibility: 0.9/2.0

---

## 1. Blinded Metadata Perception

* **Manuscript ID:** `FEXP_ANON_116`
* **Perceived Domain & Topic:** Participatory Environmental Governance / Deliberative Democracy / Conservation Social Science; small-group online cross-cultural citizen dialogue between Taiwan and Japan on biodiversity conservation (GBF / SDGs 14, 15, 16) using the Scandinavian "reflecting" method.
* **Perceived Empirical Scope:** $N = 46$ paid adult participants ($n = 24$ Taiwanese, $n = 22$ Japanese; recruited via commercial survey panels) allocated into 6 Zoom breakout groups (8 participants per group, split into 4-person speaking/listening subgroups) for a single 3.5-hour weekend session in September 2024; pre- and post-dialogue self-report surveys analyzed via $\chi^2$ tests of independence, $\phi$ coefficients, and standardized mean differences ($d$), plus qualitative topic coding across 12 dialogue rounds.

---

## 2. Executive Summary & Editorial Verdict

This exploratory study conducts a 3.5-hour online citizen dialogue connecting 24 Taiwanese and 22 Japanese participants to discuss biodiversity conservation (Round 1, single-nationality subgroups) and citizen participation (Round 2, binational subgroups) using a structured "reflecting" facilitation protocol with consecutive translation. Comparing pre- and post-dialogue survey responses, the authors report increases in self-reported SDG knowledge, perceived urgency/significance of biodiversity conservation and citizen participation ($p < 0.10$), attitude toward dialogue, boundary of collaboration across 16 binary trust attributes ($d = 0.20\text{–}0.48$), and awareness of cultural inheritance for sustainability ($p < 0.05$ in Japanese participants). Based on these findings, the authors advocate institutionalizing cross-cultural online citizen dialogues within United Nations and CBD Global Biodiversity Framework decision-making processes.

**Editorial Verdict: Major Revision / Methodologically Flawed Statistical Inference (4.4 / 10.0).** While the qualitative logistics of organizing a bilingual, consecutively interpreted small-group deliberation across Taiwan and Japan are thoughtfully described and the authors candidly acknowledge sample-size and selection-bias caveats in the Limitations section, the quantitative pre–post analysis and headline claims in the Abstract and Conclusions suffer from fundamental statistical and experimental-design flaws:
1. **Invalid application of independent-samples tests ($\chi^2$ test of independence and independent-groups Cohen's $d$) to paired within-subject pre–post data:** All pre–post comparisons on the same $n = 24$ Taiwanese and $n = 22$ Japanese individuals were analyzed using Pearson's $\chi^2$ test of independence (treating pre and post responses as independent samples) and unpaired pooled-variance standardized mean differences ($d$), ignoring within-subject pairing, small expected cell counts ($<5$), 6-group breakout clustering, and multiple testing across dozens of survey items.
2. **Severe small-sample noise overinterpreted as "expanded boundary of collaboration" (Table 3):** Because $n = 24$ (Taiwan) and $n = 22$ (Japan) on binary `0/1` trust items, a change of $\pm 0.042$ (Taiwan) or $\pm 0.045$ (Japan) represents **literally 1 participant** switching their response, and a change of $0.083$ (Taiwan) or $0.091$ (Japan) represents **2 participants** switching their response ($d \approx 0.20$). Presenting noise from 1–3 individuals across 32 unadjusted binary comparisons without $p$-values or confidence intervals as empirical evidence that cross-cultural dialogue expands collaboration boundaries is statistically untenable.
3. **Confounding of pre-study SDG reading materials and domestic dialogue with the cross-cultural intervention:** Participants completed the pre-survey *before* reading a curated packet of SDG Goals 14–16 Voluntary National Review reports and biodiversity materials (line 74), and Round 1 was conducted in single-nationality groups (line 65). Without a control group (e.g., reading materials only or domestic-only dialogue), pre–post shifts in SDG recognition and biodiversity urgency cannot be attributed to cross-cultural reflecting dialogue.

### Assessment of Specific Claims

* **Claim 1 (The structured "reflecting" protocol enabled participants across all 6 breakout groups to listen and respond directly to Session 1 utterances during Session 2 with high participant satisfaction [45/46 "somewhat good" or "good"]): `[Well Supported]`.**  
  Table 2 (satisfaction ratings) and Table 4 (qualitative mapping of Session 1 topics to Session 2 reflective responses across Groups A–F) directly document that the facilitation and consecutive translation protocol functioned as intended.
* **Claim 2 (Cross-cultural dialogue improved self-reported awareness of cultural inheritance for sustainability and urgency/significance of biodiversity conservation and citizen participation): `[Fragile]`.**  
  First, the statistical tests used ($\chi^2$ test of independence on arbitrarily dichotomized 5-point scales at $p < 0.10$) are invalid for paired repeated-measures data. Second, because the pre-survey was administered prior to reading the pre-study SDG/biodiversity reading packet and prior to Round 1 (monocultural dialogue), the design cannot separate the effect of reading the briefing materials from the effect of cross-cultural interaction.
* **Claim 3 (Cross-cultural dialogue expanded the perceived boundary of collaboration measured by trust score/ratio across social attributes): `[Overstated]`.**  
  In Table 3, most reported "positive effects" ($d \approx 0.17\text{–}0.24$) correspond to just **2 out of 24** Taiwanese participants ($\Delta = +0.083$) or **2 out of 22** Japanese participants ($\Delta = +0.091$) changing a binary `0/1` answer, while several Taiwanese attributes moved in the opposite direction ($\Delta = -0.083$ for different religion and same ethnicity). No paired statistical tests (McNemar's test) or multiple-testing adjustments were performed across the 32 attribute comparisons.
* **Claim 4 (Cross-cultural online citizen dialogue should be institutionalized in formal collective decision-making processes of the United Nations and CBD COP): `[Overstated]`.**  
  While normative policy discussion is appropriate, grounding global institutional recommendations in a single 3.5-hour uncontrolled pilot study of 46 self-selected survey-panel respondents overreaches the empirical scope.

---

## 3. Forensic Defect Inventory

### Defect 1: Use of Independent-Samples Statistical Tests ($\chi^2$ and Unpaired $d$) on Paired Pre–Post Data and Arbitrary Dichotomization [ Pillar 3, Pillar 4 — Critical ]
* **Location:** Section "Data analysis" (line 131), Section "Results" (lines 159–161, 171, 195–197, 207), Figures 2, 3, 5, and Table 3.
* **Forensic Evidence:**
  1. **Independence violation in $\chi^2$ tests:** To test pre- vs. post-dialogue changes on the *same* 24 Taiwanese and 22 Japanese participants, the authors dichotomized the 5-point Likert items (collapsing 4 of the 5 categories vs. the extreme category) and computed Pearson's $\chi^2$ test of independence and $\phi$ (lines 159, 171, 207). Pearson's $\chi^2$ test assumes independent observations between rows (Pre vs. Post) and is invalid for paired within-subject measurements. Furthermore, collapsing 5-point ordinal scales into binary indicators discards ordinal information and produces sparse cells (e.g., 23/24 positive pre-dialogue listening attitude in line 166 leaves only 1 negative response, violating the $\chi^2$ minimum expected cell count of 5).
  2. **Unpaired Cohen's $d$ on binary proportions in Table 3:** Line 195 defines the standardized mean difference as $d = (\bar{X}_{\text{post}} - \bar{X}_{\text{pre}}) / \sqrt{(s_{\text{post}}^2 + s_{\text{pre}}^2)/2}$, which is the independent-samples formula ignoring within-subject covariance $\text{Cov}(X_{\text{pre}}, X_{\text{post}})$.
  3. **Granularity of $n = 24$ and $n = 22$ binary proportions:** In Table 3(a) ($n = 24$), $\Delta = 0.042$ is $1/24$ (1 person), $\Delta = 0.083$ is $2/24$ (2 people), and $\Delta = 0.208$ is $5/24$ (5 people). In Table 3(b) ($n = 22$), $\Delta = 0.045$ is $1/22$ (1 person), $\Delta = 0.091$ is $2/22$ (2 people), $\Delta = 0.136$ is $3/22$ (3 people), and $\Delta = 0.182$ is $4/22$ (4 people). For example, the highlighted increase in Taiwanese trust toward "different political orientation" ($\Delta = +0.083$, $d = 0.206$; line 197) is a net change of **2 individuals out of 24**, which is indistinguishable from random test–retest fluctuation ($p = 0.50$ or $0.625$ under McNemar's test), especially when Taiwanese trust toward "different religion" and "same ethnicity" simultaneously *decreased* by the exact same amount ($\Delta = -0.083$, $-2/24$).
* **Fix:** Replace all unpaired $\chi^2$ tests on dichotomized 5-point scales with paired **Wilcoxon signed-rank tests** (or cumulative link mixed models with participant and breakout-group random intercepts) on the full 5-point ordinal scales. For the 16 binary trust items in Table 3, apply **exact McNemar's tests** with Benjamini–Hochberg false discovery rate (FDR) correction across the 16 attributes, and report paired confidence intervals.

### Defect 2: Uncontrolled Experimental Design Confounding Pre-Study Reading Materials and Monocultural Dialogue with Cross-Cultural Dialogue [ Pillar 1, Pillar 2, Pillar 5 — Major ]
* **Location:** Section "Design of citizen dialogue" (lines 63, 65) and Section "Attitudinal data measurement" (line 74).
* **Forensic Evidence:**
  Line 74 states: *"A pre-survey was administered after instruction, and study materials were sent and before the initiation of the citizen dialogue. The participants were asked to answer the prequestionnaire before reading the study materials."* Between the pre-survey and post-survey, participants: (1) read Voluntary National Review reports on SDGs 14, 15, and 16 and country-specific biodiversity materials (line 63); (2) participated in Round 1 in **single-country** 4-person subgroups (all-Taiwanese or all-Japanese; line 65); and (3) participated in Round 2 in mixed binational subgroups. Because there was no intermediate survey after reading the materials or after Round 1, and no domestic-only control group, attributing pre–post changes in SDG knowledge (Fig. 1) or urgency/significance (Fig. 2) to *cross-cultural* reflecting dialogue is confounded.
* **Fix:** Explicitly state in the Abstract, Results, and Conclusions that the observed pre–post shifts reflect the combined package of pre-study SDG reading materials, domestic reflection (Round 1), and cross-cultural reflection (Round 2), and cannot isolate the causal effect of cross-cultural interaction from the briefing materials or domestic deliberation.

### Defect 3: Protocol Deviation in Group C, Truncated Tables 1 and 2, Arithmetic Discrepancy, and Contradictory Data Availability Statement [ Pillar 7 — Moderate ]
* **Location:** Lines 45, 54–60 (Table 1), 141–147 (Table 2), 166, 207 of chunk 1, and lines 88–92 vs. 124–126 of chunk 2.
* **Forensic Evidence:**
  1. **Truncated Table 1:** The caption of Table 1 states *"Gender and age group distribution of Taiwanese and Japanese participants. The number in parentheses show actual participants excluding absentees."* However, Table 1 only displays the Taiwanese sub-table ($N=24$) and completely omits the Japanese sub-table ($N=22$) as well as any parenthetical numbers.
  2. **Truncated Table 2:** The caption of Table 2 states *"Satisfaction and fairness assessment by participants. There is no answer for a Taiwanese participant on fairness assessment."* However, Table 2 only displays the Satisfaction columns and completely omits the Fairness assessment data.
  3. **Impossible percentage for $N = 22$ Japanese participants:** Line 166 reports that *"95.5% and 60.0% of Japanese participants in the current dialogue (before the dialogue) showed a positive self-reported attitude toward listening and speaking, respectively."* While $21/22 = 95.45\% \approx 95.5\%$, no integer numerator divided by $22$ (or $24$, or $21$) equals $60.0\%$ ($13/22 = 59.1\%$, $14/22 = 63.6\%$).
  4. **Corrupted symbol in text:** Line 207 reads *"and the effect size ( 538 )"*, where `(\phi coefficient)` was corrupted into `( 538 )`.
  5. **Contradictory Supplementary / Data Availability statements:** Lines 7, 65, 67, 74, and 88–92 cite `Supplementary file1 (PDF 398 KB)` containing Tables A1–A3, whereas the Data Availability Statement (line 126 of chunk 2) states: *"There are no supplementary materials."*

---

## 4. Quantitative Rubric Scoring

| Rubric Dimension | Score | Max | Diagnostic Justification |
| :--- | :---: | :---: | :--- |
| **1. Methodological & Statistical Rigor** | **1.1** | **3.5** | Uses independent-samples $\chi^2$ tests and unpaired Cohen's $d$ on paired pre–post within-subject data ($n=24, 22$); dichotomizes 5-point scales creating sparse cells; ignores breakout-group clustering and multiple testing across 32 trust comparisons; confounds pre-study reading materials with dialogue. |
| **2. Claim-to-Evidence Alignment** | **1.1** | **2.5** | Although the Limitations section appropriately notes that findings are exploratory hypotheses, the Abstract and Conclusions overstate 1–3 person binary shifts ($d \approx 0.2$) and $p < 0.10$ unpaired tests as empirical proof of expanded collaboration boundaries warranting UN institutionalization. |
| **3. Data Integrity & Biological Plausibility** | **1.3** | **2.0** | Transparent documentation of the facilitation protocol, translation workflow, honoraria, Group C role-assignment accident, and baseline comparison against $N=800$ national reference surveys. |
| **4. Reproducibility & Data Integrity** | **0.9** | **2.0** | Tables 1 and 2 are missing their second halves (Japanese demographics and fairness ratings); line 166 reports an impossible percentage ($60.0\%$ of $N=22$); line 207 has a corrupted symbol `( 538 )`; Data Availability contradicts the Supplementary Information section; raw data only available upon request. |
| **Total Composite Score** | **4.4** | **10.0** | **Flawed / Overstated** (Scientific Core Score: **3.5 / 8.0**) |
