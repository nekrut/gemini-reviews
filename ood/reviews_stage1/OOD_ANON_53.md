# Review of OOD_ANON_53

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **7.7 / 10.0** (Strong / Sound)  
* **Score Breakdown:** Rigor: 2.6/3.5 | Claims: 1.8/2.5 | Biology: 1.6/2.0 | Reproducibility: 1.7/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This study integrates whole-genome resequencing, genotype-environment association (GEA), ecological niche modeling (ENM), and landscape genetics to assess intraspecific climate change vulnerability in two Sino-Himalayan montane passerines: Elliot's laughingthrush (*Trochalopteron elliotii*, $n = 55$ resequenced individuals at $19.1\times$ depth; 10.3M SNPs mapped to a new $1.12\text{ Gb}$ de novo 10X Genomics reference assembly) and the green-backed tit (*Parus monticolus*, $n = 58$ individuals at $15.5\times$ depth; 3.9M SNPs). Using `gradientForest`, generalized dissimilarity modeling (`GDM`), and three outlier detection methods (`LFMM`, `RDA`, `dbRDA`), the authors identify climate-associated SNPs (72 in *T. elliotii*, 798 in *P. monticolus*) that partition each species into three locally adapted groups: cold-dry, warm-humid, and warm-dry tolerant. Projecting across four GCMs and two emission pathways (RCP 4.5 and RCP 8.5 for 2050 and 2070), they find an inverse pattern between genomic offset and ecological niche suitability change (NSC): cold-dry populations exhibit higher genomic offset but lower habitat suitability loss than warm-tolerant populations. Combining these metrics into a genome-niche index (`gni`) alongside `Circuitscape`/MLPE landscape resistance and `fastsimcoal2` demographic modeling, they identify central Southwest Mountain populations as evolutionary rescue donors. Raw genome assemblies, resequencing reads, VCF files, occurrence records, and analysis scripts are publicly deposited in NCBI/CNGB and Dryad.

This is a comprehensive, well-executed ecological genomics study with high data quality and open code/data availability. However, two methodological issues temper the strength of the quantitative conclusions. First, the classification of museum/GBIF occurrence records into the three "climate-tolerant" genetic groups for group-specific ENMs (292 records for *T. elliotii*, 619 for *P. monticolus*) and grid-level Wilcoxon rank-sum tests ($n = 6,926$ to $42,929$ spatial grid cells) relies on geographic spatial assignment of ungenotyped occurrence records and treats tens of thousands of spatially autocorrelated raster pixels as independent observations in hypothesis testing, inflating statistical significance ($P < 0.001$). Second, the `ADMIXTURE` clustering defining the three "climate-tolerant" groups was performed exclusively on the 72 and 798 climate-outlier SNPs selected by `LFMM`/`RDA`/`dbRDA` rather than neutral genome-wide SNPs, creating circularity between environmental variable selection, group definition, and downstream niche suitability modeling. These limitations can be resolved through spatial degrees-of-freedom adjustments (or locality-level statistical tests) and explicit comparison of neutral versus adaptive genetic structure.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Both *T. elliotii* and *P. monticolus* exhibit significant intraspecific genotype-climate turnover across the Sino-Himalayan Mountains, with consistent outlier signals across `gradientForest`, `GDM`, `LFMM`, `RDA`, and `dbRDA`: [Well Supported].**  
  The whole-genome resequencing depth ($15\text{--}19\times$), de novo reference genome assembly ($90\%$ complete single-copy BUSCOs), and cross-validation across both machine-learning (`gradientForest`) and distance-based (`GDM`, which accounts for small per-locality sample sizes via $F_{ST}$ across 100,000 SNPs) methods provide robust evidence of spatial turnover along temperature and precipitation seasonality gradients.

