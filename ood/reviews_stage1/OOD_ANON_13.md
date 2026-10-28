# Review of OOD_ANON_13

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **3.2 / 10.0** (Flawed / Overstated)  
* **Score Breakdown:** Rigor: 0.9/3.5 | Claims: 0.8/2.5 | Biology: 0.9/2.0 | Reproducibility: 0.6/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This ecological niche modeling study uses MaxEnt (optimized via the R package `kuenm`) to predict current and future (2030s, 2050s, 2070s, 2090s under CMIP6 BCC-CSM2-MR SSP1-2.6 and SSP5-8.5 scenarios) suitable habitat distributions across China for the medicinal Lamiaceae species *Isodon amethystoides*. Starting from 207 herbarium occurrence records (thinned to 194 points on a $5\text{ km} \times 5\text{ km}$ grid) and 90 initial climate, topographic, and soil variables at 2.5 arc-minute resolution, the authors select 11 variables via correlation and contribution filtering, tune feature classes (`FC = TH`) and regularization (`RM = 3.5`), and report a test $\text{AUC} = 0.902$. They estimate a current suitable habitat area of $2.08 \times 10^6\text{ km}^2$ (21.66% of China's land area), identify September precipitation (`prec_09`, 46.8%), April precipitation (`prec_04`, 22.8%), and temperature seasonality (`bio_4`, 13.3%) as the primary drivers, and project overall habitat expansion under future climate scenarios with the geometric centroid remaining in Chongqing. Occurrence coordinates and raster outputs are withheld despite coming from public databases.

While applying `kuenm` to tune MaxEnt regularization and feature complexity is a reasonable methodological starting point, the manuscript is undermined by severe internal numerical and geographical contradictions, mathematical errors in area and coordinate calculations, and biological inconsistencies between the species' known ecology and the authors' narrative claims. Specifically, the authors misstate the direction of the `kuenm` Mean AUC Ratio change, report area values in Section 3.3 that are off by a factor of 10 from Table 3, compute geometric centroid migration directions in Section 3.6 that point in the opposite cardinal direction of the reported coordinates, and contradict their own Introduction and maps in the Discussion by claiming that the species is mainly produced in northern and northeastern China and southeastern Tibet.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **`kuenm` optimization (`FC = TH`, `RM = 3.5`) yields a significantly higher Mean AUC Ratio than default parameters (`FC = LQPH`, `RM = 1`): [Methodologically Flawed].**  
  In Section 3.1 (line 94), the authors write: *"When using the default parameters in Maxent (FC = LQPH, RM = 1), the Mean AUC Ratio was 1.660. Parameter optimization was performed using the Kuenm package, selecting parameters FC = TH and RM = 3.5. Under these settings, the Mean AUC Ratio was 1.5642, significantly higher than the result obtained with default parameters (FC = LQPH, RM = 1, Mean AUC Ratio = 1.660)."* Mathematically, $1.5642 < 1.660$. Claiming that $1.5642$ is "significantly higher" than $1.660$ is a direct numerical contradiction. Furthermore, the variable screening protocol (Section 2.2) uses all 194 occurrence records and all 90 variables in an initial MaxEnt fit prior to splitting training and test sets, introducing feature-selection leakage into the 25% random test evaluation.

* **Current suitable habitat area and class breakdown across China ($2.08 \times 10^6\text{ km}^2$ total): [Fragile].**  
  In Table 3, the current habitat areas (in units of $\times 10^4\text{ km}^2$) are reported as Low $= 69.96$ ($6.996 \times 10^5\text{ km}^2$), Medium $= 132.93$ ($1.3293 \times 10^6\text{ km}^2$), and High $= 5.45$ ($5.45 \times 10^4\text{ km}^2$), summing to $208.35 \times 10^4\text{ km}^2$ ($2.0835 \times 10^6\text{ km}^2$). However, in the main text of Section 3.3 (line 144), the authors report the moderate-suitability area as $1.329 \times 10^5\text{ km}^2$ (off by a factor of 10 from $1.3293 \times 10^6\text{ km}^2$) and the low-suitability area as $6.99 \times 10^4\text{ km}^2$ (off by a factor of 10 from $6.996 \times 10^5\text{ km}^2$), while simultaneously claiming these represent 13.8% and 7.27% of China's $9.6 \times 10^6\text{ km}^2$ land area. Similarly, in Section 3.4 (line 184), they state that low-suitability area under SSP1-2.6 decreases to "$3.58 \times 10^4\text{ km}^2$ by the 2090s," whereas Table 3 shows it is $66.38 \times 10^4\text{ km}^2$ (and $69.96 - 66.38 = 3.58 \times 10^4\text{ km}^2$ is the *change*, not the final area).

* **Future climate scenarios drive a consistent northwestward migration of the suitable habitat centroid within Chongqing: [Methodologically Flawed].**  
  The coordinate trajectories reported in Section 3.6 (line 202) directly contradict the stated cardinal directions and distances:
  1. From Current ($107.10^\circ\text{E}, 29.16^\circ\text{N}$) to 2021–2040 SSP1-2.6 ($107.22^\circ\text{E}, 29.69^\circ\text{N}$), longitude increases eastward ($+0.12^\circ\text{E}$) and latitude increases northward ($+0.53^\circ\text{N}$), which is **northeast**, not "northwest."
  2. From 2021–2040 ($107.22^\circ\text{E}, 29.69^\circ\text{N}$) to 2041–2060 SSP1-2.6 ($106.48^\circ\text{E}, 29.41^\circ\text{N}$), longitude moves west ($-0.74^\circ$) and latitude moves **south** ($-0.28^\circ$), which is **southwest**, not "northwest."
  3. From 2061–2080 ($107.10^\circ\text{E}, 29.17^\circ\text{N}$) to 2081–2100 SSP5-8.5: for 2061–2080 ($106.60^\circ\text{E}, 29.35^\circ\text{N}$) to 2081–2100 ($106.54^\circ\text{E}, 29.41^\circ\text{N}$), the net shift from current ($107.10^\circ\text{E}, 29.16^\circ\text{N}$) is only $\sim 60\text{ km}$ within the same municipality (Chongqing), which results from relying on a single GCM (`BCC-CSM2-MR`) without ensemble uncertainty quantification.

* **Ecological and biogeographical interpretation of *Isodon amethystoides* distribution and edaphic requirements: [Methodologically Flawed].**  
  Multiple biological and geographical statements contradict each other across sections:
  1. In the Introduction (line 17), *I. amethystoides* is described as a subtropical montane species distributed between $23^\circ\text{N}$ and $34^\circ\text{N}$ (Central, East, and South China) with a *"strong edaphic preference for acidic soils (red/yellow podzolic soils, pH 4.5–6.0)"*. Yet in the Discussion (line 215), the authors state: *"Currently, Isodon amethystoides in China is mainly produced in areas from north of the Qinling-Huaihe Line to North China and southern Northeast China, as well as southeastern Tibet."* North China, Northeast China, and southeastern Tibet lie outside the $23^\circ\text{N}\text{--}34^\circ\text{N}$ subtropical distribution shown in Figure 1 and Figure 5.
  2. Despite emphasizing soil pH (4.5–6.0) in the Introduction and Discussion (line 215: *"improving soil acidity"*), `ph` was discarded during variable screening, while Calcium Carbonate (`eq`, a marker of alkaline/calcareous soils) and Base Saturation (`bsat`) were retained, and the variable list in Section 2.2 (`cec` vs. `cec-clay` in Section 3.2 vs. `clay` ["Viscosity Content"] in Table 2) changes names across sections.
  3. In Section 3.2 and Section 5 (line 222), WorldClim `bio_4` (Temperature Seasonality = standard deviation of monthly temperatures $\times 100$) is reported as *"321.61–799.85°C"*, omitting the $\times 100$ scaling factor (a standard deviation of $321\text{--}800^\circ\text{C}$ is physically impossible on Earth; the actual SD is $3.22\text{--}8.00^\circ\text{C}$).

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Audit and Correct All Area, Coordinate, and `kuenm` Numerical Contradictions
* **WHY:** Reporting that $1.5642 > 1.660$, misstating orders of magnitude ($\times 10^4$ vs. $\times 10^5$ vs. $\times 10^6\text{ km}^2$) between Section 3.3/3.4 and Table 3, and mislabeling northeast/southwest coordinate shifts as "northwest" invalidate the quantitative results.
* **WHAT:** Reconcile every numerical value in Sections 3.1–3.6 and 5 against the raw `kuenm` output and ArcGIS zonal statistics tables.
* **HOW:**
  1. In Section 3.1, verify whether `1.660` and `1.5642` were transposed or whether model selection in `kuenm` was based on omission rate $< 5\%$ and $\Delta\text{AICc} = 0$ rather than maximizing the partial ROC AUC ratio.
  2. In Section 3.3 (line 144), correct the moderate-suitability area from $1.329 \times 10^5\text{ km}^2$ to $1.329 \times 10^6\text{ km}^2$ ($132.93 \times 10^4\text{ km}^2$) and the low-suitability area from $6.99 \times 10^4\text{ km}^2$ to $6.996 \times 10^5\text{ km}^2$ ($69.96 \times 10^4\text{ km}^2$).
  3. In Section 3.4 (line 184), state that low-suitability area *decreases by* $3.58 \times 10^4\text{ km}^2$ (from $69.96 \times 10^4$ to $66.38 \times 10^4\text{ km}^2$), rather than "reaching $3.58 \times 10^4\text{ km}^2$."
  4. In Section 3.6 (line 202), recompute the exact bearing (azimuth in degrees) between consecutive centroid coordinates and correct "northwest" to "northeast" ($107.10^\circ\text{E}, 29.16^\circ\text{N} \to 107.22^\circ\text{E}, 29.69^\circ\text{N}$) and "southwest" ($107.22^\circ\text{E}, 29.69^\circ\text{N} \to 106.48^\circ\text{E}, 29.41^\circ\text{N}$), and delete the duplicated sentence in line 202.

#### 2. Incorporate Multi-GCM Ensemble Uncertainty and Spatial Cross-Validation
* **WHY:** Projecting future species distributions using a single global climate model (`BCC-CSM2-MR`) and evaluating MaxEnt via random 75/25 bootstrap splits (rather than spatially independent block cross-validation) underestimates climate projection uncertainty and inflates test AUC due to residual spatial autocorrelation.
* **WHAT:** Average future habitat suitability projections across an ensemble of at least 3–5 CMIP6 GCMs (e.g., `BCC-CSM2-MR`, `MIROC6`, `MPI-ESM1-2-HR`, `CNRM-CM6-1`) and evaluate model transferability using spatial block cross-validation (`ENMeval`).
* **HOW:** Download the corresponding 2.5 arc-minute CMIP6 bioclimatic layers from WorldClim v2.1, project the calibrated MaxEnt model onto each GCM, and report the ensemble mean $\pm$ SD of suitable habitat area in Table 3.

#### 3. Resolve the Biogeographical Contradiction in the Discussion and Standardize Variable Names
* **WHY:** The claim in Section 4 (line 215) that *I. amethystoides* is mainly produced "north of the Qinling-Huaihe Line to North China and southern Northeast China, as well as southeastern Tibet" contradicts the species' actual subtropical distribution ($23^\circ\text{N}\text{--}34^\circ\text{N}$) described in the Introduction and shown in Figure 1. Additionally, variable names are inconsistent across Section 2.2, Section 3.2, and Table 2.
* **WHAT:** Remove or correct the erroneous northern China distribution statement in Section 4, correct the physical units of `bio_4`, and standardize the 11 retained variable codes.
* **HOW:**
  1. Rewrite line 215 to accurately reflect the subtropical distribution south of the Qinling-Huaihe Line (Anhui, Henan, Hubei, Hunan, Jiangxi, Fujian, Guangdong, Guangxi, Guizhou, Yunnan).
  2. Correct the units of `bio_4` (Temperature Seasonality) in Table 2 and line 222 from `321.61–799.85°C` to `3.22–8.00°C` (or specify $\text{SD} \times 100$).
  3. Reconcile the discrepancy between `cec` (line 74), `cec-clay` (line 105), and `clay` ("Viscosity Content", Table 2), and fix the typo `slit` $\to$ `silt` in Table 1.

#### 4. Provide Public Access to the Filtered Occurrence Coordinates and MaxEnt Outputs
* **WHY:** The Data Availability Statement (line 232) states that *"The datasets presented in this article are not readily available because the data is sourced from an open database, and the predicted results of the suitable areas generated by the model do not contain any sensitive information."* If the data come from open databases and contain no sensitive information, there is no justification for withholding them.
* **WHAT & HOW:** Include the CSV file of the 194 spatially thinned occurrence coordinates (latitude and longitude) and the ASCII/GeoTIFF suitability rasters as Supplementary Material or deposit them on Zenodo/Figshare.
