# Review of ANON_155

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **9.0 / 10.0** (Exemplary)  
* **Score Breakdown:** Rigor: 3.1/3.5 | Claims: 2.3/2.5 | Biology: 1.8/2.0 | Reproducibility: 1.8/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This study investigates the genomic epidemiology, introduction dynamics, and ecological drivers of the 2016 Zika virus (ZIKV) outbreak in Florida. The authors sequenced 39 ZIKV genomes directly from clinical diagnostic specimens (29 locally acquired cases and 3 travel-associated cases) and *Aedes aegypti* mosquito pools (7 pools from 24,351 trapped mosquitoes) without cell culture, validating their amplicon and enrichment sequencing protocols across multiple platforms (MiSeq and Ion S5). Combining these 39 genomes with 65 publicly available Pacific and American ZIKV genomes ($n = 104$), they perform Maximum Likelihood (PhyML) and Bayesian time-structured phylogenetic analyses (BEAST v1.8.4 across six clock/coalescent model combinations evaluated via path sampling and stepping-stone marginal likelihoods), negative-binomial branching-process simulations ($k = 0.1$), entomological abundance modeling, and international air/cruise passenger volume integration. They demonstrate that local Florida cases arose from at least 4 (and likely 17–42) independent introductions, that the two primary Miami-Dade lineages (F1 and F2) began circulating in spring 2016 (March–April) several months prior to clinical detection in July, that local $R_0$ was subcritical ($0.5\text{--}0.8$), and that the Caribbean was the primary source of introductions due to high local incidence coupled with heavy cruise and air traffic into Miami.

The manuscript is an exemplary genomic epidemiology study characterized by rigorous cross-platform sequencing validation, transparent model selection, convergent lines of phylodynamic and epidemiological evidence, and immediate open deposition of sequence data, BEAST XML files, and bioinformatic pipelines. The primary methodological caveats are minor: (1) the cruise-ship passenger estimation attributes 100% of a ship's capacity to *every* ZIKV-endemic port visited within 10 days prior to arrival in Miami, which multi-counts cruise passengers on multi-port Caribbean itineraries relative to point-to-point airline passengers; and (2) a discrepancy between the Methods text and Extended Data Figure 4e caption regarding which three Florida lineages (F1–F3 vs. F1, F2, F4) were used in the Miami-Dade cluster-sampling likelihood.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Local ZIKV transmission in Florida was driven by *Ae. aegypti* mosquitoes and established by March–April 2016, several months before initial detection in July 2016: [Well Supported].**  
  Of 24,351 mosquitoes trapped in Miami-Dade County, 99.8% were *Ae. aegypti*, yielding 8 ZIKV-positive pools (MLE infection rate $0.061\%$, 95% CI: $0.028\%\text{--}0.115\%$), and weekly human cases correlated with trap-night *Ae. aegypti* abundance (Spearman $r = 0.61$). Time-structured BEAST analyses show strong root-to-tip temporal signal ($1.10 \times 10^{-3}$ subs/site/yr in TempEst; $1.21 \times 10^{-3}$ subs/site/yr under UCLN + Bayesian Skyline) and consistently place the tMRCAs of the two main Miami-Dade transmission clades (F1 and F2) in March–April 2016 (95% HPD: January–May 2016) across all six tested clock and coalescent models (Extended Data Table 1a).

* **The Florida outbreak had a subcritical basic reproductive number ($R_0 \approx 0.5\text{--}0.8$) and resulted from at least 4—and likely 17–42—independent introductions: [Well Supported].**  
  Phylogenetically, F4 falls in a Central American clade distinct from Clade A (F1–F3), and the internal nodes uniting F1–F3 (Clade A) and F1–F2 (Clade B) date to summer 2015, which would require ~1 year of undetected overwinter persistence ($p \approx 0.5\%$ under birth–death simulations at $R_0 \le 0.8$). The negative-binomial branching-process model independently estimates $R_0 = 0.35\text{--}0.8$ from the ratio of 241 local to 320 travel cases and $R_0 = 0.5\text{--}0.9$ from observing 3 distinct clusters among 27 sequenced Miami-Dade human cases, with sensitivity analyses confirming robustness to preferential sampling ($\alpha = 2$) and differential under-reporting (Extended Data Fig. 4).

* **ZIKV moved between spatially distinct transmission zones within Miami-Dade County: [Well Supported].**  
  Both F1 and F2 lineages were recovered across multiple transmission zones (Wynwood, Miami Beach, and Little River, located within ~5 km of one another), and both F1 and F2 viruses were sequenced from *Ae. aegypti* pools collected in the exact same mosquito trap 26 days apart (trap samples 5 and 8, Fig. 2b).

