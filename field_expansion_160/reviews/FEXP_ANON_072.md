# Review of FEXP_ANON_072

**Overall Score:** **2.2 / 10.0** (Fundamentally Invalid) | **Scientific Core Score:** **1.6 / 8.0**  
* **Score Breakdown:** Rigor: 0.5/3.5 | Claims: 0.5/2.5 | Biology: 0.6/2.0 | Reproducibility: 0.6/2.0

---

## 1. Blinded Metadata Perception
* **Perceived Subfield & Study Design:** Genetic Epidemiology / Two-Sample Metabolome-Wide Mendelian Randomization (MR) testing 2,187 plasma metabolite traits across 3 exposure cohorts against hypertension in FinnGen and UK Biobank.
* **Data Sources:** Three plasma metabolomics GWAS datasets (CLSA $1,091$ metabolites, $N = 8,299$; Long et al. $644$ metabolites, $N = 1,920$ or $1,960$; Shin et al. $452$ or $486$ metabolites, $N = 7,824$) and two hypertension GWAS datasets (FinnGen discovery: $122,996$ cases / $289,117$ controls; UK Biobank replication: $129,909$ cases / $354,689$ controls).
* **Perceived Venue Tier:** Open-access general medical megajournal.

---

## 2. Executive Summary & Editorial Verdict

This study conducts a two-sample Mendelian randomization (MR) screen of 2,187 plasma metabolite traits pooled from three published GWASs (CLSA, Long et al., and Shin et al.) against hypertension in FinnGen ($N = 412,113$), using SNPs selected at $P < 5 \times 10^{-6}$ ($r^2 < 0.001$, window $= 10,000\text{ kb}$) and a Bonferroni threshold of $P < 0.05 / 2187 = 2.29 \times 10^{-5}$. The authors report 9 metabolites passing Bonferroni significance in FinnGen (4 positive: taurochenodeoxycholate, 1-dihomo-linolenoyl-GPC, N-acetylphenylalanine, dihomo-linolenate; 5 negative: 2-hydroxyoctanoate, 1-docosapentaenoyl-GPC, X-11538, gamma-glutamyl-alpha-lysine, 2-butenoylglycine), of which 3 reach nominal significance ($P < 0.05$) in a UK Biobank replication cohort ($N = 484,598$).

**Editorial Verdict: Reject (Fundamentally Invalid).** A forensic examination of the reported instrument metrics and tables reveals fatal mathematical impossibilities and extreme carelessness in data curation and reporting:
1. **Mathematically Impossible Variance Explained ($R^2 = 0.912$) and Inconsistent $F$-Statistics in Table 3:** Table 3 claims that 24 SNPs explain **$R^2 = 0.912$ (91.2% of total phenotypic variance!)** in plasma *N-acetylphenylalanine* (with $F = 80$), that 42 SNPs explain **$R^2 = 0.748$ (74.8% of variance!)** in *X-11538* (with $F = 36$), and that 41–51 SNPs explain **$R^2 = 0.434\text{--}0.485$** in polyunsaturated fatty acid phospholipids (with $F = 17\text{--}23$). No plasma metabolite has 91.2% of its phenotypic variance explained by 24 SNPs selected at $P < 5 \times 10^{-6}$, and moreover, $R^2 = 0.912$ with $k = 24$ SNPs in $N = 1,920\text{--}8,299$ mathematically implies $F = \frac{R^2(N - k - 1)}{k(1 - R^2)} = 818\text{ to }3,573$, directly contradicting the reported $F = 80$ in Table 3 and the statement in Line 69 that all $F$-statistics ranged from $10.1$ to $99.3$!
2. **Copy-Paste Error in Results Text (Section 3.2.2) Confusing *2-Hydroxyoctanoate* with *N-Acetylphenylalanine*:** In Section 3.2.2 ("Negative associations of metabolites with hypertension", Line 117), the authors write: *"The MR PRESSO method detected outliers in the analysis of N-acetylphenylalanine to hypertension, but the results remained significant after correction ($P = 1.42\text{e--06}$)."* In Table 2 (Line 82), $P = 1.42 \times 10^{-6}$ is the MR-PRESSO result for **2-hydroxyoctanoate**, whereas *N-acetylphenylalanine* is a positive association already reported in Section 3.2.1!
3. **Unidentified Data Provenance Across Redundant Metabolon Cohorts:** The three exposure cohorts (CLSA, Long et al., Shin et al.) all used the Metabolon platform and share hundreds of identical metabolites, yet the manuscript never specifies which of the three cohorts each of the 9 significant metabolites in Tables 2–3 came from, nor whether the same metabolite failed to replicate across the other two exposure cohorts in the study's own dataset!

