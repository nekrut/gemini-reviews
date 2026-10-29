# Review of FEXP_ANON_051

**Overall Score:** **6.3 / 10.0** (Mixed / Salvageable) | **Scientific Core Score:** **4.5 / 8.0**  
* **Score Breakdown:** Rigor: 1.8/3.5 | Claims: 1.3/2.5 | Biology: 1.4/2.0 | Reproducibility: 1.8/2.0

---

## 1. Blinded Metadata Perception

* **Perceived Field & Subfield:** Cancer Genomics & Epigenomics / Computational Microbiome-Immunome Integration in Early-Onset Colorectal Cancer (EOCRC)
* **Study Design:** Retrospective multi-cohort bioinformatic study comparing DNA methylation (HM450), epigenetic clock age acceleration, bulk tumor RNA-seq differential expression, RNA-seq-derived intratumoral microbes (`{exotic}`), and CIBERSORTx immune deconvolution between microsatellite-stable EOCRC (age $< 50$) and average-onset colorectal cancer (AOCRC, age $\ge 50$).
* **Model System & Sample Size:** Human colorectal cancer tumors from TCGA ($N = 358$: 54 EOCRC, 304 [or 303 in Table 1] AOCRC) and the Oncology Research Information Exchange Network (ORIEN; $N = 453$: 120 EOCRC, 333 AOCRC), plus 16S rRNA validation on 60 overlapping tumor/normal samples.
* **Perceived Methodological Maturity:** High data transparency and commendable null reporting on intratumoral microbe abundance, but the two headline positive findings—12.4-year epigenetic age acceleration in EOCRC and stronger microbe–immune correlations in EOCRC—suffer from severe statistical artifacts (regression-to-the-mean truncation bias in $\Delta = \text{DNAmAge} - \text{Age}$ and sample-size variance inflation in Spearman's $\rho$ for smaller cohorts).

---

## 2. Executive Summary & Editorial Verdict

This study investigates epigenetic, transcriptional, microbial, and immunological differences between microsatellite-stable early-onset colorectal cancer (EOCRC, diagnosis age $< 50$) and average-onset colorectal cancer (AOCRC, diagnosis age $\ge 50$) across TCGA ($N = 358$: 54 EOCRC, 304 AOCRC) and ORIEN ($N = 453$: 120 EOCRC, 333 AOCRC), supplemented by 16S rRNA amplicon sequencing on 60 samples (BioProject `PRJNA856973`; code at `[GITHUB_REPO_REDACTED]`). Using Illumina HM450 methylation arrays in TCGA, the authors identify 937 hypomethylated and 12 hypermethylated genes in EOCRC ($|\Delta \beta| \ge 0.1$, FDR $P < 0.05$) and evaluate three epigenetic clocks (Horvath, Hannum, PhenoAge), reporting that mean DNAm age acceleration ($\Delta = \text{DNAmAge} - \text{chronologic age}$) is 12.4 years higher in EOCRC than in AOCRC. Integrating differential methylation with bulk RNA-seq via Ingenuity Pathway Analysis (IPA) highlights four overlapping pathways (CREB signaling in neurons, GPCR signaling, phagosome formation, and S100 family signaling). Using the `{exotic}` pipeline to quantify nonhuman RNA-seq reads, the authors find no consistent microbial taxa enriched in EOCRC across TCGA, ORIEN, and 16S datasets, but report stronger positive Spearman correlations between microbial genera and CIBERSORTx-deconvolved immune cells (such as activated mast cells and neutrophils) in EOCRC than in AOCRC.

**Editorial Verdict: Major Revision (Mixed / Salvageable).** The authors deserve credit for transparent data/code sharing, rigorous contamination checks pairing `{exotic}` RNA-seq microbial calls against 16S amplicon data and negative controls, and forthrightly reporting the null result that no intratumoral microbe (including *Fusobacterium*) is enriched in EOCRC. However, both of the manuscript's primary positive conclusions rest on unaddressed statistical artifacts:
1. **Epigenetic Age Difference ($\Delta = \text{DNAmAge} - \text{Age}$) Regression Dilution Artifact:** When a cohort is dichotomized strictly by chronological age ($< 50$ vs. $\ge 50$), comparing the raw difference $\Delta = \text{DNAmAge} - \text{Age}$ without normal age-matched colonic mucosa controls is mathematically biased whenever the slope of tumor $\text{DNAmAge}$ on chronological age is less than 1 ($\beta < 1$). Indeed, in Figure 1D, Horvath's clock predicts $\Delta_{\text{AOCRC}} = -14.2$ years (severe apparent *deceleration* in older tumors) versus $\Delta_{\text{EOCRC}} = +2.1$ years, while PhenoAge shows no statistically significant difference ($P = 0.17$). Averaging the three clocks to claim a "12-year older" epigenetic age acceleration in EOCRC conflates regression-to-the-mean in dysregulated tumor methylomes with true biological aging.
2. **Sample-Size Bias in Comparing Correlation Magnitudes:** In both TCGA ($n = 54$ vs. $n = 304$) and ORIEN ($n = 120$ vs. $n = 333$), the EOCRC group is 2.8- to 5.6-fold smaller than the AOCRC group. Because the sampling variance of Spearman's $\rho$ scales as $\sim 1/(n - 1)$, a smaller cohort automatically exhibits a much wider dispersion of sample correlation coefficients, producing "more and larger positive correlations" by finite-sample variance alone unless formally tested via Fisher's $z$-transformation or equal-sized subsampling.
In addition, the transcriptomic pathway validation relies on unadjusted $P < 0.05$ cutoffs, and 28% (127/453) of ORIEN samples are metastatic biopsies (liver, lung, peritoneum, ovary) rather than primary colorectal tumors. All of these issues can be resolved computationally using the authors' existing datasets.

### Specific Conclusions and Assessment of Support

* **Intratumoral microbial abundances do not consistently differ between EOCRC and AOCRC across TCGA, ORIEN, and 16S datasets: [Well Supported].**  
  Figure 3D–I and Supplementary Figures S1–S2 demonstrate across three datasets (and validated against paired 16S sequencing and negative controls in Figure 3B) that neither *Fusobacterium* nor any other bacterial/viral genus is reproducibly enriched in EOCRC. This is a rigorous and valuable negative finding for the field.

* **EOCRC tumors exhibit 12.4 years greater epigenetic age acceleration than AOCRC tumors across three epigenetic clocks: [Methodologically Flawed].**  
  Because EOCRC and AOCRC are defined by chronological age ($< 50$ vs. $\ge 50$), any compression of tumor DNAmAge toward the mean ($\text{slope } \beta < 1$ between tumor DNAmAge and patient chronological age) mechanically forces $\Delta = \text{DNAmAge} - \text{Age} = \alpha + (\beta - 1)\text{Age}$ to be higher in younger patients and negative in older patients (as seen in Horvath $\Delta_{\text{AOCRC}} = -14.2$ years). Moreover, PhenoAge is non-significant ($P = 0.17$), making the unweighted three-clock average of 12.4 years statistically invalid.

* **Intratumoral microbes interact more strongly with immune cells in EOCRC than in AOCRC, characterized by more and larger positive correlations: [Methodologically Flawed].**  
  Comparing raw Spearman correlation magnitudes ($\rho$) and counts of significant correlations between a small cohort (EOCRC: $n = 54$ in TCGA, $n = 120$ in ORIEN) and a much larger cohort (AOCRC: $n = 304$ in TCGA, $n = 333$ in ORIEN) without downsampling or two-sample Fisher $z$-tests is confounded by finite-sample variance ($\text{SE}(\rho) \approx 1/\sqrt{n-1}$ is $2.4\times$ larger in TCGA EOCRC than AOCRC, inflating extreme $|\rho|$ values).

* **Hypomethylation in EOCRC activates transcriptional programs in CREB, GPCR, phagosome formation, and S100 family signaling pathways: [Fragile].**  
  While the HM450 differential methylation analysis uses Benjamini–Hochberg FDR $< 0.05$, the authors note on line 149 that the RNA-seq differential expression input to IPA used *unadjusted* $P < 0.05$, and the comparisons were not adjusted for tumor stage (significantly more Stage III/IV in EOCRC; Tables 1–2), primary sidedness ($P = 0.008$ in ORIEN), or metastatic biopsy site (28% of ORIEN samples).

---

## 3. Forensic Defect Inventory

### 1. Age-Truncation and Regression-to-the-Mean Bias in Epigenetic Clock Acceleration ($\Delta$) (Pillars 3, 4, 5)
* **Defect:** The authors compute $\Delta = \text{DNAmAge} - \text{Chronological Age}$ in tumor tissue and compare $\Delta_{\text{EOCRC}}$ ($\text{Age} < 50$) against $\Delta_{\text{AOCRC}}$ ($\text{Age} \ge 50$) via two-sample tests (Figure 1D), then average $\Delta$ across Horvath ($P = 7.89 \times 10^{-12}$), Hannum ($P = 1.48 \times 10^{-8}$), and PhenoAge ($P = 0.17$) to claim a 12.4-year acceleration.
* **WHY:** In solid tumors, extensive somatic CpG island hypermethylation and global hypomethylation decouple clock CpGs from chronological age, flattening the regression slope $\beta$ of $\text{DNAmAge}$ on $\text{Age}$ ($\beta < 1$). Consequently, $\text{E}[\Delta \mid \text{Age}] = \alpha + (\beta - 1)\text{Age}$ is a decreasing linear function of chronological age. Truncating the cohort at age 50 guarantees $\bar{\Delta}_{\text{Age}<50} > \bar{\Delta}_{\text{Age}\ge 50}$ even if tumor methylation is completely independent of patient age! This is directly evidenced by Horvath's clock yielding $\Delta_{\text{AOCRC}} = -14.2$ years (implying AOCRC tumors are 14 years *younger* than the patient's chronological age).
* **WHAT:** Plot raw $\text{DNAmAge}$ against chronological age across all 358 TCGA tumors and matched normal adjacent colon tissues (`TCGA-COAD`/`READ` normal samples), estimate the normal-tissue aging slope, and test whether EOCRC tumors deviate further from *age-matched normal colon mucosa* than AOCRC tumors do.
* **HOW:** Download the matched TCGA normal colon/rectum HM450 samples via `TCGAbiolinks`, fit a linear regression $\text{DNAmAge} \sim \text{Chronological Age}$ on normal mucosa to define normal colonic epigenetic aging, compute residual age acceleration relative to normal mucosa, and report each clock separately rather than averaging significant and non-significant ($P = 0.17$) clocks.

