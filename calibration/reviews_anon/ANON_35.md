# Review of ANON_35

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **3.2 / 10.0** (Flawed / Overstated)  
* **Score Breakdown:** Rigor: 0.7/3.5 | Claims: 0.7/2.5 | Biology: 0.8/2.0 | Reproducibility: 1.0/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript investigates an ecological association between national Bacillus Calmette–Guérin (BCG) vaccination policies and early COVID-19 mortality per million inhabitants (using mortality data accumulated up to April 22, 2020). The authors compare country-level COVID-19 death rates across categories of BCG policy ("current", "interrupted", "never") and historic coverage (1980–2018), first in a global "coarse" analysis and then in a "refined" subset of 22 countries filtered by arbitrary thresholds on Human Development Index ($\text{HDI} > 0.7$), urbanization ($>60\%$), age structure ($\ge 15\%$ aged $\ge 65\text{ y}$), population density ($<300/\text{km}^2$), and mortality ($\ge 1\text{ death/million}$). They also compare 5 US states against 5 Mexican/Brazilian states over the first 25 days following the first local death, compare former East vs. West German states, and regress 30-day COVID-19 mortality against a newly defined "BCG index" in a subset of European countries, reporting $r^2 = 0.88$ ($P = 8 \times 10^{-7}$) and claiming that every 10% increase in the BCG index is associated with a 10.4% reduction in COVID-19 mortality. Source data tables are included in Dataset S1.