### Assessment of Specific Conclusions
* **Claim 1: The genetic instruments for *N-acetylphenylalanine*, *X-11538*, and *1-dihomo-linolenoyl-GPC* explain $91.2\%$, $74.8\%$, and $48.5\%$ of phenotypic variance ($R^2$) with $F$-statistics of $80$, $36$, and $23$, respectively (Table 3):** `[Methodologically Flawed]`  
  These $R^2$ values are biologically and mathematically impossible. In GWASs of $N = 1,920\text{--}8,299$, 24 to 42 mostly *trans*-SNPs selected at a relaxed $P < 5 \times 10^{-6}$ threshold cannot explain $48.5\%\text{--}91.2\%$ of variance in a circulating metabolite, and the reported pairs of $(R^2, F)$ in Table 3 violate the mathematical definition of the $F$-statistic for every single row.
* **Claim 2: *1-Dihomo-linolenoyl-GPC*, *N-acetylphenylalanine*, and *X-11538* have robust causal effects on hypertension supported by discovery and replication:** `[Fragile]`  
  The authors selected 13–51 genome-wide SNPs per metabolite at a relaxed $P < 5 \times 10^{-6}$ threshold without restricting to *cis*-enzymatic/transporter loci or testing for colocalization. For polyunsaturated glycerophosphocholines (*1-dihomo-linolenoyl-GPC*), polygenic instruments at $P < 5 \times 10^{-6}$ capture broad lipid-metabolism loci (*FADS1/2*, *GCKR*, *APOE*) with extensive horizontal pleiotropy across cardiometabolic traits. Furthermore, the manuscript does not disclose whether *N-acetylphenylalanine* and *1-dihomo-linolenoyl-GPC* (which are measured in more than one of the three Metabolon cohorts analyzed) yielded concordant or null estimates in the other exposure cohort(s).
* **Claim 3: Six additional metabolites (*taurochenodeoxycholate*, *dihomo-linolenate*, *2-hydroxyoctanoate*, *1-docosapentaenoyl-GPC*, *gamma-glutamyl-alpha-lysine*, and *2-butenoylglycine*) causally influence hypertension:** `[Overstated]`  
  All six of these metabolites failed to reach even nominal significance ($P < 0.05$) in the UK Biobank replication cohort ($129,909$ cases and $354,689$ controls; Section 3.3, Line 122), and for 6 of the 9 metabolites in Table 2 (`Taurochenodeoxycholate`, `2-Hydroxyoctanoate`, `1-Dihomo-linolenoyl-GPC`, `Dihomo-linolenate`, `1-Docosapentaenoyl-GPC`, and `2-Butenoylglycine`), the MR-Egger slope is statistically non-significant ($P = 0.064\text{ to }0.408$).

---

## 3. Forensic Defect Inventory

### 1. [Critical] Mathematically Impossible $R^2$ Values ($R^2 = 0.912$) and Formula Contradictions in Table 3
* **Location:** Section 3.1 (Line 69) and Table 3 (Lines 91–102).
* **Defect:** Table 3 reports total variance explained ($R^2$) and $F$-statistics that are mutually contradictory and mathematically impossible:
  * For `N-acetylphenylalanine` ($\text{nSNP} = 24$ in Table 2), Table 3 reports **$R^2 = 0.912$** and **$F = 80$**. Under the standard formula $F = \frac{R^2 (N - k - 1)}{k (1 - R^2)}$, if $R^2 = 0.912$ and $k = 24$, then even for the smallest sample size ($N = 1,920$), $F = \frac{0.912 \times 1895}{24 \times 0.088} = 818.3$ (and for $N = 8,299$, $F = 3,573$), which differs by $10\text{--}45\times$ from the reported $F = 80$. Conversely, if the mean SNP $F$-statistic is $80$ in $N = 8,299$, then $R^2 = \frac{k F}{N - k - 1 + k F} \approx \frac{1920}{10194} = 0.188$, not $0.912$!
  * Similarly, for `X-11538` ($k = 42, R^2 = 0.748, F = 36$), `1-Dihomo-linolenoyl-GPC` ($k = 41, R^2 = 0.485, F = 23$), `Dihomo-linolenate` ($k = 51, R^2 = 0.434, F = 17$), and `1-Docosapentaenoyl-GPC` ($k = 45, R^2 = 0.436, F = 19$), the reported $R^2$ values ($43.4\%\text{--}91.2\%$) are inflated by $3\text{--}10\times$ (likely due to omitting the $2 \cdot \text{MAF}(1 - \text{MAF})$ heterozygosity factor or failing to standardize $\beta$ by the metabolite SD when computing $R^2$), and as a direct consequence, all statistical power values in Table 3 (`0.939` to `1.000`) are invalid because they were computed from these corrupted $R^2$ values.
