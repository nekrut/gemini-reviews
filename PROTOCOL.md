# Agentic Peer Review Power & Literature Error Estimation (`lit-estimation`)

## 1. Objective

Estimate:
1. **Diagnostic Power of Standardized Agentic Forensic Review:** Given only the manuscript and supplementary materials available at publication ($t_0$), what are the sensitivity ($\text{Se}$) and specificity ($\text{Sp}$) of a standardized 7-Pillar agentic review protocol ([`REVIEW_TEMPLATE.md`](REVIEW_TEMPLATE.md)) in detecting fatal methodological, statistical, consistency, or code/data failures?
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

## 3. Three-Cohort Study Design ($N = 25$ per cohort in Phase 1; $50 + 50 + 100 = 200$ in Phase 2)

### Cohort A: Known Invalid / Refuted under Scrutiny ($N = 25 \to 50$)
* **Definition:** Published manuscripts or high-profile preprints in viral evolution, genomics, bioinformatics, and biostatistics whose core conclusions were subsequently invalidated by peer-reviewed refutations, forensic re-analyses, or formal retractions due to methodological, statistical, contamination, or code/data errors.
* **Purpose:** Estimate True Positive Rate / Sensitivity ($\widehat{\text{Se}}$) and verify whether the agent independently pinpoints the ground-truth fatal flaw.

### Cohort B: Validated / Stress-Tested Controls ($N = 25 \to 50$)
* **Definition:** Published manuscripts in the same domains (matched across subfields and eras) whose core methods and empirical findings survived independent replication, benchmark validation, or extensive follow-up extensions.
* **Purpose:** Estimate True Negative Rate / Specificity ($\widehat{\text{Sp}}$) and calibrate the score boundary between minor reviewer nitpicks and fatal flaws.

### Cohort C: Stratified "Wild" Literature Sample ($N = 25 \to 100$)
* **Definition:** A stratified random sample of open-access papers from PubMed Central (PMC) across target domains that have neither been retracted nor been the subject of high-profile refutations.
* **Stratification:** Sampled across 5 core domains (`20` per domain in Phase 2) and Citation Velocity tiers (`High >=25`, `Mid 5-24`, `Low 0-4` citations, plus age-adjusted citations/year).
* **Purpose:** Estimate raw failure rate $\hat{p}_{\text{obs}}$, human-verified smoking-gun rate, and Rogan-Gladen prevalence $\hat{\pi}_{\text{true}}$.

---

## 4. Standardized Execution, De-Identification & Model Provenance

### 4.1 Rubric & Information Boundary ($t_0$ Isolation)
1. **Rubric & Template:** All reviews follow the 7-Pillar Audit and 1–10 Quantitative Scoring Rubric defined in [`REVIEW_TEMPLATE.md`](REVIEW_TEMPLATE.md).
2. **Information Boundary ($t_0$ Isolation):**
   * The reviewer receives only the manuscript text, figures, tables, and original supplementary materials/code.
   * Web search for subsequent citing papers, PubPeer commentary, retraction notices, or refutations is strictly prohibited (`search_web` disabled).

### 4.2 Deterministic De-Identification Preprocessor ([`scripts/build_deidentified.py`](scripts/build_deidentified.py))
Before any blinded review is executed, the deterministic scrubber (`scripts/build_deidentified.py` and `scripts/fetch_and_scrub_125.py`) strips identifying metadata:
* **Header & Identifier Stripping:** Strips Title (including any `RETRACTED:` or `WITHDRAWN:` prefix), Author Names, Affiliations, Correspondence lines, Journal Name, Publication Year, DOI, and PMCID/PMID (`[REDACTED FOR BLINDED REVIEW]`).
* **Section & Banner Filtering:** Removes `Acknowledgements`, `Author Contributions`, `Funding`, `Competing Interests`, and any PMC retraction notice banners.
* **Repository URL & Handle Redaction:** Redacts GitHub, GitLab, and Bitbucket URLs containing owner/lab handles (`github.com/<owner>/<repo>` $\to$ `[GITHUB_REPO_REDACTED]`, `gitlab.com/<owner>/<repo>` $\to$ `[GITLAB_REPO_REDACTED]`).
* **Self-Citation & Surname Redaction:** Redacts `<Surname> et al.` self-citations (for all author surnames $\ge 3$ characters) as well as standalone non-common author surnames ($\ge 5$ characters).
* **Post-$t_0$ Year Redaction:** Scrubs calendar years strictly greater than the publication year $t_0$ (`[POST_T0_YEAR_REDACTED]`).

