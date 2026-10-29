# Forensic Peer Review: FEXP_ANON_117

**Overall Score:** **3.6 / 10.0** (Flawed / Overstated) | **Scientific Core Score:** **2.7 / 8.0**  
* **Score Breakdown:** Rigor: 0.9/3.5 | Claims: 0.9/2.5 | Biology: 0.9/2.0 | Reproducibility: 0.9/2.0

---

## 1. Blinded Metadata Perception

* **Manuscript ID:** `FEXP_ANON_117`
* **Perceived Domain & Topic:** Ecological Niche Modeling / Paleobiogeography / Forest Conservation; MaxEnt species distribution modeling of *Corylus* (hazel) taxa across China from the Last Interglacial (LIG) to the 2070s.
* **Perceived Empirical Scope:** 1,075 reported (1,115 tabulated in Table 1) herbarium occurrence records across 18 *Corylus* species/varieties/forms from the Chinese Virtual Herbarium (CVH), thinned to 10 km × 10 km grid cells (only 7 taxa with $N \ge 72$ actually modeled in Results); 44 initial predictors screened to "24" (34 listed in Table 2) at 30 arc-second resolution; paleoclimatic (LIG, LGM, MH) and future CMIP6 (2050s, 2070s; BCC-CSM2-MR, CNRM-CM6-1, MIROC6 under SSP126, SSP245, SSP370) projections using MaxEnt v3.4.4 (`kuenm` package) and ArcGIS 10.7.

---

## 2. Executive Summary & Editorial Verdict

This study models the historical (Last Interglacial, Last Glacial Maximum, Mid Holocene), current (1970–2000), and future (2050s, 2070s under SSP126, SSP245, SSP370) habitat suitability of *Corylus* taxa in China using MaxEnt v3.4.4 tuned via `kuenm`. The authors report that `RM = 0.1` and `FC = LQPH` is the optimal parameter configuration ($\Delta\text{AICc} = 0$, $\text{AUC} > 0.980$), identify minimum temperature of the coldest month (`Bio6`, 19.5%) and Human Footprint (`HF`, 14.7%) as the top predictors, and conclude that suitable habitats for all seven focal *Corylus* taxa expanded from the Mid Holocene to the present and will continue expanding northward under future warming.