While the manuscript acknowledges in passing that clinical trials are needed to establish causality, its quantitative conclusions rest on severe methodological flaws across multiple diagnostic pillars: (1) classic ecological fallacy (inferring individual-level trained immunity protection from coarse national mortality totals during the earliest weeks of pandemic seeding); (2) post-hoc exclusion of high-leverage contradictory countries (specifically dropping the United Kingdom and France from the European BCG index regression using a rationale that directly contradicts the authors' own East vs. West Germany age-of-vaccination argument in the preceding section); (3) severe temporal pseudoreplication in the Americas analysis ($t[237] = 14.274$, treating 25 daily cumulative/rolling observations across 10 states as ~240 independent degrees of freedom); and (4) selective reporting of a single extreme subgroup $r^2 = 0.88$ in the Abstract while downplaying that 63–81% of statistical tests in the refined global analysis (Tables S2–S4) were non-significant and uncorrected for multiple hypothesis testing.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **In socially similar European countries, the national BCG index strongly predicts early COVID-19 mortality ($r^2 = 0.88, P = 8 \times 10^{-7}$), with a 10.4% mortality reduction per 10% increase in BCG index: [Methodologically Flawed].**  
  To obtain this correlation (Figure 4D–E), the authors excluded both the United Kingdom and France—two Western European countries with high early COVID-19 mortality that maintained universal BCG vaccination programs for decades—on the post-hoc grounds that they vaccinated school-age or daycare children rather than infants at birth (Section "The Pandemic in Europe", line 78). Directly contradicting this exclusion rule, in the very same section (line 70, Figure 3B–D) the authors attribute lower mortality in East Germany relative to West Germany to East Germany's vaccination of 15-year-old teenagers! Furthermore, the ad-hoc "BCG index" formula $\text{(age of oldest vaccinated cohort} \times \text{years of campaign)} / 5625 \times \text{mean coverage}$ conflates demographic age structure and historical political bloc membership (Eastern vs. Western Europe, which differed sharply in early spring 2020 travel connectivity and epidemic seeding) with biological immunity.

* **US states without BCG vaccination had significantly higher 25-day COVID-19 mortality than main entry-point states in Mexico and Brazil ($t[237] = 14.274, P < 0.001$; $r^2 = 0.84$): [Methodologically Flawed].**  
  The authors compare 5 US states (NY, IL, LA, AL, FL) against 3 Brazilian states (PE, RJ, SP) and 2 Mexican entities (Mexico State, Mexico City) across the first 25 days after the first reported death (Figure 3A). Reporting 237 degrees of freedom ($t[237] = 14.274$) for a comparison of 10 states indicates that daily time-series values from the same states were pooled as independent observations, violating independence via extreme serial autocorrelation (pseudoreplication; true state-level degrees of freedom cannot exceed $10 - 2 = 8$). Moreover, aligned by the date of the first single recorded death, the 25-day window is heavily confounded by vast differences in March/April 2020 SARS-CoV-2 diagnostic testing capacity, post-mortem surveillance, and international seeding volume between New York and Latin American states.

* **Global and filtered cross-country analyses consistently support a protective link between national BCG policy and COVID-19 mortality: [Overstated].**  
  In the coarse global analysis, COVID-19 mortality is strongly positively correlated with HDI ($r^2 = 0.49$ together with population density; Figure 1B) because high-HDI countries in Western Europe and North America experienced earlier, larger travel-seeded outbreaks and had more complete death registration in March–April 2020, while low-HDI countries preferentially maintain universal BCG programs for TB control. When the authors apply their 5-variable filter ($N = 22$ countries), the fraction of statistically significant tests drops from 46% to 19% for linear regressions, 100% to 31% for ANOVAs, and 92% to 37% for $t$-tests (Section "Filtered Analysis", line 54)—meaning that the majority (63–81%) of refined comparisons fail to reject the null hypothesis even before applying any multiple-testing correction across the dozens of metric and time-window combinations in Tables S2–S4.

* **Lower COVID-19 mortality in former East German states (14.2/million) compared to West German states (40.5/million; $t[11] = -2.592, P = 0.025$) reflects BCG vaccination of older cohorts in East Germany: [Fragile].**  
  This univariate state-level $t$-test does not control for the nearly two-fold difference in population density (154 vs. $282/\text{km}^2$), international airport connectivity, or proximity to early Alpine/Carnival superspreading introductions that seeded western and southern German states (e.g., North Rhine-Westphalia, Bavaria, Baden-Württemberg) weeks ahead of eastern states. Note also that the identical test statistic ($t[11] = -2.592, P < 0.025$) is erroneously pasted for the Western vs. Eastern Europe comparison in the next sentence (line 70).

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Include the United Kingdom and France and Fit a Multivariable Regression Controlling for Confounders Simultaneously
* **WHY:** Dropping the UK and France post-hoc because they vaccinated children rather than neonates is inconsistent with the East Germany analysis and artificially inflates $r^2$ in Figure 4D–E. Furthermore, filtering countries by coarse binary cutoffs ($\text{HDI} > 0.7$, density $< 300/\text{km}^2$) leaves substantial residual confounding within the retained group (e.g., between Western and Eastern Europe).
* **WHAT:** Re-compute the European BCG index regressions (Figure 4D–E) including the UK and France, and evaluate the partial regression coefficient of the BCG index in a multivariable linear model that simultaneously includes HDI, population density, median age / % population $\ge 65$, and epidemic arrival date.
* **HOW:** Using the Dataset S1 table, fit `lm(log_deaths_30d ~ BCG_index + HDI + pop_density + pct_age65 + urban_pct)` across all European countries (with and without the UK and France) and report the partial $R^2$, $t$-statistic, and $P$-value for `BCG_index`.

#### 2. Correct Pseudoreplication in the Americas Regional Comparison
* **WHY:** Pooling 25 daily mortality values across 10 states as $N \approx 240$ independent observations ($t[237] = 14.274$) violates statistical independence and grossly understates the $P$-value.
* **WHAT:** Perform the state-level comparison using a single summary outcome per state (day-25 cumulative mortality per 10 million, giving $N = 5$ vs. $N = 5$, $\text{df} = 8$) or a linear mixed-effects model with state as a random intercept and an $\text{AR}(1)$ temporal correlation structure.
* **HOW:** Run a two-sample Welch $t$-test and Mann–Whitney $U$ test on the 10 state-level day-25 mortality values listed in the table in Figure 3A (Right), and replace $t[237] = 14.274$ with the valid state-level test statistic ($\text{df} \le 8$).

#### 3. Apply Multiple-Testing Correction Across All Evaluated Models in Tables S2–S4
* **WHY:** Testing dozens of combinations of independent variables (BCG policy, coverage mean/median, BCG index) and dependent variables (mean, median, maximum deaths at 21 d, 30 d, 0.1/M, 1/M, midpoint, full period) at $\alpha = 0.05$ without correction guarantees false positives when 63–81% of refined tests are already null.
* **WHAT:** Apply Benjamini–Hochberg false discovery rate (FDR) or Holm–Bonferroni correction across all tests in Tables S2–S4.
* **HOW:** Compute `p.adjust(p_values, method = "BH")` across the full family of refined tests in R and report the proportion of associations that survive at $q < 0.05$.

#### 4. Fix Duplicated Test Statistics and Temper Abstract Claims
* **WHY:** Line 70 reports the exact same test statistic `t[11] = −2.592, P = 0.025` for both the East vs. West Germany state comparison (Figure 3D) and the Western vs. Eastern Europe country comparison (Figure 4A), which is a copy-paste error. Additionally, the Abstract highlights only $r^2 = 0.88$ while omitting that over two-thirds of refined models were non-significant.
* **WHAT & HOW:** Compute and report the actual degrees of freedom and $t$-statistic for the Western vs. Eastern European country comparison on line 70, and revise the Abstract to state that the $r^2 = 0.88$ correlation was obtained in a restricted subset of European countries excluding the UK and France and that the majority of global confounder-filtered tests were non-significant.
