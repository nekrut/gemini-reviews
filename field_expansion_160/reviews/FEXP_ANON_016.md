# Review of FEXP_ANON_016

**Overall Score:** **7.0 / 10.0** (Strong / Sound) | **Scientific Core Score:** **5.5 / 8.0**  
* **Score Breakdown:** Rigor: 2.0/3.5 | Claims: 1.8/2.5 | Biology: 1.7/2.0 | Reproducibility: 1.5/2.0

---

## 1. Blinded Metadata Perception
* **Anonymized Manuscript ID:** `FEXP_ANON_016`
* **Perceived Domain & Design:** One Health zoonotic seroepidemiology and Bayesian catalytic force-of-infection (`FOI`) modeling; cross-sectional multi-species study across 39 villages in northern Tanzania (2011–2016) analyzing $n = 9,476$ dentition-aged domestic ruminants (cattle, sheep, goats born strictly during the 2009–2015 inter-epidemic period) and $n = 558$ sympatric humans (`SEEDZ` cohort, 22 villages).
* **Blinding Integrity:** Double-blind review maintained; evaluated strictly on internal mathematical, biostatistical, and epidemiological merits at $t_0$.

---

## 2. Executive Summary & Editorial Verdict

This study investigates silent inter-epidemic circulation of Rift Valley fever virus (`RVFV`) in livestock and its association with human seropositivity across 39 villages in northern Tanzania between 2011 and 2016, following the major 2007–2008 East African outbreak. By restricting livestock serology ($n = 9,476$ cattle, goats, and sheep from the `BZ` and `SEEDZ` cross-sectional surveys) to animals aged $4\text{ months}$ to $5.5\text{ years}$ via dentition—thereby guaranteeing birth *after* the 2007–2008 epidemic—the authors fit Bayesian catalytic generalized linear mixed models (complementary log-log link in `JAGS`) adjusting for competitive ELISA diagnostic sensitivity and specificity ($85\%\text{–}98\%$ and $96\%\text{–}99\%$). They estimate an average annual livestock `FOI` of $3.0\%\text{–}4.0\%$, identify significant environmental drivers of village livestock `FOI` (lower elevation, banana cultivation, wetland/water proximity), and show via multivariable logistic regression (and Bayesian LASSO) on $n = 558$ humans ($8.2\%$ IgG seropositive) that human seropositivity is positively associated with village-level livestock `FOI` ($\text{OR} = 1.75$, 95% CrI $[1.22, 2.52]$), raw milk consumption ($\text{OR} = 2.53$, 95% CrI $[1.25, 5.29]$), and male sex ($\text{OR} = 2.07$, 95% CrI $[1.06, 4.13]$).

**Editorial Verdict: Minor Revision (Strong / Sound).** This is a well-conceived One Health epidemiological study whose use of dentition-aged livestock born after 2008 provides an elegant, definitive proof of substantial inter-epidemic `RVFV` transmission in domestic ruminants. The authors also deserve credit for running diagnostic sensitivity/specificity adjustments (Table 1) and candidly discussing the limitation that adult human IgG seropositivity reflects cumulative lifetime exposure (including the 2007–2008 outbreak) rather than purely inter-epidemic incidence (Discussion line 180). However, three concrete technical defects must be corrected before publication: (1) **all three mathematical equations in the Methods section (lines 43, 48, and 72) are completely missing/blank** after their introductory colons; (2) **Tables 1 and 2 contain multiple arithmetic and numerical transcription errors**—most notably Table 1 reporting a posterior mean and 95% CrI of `0.03 (0.08, 0.09)` where the lower credible bound (`0.08`) is nearly triple the point estimate (`0.03`), and Table 2 reporting male seropositivity as `27 / 258 (18.2%)` when $27 / 258 = 10.5\%$; and (3) **two-stage generated regressor bias** in the human logistic regression (Table 3), which plugs point estimates of village-level livestock `FOI` residuals (`Livestock FOI (village random effect)`, line 142) into the human model without propagating posterior estimation uncertainty from the first-stage catalytic model.

### Assessment of Specific Claims
* **Claim 1 (`RVFV` circulated endemically among livestock in northern Tanzania during the 2009–2015 inter-epidemic period, with an annual force of infection of $2\%\text{–}4\%$ and monotonically increasing seroprevalence from $4.4\%$ at age 1 year to $15.9\%$ at age 5 years): [Well Supported].**  
  Restricting the sample of $9,476$ cattle, goats, and sheep to animals whose dentition confirmed birth in or after 2009 eliminates carryover maternal antibodies ($<4\text{ months}$ excluded) and 2007–2008 epidemic cohorts. The catalytic age-seroprevalence curve (Fig. 3) and imperfect-test sensitivity analyses (Table 1) robustly establish ongoing inter-epidemic transmission.
