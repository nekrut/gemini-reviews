# Review of PMC9348750 (PMID:35881010)

**Manuscript Title:** The Huanan Seafood Wholesale Market in Wuhan was the early epicenter of the COVID-19 pandemic  
**Authors:** Worobey M, Levy JI, Malpica Serrano L, Crits-Christoph A, Pekar JE, Goldstein SA, Rasmussen AL, Kraemer MUG, Newman C, Koopmans MPG, Suchard MA, Wertheim JO, Lemey P, Robertson DL, Garry RF, Holmes EC, Rambaut A, Andersen KG.  
**Journal / Preprint:** *Science* (2022; `PMC9348750` / `PMID:35881010` / `10.1126/science.abp8715`)  
**Calibration Study Cohort:** Cohort B — Validated Control (`B07` | Double-Blinded as `ANON_41`)  
**Overall Score:** **8.5 / 10.0** (Strong / Sound)  
* **Score Breakdown:** Rigor: 2.9/3.5 | Claims: 2.0/2.5 | Biology: 1.8/2.0 | Reproducibility: 1.8/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript investigates the geographic and intra-market origins of the early COVID-19 outbreak in Wuhan during December 2019. The authors digitize residential coordinates for 155 of the 164 Wuhan cases in the March 2021 WHO mission report (35 epidemiologically linked and 120 unlinked to the Huanan Seafood Wholesale Market), compare their spatial distribution against age-matched WorldPop population densities and 737 January–February 2020 Weibo help-seeker locations, evaluate city-wide venue traffic using 1.49 million Sina Visitor System check-ins from 2013–2014, document live mammal species sold at Huanan market up to November 2019, and perform spatial relative risk (`sparr`) and binomial generalized linear model (GLM) analyses on 585 environmental samples collected inside the market in January 2020. They find that both market-linked and unlinked December 2019 cases centered tightly around Huanan market (1% highest probability density contour; center-point distance $1.02\text{ km}$, $p=0.007$ overall; $0.91\text{ km}$, $p=0.006$ for unlinked cases), and that intra-market environmental positivity clustered in the southwestern wildlife section ($p<0.05$). Data and analysis code are publicly archived.

The spatial epidemiology of the December 2019 residential cases and the forensic reconstruction of the Huanan market stall layout provide strong empirical evidence that Huanan market was the early epicenter of the COVID-19 epidemic in Wuhan. However, three statistical and inferential issues require attention: (1) the proximity test for the two early lineage A cases relies on an unverified hotel location and equates a temporary hotel stay near Wuhan's main rail and commercial hub with the city-wide residential null distribution; (2) the intra-market binomial GLM treats multiple environmental samples within and across adjacent stalls as conditionally independent observations without accounting for stall-level clustering or spatial autocorrelation; and (3) the mobility baseline relies on social media check-ins from 2013–2014 that skew toward younger smartphone users rather than wholesale market patrons in late 2019. These limitations can be resolved through mixed-effects spatial modeling, formal sensitivity bounds on the lineage A calculation, and tempered framing around direct animal-to-human transmission vs. human amplification inside the market.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **December 2019 COVID-19 cases—including those without reported market links—were spatially centered on the Huanan market: [Well Supported].**  
  Kernel density estimation, median distance ($4.28\text{ km}$ overall; $4.00\text{ km}$ for unlinked cases vs. $16.11\text{ km}$ age-matched WorldPop null, $p<0.001$), and center-point distance tests ($1.02\text{ km}$ overall, $p=0.007$; $0.91\text{ km}$ unlinked, $p=0.006$) consistently place the Huanan market at the geographic center of the December 2019 outbreak. This clustering is absent in the January–February 2020 Weibo help-seeker distribution and remains significant after removing up to 30%–68% of the closest unlinked cases to control for hypothetical neighborhood ascertainment bias, as well as under $1000\text{ m}$ coordinate jittering.

* **Live SARS-CoV-2-susceptible mammals were sold at Huanan market through November 2019, and positive environmental samples clustered in the southwest wildlife section: [Well Supported].**  
  Photographic records, business registries, and fine records establish the presence of live raccoon dogs, hog badgers, red foxes, and other susceptible mammals prior to market closure. Spatial relative risk (`sparr`) analysis accounting for the non-uniform distribution of sampled stalls confirms an elevated density of SARS-CoV-2-positive environmental samples in the southwestern section ($p<0.05$) that holds across three bias-sensitivity scenarios.

* **Distance to live mammal vendors and distance to human cases are independently predictive of environmental sample positivity in a binomial GLM ($p=0.004$ and $p=0.014$): [Fragile].**  
  Modeling environmental sample positivity across stalls with a standard binomial GLM violates conditional independence because multiple swabs were collected per stall (e.g., five positive samples in a single stall) and stalls are spatially contiguous along shared drainage and ventilation corridors. Without a stall-level random effect, quasi-binomial dispersion parameter, or spatial covariance structure, the nominal $p$-values underestimate true uncertainty. Furthermore, the text parenthetically states "(p =0.004 and 0.014, respectively for N=6; table S9)" without explaining in the main text what the effective sample size $N=6$ refers to.

