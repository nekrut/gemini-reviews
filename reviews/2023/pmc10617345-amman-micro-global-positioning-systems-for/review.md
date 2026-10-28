# Review of PMC10617345 (PMID:37877537)

**Manuscript Title:** Micro‒Global Positioning Systems for Identifying Nightly Opportunities for Marburg Virus Spillover to Humans by Egyptian Rousette Bats  
**Authors:** Amman BR, Schuh AJ, Akurut G, Kamugisha K, Namanya D, Sealy TK, Graziano JC, Enyel E, Wright EA, Balinandi S, Lutwama JJ, Kading RC, Atimnedi P, Towner JS.  
**Journal / Preprint:** *Emerg Infect Dis* (2023; `PMC10617345` / `PMID:37877537` / `10.3201/eid2911.230362`)  
**Calibration Study Cohort:** Cohort C — Wild Literature Sample (`C35` | Double-Blinded as `ANON_130`)  
**Overall Score:** **7.1 / 10.0** (Strong / Sound)  
* **Score Breakdown:** Rigor: 2.3/3.5 | Claims: 2.0/2.5 | Biology: 1.6/2.0 | Reproducibility: 1.2/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This field ecology and viral surveillance study investigates how Marburg virus (MARV) may spill over from its cave-dwelling reservoir, the Egyptian rousette bat (ERB, *Rousettus aegyptiacus*), to humans and livestock at locations distant from known roosts. The authors conducted destructive tissue sampling of 50 ERBs at Python Cave (Queen Elizabeth National Park, Uganda) to confirm ongoing MARV circulation via VP40 qRT-PCR (detecting viral RNA in 2/50 bats, 4.0%) and deployed micro-GPS loggers ($<7\text{ g}$, 5-minute fix intervals from 19:00 to 05:00) on 100 adult male ERBs ($>100\text{ g}$) across two capture sessions (50 in February 2022 and 50 in August 2022). Usable tracking data recovered from 70 bats over 1.5–4 days revealed that 68/70 (97.1%) bats foraged in agricultural areas outside the forest preserve, visiting 34 cultivated crop localities and 6 homesteads within a $1,887\text{ km}^2$ minimum convex polygon (MCP), with one-way nightly flights reaching up to 57 km. Raw GPS coordinates are withheld to protect homeowner privacy, and no anonymized movement summary table is included.

This study provides direct empirical evidence linking a confirmed MARV-infected bat roost to multi-hour nocturnal foraging in domestic fruit trees (mango, banana, papaya) adjacent to human dwellings and free-ranging livestock (pigs), offering a biologically plausible mechanism for the 9/17 historical Marburg virus disease (MVD) outbreaks that lacked direct epidemiological links to caves or mines. The primary technical limitations are an unresolved contradiction between the reported ArcGIS distance calculation method, the maximum single-night distance (57 km), and an implausible maximum total flight distance of $1,176.10\text{ km}$ over 1.5–4 days; the unstratified pooling of February and August capture cohorts; and deterministic point-estimate extrapolations of annual home visits without confidence intervals or age/sex adjustments. These issues can be addressed through straightforward data filtering, seasonal stratification, and uncertainty propagation.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Marburg virus continues to circulate endemically in the Python Cave ERB population: [Well Supported].**  
  Quantitative RT-PCR targeting the MARV VP40 gene and eukaryotic 18S rRNA internal control across necropsied tissues confirmed active MARV RNA in 2/50 (4.0%; 95% binomial CI: 0.5%–13.7%) sampled bats, consistent with historical prevalence estimates (2.5%–5.1%) at Python Cave and Kitaka mine.

* **Adult male ERBs from Python Cave routinely travel long distances outside the forest reserve to forage in cultivated crops and fruit trees adjacent to homes: [Well Supported].**  
  The recovery of 5-minute interval GPS trajectories from 70 adult male bats—corroborated by ground truthing and homeowner interviews confirming fruiting mango and banana trees visited for up to 5.5 hours overnight (Figures 3–5)—solidly establishes that ERBs bridge the spatial gap between isolated forest caves and domestic agricultural homesteads up to 57 km away.

* **Tracked ERBs had an average flight distance of 60.18 km with a range of 0.83 to 1,176.10 km over 1.5–4 days: [Fragile].**  
  There is a mathematical and physical inconsistency in the distance metrics reported in the Methods and Results. First, the Methods state that average flight distance was calculated using the ArcGIS `Generate Near Table` tool *"to calculate distances between the furthest 2 GPS locations"*, which measures maximum displacement (diameter), not cumulative flight path length. Second, while the Movement Area section states that *"the longest distance traveled by a single bat in 1 night was 57 km"* within an overall MCP of $1,887\text{ km}^2$, the GPS Tracking section reports a maximum flight distance of **$1,176.10\text{ km}$** over a battery lifespan of at most 4 nights (19:00–05:00). Even as a cumulative path length, flying $1,176\text{ km}$ in $\le 4$ nights ($\ge 294\text{ km/night}$ while spending hours stationary foraging) is incompatible with a 57 km single-night maximum and strongly suggests either an unfiltered GPS fix outlier (multipath/satellite jump common near cave entrances) or an artifact of summing all pairwise distances in the `Generate Near Table` output.

