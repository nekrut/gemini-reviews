# Review of ANON_131

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **6.8 / 10.0** (Mixed / Salvageable)  
* **Score Breakdown:** Rigor: 2.1/3.5 | Claims: 1.7/2.5 | Biology: 1.2/2.0 | Reproducibility: 1.8/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript uses `BharatSim`, an individual-level agent-based simulation framework, to model a two-step zoonotic spillover and early human-to-human transmission of highly pathogenic avian influenza (H5N1) in a synthetic rural Indian village of 9,667 residents (modeled on Namakkal district, Tamil Nadu). The model designates a single poultry workplace with 165 primary contacts (workers) and 476 secondary contacts (their household members), coupling a deterministic Susceptible–Infected–Dead (SID) avian outbreak model—or an area-matched constant force of infection (FOI) representing a wet market—to a stochastic human SEIR network model with lognormal latent ($\text{mean}=3\text{ d}, \text{SD}=1\text{ d}$) and infectious ($\text{mean}=7\text{ d}, \text{SD}=1\text{ d}$) periods across 12-hour home and work/school cycles. Across 500 stochastic runs per parameter set, the authors evaluate how avian culling timing, household quarantine thresholds (2 or 10 active cases), and targeted ring vaccination (1% or 5% of the population per day) affect the distribution of primary spillover cases, the reproductive number ($R_0$), the household secondary attack risk (SAR), and the tertiary attack risk (TAR). All simulation code and synthetic population files are publicly available on GitHub (`https://github.com/dpcherian/h5n1-spillover-model`).

The manuscript provides a well-structured, reproducible simulation framework that usefully contrasts peaked farm outbreaks against steady-state wet-market spillover risks and illustrates why locking down primary-contact households early ($QT=2$) elevates intra-household SAR while preventing tertiary community amplification. However, the quantitative conclusions regarding $R_0$ estimation and intervention effectiveness are affected by three modeling limitations: (1) computing $R_0$ solely from individuals who have recovered within 21 days of spillover introduces right-censoring bias toward shorter infectious periods and conflates the basic reproduction number ($R_0$) with the effective reproduction number under time-varying interventions ($R_c$); (2) the vaccination model assumes instantaneous (0-day lag) protective immunity and allocates 100 doses/day exclusively to the 641 primary and secondary contacts, immunizing the entire target pool in 6.4 days; and (3) case-triggered interventions assume zero diagnostic or reporting delay. Addressing these issues requires straightforward adjustments to the simulation estimators and sensitivity runs that can be executed directly within the authors' existing codebase.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Early avian culling prior to the peak of the bird force of infection substantially shifts the primary human spillover distribution toward zero, whereas farm (SID) and wet-market (constant FOI) scenarios diverge primarily at intermediate culling times: [Well Supported].**  
  The 500-run stochastic ensembles (Figure 3 and Appendix S5) and area-matched integral normalization between the peaked SID farm curve and flat wet-market FOI (Equation 2) cleanly demonstrate how the temporal profile of avian shedding interacts with culling timing to govern the probability of zero versus multiple human spillover events.

* **Quarantining all primary-contact households at a low case threshold ($QT=2$) increases household SAR but suppresses onward community transmission, whereas a higher threshold ($QT=10$) fails to prevent tertiary spread: [Moderately Supported].**  
  The trade-off shown in Figure 5—where confining primary contacts to their homes doubles their daily household exposure duration from 12 to 24 hours (increasing SAR) while severing links to workplaces and schools (preventing tertiary spread)—is mechanistically sound and consistent with prior household quarantine models. However, its practical effectiveness is overstated because the trigger ($QT=2$ active cases) assumes instantaneous, 100% sensitive case detection and immediate lockdown of all 165 farm workers' households without diagnostic lag or pre-symptomatic/mildly symptomatic shedding.

* **The basic reproductive ratio ($R_0$) can be accurately calibrated and inferred from the 21-day secondary attack risk (SAR) curve across no-intervention, vaccination, and quarantine scenarios: [Fragile].**  
  There are three methodological problems with the $R_0$ computation described in the Methods and plotted in Figures 4A and 5A:
  1. **Right-censoring bias:** With a $\text{lognormal}(3,1)$ latent period and $\text{lognormal}(7,1)$ infectious period (mean time from infection to recovery $\approx 10\text{ days}$), averaging secondary infections only over individuals who *have already recovered within 21 days of initial spillover* systematically selects for index and secondary cases who drew shorter-than-average sojourn times, biasing the estimator downward.
  2. **Conflation of $R_0$ with time-dependent effective reproduction number ($R_c$):** By definition, $R_0$ is a baseline pathogen/network property in a fully susceptible population without interventions. When vaccination starts on day 7 after case detection (Figure 4A) or quarantine triggers dynamically once 2 or 10 cases occur (Figure 5A), the population susceptibility and contact matrix change mid-window; the plotted quantity is a 21-day window-averaged effective/control reproduction number, not $R_0$.
  3. **Misattribution of co-exposed primary cases:** In the Methods, the authors note that when computing SAR they do not distinguish primary contacts infected by birds from those infected by other humans, and for $R_0$ they assign infectors by drawing at random from infectious individuals at the same location. If multiple farm workers are infected by the avian FOI or within multiple-worker households, random attribution among human co-workers/co-residents distorts the early human-to-human transmission estimate.

