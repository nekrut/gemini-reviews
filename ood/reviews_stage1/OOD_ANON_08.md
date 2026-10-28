# Review of OOD_ANON_08

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **5.8 / 10.0** (Mixed / Salvageable)  
* **Score Breakdown:** Rigor: 1.6/3.5 | Claims: 1.5/2.5 | Biology: 1.4/2.0 | Reproducibility: 1.3/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This mycological and ecological modeling study uses Maximum Entropy (`MaxEnt`) species distribution modeling to predict the current and future geographic distribution in China of the medicinal wood-inhabiting macrofungal genus *Sanghuangporus* (10 Chinese species, Hymenochaetales, Basidiomycota) across four CMIP6 Shared Socioeconomic Pathways (SSP1-2.6, SSP2-4.5, SSP3-7.0, SSP5-8.5) and four 20-year periods (2030s, 2050s, 2070s, 2090s) under the `BCC-CSM2-MR` general circulation model. Drawing on 260 fungarium specimens verified by ITS barcoding and morphology—thinned at a $10\text{ km}$ spatial threshold to 72 records—the authors combine six uncorrelated WorldClim v2.1 bioclimatic and elevation variables with a host-plant predictor derived from 18 host tree genera in GBIF. They report that including the host plant variable reduces predicted current highly suitable area from $51.701 \times 10^4\text{ km}^2$ to $20.238 \times 10^4\text{ km}^2$ (a $155.5\%$ increase when excluded) while projections under all 16 future scenarios predict a $67.2\%$ to $118.3\%$ expansion of highly suitable habitat.

The study has clear strengths in its specimen provenance: the 260 fungarium records (HMAS, BJFC, IFP) are taxonomically verified via ITS barcoding and compiled with coordinates and host metadata in Supplementary Table S1, and the $10\text{ km}$ spatial thinning is appropriate. However, the modeling framework contains a fundamental incompatibility in how the "Host plant" variable is defined between the current and future models: in the current model, "Host plant" is entered as raw GBIF occurrence point counts per $1\text{ km}^2$ pixel ($\text{tree/km}^2$, ranging from $1$ to $1,126$), whereas in the future models, "Host plant" is replaced by a MaxEnt-predicted niche suitability index ($0\%$–$100\%$, taking the maximum across 18 host tree genera). Projecting a model trained on raw specimen count density onto a $0$–$100$ probability scale violates variable-scale invariance and directly drives the claimed $67\%$–$118\%$ future habitat expansion. In addition, pooling 10 host-specialized fungal species into a single genus-level niche model and relying on a single climate model (`BCC-CSM2-MR`) limit the precision of the forecasts.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Extreme expansion ($67.2\%$ to $118.3\%$) of highly suitable habitat for *Sanghuangporus* across all future climate scenarios (Abstract, Results, Figure 3, Table S2): [Methodologically Flawed].**  
  In the "Environmental variables" section, the authors explain how the host plant variable was constructed:
  - *Current model:* "The number of host plants on each coordinate [from GBIF] was converted to raster data by ArcGIS at a spatial resolution of 30''... Host plant ($\text{tree/km}^2$)" with a response range of "$1$ to $1,126\text{ tree/km}^2$." Because GBIF records are point occurrences at $1\text{ km}^2$ resolution, $>99\%$ of grid cells in China have $0$ GBIF records and only cells containing sampled herbarium points have non-zero counts ($1$–$1,126$).
  - *Future models:* "the distribution of their host plants (18 genera) under multiple future scenarios was separately predicted with the same method as used for *Sanghuangporus*... The predicted index of niche suitability of host plants in a percentage form [$0$–$100$] was converted to raster data... If more than one host plant genera were present in a single raster, the highest index of niche suitability from these genera was selected."
  Feeding a continuous $0$–$100$ maximum-suitability raster into a MaxEnt model that was trained on sparse point-count data ($0$ vs. $1$–$1,126\text{ tree/km}^2$) causes every pixel in China where *any* of the 18 tree genera has predicted suitability $\ge 1\%$ to be treated by the current model as having $\ge 1\text{ tree/km}^2$ (which satisfies the current response curve threshold of $1$–$1,126\text{ tree/km}^2$). Thus, the massive apparent jump in highly suitable area under all future scenarios ($+67\%$ to $+118\%$ already in the 2030s across all SSPs) is an artifact of switching the host predictor from sparse GBIF point counts in the present to continuous SDM suitability surfaces in the future.

* **Decisive restricting role of host plants on current *Sanghuangporus* distribution ($155.5\%$ increase in highly suitable area when excluded, Figure 2A vs. 2B): [Fragile].**  
  While the biological premise that obligate wood-inhabiting fungi are restricted by host tree distribution is entirely sound, representing current host distribution by raw unmodeled GBIF point counts per $1\text{ km}^2$ pixel conflates true host tree range with GBIF botanical sampling effort (and suffers from $89/260 = 34.2\%$ missing or genus-unidentified host records in the fungal dataset itself). When the raw GBIF point-density layer is included (Figure 2A), it restricts high suitability to areas with dense GBIF tree collection points, whereas the future projections use modeled host SDM rasters.

