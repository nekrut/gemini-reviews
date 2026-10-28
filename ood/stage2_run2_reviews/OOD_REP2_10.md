# Review of OOD_REP2_10

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **5.0 / 10.0** (Mixed / Salvageable)  
* **Score Breakdown:** Rigor: 1.2/3.5 | Claims: 1.0/2.5 | Biology: 1.1/2.0 | Reproducibility: 1.7/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript investigates the "secondary local extinction risk" ($S_e$) of 23 *Viola* species across the eastern United States arising from climate-driven phenological mismatches with seven solitary bee species (six generalists and one specialist, *Andrena violae*). Using 4,075 crowdsourced herbarium specimens in peak flower (1895–2018) and 6,714 digitized bee collection records (1900–2022), the authors fit spatial-temporal linear mixed-effects models (`spaMM`) relating collection day-of-year (DOY) to long-term mean annual temperature (MAT), precipitation, and interannual climate anomalies. Simultaneously, they calibrate species distribution models (GLMs, GAMs, MaxEnt) on 7 PCA axes of climate and soil variables to estimate primary local extinction risk ($P_e = 1 - P(\text{occurrence})$). They define phenophase duration as the width of the $95\%$ confidence interval around the LMM-predicted mean DOY, compute proportional non-overlap ($M = 1 - O/D_p$), and define secondary extinction risk as $S_e = P(\text{occurrence}) \times M$ (Equations 1–7). After fitting power and logistic curves of $S_e$ against $M$ under current climate and projecting to the 2070s (SSP5-8.5), they use mixed-effects beta regressions to conclude that $S_e$ increases with latitude, correlates weakly with primary risk $P_e$ ($r < 0.3$), and exhibits latitude-dependent sensitivity that differs between specialist and generalist pollinators. All data and R scripts are publicly archived on GitHub.

The assembly and crowdsourced phenological scoring of 15,000 museum and herbarium records across a 120-year span is a valuable empirical dataset, and the authors' commitment to open data and code is commendable. However, the mathematical framework linking phenology to secondary extinction risk contains three fundamental flaws that invalidate the downstream statistical inferences: (1) the authors conflate the standard error of the regression mean ($\text{SE}(\hat{\mu})$ from `stats::predict`) with the biological duration of flowering and bee activity; (2) $S_e$ is algebraically defined as $P(\text{occurrence}) \times M$ (Eqs. 5–7), regressed against $M$ to fit deterministic power/logistic curves, and then re-regressed against $M \times \text{Latitude}$ in beta regressions (Table 2), creating a circular pipeline where synthetic curve outputs are tested against their own inputs ($Z = 382.4$); and (3) because $P_e = 1 - P(\text{occurrence})$ and $S_e = P(\text{occurrence}) \times M = (1 - P_e)M$, the weak or negative correlation between $P_e$ and $S_e$ (Fig. 4) is a mathematical boundary artifact rather than an independent ecological signal. Rebuilding the phenophase duration estimator using prediction intervals or quantile regression and reformulating the demographic/occurrence risk model to remove algebraic circularity are essential before the geographic projections can inform conservation policy.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Flowering time of *Viola* spp. and activity time of solitary bees advance significantly with spatial MAT gradients ($14\text{ d}$, $17\text{ d}$, and $8\text{ d}$ per SD of MAT for *Viola*, generalist bees, and *A. violae*, respectively), while *Viola* also responds to interannual MAT and precipitation anomalies: [Well Supported].**  
  The spatial-temporal LMMs (`spaMM` with Matérn spatial and AR(1) temporal random structures) are appropriately specified for museum specimen DOY data, achieve solid leave-one-out cross-validation performance ($R^2 = 0.590\text{–}0.796$), and reliably capture space-for-time and interannual phenological sensitivities.

