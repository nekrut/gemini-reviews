# Forensic Review of `FEXP_ANON_104`

**Overall Score:** **2.2 / 10.0** (Fundamentally Invalid) | **Scientific Core Score:** **1.7 / 8.0**
* **Score Breakdown:** Rigor: 0.6/3.5 | Claims: 0.5/2.5 | Biology: 0.6/2.0 | Reproducibility: 0.5/2.0

---

## 1. Blinded Metadata Perception

* **Perceived Field & Subfield:** Agricultural Ecology / Species Distribution Modeling (MaxEnt habitat suitability modeling of kiwifruit *Actinidia* spp. in Shaanxi Province, China under CMIP6 SSP scenarios).
* **Study Design Archetype:** Regional single-province MaxEnt modeling study (`n = 99` spatially thinned occurrence points across Shaanxi Province, 11 environmental predictors filtered from 26 WorldClim/HWSD/DEM variables, `ENMeval` parameter tuning) projecting habitat suitability and centroid shifts under SSP126, SSP245, SSP370, and SSP585 (2050 and 2070), plus a qualitative overlay with 31 producing counties.
* **Temporal & Venue Signals:** Recent (2025) regional MaxEnt study exhibiting pervasive machine-translation errors, omitted equations, and physically impossible numerical values.

---

## 2. Executive Summary & Editorial Verdict

This study uses `ENMeval`-tuned MaxEnt (`RM = 2.5`, `FC = LQH`) on 99 thinned occurrence records of kiwifruit (*Actinidia* spp.) in Shaanxi Province to model current suitability and future projections (2050 and 2070) under SSP126, SSP245, SSP370, and SSP585 using `BCC-CSM2-MR` (misspelled `BBC_CSM`), and overlays the current suitability map with 31 kiwifruit-producing counties.

**Editorial Verdict: Reject (Fundamentally Invalid).** The manuscript contains severe physical impossibilities, unit-conversion disasters, and internal mathematical contradictions across almost every section:
1. **Physically Impossible Soil Moisture Values ($6,508\text{--}11,333\text{ mm}$):** The authors misread unscaled integer raster IDs/codes from the HWSD `Soil Water Regime` (`R_SWR`, listed as unitless `-` in Table 1, line 70) as literal millimeters of soil water, asserting in Methods (line 36) and Conclusions (line 214) that during the fruit-swelling period, *"soil water content needs to be maintained in the appropriate range of 6508.30 - 11332.82 mm"* ($6.5$ to $11.3\text{ meters}$ of liquid water in a $30\text{--}60\text{ cm}$ root zone—roughly 15 times the annual precipitation of Shaanxi Province).
2. **Conflation of Model Suitability Thresholds with Provincial Physical Geography & Inverted Barometric Physics:** In Methods (line 36), the authors state that across Shaanxi Province, *"The annual temperature variation ranges from 31.57°C to 35.62°C, and the altitude gradient covers from 6 meters to 678.03 meters"*. In reality, Shaanxi Province reaches $3,767\text{ m}$ (Mount Taibai); the numbers `31.57°C to 35.62°C` and `678.03 meters` were copied directly from the authors' own Table 3 (`SI > 50%` threshold ranges for `BIO7` and `DEM`) and misrepresented as the physical geography of Shaanxi Province. In Discussion (line 197), the authors further assert that *"At higher altitudes, lower temperatures are observed, along with **higher atmospheric pressure** and radiation intensity"*, inverting basic atmospheric physics.
3. **100-Fold Unit Mistranslation Errors (`million km²` vs. `10^4 km²`):** In Results (line 161), machine translation of the Chinese unit `万 km²` ($10^4\text{ km}^2$) into `million square kilometers` ($10^6\text{ km}^2$) results in the claim that high-suitability area in Shaanxi decreases from $13,100\text{ km}^2$ to *"0.27, 0.55, 0.42, and 0.5 million square kilometers"* ($270,000\text{--}550,000\text{ km}^2$, exceeding the entire $205,800\text{ km}^2$ land area of Shaanxi Province).

### Assessment of Specific Claims

* **Soil moisture of 6,508–11,333 mm is required to maintain mountain kiwifruit orchards during the fruit-swelling period (Methods, line 36; Table 3, line 141; Conclusions, line 214): `[Methodologically Flawed]`**  
  A $30\text{--}60\text{ cm}$ soil layer cannot physically hold $6,508\text{--}11,333\text{ mm}$ ($6.5\text{--}11.3\text{ m}$) of water. The numbers `6508.30~11332.82` are unscaled raster grid identifiers/codes from the HWSD dataset (`R_SWR`) that were falsely interpreted as millimeters of soil water.
