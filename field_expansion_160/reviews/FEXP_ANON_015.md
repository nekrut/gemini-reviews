# Review of FEXP_ANON_015

**Overall Score:** **5.7 / 10.0** (Mixed / Salvageable) | **Scientific Core Score:** **4.3 / 8.0**  
* **Score Breakdown:** Rigor: 1.5/3.5 | Claims: 1.4/2.5 | Biology: 1.4/2.0 | Reproducibility: 1.4/2.0

---

## 1. Blinded Metadata Perception
* **Anonymized Manuscript ID:** `FEXP_ANON_015`
* **Perceived Domain & Design:** Regional viral genomic surveillance and descriptive molecular epidemiology; longitudinal narrative analysis of $n = 3,493$ SARS-CoV-2 sequences collected across two diagnostic laboratories in Mecklenburg-Western Pomerania (`M-V`), northeastern Germany, between March 2020 and April 2022 (`CoMV-Gen` project).
* **Blinding Integrity:** Double-blind review maintained; evaluated strictly on internal bioinformatic, statistical, and epidemiological merits at $t_0$.

---

## 2. Executive Summary & Editorial Verdict

This study describes two years of regional SARS-CoV-2 genomic surveillance (March 2020 to April 2022) in the sparsely populated German federal state of Mecklenburg-Western Pomerania (`M-V`, $1.61\text{ million}$ inhabitants), analyzing $3,493$ genomes sequenced by two regional centers (`CoMV-Gen` and `LALLF`) alongside national German (`RKI`) hospitalization and case incidence curves. Using `MAFFT`, `RAxML`, a local `Nextstrain` (`Augur`/`Auspice`) instance, and k-means/median clustering (`KMC`, $k = 10$ via `TMEV 4.9.0`) on monthly relative lineage proportions, the authors trace five epidemic waves across 108 Pangolin lineages (dominated successively by early B.1/B.1.177 lineages, Alpha `B.1.1.7`, Delta `AY.122`/`AY.43`/`AY.4`, and Omicron `BA.1`/`BA.2`). They report that regional epidemic waves in `M-V` lagged national German trends by 1–2 months during 2020–2021, suggest that summer holiday travel drove Delta sublineage introductions, and observe 64 unique lineages among `M-V` residents ($n = 3,144$) versus 10 unique lineages among non-residents ($n = 349$).

**Editorial Verdict: Major Revision (Mixed / Salvageable).** While regional genomic surveillance repositories (`PRJEB59319`) are valuable public health records, this manuscript suffers from substantial methodological omissions, unquantified visual inference, and severe factual/numerical proofreading errors: (1) **the Materials and Methods section omits all wet-lab sequencing and dry-lab bioinformatic assembly details**—reducing the entire experimental and bioinformatic workflow of 4 partner centers to a single sentence referring to *"different kits... different pipelines as described in supplemental material"* (line 29), without stating sequencing platforms, read depth thresholds, or consensus `N`-content quality filters in the main text; (2) **comparing raw lineage richness (`64 vs. 10 unique lineages`) between `M-V` residents ($n = 3,144$) and non-residents ($n = 349$)** (lines 79–80, Fig. 7A) without rarefaction or subsampling ignores a **9-fold difference in sample size**; (3) **claims of a "1 to 2 months delay" and holiday travel / lockdown causality** rely purely on visual inspection of timeline plots without cross-correlation lag estimation, mobility data, or phylodynamic importation modeling; and (4) the text contains glaring factual errors, including stating that global COVID-19 deaths are **"around 6,722,949 million"** ($6.7 \times 10^{12}$!) on line 12, calling clade `21J` an **"Alpha clade 21J"** on line 59 (`21J` is Delta!), and misstating `"December 2021"` for `"December 2020"` on line 71.

### Assessment of Specific Claims
* **Claim 1 (Successive epidemic waves in `M-V` between March 2020 and April 2022 were driven by sequential replacement of ancestral `B.1`/`B.1.177` lineages by Alpha [`B.1.1.7`], diverse Delta sublineages [`AY.122`, `AY.43`, `AY.4`, `B.1.617.2`], and Omicron [`BA.1`, `BA.2`]): [Well Supported].**  
  With $3,493$ sequences spanning the 25-month period (particularly from early 2021 onward), the overall variant replacement succession in Figures 3–5 accurately reflects the regional lineage landscape.
