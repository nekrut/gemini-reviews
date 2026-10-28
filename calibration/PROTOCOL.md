# Agentic Peer Review Power & Literature Error Estimation (`lit-estimation`)

## 1. Objective

Estimate:
1. **Diagnostic Power of Standardized Agentic Forensic Review:** Given only the manuscript and supplementary materials available at publication ($t_0$), what are the sensitivity ($\text{Se}$) and specificity ($\text{Sp}$) of a standardized 7-Pillar agentic review protocol ([`REVIEW_TEMPLATE.md`](../REVIEW_TEMPLATE.md)) in detecting fatal methodological, statistical, consistency, or code/data failures?
2. **Prevalence of Flawed Research in the Wild ($\hat{\pi}_{\text{true}}$):** Applying the calibrated reviewer to a stratified random sample of unscrutinized papers in quantitative biology, viral/molecular evolution, genomics, bioinformatics, and biostatistics, what fraction of published papers exhibit smoking-gun methodological or statistical failures?

---

## 2. Failure Taxonomy (Direct Detectable Failures)

A manuscript is classified as **Failed / Invalidated** when the review identifies concrete, verifiable defects in one or more of four categories:

1. **Wrong Methods (Methodological Invalidity):**
   * The mathematical, statistical, or evolutionary model violates core properties of the data-generating process (e.g., treating phylogenetically linked sequences as independent i.i.d. observations; unidentifiable parameterizations; circular conditioning or data leakage between feature selection/normalization and evaluation).
2. **Fatal Inconsistencies (Results $\not\Rightarrow$ Conclusions):**
   * Headline claims in the Title, Abstract, or Discussion are unsupported by or contradicted by the manuscript's own tables, figures, or supplementary results (e.g., asymmetric interpretation of controls vs. cases, shifting sample denominators, or negative controls showing comparable signals to focal groups).
3. **Statistical Failures:**
   * Uncorrected multiple hypothesis testing that eliminates significance under standard FDR/FWER control, pseudoreplication, severe unadjusted confounding/batch effects, conditioning on colliders, or mathematically inconsistent test statistics, degrees of freedom, and $p$-values.
4. **Code & Data Bugs:**
   * Verifiable defects in supplementary spreadsheets, alignments, or analysis scripts (e.g., label misalignment, positive-control carryover/contamination in sequences, off-by-one indexing, train/test split leakage, or duplicated data rows).

---

## 3. Three-Cohort Study Design ($N = 25$ per cohort)

### Cohort A: Known Invalid / Refuted under Scrutiny ($N = 25$)
* **Definition:** Published manuscripts or high-profile preprints in viral evolution, genomics, bioinformatics, and biostatistics whose core conclusions were subsequently invalidated by peer-reviewed refutations, forensic re-analyses, or formal retractions due to methodological, statistical, contamination, or code/data errors.
* **Purpose:** Estimate True Positive Rate / Sensitivity ($\widehat{\text{Se}}$) and verify whether the agent independently pinpoints the ground-truth fatal flaw.

### Cohort B: Validated / Stress-Tested Controls ($N = 25$)
* **Definition:** Published manuscripts in the same domains (matched across subfields and eras) whose core methods and empirical findings survived independent replication, benchmark validation, or extensive follow-up extensions.
* **Purpose:** Estimate True Negative Rate / Specificity ($\widehat{\text{Sp}}$) and calibrate the score boundary between minor reviewer nitpicks and fatal flaws.

### Cohort C: Stratified "Wild" Literature Sample ($N = 25$)
* **Definition:** A stratified random sample of open-access papers from PubMed Central (PMC) across target domains that have neither been retracted nor been the subject of high-profile refutations.
* **Stratification:** Sampled across Venue Tier (High-Impact Generalist vs. Domain Specialist) and Citation Velocity (Low/Uncited vs. Moderately/Highly Cited).
* **Purpose:** Estimate raw failure rate $\hat{p}_{\text{obs}}$, human-verified smoking-gun rate, and Rogan-Gladen / Bayesian prevalence $\hat{\pi}_{\text{true}}$.

---

## 4. Standardized Execution & Blinding Protocol