* **Mean temperature of the coldest quarter (BIO11, 0.69–3.83°C) and elevation (DEM, 282–678 m) are the top macro-environmental predictors of current kiwifruit cultivation in Shaanxi (Abstract; Results, line 131; Table 3): `[Moderately Supported]`**  
  The concentration of commercial kiwifruit orchards along the northern foothills of the Qinling Mountains and Hanjiang basin at low-to-middle elevations ($282\text{--}678\text{ m}$) with mild winters (`BIO11` $\approx 0.7\text{--}3.8^\circ\text{C}$) reflects known horticultural planting zones in Shaanxi, although restricting training data to existing commercial orchards models anthropogenic planting preference rather than the wild niche of *Actinidia* spp.
* **High-suitability kiwifruit habitat will shrink by 79.12% under SSP126 (the lowest emission pathway) vs. 58.01%–61.70% under SSP245/SSP585, while the centroid migrates northwestward (Abstract, line 9; Results, lines 161, 169): `[Fragile]`**  
  First, the paper offers no mechanistic explanation for why the mildest mitigation pathway (`SSP126`) causes a much larger collapse of high-suitability habitat ($-79.12\%$, down to $2,700\text{ km}^2$) than the most extreme fossil-fuel pathway (`SSP585`, $-61.70\%$, $5,000\text{ km}^2$). Second, in Results (line 169), the narrative compass directions contradict the reported coordinates: under `SSP126`, the centroid moves from $(108.786^\circ\text{E}, 33.853^\circ\text{N})$ to $(108.571^\circ\text{E}, 33.810^\circ\text{N})$ (southwest, not northwest), and under `SSP245` from 2060 to 2080 the text claims it moves *"in a southwesterly direction to the northern part of Chang'an District with coordinates 108.719°E, 34.177°N"* (which is north-northwest of the starting point $33.853^\circ\text{N}$).
* **Spatial coupling between main kiwifruit producing counties and climate suitability zones is 78.80% (Discussion, line 180) or 82.3% (Conclusions, line 214): `[Methodologically Flawed]`**  
  Discussion (line 180) states that 6 and 18 out of 31 main producing counties ($24 / 31 = 77.42\%$) fall in medium and high suitability zones and reports the spatial overlap as **78.80%**, whereas Conclusions (line 214) reports the exact same spatial coupling degree as **82.3%** without explanation.

---

## 3. Forensic Defect Inventory

### 3.1. Physically Impossible Quantities & Misattributed Thresholds (Pillar 3 & Pillar 6)
* **Location:** Methods (line 36), Table 1 (line 70), Table 3 (lines 138–141), Discussion (line 197), and Conclusions (line 214).
* **Defect 1 (Soil Moisture of 6.5–11.3 Meters):** Table 1 (line 70) defines `R_SWR` as unitless `Soil Water Regime (-)` from HWSD v1.0. Table 3 (line 141) lists its threshold range as `6508.30~11332.82` (mean `8920.56`). In Methods (line 36) and Conclusions (line 214), the authors attach the unit `mm` and claim that orchard soil water content during fruit swelling must be maintained at `6508.30 - 11332.82 mm`.
* **Defect 2 (Provincial Geography Copied from Model Output Table 3):** Methods (line 36) claims that Shaanxi Province's annual temperature range is `31.57°C to 35.62°C` and its altitude gradient is `6 meters to 678.03 meters`. Both intervals (`31.57°C~35.62°C` and upper bound `678.03m`) are identical to the `SI > 50%` model threshold values in Table 3 (lines 139–140), and are false for Shaanxi Province (where Mount Taibai is $3,767\text{ m}$).
* **Defect 3 (Inverted Altitude–Pressure Relationship):** Discussion (line 197) states: *"At higher altitudes, lower temperatures are observed, along with higher atmospheric pressure and radiation intensity."* Atmospheric pressure decreases exponentially with altitude.

