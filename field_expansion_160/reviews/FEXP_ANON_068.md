# Review of FEXP_ANON_068

**Overall Score:** **1.6 / 10.0** (Fundamentally Invalid) | **Scientific Core Score:** **1.2 / 8.0**  
* **Score Breakdown:** Rigor: 0.4/3.5 | Claims: 0.4/2.5 | Biology: 0.4/2.0 | Reproducibility: 0.4/2.0

---

## 1. Blinded Metadata Perception
* **Perceived Subfield & Study Design:** Genetic Epidemiology / Two-Sample Mendelian Randomization (MR) testing a single exposure (circulating interleukin-6 [IL-6]) against a single outcome (unspecified synovitis and tenosynovitis).
* **Data Sources:** Plasma proteomics GWAS (`prot-b-2`, Sun et al., $N \approx 3,301$) and FinnGen R12 (`R12_M13_TENDOSYNOVITISNAS`).
* **Perceived Venue Tier:** Open-access general medical megajournal (single-exposure null two-sample MR report).

---

## 2. Executive Summary & Editorial Verdict

This manuscript reports a two-sample Mendelian randomization (MR) analysis evaluating the effect of genetically predicted circulating interleukin-6 (IL-6) levels (`prot-b-2`, Sun et al.) on the risk of unspecified synovitis and tenosynovitis in FinnGen R12 (`R12_M13_TENDOSYNOVITISNAS`). Using 15 SNPs selected at $P < 5 \times 10^{-6}$, the primary inverse-variance weighted (IVW) analysis yields a statistically null estimate ($\beta = -0.0236, \text{SE} = 0.0189, P = 0.2106$), as do MR-Egger ($\beta = -0.0391, P = 0.1442$), weighted median ($\beta = -0.0394, P = 0.1488$), simple mode ($\beta = -0.0500, P = 0.2875$), and weighted mode ($\beta = -0.0488, P = 0.0839$). Despite these uniformly null results, the authors repeatedly assert that the shared negative sign across the five correlated estimators demonstrates a "robust" inverse trend and supports a protective biological role of IL-6 in tendon sheaths.

**Editorial Verdict: Reject (Fundamentally Invalid).** A forensic audit of the numbers and tables in this manuscript uncovers pervasive mathematical impossibilities, internal numerical contradictions, and factual errors that point to severe computational corruption or fabrication of summary metrics:
1. **Impossible Instrument Metrics in Table 1:** The authors state they had to relax the instrument threshold from $P < 5 \times 10^{-8}$ to $P < 5 \times 10^{-6}$ due to a lack of genome-wide significant SNPs for IL-6 (Section 2.2.1, Line 38). Yet Table 1 reports that SNP `rs2995802` explains **$R^2 = 0.26$ (26% of total phenotypic variance in plasma IL-6!)** with an **$F$-statistic of $1171.47$** (which would correspond to $P < 10^{-200}$), and that the 15 SNPs combined explain $\sum R^2 = 0.45$ (45% of variance!). Worse, Table 1's `Power calculation` column assigns `rs2995802` ($R^2 = 0.26, F = 1171.47$) a *lower* power (`23.72`) than `rs4845373` ($R^2 = 0.01, F = 28.81$, `Power = 28.21`).
2. **Mathematically Impossible Benjamini-Hochberg FDR Values in Table 2:** Table 2 reports `p_fdr` values (`0.9985, 0.9505, 0.9552, 0.9973, 0.9659`) that are non-monotonic with the raw $P$-values (`0.2106, 0.1442, 0.2875, 0.1488, 0.0839`) and cannot be produced by the Benjamini-Hochberg `p.adjust` algorithm (which deterministically yields `0.2875` for all five rows).
3. **Self-Contradictory Sensitivity Statistics Across Sections:** The MR-Egger intercept is reported as `0.0126 (P = .369)` in Sections 3.1.3, 3.3.2, and 4, but as `0.005 (P = .631)` in Section 3.3.4. Similarly, MR-Egger Cochran's $Q$ is reported as `8.48 (P = .810)` in Section 3.3.5, but as `10.8 (P = .29)` in Section 4 (which is also mathematically impossible because $Q_{\text{Egger}}$ cannot exceed $Q_{\text{IVW}} = 9.35$ on the same data).
4. **Factual Errors in Data Provenance:** The manuscript states three times (Abstract, Line 28, Line 50) that Sun et al. (`prot-b-2`) used a "mass spectrometry-based proteomics platform," whereas Sun et al. (2018) used the aptamer-based SOMAscan platform.

