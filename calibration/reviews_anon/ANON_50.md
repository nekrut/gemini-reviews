# Review of ANON_50

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **8.8 / 10.0** (Strong / Sound)  
* **Score Breakdown:** Rigor: 3.0/3.5 | Claims: 2.2/2.5 | Biology: 1.9/2.0 | Reproducibility: 1.7/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript reconstructs the spatiotemporal spread and metapopulation dynamics of the 2013–2016 West African Ebola virus disease (EVD) epidemic using 1,610 complete Ebola virus (EBOV) genomes (~5.8% of known and suspected cases) sampled across 56 administrative regions in Guinea, Sierra Leone, and Liberia between March 2014 and October 2015. The authors mask 15 tracts of putative ADAR-mediated T-to-C hypermutation, fit a four-partition relaxed-clock Skygrid coalescent model coupled with a Bayesian generalized linear model (GLM) of discrete-trait continuous-time Markov chain (CTMC) phylogeographic diffusion incorporating two-way origin/destination random effects and stochastic search variable selection (SSVS) over 25 covariates, extend the CTMC GLM with epoch change-points to evaluate international border closures, and fit a negative-binomial GLM to regional WHO case counts. They demonstrate that viral dispersal followed a classic gravity model driven by origin/destination population sizes and inverse geographic distance ($50\%$ of migrations $<72\text{ km}$, $\text{BF} > 50$), with attenuation across international borders ($\text{BF} > 50$) that increased after August–September 2014 border closures but occurred too late to prevent epidemic establishment. They further show that the epidemic was sustained by a metapopulation of repeated regional introductions yielding small, short-lived clusters (mean 4.3 sampled sequences, mean persistence 41.3 days). Sequence alignments, BEAST XML files, and scripts are publicly archived.

This is a landmark phylodynamic investigation that pairs careful molecular data curation (such as isolating ADAR hypermutation tracts so they do not distort branch rates) with a well-designed two-way random-effects phylogeographic GLM and a mid-epidemic (October 2014, $N=787$) robustness check. Three methodological and technical issues merit improvement: (1) the non-phylogenetic negative-binomial GLM for regional cumulative case counts (Table 2) assumes independent errors across the 56 contiguous administrative polygons without accounting for spatial autocorrelation or epidemic arrival timing, confounding coastal spatial clustering with climatic predictors (temperature seasonality and precipitation); (2) when extrapolating expected viral imports to unaffected regions (Figs. 8a, 9a) and fitting epoch change-points, the two-way location random effects ($\varepsilon_i + \varepsilon_j$) are dropped without propagating their variance ($\sigma^2$) into the out-of-sample prediction intervals; and (3) there is an unexplained discrepancy in the 95th percentile of cluster size between the main text (17) and the Figure 11c caption (32), alongside minor equation and URL typos.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **The West African EBOV epidemic originated in Guéckédou Prefecture in late 2013 / early 2014 and dispersed across administrative regions according to a gravity model attenuated by international borders: [Well Supported].**  
  The joint Bayesian Skygrid + two-way random-effects CTMC GLM strongly supports five predictors ($\text{BF} > 50$, inclusion probability 1.0): national vs. international dispersal ($\beta = 3.07$), shared international border ($\beta = 3.39$), origin population size ($\beta = 1.36$), destination population size ($\beta = 0.74$), and inverse great-circle distance ($\beta = -0.77$). These exact five predictors and effect sizes are replicated in the October 2014 "real-time" subset ($N=787$, Fig. 5), and sampling-residual covariates receive zero support, confirming robustness against regional sequencing skew.

* **The epidemic was sustained as a spatially dissociated metapopulation of frequent regional introductions generating small, transient local transmission clusters: [Well Supported].**  
  Markov jump reconstructions across the posterior tree distribution reveal an average inter-regional migration rate of 0.85 events/lineage/year (~3.6% per 15.3-day serial interval), with repeated re-introductions into Guinea (21, 95% CI 16–25) and Sierra Leone (9, 95% CI 6–12) generating clusters that went extinct locally within a mean of 41.3 days.

* **International border closures coincided with an increase in the national-to-international dispersal ratio after August 2014, but occurred after cross-border seeding was already established: [Well Supported].**  
  The time-inhomogeneous change-point epoch GLM detects a shift in the `Nat/Int` coefficient from 1.15 to 2.83 between August and September 2014 (80% posterior support, Fig. 4b), while phylogenetic lineage tracking confirms that the major Sierra Leone and Liberia epidemic clades were already introduced in April–May 2014 prior to border closures.