* **Targeted vaccination of primary and secondary contacts at 1% daily vaccination rate (DVR) substantially shifts the epidemic threshold while leaving SAR unchanged: [Overstated].**  
  A DVR of 1% of the village population ($N=9,667$) equals $\approx 97\text{–}100$ vaccines per day. Because the authors restrict vaccine eligibility exclusively to primary ($165$) and secondary ($476$) contacts ($641$ individuals total) and assume that *"the effect of the vaccine is immediate"*, 100% of the eligible target population is vaccinated within $6.4\text{ days}$ of campaign initiation (and within $1.3\text{ days}$ at $\text{DVR}=5\%$). In reality, human H5N1 vaccines require 10–14 days post-administration (and typically a two-dose prime-boost schedule) to elicit protective neutralizing titers. Ignoring the immunological ramp-up period overestimates how much a reactive vaccination drive starting 7 days after index detection can alter transmission within the first 21 days.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Correct the 21-Day Right-Censoring Bias and Separate $R_0$ from the Control Reproduction Number ($R_c$)
* **WHY:** Conditioning the reproduction number calculation on individuals who recover within 21 days of initial spillover preferentially samples shorter infectious periods and truncates secondary cases infected during week 2. Furthermore, labeling post-intervention reproduction numbers in Figures 4A and 5A as "$R_0$" is epidemiologically imprecise.
* **WHAT:** Compute true generation-based $R_0$ (for the index cohort without right-censoring truncation) and relabel the intervention curves in Figures 4A and 5A as the effective/control reproduction number $R_c$ (or $R_{\text{eff}}$).
* **HOW:** In `BharatSim`, track the complete secondary infection count of all generation-1 (primary human) and generation-2 (secondary human) cases until they recover—even if their recovery occurs after day 21—rather than truncating recovery at day 21. In addition, explicitly tag bird-to-human infections (`infector = BIRD`) so that human primary contacts infected by the avian FOI are never misassigned to a human infector at the farm workplace.

#### 2. Incorporate an Immunological Ramp-Up Delay in the Vaccination Model
* **WHY:** Assuming instantaneous 50% or 100% protection upon vaccine administration while delivering 100 doses/day to a pool of only 641 primary/secondary contacts means the entire ring is protected within 6 days, which is biologically unrealistic for an emerging H5N1 outbreak.
* **WHAT:** Add a realistic delay (e.g., 7 to 14 days) between vaccine administration and the onset of reduced susceptibility, and clarify in the text that 1% DVR of the total village ($97$ doses/day) saturates the 641 primary/secondary contacts in under one week.
* **HOW:** Modify the agent vaccination state transition in the codebase so that a vaccinated agent's susceptibility reduction ($\text{VE}$) takes effect $\tau_{\text{vac}} \in \{7, 14\}$ days after administration (or ramps linearly over 14 days), and plot the resulting $R_{\text{eff}}$ and epidemic curves alongside the instantaneous-protection upper bound in Figure 4.

#### 3. Add a Diagnostic/Reporting Lag to Case-Triggered Interventions
* **WHY:** Triggering village-wide quarantine of all 165 farm-worker households the instant the 2nd individual enters the `Infectious` compartment ($QT=2$) assumes perfect, zero-delay syndromic/molecular surveillance. With a 3-day latent period, a 3–5 day delay in symptom recognition and H5N1 laboratory confirmation allows tertiary workplace/school exposures to occur before quarantine begins.
* **WHAT:** Evaluate how a realistic detection delay ($\tau_{\text{det}} = 3\text{–}7\text{ days}$ after entering the `I` state, or triggering on hospitalization/severe symptoms) affects the $QT=2$ quarantine threshold in Figure 5.
* **HOW:** Add a detection lag parameter $\tau_{\text{det}}$ before an `I` agent is counted toward the quarantine threshold $QT$ (and before the 7-day vaccination timer starts), and report the critical detection delay beyond which $QT=2$ no longer keeps $R_{\text{eff}} < 1$.

#### 4. Technical, Mathematical, and Editorial Cleanup
* **WHY:** Multiple mathematical symbols and equations are missing or corrupted in the manuscript text and tables, and several grammatical typos appear in the Methods.
* **WHAT & HOW:**
  * **Missing Mathematical Symbols Across Text and Table 1:** Restore all dropped inline mathematical symbols in the manuscript conversion (e.g., $S_b, I_b, D_b$ in "Disease progression"; parameter symbols $\beta_{bh}, \beta_{bb}, R_0^b, N, \tau_E, \tau_I, \beta_{hh}$ in Table 1; Equations 1–5; and $R_0, \beta_{hh}, \beta_{bh}$ throughout the Results and Figure 3–5 captions).
  * **Methods ("Force of infection", paragraph 2):** Fix the typo *"applicable to a wet-market where birds and move in and out at constant rate"* to *"where birds move in and out at a constant rate"*.
  * **Methods ("Disease progression", paragraph 1):** Fix *"containing information about to the force of infection"* to *"containing information about the force of infection"*.
  * **Methods ("Parameters", paragraph 1):** Fix *"Since our interest in the trajectory of initial infections"* to *"Since our interest is in the trajectory of initial infections"*.
