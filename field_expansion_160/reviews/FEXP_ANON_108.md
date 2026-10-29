# Forensic Review of `FEXP_ANON_108`

**Overall Score:** **6.1 / 10.0** (Mixed / Salvageable) | **Scientific Core Score:** **4.6 / 8.0**
* **Score Breakdown:** Rigor: 2.0/3.5 | Claims: 1.3/2.5 | Biology: 1.3/2.0 | Reproducibility: 1.5/2.0

---

## 1. Blinded Metadata Perception

* **Perceived Field & Subfield:** Macroecology / Urban Ecology / Biogeography (Species–area relationships, socio-ecological drivers, and future climate/urbanization exposure of terrestrial vertebrate richness across Mexican municipalities).
* **Study Design Archetype:** National-scale macroecological synthesis filtering 6.76 million SNIB occurrence records across 2,731 terrestrial vertebrate species via `vegan::specaccum` rarefaction completeness (slope $\le 0.05$) down to 389 Mexican municipalities, fitting 20 species–area relationship (SAR) models (`sars` package), Random Forest partial-dependence models (`rfUtilities`) on 19 predictors (with and without area residualization), and a composite future risk index (CMIP5 RCP2.6/8.5 temperature anomalies + LUCC urban expansion + population-derived UHI).
* **Temporal & Venue Signals:** Post-2021 Latin American macroecology study with open dataset and R code archived on Figshare (`14881755`).

---

## 2. Executive Summary & Editorial Verdict

This study compiles terrestrial vertebrate occurrence records (amphibians, reptiles, mammals, and birds) from Mexico's National Biodiversity Information System (SNIB) across INEGI urban and rural polygons, retaining 389 municipalities that pass a species-accumulation completeness threshold (slope $\le 0.05$). The authors compare log-log urban vs. rural species–area relationships (SAR), fit 20 untransformed SAR functional forms via AICc multimodel inference, use Random Forest models across 19 ecological and socioeconomic predictors (both raw and area-residualized) to identify drivers of urban richness, and construct a multivariate risk index combining projected 2070 urban expansion, CMIP5 temperature anomalies, and an empirical population-based urban heat island (UHI) proxy.

**Editorial Verdict: Major Revision (Mixed / Salvageable).** The dataset curation (filtering 6.76 million SNIB records with taxonomic harmonization and `specaccum` rarefaction completeness) and the decision to re-run Random Forest models on area-residualized richness (Fig. 2b, which reveals that GDP, protected area size, ecoregion count, and primary-sector employment lose significance once urban area is controlled) are commendable and openly reproducible via Figshare. However, several methodological and interpretive flaws require correction:
1. **Unvalidated 1988 US Population Power-Law Used as "Urban Heat Island" & Omitted Equation:** The UHI component of the future risk index is not derived from remote-sensing land surface temperature (e.g., MODIS) or meteorological stations, but by plugging 2020 Mexican municipal population into an empirical equation ($\Delta T = a P^b$, $a = 1.74 \times 10^{-3}, b = 0.45$) calibrated by Karl et al. (1988) for mid-latitude US weather stations (Methods, lines 67–69)—and the equation itself is omitted from line 68. Because this proxy is a deterministic function of 2020 population size, populous boroughs of Greater Mexico City (`Iztapalapa`, `Ecatepec`, `Gustavo A. Madero`) automatically receive maximal "UHI" risk regardless of elevation, albedo, or vegetation, and 2020 population is combined mismatchingly with 2070 climate/LUCC projections.
2. **Overinterpretation of Tied, Low-$R^2$ Sigmoidal SAR Models:** In Table 2, untransformed SAR models explain very little variance ($R^2 = 0.028\text{--}0.038$ for amphibians, $0.110$ for birds, $0.137$ for mammals, $0.230\text{--}0.280$ for reptiles), and linear, convex-down (`PowerR`), and sigmoidal (`EPM-1`) forms are statistically indistinguishable ($\Delta\text{AICc} = 0.03\text{--}0.23$ in reptiles and mammals). Inferring city-level "carrying capacity" and "biotic homogenization" from these weak cross-sectional fits is unwarranted.
3. **Internal Geographic & Hypothesis Contradictions:** The Abstract claims *"Mexican cities in the northeast region may be at a higher risk"*, whereas Results (lines 119, 124) identifies northwestern/north-central cities (*Hermosillo, Juárez, Chihuahua*) and central valleys (*Iztapalapa, Puebla, Ecatepec, León*), before contradictorily stating in the same paragraph that the highest-risk municipalities *"are concentrated in three states (Distrito Federal, Mexico, and Jalisco)"*.