* **Regional cumulative EVD case counts were driven by lower temperature seasonality ($\text{BF} > 50$) and higher precipitation ($\text{BF} = 4.4$) in addition to urbanization (Table 2): [Fragile].**  
  In the within-location negative-binomial GLM (Eq. in Line 136, Table 2), the response variable is cumulative regional case count $Y_i$ across 56 administrative units modeled as independent observations without a spatial covariance structure or an offset for time since initial viral introduction. Because both the epidemic epicenter (forest region) and the largest urban outbreaks (Conakry, Freetown, Monrovia) lie along a contiguous coastal/forest belt with distinct rainfall and temperature seasonality compared to inland savannah prefectures, an i.i.d. regression over 56 polygons easily confounds spatial proximity to the epidemic core and collinear urbanization metrics (`tt50K` and `tt100K` both included in Table 2) with climatic effects.

* **Unaffected regions in neighboring countries had low predicted viral importations but high intrinsic susceptibility to large outbreaks if seeded (Figs. 8 and 9): [Moderately Supported].**  
  The gravity model plausibly explains why distant non-contiguous regions in neighboring countries experienced few introductions. However, when computing expected transitions $\zeta_{ij}$ to unrecorded regions (Line 114), the authors drop the two-way random effects ($\varepsilon_i + \varepsilon_j$) used in the main GLM (Eq. 1) rather than integrating over the random-effect distribution $\varepsilon_j \sim \mathcal{N}(0, \sigma^2)$, which understates predictive uncertainty for out-of-sample regions.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Account for Spatial Autocorrelation and Introduction Timing in the Regional Case-Count GLM (Table 2)
* **WHY:** Treating cumulative case counts in 56 contiguous administrative regions as conditionally independent in a negative-binomial GLM ignores spatial autocorrelation and the number/timing of viral introductions, inflating Bayes factors for spatially smooth climatic variables (`TempSS` and `Precip`).
* **WHAT:** Test whether climatic predictors retain support in Table 2 after controlling for spatial autocorrelation and the phylogeographically inferred number/date of introductions per region.
* **HOW:** Include a conditional autoregressive (CAR) or Gaussian process spatial random effect over region centroids and add the log number of inferred introductions (or date of first introduction from Fig. 10) as a predictor in the negative-binomial GLM; also orthogonalize or select between the collinear travel-time predictors `tt50K` and `tt100K`.

#### 2. Propagate Random-Effect Variance ($\sigma^2$) Into Out-of-Sample Importation Predictions
* **WHY:** Dropping the location random effects $\varepsilon_i + \varepsilon_j$ when predicting expected transitions $\zeta_{ij}$ into unaffected regions (Line 114) ignores the unexplained location heterogeneity captured in Eq. 1.
* **WHAT:** Propagate the posterior distribution of $\varepsilon_i$ (for sampled origins) and draw $\varepsilon_j \sim \mathcal{N}(0, \sigma^2)$ (for unsampled destinations) when simulating expected importations in Figs. 8a and 9a.
* **HOW:** For each MCMC sample in the 1,000-tree posterior subset, sample $\varepsilon_j \sim \mathcal{N}(0, \sigma^2)$ for each of the 25 unaffected regions when evaluating $\Lambda_{ij} = \exp(X'_{ij}\delta\beta + \varepsilon_i + \varepsilon_j)$ in Eq. 2, and report the resulting 95% credible intervals.

#### 3. Reconcile Numerical Discrepancies Between the Main Text and Figure 11/12 Captions and Fix Equations/URLs
* **WHY:** Summary statistics for cluster size and persistence differ between the main text and figure captions without explanation, and several URLs and an equation contain typographical errors.
* **WHAT & HOW:**
  * **Main text (Line 60) vs. Figure 11c caption:** Line 60 states *"a mean cluster size of 4.3 and only 5% larger than 17 in our sample; Figure 11c"*, whereas the Figure 11c caption states *"with at least 2 sampled cases: 50% < 5.3, 95% < 32"*. Explicitly state in Line 60 that the 95th percentile is 17 across all introductions (including singletons of size 1) and 32 when restricted to clusters of size $\ge 2$ as plotted in Fig. 11c. Similarly, clarify the relationship between the mean persistence of 41.3 days (Line 60), the median of 36 days (Fig. 11d caption), and ~25 days (Fig. 12 caption).
  * **Methods Equation (Line 136):** Fix the missing division slash in the negative-binomial parameterization: change `pi=r(r+λi)` $\rightarrow$ $p_i = r / (r + \lambda_i)$.
  * **Methods URLs (Lines 79, 89, and 146):** Fix the malformed GitHub URLs in Lines 79 and 89 (`https://github/ebov/space-time/data/` $\rightarrow$ `[GITHUB_REPO_REDACTED]/`) and remove the trailing unmatched parenthesis in Line 146 (`[GITHUB_REPO_REDACTED])` $\rightarrow$ `[GITHUB_REPO_REDACTED]`).
