# Review of OOD_ANON_32

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **5.5 / 10.0** (Mixed / Salvageable)  
* **Score Breakdown:** Rigor: 1.5/3.5 | Claims: 1.2/2.5 | Biology: 1.2/2.0 | Reproducibility: 1.6/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This study compiles digitized natural history records spanning ca. 120 years across the eastern United States—comprising 4,075 main-flowering herbarium specimens across 23 *Viola* species (1895–2018, scored via CrowdCurio) and 6,714 collection records across 7 solitary bee species (6 generalists and 1 specialist, *Andrena violae*, 1900–2022)—to evaluate how climate-driven phenological mismatches between plants and pollinators influence future plant "secondary local extinction risk" ($S_e$) in the 2070s (SSP5-8.5). The authors fit linear mixed-effects models (LMMs) for flowering and bee activity day-of-year (DOY), species distribution models (GLM, GAM, MaxEnt) for plant occurrence probability, and beta regressions of projected $S_e$ across latitude. Code and datasets are publicly archived on GitHub.

While the 120-year herbarium and entomological dataset is a valuable empirical resource, the modeling pipeline that connects phenology to "secondary local extinction risk" rests on two major statistical flaws. First, $S_e$ is not an empirical measurement of population decline; it is defined algebraically in Equations 6–7 as the product of SDM occurrence probability and phenological mismatch, $S_e = P(\text{occurrence}) \times M$. Regressing this synthetic product $S_e$ back onto $M$ across current grid cells using power and logistic curves (and discarding 63%–68% of species pairs with $R^2 \le 0.5$) is circular: deviations from linearity merely reflect spatial covariance between current habitat suitability $P(\text{occurrence})$ and current $M$, and projecting future $S_e$ solely by plugging future $M$ into that fitted curve drops future $P(\text{occurrence})$ altogether. Second, the authors equate the 95% confidence interval of the LMM predicted mean ($\hat{\mu} \pm 1.96\,\text{SE}(\hat{\mu})$) with the biological duration of flowering and bee activity ($D_p$). Because $\text{SE}(\hat{\mu})$ measures estimation uncertainty of the mean rather than within-population phenophase duration, $D_p$ is systematically confounded by sampling density and leverage along the latitudinal gradient. These issues can be resolved through computational re-analysis of the existing dataset by replacing mean CIs with quantile/prediction intervals and directly computing joint plant–pollinator suitability without circular intermediate curve-fitting.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Flowering times of *Viola* spp. and activity times of solitary bees advance with higher long-term mean annual temperature (MAT), while *Viola* flowering also responds to interannual temperature and precipitation anomalies: [Well Supported].**  
  The spatio-temporal LMMs fitted in `spaMM` with Matérn spatial random effects and AR(1) temporal structure across 4,075 plant specimens and 6,714 bee records show strong cross-validated predictive performance (LOOCV $R^2 = 0.796, 0.697,$ and $0.590$ for plants, generalist bees, and the specialist bee; lines 46–48). One caveat is a methodological discrepancy in how anomalies are defined between historical fitting (differences from long-term mean, centered and scaled; second chunk lines 9, 26) and future projection (where precipitation anomalies are described as a "proportion of its long-term mean precipitation"; second chunk line 34).

* **Flowering duration and phenological overlap decrease with latitude, driving higher future secondary local extinction risk ($S_e$) at northern latitudes: [Methodologically Flawed].**  
  In the Materials and Methods (second chunk, line 34) and Fig. 5 caption (line 72), flowering duration ($D_p$) and bee activity duration are approximated by the **95% confidence interval of the predicted mean DOY** from the LMM (`predict` SE). Statistically, $\pm 1.96\,\text{SE}(\hat{\mu})$ quantifies uncertainty in the regression mean, not the biological duration of the flowering period across individuals or weeks. In addition, the Materials and Methods contradict themselves regarding bee phenophase duration: lines 198–200 state that bee main activity periods were extracted from the 95% CI of presence-only `MaxLike` environmental models, whereas second chunk line 34 states that both plant and bee durations were approximated from the 95% CIs of the DOY LMMs.

* **Secondary local extinction risk ($S_e$) follows a nonlinear power or logistic functional response to phenological mismatch ($M$) that differs between generalist and specialist pollinators across latitudes: [Methodologically Flawed].**  
  Equations 5–7 define $S_e = P(\text{occurrence}) - P(\text{occurrence})\frac{O}{D_p} = P(\text{occurrence}) \times M$. Because $S_e$ is algebraically constructed as $P(\text{occurrence}) \times M$, fitting power ($y = ax^b$) and logistic functions of $S_e$ against $M$ across current grid cells (second chunk lines 100–102) does not estimate a mechanistic ecological response; it merely fits the spatial covariation between $P(\text{occurrence})$ and $M$. Furthermore, substituting future 2070s $M$ into the historical curve $S_e = f(M)$ to predict future $S_e$ ignores future changes in $P(\text{occurrence})$, and switching from a power to a logistic functional form reverses the sign of the latitudinal sensitivity trend for generalist bees (decreasing in Fig. 6A vs. increasing in Fig. 6C; line 66).

