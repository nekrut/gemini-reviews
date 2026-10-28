# Review of ANON_93

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **4.3 / 10.0** (Flawed / Overstated)  
* **Score Breakdown:** Rigor: 1.2/3.5 | Claims: 1.1/2.5 | Biology: 0.9/2.0 | Reproducibility: 1.1/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This short report screens 9,144 archived serum samples collected between 4 November 2019 and 16 March 2020 from adults in the French nationwide `CONSTANCES` cohort for anti-SARS-CoV-2 antibodies. Samples were first tested using a commercial anti-Spike S1 IgG ELISA (`Euroimmun`, positive optical density ratio $\ge 1.1$, indeterminate $0.8\text{--}1.1$). All sera with $\text{ELISA-S} \ge 0.7$ were subsequently tested with an in-house live-virus cytopathic effect microneutralization (`SN`) assay in six replicates (positive titer $\ge 40$). Overall, 353/9,144 (3.9%) participants were `ELISA-S` positive and 44 (0.48%) were `SN` positive. Focusing on 13 participants sampled between 5 November 2019 and 30 January 2020 who were positive on both `ELISA-S` and `SN`, the authors conducted retrospective telephone interviews in 11 individuals and concluded that SARS-CoV-2 was already circulating in France as early as November 2019. Individual-level data are restricted under French CNIL regulations.

While leveraging a large national biobank to investigate early pandemic circulation is an important epidemiological objective, the conclusion that SARS-CoV-2 circulated in France in early November 2019 is not adequately supported because the study fails to account for assay false-positive rates at near-zero pre-test prevalence and omits pre-pandemic negative control sera from the same biobank. Specifically, the `ELISA-S` positivity rate in November 2019 (1.9%, 42/2,218) and December 2019 (1.3%, 20/1,534) reflects the known ~1.5–2.0% false-positive rate of the Euroimmun S1 IgG assay at the 1.1 cutoff, and the proportion of dual `ELISA-S+ / SN+` samples remained completely flat across November 2019 (7/2,218 = 0.32%), December 2019 (3/1,534 = 0.20%), and January 2020 (3/2,268 = 0.13%) rather than exhibiting epidemic growth. Because IgG seroconversion requires 2–3 weeks post-infection, the seven November 2019 cases would imply widespread community transmission in France in mid-October 2019, which conflicts with viral phylodynamic and hospital surveillance evidence. Testing blinded pre-2019 `CONSTANCES` control sera in parallel and formally calculating the Bayesian positive predictive value (PPV) are essential to distinguish true early infections from cross-reactive false positives.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Thirteen dual `ELISA-S`-positive and `SN`-positive sera collected between 5 November 2019 and 30 January 2020 demonstrate early circulation of SARS-CoV-2 in France starting in November 2019: [Fragile].**  
  Seven of the 13 dual-positive samples were collected in November 2019 (starting 5 November 2019; Table 1), 3 in December 2019, and 3 in January 2020. Because IgG and neutralizing antibodies take 14–21 days to develop after infection, a positive serum on 5 November 2019 requires infection in mid-October 2019. More importantly, the dual-positivity rate did not rise between November 2019 (0.32%), December 2019 (0.20%), and January 2020 (0.13%), which is the statistical hallmark of a constant baseline assay false-positive rate ($\sim 0.2\%$) rather than an expanding infectious outbreak. In addition, 10 of the 13 samples had the minimum positive `SN` titer of 40, and 11 of the 13 had `ELISA-S` ratios below the 2.5 threshold required for 100% `ELISA-S` specificity (Discussion, line 76).

* **Sequential confirmation of `ELISA-S` ($\ge 1.1$) with `SN` ($\ge 40$) eliminates false positives because `SN` had 100% specificity in external 2017–2018 blood donor controls: [Overstated].**  
  First, the authors did not include any pre-2019 negative control sera from the `CONSTANCES` biobank (which has collected sera since 2012) blinded within the same laboratory runs. Second, even if an assay observed 0 false positives in, say, 1,000 external pre-pandemic blood donors, the upper 95% Clopper–Pearson confidence bound on the false-positive rate is $0.37\%$, which in 5,920 samples collected between November 2019 and January 2020 would yield up to 22 false positives. Third, `SN` specificity was not evaluated *conditionally* on sera pre-selected for cross-reactive anti-coronavirus S1 IgG binding ($\text{ELISA-S} \ge 0.7$), where cross-reactive seasonal human coronavirus (HCoV-OC43, HCoV-HKU1, HCoV-NL63, HCoV-229E) antibodies or non-specific serum factors can correlate across both assays.

