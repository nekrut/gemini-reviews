# Review of PMC11410272 (PMID:39292644)

**Manuscript Title:** A systematic evaluation of the performance and properties of the UK Biobank Polygenic Risk Score (PRS) Release  
**Authors:** Thompson DJ, Wells D, Selzam S, Peneva I, Moore R, Sharp K, Tarran WA, Beard EJ, Riveros-Mckay F, Giner-Delgado C, Palmer D, Seth P, Harrison J, Futema M, Genomics England Research Consortium, McVean G, Plagnol V, Donnelly P, Weale ME.  
**Journal / Preprint:** *PLoS One* (2024; `PMC11410272` / `PMID:39292644` / `10.1371/journal.pone.0307270`)  
**Calibration Study Cohort:** Cohort C — Wild Literature Sample (`C74` | Double-Blinded as `ANON_116`)  
**Overall Score:** **8.0 / 10.0** (Strong / Sound)  
* **Score Breakdown:** Rigor: 2.8/3.5 | Claims: 2.1/2.5 | Biology: 1.7/2.0 | Reproducibility: 1.4/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript evaluates the UK Biobank (UKB) Polygenic Risk Score (PRS) Release across 28 disease traits and 25 quantitative traits, accompanied by an open-source benchmarking pipeline (`ukb-pret`). The authors evaluate a Standard PRS set (trained exclusively on external GWAS summary statistics) and an Enhanced PRS set (trained on external data plus a White British Unrelated UKB training subset) within an independent UKB Testing Subgroup curated to maximize non-European representation ($N = 97,608$ European, $9,542$ South Asian, $9,476$ Sub-Saharan African, and $2,864$ East Asian ancestry individuals). They benchmark predictive performance (odds ratio/hazard ratio per SD, AUC, and standardized linear effects) against 76 published comparator PRSs from the PGS Catalog, compare cumulative incidence against carriers of rare monogenic pathogenic variants (in *APOB*, *APOE*, *LDLR*, *PCSK9* for familial hypercholesterolemia and *BRCA1/2*, *PALB2*, *ATM*, *CHEK2* for breast cancer), quantify age- and sex-specific effect differences, model all-cause mortality, and externally validate 12 disease PRSs in 39,947 whole-genome sequenced individuals from the 100,000 Genomes Project (100KGP). The evaluation software (`https://github.com/Genomicsplc/ukb-pret`) and UKB GWAS training summary statistics (`doi:10.5281/zenodo.7034289`) are publicly available.

The study is well-designed, adheres to PRS-RS reporting standards, and provides a valuable standardized evaluation framework that prevents phenotype-definition and sample-overlap confounding in UKB. The primary limitations are: (1) the proprietary, closed-source nature of the PRS generation methodology and variant weights, which prevents independent researchers from auditing the underlying algorithms or applying them outside UKB and 100KGP; (2) the confounding of algorithmic comparisons against the 76 published PRSs by larger GWAS training sample sizes in the UKB Release; (3) reliance on unadjusted nominal significance ($p < 0.05$) across dozens of parallel hypothesis tests for age, sex, and comparator differences, alongside stepwise variable selection for the multi-PRS mortality model; and (4) combining retrospective prevalent cases with prospective incident cases in lifetime cumulative incidence curves. These analytical and framing points can be addressed through computational re-analysis and textual clarification without generating new data.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **The UKB Standard and Enhanced PRS sets outperform 76 published comparator PRSs across almost all evaluated traits and ancestries: [Well Supported].**  
  Using a strictly held-out UKB Testing Subgroup and standardized phenotype definitions, the Enhanced PRS achieves higher OR per SD than published comparators for 27 of 28 diseases (significant at $p < 0.05$ via 5,000 bootstraps for 26 diseases) and all quantitative traits, with the Standard PRS showing similar gains (Fig 4, S6 Fig, S5 Table). However, as shown in S7 Fig, the UKB PRS Release generally leveraged larger effective GWAS training sample sizes than the published comparators; thus, the benchmark demonstrates the superiority of the released *scores* rather than isolating the contribution of the proprietary PRS *methodology* at matched training sample sizes.

