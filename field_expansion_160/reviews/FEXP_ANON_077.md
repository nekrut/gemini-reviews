# Forensic Scientific Review: FEXP_ANON_077

**Overall Score:** **1.6 / 10.0** (Fundamentally Invalid) | **Scientific Core Score:** **1.2 / 8.0**
* **Score Breakdown:** Rigor: 0.4/3.5 | Claims: 0.4/2.5 | Biology: 0.4/2.0 | Reproducibility: 0.4/2.0

---

## 1. Blinded Metadata Perception
* **Perceived Field & Subfield:** Urologic Oncology / Statistical Genetics / Computational Immunology (Bidirectional Two-Sample Mendelian Randomization of 731 circulating immune cell phenotypes across three urological malignancies).
* **Perceived Study Design:** Public-summary-data bidirectional two-sample Mendelian Randomization pairing 731 Sardinian flow-cytometry immunophenotypes (`GCST90001391`–`GCST90002121`, Orrù et al., $N = 3,757$) with three FinnGen urological cancer GWAS datasets (renal cancer: $2,372$ cases / $314,193$ controls; bladder cancer: $2,193$ cases / $314,193$ controls; prostate cancer: $15,199$ cases / $131,266$ controls).

---

## 2. Executive Summary & Editorial Verdict
This manuscript represents a textbook mass-screen Mendelian Randomization study ($731\text{ immune traits} \times 3\text{ cancers} = 2,193\text{ tests}$) compromised by fatal mathematical errors in its False Discovery Rate (`P_FDR`) calculations, severe table corruption, internal numerical contradictions between the text and tables, and machine-translation / template copy-paste artifacts. First and most decisively, every single `P_FDR` value reported in `Table 1`, `Table 2`, and `Table 3` is mathematically impossible under a Benjamini–Hochberg correction across $m = 731$ tested immunophenotypes: raw IVW $P$-values of `.008`, `.007`, `.005`, `.004`, `.003`, and `.002` are reported as having `P_FDR` values of `.008`, `.008`, `.009`, `.009`, `.008`, and `.007`—a result that is only possible if `p.adjust()` was applied post-hoc to a pre-filtered subset of ~12 already-significant hits rather than across all 731 tested exposures. When properly adjusted across $m = 731$ traits per cancer, $21$ of the $22$ claimed causal associations fail $\text{FDR} < 0.05$ (`q = 0.14` to `0.55`). Second, `Table 1` is physically truncated after the 9th trait (omitting 3 of the 12 claimed renal cancer traits and truncating the 9th trait after its `IVW` row), while `Table 3` exhibits severe column-shift and row-duplication corruption (`Heterogeneity Q` and `Q-P val` values appear inside `Weighted mode` and `Weighted median` rows and are duplicated verbatim across unrelated traits). Third, the text displays severe machine-translation and editing failures, including translating "prostate cancer" (Chinese: 前列腺癌) as **"anterior adenocarcinoma"** (`Line 192`), garbling `unsw mem` (unswitched memory B cells) into **"unsaw mem"** (`Lines 145, 196`), labeling both the bladder cancer (`Figure 5`, `Line 148`) and prostate cancer (`Figure 6`, `Line 177`) forest plots as showing *"protective factors (OR < 1) and risk factors (OR > 1) for **renal cancer**"*, and formatting numbers with South Asian lakh/crore comma separators (`3,14,193`, `1,98,38,363`, `5,00,000`).

* **Claim 1:** *"Notably, we identified 12 immune cell phenotypes with causal associations with renal cancer, 4 with bladder cancer, and 6 with prostate cancer (PFDR < 0.05)."* — **`[Methodologically Flawed]`** (Mathematically impossible under Benjamini–Hochberg FDR across $m = 731$ tested immune traits; raw IVW $P$-values of $0.002\text{--}0.008$ yield true BH $q$-values of $0.14\text{--}0.55$, proving that FDR adjustment was improperly computed only on the pre-selected subset of nominal hits rather than the 731-trait hypothesis space).
* **Claim 2:** *"Specifically, in renal cancer, a genetic predisposition to CD20 on IgD− CD38br... was associated with an increased risk (odds ratio [OR] = 1.067, 95% confidence interval [CI]: 1.017–1.120, P = .008, PFDR = 0.008). Similarly, CD25 on B cells... showed a positive association (OR = 1.067, 95% CI: 1.022–1.114, P = .004, PFDR = 0.009)."* — **`[Methodologically Flawed]`** (In addition to the invalid `P_FDR` calculation, `Abstract Line 5` and `Section 3.2 Line 137` invert the 95% CIs and $P$-values of `CD20 on IgD− CD38br` and `CD25 on B cell` relative to `Table 1 Lines 74 & 78`).
* **Claim 3:** *"Reverse MR analysis did not identify any significant causal effects of these malignancies on immune cell phenotypes."* — **`[Fragile]`** (The manuscript provides zero quantitative tables, instrument counts, or effect estimates for any of the $3 \times 731 = 2,193$ reverse MR analyses).

