# Review of OOD_REP2_07

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **4.8 / 10.0** (Flawed / Overstated)  
* **Score Breakdown:** Rigor: 1.4/3.5 | Claims: 1.2/2.5 | Biology: 1.0/2.0 | Reproducibility: 1.2/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This study compiles 260 taxonomically verified (primarily ITS-barcoded) fungarium records across 10 Chinese species of the medicinal wood-inhabiting fungal genus *Sanghuangporus*, spatially thins them at a $10\text{ km}$ threshold to $n = 72$ occurrence localities, and applies MaxEnt to model current (1970–2000) and future (2030s–2090s across CMIP6 SSP1-2.6, SSP2-4.5, SSP3-7.0, and SSP5-8.5 using BCC-CSM2-MR) habitat suitability across China. The authors compare current models with and without a `Host plant` predictor layer, reporting $\text{AUC} = 0.903$ (with host plant) and $\text{AUC} = 0.899$ (without host plant), a $155.468\%$ increase in highly suitable habitat when `Host plant` is omitted, and a $67.179\%$ to $118.255\%$ expansion of highly suitable habitat across all future climate scenarios. Occurrence metadata are provided in Supplementary Table S1.

Curating sequence-verified fungarium records to resolve historical taxonomic confusion between *Sanghuangporus* and *Phellinus s.l.* and applying $10\text{ km}$ spatial filtering are clear empirical strengths. However, the ecological modeling and future climate projections suffer from three major methodological and biological flaws: (1) the `Host plant` variable is defined in incompatibly different units and spatial representations between the current baseline (raw count of GBIF occurrence records per $1\text{ km}^2$ cell, in $\text{tree/km}^2$) and the future projections (maximum MaxEnt niche suitability index in $\%$ from $0$ to $100$ across 18 tree genera), which is the direct mathematical cause of the sudden $+67\%$ to $+118\%$ jump in future suitable habitat; (2) pooling 10 ecologically distinct, host-specialized fungal species and 18 host tree genera into a single genus-level model violates niche homogeneity and yields biologically impossible "highly suitable" environmental ranges (e.g., elevations up to $6,852\text{ m}$, nearly $2,000\text{ m}$ above the highest alpine treeline); and (3) the comparison between models with and without `Host plant` fails to hold the climatic predictor set constant (swapping `Bio12` for `Bio18`). These issues can be resolved by standardizing the host plant layer across current and future periods, holding climate predictors fixed during ablation, and modeling dominant species individually.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Highly suitable habitat for *Sanghuangporus* will extremely increase (by $67.179\%$ to $118.255\%$) across all future climate scenarios from the 2030s to the 2090s: [Methodologically Flawed].**  
  In Materials and Methods (line 82) and Table 1 (line 75), the current distribution model defines `Host plant` by converting raw GBIF point coordinates into point counts per $30''$ ($\sim 1\text{ km}^2$) grid cell (units: $\text{tree/km}^2$, ranging from $0$ to $1,126\text{ tree/km}^2$, line 100). Because GBIF point records cover only a tiny fraction of $1\text{ km}^2$ cells across China, the current model restricts highly suitable habitat ($20.238 \times 10^4\text{ km}^2$) to cells with $\ge 1$ recorded GBIF host point (as shown when removing `Host plant` causes current highly suitable area to jump by $+155.5\%$ to $51.701 \times 10^4\text{ km}^2$, line 108). For the future scenarios (line 82), however, the authors replace the sparse GBIF count raster with the continuous MaxEnt-predicted niche suitability percentage ($0\%$–$100\%$) taking the maximum value across 18 host tree genera. Feeding a wall-to-wall continuous percentage raster ($0$–$100$) into a MaxEnt response curve trained on sparse point counts ($\ge 1\text{ tree/km}^2$) causes the model to treat nearly all forested cells in China as having host densities $\ge 1\text{ tree/km}^2$. This unit and representation mismatch—not climate warming—explains why every single future scenario immediately jumps to $33.8$–$44.2 \times 10^4\text{ km}^2$ in the 2030s.

* **Excluding the host plant variable increases current highly suitable habitat by 155.468% while barely changing AUC ($0.903$ vs. $0.899$): [Fragile].**  
  First, in Table 1 (lines 66, 72) and Results (line 108), the model with `Host plant` uses `Bio12` (Annual precipitation, $48.0\%$ contribution) and excludes `Bio18`, whereas the model without `Host plant` drops `Bio12` and substitutes `Bio18` (Precipitation of warmest quarter, $57.1\%$ contribution). Changing the climatic predictor set simultaneously with removing `Host plant` confounds the ablation comparison. Second, the reason `Host plant` restricts the current modeled area so drastically while contributing only $16.9\%$ to training gain is that raw GBIF occurrence counts at $1\text{ km}^2$ resolution act as an incomplete spatial sampling mask (reflecting collector effort in GBIF rather than true host tree absence), which also introduces shared collector-location bias with the fungal records.

