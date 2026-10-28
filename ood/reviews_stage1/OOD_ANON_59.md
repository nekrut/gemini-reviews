# Review of OOD_ANON_59

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **2.5 / 10.0** (Fundamentally Invalid)  
* **Score Breakdown:** Rigor: 0.6/3.5 | Claims: 0.6/2.5 | Biology: 0.7/2.0 | Reproducibility: 0.6/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript uses the MaxEnt species distribution model (`ENMeval`-tuned parameters $\text{RM} = 1.5$, $\text{FC} = \text{LQHPT}$) to predict current (1970–2000) and future (2050s and 2090s under SSP1-2.6, SSP2-4.5, and SSP5-8.5 from the BCC-CSM model) suitable habitat distributions across China for the medicinal plant *Angelica dahurica* based on 234 occurrence records from GBIF and the Chinese Virtual Herbarium (CVH). Using bioclimatic, topographic, and HWSD soil variables at 2.5-arcminute ($\sim 5\text{ km}$) resolution, the authors report a training AUC of 0.879 and TSS of 0.62, identify annual precipitation (`Bio12`, 51.4%), elevation (23.3%), driest-quarter precipitation (`Bio17`, 6.3%), coldest-month minimum temperature (`Bio6`, 4.4%), and slope (4.2%) as the top five predictors (89.6% cumulative contribution), and project that suitable habitats will expand and shift northward by $\sim 250\text{ km}$ from Zhengzhou (Henan) to Shijiazhuang and Baoding (Hebei). Raw occurrence coordinates and modeling scripts are not deposited in an external repository.

