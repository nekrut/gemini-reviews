# Forensic Peer Review: FEXP_ANON_118

**Overall Score:** **4.4 / 10.0** (Flawed / Overstated) | **Scientific Core Score:** **3.4 / 8.0**  
* **Score Breakdown:** Rigor: 1.2/3.5 | Claims: 1.0/2.5 | Biology: 1.2/2.0 | Reproducibility: 1.0/2.0

---

## 1. Blinded Metadata Perception

* **Manuscript ID:** `FEXP_ANON_118`
* **Perceived Domain & Topic:** Arid-Zone Plant Ecology / Ecological Niche Modeling; MaxEnt distribution and co-occurrence modeling of the desert shrub/climber *Ochradenus baccatus* and its nurse tree *Vachellia tortilis* across Saudi Arabia under current and future climate scenarios.
* **Perceived Empirical Scope:** $N = 130$ (*O. baccatus*) and $N = 138$ (*V. tortilis*) spatially filtered occurrence records compiled from 2022–2024 field surveys, GBIF, and literature; 6 environmental predictors (`bio4`, `bio6`, `bio12`, `bio14`, soil `nitrogen`, and soil organic carbon `soc`) at 30 arc-second (~1 km) resolution; future projections for 2041–2060 and 2061–2080 using CMIP6 `BCC-CSM2-MR` under SSP2-4.5 and SSP5-8.5.

---

## 2. Executive Summary & Editorial Verdict

This study models the current and future habitat suitability and spatial overlap of two co-occurring arid-zone plant species in Saudi Arabia—*Ochradenus baccatus* ($N = 130$) and *Vachellia tortilis* ($N = 138$)—using MaxEnt v3.4.4 with four WorldClim bioclimatic variables (`bio4`, `bio6`, `bio12`, `bio14`) and two SoilGrids edaphic layers (`nitrogen`, `soc`). The authors report cross-validated $\text{AUC} = 0.946$ (*O. baccatus*) and $0.909$ (*V. tortilis*), estimate a current co-occurrence zone of ~18,500 $\text{km}^2$ concentrated along the western Hijaz and Asir mountains, and project an ~40% decline in spatial overlap under SSP5-8.5.

**Editorial Verdict: Major Revision / Self-Contradictory Narrative and Incomplete Reporting (4.4 / 10.0).** Investigating how climate change may decouple facilitative nurse-plant interactions (*V. tortilis* facilitating *O. baccatus*) in hyper-arid ecosystems is an ecologically interesting question. However, the manuscript is undermined by direct contradictions between the Results and Discussion, omitted methodological outputs, and unsubstantiated variable interpretations:
1. **180-degree contradiction between the Results and Discussion on the direction of future range shifts:** In the Results (lines 109 and 119; Figure 7a–d), the authors report that under SSP2-4.5 and SSP5-8.5, *O. baccatus* **contracts from the western highlands (Hijaz and Asir)** and **shifts into the east-central, northern, and northeastern regions**, with *"an apparent loss of overlapping habitat along the Hijaz and Asir ranges."* Yet in the Discussion (line 130) and Conclusion (line 144), the authors state the exact opposite: that *O. baccatus* *"is expected to experience range contractions in the central and northeastern deserts under high-emission scenarios, while maintaining core populations in climatically buffered highlands [Hijaz and Asir]"*!
2. **Fabricated/erroneous Discussion of `Isothermality` (excluded from the model) and reversed edaphic dependencies:** Discussion line 126 claims that *"Isothermality... also had a role in shaping distribution... Its contribution to habitat suitability appeared to influence the broader ecological amplitude of V. tortilis,"* even though Isothermality (`bio3`) was excluded prior to modeling and is not among the 6 modeled variables (Table 1). Furthermore, Discussion line 128 reverses the species' relative reliance on soil organic carbon (`soc`) versus `nitrogen` compared to Table 1 and Results lines 73 & 83.
3. **Complete omission of `ENMeval`, `pROC`, and `SDMTune` outputs and quantitative area tables:** Although the Methods state that models were tuned via `ENMeval` ($\Delta\text{AICc}$, omission rates) and validated via `pROC` (AUC ratios) and `SDMTune` (lines 47–52), none of these statistics or chosen hyperparameters are reported in the Results, nor is there any quantitative table of predicted areas ($\text{km}^2$) across scenarios and suitability classes.

