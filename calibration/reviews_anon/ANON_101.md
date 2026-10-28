# Review of ANON_101

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **4.3 / 10.0** (Flawed / Overstated)  
* **Score Breakdown:** Rigor: 1.1/3.5 | Claims: 1.0/2.5 | Biology: 1.0/2.0 | Reproducibility: 1.2/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This study profiles the fecal microbiota of 33 patients with type I endometrioid endometrial cancer (`EC group`) and 32 female inpatient controls undergoing diagnostic curettage with normal endometrial histology (`N group`) recruited between February and July 2021, using V3–V4 16S rRNA sequencing on an Illumina NovaSeq platform (`PRJNA897842`). Using `QIIME2 (v2019.4)` with 97% operational taxonomic unit (OTU) clustering, UniFrac PCoA/Adonis, Wilcoxon rank-sum tests across six taxonomic levels, and `LEfSe` ($\text{LDA} > 4.0$), the authors report 28,537 OTUs in the `N` group and 18,465 OTUs in the `EC` group (42,231 total OTUs, with only 4,771 [11.3%] shared), significantly lower alpha diversity (Chao1, Shannon, Simpson, Observed species) in `EC`, a decrease in *Firmicutes* (*Clostridia* $\to$ *Clostridiales* $\to$ *Ruminococcaceae* $\to$ *Faecalibacterium* $\to$ *F. prausnitzii* and *Gemmiger formicilis*), and an increase in *Proteobacteria* (*Gammaproteobacteria* $\to$ *Enterobacteriales* $\to$ *Enterobacteriaceae* $\to$ *Shigella*). They conclude that gut microbiota dysbiosis may contribute to endometrial cancer and that modulating the gut microbiome may serve as a preventive and therapeutic strategy.

While the study provides publicly accessible 16S sequencing data (`PRJNA897842`) and excludes recent antibiotic/probiotic users, several technical, statistical, and reporting errors undermine its conclusions. First, the sample sizes of the cancer and control groups are swapped between the text ($33$ `EC` and $32$ `N` in Abstract line 8 and Methods line 28) and Table 1 ($33$ `Normal endometrium` and $32$ `Endometrial cancer`), and inside Table 1 the FIGO stage counts for the `EC` column ($21$ Stage I $+ 12$ Stage III $= 33$, summing to $103.13\%$) contradict both the column header ($n = 32$) and the Results text ($19$ Stage IA $+ 1$ Stage IB $= 20$ Stage I cases, line 59). Second, reporting 42,231 distinct 97% OTUs across just 65 human fecal samples (with 88.7% of OTUs exclusive to one group) is biologically implausible and indicates a lack of chimera, singleton, or sequencing-artifact filtering. Third, the differential abundance tests across six nested taxonomic levels omit false discovery rate (FDR) correction and fail to adjust for the 8-year median age gap between groups (median 48 years in `N` vs. 56 years in `EC`), which spans the menopausal transition. Re-processing the raw reads with modern denoising/filtering (`DADA2` with prevalence filtering), reconciling Table 1, and adjusting for age and menopausal status are doable steps needed to make the results reliable.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **The `N` and `EC` cohorts harbor 28,537 and 18,465 OTUs respectively (42,231 total OTUs, with only 11.30% shared between groups), and alpha diversity is significantly lower in endometrial cancer: [Methodologically Flawed].**  
  The human gut microbiota across 65 individuals contains on the order of $10^2\text{--}10^3$ genuine 97% 16S rRNA OTUs, not 42,231. Generating 42,231 OTUs with nearly 90% group-unique OTUs (Figure 1) on an Illumina NovaSeq platform is a classic artifact of clustering unscreened PCR chimeras, index-hopping reads, and low-abundance sequencing errors without singleton/abundance filtering (e.g., removing OTUs with $<0.005\%$ relative abundance or present in only 1 sample). Because Chao1 and Observed-species richness estimators are heavily driven by singleton and rare OTUs, this artifact directly distorts the alpha-diversity comparisons in Figure 2.

