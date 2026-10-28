# Review of ANON_190

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **4.5 / 10.0** (Flawed / Overstated)  
* **Score Breakdown:** Rigor: 1.2/3.5 | Claims: 1.1/2.5 | Biology: 1.0/2.0 | Reproducibility: 1.2/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This study applies a two-stage presence-only Maximum Entropy (MaxEnt) ecological niche modeling (ENM) framework, alongside SaTScan space-time permutation and Ripley's $K$ spatial cluster analysis, to map H5N1 highly pathogenic avian influenza (HPAI) poultry outbreak risk across the Philippines. In Stage 1, 38 satellite remote sensing and demographic variables (2010–2021 CHIRPS precipitation, MODIS LST and NDVI, WorldPop human population density, and land cover) are used to model the distributions of the 10 most frequently reported bird species in eBird (2010–2022). In Stage 2, these 10 predicted avian raster layers are combined with the 38 environmental covariates to predict 188 unique H5N1-HPAI poultry farm outbreaks (FAO EMPRES-i+, 2022–2023). The authors report an $\text{AUC}_{\text{ROC}}$ of $0.936 \pm 0.026$, identifying December precipitation (19.9% permutation importance), Eurasian Tree Sparrow (18.1%), and Zebra Dove (12.0%) as the top predictors, and conclude that these two synanthropic species pose a heightened H5N1 spillover risk in Metro Manila and Central Luzon.

While compiling spatial outbreak records and environmental layers for Philippine H5N1 surveillance addresses a practical veterinary public health need, the study's core conclusions rest on severe spatial ascertainment bias, collinearity confounding, and internal contradictions. Specifically, unfiltered eBird citizen-science checklists are heavily concentrated in densely populated urban/peri-urban centers (Metro Manila and Central Luzon), and selecting the 10 most frequently observed species simply captures human observer effort and urban synanthropy rather than wild avian reservoir ecology. Feeding these human-density-driven bird rasters into a poultry outbreak model—while omitting or eliminating gridded chicken and duck density (described in Section 3.2 but absent from all results)—confounds urban/agricultural reporting density with biological spillover. Furthermore, the Results text directly contradicts itself regarding the direction of association for June precipitation, and the SaTScan cluster geometries are mathematically inconsistent with the geographic provinces they are claimed to span. Substantial methodological restructuring is required before the risk maps or species claims can be considered valid.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Eurasian Tree Sparrow and Zebra Dove distributions are major drivers of H5N1-HPAI poultry outbreak risk (18.1% and 12.0% permutation importance; Table 2) and face elevated spillover risk: [Methodologically Flawed].**  
  In Stage 1, human population density and NDVI were top predictors for all 10 eBird species (Table 1) because uncorrected eBird checklists cluster around urban birdwatchers in Metro Manila and Central Luzon, and the Eurasian Tree Sparrow (*Passer montanus*) and Zebra Dove (*Geopelia striata*) are ubiquitous urban/peri-urban synanthropes. Because commercial poultry outbreak reports in Luzon also cluster near major population and agricultural centers, the Stage 2 MaxEnt model uses Stage 1 predicted rasters (which are smooth proxies for human/urban density and eBird sampling effort) to predict poultry outbreaks. This spatial confounding does not constitute evidence of viral spillover or vector transmission.

* **The Stage 2 MaxEnt model achieves robust predictive accuracy ($\text{AUC}_{\text{ROC}} = 0.936 \pm 0.026$; Fig. 6a): [Overstated].**  
  Model validation relied on a random 80%/20% train/test split of 188 spatially clustered poultry outbreaks using 10,000 random background points across the entire Philippine archipelago (7,600+ islands, 72.9% tree cover). When presence points are tightly clustered in Central Luzon and background points are drawn nationwide from forested and mountainous islands where commercial poultry farms do not exist, random holdout points fall immediately adjacent to training points, inflating $\text{AUC}_{\text{ROC}}$ via spatial autocorrelation and trivial land-cover discrimination.

* **Precipitation in June and December and human population density exhibit specific nonlinear/directional correlations with H5N1-HPAI risk (Section 4.2, Fig. 6b–f): [Methodologically Flawed].**  
  Paragraph 5 of Section 4.2 contains a direct self-contradiction in consecutive sentences: *"We observed an inverse correlation between precipitation levels in December and June, population density, and the risk of H5N1-HPAI transmission (Figures 6b, 6e, and 6f). In contrast, we identified a positive correlation between the presence of the Eurasian Tree Sparrow, Zebra Dove, and precipitation levels in June in response to H5N1-HPAI outbreak (Figures 6d and 6e)."* June precipitation cannot be simultaneously inversely and positively correlated with H5N1 risk in the same response curve, and the figure citations in the text (`6d and 6e`) do not match the caption of Figure 6 (`6c: Eurasian Tree Sparrow`, `6d: Zebra Dove`, `6e: Population Density`, `6f: Precipitation in June`).

