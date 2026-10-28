# Forensic Scientific Peer Review: `ANON_162`

**Overall Score:** **4.3 / 10.0** (Flawed / Overstated)
* **Score Breakdown:** Rigor: 1.1/3.5 | Claims: 1.0/2.5 | Biology: 1.3/2.0 | Reproducibility: 0.9/2.0

---

## 1. Executive Summary & Synthesis

This cross-sectional retrospective cohort study analyzes 302 SARS-CoV-2 clinical nasopharyngeal specimens collected at the Cleveland Clinic during the initial six weeks of the pandemic (March 11 to April 22, 2020) using amplicon-based next-generation sequencing (Swift Normalase SNAP panel) to evaluate associations between GISAID viral clades (specifically the Spike D614G / 23403A>G substitution separating Clade group 1 [S, V, L, O] from Clade group 2 [G, GH, GR]) and clinical outcomes (hospitalization, ICU admission, laboratory abnormalities, and mortality). The authors report 487 single-nucleotide variants (including 152 previously unreported rare variants), observe a temporal sweep of D614G-bearing Clade group 2 strains, and conclude from multivariable logistic regression that Clade group 1 (lacking D614G) is independently associated with markedly higher mortality ($\text{OR} = 22.4$) and higher serum creatinine in Clade V infections.

While the sequencing effort and clinical chart review from the early pandemic period represent useful observational data, the statistical analysis and quantitative reporting suffer from severe errors that invalidate the primary clinical associations:
1. **Conflicting and Mathematically Impossible Confidence Intervals:** In the Abstract (line 31) and Results (line 171), the primary mortality association for Clade group 1 is reported as `OR, 22.4; 95% CI, 0.6 to 5.6; P = .01`. A point estimate of `22.4` cannot lie outside its own 95% confidence interval (`0.6 to 5.6`), nor can an odds ratio CI spanning `1.0` yield `P = .01`. Cross-checking against Table 3 (line 196), where the 95% CI is reported as `1.9-269.9`, reveals that the authors accidentally reported the natural log-odds bounds ($\ln(1.9) \approx 0.64$, $\ln(269.9) \approx 5.60$) as the odds ratio confidence interval in both the Abstract and main text.
2. **Impossible Negative Interquartile Range for Serum Creatinine:** In the Abstract (line 31) and Results (line 163), serum creatinine in Clade V patients is reported as `median [interquartile range], 2.6 [−0.4 to 5.5] mg/dL`. Because serum creatinine concentration is strictly positive, the 25th percentile cannot be `-0.4 mg/dL`; the authors evidently subtracted a spread statistic (e.g., $\text{median} \pm \text{IQR}$ or $\text{mean} \pm \text{SD}$) rather than reporting actual quartile bounds.
3. **Severe Small-Sample Overfitting and Stepwise Selection Bias:** Mortality regression was restricted to hospitalized patients ($n = 91$, with only $17$ total deaths) and further split 80%/20% into training (~73 patients, ~13–14 deaths) and testing sets. Fitting iterative backward stepwise elimination across dozens of imputed binary lab variables, comorbidities, demographics, and clade indicators on ~13–14 events violates minimum events-per-variable requirements by an order of magnitude and causes quasi-complete separation ($\text{OR} = 22.4$, 95% CI `1.9–269.9`; $\text{OR} = 0.01$ for Spike variants).
4. **Uncontrolled Temporal Ascertainment Confounding and Table Arithmetic Errors:** Early Clade group 1 cases were ascertained when testing was restricted to older, hospitalized non-employees (median age 62.2 years; 23.4% healthcare workers), whereas later Clade group 2 cases included routine employee screening (median age 50.5 years; 45.9% healthcare workers, $P = .004$). Furthermore, Table 1 and Table 2 contain multiple row and column summation errors.

---

## 2. Claim-by-Claim Evaluation

* **Claim 1 (Abstract, line 31; Results, line 171): "In multivariable regression analyses, infection by paths lacking the 23403A>G (D614G) variant [Clade group 1] showed higher rates of mortality when controlling for patient demographics, comorbidities, and physiological parameters (OR, 22.4; 95% CI, 0.6 to 5.6; P = .01)."** — `[Methodologically Flawed]`
  * **Evidence & Audit:** First, the reported 95% CI (`0.6 to 5.6`) in the Abstract and Results is a transcription of the log-odds interval `[0.64, 5.60]` corresponding to the exponentiated interval `1.9–269.9` in Table 3 (line 196). Second, the multivariable model was fit on an 80% training split of 91 hospitalized patients containing only ~13–14 deaths total (5 deaths in Clade group 1 and 12 deaths in Clade group 2 across the entire cohort; Table 1, line 127) using iterative backward stepwise p-value filtering across dozens of candidate variables followed by manually re-inserting eliminated viral predictors (Methods, line 78). An odds ratio of `22.4` spanning two orders of magnitude (`1.9–269.9`) on ~13 events is an artifact of small-sample sparse-data bias and stepwise overfitting.
