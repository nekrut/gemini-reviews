# Review of OOD_ANON_21

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **7.3 / 10.0** (Strong / Sound)  
* **Score Breakdown:** Rigor: 2.3/3.5 | Claims: 1.8/2.5 | Biology: 1.7/2.0 | Reproducibility: 1.5/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This study analyzes a 9-year light-level geolocator dataset (274 post-breeding migrations from 145 individuals between 2010 and 2018) to investigate how individual behavioral plasticity and population turnover contribute to a northward range shift in the Critically Endangered Balearic shearwater (*Puffinus mauretanicus*). Using Gaussian mixture models to classify post-breeding destinations into southern (Iberian) and northern (Biscay/Brittany) areas and subject-centering linear mixed models (van de Pol & Wright's method), the authors report a northward shift of $0.2317^\circ/\text{year}$ best explained by July–August sea-surface temperature ($\Delta\text{AICc} = -10.85$), driven at least in part by within-individual flexibility ($0.662^\circ/\text{^\circ C}$, $P = 0.044$). They further show that birds migrating further north return faster ($0.207\text{ km/h per } 1^\circ$ within individuals), that speed during the initial 25% of the return journey is better predicted by coastal sea-route distance than beeline distance ($\Delta\text{AICc} = -5.00$), and that return arrival in the Mediterranean is nevertheless delayed by $4.4\text{ days per } 1^\circ$ of maximum latitude. Processed tracking data are publicly archived on Figshare.

This is a valuable longitudinal tracking dataset addressing an important evolutionary and behavioral question, strengthened by thoughtful spatial controls for geolocator latitudinal noise and habitat confounds (testing speed within the shared $35^\circ\text{N}–45^\circ\text{N}$ latitudinal corridor). However, the statistical presentation has several methodological flaws that need correction: (1) the headline linear regression test of the northward shift ($F_{4,93} = 108.55, P < 10^{-15}$) reports the omnibus 4-degree-of-freedom full-model $F$-statistic—which is overwhelmingly driven by the binary northern/southern `area` covariate defined from the response variable itself—rather than the single-degree-of-freedom test for `year`; (2) `area` is derived by applying a mixture model to `median latitude` and then entered as a fixed covariate predicting `median latitude` (and erroneously listed as a fixed effect predicting itself in Table 1); (3) the initial-25% return speed model ($F_{1,272} = 8.931$) omits the individual random intercept, pseudoreplicating repeated migrations from the same birds; and (4) the conclusion that turnover does not contribute to the latitudinal shift rests on an underpowered difference test between a between-individual slope ($1.421^\circ/\text{^\circ C}$) that is more than twice the within-individual slope ($0.662^\circ/\text{^\circ C}$). All of these issues can be resolved through statistical re-analysis and textual revision using the existing dataset.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Post-breeding migratory latitude shifted northward over 2010–2018 and tracks sea-surface temperature better than calendar year: [Moderately Supported].**  
  While the positive trend with year ($0.2317 \pm 0.0734^\circ/\text{year}$) and the superior fit of the SST model ($\Delta\text{AICc} = -10.85$) are plausible, the reported test statistic ($F_{4,93} = 108.5515, P < 1 \times 10^{-15}$) is the omnibus $F$-test for all four predictors combined (`year`, `area`, `sex`, and `island`), where `area` is a binary split of the response variable (`median latitude`) separating Iberia ($\sim 39^\circ\text{N}$) from Brittany ($\sim 47^\circ\text{N}$). Moreover, the residual degrees of freedom ($\text{df} = 93$, implying $n = 98$ birds) indicate that 47 of the 145 tracked individuals were silently dropped (likely due to missing sex data).

* **Within-individual phenotypic flexibility contributes to the northward shift within migratory areas, whereas individual turnover does not: [Overstated].**  
  The within-individual slope is statistically significant ($\beta_W = 0.662 \pm 0.65^\circ\text{ latitude per }^\circ\text{C}$, $\chi^2_1 = 4.063, P = 0.044$), supporting a plastic component. However, the between-individual slope is more than double the within-individual slope ($\beta_B = 1.421 \pm 0.80^\circ/\text{^\circ C}$, $\chi^2_1 = 12.07, P = 0.001$). Concluding that "phenotypic flexibility in migratory latitude, but not turnover of individuals, has a detectable contribution" because the 95% CI of $(\beta_B - \beta_W)$ spans $[-0.262, 1.763]$ conflates low statistical power to detect a slope difference of $+0.76^\circ/\text{^\circ C}$ with evidence against turnover.

* **Return migration speed increases with maximum latitude within individuals and is adjusted during the first 25% of the return trip based on sea-route distance: [Moderately Supported].**  
  The subject-centered mixed model for overall return speed ($\beta_W = 0.207\text{ km/h per } 1^\circ$, $P = 0.044$) and the control analysis restricted to the $35^\circ\text{N}–45^\circ\text{N}$ band ($0.218\text{ km/h per } 1^\circ$, $P = 0.012$) are well designed. However, the model comparing route distance, beeline distance, and maximum latitude during the initial 25% of return migration ($F_{1,272} = 8.931, P = 0.00306$) was fitted as an ordinary least-squares regression across all 274 tracks without an individual random effect, treating repeated tracks from the same 145 birds as independent.

* **Migrating further north delays return arrival into the Mediterranean Sea within individuals despite faster return travel: [Well Supported].**  
  Both within-individual ($4.4 \pm 1.4\text{ d per } 1^\circ$, $\chi^2_1 = 42.53, P < 10^{-10}$) and between-individual ($5.4 \pm 1.0\text{ d per } 1^\circ$, $\chi^2_1 = 81.78, P < 10^{-15}$) slopes are large, tightly estimated, and consistent across statistical specifications.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Report Partial Test Statistics for `Year` and `SST` and Account for Excluded Individuals
* **WHY:** In the first-migration linear regression (`median latitude ~ year + area + sex + island`), $F_{4,93} = 108.55$ tests the joint null hypothesis that all four coefficients equal zero. Because `area` was created by dichotomizing `median latitude`, `area` alone accounts for almost all of that $F$-ratio, grossly inflating the apparent significance ($P < 10^{-15}$) attributed to the yearly trend. Additionally, $4 + 93 + 1 = 98$ observations means 47 of the 145 individuals were omitted without explanation.
* **WHAT:** Report the single-degree-of-freedom $t$- or $F_{1,93}$-statistic and exact $P$-value specifically for the `year` coefficient, clarify whether $\pm 0.07339^\circ$ is a standard error or 95% confidence interval, and report a sensitivity model dropping the non-significant `sex` term so all 145 individuals can be included.
* **HOW:** Extract `summary(lm_model)$coefficients["year", ]` and `drop1(lm_model, test = "F")` in R, state the exact sample size ($n = 98$ sexed individuals vs. $n = 145$ total individuals), and verify that $\Delta\text{AICc}$ between the `year` and `SST` models is computed on identical sample sizes.

#### 2. Remove Endogenous `Area` Conditioning in Sensitivity Models and Fix Table 1
* **WHY:** Defining `area` via a 3-year-batched Gaussian mixture model on `median latitude` and then including `area` as a fixed effect when modeling `median latitude` introduces circular conditioning: if the mixture boundary shifts across the three 3-year batches (2010–2012, 2013–2015, 2016–2018), part of the latitudinal shift is absorbed or distorted by the batch-specific classification. Furthermore, Row 3 of Table 1 lists `area` as a fixed effect in the binomial GLMM whose response variable is `Log odds of migrated to the northern area`.
* **WHAT:** (1) Remove `area` from the fixed-effects column of Row 3 in Table 1. (2) Re-fit the subject-centered mixed model for `median latitude` using a single time-invariant latitudinal cutoff (e.g., the overall antimode at $\sim 43.5^\circ\text{N}$) to define northern vs. southern tracks, and also report the unconditioned within-individual slope across birds that never switched areas.
* **HOW:** Classify northern vs. southern migrations using a fixed threshold across all years (`median_lat > 43.5`), re-estimate the `lme4` model `median_lat ~ SST_between + SST_within + area_fixed + sex + (1|bird_id)`, and compare the resulting $\beta_W$ and $\beta_B$ estimates.

#### 3. Include Individual Random Intercepts in the Initial-25% Return Speed Models
* **WHY:** The analysis of initial return speed (Results line 63; $F_{1,272} = 8.931$) uses $\text{df} = 272$, indicating that all 274 migrations from 145 individuals were pooled in a simple linear regression without accounting for repeated measures per bird or area/outbound speed covariates.
* **WHAT:** Re-fit the three competing spatial representation models (route distance, beeline distance, and maximum latitude) as linear mixed-effects models with `(1 | Individual)` random intercepts, and apply van de Pol & Wright subject-centering to route distance.
* **HOW:** Run `lmer(initial_speed ~ route_dist + (1 | Individual), REML = FALSE)` (and analogous models for `beeline_dist` and `max_lat`) in `lme4`, recompute $\text{AICc}$ across the three models, and report the within- and between-individual slopes for route distance.

#### 4. Temper Claims Eliminating Individual Turnover in Latitudinal Range Shift
* **WHY:** The point estimate for the between-individual temperature slope ($1.421^\circ/\text{^\circ C}$) is more than twice the within-individual slope ($0.662^\circ/\text{^\circ C}$), and the 95% CI of their difference ($-0.262$ to $1.763^\circ/\text{^\circ C}$) is compatible with substantial cohort turnover contributing alongside plasticity.
* **WHAT:** Revise the Results (line 44) and Discussion (lines 83–84) to state that while within-individual plasticity significantly contributes to the northward shift, a parallel contribution from between-individual turnover cannot be ruled out given the larger point estimate of the between-individual slope and wide confidence interval of the difference.
* **HOW:** Replace "suggesting that phenotypic flexibility in migratory latitude, but not turnover of individuals, has a detectable contribution" (line 44) with "demonstrating a statistically significant contribution of within-individual phenotypic flexibility, while a concomitant contribution of between-individual turnover ($\beta_B - \beta_W = 0.759^\circ/\text{^\circ C}$, 95% CI: $-0.262, 1.763$) cannot be excluded."