### 2. Sample-Size Variance Inflation in Microbe–Immune Correlation Comparisons (Pillars 3, 4, 5)
* **Defect:** In Figure 4, the authors conclude that EOCRC has stronger microbe–immune interactions because the distribution of Spearman's $\rho$ values in EOCRC ($n = 54$ TCGA; $n = 120$ ORIEN) has more extreme positive values than in AOCRC ($n = 304$ TCGA; $n = 333$ ORIEN).
* **WHY:** For any pair of weakly correlated or uncorrelated variables, the standard error of Spearman's $\rho$ is approximately $1/\sqrt{n - 1}$. In TCGA, $\text{SE}(\rho) \approx 0.137$ in EOCRC ($n = 54$) versus $0.057$ in AOCRC ($n = 304$). Thus, a sample correlation of $\rho = 0.30$ is only $2.2\,\text{SD}$ in EOCRC but $5.2\,\text{SD}$ in AOCRC. Plotting raw correlation magnitudes without accounting for the 5.6-fold difference in $n$ guarantees that the smaller group displays a wider spread of larger $|\rho|$ values purely from sampling noise.
* **WHAT:** Perform formal two-sample hypothesis tests for differences in correlation coefficients ($\rho_{\text{EOCRC}} - \rho_{\text{AOCRC}}$) and conduct sample-size-matched bootstrap downsampling of AOCRC.
* **HOW:** (a) Randomly subsample $n = 54$ AOCRC tumors in TCGA and $n = 120$ AOCRC tumors in ORIEN across 1,000 permutations to compare the distribution of $\rho$ at identical sample sizes. (b) For each microbe–immune pair, compute Fisher's $z$-test statistic $z = [\text{atanh}(\rho_{\text{EOCRC}}) - \text{atanh}(\rho_{\text{AOCRC}})] / \sqrt{1/(n_{\text{EOCRC}}-3) + 1/(n_{\text{AOCRC}}-3)}$ and adjust the resulting $P$-values via Benjamini–Hochberg FDR.