* **Patients with endometrial cancer exhibit a significant depletion of *Firmicutes* (*Faecalibacterium prausnitzii*, *Gemmiger formicilis*) and enrichment of *Proteobacteria* (*Shigella*) compared with healthy controls: [Fragile].**  
  First, the five taxa reported as increased (`Proteobacteria -> Gammaproteobacteria -> Enterobacteriales -> Enterobacteriaceae -> Shigella`, all $P \approx 0.0055\text{--}0.0057$) and the five reported as decreased (`Firmicutes -> Clostridia -> Clostridiales -> Ruminococcaceae -> Faecalibacterium`) represent two single hierarchical taxonomic lineages tested repeatedly at every taxonomic rank without Benjamini–Hochberg FDR correction across all detected taxa. At the species level, *F. prausnitzii* has a raw $P = 0.041$ (line 147), which would not survive multiple-testing correction across all species. Second, the `N` group has a median age of 48 years (range 39–58, predominantly pre-/perimenopausal) whereas the `EC` group has a median age of 56 years (range 34–72, predominantly postmenopausal), and the `N` group consists of hospitalized patients admitted for diagnostic curettage (line 28) rather than healthy community controls. Because menopausal estrogen decline and preoperative bowel/hospital preparation strongly shift the gut *Firmicutes*-to-*Proteobacteria*/*Enterobacteriaceae* ratio, unadjusted two-group Wilcoxon tests are confounded by menopausal status and inpatient care.

* **Baseline clinicopathological data in Table 1 accurately summarize the 33 endometrial cancer and 32 control participants: [Methodologically Flawed].**  
  The group sample sizes are inverted between the text and Table 1: the Abstract (line 8) and Methods (line 28) state `33 endometrial cancer patients (EC group) and 32 healthy controls (N group)`, whereas Table 1 (line 68) is headed `Normal endometrium (n = 33)` and `Endometrial cancer (n = 32)`. Furthermore, inside the `Endometrial cancer (n = 32)` column of Table 1:
  1. Under `FIGO stage`, Stage I is listed as `21 (65.63%)` and Stage III as `12 (37.50%)`, which sums to $21 + 12 = 33$ patients and $103.13\%$, while contradicting the Results text (line 59: `stage IA (19 cases), stage IB (1 case)` $= 20$ Stage I cases).
  2. Under `Differentiation`, the counts are `12 + 15 + 5 = 32` (summing to 32, not 33), and under `LN metastasis`, the counts are `21 + 11 = 32` (matching line 59). Thus, some rows in the `EC` column sum to 32 while others sum to 33.

* **Adjusting the gut microbiota is an effective strategy for preventing and treating endometrial cancer: [Overstated].**  
  A cross-sectional, single-center 16S rRNA observational study of 65 individuals cannot establish whether gut microbiome differences precede endometrial carcinogenesis or result from tumor presence, menopausal status, or hospital admission, nor does it test any microbiome-targeted intervention.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Reconcile the Inverted Sample Sizes and Arithmetic Errors in Table 1 and Results
* **WHY:** Swapping $n = 33$ and $n = 32$ between the main text and Table 1 and reporting FIGO stage counts that sum to 33 ($103.13\%$) in a column labeled $n = 32$ undermines confidence in the dataset metadata.
* **WHAT:** Verify the exact number of `EC` and `N` samples among the 65 SRA files in `PRJNA897842` and correct Table 1 and the main text so all counts and percentages are internally consistent.
* **HOW:** Check the clinical spreadsheet for the 65 participants, confirm whether `EC` is $n = 32$ or $n = 33$, correct the Stage I count (`20` vs. `21`) and percentages in Table 1 (lines 68–91) and Results (line 59), and ensure that all percentage denominators match the true group sample size.

#### 2. Apply Standard Abundance and Chimera Filtering to Remove the 42,231 Spurious OTU Artifact
* **WHY:** Retaining 42,231 OTUs across 65 fecal samples means that $>95\%$ of the OTU table consists of unremoved PCR chimeras, sequencing errors, and singletons, which severely inflates Chao1 and Observed species richness and distorts unweighted UniFrac distances.
* **WHAT:** Re-process the 65 fastq files from `PRJNA897842` in `QIIME2` using `DADA2` amplicon sequence variants (ASVs) (or 97% OTUs after `uchime-denovo` chimera removal and filtering out features with total read count $< 10$ or present in $< 2$ samples).
* **HOW:** Run `qiime dada2 denoise-paired` followed by `qiime feature-table filter-features --p-min-frequency 10 --p-min-samples 2`. Recompute the Venn diagram (Figure 1), rarefaction curves and alpha diversity (Figure 2), and UniFrac PCoA/Adonis (Figure 3) on the filtered table, where total genuine gut ASVs/OTUs should be on the order of $500\text{--}2,500$.

#### 3. Apply Benjamini–Hochberg FDR Correction and Adjust for Age and Menopausal Status
* **WHY:** Testing dozens of taxa across six taxonomic levels with unadjusted Wilcoxon tests inflates false positives, and the 8-year median age difference between `N` (48 years) and `EC` (56 years) confounds cancer status with menopausal status.
* **WHAT:** Report Benjamini–Hochberg FDR-adjusted $q$-values for all taxonomic comparisons and run multivariable differential abundance models adjusting for age, BMI, and menopausal status.
* **HOW:** Add menopausal status (premenopausal vs. postmenopausal) to Table 1, apply `p.adjust(p_values, method = "BH")` within each taxonomic rank in Figure 4, and run `MaAsLin2` or `ANCOM-BC2` (`~ Group + Age + BMI`) in R to verify whether *Shigella*/*Enterobacteriaceae* enrichment and *Faecalibacterium* depletion remain statistically significant after adjusting for age and BMI.