**Editorial Verdict: Reject / Fundamentally Flawed Methodology and Internal Contradictions (3.6 / 10.0).** The manuscript exhibits pervasive contradictions between its Methods, Tables, and Results, alongside severe ecological modeling errors:
1. **Direct contradiction between the occurrence filtering rule, Table 1, and modeled taxa:** Section "Distribution Data" (line 28) states that *"species with fewer than 30 recorded sites were excluded from the analysis... Ultimately, 1075 occurrence records from 18 Corylus species were retained for modeling (Table 1)."* Yet Table 1 lists 18 taxa (including varieties and forms, contradicting the Introduction's statement that 8 *Corylus* species occur in China) whose records sum to **1,115** (not 1,075), and **11 of those 18 taxa have fewer than 30 records** (ranging from 1 to 10 records, including three taxa with $N = 1$). In the Results, only 7 taxa ($N = 72\text{–}344$, summing to 1,072 records) are analyzed.
2. **Anachronistic projection of contemporary Human Footprint (14.7% model weight) into the Last Interglacial (~120 ka) and Last Glacial Maximum (~21 ka):** The model incorporates contemporary 21st-century Human Footprint (`HF`, the second largest contributor at 14.7%) and static soil/land-cover variables, yet projects habitat suitability backward to the Last Interglacial, Last Glacial Maximum, and Mid Holocene (lines 140–142) and forward to the 2070s without explaining how modern anthropogenic infrastructure was handled in paleoclimatic epochs predating human civilization.
3. **Misinterpretation of extreme under-regularization (`RM = 0.1, FC = LQPH`) as "reduced complexity":** Setting the regularization multiplier to the minimum grid value (`RM = 0.1`, tenfold weaker penalty than the MaxEnt default of `1.0`) while combining four complex feature classes (`LQPH`) produces severe overfitting rather than "reduced complexity," explaining the artificially inflated $\text{AUC} > 0.980$ values and erratic paleoclimatic/future projections.

### Assessment of Specific Claims

* **Claim 1 (Parameter tuning via `kuenm` yielded `RM = 0.1, FC = LQPH`, reducing model complexity and overfitting while achieving $\text{AUC} > 0.980$ for all species): `[Methodologically Flawed]`.**  
  A regularization multiplier of $0.1$ with `LQPH` features is nearly unregularized and maximally complex; claiming that `RM = 0.1, FC = LQPH` reduces overfitting and complexity reverses the mathematical meaning of $L_1$ regularization in MaxEnt. Furthermore, reporting a single `RM = 0.1, FC = LQPH` and a single variable contribution ranking (`Bio6 = 19.5%`, `HF = 14.7%`) across 7–18 distinct species with sample sizes ranging from 1 to 344 indicates either undocumented species pooling or failure to report species-specific tuning outputs.
* **Claim 2 (Minimum temperature of the coldest month [`Bio6`, 19.5%] and Human Footprint [`HF`, 14.7%] are the primary determinants of *Corylus* distribution across China): `[Fragile]`.**  
  Herbarium collection records in CVH are heavily biased toward road-accessible, human-populated areas; including `HF` (14.7% contribution) as an environmental predictor without spatial bias correction confounds herbarium collection effort with the biological niche of *Corylus*. Moreover, `HF` is not even listed in Table 2 (which purports to list the retained predictor variables).
* **Claim 3 (Suitable habitats of all 7 *Corylus* taxa expanded substantially from the Last Glacial Maximum and Mid Holocene to the present and will expand by up to 62.83% in the 2050s–2070s): `[Methodologically Flawed]`.**  
  Projecting a model heavily weighted by contemporary Human Footprint (14.7%) and static soil/land-cover variables into the LIG, LGM, MH, and 2050s–2070s is invalid. In addition, the Methods state that three GCMs (`BCC-CSM2-MR`, `CNRM-CM6-1`, `MIROC6`) were downloaded, but the Results never state whether projections were averaged across the three GCMs or derived from a single model.
* **Claim 4 (Least-cost path resistance modeling identifies historical and future migration corridors for *Corylus* species across Chinese provinces): `[Methodologically Flawed]`.**  
  Although the Methods (lines 115–117) describe assigning landscape resistance values and running least-cost path analysis in ArcGIS, no resistance table, cost parametrization, or least-cost corridor map is presented; Figure 4 merely plots vectors connecting temporal range centroids.

---

## 3. Forensic Defect Inventory

### Defect 1: Contradictions Between Occurrence Filtering Criteria, Table 1 Arithmetic, and Modeled Taxa [ Pillar 2, Pillar 3, Pillar 7 — Critical ]
* **Location:** Introduction (line 14), Section "Distribution Data" (line 28), Table 1 (lines 31–51), and Results (lines 140–180).
* **Forensic Evidence:**
  1. **Violation of the $N \ge 30$ filter:** Line 28 states: *"Due to the sensitivity requirements of the MaxEnt model, species with fewer than 30 recorded sites were excluded from the analysis (Gebrewahid et al. 2020)... Ultimately, 1075 occurrence records from 18 Corylus species were retained for modeling (Table 1 and Table S1)."* Yet in Table 1, taxa #8 through #18 have $10, 7, 6, 5, 5, 3, 2, 2, 1, 1$, and $1$ records, respectively (all $< 30$).
  2. **Arithmetic mismatch in Table 1:** Summing the 18 rows of Table 1 yields $344 + 183 + 172 + 116 + 97 + 88 + 72 + 10 + 7 + 6 + 5 + 5 + 3 + 2 + 2 + 1 + 1 + 1 = 1,115$ records, contradicting the $1,075$ total reported in line 28 (meanwhile, the top 7 taxa with $\ge 30$ records sum to $1,072$).
  3. **Taxonomic inflation:** Line 14 states that eight *Corylus* species are found in China, whereas line 28 and Table 1 treat 18 intraspecific varieties (`var.`) and forms (`f.`) as "18 *Corylus* species."
* **Fix:** Remove the 11 taxa with $< 30$ records from Table 1 (or move them to an excluded-records note), reconcile the exact record count ($1,072$ across the 7 modeled taxa vs. $1,075$ vs. $1,115$), and clarify taxonomic rank (species vs. varieties).

### Defect 2: Inconsistent Predictor Variable Screening (Table 2) and Anachronistic Use of Human Footprint in Paleoclimatic Projections [ Pillar 2, Pillar 3, Pillar 6 — Critical ]
* **Location:** Section "Predictor Variables" (lines 55–59), Table 2 (lines 62–99), Section "Key Predictor Variables" (line 134, Figure 1), Section "Potential Suitable Habitats of Corylus Species in Paleoclimatic" (lines 140–142), and Discussion (line 185).
* **Forensic Evidence:**
  1. **Predictor count and Table 2 omissions:** Line 55 states 44 initial variables were compiled, and line 59 states *"Finally, 24 predictor variables were left for subsequent modeling (Table 2)."* However, Table 2 lists **34 variables** (with 14 marked by an unexplained asterisk `*`) and completely omits `Human footprint (HF)`, `NDVI`, `Land cover`, and `Population (POP)`. Yet Figure 1, line 134, and line 185 report that `Human footprint (HF)` is the second most important predictor in the final model (14.7% contribution)!
  2. **Dataset misidentification:** Line 55 states *"Additionally, we obtained 1-km resolution NDVI data from the MOD17A3H dataset"*—`MOD17A3H` is the MODIS Net Primary Production (NPP) product, not NDVI.
  3. **Paleoclimatic projection with static modern predictors:** WorldClim paleoclimate layers (LIG, LGM, MH) only provide the 19 bioclimatic variables (`Bio1–Bio19`). They do not provide LIG/LGM wind speed, solar radiation, vapor pressure, soil pH, or Human Footprint. Projecting a model in which contemporary Human Footprint contributes 14.7% (plus static soil and topography) into the Last Interglacial (~120,000 years ago) and Last Glacial Maximum (~21,000 years ago) is methodologically and biologically invalid.
* **Fix:** Correct Table 2 so that it lists the exact predictors retained in the final models and defines the `*` symbol. For paleoclimatic (LIG, LGM, MH) and future projections, refit models restricted to bioclimatic and topographic variables available across all epochs (excluding contemporary Human Footprint, Population, Land Cover, and MODIS products).

### Defect 3: Overfitting via Minimal Regularization (`RM = 0.1, FC = LQPH`) and Undocumented Species Pooling vs. Per-Species Modeling [ Pillar 3, Pillar 4 — Major ]
* **Location:** Section "Model Simulation and Evaluation" (line 104), Section "Model Accuracy Evaluation" (line 129), and Section "Key Predictor Variables" (line 134).
* **Forensic Evidence:**
  1. **Candidate model arithmetic error:** Line 104 states *"We then evaluated 1240 candidate models, encompassing combinations of 40 regularization multiplier settings (ranging from 0.1 to 4 at intervals of 0.1) and 29 feature class combinations."* However, $40 \times 29 = 1,160 \neq 1,240$ ($40 \times 31 = 1,240$).
  2. **Misinterpreting `RM = 0.1`:** Line 129 states that under `RM = 0.1, FC = LQPH`, *"the overfitting degree and complexity of the optimized model have been reduced."* In MaxEnt, decreasing the regularization multiplier from $1.0$ to $0.1$ *reduces* the penalty on feature weights by a factor of 10, *increasing* model complexity and overfitting.
  3. **Single parameter set and single variable importance reported for multiple species:** Although 7 distinct taxa are mapped in Figures 2–4, the manuscript reports only a single optimal parameter setting (`RM = 0.1, FC = LQPH`, line 129) and a single set of predictor contributions (`Bio6 = 19.5%`, `HF = 14.7%`, Figure 1 and line 185), without clarifying whether `kuenm` and Figure 1 were run on a pooled genus-level dataset or whether per-species values were omitted.
* **Fix:** Report species-specific `kuenm` optimal parameters ($\text{RM}$, $\text{FC}$, $\Delta\text{AICc}$, omission rate, pROC) and species-specific predictor contributions for each of the 7 modeled *Corylus* taxa in a summary table, and constrain $\text{RM} \ge 0.5$ to prevent severe overfitting.

### Defect 4: Unsubstantiated "Habitat Resistance" and "Least-Cost Path" Claims and Repeated Editorial Artifacts [ Pillar 5, Pillar 7 — Moderate ]
* **Location:** Section "Data Analysis" (lines 115–117) and Section "Result" (lines 170, 180).
* **Forensic Evidence:**
  1. Lines 115–117 claim that landscape resistance surfaces and least-cost path analyses (Adriaensen et al. 2003) were computed in ArcGIS to identify dispersal corridors. No resistance values, cost surfaces, or least-cost paths appear anywhere in the Results; Figure 4 only displays centroid shift trajectories between time periods.
  2. Lines 170 and 180 repeat the exact same boilerplate sentence twice at the end of the Results section: *"The following sections will delve into the environmental factors driving these shifts/distributions and their implications for biodiversity and ecosystem management."*

---

## 4. Quantitative Rubric Scoring

| Rubric Dimension | Score | Max | Diagnostic Justification |
| :--- | :---: | :---: | :--- |
| **1. Methodological & Statistical Rigor** | **0.9** | **3.5** | Contradicts its own $N \ge 30$ filter in Table 1; projects contemporary Human Footprint (14.7% contribution) into the Last Interglacial and Last Glacial Maximum; misinterprets `RM = 0.1, FC = LQPH` as complexity reduction; reports a single parameter/contribution set for 7–18 taxa. |
| **2. Claim-to-Evidence Alignment** | **0.9** | **2.5** | Claims of paleoclimatic/future habitat expansion and least-cost dispersal corridors are unsupported by valid temporally consistent models or resistance surface outputs. |
| **3. Data Integrity & Biological Plausibility** | **0.9** | **2.0** | Confounds herbarium sampling bias (proximity to human infrastructure) with biological habitat preference via unadjusted Human Footprint; misidentifies `MOD17A3H` (NPP) as NDVI; conflates intraspecific varieties/forms with species counts. |
| **4. Reproducibility & Data Integrity** | **0.9** | **2.0** | Table 1 sum ($1,115$) contradicts text ($1,075$); Table 2 lists 34 variables instead of 24, omits top predictor `HF`, and leaves `*` undefined; candidate model count ($40 \times 29 = 1,160$) contradicts text ($1,240$). |
| **Total Composite Score** | **3.6** | **10.0** | **Flawed / Overstated** (Scientific Core Score: **2.7 / 8.0**) |
