# Review of PMC9488757 (PMID:36125984)

**Manuscript Title:** Spurious early ecological association suggesting BCG vaccination effectiveness for COVID-19  
**Authors:** Ledesma JR, Lurie P, Yorlets RR, Daly G, Chrysanthopoulou S, Lurie MN.  
**Journal / Preprint:** *PLoS One* (2022; `PMC9488757` / `PMID:36125984` / `10.1371/journal.pone.0274900`)  
**Calibration Study Cohort:** Cohort A — Known Invalid / Refuted (`A42` | Double-Blinded as `ANON_139`)  
* **Overall Score:** **7.3 / 10.0** (Strong / Sound)
* **Score Breakdown:** Rigor: 2.4/3.5 | Claims: 2.2/2.5 | Biology: 1.5/2.0 | Reproducibility: 1.2/2.0
* **Synthesis:** This brief report conducts a longitudinal sensitivity and replication audit of an influential March 2020 ecological study (Miller et al.) that claimed universal Bacillus Calmette-Guérin (BCG) vaccination policies and longer BCG policy duration protected middle-high and high-income countries against COVID-19 mortality and case incidence. By re-running Miller et al.'s exact bivariate statistical procedures (unadjusted Wilcoxon rank-sum tests and Pearson correlation coefficients) across all ten months from March through December 2020 using Johns Hopkins University CSSE surveillance data and BCG World Atlas classifications ($N = 55$ current universal BCG countries, $N = 5$ never-universal BCG countries, and $N = 17$ prior universal BCG countries), the authors demonstrate that 6 of 9 statistically significant tests in March 2020 vanished in subsequent months, with only 2 of 9 tests (and 0 of 6 policy-duration correlations) remaining significant by December 2020. The study's claims are appropriately measured and provide a clear empirical demonstration of how early pandemic timing confounded cross-national ecological correlations; its main methodological limitations are a lack of explicit clarity on whether the monthly April–December series analyzed cumulative year-to-date totals or discrete monthly incident counts, reliance on parametric Pearson's $r$ without nonparametric rank-correlation sensitivity checks, and the absence of a supplementary country-level data table or analysis script.

---

## 2. Claim-by-Claim Evaluation & Empirical Audit

* **Claim 1:** Replicating Miller et al.'s bivariate design in March 2020 yields statistically significant differences in 6 of 9 tests (all 3 Wilcoxon rank-sum comparisons of mortality per 100,000, cases per 100,000, and mortality-to-incidence ratio between $N = 55$ current universal BCG and $N = 5$ never-universal BCG countries, plus 3 of 6 Pearson correlations with years of universal BCG policy duration), with only minor numerical discrepancies from Miller et al. caused by retroactive updates in the Johns Hopkins CSSE dataset.
  * **Support Level:** **[Well Supported]**
  * **Audit Trail:** Results (pages 4–5), Figure 1A–C (March 2020 column), and Table 1 (March 2020 row).
  * **Assessment:** The authors successfully reproduce the qualitative pattern of the original March 2020 analysis (e.g., March 2020 mortality Wilcoxon $p < 0.001$, incidence $p < 0.001$, mortality-to-incidence ratio $p = 0.01$; Pearson $r = -0.35, p = 0.036$ for mortality vs. current BCG duration, and $r = -0.58, p = 0.009$ and $r = -0.49, p = 0.025$ for mortality and incidence vs. prior BCG duration) and transparently document why retroactive JHU reporting adjustments shifted exact $p$-values slightly relative to the March 21, 2020 snapshot used by Miller et al.

* **Claim 2:** Extending the exact same analyses from April through December 2020 shows that the apparent protective associations with universal BCG vaccination and policy duration largely disappear over time: by December 2020, only 2 of 9 tests remain statistically significant at $p < 0.05$ (group mortality difference and group incidence difference), and 0 of 6 correlations between BCG policy duration and COVID-19 outcomes remain significant from May through December 2020.
  * **Support Level:** **[Well Supported]**
  * **Audit Trail:** Results (pages 4–5), Figure 1A–C (April–December 2020 boxplots), and Table 1 (April–December 2020 correlation and $p$-value time series).
  * **Assessment:** Table 1 and Figure 1 clearly show that Pearson correlations for current BCG duration ($N = 28$) hover near zero from April to December ($r \in [-0.14, 0.14]$, all $p \ge 0.24$), correlations for prior BCG duration ($N = 17$) become non-significant from May onward (and even flip sign to $r = +0.29$ for incidence by November–December), and the mortality-to-incidence ratio difference between current and never BCG countries is non-significant in every month from April to December ($p \ge 0.13$).