### Assessment of Specific Claims

* **Claim 1 (Current distributions of *O. baccatus* and *V. tortilis* are primarily driven by temperature seasonality [`bio4`: 54.4% and 42.7%], coldest-month minimum temperature [`bio6`: 22.8% and 30.5%], and annual precipitation [`bio12`: 12.6% and 20.5%]): `[Moderately Supported]`.**  
  Table 1 and Figure 5 (jackknife tests) support the dominance of `bio4`, `bio6`, and `bio12`, though the optimal `ENMeval` feature classes, regularization multipliers, kernel density bias surface bandwidth, and spatial filtering distance are omitted from the text.
* **Claim 2 (*O. baccatus* has a stronger dependence on soil organic carbon [`soc`], whereas *V. tortilis* has a lower dependence on `soc` and stronger dependence on `nitrogen`, and `Isothermality` broadens the amplitude of *V. tortilis*): `[Methodologically Flawed]`.**  
  Directly contradicted by Table 1 and Results lines 73 & 83, where *V. tortilis* has higher `soc` contribution ($3.9\%$ vs. $1.9\%$) and permutation importance ($13.4\%$ vs. $2.0\%$) than *O. baccatus*, while *O. baccatus* has higher `nitrogen` contribution ($4.2\%$ vs. $1.5\%$). Moreover, `Isothermality` (`bio3`) was never included in the models.
* **Claim 3 (Under SSP5-8.5, suitable habitat for *O. baccatus* and species co-occurrence shift out of the western Hijaz/Asir mountains into northern/northeastern Saudi Arabia [Results], while simultaneously the western Hijaz/Asir mountains serve as the primary climatically stable future refugia where core populations are maintained [Discussion/Conclusion]): `[Methodologically Flawed]`.**  
  The Results text (lines 109, 119) and Figure 7c–d directly contradict the Discussion (lines 130, 134) and Conclusion (line 144). If the model projects loss of suitability and loss of co-occurrence along the Hijaz and Asir escarpments under SSP5-8.5 (Figure 7c–d), those ranges cannot simultaneously be claimed as the model-identified future refugia for *O. baccatus*.
* **Claim 4 (Co-occurrence area between *O. baccatus* and *V. tortilis* is currently ~18,500 $\text{km}^2$ and declines by nearly 40% under SSP5-8.5): `[Fragile]`.**  
  The probability threshold used to define binary presence/co-occurrence ($>0.2$, $>0.4$, or $>0.6$) is never specified, no scenario-by-time-period area table is provided, and projections rely on a single GCM (`BCC-CSM2-MR`).

---

## 3. Forensic Defect Inventory