* **Cold-dry tolerant populations exhibit significantly higher genomic offset but significantly less niche suitability decline (NSC) under future climate scenarios than warm-humid and warm-dry tolerant populations: [Moderately Supported].**  
  While the qualitative divergence between genomic offset (driven by steeper projected temperature changes at high elevations in the southern Tibetan and eastern Himalayan zones) and ENM niche suitability change (driven by topographic buffering and upslope availability in high-relief mountains versus summit traps in mid-elevation eastern mountains) is biologically coherent, the statistical tests in Figures 3c–d, 4g–j, and 5a–b apply two-tailed Wilcoxon rank-sum tests across all raster grid cells ($n = 6,926$ to $42,929$ grids) without accounting for spatial autocorrelation. Furthermore, assigning 292 and 619 museum/GBIF occurrence records (which lack genetic data) to the three `ADMIXTURE` groups based on geographic polygons (while dropping admixed central localities Mangkang, Hanyuan, and Wulong) forces geographic separation into the group-specific `biomod2` ENMs.

* **Central Southwest Mountain populations represent optimal donor populations for evolutionary rescue based on the combined genome-niche index (`gni`), with historical secondary contact (11.5–17.5 kya) and low landscape resistance supporting westward dispersal: [Moderately Supported].**  
  The `fastsimcoal2` coalescent simulations (supporting secondary gene flow during post-glacial expansion) and `Circuitscape`/MLPE resistance models provide solid support that the central Southwest Mountains act as a historical suture zone and dispersal corridor. However, the mathematical formulation of the genome-niche index $gni_i = nsc_i^\alpha \cdot go_i^{1-\alpha}$ (Methods, lines 51–59) is restricted only to grid cells with positive niche suitability change ($nsc_i > 0$), and because both $nsc_i$ (where larger positive values mean *better* future habitat suitability) and $go_i$ (where larger values mean *worse* genomic disruption) are raised to positive powers ($\alpha \approx 0.53\text{--}0.62$, $1-\alpha \approx 0.38\text{--}0.47$), multiplying $nsc_i^\alpha$ by $go_i^{1-\alpha}$ conflates high habitat gain with high genomic offset unless $go_i$ or $nsc_i$ was inverted during normalization—a detail not specified in the text.

* **Shared candidate gene *CRB1* (Crumbs cell polarity complex component 1) underlies adaptation to extreme temperatures in both bird species: [Fragile].**  
  Observing an overlap of 1 gene (*CRB1*) between 23 candidate genes in *T. elliotii* and 147 candidate genes in *P. monticolus* (out of 17,585 annotated genes; hypergeometric $P \approx 0.18$) is consistent with chance overlap. Moreover, *CRB1* is primarily a photoreceptor morphogenesis gene (associated with retinal degeneration and visual sensitivity in penguins under dim/photic conditions rather than thermoregulation), so attributing its allele frequency correlation with mean diurnal temperature range (BIO2) and isothermality (BIO3) to thermal tolerance without functional validation is speculative.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Account for Spatial Autocorrelation in Grid-Level Comparisons of Genomic Offset and NSC
* **WHY:** Applying Wilcoxon rank-sum tests to $6,926\text{--}42,929$ contiguous 2.5-arcminute raster pixels (Figures 3, 4, and 5) violates observation independence due to strong spatial autocorrelation in interpolated climate and `gradientForest`/`biomod2` surfaces, artificially deflating $P$-values by orders of magnitude.
* **WHAT:** Re-evaluate the between-group differences in genomic offset and NSC at the level of actual sampled localities/occurrence points or using spatially corrected degrees of freedom.
* **HOW:** Extract genomic offset and NSC values specifically at the 55 (*T. elliotii*) and 58 (*P. monticolus*) sequenced individual localities (and at the 10-km thinned presence coordinates) and run the Wilcoxon rank-sum tests on those point datasets. For full-raster comparisons, use Clifford-Richardson-Hemon modified $t$-tests (`SpatialPack::modified.ttest` in R) or spatial block bootstrap resampling to account for effective sample size.