---

## 3. Forensic Defect Inventory

### 3.1 Major Statistical, Table Integrity, and Editorial Defects

1. **Mathematically Impossible Benjamini–Hochberg `P_FDR` Values Across All Three Tables (`Table 1`, `Table 2`, `Table 3`, `Lines 66–131`):**
   * The authors tested $m = 731$ immune cell traits against each of the three cancers (`Section 2.2`, `Line 37`) and claim in `Section 2.5` (`Line 55`) and `Section 3.1` (`Line 62`) that $12$ renal cancer traits, $4$ bladder cancer traits, and $6$ prostate cancer traits passed `P_FDR < 0.05`.
   * Under the Benjamini–Hochberg step-up procedure across $m = 731$ tests, the adjusted $q$-value for the $k$-th smallest $P$-value $p_{(k)}$ is bounded below by $\frac{731}{k} p_{(k)}$ (monotonically enforced). Let us audit the reported `P` and `P_FDR` columns in `Tables 1–3`:
     * **Renal cancer (`Table 1` and `Section 3.2`):** Only $12$ traits had $P < 0.01$, with the 12th-ranked trait having $p_{(12)} = 0.008$ (`CD20 on IgD- CD38br` / `CD25 on B cell`). Across $m = 731$ tests, the BH-adjusted value at rank $k = 12$ is:
       $$q_{(12)} = \frac{731}{12} \times 0.008 = \mathbf{0.4873}$$
       Even for the 2nd most significant renal trait (`CD62L- dendritic cell %dendritic cell`, $p_{(2)} = 7.38 \times 10^{-4}$), $q_{(2)} = \frac{731}{2} \times 7.38 \times 10^{-4} = \mathbf{0.2697}$! Only the single smallest $P$-value (`CD127- CD8br AC`, $p_{(1)} = 6.73 \times 10^{-5}$, reported in text `Line 137` but missing from truncated `Table 1`) barely reaches $q_{(1)} = 731 \times 6.73 \times 10^{-5} = 0.0492$. Yet `Table 1` reports `P_FDR = .004` for $P = 7.38 \times 10^{-4}$, `P_FDR = .007` for $P = .002$, and `P_FDR = .008` / `.009` for $P = .008$!
     * **Bladder cancer (`Table 2`, `Lines 106–116`):** $4$ traits are reported with raw IVW $P$-values of `.003`, `.006`, `.006`, and `.007`. Across $m = 731$ tests, their true BH $q$-values are $\ge \frac{731}{4} \times 0.007 = \mathbf{1.00}$ (completely null), yet `Table 2` reports `P_FDR` values of `.007`, `.008`, `.008`, and `.008`!
     * **Prostate cancer (`Table 3`, `Lines 120–131`):** $6$ traits are reported with raw IVW $P$-values of `.001`, `.003`, `.004`, `.005`, `.005`, and `.006`. Across $m = 731$ tests, their true BH $q$-values are $\mathbf{0.731}$ to $\mathbf{0.731}$, yet `Table 3` reports `P_FDR` values of `.006`, `.007`, `.008`, `.008`, `.008`, and `.009`!
   * **Forensic Diagnosis:** Notice that in `Table 1`, $\frac{0.004}{7.38 \times 10^{-4}} \approx 5.4$ and $\frac{0.009}{0.008} = 1.125$. The authors first filtered the 731 results by raw $P < 0.01$ (leaving ~12, 4, or 6 traits) and then ran `p.adjust(..., method = "fdr")` on **only the pre-filtered winners** rather than the 731-trait hypothesis space!