### Defect 1: Direct Self-Contradictions Between Results/Figures and Discussion/Abstract/Conclusion [ Pillar 1, Pillar 3, Pillar 5 — Critical ]
* **Location:** Abstract (line 5), Results (lines 73, 83, 109, 119), Table 1 (lines 78–82), Discussion (lines 126, 128, 130, 134), and Conclusion (line 144).
* **Forensic Evidence:**
  1. **Contradictory geographic direction of future range shifts and refugia:**
     - **Results (line 109):** *"Under SSP2-4.5, the species' [O. baccatus] suitable habitat contracts from the western highlands and Najd Plateau and shifts predominantly toward the east-central regions... Under the more extreme SSP5-8.5 scenario (Fig. 7 c and d), there is a more pronounced redistribution, with core suitable zones emerging in northern and northeastern regions... The traditional western range (Hijaz and Asir) becomes less suitable..."*
     - **Results (line 119):** *"Notably, both species show an apparent loss of overlapping habitat along the Hijaz and Asir ranges, which currently represent their major co-existence zones."*
     - **Discussion (line 130):** *"O. baccatus is expected to experience range contractions in the central and northeastern deserts under high-emission scenarios, while maintaining core populations in climatically buffered highlands [81, 82]."*
     - **End of Results (line 119) / Discussion (line 134) / Conclusion (line 144):** Claims that the western and southwestern highlands (Al Bahah, Asir, Hijaz) are *"climatically stable areas... likely to function as future refugia."*
     The Discussion reverses the spatial pattern shown in Figure 7c–d and described in Results lines 109 and 119.
  2. **Reversed edaphic variable importance between Table 1/Results and Discussion:**
     - **Table 1 & Results (lines 73, 83):** *O. baccatus* has `nitrogen` $= 4.2\%$ and `soc` $= 1.9\%$ (permutation importance $1.9\%$ and $2.0\%$); *V. tortilis* has `nitrogen` $= 1.5\%$ and `soc` $= 3.9\%$ (permutation importance $2.5\%$ and $13.4\%$). Line 73 notes: *"In contrast to O. baccatus, V. tortilis showed a slightly greater reliance on soil organic carbon (3.9%) than nitrogen (1.5%)."*
     - **Discussion (line 128):** *"O. baccatus exhibited higher suitability in areas with richer soil organic carbon... V. tortilis, in contrast, showed lower dependence on SOC but responded positively to higher nitrogen concentrations."*
  3. **Unmodeled predictors claimed in the Abstract and Discussion:**
     - **Abstract (line 5):** Claims *"A suite of bioclimatic, edaphic, topographic, and anthropogenic variables was used"* to build the ENMs, yet Methods (line 39) states that only 4 bioclimatic and 2 edaphic variables were retained for modeling (excluding all topographic [SRTM elevation], anthropogenic [HII], NDVI, and Aridity Index layers).
     - **Discussion (line 126):** Claims `Isothermality` (`bio3`) contributed to the model of *V. tortilis*, whereas `bio3` was excluded during collinearity screening and never entered the model (Table 1, Figure 3).
* **Fix:** Align the Discussion, Abstract, and Conclusion strictly with the actual MaxEnt outputs in Table 1 and Figure 7. Remove all claims regarding `Isothermality`, topographic, and anthropogenic predictors from the model interpretation. Investigate why the MaxEnt model for *O. baccatus* projects a counterintuitive collapse in the cooler western mountains (Hijaz/Asir) and expansion into hot northern/eastern basins under SSP5-8.5 (which likely reflects unimodal response curve truncation on `bio6` peaking at $7\text{–}8\,^\circ\text{C}$, line 91).

### Defect 2: Omission of Model Tuning (`ENMeval`), Partial ROC (`pROC`), and Spatial Thinning Parameters, and Mislabeling of Fixed Thresholds [ Pillar 3, Pillar 4, Pillar 7 — Major ]
* **Location:** Methodology (lines 28, 47, 52) and Results (lines 65, 119).
* **Forensic Evidence:**
  1. **Missing tuning and validation outputs:** Line 47 states `ENMeval` was used to tune feature classes (`L, Q, H, P, T`) and regularization multipliers (`1–5`) via $\Delta\text{AICc}$, test AUC, and omission rates, and line 52 states partial ROC (`pROC` ratio $> 1.8$) and `SDMTune` were computed. None of the selected `FC`/`RM` parameters, $\Delta\text{AICc}$ values, omission rates, or `pROC` ratios are reported anywhere in the manuscript.
  2. **Missing spatial filtering and bias file specifications:** Line 28 states occurrence points were spatially filtered, and line 47 states a kernel density bias file was generated, but neither the spatial thinning distance (in km) nor the kernel bandwidth is reported.
  3. **Misclassification of equal-interval cutoffs as "natural breakpoints":** Line 52 states that suitability maps were *"reclassified based on natural breakpoints from continuous suitability values to define four categories: unsuitable (p < 0.2), low suitability (0.2–0.4), moderate suitability (0.4–0.6), and high suitability (p > 0.6)."* Cutoffs of $0.2, 0.4, 0.6$ are arbitrary fixed equal intervals, not Jenks natural breaks.
  4. **Missing quantitative area tables:** While line 119 mentions a current overlap of ~18,500 $\text{km}^2$ and an ~40% decline under SSP5-8.5, the manuscript provides no table of predicted area ($\text{km}^2$ and $\%$ change) by suitability class for *O. baccatus*, *V. tortilis*, and their overlap across current, 2041–2060, and 2061–2080 periods under SSP2-4.5 and SSP5-8.5, nor does it state what suitability threshold defined the 18,500 $\text{km}^2$ co-occurrence zone.