### 3. Unadjusted Transcriptomic P-Values and Uncontrolled Confounding by Metastatic Site and Stage (Pillars 2, 3, 4)
* **Defect:** (a) Line 149 states that differential gene expression input to IPA used unadjusted $P < 0.05$ (`|Fold change| > 1.5`). (b) Line 188 reveals that 127 of 453 ORIEN samples (28%) were biopsies from metastatic sites (liver, lung, pelvis, peritoneum, ovary) rather than primary colorectal tissue, and Tables 1–2 show significant differences in tumor stage ($P = 0.046$ and $P = 0.018$) and left/right sidedness ($P = 0.008$) between EOCRC and AOCRC.
* **WHY:** Hepatic, pulmonary, and peritoneal metastases contain contaminating host parenchyma (hepatocytes, pneumocytes, mesothelium) and distinct resident immune populations (e.g., Kupffer cells, alveolar macrophages) that severely confound bulk RNA-seq DEG analysis, CIBERSORTx immune deconvolution, and intratumoral microbiome profiles.
* **WHAT:** Restrict the primary ORIEN transcriptomic, CIBERSORTx, and `{exotic}` analyses to primary colorectal resection specimens ($n = 326$)—evaluating metastatic biopsies in a separate stratified sensitivity analysis—and include AJCC stage and primary tumor location (left vs. right) as covariates in `limma/voom` and `TCGAbiolinks` linear models with Benjamini–Hochberg FDR correction.
* **HOW:** Update the `limma/voom` design matrix to `~ age_group + stage + tumor_location` on primary tumor samples only, apply FDR $< 0.05$ for DEGs, and regenerate Figures 2C–E and 4.