* **SaTScan space-time permutation identified three clusters spanning 43.41, 28.51, and 21.50 $\text{km}^2$ across multi-province regions (Section 4.2, Fig. 5b): [Methodologically Flawed].**  
  Section 4.2 states that Cluster 1 *"spanned 43.41 square kilometers, including Metro Manila, extending to Bulacan, Rizal, Cavite, and Laguna"*. A circle of area $43.41\text{ km}^2$ has a radius of only $3.72\text{ km}$, which cannot physically extend across Metro Manila, Bulacan, Rizal, Cavite, and Laguna (an area exceeding $5,000\text{ km}^2$). A circle with a *radius* of $43.41\text{ km}$ has an area of $\pi (43.41)^2 \approx 5,920\text{ km}^2$, indicating that the authors misreported the SaTScan cluster radii (in km) as areas (in $\text{km}^2$).

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Control for eBird Spatial Sampling Bias and Include Poultry Density as a Baseline Exposure
* **WHY:** Unfiltered eBird occurrences reflect where birdwatchers go (roads and cities), and omitting domestic chicken and duck density (despite processing GLW v4 data in Section 3.2) forces synanthropic bird rasters to act as proxies for agricultural/human density.
* **WHAT:** Apply target-group background weighting to Stage 1 eBird models, and force gridded chicken and duck density into the Stage 2 H5N1 poultry outbreak model to test whether wild bird distributions add predictive value above host poultry density.
* **HOW:**
  1. In Stage 1 MaxEnt, replace uniform random background points with a target-group background raster derived from the spatial density of all eBird checklists across the Philippines (2010–2022) so that observer effort is factored out of the species habitat suitability predictions.
  2. In Stage 2, compare a baseline model containing only environmental covariates + GLW v4 chicken/duck density + human population density against the full model adding avian distribution rasters, and report the jackknife gain and $\Delta\text{AIC}_c$ (`ENMeval` package in R). Explain in Section 4.2 what happened to the chicken and duck density layers described in Section 3.2.

#### 2. Implement Spatial Block Cross-Validation Instead of Random 80/20 Partitioning
* **WHY:** Random 80/20 splits on clustered outbreak farms in Central Luzon leak spatial autocorrelation between training and test sets, producing artificially high $\text{AUC}_{\text{ROC}}$ ($0.936$).
* **WHAT:** Re-evaluate both Stage 1 and Stage 2 MaxEnt models using spatial block cross-validation and restrict background sampling to agricultural/poultry-producing regions or weight by poultry presence.
* **HOW:** Use the `blockCV` or `ENMeval` R package to partition the Philippines into spatial blocks (or latitudinal/regional bands separating Northern/Central Luzon, Southern Luzon, Visayas, and Mindanao) and report spatially blocked $\text{AUC}_{\text{ROC}}$, Continuous Boyce Index (CBI), and 10% training omission rates.

#### 3. Include Relevant Waterfowl Reservoir Guilds (Anseriformes and Charadriiformes)
* **WHY:** Selecting only the 10 most common eBird species overall restricts the study to urban passerines, doves, and kingfishers while excluding migratory ducks, egrets/herons (beyond Little Egret), and shorebirds that are the actual primary biological reservoirs of H5N1-HPAI.
* **WHAT:** Construct guild-specific or species-specific ENM layers for migratory and resident Anatidae (ducks/waterfowl) and Ardeidae/Charadriiformes recorded in Philippine eBird checklists.
* **HOW:** Filter the Philippine GBIF/eBird dataset for Anseriformes and Charadriiformes species with $\ge 50$ unique spatial occurrences (or pool migratory Anatidae into a waterfowl guild layer), run bias-corrected MaxEnt models, and include these reservoir layers in Stage 2 alongside the synanthropic species.

#### 4. Correct Internal Contradictions and Misreported Spatial Statistics
* **WHY:** Contradictory statements about covariate directions and confusion between circle radius and area undermine the credibility of the quantitative results.
* **WHAT & HOW:**
  * **Section 4.2 (line 169) and Fig. 6:** Inspect the marginal vs. single-variable MaxEnt response curves for June precipitation (Fig. 6f), December precipitation (Fig. 6b), and population density (Fig. 6e). Rewrite the paragraph to accurately describe the non-monotonic/unimodal or monotonic shapes shown in the plots, remove the contradictory statement that June precipitation is both inversely and positively correlated with H5N1 risk, and fix the figure panel pointers (`Fig. 6c` for Eurasian Tree Sparrow, `Fig. 6d` for Zebra Dove, `Fig. 6e` for Population Density, `Fig. 6f` for Precipitation in June).
  * **Section 4.2 (line 145):** Verify the SaTScan v10.1 output file (`43.41`, `28.51`, and `21.50` km). Change *"spanned 43.41 square kilometers"* (and clusters 2 and 3) to *"had a radius of 43.41 km (spanning an area of 5,920 km²)"* (or report the exact SaTScan radius and computed area $\pi r^2$).
  * **Table 2 (line 163) & Fig. 4 caption (line 114):** Fix typos *"Eurarsian Tree Sparrow"* in Table 2 and *"Philppines"* / *"central luzon"* in Figure 4 and 5 captions.