* **Secondary local extinction risk ($S_e$) increases with latitude and exhibits differential latitudinal sensitivity to mismatch with specialist versus generalist bees (Tables 1–2, Figs. 5–6): [Methodologically Flawed].**  
  This conclusion rests on two mathematical errors:
  1. **Conflation of regression SE with phenophase duration:** In Materials and Methods (second part, line 34) and the Fig. 5 caption, phenophase duration ($D_p$) is defined as the $95\%$ confidence interval of the predicted mean DOY from `stats::predict` ($\hat{\mu} \pm 1.96\,\text{SE}(\hat{\mu})$). Statistically, $\text{SE}(\hat{\mu})$ measures uncertainty in the conditional mean (which shrinks with sample size and grows quadratically toward the edges of climate space), *not* the biological duration of flowering or flight activity across individuals ($\pm 1.96\,\hat{\sigma}_{\text{residual}}$ or the $5\text{th}–95\text{th}$ quantiles).
  2. **Circular curve-fitting and beta regression:** Substituting Eq. 5 ($M = 1 - O/D_p$) and Eq. 6 ($P(\text{mismatch}) = P(\text{occurrence}) \times O/D_p$) into Eq. 7 yields the identity $S_e = P(\text{occurrence}) \times M$. The authors fit power ($a M^b$) and logistic ($L / [1 + e^{-k(M-x_0)}]$) curves of $S_e$ onto $M$ under current climate, plug 2070s $M$ into those curves to generate deterministic predictions $\hat{S}_e = f(M_{\text{2070s}})$, and then run mixed-effects beta regressions of $\hat{S}_e$ on `M * Latitude` (Table 2). Regressing a deterministic function $f(M)$ on $M$ and `M * Latitude` on a logit link yields artificial test statistics ($Z = 382.4, P < 0.001$) and simply measures the second-derivative mismatch between a power/logistic function and the logit link over the latitudinal range of $M$. This explains why power and logistic fits produce opposite signs for the latitudinal sensitivity of generalist bees (Fig. 6A vs. 6C).