* **Claim 2 (Abstract, line 31; Results, line 163): "Notable differences included higher levels of serum creatinine individually vs all other clades in infection by clade V (median [interquartile range], 2.6 [−0.4 to 5.5] mg/dL vs 0.9 [0.6 to 1.2] mg/dL; P = .008)."** — `[Methodologically Flawed]`
  * **Evidence & Audit:** A blood analyte concentration cannot have a negative 25th percentile (`-0.4 mg/dL`). Moreover, the entire cohort contained only $n = 11$ Clade V patients (line 146), and laboratory tests were only ordered for subsets of hospitalized patients (in Methods, line 78, missing labs had to be imputed with "normal value" categories for regression). Nor was any multiple-testing correction applied across the 6 clades $\times$ multiple laboratory parameters tested via pairwise Mann-Whitney $U$ tests.
* **Claim 3 (Results, line 88; Figure 2A): "The unadjusted survival rate of patients inside clade group 2 was significantly higher compared with those within clade group 1 (log-rank P < .001; Figure 2A)."** — `[Overstated]`
  * **Evidence & Audit:** As documented in Table 1 (lines 94–106), Clade group 1 ($n = 64$) and Clade group 2 ($n = 238$) were sampled from entirely different patient populations due to shifting institutional testing criteria over the 6-week period (Results, line 159; Discussion, line 235): Clade group 1 patients were 11.7 years older on average (median age 62.2 vs. 50.5 years, $P = .01$) and half as likely to be healthcare workers screened via occupational health (23.4% vs. 45.9%, $P = .004$). Presenting an unadjusted Kaplan-Meier log-rank test without age or occupational stratification conflates institutional testing expansion with viral virulence.
* **Claim 4 (Results, lines 129–139; Figure 4): "For the first 2 weeks after we started testing, most strains mapped to dynamic lineages bearing the wild-type D614 variant... However, during the ensuing weeks, prevalence of the 614G variant steadily increased... persisted at nearly 90% of the total isolates in the final week recorded."** — `[Well Supported]`
  * **Evidence & Audit:** The temporal transition from ancestral D614 lineages (A / B.2 / B.4) to D614G-bearing B.1 lineages across March–April 2020 is clearly supported by the longitudinal sequencing counts across the 6 weeks (Figure 4A–B), even accounting for the $C_T \le 30$ selection threshold.
* **Claim 5 (Results, line 179; Table 3): "Variants in the S protein were associated with improved survival despite persistence in circulation (OR, 0.01; 95% CI, 0 to 0.7; P = .03)."** — `[Methodologically Flawed]`
  * **Evidence & Audit:** In Table 3 (Model 2, line 206), "Variation in structural and nonstructural coding regions: S" has `OR = 0.01 (0.0-0.7), P = .03`. An odds ratio of `0.01` (a 99% reduction in odds of death) with a lower confidence bound of `0.0` in a sample with 17 total deaths is a classic manifestation of quasi-complete separation in small-sample logistic regression.

---

## 3. Technical & Methodological Critique

### 3.1 Arithmetic and Tabular Inconsistencies in Tables 1 and 2
A forensic audit of the summary tables reveals multiple arithmetic discrepancies where subgroup counts fail to sum to the stated totals:
* **Table 1 Race Counts (lines 99–102):**
  * For the column `All (N = 302)`, the reported race counts are `White: 195`, `Black: 67`, `Multiracial or Hispanic: 8`, `Other: 14`. These sum to $195 + 67 + 8 + 14 = 284$, leaving 18 patients unaccounted for without any footnote indicating missing race data.
  * Worse, comparing the `All` column against the sum of `Clade group 1 (n = 64)` and `Clade group 2 (n = 238)`:
    * `Multiracial or Hispanic`: Clade group 1 has `4 (6.3%)` and Clade group 2 has `12 (5.0%)`. Their sum is $4 + 12 = 16$, yet the `All` column reports `8 (2.6%)`!
    * `Other`: Clade group 1 has `2 (3.1%)` and Clade group 2 has `22 (9.2%)`. Their sum is $2 + 22 = 24$, yet the `All` column reports `14 (4.6%)`!
    * Notice that $(16 - 8) + (24 - 14) = 8 + 10 = 18$, which is the exact number of "missing" patients in the `All` column ($302 - 284 = 18$). Thus, the `All` column was computed from an outdated or corrupted tally.