### Assessment of Specific Claims

* **Urban area is the primary scaling driver of urban vertebrate richness across Mexican municipalities, and controlling for urban area eliminates the effects of GDP, ecoregion count, and primary-sector share while leaving topographic complexity significant (Results, line 111; Fig. 2a–b): `[Well Supported]`**  
  Comparing Fig. 2a (raw richness) with Fig. 2b (residuals from log-log richness vs. urban area regression) cleanly demonstrates that municipal GDP, urban protected area extent, ecoregion overlap, and primary-sector workforce share act primarily as collinear proxies for city size rather than direct area-independent drivers.
* **Urban species richness across Mexican municipalities follows a sigmoidal SAR curve reflecting a species carrying capacity and biotic homogenization in large cities (Results, line 79; Table 2; Discussion, lines 137–139): `[Overstated]`**  
  In Table 2, $R^2$ values are low ($0.028\text{--}0.280$) because the 389 municipalities span desert, temperate montane, and wet tropical biomes with vastly different regional species pools. For reptiles, the Linear model ($\text{AICc} = 27.023$, weight $= 0.158$), convex-down `PowerR` ($\text{AICc} = 27.051$, weight $= 0.156$), and sigmoidal `EPM-1` ($\text{AICc} = 27.084$, weight $= 0.153$) are tied ($\Delta\text{AICc} \le 0.06$); for mammals, `EPM-1` and convex-down `PowerR` differ by $\Delta\text{AICc} = 0.226$. Furthermore, no taxonomic beta-diversity (jaccard/Sorensen similarity) analysis was performed to test biotic homogenization.
* **The multivariate risk index accurately captures future exposure to urban heat islands (UHI), urban expansion, and climate change, with highest risk in northeast Mexico (Abstract; Methods, lines 67–71; Results, lines 119–124): `[Methodologically Flawed]`**  
  First, the UHI term is merely $a \cdot P_{2020}^{0.45}$ calibrated on 20th-century US cities, ignoring actual surface temperature, aridity, altitude, and projected 2070 population growth. Second, the Abstract's claim that *"northeast"* cities face the highest risk contradicts the Results text (lines 119, 124), which highlights *Hermosillo* (Sonora, northwest), *Juárez* and *Chihuahua* (Chihuahua, north-central/northwest), and central Mexican municipalities (*Iztapalapa, Puebla, Ecatepec, León*), and then contradicts itself again in line 124 by stating that the highest-risk municipalities are concentrated in *"three states (Distrito Federal, Mexico, and Jalisco)"*.
* **Negative association of primary-sector employment (porPob) with raw urban richness indicates that high social marginalization reduces green spaces and species (Discussion, line 141): `[Overstated]`**  
  In Table 1 (line 33), the authors hypothesized the exact opposite: that higher `porPob` would *increase* urban species richness via rural mass/rescue effects. When Fig. 2a showed a negative effect on raw richness (which vanished entirely after controlling for urban area in Fig. 2b, because agricultural municipalities simply have smaller urban footprints), the Discussion inverted the interpretation of `porPob` into a proxy for "social marginalization" without acknowledging that the effect is a city-size confounder.

---

## 3. Forensic Defect Inventory

### 3.1. Unvalidated US Population Power-Law UHI Proxy & Omitted Equation (Pillar 3, Pillar 6 & Pillar 7)
* **Location:** Methods ("Multivariate future risk index", lines 67–71).
* **Defect 1 (Missing Equation):** Line 67 ends with *"The UHI is a simple approximation based on empirical relationships of the form:"*, followed by a blank line (line 68) where the formula was omitted before line 69 defines parameters $a = 1.74 \times 10^{-3}$ and $b = 0.45$.
* **Defect 2 (Physical & Temporal Misspecification):** Applying Karl et al.'s (1988) US weather-station population regression to 2020 Mexican municipalities treats individual administrative municipalities within contiguous megacities (e.g., *Iztapalapa*, *Ecatepec*, *Gustavo A. Madero* within Greater Mexico City) as isolated cities, and mixes static 2020 population counts with 2070 climate and land-use projections.