* **Remediation:** Recompute per-SNP and total $R^2$ using standardized effect sizes ($\hat{R}_j^2 = \frac{\hat{\beta}_j^2}{\hat{\beta}_j^2 + N \cdot \text{SE}(\hat{\beta}_j)^2}$ or $\frac{F_j}{N - 2 + F_j}$), verify that total $R^2 < 1$, and recalculate all $F$-statistics and power estimates in Table 3.

### 2. [Major] Copy-Paste Error in Section 3.2.2 Confusing *2-Hydroxyoctanoate* with *N-Acetylphenylalanine*
* **Location:** Section 3.2.1 (Line 112), Section 3.2.2 (Line 117), and Table 2 (Lines 82, 84).
* **Defect:** In Section 3.2.1 (Positive associations, Line 112), the authors write: *"The MR PRESSO method detected outliers in the analysis of N-acetylphenylalanine to hypertension, but the results remained significant after correction (P = 3.51e–09)."* Then in Section 3.2.2 (Negative associations, Line 117), the authors paste the exact same sentence with a different $P$-value: *"The MR PRESSO method detected outliers in the analysis of N-acetylphenylalanine to hypertension, but the results remained significant after correction (P = 1.42e–06)."* Inspection of Table 2 (Line 82) shows that $P = 1.42 \times 10^{-6}$ ($\text{OR} = 0.948$) belongs to **2-Hydroxyoctanoate**, not *N-acetylphenylalanine*.
* **Remediation:** Correct `"N-acetylphenylalanine"` to `"2-hydroxyoctanoate"` in Section 3.2.2 (Line 117).

### 3. [Major] Missing Cohort Provenance and Cross-Cohort Consistency for Overlapping Metabolites
* **Location:** Section 2.1–2.2 (Lines 24–43) and Tables 1–3.
* **Defect:**
  1. The three exposure GWASs (CLSA, Long et al., Shin et al.) all quantified plasma/serum metabolites using the Metabolon platform and share substantial metabolite overlap. However, Tables 2 and 3 do not report which of the three exposure cohorts each of the 9 significant metabolites came from, nor whether the same metabolite was also tested in the other two cohorts (and if so, why it failed to reach significance there).
  2. Internal sample-size and trait-count inconsistencies appear between Table 1 and the text: Long et al. is listed as $N = 1,920$ in Table 1 (Line 31) but $N = 1,960$ in Section 2.2 (Line 40); Shin et al. is listed as $452$ metabolites in Table 1 (Line 32) and Section 2.5 (Line 61), but $486$ metabolites in Section 2.2 (Line 42).
* **Remediation:** Add a column to Tables 2 and 3 specifying the exact source cohort (CLSA, Long et al., or Shin et al.) and GWAS ID for each metabolite, report cross-cohort exposure consistency for metabolites present in more than one dataset, and reconcile the sample size ($1,920$ vs. $1,960$) and metabolite count ($452$ vs. $486$) discrepancies.

---

## 4. Quantitative Rubric Scoring

| Rubric Dimension | Score | Max | Forensic Justification |
| :--- | :---: | :---: | :--- |
| **1. Methodological & Statistical Rigor** | **0.5** | **3.5** | Mathematically impossible $R^2$ values ($R^2 = 0.912$ for 24 SNPs, $0.748$ for 42 SNPs) that contradict the reported $F$-statistics in Table 3 and invalidate the power calculations; reliance on 13–51 $P < 5 \times 10^{-6}$ genome-wide SNPs without *cis*/colocalization filtering. |
| **2. Claim-to-Evidence Alignment** | **0.5** | **2.5** | Six of the nine discovery metabolites fail to reach even $P < 0.05$ in the UK Biobank replication cohort ($N = 484,598$), yet all nine are highlighted in the Abstract as causal; cross-cohort consistency across the 3 Metabolon exposure studies is unreported. |
| **3. Data Integrity & Biological Plausibility** | **0.6** | **2.0** | Claiming that 24 common SNPs explain 91.2% of phenotypic variance in plasma *N-acetylphenylalanine* violates basic quantitative genetics; discussion provides almost no mechanistic analysis for 8 of the 9 reported metabolites (Lines 127–132). |
| **4. Reproducibility & Data Integrity** | **0.6** | **2.0** | Copy-paste error in Section 3.2.2 attributing *2-hydroxyoctanoate*'s MR-PRESSO result to *N-acetylphenylalanine*; inconsistent sample sizes ($1,920$ vs. $1,960$) and metabolite counts ($452$ vs. $486$); source cohort omitted from Tables 2–3. |
| **Scientific Core Score** | **1.6** | **8.0** | Sum of Rigor + Claims + Biology. |
| **Total Composite Score** | **2.2** | **10.0** | **Fundamentally Invalid** (22 / 100 equivalent). |