1. **Rubric & Template:** All reviews follow the 7-Pillar Audit and 1–10 Quantitative Scoring Rubric defined in [`REVIEW_TEMPLATE.md`](../REVIEW_TEMPLATE.md).
2. **Information Boundary ($t_0$ Isolation):**
   * The reviewer receives only the manuscript text, figures, tables, and original supplementary materials/code.
   * Web search for subsequent citing papers, PubPeer commentary, retraction notices, or refutations is strictly prohibited.
   * **Blinding Check (De-identification):** On Cohort A and Cohort B, manuscripts can be evaluated in both standard format and de-identified format (stripping title, authors, journal, and DOI) to quantify any memorization or prestige bias.
3. **Decision Thresholds:**
   * **Continuous:** Overall Score $S \in [1.0, 10.0]$ and sub-scores (`rigor` $/3.5$, `claims` $/2.5$, `biology` $/2.0$, `reproducibility` $/2.0$).
   * **Binary Failure Classification:** Pre-specified cutoff at **Overall Score $< 5.0$** (`Flawed / Overstated` or `Fundamentally Invalid`) or $\ge 50\%$ of headline claims in Section 2 rated `Methodologically Flawed` / `Overstated`.

---

## 5. Statistical Estimators

1. **Diagnostic Performance (Cohorts A & B):**
   * Sensitivity: $\widehat{\text{Se}} = P(S < 5.0 \mid \text{Cohort A})$
   * Specificity: $\widehat{\text{Sp}} = P(S \ge 5.0 \mid \text{Cohort B})$
   * Ground-Truth Defect Recall: Fraction of Cohort A papers where the specific primary flaw identified in the published refutation/retraction is explicitly recovered in Section 1/2 of the agentic review.
   * Nonparametric Mann-Whitney $U$ / ROC-AUC comparing score distributions $S_A$ vs. $S_B$.
2. **Prevalence in the Unscrutinized Literature (Cohort C):**
   * **Rogan-Gladen Prevalence Estimator:**
     $$\hat{\pi}_{\text{true}} = \text{clip}_{[0,1]}\left(\frac{\hat{p}_{\text{obs}} - (1 - \widehat{\text{Sp}})}{\widehat{\text{Se}} - (1 - \widehat{\text{Sp}})}\right)$$
   * **Direct Verified Defect Rate ($\hat{\pi}_{\text{verified}}$):** Every Cohort C paper flagged as $< 5.0$ (or with a fatal claim defect) undergoes direct human domain audit to confirm whether the flagged defect is an undeniable smoking gun ($FP_{\text{verified}} = 0 \implies \hat{p}_{\text{verified}}$ is a strict lower bound on $\pi_{\text{true}}$).

---

## 6. Protocol Amendments (post hoc, undated)

The study as executed and reported in [`CALIBRATION.md`](../CALIBRATION.md) deviates from the protocol above as follows:

1. **Sample size:** $N$ expanded from 25/25/25 (phase 1, Results Sections 2–5 of `CALIBRATION.md`) to 50/50/100 (Cohorts A/B/C; Section 6 of `CALIBRATION.md`, `cohorts_200.json`, `results_200.json`).
2. **Cutoffs:** Only $S < 5.0$ and the claim-based rule (Section 4.3) were pre-specified. Cutoffs $S < 5.5$, $< 6.0$ and $< 6.5$ were added and should be treated as exploratory.
3. **Internal ($N=45$) vs. Upstream ($N=5$) Cohort A split:** Not specified in this protocol; defined after phase 1, where the 5 Cohort A papers scoring $\ge 7.0$ motivated the internal/upstream distinction. `CALIBRATION.md` Section 1.1 describes this stratification as a priori.
4. **Cohort reassignment:** `PMC8135569` (Kumar et al. 2021, *Mol Biol Evol*) moved from Cohort B (`B02`) to Cohort A (`A26`) after phase 1; `B02` was reassigned to `PMC7418704` (Starr et al. 2020, *Cell*).
5. **Review reuse:** All 75 phase-1 de-identified reviews (`ANON_01`–`ANON_75`) were reused unchanged in the $N = 200$ analysis (same anon IDs, scores and review files in `deidentified_results.json` and `results_200.json`).
6. **Not yet performed:** the claim-based binary failure rule ($\ge 50\%$ of headline claims `Methodologically Flawed` / `Overstated`), Ground-Truth Defect Recall, Bayesian prevalence estimation, and the human domain audit of flagged Cohort C papers ($\hat{\pi}_{\text{verified}}$).