#### 4. Clarify V3–V4 16S Taxonomic Resolution Limits and Temper Clinical Claims
* **WHY:** Short-read V3–V4 16S rRNA amplicons (~468 bp) cannot reliably distinguish *Shigella* from *Escherichia coli* (which share $>99.5\%$ 16S rRNA sequence identity and are properly denoted *Escherichia-Shigella*), nor can cross-sectional associations support clinical prevention/treatment claims.
* **WHAT:** Relabel *Shigella* as *Escherichia-Shigella* (or note the 16S resolution limit) and temper the preventive/therapeutic claims in the Abstract and Conclusion.
* **HOW:** Update the Abstract, Results, and Discussion to note that V3–V4 16S sequences assigned to *Shigella* represent the *Escherichia-Shigella* group, and revise the final sentence of the Abstract and Conclusion to state that these cross-sectional associations warrant longitudinal and mechanistic validation.

#### 5. Technical and Editorial Fixes
* **WHY:** Several minor errors appear in the PCR protocol description and species spelling.
* **WHAT & HOW:**
  1. **PCR thermal cycle description (Materials and Methods, line 37):** Change `"25 cycles of predenaturation at 98 °C for 5 min, denaturation at 98 °C for 30 s..."` to `"initial predenaturation at 98 °C for 5 min, followed by 25 cycles of denaturation at 98 °C for 30 s, annealing at 52 °C for 30 s, and extension at 72 °C for 45 s, with a final extension at 72 °C for 5 min"` (predenaturation for 5 min at $98^\circ\text{C}$ is performed once, not repeated 25 times).
  2. **Species name spelling (Abstract line 8, Discussion line 163):** Change `"Gemmiger_formicis"` to `"Gemmiger formicilis"`.
  3. **Terminology (Abstract line 8, Introduction line 20, Methods line 37, Discussion line 163):** Change `"microbioma"` to `"microbiome"` or `"microbiota"`.