* **Retrospective interviews in 11 of the 13 positive participants reveal symptoms or exposure histories supporting early SARS-CoV-2 infection: [Overstated].**  
  The interviews were conducted unblinded without a matched control group of seronegative `CONSTANCES` participants sampled in the same weeks. Six of the 11 interviewed participants reported no symptoms at all (line 39; Table 1), and three November 2019 cases (#1, #2, #5, all with borderline $\text{SN} = 40$) reported neither symptoms nor any exposure risk factors. In the remaining participants, non-specific respiratory symptoms in autumn/winter (e.g., cough or febrile illness in October–November 2019, or travel to Spain or Rome in autumn 2019) are common in the general population during seasonal respiratory virus circulation and subject to retrospective recall bias.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Assay Blinded Pre-2019 `CONSTANCES` Biobank Sera to Empirically Calibrate the Joint False-Positive Rate
* **WHY:** Because `CONSTANCES` collected and stored serum samples using the exact same pre-analytical protocol starting in 2012, the biobank contains ideal internal negative controls. Relying on historical specificity estimates from external blood donor cohorts fails to control for matrix effects, storage duration, and conditional dependence between `ELISA-S` ($\ge 0.7$) and `SN` ($\ge 40$).
* **WHAT:** Test a matched set of pre-2019 `CONSTANCES` sera (e.g., $n = 1,500\text{--}2,000$ samples from November 2017–January 2018 or November 2018–January 2019) using the identical two-step `ELISA-S` ($\ge 0.7$) + `SN` ($\ge 40$) pipeline.
* **HOW:** Randomize and blind pre-2019 `CONSTANCES` aliquots alongside the 2019–2020 samples (or run them under identical lot/operator conditions), record the exact proportion of pre-2019 samples meeting $\text{ELISA-S} \ge 1.1$ and $\text{SN} \ge 40$, and compare the November 2019–January 2020 dual-positive rate (13/6,020 = 0.22%) against the empirical pre-2019 false-positive rate using an exact Fisher or binomial test.

#### 2. Compute Formal Bayesian Positive Predictive Values (PPV) and Rohan–Gladen Prevalence Adjustments
* **WHY:** When true disease prevalence $p$ is extremely low (e.g., $p < 10^{-4}$ in November 2019), even a two-step test with 99.8% joint specificity produces mostly false positives ($\text{PPV} = \frac{\text{Se} \cdot p}{\text{Se} \cdot p + (1 - \text{Sp})(1 - p)} < 5\%$).
* **WHAT:** Report the joint sensitivity/specificity confidence intervals and calculate the PPV and Rogan–Gladen adjusted seroprevalence for each month from November 2019 to March 2020.
* **HOW:** Using the binomial 95% confidence interval for joint specificity $\text{Sp}_{\text{joint}}$ (accounting for uncertainty in the 2017–2018 donor validation size $N_{\text{control}}$), plot the posterior probability that at least $k$ of the 7 November 2019 and 3 December 2019 positives are true positives across plausible prior prevalence values ($10^{-5}$ to $10^{-2}$), and stratify the monthly trend test (Figure 1) by `SN` confirmation status and by the high-specificity $\text{ELISA-S} \ge 2.5$ cutoff.

#### 3. Perform Multi-Antigen Confirmation (Anti-Nucleocapsid and Anti-RBD IgG) on the 13 Sera
* **WHY:** Ten of the 13 sera had borderline neutralization titers ($\text{SN} = 40$) and 11 had moderate `ELISA-S` ratios ($1.16\text{--}2.01$). True post-infection convalescent sera frequently target multiple SARS-CoV-2 antigens (Nucleocapsid, RBD, and S2), whereas false positives on S1 ELISA are rarely positive on orthogonal Nucleocapsid assays.
* **WHAT:** Test the 13 candidate sera (and pre-2019 controls) on orthogonal anti-Nucleocapsid (anti-N) and anti-RBD IgG assays, and assess cross-reactivity against seasonal human coronaviruses (HCoV-OC43, HKU1, NL63, 229E).
* **HOW:** Run the remaining serum volume of the 13 samples on a validated anti-N and anti-RBD multiplex immunoassay (e.g., Roche Elecsys anti-SARS-CoV-2 N or Meso Scale / Luminex multiplex panel including the four seasonal HCoVs) and add the anti-N, anti-RBD, and seasonal HCoV titers to Table 1.

#### 4. Compare Interview Responses Against Matched Seronegative Controls and Temper Claims
* **WHY:** Without knowing how often seronegative `CONSTANCES` participants sampled in November–December 2019 also recall a partner's cough, febrile illness, or travel within Europe, the anecdotal descriptions in Table 1 have no diagnostic specificity.
* **WHAT:**Either report baseline symptom/travel frequencies from matched seronegative `CONSTANCES` participants or reframe the interview findings as descriptive and non-confirmatory.
* **HOW:** Query the standard `CONSTANCES` follow-up questionnaires (or interview 3–4 age-, sex-, and week-matched seronegative controls per case) to report the background rate of autumn respiratory symptoms, and revise the Abstract and Discussion to state that false-positive cross-reactivity cannot be excluded for the November–December 2019 samples.

#### 5. Technical, Arithmetic, and Editorial Corrections
* **WHY:** Sample counts in the Results do not add up to the cohort total of 9,144, and a key date is misprinted by a full year.
* **WHAT & HOW:**
  1. **Sample count discrepancy (Results, line 39):** The `SN` breakdown states *"detected in 44 (0.48%) participants... undetermined in 15 participants, negative in 498 and not done in 8597"*. However, $44 + 15 + 498 + 8,597 = 9,154$, which is 10 more than the 9,144 total samples stated in the Abstract and line 22. Audit and correct the exact counts for each category in the text and Figure 2.
  2. **Date error for Participant #7 (Results, line 39):** Correct *"participant #7 who was tested positive on Nov 29, 2020 had a second serological sample collected in July 2020"* to *"Nov 29, 2019"* (matching `2019-11` in Table 1, line 62).
  3. **Typo in March positivity fraction (Results, line 31):** Change `"6.7% (63 or 945)"` to `"6.7% (63 of 945)"`.