### 3.2. Severe Numerical, Area, and Unit Contradictions (Pillar 3 & Pillar 7)
* **Area Threshold Contradiction (Line 112):** Methods (line 104) defines `P < 0.1` as non-suitable, `0.1 ≤ P < 0.3` as low suitable, `0.3 ≤ P < 0.6` as medium suitable, and `P ≥ 0.6` as high suitable. However, Results (line 112) states: *"with a suitability index of 30 per cent as the threshold, and areas with a suitability index greater than 30 per cent were classified as suitable habitat... The total area of suitable habitats was 83,000 km², of which 13,100 km² were highly suitable habitats and 32,600 km² were moderately suitable habitats."* If $P > 0.30$ defines suitable habitat, the total suitable area must be $13,100 + 32,600 = 45,700\text{ km}^2$, not $83,000\text{ km}^2$ (which includes the $37,300\text{ km}^2$ low-suitability class $0.1 \le P < 0.3$).
* **100-Fold Unit Mistranslation (Line 161):** Results (line 161) reports that high-suitability area decreases from $13,100\text{ km}^2$ to *"0.27, 0.55, 0.42, and 0.5 million square kilometers"* (mistranslating $10^4\text{ km}^2$ as $10^6\text{ km}^2$) and reports low-suitability areas as *"606, 626, 659, and 63,200 square kilometers"* (dropping a factor of $100$ on the first three values).
* **Contradictory Overlap Percentages:** Discussion (line 180) reports `78.80%` spatial overlap with producing counties, while Conclusions (line 214) reports `82.3%`.

### 3.3. Omitted Equation, Hyperparameter Grid Arithmetic Error, and Machine-Translation Artifacts (Pillar 7)
* **Missing MaxEnt Equation:** Methods (lines 85–87) introduces the MaxEnt formula (*"with the following formula:"*), leaves the equation completely blank, and then defines the symbols `P(y|x)`, `f_i(x, y)`, `\lambda_i`, and `Z(x)` of the missing equation.
* **Hyperparameter Grid Multiplication Error:** Methods (line 94) states that `72 candidate models` were generated by combining *"12 RM settings (from 0 to 6, with a spacing of 0.5) with the five FC class settings"*. First, $0\text{ to }6$ in steps of $0.5$ is 13 values (or 12 positive values from $0.5\text{ to }6.0$, since $\text{RM}=0$ is invalid in MaxEnt), and $12 \times 5 = 60 \ne 72$ (72 requires 6 FC combinations, which the same sentence contradictorily alludes to as *"combining all six combinations of the 12 RM settings... with the five FC class settings"*).
* **Pervasive Machine-Translation Garble:** Jackknife test is repeatedly mistranslated as *"Knife cut tests"* (line 20) and *"folding knife test"* (line 145); `BCC-CSM2-MR` is written `"BBC_CSM"` (line 44); `ENMeval` is written `"ENMevel"` (line 28); and soil resolution is written `"30'"` (30 arc-minutes $\approx 55\text{ km}$) instead of `30"` (30 arc-seconds $\approx 1\text{ km}$) in line 44.

---

## 4. Quantitative Rubric Scoring

| Rubric Dimension | Score | Max | Forensic Justification |
| :--- | :---: | :---: | :--- |
| **1. Methodological & Statistical Rigor** | **0.6** | 3.5 | Pre-screening predictors on the full dataset before `ENMeval`; misinterpreting categorical/integer HWSD codes as `6508–11333 mm` of water; contradictory suitability threshold definitions ($P>0.3$ vs $P\ge 0.1$); single GCM (`BBC_CSM`). |
| **2. Claim-to-Evidence Alignment** | **0.5** | 2.5 | Claims to quantify the maintenance effect of `6508–11333 mm` soil moisture for the first time; contradicts its own spatial coupling statistics (`78.80%` vs `82.3%`) and centroid directions. |
| **3. Data Integrity & Biological Plausibility** | **0.6** | 2.0 | Physically impossible $6.5\text{--}11.3\text{ m}$ soil water content; false claim that Shaanxi Province's max altitude is $678.03\text{ m}$ (copied from Table 3); false statement that atmospheric pressure increases with altitude. |
| **4. Reproducibility & Data Integrity** | **0.5** | 2.0 | Omitted MaxEnt equation (line 86); 100-fold unit errors (`0.27–0.55 million km²` and `606, 626, 659, and 63,200 km²`); machine-translation errors ("Knife cut tests", "folding knife test"); no occurrence coordinates deposited. |
| **Total Composite Score** | **2.2** | **10.0** | **Fundamentally Invalid** (**Scientific Core Score: 1.7 / 8.0**) |