### 3.2. Uninformative SAR Model Selection & Missing Sample Sizes per Taxon (Pillar 3, Pillar 4 & Pillar 7)
* **Location:** Methods (lines 50, 55), Results (line 79; Table 2, lines 85–107), and Discussion (lines 137–139).
* **Defect 1 (Extreme Model Uncertainty & Low $R^2$):** In Table 2, Akaike weights for the top model are only `0.118` (amphibians, $R^2 = 0.038$), `0.158` (reptiles, $R^2 = 0.230$, tied with `PowerR` and `EPM-1`), `0.271` (mammals, $R^2 = 0.137$, $\Delta\text{AICc} = 0.23$ vs `PowerR`), and `0.341` (birds, $R^2 = 0.110$).
* **Defect 2 (Ambiguous Sample Size After `< 5` Species Exclusion):** Methods (line 50) states that out of 389 municipalities, those with $< 5$ species (e.g., 66 for amphibians, 8 for birds, plus unstated counts for reptiles and mammals) were excluded from both the SAR and Random Forest analyses, yet the exact $N$ analyzed for each taxon in Table 2 and for total richness in the Random Forest (Fig. 2) is not reported in the main text.

### 3.3. Geographic & Variable-Label Contradictions (Pillar 5 & Pillar 7)
* **Geographic Contradictions:** Abstract (line 5) states *"northeast region"*; Results (lines 119, 124) lists *Hermosillo, Juárez, and Chihuahua* (northwest / north-central) and *Iztapalapa, Puebla, Ecatepec, León* (central), and then at the end of line 124 states *"concentrated in three states (Distrito Federal, Mexico, and Jalisco)"* (even though none of Hermosillo, Juárez, Chihuahua, Puebla, or León is in those three states).
* **Table 1 Variable Label Error (Line 28):** Table 1 writes `"Human total density (Dens_total) / Human rural density (Dens_urban)"`, mislabeling `Dens_urban` as rural density.
* **Table 2 Column Header:** Methods (line 55) states model selection used small-sample corrected `AICc`, whereas Table 2 (line 87) labels the column `AIC`.

---

## 4. Quantitative Rubric Scoring

| Rubric Dimension | Score | Max | Forensic Justification |
| :--- | :---: | :---: | :--- |
| **1. Methodological & Statistical Rigor** | **2.0** | 3.5 | Sound `specaccum` rarefaction completeness filtering and informative area-residualized Random Forest analysis (Fig. 2b); penalized for the 1988 US population-based UHI formula, unacknowledged $\Delta\text{AICc}$ ties and low $R^2$ ($0.03\text{--}0.28$) in Table 2, and unstated post-filtering $N$ per taxon. |
| **2. Claim-to-Evidence Alignment** | **1.3** | 2.5 | Area-scaling conclusions are well supported, but claims of sigmoidal carrying capacity / biotic homogenization, post-hoc reversal of the `porPob` hypothesis, and inconsistent geographic risk claims (`northeast` vs `northwest/north` vs `DF/Mexico/Jalisco`) overreach the evidence. |
| **3. Data Integrity & Biological Plausibility** | **1.3** | 2.0 | Careful curation and taxonomic harmonization of 6.76M SNIB records across 389 municipalities; UHI population proxy lacks physical/microclimatic realism across heterogeneous Mexican elevations and biomes. |
| **4. Reproducibility & Data Integrity** | **1.5** | 2.0 | Open data and R code provided on Figshare (`14881755`); docked for the omitted UHI equation in line 68, `Dens_urban` mislabeling in Table 1, and geographic contradictions between Abstract and Results. |
| **Total Composite Score** | **6.1** | **10.0** | **Mixed / Salvageable** (**Scientific Core Score: 4.6 / 8.0**) |