### 4.3 Model & Prompt Provenance
* **Model & Harness:** All reviews across the calibration study ($N=200$), repeatability study ($N=30 \times 3$), out-of-domain generalization study ($N=60$), paired preprint-to-published audit ($N=20 \times 2$), longitudinal secular trend study ($N=70$), and blinded Pond self-audit ($N=164$) were executed using **`Gemini 4 Argon`** via the Antigravity agentic harness using isolated, stateless `anon-reviewer` subagents with web search disabled (`search_web = false`) and filesystem access restricted to the de-identified manuscript file and `REVIEW_TEMPLATE.md`.
* **Prompt Version History (`REVIEW_TEMPLATE.md`):**
  * **Commit `01665db` (`9,661` bytes / `9.7 KB`):** Clean 7-Pillar Forensic Review Protocol without empirical calibration outcome tables; used during the 200-paper calibration study (`CALIBRATION.md`).
  * **Commit `2945b80` (`12,830` bytes):** Added empirical summary notes in Part 0 and Part 5 following completion of the 200-paper calibration; present during Experiments 1–5.
  * **v1.1 Clean Rubric Restoration:** All empirical calibration outcome summaries and prevalence tables live strictly in [`CALIBRATION.md`](CALIBRATION.md) rather than inside `REVIEW_TEMPLATE.md`, ensuring zero circularity between prompt text and calibration outcomes.
* **Reproducible Verification Script:** [`scripts/verify_repeatability_and_calibration.py`](scripts/verify_repeatability_and_calibration.py) deterministically recomputes all pooled and per-cohort $\text{ICC}(2,1)$, $\text{ICC}(3,1)$, $\text{ICC}(2,3)$, sub-score ICCs, Fleiss' $\kappa$, Pilot vs. Held-Out calibration sensitivity matrices, Cohort B control-composition sensitivity tables, and OOD Stage-1 vs. Stage-2 metrics directly from the committed JSON files.

### 4.4 Decision Thresholds
* **Primary Pre-Specified Failure Endpoint:** **Overall Score $S < 5.0$** (`Flawed / Overstated` or `Fundamentally Invalid`).
* **Exploratory / Secondary Thresholds:** $S < 5.5$, $S < 6.0$ (calibrated boundary separating `Mixed / Salvageable` lower half from `Strong / Sound`), and $S < 6.5$ (`Any Major Pillar Violation`), reported alongside full sensitivity matrices in [`CALIBRATION.md`](CALIBRATION.md).

---

## 5. Statistical Estimators

1. **Diagnostic Performance (Cohorts A & B):**
   * Sensitivity: $\widehat{\text{Se}} = P(S < \tau \mid \text{Cohort A})$
   * Specificity: $\widehat{\text{Sp}} = P(S \ge \tau \mid \text{Cohort B})$
   * Ground-Truth Defect Recall: Fraction of Cohort A papers where the specific primary flaw identified in the published refutation/retraction is explicitly recovered in Section 1/2 of the agentic review.
   * Nonparametric Mann-Whitney $U$ / ROC-AUC comparing score distributions $S_A$ vs. $S_B$.
2. **Prevalence in the Unscrutinized Literature (Cohort C):**
   * **Rogan-Gladen Prevalence Estimator:**
     $$\hat{\pi}_{\text{true}} = \text{clip}_{[0,1]}\left(\frac{\hat{p}_{\text{obs}} - (1 - \widehat{\text{Sp}})}{\widehat{\text{Se}} - (1 - \widehat{\text{Sp}})}\right)$$
   * **Direct Verified Defect Rate ($\hat{\pi}_{\text{verified}}$):** Every Cohort C paper flagged as $< 5.0$ undergoes direct domain audit of the specific mathematical, statistical, or table inconsistency cited in the review.