* **Existing conservation priorities based on primary climate extinction risk ($P_e$) miss secondary extinction risks ($S_e$) because $P_e$ and $S_e$ are weakly correlated ($r < 0.3$): [Overstated].**  
  Because $P_e = 1 - P(\text{occurrence})$ and current $S_e = P(\text{occurrence}) \times M = (1 - P_e) \times M$, the weak or negative correlation between $P_e$ and $S_e$ is partly a mathematical consequence of $P(\text{occurrence})$ appearing with opposite signs in the two definitions (a grid cell where a plant already has $P(\text{occurrence}) \approx 0$ has $P_e \approx 1$ and $S_e = P(\text{occurrence}) \times M \approx 0$ by definition). Biologically, the model also assumes all 7 bee species are present across every grid cell in the eastern US (line 160) and omits reproductive assurance from cleistogamous self-pollinating flowers present in ~82% of North American *Viola* species (line 172).

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Eliminate Circular Regression of Synthetic $S_e$ on $M$ and Incorporate Bee SDMs
* **WHY:** Defining $S_e = P(\text{occurrence}) \times M$ and then regressing $S_e$ on $M$ to forecast future $S_e = f(M_{\text{future}})$ conflates current habitat suitability with mismatch sensitivity and omits future habitat suitability $P_{\text{future}}(\text{occurrence})$.
* **WHAT:** Compute future interaction-adjusted occurrence directly from future SDM suitability and future phenological overlap, and incorporate spatially explicit bee SDMs rather than assuming all 7 bee species occupy the entire eastern US.
* **HOW:** Using the 6,714 bee occurrence records already mapped to grid cells, fit the same GLM/GAM/MaxEnt ensemble SDMs for the 7 bee species to obtain $P_{\text{bee}}(\text{occurrence})$, and compute future interaction risk directly as $\Delta P_{\text{future}} = P_{\text{plant, future}}(\text{occurrence}) \times \left[1 - P_{\text{bee, future}}(\text{occurrence}) \frac{O_{\text{future}}}{D_{p,\text{future}}}\right]$ at each grid cell without intermediate power/logistic curve-fitting or $R^2$ filtering.

#### 2. Replace LMM Mean Confidence Intervals with Population Prediction Intervals or Quantile Regression for Phenophase Duration
* **WHY:** The 95% CI of the conditional mean ($\hat{\mu} \pm 1.96\,\text{SE}(\hat{\mu})$) measures parameter estimation error rather than biological flowering or flight duration.
* **WHAT:** Estimate phenophase onset (10th percentile), offset (90th percentile), and duration ($D_p = \hat{q}_{0.90} - \hat{q}_{0.10}$) using quantile mixed regression or population prediction intervals that include residual variance $\hat{\sigma}^2$.
* **HOW:** Fit linear quantile mixed models (e.g., `lqmm` in R for $\tau = 0.10$ and $\tau = 0.90$) or compute the 90%/95% prediction interval $\hat{\mu} \pm z_{\alpha/2}\sqrt{\text{SE}(\hat{\mu})^2 + \hat{\sigma}_{\text{residual}}^2}$ from the `spaMM` models, and reconcile the contradictory text on `MaxLike` vs. LMM CIs for bees (lines 198–200 vs. second chunk line 34).

#### 3. Account for Spatial Autocorrelation and Propagate Uncertainty in Latitudinal Beta Regressions
* **WHY:** Treating thousands of $40 \times 40\text{ km}$ grid cells as independent observations in `glmmTMB` inflates degrees of freedom and produces artificially extreme test statistics ($Z = 131.61$ to $382.4$ in Tables 1–2).
* **WHAT:** Include a spatial Matérn random effect over grid-cell coordinates in the `glmmTMB` beta regressions and propagate SDM/phenology prediction variance via parametric bootstrap.
* **HOW:** Add `+ matern(pos + 0 | group)` to the `glmmTMB` formulas in Tables 1 and 2, and run 200 bootstrap draws sampling from the posterior/prediction distributions of the LMM and SDM models to report uncertainty-propagated standard errors and $p$-values.

#### 4. Standardize Anomaly Definitions and Equal-Area Spatial Grid Projections
* **WHY:** Web Mercator (`EPSG:3857`) distorts grid-cell area by more than 2-fold between Florida and Maine, and computing future precipitation anomalies as proportions rather than standardized differences creates a covariate shift relative to the historical training model.
* **WHAT:** Project grid cells in an equal-area coordinate system (e.g., North America Albers Equal Area Conic, `EPSG:5070`) and apply identical z-score standardization (using historical 1895–2018 mean and SD at each cell) to historical, recent, and 2070s temperature and precipitation anomalies.
* **HOW:** Reproject the occurrence grid to `EPSG:5070` and verify that the anomaly transformation in the prediction script matches the training design matrix in `spaMM`.

#### 5. Technical, Mathematical, and Editorial Cleanup
* **WHY:** Internal contradictions in grid size and sign typos in regression tables reduce clarity.
* **WHAT & HOW:**
  1. **Results line 53 vs. Methods lines 181, 193:** Reconcile the contradiction between "20 × 20 km grid cells" (line 53) and "40×40-km grid cells (area smaller than 800 km²)" (lines 181, 193, second chunk line 39).
  2. **Table 1 (line 86):** Correct the sign of the $Z$-value for `Scale(latitude): Specialist` from `3.91` to `-3.91` (since Estimate $\pm$ SE is $-0.044 \pm 0.011$).
  3. **Fig. 2 caption (line 28):** Correct the terminology "general exponential model ($y = ax^b$)" to "power function ($y = ax^b$)".