* **The Python Cave colony generates approximately 95 home visits by MARV-infected bats every 4 days (8,668 infected visits per year): [Overstated].**  
  In the Discussion, the authors multiply 40,000 bats $\times$ 2.8% infection prevalence $\times$ $6/70$ (8.57%) home visitation rate $\times$ $365/4$ to obtain an exact figure of 8,668 infected home visits per year. While useful as an illustrative order-of-magnitude calculation, presenting exact point estimates without uncertainty bounds ignores (1) wide binomial sampling variance on $6/70$ (95% CI: 3.2%–17.7%) and $2/50$ (95% CI: 0.5%–13.7%), (2) the fact that only large adult males ($>100\text{ g}$) were tracked whereas viral shedding is concentrated in juvenile bats (which have smaller body mass and potentially shorter foraging ranges), and (3) strong seasonal variation in domestic tree fruiting across the year.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Audit and Reconcile the Flight Distance Calculation and the 1,176.10 km Outlier
* **WHY:** Using ArcGIS `Generate Near Table` between the furthest two GPS locations computes maximum straight-line displacement rather than cumulative flight distance, and a value of $1,176.10\text{ km}$ over $\le 4$ nights contradicts both the $1,887\text{ km}^2$ MCP and the stated 57 km maximum single-night distance.
* **WHAT:** Clarify the exact geometric definition of flight distance, inspect the trajectories for GPS fix outliers, and report both maximum nightly one-way displacement from Python Cave and cumulative nightly path length.
* **HOW:** Filter the 5-minute GPS fixes for biologically impossible ground speeds (e.g., $>25\text{ m/s}$ or $90\text{ km/h}$ between consecutive 5-minute fixes) to remove satellite multipath jumps. Then separately compute and report: (a) **Maximum displacement radius** from Python Cave per bat (mean, median, IQR, and min–max across the 70 bats), and (b) **Cumulative nightly track length** (sum of sequential 5-minute geodesic segments per night) using the ArcGIS `Points To Line` tool rather than `Generate Near Table`.

#### 2. Stratify GPS Recovery and Foraging Metrics by Capture Season (February vs. August 2022)
* **WHY:** Fifty bats were tagged in February 2022 and 50 in August 2022, corresponding to distinct wet/dry transition and fruiting seasons in southwest Uganda, as well as the biannual birthing pulses of ERBs. Pooling all 70 recovered bats into a single MCP ($1,887\text{ km}^2$) obscures seasonal shifts in foraging range and crop visitation.
* **WHAT:** Provide a breakdown of the 70 usable datasets, flight distances, crop/home visits, and MCP areas separately for February 2022 and August 2022.
* **HOW:** Add a concise summary table listing for each cohort (February 2022, August 2022, and Combined): number of bats tagged ($n=50$ each), number of usable GPS tracks recovered, mean/median tracking duration (days), mean/median maximum distance from roost (km), number of crop and home visits, and seasonal MCP area ($\text{km}^2$), along with which cohort contained the $2/50$ MARV PCR-positive bats.

#### 3. Propagate Binomial Uncertainty in the Spillover Exposure Extrapolation
* **WHY:** Multiplying point estimates ($40,000 \times 0.028 \times 6/70$) without confidence intervals or repeat-visit adjustments treats a small sample of 6 adult male bats over 4 days as an invariant annual rate across all age/sex classes.
* **WHAT:** Report 95% confidence/uncertainty intervals around the estimated number of home visits by infected bats and explicitly note that a single bat visiting the same home on consecutive nights represents repeated exposure of the same household rather than independent households.
* **HOW:** Use Clopper–Pearson exact 95% confidence intervals for the home-visitation proportion ($6/70 = 8.6\%$, 95% CI: $3.2\%\text{–}17.7\%$) and active infection prevalence ($2.8\%$ historical or $4.0\%$ current, 95% CI: $0.5\%\text{–}13.7\%$) via Monte Carlo propagation to report an uncertainty range alongside the point estimate in the Discussion.

#### 4. Provide Privacy-Preserving Anonymized Trajectory Summary Data
* **WHY:** While withholding exact homestead GPS coordinates is appropriate to protect homeowner privacy, providing no bat-level summary table makes it impossible to verify the distribution of flight distances, foraging durations, or fix counts across the 70 bats.
* **WHAT:** Include a supplementary bat-level summary table with relative distances and durations that does not disclose geographic coordinates.
* **HOW:** Add a supplementary CSV/table with one row per bat ($N=70$) reporting: Bat ID, capture month (Feb/Aug), body mass (g), number of valid GPS fixes, tracking duration (hours/nights), maximum geodesic displacement from Python Cave (km), cumulative path length (km), and number of foraging bouts $>30\text{ min}$ in forest, crop, and home categories.

#### 5. Technical, Mathematical, and Editorial Cleanup
* **WHY:** Arithmetic and typographical errors in the text and captions should be corrected prior to final publication.
* **WHAT & HOW:**
  * **Results ("Movement Area", paragraph 1):** Correct *"where, in 2007, 2.8% of an ERB colony containing >100,000 animals, or ≈5,000 bats total, were found to be actively infected"*—$2.8\%$ of $100,000$ is $\approx 2,800$ bats (whereas $\approx 5,000$ corresponds to the $5.1\%$ prevalence reported by Towner et al., 2009). Reconcile the percentage and the total count.
  * **Methods ("Bat Capture and Processing", paragraph 2):** Fix the missing number and inverted parenthesis in *"placed in of virucidal lysis buffer"* and *"double gloves )including bite-resistant gloves if necessary)"*.
  * **Figure 3 Caption:** Fix the missing opening parenthesis in *"Google Earth Pro https://www.google.com/earth/versions )"* and *"1 hour and 30 minutes 02:00 am –3:30 am )"*.
