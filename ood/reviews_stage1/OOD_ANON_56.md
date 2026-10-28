# Review of OOD_ANON_56

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **8.4 / 10.0** (Strong / Sound)  
* **Score Breakdown:** Rigor: 2.9/3.5 | Claims: 1.9/2.5 | Biology: 1.7/2.0 | Reproducibility: 1.9/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This macroecological study evaluates the relative roles of land-use change, climate extremes, national governance/socioeconomics, and species traits in driving population abundance trends across 1,123 populations of 50 large mammalian carnivore species (families Canidae, Felidae, Hyaenidae, and Ursidae) spanning 75 countries between 1970 and 2015, compiled from the CaPTrends and Living Planet databases. The authors first estimate annual instantaneous rates of change ($r_t$) for 985 quantitative time series using log-linear regressions with a continuous Ornstein-Uhlenbeck (OU) autoregressive error structure, and integrate 138 qualitative trend records ("Increase," "Stable," "Decrease") into a unified hierarchical Bayesian linear mixed-effects model in JAGS using interval-censored response priors and observation quality weights. Accounting for phylogenetic (species nested in genus) and spatial (country nested in UN subregion) random intercepts, covariate imputation uncertainty, and Kuo-Mallick variable selection across 16 main covariates and 7 interactions (tested across 0-, 5-, and 10-year temporal lags), they find that local primary habitat loss and national rate of change in the Human Development Index (HDI) are negatively associated with carnivore trends, whereas extreme heat declines are buffered inside protected areas. Counterfactual analyses and space-for-time abundance projections suggest that rapid socioeconomic growth drives sharp initial carnivore declines, followed by potential recovery once HDI growth decelerates below $\sim 1.2\%$ per year. All data sources and JAGS/R code are publicly archived on Zenodo and in the Source Data file.

This is a statistically rigorous, transparently documented study that sets a high standard for macroecological synthesis by propagating covariate imputation uncertainty, controlling for temporal autocorrelation via an OU process, checking spatial and phylogenetic residual autocorrelation, and incorporating qualitative records via interval censoring to reduce geographic bias toward the Global North. The primary limitations are causal and structural: (1) the headline claim that "human socioeconomic development is more associated with carnivore population declines than habitat loss or climate change" in the counterfactual analysis (Figure 4) is partly an artifact of comparing a national-scale covariate with a non-zero positive change in virtually every country (HDI growth) against local covariates whose historical changes in the sampled buffer zones were highly zero-inflated (only 6% of studied populations experienced $\ge 5\%$ primary habitat loss); (2) the two-stage estimation (fitting OU regressions to extract $r_t$ point estimates, then using $a\text{ posteriori}$ quality weights rather than propagating the exact standard error of each $r_t$ slope into the second-stage Bayesian model); and (3) the ecological fallacy of linking national-level HDI growth rates to local carnivore populations while assuming a space-for-time Kuznets-like trajectory without modeling historical baseline extirpations. These caveats are largely acknowledged by the authors in the text and can be further strengthened through targeted sensitivity analyses and nuanced framing.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Primary habitat loss is consistently associated with local carnivore population declines regardless of ecological specialization or replacement land cover, while protected area coverage buffers against extreme temperature anomalies: [Well Supported].**  
  The hierarchical Bayesian model shows a clear negative posterior effect for annual primary habitat loss and a credible positive interaction between extreme heat frequency and protected area coverage (Figure 3a, b, e). The model accounts for phylogenetic and spatial random effects, tests 0-, 5-, and 10-year lags, and verifies the absence of spatial (Moran's $I$) and phylogenetic (Pagel's $\lambda$) residual structure.

* **Rapid national socioeconomic development growth (annual change in HDI), rather than absolute HDI or governance level, is negatively associated with carnivore population trends: [Moderately Supported].**  
  The negative slope for national HDI growth rate (median standardized effect $-0.44$, Figure 3f) holds across linear and quadratic specifications of baseline HDI and across data subsets (Supplementary Table 6). However, because HDI change is measured at the national scale whereas habitat loss and climate anomalies are measured within local circular buffer zones around each population centroid, national HDI growth acts as an aggregate proxy that may absorb unmeasured sub-national land-use intensification, road expansion, or hunting/persecution pressures outside the immediate buffer radius.

* **Human socioeconomic development is a stronger driver of global carnivore population declines than habitat loss or climate change (Counterfactual analysis, Figure 4): [Overstated].**  
  While the standardized slope of primary habitat loss is comparable in magnitude to HDI growth (Figure 3a), the counterfactual scenario ("No growth in human development" vs. "No loss in primary habitat," Figure 4) shifts nearly all 1,123 populations positively for HDI growth because almost every country experienced positive HDI growth between 1970 and 2015, whereas 94% of the monitored carnivore populations were located in protected or remote areas that experienced near-zero primary habitat loss during their monitoring windows. Thus, Figure 4 measures the sample-specific *exposure prevalence* in the CaPTrends/LPD monitoring network rather than proving that socioeconomic development is intrinsically a stronger biological driver of carnivore decline than habitat destruction.

* **Decelerating socioeconomic development (<1.2% annual HDI growth) enables carnivore populations to transition from steep decline to recovery along a Kuznets-like trajectory (Figure 5): [Fragile].**  
  The idealized 1960–2020 abundance projections in Figure 5c rely on a space-for-time substitution across countries at different stages of development. As the authors candidly note (Line 89), developed countries with slow HDI growth (<1.2%/yr) between 1970 and 2015 had already extirpated their most sensitive carnivore populations prior to 1960 and were often witnessing legal protection and recolonization from depressed baselines, whereas developing countries with high HDI growth (>1.5%/yr) still harbored fuller carnivore assemblages undergoing initial contraction. In addition, the positive intercept when HDI growth approaches zero depends on holding all other covariates at their sample mean (where well-monitored North American and European recovering populations are overrepresented).

