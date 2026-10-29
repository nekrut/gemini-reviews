# Review of FEXP_ANON_059

**Overall Score:** **5.8 / 10.0** (Mixed / Salvageable) | **Scientific Core Score:** **4.1 / 8.0**  
* **Score Breakdown:** Rigor: 1.5/3.5 | Claims: 1.3/2.5 | Biology: 1.3/2.0 | Reproducibility: 1.7/2.0

---

## 1. Blinded Metadata Perception

* **Perceived Field & Subfield:** Infectious Disease Microbiome Meta-Analysis / Pulmonary Tuberculosis (PTB) and Antitubercular Therapy (ATT) 16S rRNA Profiling
* **Study Design:** Secondary bioinformatic re-analysis of four publicly available 16S rRNA amplicon sequencing datasets across four geographical regions using a unified QIIME2 (DADA2, SILVA v138) and PICRUSt2/STAMP pipeline.
* **Model System & Sample Size:** Human fecal 16S rRNA samples ($N = 213$ total across 4 NCBI SRA studies: Dataset 1 India `SRP079687` [V3 region, $n = 24$: 6 TB, 6 TBW, 6 TBM, 6 HHC], Dataset 2 Taiwan `PRJEB29035` [V3–V5 region, $n = 51$: 31 TB, 20 HC], Dataset 3 West Africa/Mali `PRJNA622267` [V4 region, $n = 50$: 20 TB, 20 TB2M, 10 HC], and Dataset 4 South Africa `PRJNA664352` [V4 region, $n = 88$: 31 TB, 57 CC]).
* **Perceived Methodological Maturity:** Commendable open-science reproducibility (all QIIME2 artifacts and R scripts archived on Zenodo `10.5281/zenodo.15321064`), but weakened by 100% collinearity between "geographical location" and incompatible 16S hypervariable regions (V3 vs. V3–V5 vs. V4) in the cross-study weighted UniFrac analysis, reliance on unadjusted $p$-values in LEfSe after FDR correction eliminated significance in 3 of 4 cohorts, unadjusted STAMP Welch's $t$-tests on PICRUSt2 pathways, and internal contradictions regarding global PERMANOVA significance.

---

## 2. Executive Summary & Editorial Verdict

This study re-analyzes 213 publicly available fecal 16S rRNA amplicon samples from four pulmonary tuberculosis (PTB) cohorts spanning India (`SRP079687`, V3), Taiwan (`PRJEB29035`, V3–V5), West Africa/Mali (`PRJNA622267`, V4), and South Africa (`PRJNA664352`, V4) through a single bioinformatic workflow (`FastQC` $\rightarrow$ `BBDuk` $\rightarrow$ `QIIME2 2023.5 DADA2` rarefied to 12,400 reads $\rightarrow$ `SILVA v138` $\rightarrow$ `phyloseq`/`microeco` $\rightarrow$ `PICRUSt2 2.5.2` + `STAMP`; Zenodo `10.5281/zenodo.15321064`). Within individual regions, significant reductions in alpha diversity (Observed taxa $p < 0.001$; Shannon index $p < 0.05$) and FDR-corrected LEfSe taxonomic differences are detected only in the West African cohort after two months of antitubercular therapy (`TB2M`). Across regions, pairwise weighted UniFrac distances differ significantly between countries but not between disease/control groups within the same country. Using unadjusted $p < 0.05$ in LEfSe and STAMP Welch's $t$-tests, the authors report candidate discriminant genera in all four cohorts (noting `Clostridia_UCG-014` in healthy groups across three cohorts) and predicted depletion of 62 MetaCyc pathways (including vitamin, amino acid, and energy biosynthesis) after two months of ATT in West Africa.

**Editorial Verdict: Major Revision (Mixed / Salvageable).** The systematic screening of public SRA tuberculosis datasets and complete archiving of QIIME2 outputs and R code on Zenodo (`10.5281/zenodo.15321064`) are valuable contributions. However, three major methodological issues must be corrected:
1. **Confounding of "Geographical Location" with Incompatible 16S Hypervariable Regions (V3 vs. V3–V5 vs. V4) in Weighted UniFrac Beta Diversity:** The manuscript's central conclusion—that *"geographical location exerts a more significant impact on microbial diversity than the disease state in a specific location"*—is based on weighted UniFrac comparisons across India (V3 amplicon), Taiwan (V3–V5 amplicon), and West/South Africa (V4 amplicon) (Table 1, Figure 2). Because DADA2 generates exact amplicon sequence variants (ASVs) specific to the amplified primer region, ASVs from non-overlapping or differently framed regions (e.g., V3 vs. V4) cannot be validly aligned de novo to build a unified phylogenetic tree for UniFrac without fragment insertion (`q2-fragment-insertion` / `SEPP`), and even with fragment insertion, each geographical location (India, Taiwan) is 100% confounded with its unique primer pair, DNA extraction protocol, and study batch.
2. **Reverting to Unadjusted LEfSe P-Values After FDR Correction Fails in 3 of 4 Cohorts:** In Section "Statistical analysis" (line 61), the authors candidly note that after Benjamini–Hochberg FDR correction in `microeco`, *"significant differences were detected only in the sub-groups of the West African population."* Yet in Section "Discriminant taxa" (line 92, Figure 3), they proceed to report and interpret 18, 21, and 4 "discriminative marker genera" in Taiwan, South Africa, and India based on **unadjusted** $p < 0.05$. Similarly, PICRUSt2 MetaCyc pathway comparisons in STAMP (Table 2, lines 68 and 119–138) use unadjusted Welch's $t$-tests ($p < 0.05$) across hundreds of predicted pathways.
3. **Internal Contradiction on Global Beta-Diversity PERMANOVA:** Methods line 61 states *"The compositional variations among the groups were found to be statistically significant based on PERMANOVA test,"* whereas Results line 84 and the Abstract state *"Additionally, no significant differences were observed in overall beta diversity across the datasets."*