---

## 6. Protocol Amendments & Sensitivity Audit Log

The study as executed and reported in [`CALIBRATION.md`](CALIBRATION.md) evolved from Phase 1 ($N=75$) to Phase 2 ($N=200$) as follows, with all choices audited via full sensitivity matrices in `CALIBRATION.md` Section 7:

1. **Sample size & Held-Out Confirmatory Split:** $N$ expanded from `25/25/25` (Phase 1 Pilot, `ANON_01`–`ANON_75`) to `50/50/100` (`cohorts_200.json`, `results_200.json`). Phase 1 reviews (`ANON_01`–`ANON_75`) were retained unchanged, while the **`125` expansion manuscripts (`ANON_76`–`ANON_200`: `A26–A50`, `B26–B50`, `C26–C100`)** serve as a strictly held-out confirmatory validation cohort evaluated after thresholds were fixed ($\text{Held-Out AUC} = 0.9824$, $\widehat{\text{Se}}_{<5.0} = 64.0\%$, $\widehat{\text{Sp}}_{<5.0} = 100.0\%$, $\widehat{\text{Se}}_{<6.0} = 76.0\%$, $\widehat{\text{Sp}}_{<6.0} = 100.0\%$, Held-Out Cohort C failure rate $= 44.0\%$ at $<5.0$ and $60.0\%$ at $<6.0$).
2. **Cutoffs:** $S < 5.0$ is the primary pre-specified endpoint. Cutoffs $S < 5.5$, $< 6.0$, and $< 6.5$ were added after Phase 1 and are reported across both the Phase-1 pilot and the held-out `125`-paper expansion cohort.
3. **Internal vs. Upstream Cohort A Split:** Defined after Phase 1 to distinguish flaws internal to the manuscript's own equations/tables/methods from flaws residing in external consortium inputs (e.g., GIANT GWAS summary statistics) or later mathematical congruence theorems. `CALIBRATION.md` Section 7 reports all four definitions side by side: All Cohort A ($N=50$), Strict GIANT-Consortium Exclusion (`A11, A23, A24`; $N=47$), Phase-1 Upstream/Congruence Exclusion (`A07, A11, A19, A24, A25`; $N=45$), and Broad Upstream/Congruence Exclusion (`A07, A11, A19, A23, A24, A25`; $N=44$).
4. **Cohort Reassignment (`PMC8135569`, Kumar et al. 2021):** Moved from pilot `B02` (where the identified review accidentally evaluated the 2020 bioRxiv preprint `PMC7523107` at `7.5/10`) to `A26` (refuted by Pekar et al. 2022 *Science* for `proCoV2` mutational-order rooting; blinded review of published *MBE* text `PMC8135569` scored `3.3/10`), and `B02` was assigned to `PMC7418704` (Starr et al. 2020 *Cell*). `CALIBRATION.md` Section 7 reports all metrics under both the published labels ($\text{AUC} = 0.9688$, $\widehat{\text{Sp}}_{<5.0} = 100\%$), the original pilot labels ($\text{AUC} = 0.9553$, $\widehat{\text{Sp}}_{<5.0} = 98.0\%$), and excluding `PMC8135569` entirely ($\text{AUC} = 0.9682$, $\widehat{\text{Sp}}_{<5.0} = 100\%$). In our independent 164-paper Blinded Pond Self-Audit ([`SPOND_SELF_AUDIT.md`](SPOND_SELF_AUDIT.md)), `PMC8135569` (`SP_ANON_003`) independently scored **`4.2 / 10.0` (`Reject`)**.
5. **Retraction Notices & Defect Recall for `A44–A50`:** Exact retraction notice DOIs and PMIDs are recorded in `calibration/cohorts_200.json`. Across all 50 Cohort A papers, the blinded reviewer explicitly recovered the exact ground-truth refuted/retracted defect in **`38 / 40` (`95.0%`)** of papers scoring $< 6.5$ (`76.0%` [`38/50`] across all 50 Cohort A papers including upstream consortium flaws).