* **The Caribbean was the primary geographic source of ZIKV introductions into Miami, driven by high regional incidence and heavy passenger traffic (~60%–70% of infected travelers): [Moderately Supported].**  
  Lineages F1–F3 cluster within Caribbean sequences (Dominican Republic and Guadeloupe), 67% of Florida travel-associated ZIKV cases reported Caribbean travel (Fig. 3e), and expected Caribbean importations correlate with weekly observed travel cases ($r = 0.8$). However, the calculation of cruise-ship passenger traffic (Methods, line 170) counts a ship's full passenger capacity toward *every* ZIKV-transmitting country/territory visited within 10 days prior to arrival in Miami. Because a single Caribbean cruise typically calls at 3–5 Caribbean ports during a 10-day itinerary, summing ship capacity across each visited port multiplies the true number of unique cruise travelers by the number of port calls, inflating the estimated 2.4 million Caribbean cruise travelers (Fig. 3b) and the resulting Caribbean share of expected importations ($\lambda = \sum_i C_i I_i / N_i$) relative to single-origin flights.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Correct Multi-Port Double-Counting in Cruise Ship Passenger Volume and Expected Importations
* **WHY:** In the Methods (line 170), the authors state: *"Every country/territory with ZIKV transmission visited by a cruise ship 10 days... prior to arrival was counted as contributing the ship's capacity worth of passengers to Miami to the month of arrival."* If a 3,000-passenger cruise ship visits three Caribbean islands on a 7-day itinerary before returning to Miami, this rule counts 9,000 passengers entering Miami and weights their exposure as three full 10-day residential person-periods rather than brief ~8-hour daytime port excursions by 3,000 people.
* **WHAT:** Adjust the cruise-ship exposure model so that each arriving ship contributes its passenger capacity once to total traveler counts, and weight country-specific infection probabilities by actual port-stay duration (or fraction of itinerary days spent in each port).
* **HOW:** For each ship arrival $s$ with capacity $C_s$ visiting ports $p \in P_s$ during the 10-day window, set the unique passenger count to $C_s$ in Figure 3b and Extended Data Figure 6, and compute expected infected cruise travelers as $\lambda_{\text{cruise}} = \sum_s C_s \sum_{p \in P_s} w_{sp} (I_p / N_p)$, where $w_{sp} \le 1/|\text{days}|$ reflects the fraction of exposure time spent in port $p$ (plus a sensitivity parameter $\beta_{\text{port}} \in [0.1, 1.0]$ for lower daytime onshore vector exposure compared to resident populations).

#### 2. Reconcile the Miami-Dade Genetic Cluster Count Between Methods and Extended Data Figure 4
* **WHY:** In the Methods ("Expected number and distribution of local cases from Zika virus importations," line 152), the text states that the hypergeometric sampling likelihood was calculated for *"observing 3 distinct genetic clusters (F1, F2 and F3) representing 3 introduction events in a sample of 27 ZIKV genomes from Miami-Dade County."* However, the caption to Extended Data Figure 4e (line 13 of the second section) states *"Log likelihood of observing 3 clusters (i.e., ZIKV lineages F1, F2, and F4, Fig. 2a) in 27 sequenced cases."* Furthermore, if all 4 lineages (F1–F4) were sampled in Florida (29 local human genomes total, 27 from Miami-Dade), it should be explicitly clarified which single-case lineage (F3 or F4) was collected outside Miami-Dade County (e.g., Broward or Palm Beach).
* **WHAT & HOW:** Cross-check Supplementary Table 1a to identify which three lineages were present among the 27 Miami-Dade human genomes, and harmonize the text in the Methods (line 152) and Extended Data Figure 4e caption so they refer to the exact same three lineages.

#### 3. Account for Identical/Near-Identical Co-Introducers Within Lineages F1 and F2
* **WHY:** The tMRCA analysis of F1 and F2 (March–April 2016) assumes each clade represents a single introduction into Florida, whereas the branching-process analysis estimates 17–42 introductions (meaning multiple travelers likely introduced closely related Caribbean Clade A viruses that coalesce shortly before or during the Florida outbreak).
* **WHAT:** Quantify how multiple co-introductions from a low-diversity source population (e.g., the Dominican Republic clade) affect both the cluster-count MLE of $R_0$ and the inferred timing of earliest local transmission in Florida.
* **HOW:** In the hypergeometric cluster-sampling simulation (Methods, line 152), add a coalescence probability $p_{\text{coal}}$ (estimated from the pairwise genetic diversity of Caribbean Clade A sequences) whereby two independent introductions from the same source clade are grouped into a single observed phylogenetic lineage, and report the updated MLE range for $R_0$.

#### 4. Technical, Mathematical, and Editorial Cleanup
* **WHY:** Minor typographical errors in mathematical equations and table headers should be corrected for clarity.
* **WHAT & HOW:**
  * **Methods, "Relative monthly *Ae. aegypti* abundance" (Line 92):** Close the missing parenthesis in the Poisson transformation equation: change `λ = - log ( 1 - P ( Y = 1 )` to $\lambda = -\log(1 - P(Y = 1))$.
  * **Methods, "Multivariable/Statistical Analysis" (Line 78):** Fix `Supplementary Table 1` reference to `Supplementary Table 1a` for consistency with the rest of the text.
  * **Methods, "Expected number of travelers infected with Zika virus" (Line 183):** Change `Extended Data 7b` to `Extended Data Fig. 7a` (since panel `a` shows the projected attack-rate proportions, whereas panel `b` shows the weekly incidence correlation).