### Assessment of Specific Conclusions
* **Claim 1: The 15 genetic instruments for IL-6 have $F$-statistics from $26.07$ to $1171.47$ (explaining $45\%$ of variance) and SNP-level statistical power between $21.15$ and $28.21$ (Table 1):** `[Methodologically Flawed]`  
  These values are mathematically irreconcilable. If `rs2995802` truly explained $R^2 = 0.26$ with $F = 1171.47$, it would have $P \ll 5 \times 10^{-8}$ and would yield vastly higher power than an instrument with $R^2 = 0.01$ ($F = 28.81$). Instead, the `Power calculation` numbers in Table 1 (`21.15` to `28.21`) bear no functional relationship to $R^2$ or $F$.
* **Claim 2: FDR-adjusted $P$-values across the five MR methods range from $0.9505$ to $0.9985$ via Benjamini-Hochberg correction (Table 2):** `[Methodologically Flawed]`  
  Applying Benjamini-Hochberg (`p.adjust(c(0.2106, 0.1442, 0.2875, 0.1488, 0.0839), method = "BH")`) in R yields `0.2875` for every single method. The reported `p_fdr` values (`0.9985, 0.9505, 0.9552, 0.9973, 0.9659`) violate step-up monotonicity ($p = 0.1488 \mapsto 0.9973$ while $p = 0.2875 \mapsto 0.9552$) and are mathematically impossible under BH adjustment.
* **Claim 3: Consistent negative point estimates across the five MR estimators ($\beta = -0.0236$ to $-0.0500$, all $P > 0.08$) demonstrate a "robust" protective trend of circulating IL-6 against tenosynovitis:** `[Overstated]`  
  IVW, MR-Egger, weighted median, simple mode, and weighted mode are five estimators applied to the *exact same 15 SNPs* and the *exact same exposure and outcome summary statistics*. Sharing the same sign across algebraically correlated estimators on a single dataset with $P_{\text{IVW}} = 0.2106$ is not independent replication and provides no statistical evidence of a protective effect.

---

## 3. Forensic Defect Inventory

### 1. [Critical] Mathematically Impossible $R^2$, $F$-Statistics, and Power Values in Table 1
* **Location:** Section 2.2.1 (Line 38), Section 3.1.1 (Line 68), and Table 1 (Lines 71–89).
* **Defect:**
  1. In Section 2.2.1 (Line 38), the authors state they had to relax the threshold from $P < 5 \times 10^{-8}$ to $P < 5 \times 10^{-6}$ due to the limited number of variants reaching genome-wide significance. In a sample of $N \approx 3,301$ (`prot-b-2`), a SNP with $5 \times 10^{-8} < P < 5 \times 10^{-6}$ has an $F$-statistic between $20.8$ and $29.7$ and $R^2 \approx 0.006\text{--}0.009$. Yet Table 1 reports $F$-statistics of $49.44\text{--}75.46$ ($R^2 = 0.01\text{--}0.02$) for 9 SNPs and an impossible **$R^2 = 0.26, F = 1171.47$** for `rs2995802`!
  2. The `Power calculation` column in Table 1 is decoupled from instrument variance: `rs2995802` ($R^2 = 0.26, F = 1171.47$) is assigned `Power calculation = 23.72`, whereas `rs4845373` ($R^2 = 0.01, F = 28.81$) is assigned `Power calculation = 28.21`. Statistical power in MR is strictly monotonically increasing with $R^2$; these numbers cannot come from a valid power formula.
* **Remediation:** Audit and replace Table 1 with the authentic SNP-level $\beta$, $\text{SE}$, $\text{EAF}$, $P$-values, $R^2$, and $F$-statistics extracted directly from `prot-b-2`, and compute a single study-level MR power curve rather than nonsensical per-SNP power numbers.

### 2. [Critical] Fabricated or Corrupted Benjamini-Hochberg FDR Values in Table 2
* **Location:** Section 2.3 (Line 57) and Table 2 (Lines 100–107).
* **Defect:** Line 57 states: *"FDR correction was performed using the Benjamini–Hochberg method, with a target $\alpha = 0.05$, implemented using the R package 'p.adjust.'"* For the 5 raw $P$-values in Table 2 (`0.2106, 0.1442, 0.2875, 0.1488, 0.0839`), the exact output of R's `p.adjust(p, method = "BH")` is `0.2875` for all 5 methods. Furthermore, under *any* step-up or step-down multiple-testing procedure, adjusted $P$-values must preserve the rank order of raw $P$-values ($p_1 \le p_2 \implies p_{1,\text{adj}} \le p_{2,\text{adj}}$) and cannot exceed $\min(1, m \cdot p_{(i)})$. In Table 2, `pval = 0.2875` has a *smaller* `p_fdr` (`0.9552`) than `pval = 0.2106` (`0.9985`), `pval = 0.1488` (`0.9973`), and `pval = 0.0839` (`0.9659`).
* **Remediation:** Remove the invalid `p_fdr` column from Table 2 (moreover, applying BH FDR across 5 sensitivity estimators of the *same* hypothesis is statistically inappropriate).