* **Claim 2 (Raw milk consumption [$\text{OR} = 2.53$, 95% CrI $1.25\text{–}5.29$] and male sex [$\text{OR} = 2.07$, 95% CrI $1.06\text{–}4.13$] are independent behavioral/demographic risk factors for human `RVFV` seropositivity): [Well Supported].**  
  Both multivariable hierarchical logistic regression and the 18-variable Bayesian LASSO (`Fig. 4`) consistently identify raw milk consumption as the strongest dietary/behavioral predictor of human IgG seropositivity.
* **Claim 3 (Human seropositivity is positively associated with village-level inter-epidemic livestock `FOI` [$\text{OR} = 1.75$, 95% CrI $1.22\text{–}2.52$], supporting zoonotic spillover during the inter-epidemic period): [Moderately Supported].**  
  While the spatial correlation between village livestock `FOI` (2009–2015) and human IgG prevalence is clear, **0 of 33 children aged $<12\text{ years}$** (the human cohort born during or just before the inter-epidemic period; Table 2 line 127) were seropositive (`0 / 33 [0.0%]`), and all seropositive humans were adults or adolescents exposed to the massive 2007–2008 epidemic (plus earlier outbreaks). Because ecologically permissive low-elevation, wet villages experience *both* higher inter-epidemic livestock `FOI` and more intense epidemic outbreaks, spatial correlation between adult human IgG and 2009–2015 livestock `FOI` is partially confounded by persistent village-level environmental risk across epidemic and inter-epidemic eras (as the authors thoughtfully acknowledge in Discussion line 180).

---

## 3. Forensic Defect Inventory

1. **Pillar 5 & 7 Violation — Missing Mathematical Equations in the Methods Text (Lines 43, 48, and 72):**  
   In three separate places in Materials and Methods, the text introduces a mathematical equation with a colon followed by blank space where the equation was dropped:
   * **Line 43:** *"Assuming a constant FOI over time, cohort prevalence, $P_a$, at age $a$ is given as [ 30 ]:"* $\to$ **(Equation missing)**.
   * **Line 48:** *"Age-specific seroprevalence sits at the intersection of two axes... (Fig 1) with force of infection (FOI) epochs mapping directly onto the year-specific peeling parameters in a catalytic framework as [ 41 ]:"* $\to$ **(Equation missing)**.
   * **Line 72:** *"In order to account for a test with known sensitivity ($Se$) and specificity ($Sp$), the following equation was used to adjust obtaining test positive results ($p_a$) given a cohort's true seroprevalence ($P_a$), test sensitivity and specificity following equation [ 52 ]:"* $\to$ **(Equation missing; i.e., Rogan-Gladen relation $p_a = P_a \cdot Se + (1 - P_a)(1 - Sp)$)**.
2. **Pillar 5 Violation — Impossible Credible Interval in Table 1 and Multiple Percentage/Count Arithmetic Errors in Table 2 (Lines 105 and 126–134):**  
   * **Table 1 (line 105):** Under `Specificity = 96%` and `Sensitivity = 85%`, the posterior mean and 95% CrI of the average livestock `FOI` is printed as **`0.03 (0.08, 0.09)`**. A posterior point estimate (`0.03`) cannot lie outside and below its own 95% credible interval (`0.08, 0.09`)! (Likely `0.08 (0.03, 0.09)` or `0.03 (0.02, 0.04)`).
   * **Table 2 Gender row (line 130):** Male human seropositivity is printed as **`27 / 258 (18.2%)`**. However, $27 / 258 = \mathbf{10.47\%}$ ($\approx 10.5\%$), *not* $18.2\%$! ($18.2\%$ appears to be a copy-paste error from the `>61 years` age row `10 / 55 (18.2%)` immediately above it).
   * **Table 2 Count & Percentage discrepancies (lines 126–132):** The text (line 122) states that $46$ of $558$ humans were seropositive ($46 / 558 = 8.2\%$). While Gender (`19 + 27 = 46`) and Milk (`12 + 34 = 46`) sum to 46 seropositives, the Age rows (`0 + 3 + 18 + 14 + 10 = 45`) and Animal Slaughter rows (`13 + 32 = 45`) sum to only **45** seropositives (with no missing-data footnote). Furthermore, in line 131, `Animal slaughter = No` is printed as `13 / 304 (4.6%)`, whereas $13 / 304 = \mathbf{4.28\%}$ ($\approx 4.3\%$).