### Specific Conclusions and Assessment of Support

* **Two months of antitubercular therapy (ATT) in the West African cohort significantly reduces gut microbial richness and Shannon diversity: [Well Supported].**  
  Within Dataset 3 (`PRJNA622267`, uniform V4 protocol), Observed ASVs ($p < 0.001$, HC vs. TB2M) and Shannon diversity ($p < 0.05$, TB vs. TB2M) decline significantly after 2 months of ATT (Figure 1), and discriminant taxa in this cohort survive Benjamini–Hochberg FDR correction (line 61).

* **Geographical location exerts a stronger effect on gut microbial beta diversity than tuberculosis disease status: [Methodologically Flawed].**  
  In Table 1, geographical location is completely collinear with 16S target region (India = V3, Taiwan = V3–V5, West/South Africa = V4) and study-specific wet-lab protocols. Computing weighted UniFrac across ASVs derived from different 16S hypervariable regions without phylogenetic fragment insertion (`SEPP`) or genus-level harmonization confounds technical primer/amplicon divergence with human biogeography. Only the comparison between West Africa (Mali, V4) and South Africa (Cape Town, V4) shares the same hypervariable region.

* **Specific discriminative marker genera distinguish PTB patients from controls across all four populations (India, Taiwan, West Africa, and South Africa): [Overstated].**  
  As stated on line 61, no genera in the Indian, Taiwanese, or South African datasets survived Benjamini–Hochberg FDR correction. Presenting unadjusted $p < 0.05$ hits across hundreds of tested genera as population-specific "marker taxa" (Figure 3, lines 92–101) inflates false positives, especially in Dataset 1 (India), where each subgroup contains only $n = 6$ samples.

* **Antitubercular therapy depletes 62 predicted microbial metabolic pathways (including vitamin, amino acid, and energy biosynthesis) after two months of treatment: [Fragile].**  
  PICRUSt2 functional inferences from short 16S amplicons were tested in STAMP using unadjusted pairwise Welch's $t$-tests ($p < 0.05$, line 68) without Benjamini–Hochberg FDR correction, and longitudinal treatment groups in India (`TB`, `TBW`, `TBM`, $n = 6$ each) and Mali (`TB`, `TB2M`, $n = 20$ each) were analyzed as unpaired samples.

---

## 3. Forensic Defect Inventory

### 1. Cross-Region Weighted UniFrac Confounded by Non-Overlapping 16S Amplicons (V3, V3–V5, V4) (Pillars 2, 3, 5)
* **Defect:** Table 1 shows that the four datasets amplified three different 16S regions: V3 (India), V3–V5 (Taiwan), and V4 (West Africa and South Africa). The authors generated ASVs with DADA2 and computed weighted UniFrac distances across all four studies simultaneously (Figure 2).
* **WHY:** DADA2 ASVs from V3 and V4 do not share homologous nucleotide coordinates. A standard de novo multiple sequence alignment of non-overlapping V3 and V4 ASVs places them on artificial deep branches of the phylogenetic tree, making weighted UniFrac distances between V3 (India) and V4 (Africa) an artifact of amplicon region rather than biological phylogenetic turnover.
* **WHAT:** Use SATé-enabled phylogenetic placement (`q2-fragment-insertion sepp` into the SILVA 128/138 full-length reference tree) or aggregate counts to the shared **genus** level (using Bray–Curtis or Aitchison distance) before performing cross-study ordinations, and explicitly partition variance (`adonis2`) between `hypervariable_region`, `country`, and `disease_status`.
* **HOW:** Run `qiime fragment-insertion sepp` on all representative ASV sequences to place V3, V3–V5, and V4 reads onto a single reference backbone tree (or compute genus-level Bray–Curtis distances in `phyloseq`), and test `adonis2(dist ~ hypervariable_region + location + group)` to quantify how much cross-location variance remains between West Africa and South Africa (both V4) independent of primer region.