### 3. [Critical] Internal Contradictions in MR-Egger Intercept and Cochran's $Q$ Statistics
* **Location:** Section 3.1.3 (Lines 97, 108), Section 3.3.2 (Line 140), Section 3.3.4 (Line 153), Section 3.3.5 (Line 158), and Section 4 (Line 167).
* **Defect:** The manuscript reports two mutually contradictory sets of sensitivity statistics for the exact same analysis:
  * **MR-Egger Intercept:** Reported as `0.0126 (P = .369)` in Lines 97, 108, 140, and 167, but reported as `0.005 (P = .631)` in Section 3.3.4 (Line 153).
  * **MR-Egger Cochran's $Q$:** Reported as `Q = 8.48 (P = .810)` in Section 3.3.5 (Line 158), but reported as `Q = 10.8 (P = .29)` in Section 4 (Line 167). Because MR-Egger adds a free intercept parameter to the IVW weighted regression on the same SNPs, $Q_{\text{Egger}} \le Q_{\text{IVW}}$ is an algebraic identity; having $Q_{\text{Egger}} = 10.8 > Q_{\text{IVW}} = 9.35$ on Line 167 is mathematically impossible.
* **Remediation:** Re-run `mr_pleiotropy_test()` and `mr_heterogeneity()` on the harmonized dataset and report a single, verified set of statistics throughout the manuscript.

### 4. [Major] Factual Misrepresentation of Proteomics Assay Platform and Invalid "Zero Overlap $\chi^2$ Test"
* **Location:** Abstract (Line 5), Section 2.1 (Line 28), and Section 2.2.3 (Line 50).
* **Defect:**
  1. The authors repeatedly state that Sun et al. (`prot-b-2`) measured plasma proteins using a *"mass spectrometry-based proteomics platform."* Sun et al. (2018, *Nature* 558:73–79) used SOMAscan (modified DNA aptamers / SOMAmers), not mass spectrometry.
  2. Line 28 states: *"the exposure and outcome datasets were cross-validated for zero overlap ($\chi^2 = 0.00, P = 1.0$)."* Cohort sample overlap between two summary-level GWAS datasets (INTERVAL in the UK vs. FinnGen in Finland) is determined by cohort provenance, not by a $\chi^2$ contingency test.
  3. Rather than using biologically validated functional *cis*-variants in the IL-6 receptor pathway (*IL6R* Asp358Ala `rs2228145` or *cis*-pQTLs at *IL6*), the study uses 15 uncharacterized genome-wide (*trans*) SNPs at $P < 5 \times 10^{-6}$ without reporting which chromosome or gene any SNP resides in.
* **Remediation:** Correct the description of the SOMAscan platform, remove the meaningless $\chi^2 = 0.00$ overlap statement, and benchmark the analysis against established functional *cis*-instruments for IL-6 signaling (*IL6* and *IL6R*).

---

## 4. Quantitative Rubric Scoring

| Rubric Dimension | Score | Max | Forensic Justification |
| :--- | :---: | :---: | :--- |
| **1. Methodological & Statistical Rigor** | **0.4** | **3.5** | Mathematically impossible `p_fdr` values in Table 2; impossible $R^2 = 0.26 / F = 1171.47$ and inverted per-SNP power values in Table 1; algebraic violation $Q_{\text{Egger}} = 10.8 > Q_{\text{IVW}} = 9.35$; reliance on uncharacterized $P < 5 \times 10^{-6}$ *trans* SNPs instead of *cis*-*IL6*/*IL6R* instruments. |
| **2. Claim-to-Evidence Alignment** | **0.4** | **2.5** | Repeatedly frames a completely null result ($P_{\text{IVW}} = 0.2106$) as a "robust" protective relationship based on sign agreement across 5 correlated estimators on the same 15 SNPs. |
| **3. Data Integrity & Biological Plausibility** | **0.4** | **2.0** | Misidentifies SOMAscan (`prot-b-2`) as mass spectrometry; claims 15 SNPs at $P < 5 \times 10^{-6}$ explain 45% of plasma IL-6 variance; cites a nonsensical $\chi^2 = 0.00$ test for sample overlap. |
| **4. Reproducibility & Data Integrity** | **0.4** | **2.0** | Direct numerical contradictions in MR-Egger intercept (`0.0126` vs `0.005`) and Cochran's $Q$ (`8.48` vs `10.8`) across paragraphs; Table 1 omits $\beta$, SE, alleles, and genomic coordinates; `p.adjust` output in Table 2 cannot be reproduced. |
| **Scientific Core Score** | **1.2** | **8.0** | Sum of Rigor + Claims + Biology. |
| **Total Composite Score** | **1.6** | **10.0** | **Fundamentally Invalid** (16 / 100 equivalent). |