* **Claim 3:** Cross-sectional ecological comparisons at a single early timepoint in an epidemic are vulnerable to confounding by epidemic arrival timing, testing capacity, age structure, and policy interventions, and therefore cannot establish a causal protective effect of BCG vaccination against COVID-19.
  * **Support Level:** **[Well Supported]**
  * **Audit Trail:** Discussion (pages 5–6) and empirical attenuation trajectory across Figure 1 and Table 1.
  * **Assessment:** The authors' interpretation is fully aligned with epidemiological principles of the ecological fallacy and time-varying pandemic wave synchronicity.

---

## 3. Technical & Methodological Deep-Dive

### 1. Ambiguity Between Cumulative Year-to-Date Outcomes and Discrete Monthly Incident Outcomes in Figure 1 and Table 1
In the Methods (page 4), the authors state: *"Data were stripped down to include only data from the 10-month range (March 2020 to December 2020) and used to calculate mortality rate per 100,000, incidence rate per 100,000, and mortality-to-incidence ratio for each month."* However, it is not explicitly stated whether each month's value represents:
1. **Cumulative year-to-date cases and deaths** up to the end of that month (which matches Miller et al.'s cumulative January 1–March 21, 2020 definition), or
2. **Discrete monthly incident cases and deaths** occurring within that specific calendar month.

Inspecting the monotonically increasing y-axis scales across the monthly facets of Figure 1A (where the median and interquartile range of deaths per 100,000 rise steadily from ~0.1–1 in March to ~40–100+ in December) and Figure 1B (where cases per 100,000 rise from ~10–50 in March to ~2,000–5,000+ in December) indicates that **cumulative totals** through each month were plotted and tested. Because cumulative totals through December 2020 still include the spring 2020 wave—when the $N = 5$ "never universal BCG" countries (e.g., Italy, Belgium, Netherlands, USA, Lebanon) experienced early, high-fatality first waves prior to widespread testing or clinical protocols like dexamethasone—cumulative December comparisons partly carry forward early-wave mortality. Explicitly stating in the Methods that cumulative end-of-month totals were used, and adding a supplementary table of **discrete monthly incident rates** (which would likely show even faster convergence during late-2020 autumn/winter waves in Eastern and Central Europe and Latin America), would strengthen the paper's central point.

### 2. Extreme Group-Size Imbalance ($N = 55$ vs. $N = 5$) and Outlier Sensitivity of Pearson's $r$
1. **Five-Country Control Group:** The primary Wilcoxon rank-sum comparison pits $N = 55$ middle-high and high-income countries with universal BCG against just $N = 5$ countries that never had universal BCG. With $N_2 = 5$, the Wilcoxon rank-sum statistic is highly sensitive to the epidemic trajectory of 2–3 Western European/North American countries that happened to be the earliest epicenters outside China in March 2020. Listing the exact 5 "never BCG" countries (as well as the 55 "current BCG" and 17 "prior BCG" countries) directly in a table or appendix would make this structural limitation transparent to readers.
2. **Pearson's $r$ on Skewed Country Rates:** While using Pearson's $r$ is fully justified to maintain an exact methodological replication of Miller et al., country-level per-capita COVID-19 mortality and case rates in March 2020 were right-skewed over multiple orders of magnitude. Reporting nonparametric Spearman rank correlations ($\rho$) alongside Pearson's $r$ in Table 1 would demonstrate whether the March–April 2020 correlations in the $N = 17$ prior-BCG subgroup were driven by a single extreme outlier (such as Italy or Spain).

### 3. Reproducibility & Data/Code Availability
Although the raw surveillance data (`github.com/CSSEGISandData/COVID-19`), World Bank income classifications, and BCG World Atlas (`bcgatlas.org`) are public, the BCG World Atlas and JHU CSSE repositories have undergone periodic updates. Providing a supplementary CSV table listing the exact countries included in each group ($N = 55$, $N = 5$, $N = 28$, and $N = 17$), their assigned BCG start/end years, their population denominators, and the R script used to compute Figure 1 and Table 1 would ensure 100% long-term reproducibility.