* **Predictive performance generalizes to an external whole-genome sequenced cohort (100,000 Genomes Project) without UKB-specific overfitting, while exhibiting expected cross-ancestry attenuation: [Well Supported].**  
  In 35,123 European-ancestry 100KGP participants free of rare genetic disorders, log OR per SD correlates strongly with UKB Testing Subgroup estimates ($r = 0.957$ for Enhanced, $r = 0.974$ for Standard across 12 diseases; Fig 9). Across ancestries in UKB, disease OR per SD declines by an average of $9.4\%$ in South Asian, $14.0\%$ in East Asian, and $27.5\%$ in African ancestry groups relative to European ancestry (Fig 3), while differences in baseline prevalence (e.g., type 2 diabetes in South Asian ancestry; Fig 5) can still yield large absolute risk stratification.

* **High-PRS individuals exhibit average cumulative disease risk comparable to rare monogenic mutation carriers while accounting for 18–29 times more CAD events: [Moderately Supported].**  
  The comparison of Enhanced CAD PRS (top $19\%$ overall, or top $8\%$ among statin-free primary-care-linked participants) with whole-exome-sequenced FH variant carriers ($0.35\%$ overall, $0.22\%$ statin-free) and Enhanced breast cancer PRS (top $0.3\%$) with *BRCA1/2* carriers clearly illustrates the population burden of polygenic risk (Fig 6, S8 Fig). Two methodological caveats temper the exact equivalence percentiles: first, cumulative incidence curves spanning ages 0 to 70 in a cohort recruited at ages 40–69 pool retrospective prevalent diagnoses (which are subject to survival bias prior to enrollment) with prospective incident diagnoses; second, conditioning on the absence of pre-CAD statin prescriptions (Fig 6B) conditions on a clinical decision influenced by baseline lipid levels, which may differentially select lower-penetrance FH carriers.

* **PRS effect sizes decline with age across 9 of 22 diseases and differ by sex across 6 diseases and 9 quantitative traits: [Fragile].**  
  In Fig 7 (comparing 10-year incident log HR per SD between ages 40–49 and 60–69 across 22 diseases) and Fig 8 (comparing sex-specific effects across 53 traits), significance is declared at a nominal two-tailed $\alpha = 0.05$ without multiple-testing correction. Under 53 independent tests in Fig 8, ~2.65 false positives are expected by chance alone, and several single-asterisk effects ($0.01 \le p < 0.05$) may not survive Benjamini–Hochberg FDR control.