* **Genus-level niche modeling pooling 10 ecologically distinct *Sanghuangporus* species (Introduction, Materials and methods): [Fragile].**  
  As the authors note in the Introduction, the 10 Chinese *Sanghuangporus* species inhabit different host plant genera with strong specificity and occupy distinct climatic niches—from high-altitude boreal/subalpine *S. alpinus* and temperate *S. baumii* / *S. vaninii* (northeastern China) to subtropical *S. sanghuang* and *S. zonatus* (central/southern China). Pooling all 10 species into a single genus-level MaxEnt model produces an artificial composite niche spanning Annual Mean Temperatures (`Bio1`) from $-6.7^\circ\text{C}$ to $+21.4^\circ\text{C}$ and Elevations from $42\text{ m}$ to $6,852\text{ m}$ (Results, page 5). Moreover, take-the-maximum aggregation across all 18 host tree genera assumes that any *Sanghuangporus* species can colonize any of the 18 tree genera, erasing species-specific host constraints.

* **Taxonomic verification and curation of the 260 *Sanghuangporus* fungarium records (Materials and methods, Table S1): [Well Supported].**  
  The authors' curation of 260 specimen records from HMAS, BJFC, and IFP using ITS barcoding to resolve historical misidentifications (such as *Phellinus igniarius*, *S. baumii*, and *S. vaninii* complexes) and their $10\text{ km}$ spatial filtering to 72 independent localities represent a high-quality, reproducible biodiversity dataset.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Harmonize the Host Plant Variable Between Current and Future Models
* **WHY:** Training the current *Sanghuangporus* MaxEnt model on raw GBIF point counts per $1\text{ km}^2$ ($\text{tree/km}^2$) and projecting future models onto MaxEnt-predicted host suitability percentages ($0$–$100\%$) creates a severe scale and sparsity mismatch that artificially inflates future habitat area by $67\%$–$118\%$.
* **WHAT:** Use the exact same MaxEnt-modeled host niche suitability index ($0$–$100\%$) for the **current** climate baseline as is used for the **future** climate scenarios.
* **HOW:** Since the authors already ran MaxEnt models for the 18 host tree genera to project their future distributions (Supplementary Figure S5), take the **current** predicted suitability rasters ($0$–$100\%$) of those 18 host tree genera, compute the per-pixel maximum suitability index in the exact same way as done for the future scenarios, and re-fit the current *Sanghuangporus* MaxEnt model using that continuous current host suitability raster. Then recompute the percentage change between current and future suitable areas in Table S2.

#### 2. Run Separate Species-Level Models for the Major Well-Sampled *Sanghuangporus* Species
* **WHY:** Pooling subalpine (*S. alpinus*), temperate (*S. baumii*, *S. vaninii*, *S. lonicericola*), and subtropical (*S. sanghuang*) species yields an overly broad composite niche ($-6.7^\circ\text{C}$ to $21.4^\circ\text{C}$; $42\text{ m}$ to $6,852\text{ m}$) and pairs temperate fungi with subtropical host trees.
* **WHAT:** Fit individual species-level MaxEnt models (paired with each species' specific host tree genus, e.g., *Syringa* for *S. baumii*, *Populus* for *S. vaninii*, *Morus* for *S. sanghuang*, *Lonicera* for *S. lonicericola*) for the 3–4 species with $\ge 15$ spatially independent records, and compare their stacked suitability against the genus-level model.
* **HOW:** Subset Supplementary Table S1 by species, retain species with $\ge 15$ thinned occurrences, include only the corresponding host genus suitability layer for each species, and report species-specific range shifts alongside the genus composite.

#### 3. Incorporate Multiple CMIP6 General Circulation Models (GCMs) and Evaluate with TSS
* **WHY:** Relying on a single climate model (`BCC-CSM2-MR`) exposes future projections to individual GCM structural bias, and relying solely on MaxEnt default parameters and AUC ignores prevalence sensitivity and model complexity tuning.
* **WHAT:** Average future climate projections across at least 3 CMIP6 GCMs (e.g., `BCC-CSM2-MR`, `MIROC6`, `CESM2` or `MRI-ESM2-0`) and report the True Skill Statistic (TSS) alongside AUC.
* **HOW:** Download the corresponding WorldClim v2.1 30-arc-second rasters for two additional CMIP6 GCMs, average the ensemble predictions across GCMs for each SSP/decade, and report mean $\pm$ SD of both AUC and TSS across the 10 cross-validation replicates.