2. **Physical Truncation of `Table 1` and Severe Column/Row Corruption in `Table 3` (`Lines 66–102`, `Lines 120–131`):**
   * **`Table 1` Truncation (`Line 102`):** Although the text states that 12 immune traits are associated with renal cancer (`Section 3.2`, `Line 137`), `Table 1` stops abruptly at the `Inverse variance weighted` row of the 9th trait (`Myeloid cell | HLA DR on CD33dim HLA DR+ CD11b-`), omitting its `MR-Egger`, `Weighted median`, and `Weighted mode` rows as well as the entire entries for the remaining 3 traits (`HLA DR on B cell`, `CD127- CD8br AC`, and `CD25 on CD39+ activated Treg`).
   * **`Table 3` Row-Shift and Copy-Paste Corruption (`Lines 123–131`):**
     * For `CD86+ plasmacytoid DC` (`Line 123`), the `Heterogeneity (Q, Q-P val)` values (`29.424 | .205`) are placed in the `Weighted mode` row instead of the `IVW` or `MR-Egger` rows!
     * For `CD25hi CD45RA+ CD4 not Treg AC` (`Lines 124–125`), the `MR-Egger` row has blank `Q` and `Q-P val`, whereas its `Weighted mode` row contains `Q = 11.760 | Q-P val = .896`!
     * Immediately below, for `CD127 on CD28- CD8br` (`Lines 126–127`), the `IVW` row repeats the exact same `Q = 11.760 | Q-P val = .896` from the preceding trait, while its `MR-Egger` (`22.381 | .557`) and `Weighted median` (`22.320 | .617`) rows duplicate the exact `Q` and `Q-P val` numbers from `CD19 on IgD- CD38-` (`Lines 128–129`)!

3. **Contradictory Numbers Between Abstract/Text and `Table 1` (`Lines 5, 74, 78, 137`):**
   * In `Abstract Line 5` and `Section 3.2 Line 137`:
     * `CD20 on IgD− CD38br`: `OR = 1.067, 95% CI: 1.017–1.120, P = .008, PFDR = 0.008`
     * `CD25 on B cell`: `OR = 1.067, 95% CI: 1.022–1.114, P = .004, PFDR = 0.009`
   * In `Table 1` (`Lines 74 & 78`), the exact opposite values are printed:
     * `CD20 on IgD− CD38br` (`Line 74`): `OR = 1.067, 95% CI: 1.022–1.114, P = .004, PFDR = .009`
     * `CD25 on B cell` (`Line 78`): `OR = 1.067, 95% CI: 1.017–1.120, P = .008, PFDR = .008`

4. **Severe Machine-Translation / LLM Hallucinations and Copy-Pasted Figure Captions (`Lines 40, 145, 148, 177, 192, 196`):**
   * **"Anterior adenocarcinoma" for Prostate Cancer (`Line 192`):** In `Section 4` (`Line 192`), the authors write: *"However, up to now, no study has focused on CD86+ plasmacytoid DC and **anterior adenocarcinoma**."* In Chinese, prostate cancer is 前列腺癌 (*qiánlièxiàn ái*), where 前 (*qián*) literally means "anterior/front"—an unmistakable machine-translation artifact.
   * **"Unsaw mem" for `unsw mem` (`Lines 145, 196`):** In `Section 3.3` (`Line 145`) and `Section 4` (`Line 196`), `IgD on IgD+ CD38− unsw mem` (unswitched memory B cells) is garbled into *"the theory that egged on 'unsaw mem,' also known as 'unswitched memory B cells expressing IgD'"*.
   * **Copy-Pasted Figure Captions (`Lines 148, 177`):** Both `Figure 5` (which displays the 4 **bladder cancer** traits, `Line 148`) and `Figure 6` (which displays the 6 **prostate cancer** traits, `Line 177`) carry the copy-pasted caption: *"This figure highlights both protective factors (OR < 1) and risk factors (OR > 1) for **renal cancer**."* Furthermore, `Figure 5`'s caption (`Line 148`) erroneously defines `AC` as *"activated cells"* instead of *"absolute count"*.
   * **South Asian Lakh/Crore Number Formatting (`Section 2.3`, `Line 40`):** Sample sizes and SNP counts are formatted as `3,14,193`, `1,98,38,363`, `1,98,38,275`, and `5,00,000`.

---

## 4. Quantitative Rubric Scoring

* **1. Methodological & Statistical Rigor (0.4 / 3.5):** Complete invalidation of the primary multiple-testing correction (`P_FDR` computed on pre-filtered nominal hits instead of across the 731 tested exposures, leaving 21 of 22 hits non-significant at $\text{FDR} < 0.05$).
* **2. Substantiation of Claims & Internal Consistency (0.4 / 2.5):** Severe internal contradictions (`Table 1` vs. text swaps, truncated `Table 1`, shifted/duplicated columns in `Table 3`, wrong diseases in `Figure 5` and `Figure 6` captions).
* **3. Biological, Evolutionary, or Clinical Plausibility & Novelty (0.4 / 2.0):** Formulaic univariable two-sample MR cataloging with machine-translated immunological prose ("anterior adenocarcinoma", "the theory that egged on 'unsaw mem'") and zero biological validation.
* **4. Reproducibility, Data Hygiene & Transparency (0.4 / 2.0):** Truncated and corrupted main tables, unstated reverse MR statistics, and post-hoc falsified `P_FDR` columns fail basic data hygiene standards.