### 2. Unadjusted Multiple Testing in LEfSe (Figure 3) and PICRUSt2/STAMP (Table 2) (Pillars 1, 4)
* **Defect:** (a) After finding that Benjamini–Hochberg FDR correction in `microeco` left zero significant taxa in India, Taiwan, and South Africa (line 61), the authors plotted and interpreted unadjusted $p < 0.05$ LEfSe results across all four datasets (line 92, Figure 3). (b) In Section "Predicted metabolic gene pathway analysis" (line 68, Table 2), STAMP Welch's $t$-tests across hundreds of MetaCyc pathways were conducted at unadjusted $p < 0.05$ without FDR control.
* **WHY:** Testing hundreds of genera and MetaCyc pathways at unadjusted $p < 0.05$ guarantees dozens of false-positive discoveries by chance alone.
* **WHAT:** Report Benjamini–Hochberg FDR-adjusted $q$-values for all LEfSe and STAMP MetaCyc pathway comparisons, and clearly distinguish FDR-significant findings (West Africa `TB2M`) from exploratory nominal trends ($p < 0.05, q > 0.05$).
* **HOW:** In STAMP (or R), apply Benjamini–Hochberg FDR correction (`p.adjust(..., method = "BH")`) to the Welch's $t$-test / Wilcoxon $p$-values for all MetaCyc pathways in Table 2, add a column to Table 2 showing the number of pathways surviving $q < 0.05$, and label the India, Taiwan, and South Africa panels in Figure 3 as exploratory unadjusted trends.

### 3. Contradictory Statements on Global Beta-Diversity PERMANOVA (Pillars 3, 7)
* **Defect:**
  * Abstract (line 9): *"Additionally, there were no statistically significant differences observed in pairwise comparisons within the same location or in the aggregate beta diversity of the datasets."*
  * Methods (line 61): *"The compositional variations among the groups were found to be statistically significant based on PERMANOVA test."*
  * Results (line 84): *"Several statistically significant pairwise comparisons between different locations were found... Additionally, no significant differences were observed in overall beta diversity across the datasets."*
* **WHY:** It is mathematically contradictory for the omnibus PERMANOVA test across groups to be both "statistically significant" (line 61) and show "no significant differences... in overall beta diversity across the datasets" (line 84) while numerous cross-location pairwise comparisons in Figure 2 are highly significant.
* **WHAT & HOW:** Report the exact omnibus PERMANOVA $F$-statistic, $R^2$, degrees of freedom, and $p$-value in the Results (Section "Beta diversity analysis", line 84), and clarify whether the non-significant omnibus statement referred to testing `Disease_Status` pooled across all four countries (which is masked by inter-study variance) versus testing `Location_Group` across all 12 study subgroups.

---

## 4. Quantitative Rubric Scoring

| Rubric Dimension | Score | Max | Forensic Justification |
| :--- | :---: | :---: | :--- |
| **1. Methodological & Statistical Rigor** | **1.5** | **3.5** | Cross-region weighted UniFrac analysis is confounded by non-overlapping 16S amplicon regions (V3 vs. V3–V5 vs. V4); LEfSe (Figure 3) and STAMP PICRUSt2 (Table 2) rely on unadjusted $p < 0.05$ after FDR correction yielded null results in 3 of 4 cohorts; longitudinal ATT timepoints treated as unpaired. |
| **2. Claim-to-Evidence Alignment** | **1.3** | **2.5** | Limitations section candidly acknowledges primer-region biases, PICRUSt2 limits, and unadjusted LEfSe $p$-values, but the Abstract and Conclusions still attribute cross-study variance primarily to "geographical location" and highlight unadjusted taxon/pathway hits. |
| **3. Data Integrity & Biological Plausibility** | **1.3** | **2.0** | Thoughtful discussion of household contact (`HHC`/`CC`) latent exposure vs. community controls (`HC`) and ATT duration effects, but de novo ASV UniFrac across different 16S variable regions is biologically distorted by primer non-overlap. |
| **4. Reproducibility & Data Integrity** | **1.7** | **2.0** | High reproducibility: all four public SRA accessions and group sample sizes are clearly tabulated in Table 1, and the processed QIIME2 outputs and R analysis scripts are publicly archived on Zenodo (`10.5281/zenodo.15321064`). Minor contradiction in omnibus PERMANOVA reporting between lines 61 and 84. |
| **Scientific Core Score** | **4.1** | **8.0** | Sum of Rigor (1.5) + Claims (1.3) + Biology (1.3). |
| **Overall Composite Score** | **5.8** | **10.0** | **Mixed / Salvageable Tier** (Sum of all four dimensions). |