* **Claim 2 (Lineages in `M-V` arrived with a "one to two months delay" compared to national German trends, and summer holiday tourism drove the introduction of diverse Delta lineages): [Fragile].**  
  First, prior to calendar week 4 of 2021, sequencing volume in `M-V` was extremely sparse (only isolated sporadic sequences in 2020, as shown in Fig. 1B and acknowledged on lines 45 and 136). In low-sampling regimes, first-detection dates lag true introduction dates by weeks or months simply due to low detection probability ($p_{\text{detect}} = 1 - (1 - f)^N$). Second, no quantitative cross-correlation function (CCF), importation time-to-most-recent-common-ancestor ($t_{\text{MRCA}}$) phylodynamic analysis, or tourism/mobility time-series regression is performed to test holiday travel causality.
* **Claim 3 (Resident `M-V` samples harbored 64 unique lineages compared to only 10 unique lineages in non-resident samples, showing higher diversity within `M-V` residents): [Methodologically Flawed].**  
  In Results lines 79–80 and Figure 7A, the authors compare the raw count of unique Pangolin lineages detected in $n = 3,144$ sequences from `M-V` residents ($64$ unique + $34$ shared = $98$ lineages) against $n = 349$ sequences from non-residents ($10$ unique + $34$ shared = $44$ lineages). In ecology and population genetics, allelic/lineage richness ($S$) scales sub-linearly with sample size $n$ (especially for rare singleton/doubleton sublineages). Comparing raw richness across a $9\times$ sample size disparity ($3,144$ vs. $349$) without rarefaction (e.g., 1,000 random subsamples of $n = 349$ from the resident pool) is statistically invalid.
* **Claim 4 (K-means/median clustering [`KMC`, $k = 10$] of monthly relative lineage frequencies identifies 10 biologically distinct co-circulating viral clusters): [Moderately Supported].**  
  Clustering time-series profiles by Pearson correlation groups lineages that peaked in the same month (e.g., grouping lineages peaking in late 2020 vs. Spring 2021 vs. Summer/Autumn 2021). However, $k = 10$ was selected *ad hoc* without silhouette width, gap statistic, or elbow validation, and normalizing monthly counts to relative percentages (lines 38, 69) gives noisy singleton detections in low-sequencing months (2020) equal weight to major waves.

---

## 3. Forensic Defect Inventory

1. **Pillar 5 & 7 Violation — Omission of Essential Wet-Lab and Bioinformatic Methods from the Main Text (Methods Lines 25–30):**  
   The entire section `RNA-Extraction, Library Preparation, Sequencing and Whole Genome Reconstruction` (lines 25–30) consists of 5 sentences that provide zero methodological specifics: *"Extracted RNA... was sent to four sequencing centers and processed using different kits for library preparation and sequencing on different platforms as described in the supplemental material. Subsequent assembly of raw data makes use of different pipelines as described in supplemental material."* Neither the sequencing platforms (Illumina vs. ONT vs. Ion Torrent), amplicon primer schemes (`ARTIC` v3 vs. v4, which critically affects Omicron/Delta dropout!), minimum read depth, nor maximum `N`-content quality filters are stated in the manuscript text.
2. **Pillar 2 & 4 Violation — Unrarefied Lineage Richness Comparison Across a 9-Fold Sample Size Disparity ($n = 3,144$ vs. $n = 349$, Lines 79–80 & Fig. 7A):**  
   Observing 64 group-exclusive lineages in $3,144$ resident sequences ($2.0\%$ per sequence) versus 10 group-exclusive lineages in $349$ non-resident sequences ($2.9\%$ per sequence!) actually indicates *slightly higher* per-sample unique lineage yield among non-residents ($10/349 = 2.87\%$ vs. $64/3144 = 2.04\%$). Presenting the raw unrarefied totals (`64 vs. 10`) as evidence of greater lineage diversity in residents is a classic sample-size artifact.
3. **Pillar 2 Violation — Arbitrary K-Means Clustering ($k = 10$) on Unsmoothed Compositional Percentages Without Uncertainty Bounds (Lines 38, 69–76):**  
   In lines 38 and 69, monthly sequence counts were converted into relative percentages ($0\%\text{–}100\%$) and clustered via `KMC` ($k = 10$, Pearson correlation, 1,000 iterations). Because sample sizes in 2020 were tiny (often $<10$ sequences/month), a single sequence produces a massive percentage spike, distorting Pearson correlation distances, and no justification (e.g., silhouette score or BIC) is given for choosing $k = 10$.