* **Multi-PRS stepwise regression improves all-cause mortality prediction in participants and their parents: [Moderately Supported].**  
  While the 2:1 offspring-to-parent log hazard ratio relationship (S13 Fig) is biologically consistent with Mendelian transmission, using bidirectional/stepwise selection across 53 correlated PRSs is known to produce unstable predictor subsets and inflated nominal significance, and the incremental discrimination ($\Delta\text{Harrell's } C = 0.0043$, Royston's $R^2 = 1.5\%$) confirms the authors' own conclusion that the multi-PRS mortality model offers limited standalone clinical discrimination.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Apply Formal Multiple-Testing Corrections Across Multi-Trait Scans
* **WHY:** The manuscript applies multiple-testing correction when evaluating whether South Asian performance exceeds European performance (page 6, line 62), but relies on unadjusted nominal $p < 0.05$ thresholds when reporting Enhanced vs. Standard comparisons (37 traits), comparator benchmarks (76 PRSs), age-stratified hazard ratios (22 diseases, Fig 7), sex-stratified effects (53 traits, Fig 8), and 100KGP validation differences (12 diseases, Fig 9).
* **WHAT:** Report Benjamini–Hochberg false discovery rate ($q$-values) alongside nominal $p$-values for all multi-trait scans in Figs 4, 7, 8, and 9 and Supporting Tables S2–S8.
* **HOW:** Apply `p.adjust(p_values, method = "BH")` across the tested traits within each family of hypotheses and indicate in the captions of Figs 4, 7, and 8 which comparisons remain significant at $\text{FDR} < 0.05$.

#### 2. Decouple Algorithmic Methodology from GWAS Sample Size in Comparator Benchmarks
* **WHY:** Because the Enhanced and Standard PRSs generally use larger GWAS discovery sample sizes than the 76 PGS Catalog comparators (S7 Fig), readers may conflate the predictive advantage of larger training data with the performance of the proprietary PRS algorithm.
* **WHAT:** Quantify the performance gain attributable to the PRS methodology when training sample size is matched or controlled.
* **HOW:** Using the data already plotted in S7 Fig and S5/S6 Tables, fit a meta-regression of $\Delta\log\text{OR}$ (Standard PRS minus best comparator PRS) on $\log(N_{\text{eff, Standard}} / N_{\text{eff, Comparator}})$, and explicitly highlight the subset of traits (indicated by dashed lines in S7 Fig) where the Standard PRS outperforms a comparator despite having an equal or *smaller* effective training sample size.

#### 3. Separate Prospective Incident Events from Prevalent Diagnoses in Cumulative Incidence Curves
* **WHY:** Estimating cumulative incidence from birth to age 70 (Figs 2, 5, 6) in UKB participants recruited at ages 40–69 treats retrospective diagnoses prior to baseline assessment as equivalent to prospective follow-up, which can be distorted by survival bias (e.g., lethal early-onset CAD or cancer cases missing from recruitment) and changing diagnostic/prescribing practices over calendar time.
* **WHAT:** Provide a sensitivity analysis restricting cumulative incidence (specifically for the FH and *BRCA1/2* equivalence comparisons in Fig 6 and S8 Fig) to prospective incident events using age as the time scale with left-truncation at age of UKB assessment.
* **HOW:** Re-estimate the Kaplan–Meier / Aalen–Johansen cumulative incidence curves in `ukb-pret` using delayed entry (`Surv(age_at_recruitment, age_at_event_or_censoring, event)`) among individuals disease-free at baseline, and compare the resulting PRS-to-carrier equivalence percentiles against the full-lifecourse curves.

#### 4. Replace Stepwise Selection with Penalized Cox Regression for Multi-PRS Mortality Modeling
* **WHY:** Stepwise regression across 53 traits (some with pairwise correlations up to $r = 0.99$, such as phosphatidylcholines and phosphoglycerides, or $r = 0.80$ for CAD and CVD) suffers from collinearity instability and selection bias.
* **WHAT:** Validate the multi-PRS mortality model using $L_1$/$L_2$-penalized Cox regression (elastic net) in the White British Unrelated training set.
* **HOW:** Fit a cross-validated Cox elastic net (`glmnet` with `family = "cox"`) on the WBU training cohort using all Standard PRSs, evaluate Harrell's $C$ and Royston's $R^2$ in the held-out UKB Testing Subgroup, and verify that the 2:1 offspring-to-parent hazard ratio slope in S13 Fig is preserved.

#### 5. Technical, Mathematical, and Editorial Cleanup
* **WHY:** Minor terminology inconsistencies between "Enhanced" and "Extended" PRS sets appear in the text and figure captions.
* **WHAT & HOW:**
  1. **Fig 8 Caption (line 120) and Results (line 136):** Replace *"Extended PRS set"* with *"Enhanced PRS set"* to maintain consistent terminology throughout the manuscript.
  2. **Supporting Information / Supplementary Materials (lines 9–35 and 54–81):** The supplementary figure descriptions are duplicated verbatim twice at the end of the manuscript; remove the duplicate block and prefix each paragraph with its corresponding label (`S1 Fig` through `S13 Fig`).