3. **Pillar 2 & 3 Violation — Two-Stage Generated Regressor Uncertainty Omission in the Human Seropositivity Model (Methods Line 82; Table 3 Line 142):**  
   In the human logistic regression (Table 3), the primary exposure variable `Livestock FOI (village random effect)` is the point estimate (posterior mean/median residual) extracted from the first-stage livestock catalytic GLMM (line 82). Because village sample sizes vary and village-level random effects have substantial posterior variance, plugging first-stage point estimates into a second-stage regression without propagating their posterior distributions (or jointly fitting the livestock and human likelihoods in `JAGS`) underestimates the standard error and narrows the 95% CrI of the livestock `FOI` odds ratio ($\text{OR} = 1.75$, $[1.22, 2.52]$) while inducing attenuation bias in the point estimate.

---

## 4. Quantitative Rubric Scoring

| Rubric Dimension | Score | Max | Forensic Justification |
| :--- | :---: | :---: | :--- |
| **1. Methodological & Statistical Rigor** | **2.0** | **3.5** | Rigorous Bayesian catalytic GLMM with imperfect test sensitivity/specificity adjustment on $n=9,476$ dentition-aged livestock, plus Bayesian LASSO; penalized for missing equations in text, Table 1/2 arithmetic errors, and two-stage unpropagated uncertainty in the human regression. |
| **2. Claim-to-Evidence Alignment** | **1.8** | **2.5** | Claims of inter-epidemic livestock transmission and raw milk risk are strongly supported; the human-livestock `FOI` association is appropriately caveated regarding cumulative adult exposure vs. inter-epidemic incidence. |
| **3. Data Integrity & Biological/Behavioral Plausibility** | **1.7** | **2.0** | High biological plausibility and clever use of dentition aging to isolate post-2008 livestock cohorts across 39 villages. |
| **4. Reproducibility & Data Integrity** | **1.5** | **2.0** | Data archived at University of Glasgow (`10.5525/gla.researchdata.1239`), but all three mathematical equations in the Methods section are missing and Tables 1–2 contain numerical transcription errors. |
| **Total Composite Score** | **7.0** | **10.0** | **Strong / Sound** (Scientific Core Score: **5.5 / 8.0**) |

---

### Constructive and Doable Suggestions for Improvement

1. **Restore the Three Missing Mathematical Equations in Materials and Methods (Lines 43, 48, and 72):**  
   * **WHY:** Currently, lines 43, 48, and 72 end with colons followed by blank lines where the catalytic `FOI` equations and the Rogan-Gladen imperfect-test adjustment equation were omitted.  
   * **WHAT & HOW:** Insert the explicit mathematical formulas for constant-`FOI` cohort seroprevalence $P_a = 1 - \exp(-\lambda a)$ (line 43), time-varying catalytic `FOI` $P_a = 1 - \exp(-\sum_{t} \lambda_t \Delta t)$ with clog-log link $\log(-\log(1 - P_{i,a})) = \dots$ (line 48), and test-adjusted apparent prevalence $p_a = P_a \cdot Se + (1 - P_a)(1 - Sp)$ (line 72).
2. **Correct the Numerical and Arithmetic Errors in Table 1 and Table 2:**  
   * **WHY:** In Table 1 (line 105), `0.03 (0.08, 0.09)` has a lower 95% CrI bound higher than the mean. In Table 2 (line 130), Male seropositivity `27 / 258` is listed as `18.2%` instead of `10.5%`, and Age/Slaughter seropositive counts sum to 45 instead of 46.  
   * **WHAT & HOW:** Verify the posterior summary for `Sp = 96%, Se = 85%` in Table 1, recalculate the exact percentages in Table 2 (`27/258 = 10.5%`, `13/304 = 4.3%`), and add a footnote explaining the 1 missing observation in Age and Animal Slaughter.
3. **Propagate Posterior Uncertainty of Village-Level Livestock `FOI` into the Human Logistic Regression:**  
   * **WHY:** Treating estimated village random effects from the livestock model as fixed, known covariates in the human model (Table 3) ignores first-stage estimation error.  
   * **WHAT & HOW:** Since both models are already implemented in `JAGS`, either link the livestock catalytic model and human logistic regression jointly in a single `JAGS` model where the latent village random effect $u_v$ enters both likelihoods, or draw village `FOI` values across the posterior MCMC iterations (`multiple imputation` across posterior draws) when fitting the human model.