4. **Pillar 7 Violation — Severe Factual, Taxonomic, and Chronological Errors in the Text:**  
   * **Order-of-magnitude mortality error (Line 12):** *"leading to a massive global health crisis... with a current death toll of around 6,722,949 million"* (`6,722,949 million` = $6.72 \times 10^{12}$, i.e., $6.7\text{ trillion}$ deaths—800 times the human population of Earth!).
   * **Misclassification of Nextstrain clade `21J` as "Alpha" (Line 59):** *"Noticeably, at the end of May the first Alpha clade 21J case was detected, quickly becoming the dominant clade starting at the end of June 2021"* (`21J` is the main **Delta** clade, not Alpha, which is `20I`!).
   * **Chronological year error (Line 71):** *"Lineage B.1.177 (20E (EU1), cluster 3) is already present in fall 2020 and replaced the lineages of cluster 1 already in December 2021 as did further B.1 lineages of cluster 2... in January 2021"* (`December 2020`, not `December 2021`!).

---

## 4. Quantitative Rubric Scoring

| Rubric Dimension | Score | Max | Forensic Justification |
| :--- | :---: | :---: | :--- |
| **1. Methodological & Statistical Rigor** | **1.5** | **3.5** | Standard Nextstrain visualization of $3,493$ sequences, but lacks formal statistical testing for lag/mobility claims, omits rarefaction for the $9\times$ sample size gap in Fig. 7A, and uses arbitrary $k=10$ KMC clustering on noisy percentages. |
| **2. Claim-to-Evidence Alignment** | **1.4** | **2.5** | Major VOC replacement timelines are well supported, but claims of a 1–2 month regional delay in 2020 are confounded by sparse early sequencing, and travel/lockdown attributions are purely narrative. |
| **3. Data Integrity & Biological/Behavioral Plausibility** | **1.4** | **2.0** | Authentic regional genomic dataset, but marred by egregious proofreading errors (`6,722,949 million` deaths on line 12, calling clade `21J` "Alpha clade 21J" on line 59, and `December 2021` vs. `2020` on line 71). |
| **4. Reproducibility & Data Integrity** | **1.4** | **2.0** | Sequences deposited in ENA (`PRJEB59319`) and GISAID, but all wet-lab sequencing and bioinformatic assembly methods are absent from the main text Methods section. |
| **Total Composite Score** | **5.7** | **10.0** | **Mixed / Salvageable** (Scientific Core Score: **4.3 / 8.0**) |

---

### Constructive and Doable Suggestions for Improvement

1. **Perform Rarefaction (Subsampling) When Comparing Lineage Richness Between `M-V` Residents ($n = 3,144$) and Non-Residents ($n = 349$):**  
   * **WHY:** Raw lineage counts (`64` unique in residents vs. `10` unique in non-residents; lines 79–80, Fig. 7A) are heavily confounded by the 9-fold difference in sample size ($3,144$ vs. $349$).  
   * **WHAT & HOW:** Draw 1,000 random subsamples of size $n = 349$ without replacement from the $3,144$ resident sequences (matched by collection month/quarter) and report the rarefied mean and 95% interval of total and unique lineages compared to the 44 total (10 unique) lineages observed in non-residents.
2. **Summarize Core Sequencing and Bioinformatic QC Metrics in the Main Text Materials and Methods:**  
   * **WHY:** Readers cannot evaluate genome quality or amplicon dropout without knowing the sequencing platforms, primer schemes, and QC cutoffs in the main text (lines 25–30).  
   * **WHAT & HOW:** Add a brief paragraph (or summary table) to the main text specifying the platforms, primer panels (`ARTIC` v3/v4), minimum read depth, and maximum `N`-content threshold used across the four sequencing centers.
3. **Correct Factual, Taxonomic, and Chronological Errors:**  
   * **WHAT & HOW:** Fix `"around 6,722,949 million"` $\to$ `"around 6.7 million (6,722,949)"` on line 12; fix `"Alpha clade 21J"` $\to$ `"Delta clade 21J"` on line 59; and fix `"December 2021"` $\to$ `"December 2020"` on line 71.