* **Both earliest lineage A cases were unlikely to occur near Huanan market by chance ($p \le 0.001$): [Overstated].**  
  With only $n=2$ geolocated lineage A cases from December 2019, the first resided $2.31\text{ km}$ from the market ($p=0.034$). The second case did not reside in Wuhan or report market contact, but stayed at an unidentified "hotel near the market." Assuming this hotel was within $2.31\text{ km}$ because the narrative source described it as "near the market" is circular, and evaluating a short-term visitor hotel stay against an age-matched residential WorldPop distribution ignores the extreme spatial concentration of hotels around Hankou Railway Station (~$1\text{ km}$ from Huanan market).

* **Huanan market accounted for only 0.12% of market visits and 0.04% of potential superspreader venue visits across Wuhan: [Moderately Supported].**  
  While Huanan market was clearly only one of hundreds of high-traffic commercial venues in Wuhan, deriving exact visit shares (120 of 98,146 market check-ins) from 2013–2014 Sina Visitor System social media check-ins introduces severe temporal and demographic ascertainment bias. Check-ins from 5–6 years prior on a youth-skewed social platform poorly represent the daily foot traffic of older shoppers and wholesale buyers at wet markets in late 2019.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Account for Overdispersion and Spatial Clustering in the Intra-Market Environmental Regression
* **WHY:** Standard binomial GLMs assume independent Bernoulli trials within each stall and independence across stalls. Multiple swabs taken from the same surfaces, cages, and shared floor drains within a stall are highly correlated, inflating Type I error rates.
* **WHAT:** Re-estimate the regression of environmental positivity on distance to live mammal vendors and human cases using a model that accounts for stall-level clustering and spatial autocorrelation, and clarify the meaning of "$N=6$" in the main text.
* **HOW:** Fit a beta-binomial or generalized linear mixed model (GLMM) with a stall-level random intercept and a Matérn or exponential spatial covariance term over stall centroids (or a binary stall-level logistic regression testing whether $\ge 1$ positive sample was detected per sampled business). Report the updated effect sizes, confidence intervals, and $p$-values alongside the original binomial GLM in Table S9.

#### 2. Replace the Residential Null for the Second Lineage A Case with an Empirical Hotel Distribution
* **WHY:** Evaluating a traveler's hotel location against the city-wide WorldPop residential distribution is mismatched because hotels cluster heavily around transport hubs like Hankou Railway Station, which lies immediately adjacent to Huanan market. Moreover, conditioning on the qualitative description that the hotel was "near the market" to bound its distance at $\le 2.31\text{ km}$ is post-hoc circular.
* **WHAT:** Separate the residential test for the first lineage A case ($p=0.034$) from the hotel-based second case, and evaluate the second case against the spatial distribution of hotels across Wuhan.
* **HOW:** Extract hotel coordinates across Wuhan from Baidu Maps or OpenStreetMap (already used to count the $\ge 20$ hotels within $500\text{ m}$ in Table S1) to compute the empirical probability that a randomly selected hotel in Wuhan lies within $2.31\text{ km}$ of Huanan market, and report the resulting sensitivity range rather than a single combined $p \le 0.001$.

#### 3. Quantify Demographic and Temporal Caveats in the 2013–2014 Sina Check-In Mobility Analysis
* **WHY:** Using 2013–2014 Sina Visitor System check-ins to quantify late-2019 foot traffic conflates social media check-in propensity (which favors malls, universities, and tourist sites over wholesale seafood/meat markets) with physical visitor volume.
* **WHAT:** Temper the precision of the 0.12% and 0.04% check-in share claims in the Results and validate market size using time-matched business or floor-area metrics where available.
* **HOW:** Compare the physical footprint or registered vendor count of Huanan market (~650+ stalls) against the other 70 markets in the Wuhan dataset, and explicitly state in the Results text that the 2013–2014 check-in percentages reflect social media activity 5–6 years prior rather than direct 2019 pedestrian counts.

#### 4. Temper Causal Wording Distinguishing Environmental Contamination from Confirmed Animal Infection
* **WHY:** Because no live mammals at Huanan market were tested for SARS-CoV-2, PCR-positive environmental swabs on cages, carts, and drains in live-mammal stalls cannot definitively distinguish viral shedding by infected animals from contamination by infected market workers or customers.
* **WHAT:** Align the causal language in the Abstract and Discussion with the Study Limitations section.
* **HOW:** Revise the Abstract sentence ("our analyses indicate that the emergence of SARS-CoV-2 occurred via the live wildlife trade in China, and show that the Huanan market was the epicenter of the COVID-19 pandemic") to state that the analyses establish the Huanan market as the early epicenter of the COVID-19 pandemic and show a spatial association between positive environmental samples and live-mammal stalls consistent with an emergence via the wildlife trade.