### 4. Sample Count Discrepancy in Table 1 (Pillar 7)
* **Defect:** The Abstract, Methods (line 28), and Results (line 59) state that the TCGA cohort comprises 358 cases (54 EOCRC and 304 AOCRC), whereas Table 1 (line 65) lists $N = 54$ EOCRC and $N = 303$ AOCRC (total $N = 357$).
* **WHY:** Numerical inconsistencies between main text and summary tables obscure the exact denominator used in statistical tests.
* **WHAT & HOW:** Reconcile whether 303 or 304 AOCRC patients were included in Table 1 and update the text and table to match exactly.

---

## 4. Quantitative Rubric Scoring

| Rubric Dimension | Score | Max | Forensic Justification |
| :--- | :---: | :---: | :--- |
| **1. Methodological & Statistical Rigor** | **1.8** | **3.5** | Rigorous 16S and negative-control validation of `{exotic}` microbial calls, but the two main positive claims suffer from unaddressed age-truncation bias in $\Delta = \text{DNAmAge} - \text{Age}$ and sample-size variance inflation ($n=54$ vs $n=304$) in Spearman's $\rho$; DEG pathway analysis used unadjusted $P$-values. |
| **2. Claim-to-Evidence Alignment** | **1.3** | **2.5** | Commendably transparent reporting of the null microbiome abundance result, but overstates epigenetic age acceleration (averaging across a non-significant PhenoAge clock, $P=0.17$) and microbe–immune correlation differences without formal two-sample correlation testing. |
| **3. Data Integrity & Biological Plausibility** | **1.4** | **2.0** | Inclusion of 127/453 (28%) metastatic organ biopsies (liver, lung, peritoneum) in ORIEN alongside primary colon tumors without stratification confounds bulk RNA-seq expression and CIBERSORTx immune deconvolution. |
| **4. Reproducibility & Data Integrity** | **1.8** | **2.0** | Exemplary open science: raw/processed data deposited under BioProject `PRJNA856973` and full analysis scripts provided on GitHub (`spakowiczlab/exorien-exogieo`). Minor $N = 303$ vs. $304$ discrepancy in Table 1. |
| **Scientific Core Score** | **4.5** | **8.0** | Sum of Rigor (1.8) + Claims (1.3) + Biology (1.4). |
| **Overall Composite Score** | **6.3** | **10.0** | **Mixed / Salvageable Tier** (Sum of all four dimensions). |