* **Geographic patterns of secondary local extinction risk ($S_e$) are weakly correlated with primary climate extinction risk ($P_e$, mean Pearson's $r < 0.3$; Fig. 4): [Methodologically Flawed].**  
  Primary extinction risk is defined as $P_e = 1 - P(\text{occurrence})$, while baseline secondary extinction risk is defined as $S_e = P(\text{occurrence}) \times M = (1 - P_e) \times M$. By construction, $S_e$ is bounded above by $1 - P_e$: in grid cells where a plant has high primary extinction risk ($P_e \to 1$, so $P(\text{occurrence}) \to 0$), $S_e$ is algebraically forced toward $0$ even if pollinator mismatch is $100\%$ ($M = 1$). Conversely, $S_e$ can only approach $1$ where $P(\text{occurrence})$ is high ($P_e \to 0$). Thus, defining $S_e$ as the absolute reduction in occurrence probability $P(\text{occurrence}) \times M$ rather than the conditional risk given suitability ($M$) or total combined risk ($1 - P(\text{occurrence})(1 - M) = P_e + (1 - P_e)M$) mechanically prevents a positive correlation between $P_e$ and $S_e$.

* **Phenological mismatch with solitary bees threatens the persistence of *Viola* populations across the eastern United States: [Overstated].**  
  As noted in the Discussion (lines 136, 160, 172), 60 of 73 North American *Viola* species produce self-pollinating cleistogamous flowers that set abundant seed without insect visitation, non-bee pollinators (lepidopterans, syrphid flies, bombyliids) are omitted, and all seven bee species were assumed to be present in every grid cell from Florida to Maine without bee SDMs.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Replace the Standard Error of the Mean ($\text{SE}(\hat{\mu})$) with Within-Population Phenophase Duration
* **WHY:** The $95\%$ CI of the LMM mean prediction ($\hat{\mu} \pm 1.96\,\text{SE}(\hat{\mu})$) measures parameter estimation uncertainty, not the length of the flowering or flight season in days. Using $\text{SE}(\hat{\mu})$ makes predicted flowering duration an artifact of local sample density and leverage in climate space.
* **WHAT:** Estimate phenophase onset, offset, and duration using either the $95\%$ prediction interval (incorporating residual within-cell variance $\sigma_\epsilon^2$), quantile regression ($10\text{th}$ and $90\text{th}$ percentiles of DOY), or Weibull onset/offset estimators (`phenesse`).
* **HOW:** In the existing R pipeline, either fit linear quantile mixed models (`lqmm` package) for the $\tau = 0.05$ and $\tau = 0.95$ quantiles of DOY as functions of climate, or model local flowering duration directly by computing the empirical $5\text{th}–95\text{th}$ DOY spread within spatial-temporal cells with sufficient records and regressing duration on climate covariates. Also clarify the discrepancy between the `MaxLike` bee phenology procedure (Methods lines 198–200) and the LMM `stats::predict` procedure (Methods second part, line 34).

#### 2. Remove the Algebraic Circularity in $S_e$ and Separate Conditional Mismatch Risk from Baseline Occurrence
* **WHY:** Defining $S_e = P(\text{occurrence}) \times M$, fitting $S_e = f(M)$ on current data, projecting $\hat{S}_e = f(M_{\text{2070s}})$ without 2070s $P(\text{occurrence})$, and then fitting beta regressions of $\hat{S}_e$ on $M \times \text{Latitude}$ is algebraically circular. Furthermore, multiplying $M$ by $P(\text{occurrence})$ forces $S_e \to 0$ wherever $P(\text{occurrence}) \to 0$ ($P_e \to 1$).
* **WHAT:** Distinguish three clearly defined quantities in every grid cell $i$ and time period $t$:
  1. **Primary climatic extinction risk:** $P_{e,it} = 1 - P_{it}(\text{occurrence})$.
  2. **Conditional phenological mismatch risk (given climatic suitability):** $M_{it} = 1 - O_{it} / D_{p,it}$.
  3. **Total combined local extinction risk:** $R_{\text{total},it} = 1 - P_{it}(\text{occurrence})(1 - M_{it}) = P_{e,it} + (1 - P_{e,it})M_{it}$.
* **HOW:** Directly compute $M_{it}$ and $R_{\text{total},it}$ in the 2070s from the 2070s LMM phenophase overlap $O_{it}/D_{p,it}$ and 2070s SDM $P_{it}(\text{occurrence})$ without the intermediate step of fitting empirical curves of $P_{\text{current}}(\text{occurrence}) \times M_{\text{current}}$ on $M_{\text{current}}$. Test latitudinal trends directly on $\Delta M = M_{\text{2070s}} - M_{\text{current}}$ and $\Delta R_{\text{total}}$ across species.

#### 3. Restrict Bee–Plant Overlap Calculations to Each Bee Species' Predicted Geographic Range
* **WHY:** Assuming all seven bee species occur in every grid cell across the entire eastern United States (from southern Florida to northern Maine) introduces counterfactual interactions where boreal or temperate bees do not occur.
* **WHAT:** Mask each plant–bee calculation to grid cells falling within the bee species' geographic range (estimated via SDM or convex hull/buffered occurrence polygons from the 6,714 SCAN/GBIF bee records).
* **HOW:** Run the same GLM/GAM/MaxEnt SDM pipeline (already implemented for *Viola*) on the 6,714 bee occurrences to generate binary presence/absence maps (thresholded by `maxSSS`) for each of the seven bee species, and compute mismatch only in grid cells where the bee species is predicted to be present.

#### 4. Technical, Mathematical, and Editorial Cleanup
* **WHY:** Inconsistent grid cell dimensions and sign mismatches in regression tables confuse readers.
* **WHAT & HOW:**
  1. **Grid resolution contradiction:** Results line 53 states *"We divided the eastern United States into 20 × 20 km grid cells,"* whereas Materials and Methods lines 181, 193, and second part line 39 state *"40 × 40-km grid cells... area smaller than 800 km2"* ($40 \times 40\text{ km} = 1,600\text{ km}^2$, half of which is $800\text{ km}^2$). Correct line 53 to $40 \times 40\text{ km}$.
  2. **Table 1 sign typo (line 86):** For `Scale(latitude): Specialist`, the Estimate is negative (`−0.044 ± 0.011`) while the `Z-value` is positive (`3.91`). Correct the sign of the $Z$-value to `−3.91`.
  3. **Chasmogamous vs. cleistogamous reproduction:** Explicitly qualify in the Abstract that the modeled secondary risk applies to *outcrossing chasmogamous reproduction*, not necessarily whole-population local extinction in cleistogamous *Viola* species.