* **In the highly suitable habitat of *Sanghuangporus*, elevation ranges from $42$ to $6,852\text{ m}$ and annual mean temperature ranges from $-6.7$ to $21.4^\circ\text{C}$: [Methodologically Flawed].**  
  On line 100, the authors state that "Response curves of these critical environmental variables indicated that in the highly suitable habitat Bio1 ranges from $-6.7$ to $21.4^\circ\text{C}$... Bio12 from $371$ to $4,434\text{ mm}$... Elev from $42$ to $6,852\text{ m}$, and Host plant from $1$ to $1,126\text{ tree/km}^2$." Biologically, *Sanghuangporus* species are obligate wood-decaying macrofungi growing on angiosperm trees and shrubs (*Morus*, *Syringa*, *Populus*, *Lonicera*, *Quercus*, etc.); no angiosperm trees exist at $6,852\text{ m}$ on the Tibetan Plateau (where the alpine treeline is $\le 4,900\text{ m}$). Statistically, the reported intervals ($42$–$6,852\text{ m}$, $-6.7$ to $21.4^\circ\text{C}$, $371$–$4,434\text{ mm}$) appear to be the full horizontal axis domains of the MaxEnt response curve plots (where predicted suitability is $>0\%$, not $\ge 75\%$), misread as the thresholds for "highly suitable habitat" ($75\%$–$100\%$).

* **Genus-level modeling accurately captures the ecological niche of the 10 Chinese *Sanghuangporus* species: [Overstated].**  
  As noted in the Introduction (lines 19, 23), individual *Sanghuangporus* species exhibit strict host specialization and distinct thermal/elevational niches (e.g., subalpine *S. alpinus* on *Lonicera* vs. temperate *S. baumii* on *Syringa* and *S. vaninii* on *Populus* vs. subtropical *S. zonatus*). Pooling all 10 species and taking the maximum suitability across 18 host tree genera creates a composite envelope where a subalpine fungus's climate tolerance can be paired with a lowland subtropical host genus, overestimating ecological breadth.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Standardize the Host Plant Predictor Between Current and Future Models
* **WHY:** Training the current *Sanghuangporus* MaxEnt model on raw GBIF point counts per $1\text{ km}^2$ ($\text{tree/km}^2$) and then projecting future distributions using continuous MaxEnt host suitability percentages ($0\%$–$100\%$) violates variable consistency and creates an artificial $+67\%$ to $+118\%$ surge in future suitable habitat.
* **WHAT:** Use the exact same variable definition—the MaxEnt-predicted current niche suitability index ($0\%$–$100\%$) of the host plant genera—as the `Host plant` predictor in the **current** (1970–2000) *Sanghuangporus* model before projecting onto the future (2030s–2090s) host suitability rasters.
* **HOW:** Since the authors already fitted current and future MaxEnt models for the 18 host plant genera (line 82, Supplementary Fig. S5), replace the raw GBIF count raster in the current *Sanghuangporus* model with the current ($1970$–$2000$) composite host suitability raster ($0\%$–$100\%$), re-fit the current *Sanghuangporus* MaxEnt model, and recompute the future area changes in Supplementary Tables S2 and S3 against this commensurate baseline.

#### 2. Hold Climate Predictors Fixed When Testing Host Plant Exclusion
* **WHY:** Comparing the current model with `Host plant` (which uses `Bio12`) against a model without `Host plant` (which replaces `Bio12` with `Bio18`, Table 1) conflates the removal of the host variable with a change in the precipitation variable.
* **WHAT:** Retain the exact same six abiotic variables (`Bio1`, `Bio3`, `Bio7`, `Bio12`, `Bio15`, `Elev`) in both the host-included and host-excluded models.
* **HOW:** Re-run the host-excluded MaxEnt model using `Bio1`, `Bio3`, `Bio7`, `Bio12`, `Bio15`, and `Elev`, and report the resulting $\text{AUC}$, variable contributions, and habitat area in Table 1 and Supplementary Table S2.

#### 3. Correct the Environmental Range Thresholds for Highly Suitable Habitat
* **WHY:** Reporting that "highly suitable habitat" spans elevations up to $6,852\text{ m}$ and temperatures down to $-6.7^\circ\text{C}$ (line 100) reflects the entire x-axis range of the marginal response plots rather than the interval where suitability exceeds the high-suitability threshold ($\ge 0.75$).
* **WHAT:** Extract and report the exact intervals of `Bio1`, `Bio3`, `Bio7`, `Bio12`, `Bio15`, `Elev`, and `Host plant` where the MaxEnt logistic/cloglog response curves (and mapped highly suitable pixels) satisfy $\text{Suitability} \ge 0.75$ (or $\ge 0.50$).
* **HOW:** From the MaxEnt `.html` response curve output tables (or by extracting raster values across all pixels with suitability $\ge 0.75$ in ArcGIS), report the 5th–95th percentile range (and min–max at $P \ge 0.75$) for each variable in the Results text.

#### 4. Provide Species-Specific Models for Well-Sampled Taxa and Report Uncertainty Across Replicates
* **WHY:** Pooling 10 species with distinct host tree requirements obscures species-specific conservation needs, and reporting single point estimates to 3 decimal places (e.g., $155.468\%$, $261.312\text{ km}$) overstates precision from $n = 72$ points and a single GCM (`BCC-CSM2-MR`).
* **WHAT:** Fit separate MaxEnt models for the 2–3 most abundant individual species in Supplementary Table S1 (pairing each species only with its documented host genus), report mean $\pm$ SD across the 10 cross-validation replicates, and round percentage and distance estimates to 1 decimal place.
* **HOW:** Subset the occurrence records for the best-sampled species (those with $\ge 15$ spatially thinned points), run MaxEnt with their specific host genus suitability layer, and include these species-specific maps alongside the genus-level composite.