#### 2. Decouple Neutral Population Structure from Adaptive Outlier Clustering and Clarify GBIF Record Assignment
* **WHY:** Running `ADMIXTURE` on the 72 and 798 outlier SNPs identified by `LFMM`/`RDA`/`dbRDA` (where `LFMM` itself already used $K = 3$ latent factors) is circular, and the Methods do not explain how the 292 and 619 ungenotyped GBIF/museum records were assigned to the three genetic clusters for `biomod2` modeling.
* **WHAT:** Compare neutral genome-wide `ADMIXTURE` structure against outlier-SNP clustering, and explicitly document the spatial rule used to assign GBIF records to genetic groups.
* **HOW:** Present the `ADMIXTURE` plot and cross-validation error curve for LD-pruned genome-wide neutral SNPs alongside Supplementary Fig. 3 to show whether the three groups reflect deep phylogeographic lineages or purely adaptive ecotypes. In the Methods (Section "Ecological niche modelling"), specify the exact spatial polygon or interpolation boundary used to classify ungenotyped GBIF/museum points into cold-dry, warm-humid, and warm-dry groups, and test sensitivity to including vs. excluding the admixed central Southwest Mountain records.

#### 3. Clarify the Normalization Direction of Genomic Offset and NSC in the Genome-Niche Index (`gni`)
* **WHY:** In $gni_i = nsc_i^\alpha \cdot go_i^{1-\alpha}$, a higher $nsc_i$ indicates *favorable* habitat expansion (low vulnerability), whereas a higher $go_i$ indicates *unfavorable* genetic mismatch (high vulnerability). If both are min-max normalized positively to $[0.1, 0.9]$, their weighted geometric mean multiplies an advantage by a vulnerability, making low $gni_i$ ambiguous (it could mean low genomic offset *or* near-zero niche gain).
* **WHAT:** Explicitly write out the normalization formula for $nsc_i$ and $go_i$ prior to computing $gni_i$.
* **HOW:** In the Methods (Section "Combining genomic offset and NSC"), state whether $nsc_i$ was inverted (e.g., $1 - \text{norm}(nsc_i)$ so that both metrics measure "interruption/vulnerability") or whether $go_i$ was inverted, and verify that the artificial bee colony (`ABCoptim`) objective function $\min Y$ (which minimizes relative entropy/deviation between $gni_i$ and the two input surfaces) is applied to consistently oriented vulnerability metrics.

#### 4. Temper Functional Claims Around *CRB1* and Test Overlap Significance
* **WHY:** Sharing 1 gene (*CRB1*) across gene lists of size 23 and 147 is not statistically enriched above random expectation, and *CRB1* functions in retinal photoreceptor integrity (which covaries with solar radiation/cloud cover captured by diurnal temperature range BIO2).
* **WHAT:** Report the exact hypergeometric $P$-value for gene-list overlap and discuss photic/radiation gradients alongside temperature.
* **HOW:** Add a one-sentence caveat in the Results/Discussion noting that the single-gene overlap (*CRB1*) does not exceed genome-wide chance expectation ($P > 0.15$) and may reflect adaptation to high-elevation light/UV regimes correlated with diurnal temperature range (BIO2/BIO3).

#### 5. Technical, Mathematical, and Editorial Cleanup
* **WHY:** Several typographical errors in years, elevations, and method acronyms appear in the main text and Methods.
* **WHAT & HOW:**
  * **Results (Line 67):** Correct the future projection year typo `"in 2050 and 5070, respectively"` to `"in 2050 and 2070, respectively"`.
  * **Methods (Line 135):** Correct the upper elevation typo `"commonly found between 1500 and 45,000 m a.s.l."` to `"1500 and 4500 m a.s.l."` (and fix `"P. monticulus"` to `"P. monticolus"`).
  * **Fig. 4 Caption (Line 75) & Methods (Line 31):** Correct the repeated acronym typo `"RAD and dbRAD"` to `"RDA and dbRDA"` (Redundancy Analysis and distance-based Redundancy Analysis, not Restriction-site Associated DNA).
  * **Results (Line 79):** Correct the figure cross-reference `"Fig. 3i, j"` to `"Fig. 4i, j"`.
  * **Methods (Line 140):** Correct `"TABASTN v2.2.26"` to `"TBLASTN v2.2.26"`.