* **Increased drought frequency is positively associated with carnivore population trends (Figure 3d): [Fragile].**  
  The positive main effect of drought frequency (months exceeding pre-industrial mean + 2 SD) runs counter to physiological and trophic expectations and, as the authors acknowledge (Line 56), likely reflects short-term prey vulnerability, aggregation of carnivores and prey around permanent water sources (inflating local sightability/density estimates during short monitoring windows), or collinearity with arid/savanna protected area monitoring sites.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Separate Effect Size (Sensitivity) from Sample Exposure Prevalence in the Counterfactual Framing
* **WHY:** Setting primary habitat loss to zero in the counterfactual scenario (Figure 4a) produces near-zero median change across non-African continents only because most monitored populations in the database experienced near-zero primary habitat loss during their monitoring periods, not because habitat loss has a weak effect when it occurs.
* **WHAT:** Compute and report a conditional counterfactual comparison restricted to populations actually exposed to moderate-to-high threat levels (e.g., top quartile of habitat loss vs. top quartile of HDI growth), and temper the Abstract/Section header claims.
* **HOW:** Alongside Figure 4 (which shows the unconditional sample-wide counterfactual across all 1,123 populations), add a panel or summary statistic comparing the predicted counterfactual difference for populations at the 90th percentile of observed primary habitat loss vs. the 90th percentile of observed HDI growth. Revise the Abstract and Figure 4 title ("Human development is the primary driver...") to clarify that human development growth was the most *pervasive* correlate of decline across monitored populations.

#### 2. Propagate First-Stage Regression Standard Errors Directly into the JAGS Hierarchical Model
* **WHY:** For time-series records, the annual rate of change $r_t$ was estimated in a first-stage log-linear OU regression, and observation quality was subsequently approximated via a composite heuristic weighting term (duration, number of time points, method) rather than passing the exact standard error $\hat{\sigma}_{r_i}$ of each slope estimate into the second-stage Bayesian model.
* **WHAT:** Test a formal measurement-error (meta-analytic) specification for the quantitative time-series subset ($N = 985$).
* **HOW:** Extract the standard error $\text{SE}(\hat{r}_i)$ from the first-stage OU regression for each time-series record and specify the observation-level likelihood in JAGS as $y_i \sim \mathcal{N}(\mu_i, \sigma_{\text{proc}}^2 + \text{SE}(\hat{r}_i)^2)$. Compare the resulting posterior slope credible intervals against the heuristic quality-weighted model.

#### 3. Test Non-Overlapping Ordinal Thresholds for the Censored Qualitative Records
* **WHY:** In the interval-censoring specification (Methods, Line 122), the prior intervals for qualitative categories overlap (`Decrease`: $[-50\%, 0\%]$, `Stable`: $[-5\%, +5\%]$, `Increase`: $[0\%, +50\%]$). While JAGS `dinterval` requires strictly ordered cutpoints (or custom latent bounds), overlapping bounds mean that latent values in $[-5\%, 0\%]$ and $[0\%, +5\%]$ satisfy two categories simultaneously.
* **WHAT:** Clarify how overlapping interval censoring was coded in JAGS and verify sensitivity to strictly non-overlapping ordinal cutpoints (e.g., `Decrease`: $[-50\%, -2\%]$, `Stable`: $[-2\%, +2\%]$, `Increase`: $[+2\%, +50\%]$).
* **HOW:** Run a sensitivity model using non-overlapping thresholds at $\pm 1\%$ and $\pm 2.5\%$ (which is standard for ordinal probit/censored regression in JAGS) and confirm that the posterior estimates in Figure 3a remain unchanged.

#### 4. Test Within-Country Longitudinal HDI Deceleration to Validate the Space-for-Time Substitution
* **WHY:** The Kuznets-like recovery trajectory in Figure 5c relies on cross-country variation in HDI growth rate, which is confounded by historical baseline depletion in high-HDI countries (Europe/North America).
* **WHAT:** Test whether carnivore populations within the *same* countries or regions show improving trends over time as national HDI growth decelerates across decades (e.g., 1970s–1980s vs. 2000s–2010s).
* **HOW:** Decompose Change in HDI into a between-country mean ($\overline{\Delta\text{HDI}}_c$) and a within-country temporal deviation ($\Delta\text{HDI}_{i,c} - \overline{\Delta\text{HDI}}_c$, i.e., Mundlak / within-between random-effects centering) for countries with multi-decade monitoring records. If the within-country slope is also negative, this provides much stronger support for the dynamic trajectory in Figure 5c than cross-national comparison alone.

#### 5. Technical, Mathematical, and Editorial Cleanup
* **WHY:** A few figure cross-reference errors in the Methods section should be corrected for clarity.
* **WHAT & HOW:**
  * **Methods (Lines 158, 160):** Correct the figure cross-references `"at year 1960 (Fig. 4a)"`, `"we used our fitted model (Fig. 2)"`, and `"in the year 1960 (Fig. 4c)"` to `"Fig. 5a"`, `"Fig. 3"`, and `"Fig. 5c"`, respectively.
  * **Methods (Line 158):** Correct `"Supplementary Fig. 2"` (cited for human development parameter values) to `"Supplementary Fig. 12"`.