* **Table 2 Hospitalization and ICU Counts (lines 143–154):**
  * The column headers (line 143) state: `All (N = 91)`, `ICU (n = 35)`, `No ICU (n = 56)` ($35 + 56 = 91$).
  * However, in the bottom row (`All, No. (%)`, line 154), the totals are reported as `All: 91 (30.1)`, `ICU: 35 (38.5)`, `No ICU: 58 (63.7)` ($35 + 58 = 93 \ne 91$, and $38.5\% + 63.7\% = 102.2\%$).
  * The source of this 2-patient error is the `GH` clade row (line 150), which lists `All: 56`, `ICU: 22 (39.3)`, `No ICU: 36 (64.3)`. Here, $22 + 36 = 58 \ne 56$ (and $39.3\% + 64.3\% = 103.6\%$).

### 3.2 Flawed Stepwise Regression and Imputation Pipeline
In Methods ("Statistical Analysis", line 78), the authors describe their multivariable modeling procedure:
1. Only hospitalized patients ($n = 91$) were included because laboratory tests were unavailable for outpatients.
2. Continuous laboratory variables were dichotomized at arbitrary thresholds, and missing values were imputed as a `"normal value"` category. Treating "test not ordered by clinician" as "normal value" introduces clinical indication bias.
3. The 91 hospitalized patients were split 80% (~73 patients, ~13–14 deaths) for training and 20% (~18 patients, ~3–4 deaths) for testing.
4. Dozens of variables were entered simultaneously, and variables were iteratively eliminated one by one based on the largest Wald $p$-value until all remaining variables had $p < 0.05$. If viral clade/variant variables were eliminated during backward selection, they were manually forced back into the reduced model!
This pipeline violates basic principles of biostatistical modeling: backward elimination followed by forcing the predictor of interest back into a model overfit on ~13 events invalidates all resulting nominal $p$-values and confidence intervals, while evaluating ROC-AUC on a 20% holdout containing ~3 deaths provides virtually zero statistical power.

### 3.3 Viral Load Selection Bias ($C_T \le 30$)
Out of 1,750 positive specimens during the study window, 302 (17.3%) were sequenced by selecting specimens with $C_T \le 30$ (and preferentially $C_T \le 26$; Methods, line 54). Because Clade group 2 (carrying D614G) is associated with higher upper-respiratory viral loads (lower $C_T$; Table 1 shows median $C_T$ of 21.0 in Clade group 2 vs. 23.0 in Clade group 1, $P < .001$), restricting inclusion to $C_T \le 30$ differentially samples the two clade groups at different stages of clinical presentation (e.g., capturing mild/asymptomatic healthcare workers in Clade group 2 whose high viral loads met the $C_T$ cutoff, while only capturing severe early-stage patients in Clade group 1).

### 3.4 Data and Code Availability
Despite reporting 302 full-length SARS-CoV-2 clinical genomes and 152 novel variants, the manuscript provides no GISAID EPI_ISL accession numbers, no NCBI GenBank/SRA BioProject identifiers, and no link to the custom Python/R variant-calling and regression scripts.

### 3.5 Actionable Recommendations for Revision
1. **Correct the Confidence Interval and IQR Errors:** Replace the log-odds bounds (`0.6 to 5.6`) in the Abstract and Results with the actual exponentiated bounds (`1.9 to 269.9`), and recompute the true 25th and 75th percentiles for serum creatinine (and all other continuous variables) so that no strictly positive physiological measure has a negative lower quartile (`-0.4 mg/dL`).
2. **Audit and Fix Tables 1 and 2:** Correct the `All` column race totals in Table 1 (`Multiracial or Hispanic = 16`, `Other = 24`, summing to 302) and fix the `GH` clade row in Table 2 so that `ICU + No ICU = 56` and the column total equals `56` rather than `58`.
3. **Replace Overfit Stepwise Regression with Penalized or Exact Regression:** Given only 17 deaths in the entire cohort, abandon the 80/20 split and iterative backward stepwise elimination. Instead, fit a pre-specified Firth penalized likelihood logistic regression (or exact logistic regression) on the full cohort adjusted for a parsimonious set of *a priori* confounders (age, sex, healthcare worker status / calendar week, and Charlson comorbidity index).
4. **Deposit Genomic Sequences:** Deposit all 302 consensus genomes and raw reads in GISAID and NCBI SRA/GenBank and provide an accession table.