* **Fix:** Report the selected `ENMeval` parameters ($\text{FC}$, $\text{RM}$, $\Delta\text{AICc}$, $\text{OR}_{10}$), `pROC` ratios, spatial thinning distance, and kernel bandwidth in Section "Results," and add a complete table of predicted suitable and co-occurring areas ($\text{km}^2$) across all scenarios and time periods.

### Defect 3: Unfulfilled Data Availability Statement [ Pillar 7 — Moderate ]
* **Location:** Data Availability Statement (lines 161, 183) and Supplementary Information (lines 39, 91, 149–151).
* **Forensic Evidence:**
  Lines 161 and 183 state *"Data is contained within the article."* However, the compiled occurrence coordinates ($N = 130$ for *O. baccatus* and $N = 138$ for *V. tortilis*), including the new 2022–2024 field survey coordinates, are not included in the article text, tables, or described supplementary files (Additional file 1 is Table S1 of environmental predictor metadata; Additional file 2 is Figures S1–S2 of response curves).
* **Fix:** Provide the complete CSV table of spatially filtered occurrence coordinates (latitude, longitude, species, source) as a Supplementary Dataset or deposit it in an open repository (e.g., Zenodo/Dryad/Figshare).

---

## 4. Quantitative Rubric Scoring

| Rubric Dimension | Score | Max | Diagnostic Justification |
| :--- | :---: | :---: | :--- |
| **1. Methodological & Statistical Rigor** | **1.2** | **3.5** | Reasonable 6-variable predictor screening (`|r| < 0.8`), 10-fold CV, and kernel bias correction, but omits all `ENMeval` optimal parameters, $\Delta\text{AICc}$, omission rates, `pROC` ratios, spatial thinning distances, and quantitative area tables, and relies on a single GCM (`BCC-CSM2-MR`). |
| **2. Claim-to-Evidence Alignment** | **1.0** | **2.5** | Severe self-contradictions between Results/Figure 7 (which show loss of western highland habitat and shift to northern/eastern basins) and Discussion/Conclusion (which claim loss in northern/eastern deserts and persistence in western highland refugia), plus reversed edaphic claims and fabricated `Isothermality` interpretation. |
| **3. Data Integrity & Biological Plausibility** | **1.2** | **2.0** | Combines field surveys (2022–2024, voucher specimens deposited) with GBIF data to study a biologically meaningful desert nurse-plant association, though unimodal clamping on `bio6` ($7\text{–}8\,^\circ\text{C}$) produces questionable projections of highland disappearance under warming. |
| **4. Reproducibility & Data Integrity** | **1.0** | **2.0** | Although "Data is contained within the article" is stated, the 268 occurrence coordinates and analysis scripts are not provided, and fixed $0.2/0.4/0.6$ cutoffs are mislabeled as "natural breakpoints." |
| **Total Composite Score** | **4.4** | **10.0** | **Flawed / Overstated** (Scientific Core Score: **3.4 / 8.0**) |