Despite following a recognizable SDM workflow template, the manuscript contains pervasive, disqualifying mathematical, geographical, and internal data inconsistencies across almost every section and table. First, the environmental variable screening (Section 2.2) explicitly eliminates `Bio17` (Precipitation of Driest Quarter) and `Slope`—retaining only 6 climatic factors (`Bio1`, `Bio5`, `Bio6`, `Bio12`, `Bio14`, `Bio16`), 1 topographic factor (`Elevation`), and 11 soil factors (totaling 18 variables)—yet in the Results (Section 3.4, Table 4, Table 5), `Bio17` and `Slope` suddenly reappear as two of the top five predictors in the final model. Second, the area calculations in Table 3 and Section 3.3 state that the total land area of China modeled is $424,536 + 109,898 = 534,434\text{ km}^2$ (claiming $109,898\text{ km}^2$ is $20.6\%$ of China's total land area), which is off by an order of magnitude from China's actual land area ($\sim 9,600,000\text{ km}^2$). Third, the physical units and values of `Slope` in Section 3.4 ($0.3 \times 10^6$ to $0.5 \times 10^6$) and Table 5 ($245,018.6$) are physically impossible for topographic slope ($0^\circ\text{--}90^\circ$), indicating corrupted raster values or unprojected DEM differentiation errors. Because the predictor set, raster values, and area calculations are internally contradictory, the quantitative projections cannot be trusted without rebuilding the GIS and MaxEnt pipeline from scratch.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **After correlation ($|r| < 0.8$) and VIF ($< 10$) screening of 34 environmental factors, 18 variables were selected for MaxEnt modeling, and the top five factors driving *A. dahurica* distribution are `Bio12` (51.4%), `Elevation` (23.3%), `Bio17` (6.3%), `Bio6` (4.4%), and `Slope` (4.2%): [Methodologically Flawed].**  
  The manuscript contradicts itself regarding how many environmental variables were used and which ones were retained:
  1. The Abstract (Line 8) says "22 environmental factors"; Section 2.2 (Line 40) lists 19 bioclimatic + 14 soil + topographic factors, while Section 4.1 (Line 233) says "34 environmental factors."
  2. Section 2.2 (Line 72) explicitly lists the 18 variables that survived VIF/correlation screening: 6 climatic (`Annual Mean Temperature [Bio1]`, `Max Temperature of Warmest Month [Bio5]`, `Min Temperature of Coldest Month [Bio6]`, `Annual Precipitation [Bio12]`, `Precipitation of Driest Month [Bio14]`, `Precipitation of Wettest Quarter [Bio16]`), 1 topographic (`elevation`), and 11 soil factors. Notice that neither `Bio17` (Precipitation of Driest Quarter) nor `Slope` is among the 18 retained variables!
  3. Yet in Section 3.4 (Line 173), Table 4 (Lines 188–195), and Table 5 (Lines 218, 221), `Bio17` (6.3% contribution) and `Slope` (4.2% contribution) are reported as two of the top five predictors in the model.

* **The current total suitable area for *A. dahurica* in China is $109,898\text{ km}^2$, accounting for 20.6% of China's total land area, and will expand to $144,528\text{--}183,637\text{ km}^2$ (27.0%–34.4%) under future scenarios: [Methodologically Flawed].**  
  In Table 3, across every row, the sum of `Unsuitable area` + `Total suitable area` equals exactly $534,434\text{ km}^2$ (e.g., Current: $424,536 + 109,898 = 534,434\text{ km}^2$, where $109,898 / 534,434 = 20.56\%$). However, the study area is the entire territory of China (Figure 1, Figure 3), which has a land area of $\sim 9,600,000\text{ km}^2$, not $534,434\text{ km}^2$. The authors appear to have counted the number of 2.5-arcminute raster grid cells ($\sim 534,434$ pixels across China at middle latitudes, where each 2.5-arcminute pixel is $\sim 18\text{ km}^2$) and misreported raw pixel counts as $\text{km}^2$, while simultaneously claiming that $109,898\text{ km}^2$ represents 20.6% of China's land area. Furthermore, Section 3.3 (Line 130) states `"Comparing the predicted suitable areas of A. dahurica in the 1950s and 1970s"`, confusing the future 2050s and 2090s projections with the 1950s and 1970s.

* **Response curves show optimal *A. dahurica* presence at annual precipitation of 1,043 mm, elevation of 491 m, and slope of $0.3 \times 10^6$ (with mean slope of $245,018.6$ across occurrence sites): [Methodologically Flawed].**  
  In Section 3.4 (Line 197), the authors state that survival probability `"increased rapidly from 0 to 0.5*10^6, and reached a maximum at 0.3*10^6"` for slope, and Table 5 (Line 221) reports the mean `Slope` across distribution sites as `245,018.6`. Topographic slope is measured in degrees ($0^\circ\text{--}90^\circ$) or percent ($0\%\text{--}100\%$). A slope value of $245,018.6$ to $500,000$ is a classic GIS error caused by computing slope in ArcGIS on an unprojected geographic coordinate system (`GCS-WGS-1984`, where horizontal units are decimal degrees and vertical DEM units are meters, without applying a $Z$-factor of $\sim 10^{-5}$, or multiplying instead of dividing by the Z-factor). Additionally, Section 3.4 states `"the probability of the existence of A. dahurica is extremely small when the rainfall of the current year is < 0 mm"` and `"at a slope of < 0"`—neither rainfall nor slope can be negative ($< 0$).

* **Spatial thinning was not performed on the 234 GBIF/CVH occurrence points, and figure captions for Figures 7 and 8 are inverted: [Methodologically Flawed].**  
  Unlike standard MaxEnt workflows, Section 2.1 only deleted "duplicated and erroneous sample points" without spatial thinning to match the 2.5-arcminute ($\sim 5\text{ km}$) environmental grid, and the sample size fluctuates unexplainedly between $234$ points (Sections 2.1, 3.1, 4.1) and $235$ points (Section 3.4, Line 205: `"Annual rainfall at 235 A. dahurica distribution sites"`). Moreover, in Section 3.4, Figure 7 is cited as the Jackknife analysis (`"Based on the results of the Jackknife analysis (Figure 7)"`) but its caption reads `"Response curves for dominant environmental factors"`, while Figure 8 is cited as the response curves (`"draw the response curves of environmental variables, which are shown in Figure 8"`) but its caption reads `"Spatial changes in A. dahurica in China in ssp126..."`.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Re-Compute Topographic Slope in a Projected Coordinate System and Reconcile the Predictor Variable Set
* **WHY:** Computing slope on a `GCS-WGS-1984` DEM (decimal degrees horizontal vs. meters vertical) without a metric projection produced physically meaningless slope numbers ($245,018.6$ to $500,000$), and the manuscript contradicts itself on whether `Slope` and `Bio17` were excluded during VIF screening (Section 2.2) or retained as top predictors (Section 3.4, Tables 4–5).
* **WHAT:** Project the DEM to an equal-area metric projection (e.g., Asia North Albers Equal Area Conic) before deriving slope in degrees ($0^\circ\text{--}90^\circ$), and ensure the exact same set of screened variables is reported in Section 2.2 and Section 3.4.
* **HOW:** In ArcGIS, project the DEM raster to `Asia_North_Albers_Equal_Area_Conic` (meters) or specify `Z-factor = 0.00001` in `Spatial Analyst -> Surface -> Slope`. Re-run the Pearson correlation ($|r| < 0.8$) and VIF ($< 10$) screening on the corrected rasters extracted at spatially thinned occurrence points (1 point per 2.5-arcminute cell). Update Section 2.2, Table 1 (which currently lists only the 19 bioclimatic variables despite the text referring to soil and topographic variables), Table 4, and Table 5 so that the variable lists match 100%.

#### 2. Convert Raw Pixel Counts to Actual Square Kilometers ($\text{km}^2$) in Table 3 and Section 3.2–3.3
* **WHY:** Table 3 reports China's total modeled land area (`Unsuitable` + `Total suitable`) as $534,434\text{ km}^2$, which is the count of 2.5-arcminute grid cells rather than area in $\text{km}^2$ ($\sim 9.6 \times 10^6\text{ km}^2$).
* **WHAT:** Multiply cell counts in an equal-area projection by the true cell area in $\text{km}^2$ (or integrate geodesic cell areas by latitude).
* **HOW:** Reproject the classified MaxEnt suitability rasters to an Albers Equal-Area Conic projection (e.g., $4\text{ km} \times 4\text{ km} = 16\text{ km}^2$ or $5\text{ km} \times 5\text{ km} = 25\text{ km}^2$ cells) so that total pixels $\times$ cell area equals $\sim 9.6 \times 10^6\text{ km}^2$, and recompute all area columns in Table 3 and text values in Sections 3.2 and 3.3.

#### 3. Perform Spatial Thinning of Occurrence Records and Report Test AUC (Not Just Training AUC)
* **WHY:** Retaining unthinned herbarium/GBIF points inflates spatial autocorrelation, and Section 3.1 (Line 95) reports `"the AUC value of the simulated training under this parameter was 0.879"`, whereas model evaluation requires out-of-sample *test* AUC on the held-out 25% test set (or checkerboard cross-validation folds).
* **WHAT:** Spatially thin the 234 occurrence records to one record per 2.5-arcminute grid cell and report both training and test AUC ($\pm\text{SD}$) and TSS from cross-validation.
* **HOW:** Use `spThin` or `ENMTools` to thin the 234 points to a minimum distance of $5\text{ km}$, report the exact thinned sample size $N$, and report the mean test AUC and test omission rate from `ENMeval` checkerboard2 cross-validation.

#### 4. Fix Biographical, Botanical, and Citation Errors in the Introduction and Discussion
* **WHY:** The Introduction contains factual and citation errors that indicate machine-translation or citation-matching mistakes:
  * **Section 1 (Line 19):** States `"Currently, A. dahurica is used medicinally in four major medicinal varieties: A. dahurica Chuan, A. dahurica Hang, A. dahurica Yu, and A. dahurica Qi (Elith et al., 2006)"`—citing Jane Elith's 2006 ecological modeling paper for traditional Chinese medicinal cultivars of *Angelica dahurica*.
  * **Section 1 (Line 19):** States `"The main medicinal components in A. dahurica herb are coumarins, including epoprostenol, epoprostenol, and oxidized prostenol (Li, 2012)"`—"epoprostenol" is prostacyclin ($\text{PGI}_2$, a human eicosanoid vasodilator drug), a mistranslation of *imperatorin* / *isoimperatorin* / *oxypeucedanin* (欧前胡素 / 异欧前胡素 / 氧化前胡素).
* **WHAT & HOW:** Replace `(Elith et al., 2006)` in Line 19 with the appropriate Chinese Pharmacopoeia reference, and replace `"epoprostenol, epoprostenol, and oxidized prostenol"` with the correct furanocoumarin names: `"imperatorin, isoimperatorin, and oxypeucedanin"`.

#### 5. Technical and Editorial Cleanup
* **WHY:** Multiple typos, mismatched figure captions, and date errors appear throughout the manuscript.
* **WHAT & HOW:**
  * **Section 3.3 (Line 130):** Change `"Comparing the predicted suitable areas of A. dahurica in the 1950s and 1970s"` to `"in the 2050s and 2090s"`.
  * **Section 3.4 & Figures 7–8 (Lines 173–203):** Fix the mismatched figure numbering and captions: Figure 7 is cited in text as the Jackknife test, Figure 8 is cited in text as the univariate response curves, and the spatial change maps (currently captioned as Figure 8) are not cited properly.
  * **Section 3.4 (Line 197):** Remove impossible statements about `"rainfall of the current year is < 0 mm"` and `"slope of < 0"`, and correct `"3°"` for `Bio6` (`Min Temperature of Coldest Month`, which is $-7.44\text{ }^\circ\text{C}$ to $-2.18\text{ }^\circ\text{C}$ in Table 5).
  * **Section 4.1 (Line 235):** Correct `"based on the 5th climate model released by the IPCC"`—SSP126, SSP245, and SSP585 are CMIP6 (IPCC Sixth Assessment Report, AR6) scenarios, not IPCC AR5.
