# Review of FEXP_ANON_073

**Overall Score:** **2.4 / 10.0** (Fundamentally Invalid) | **Scientific Core Score:** **1.7 / 8.0**  
* **Score Breakdown:** Rigor: 0.5/3.5 | Claims: 0.4/2.5 | Biology: 0.8/2.0 | Reproducibility: 0.7/2.0

---

## 1. Blinded Metadata Perception
* **Perceived Subfield & Study Design:** Genetic Epidemiology / Multi-Omics Two-Sample Mendelian Randomization (MR) screening 6,742 exposure traits (immune cells, inflammatory cytokines, gut microbiota, circulating metabolites, and plasma proteins) against preeclampsia.
* **Data Sources:** Sardinian immune cell GWAS ($731$ traits, $N = 3,757$), Zhao et al. inflammatory protein GWAS ($91$ traits, $N = 14,824$), Dutch Microbiome Project ($412$ taxa/pathways, $N = 7,738$), KORA/TwinsUK metabolomics ($486$ metabolites, $N = 7,824$), CLSA metabolomics ($1,400$ metabolites/ratios, $N = 8,299$), INTERVAL plasma proteomics ($3,622$ proteins, $N = 3,301$), and FinnGen R9 preeclampsia (`O15_PRE_OR_ECLAMPSIA`, $7,212$ cases and $194,266$ controls).
* **Perceived Venue Tier:** Open-access clinical or general medical journal.

---

## 2. Executive Summary & Editorial Verdict

This manuscript performs an exploratory two-sample Mendelian randomization (MR) screen across five biological domains—731 immune cell phenotypes, 91 inflammatory proteins, 412 gut microbiome features, 1,886 metabolic traits ($486$ from KORA/TwinsUK and $1,400$ from CLSA), and 3,622 plasma proteins (a total of $6,742$ exposures)—against preeclampsia in FinnGen R9 ($7,212$ cases and $194,266$ controls). Using relaxed genome-wide instrument thresholds ($P < 1 \times 10^{-5}$ for gut microbiota and CLSA metabolites; $P < 5 \times 10^{-6}$ for immune cells, inflammatory factors, KORA metabolites, and plasma proteins), the authors define "Bonferroni-corrected statistical significance" as $P < 0.0125$ ($0.05 / 4$, dividing by the 4 MR estimators rather than the 6,742 tested exposures) and report 81 putative causal factors across the five domains.

**Editorial Verdict: Reject (Fundamentally Invalid).** The study's entire discovery set is a textbook multiple-testing artifact driven by a mathematically invalid Bonferroni denominator:
1. **Invalid Multiple-Testing Correction ($0.05 / 4$ Methods Instead of $6,742$ Exposures):** The authors test $6,742$ exposures but divide $\alpha = 0.05$ by $4$ (the number of sensitivity estimators run on each exposure: IVW, MR-Egger, weighted median, weighted mode) to set a threshold of $P < 0.0125$. Under the global null hypothesis across $6,742$ independent exposures, a threshold of $P < 0.0125$ yields an expected $6,742 \times 0.0125 = \mathbf{84.3}$ false-positive associations by pure chance—which matches the **81** associations reported by the authors ($17$ immune $+ 1$ inflammatory $+ 9$ microbiome $+ 6$ KORA $+ 16$ CLSA $+ 32$ proteins $= 81$). Not a single one of the 81 reported associations passes a true study-wide Bonferroni threshold ($P < 0.05 / 6,742 = 7.42 \times 10^{-6}$) or even domain-specific Benjamini-Hochberg FDR $< 0.05$.
2. **Reliance on Uncharacterized *Trans* Instruments ($P < 5 \times 10^{-6}$ / $10^{-5}$) and Sex-Combined Exposures for a Pregnancy-Specific Outcome:** Preeclampsia occurs exclusively in pregnant females, yet all exposure instruments are drawn from sex-combined adult cohorts at relaxed $P < 5 \times 10^{-6}$ or $P < 10^{-5}$ thresholds without *cis*-pQTL filtering or colocalization. For instance, the authors highlight plasma **ASTL (ovastacin)**—an oocyte-specific cortical granule protease—as a top druggable target for preeclampsia based on $P = 0.009$ from sex-combined plasma aptamer data ($N = 3,301$).
3. **Taxonomic Double-Counting in Microbiome Results:** Three of the 9 reported gut microbiome hits are the exact same nested lineage counted three times at the genus (*Bifidobacterium*), family (*Bifidobacteriaceae*), and order (*Bifidobacteriales*) levels (Line 68).

### Assessment of Specific Conclusions
* **Claim 1: The multi-omics MR screen identifies 81 statistically significant causal factors for preeclampsia after multiple-testing correction ($P < 0.0125 = 0.05/4$):** `[Methodologically Flawed]`  
  Dividing $\alpha = 0.05$ by the 4 estimators applied to the same exposure-outcome pair does not control the family-wise error rate (FWER) or false discovery rate (FDR) across the $6,742$ tested exposures. In every single omics domain, the number of claimed hits is at or below the expected false-positive count under the null at $P < 0.0125$: immune cells ($17$ observed vs. $9.1\text{--}36.6$ expected at $P < 0.0125\text{--}0.05$), inflammatory proteins ($1$ observed vs. $1.1$ expected), gut microbiota ($9$ observed [only $7$ non-nested] vs. $5.2$ expected), KORA metabolites ($6$ observed vs. $6.1$ expected), CLSA metabolites ($16$ observed vs. $17.5$ expected), and INTERVAL proteins ($32$ observed vs. $45.3$ expected).
* **Claim 2: Circulating plasma proteins ASTL ($OR = 0.84, P = 0.009$) and BIRC3 ($OR = 1.19, P < 0.001$) exhibit "strong causal evidence" as novel druggable targets for preeclampsia:** `[Overstated]`  
  Screening $3,622$ proteins in a small SOMAscan cohort ($N = 3,301$) using relaxed genome-wide (*cis* + *trans*) SNPs at $P < 5 \times 10^{-6}$ without colocalization or *cis*-pQTL restriction produces dozens of false positives at $P \sim 10^{-3}$. Neither ASTL ($P = 0.009$) nor BIRC3 survives proteome-wide FDR or Bonferroni correction ($P < 0.05 / 3,622 = 1.38 \times 10^{-5}$).
* **Claim 3: Gut *Bifidobacterium* ($OR \approx 0.82\text{--}0.83$), circulating guanidinoacetate ($OR = 1.15, P = 0.001$), and specific regulatory T/B cell traits causally influence preeclampsia risk:** `[Fragile]`  
  All of these associations rely on weak/polygenic instruments selected at $P < 1 \times 10^{-5}$ or $P < 5 \times 10^{-6}$ in modest discovery cohorts ($N = 3,757\text{--}8,299$) and have nominal $P$-values ($0.001\text{--}0.009$) that do not survive domain-wide multiple-testing adjustment.

---

## 3. Forensic Defect Inventory

### 1. [Critical] Invalid Multiple-Testing Correction ($P < 0.05 / 4$ Estimators Across $6,742$ Tested Exposures)
* **Location:** Section "Statistical Analysis and Sensitivity Analysis" (Line 42) and Discussion (Line 111).
* **Defect:** Line 42 states: *"We implemented a threshold of P < 0.0125 (0.05/4) to indicate statistical significance after correction. Meanwhile, a cutoff of P < 0.05, falling above the Bonferroni correction threshold, was designated as indicating a suggestive significant association."* Line 111 explains that $4$ is *"the number of MR methods used."* Furthermore, in Results Section 3.1 (Line 53), the authors state they selected traits that were *"nominally significant (P < 0.05) and exhibited consistent direction of effect across all sensitivity analyses"*.
  * Mathematically, running 4 algebraically correlated MR estimators on the same SNP set is not a multiple-testing correction across $M = 6,742$ exposures.
  * Across $6,742$ null exposures, testing at $P < 0.0125$ generates an expected $84.3$ false positives (and testing at $P < 0.05$ with a sign-concordance filter generates a similar number). The total number of hits reported across the entire paper is $81$, meaning the observed hit rate ($81 / 6,742 = 1.20\%$) is completely indistinguishable from pure Gaussian noise under the global null hypothesis.
* **Remediation:** Apply Benjamini-Hochberg FDR ($\text{FDR} < 0.05$) within each of the five omics domains (and Bonferroni $P < 7.42 \times 10^{-6}$ across all $6,742$ traits) and explicitly reclassify all associations with nominal $P < 0.05$ that fail domain-wide $\text{FDR} < 0.05$ as non-significant / exploratory.

### 2. [Major] Absence of *Cis*-pQTL Filtering and Colocalization in the Proteome Screen ($N = 3,301$)
* **Location:** Section "Data Sources" and "Genetic Instruments Selection" (Lines 32, 37) and Section "Causal Relationship Between Circulating Proteins and Preeclampsia" (Line 91).
* **Defect:** For the 3,622 plasma proteins from the INTERVAL SOMAscan cohort ($N = 3,301$), the authors select genome-wide SNPs at $P < 5 \times 10^{-6}$ without distinguishing *cis*-pQTLs (variants near the protein-coding gene) from *trans*-pQTLs (pleiotropic hubs such as *ABO*, *CFH*, *APOE*, *KLKB1*, and *VTN* that alter aptamer binding or levels of hundreds of unrelated proteins). In addition, no Bayesian colocalization (`coloc`) is performed to verify that any protein and preeclampsia share a causal variant.
* **Remediation:** Restrict the proteomic MR analysis to biologically validated *cis*-pQTLs ($\pm 1\text{ Mb}$ of the encoding gene) at $P < 5 \times 10^{-8}$ and perform colocalization (`PP.H4 > 0.80`) for any candidate protein target.

### 3. [Major] Taxonomic Redundancy in Gut Microbiome Hits and Sex-Mismatch Caveats
* **Location:** Section "Causal Relationship Between Gut Microbiome and Preeclampsia" (Line 68).
* **Defect:**
  1. Line 68 reports 9 causal microbiological traits, of which 3 are the genus *Bifidobacterium*, family *Bifidobacteriaceae*, and order *Bifidobacteriales* (all with identical $OR \approx 0.82\text{--}0.83$). In the Dutch Microbiome Project (Lopera-Maya et al.), *Bifidobacterium* accounts for nearly 100% of reads in *Bifidobacteriaceae* and *Bifidobacteriales*, so their relative abundances and genetic instruments are virtually identical. Counting them as 3 separate causal discoveries inflates the microbiome hit count.
  2. All exposure GWASs combine male and non-pregnant female participants, whereas preeclampsia is a female-only gestational phenotype; potential sex-specific genetic effects on immune, metabolic, and proteomic traits are not addressed.
* **Remediation:** Collapse nested redundant microbial clades into a single non-redundant signal and add a limitation discussing sex-combined exposure instruments applied to a pregnancy-specific outcome.

### 4. [Minor] Inconsistent Metabolite Counts (`1400` vs. `1440`) and Lack of Main-Text Summary Tables
* **Location:** Section "Data Sources" (Line 32) vs. Section "Causal Relationship Between Circulating Metabolites and Preeclampsia" (Lines 76, 83).
* **Defect:** Line 32 states that the CLSA dataset comprises `1091 plasma metabolites and 309 metabolite ratios` ($1,400$ total), and Line 83 and Figure 5 state `1400 metabolic traits`, but Line 76 states `1440 metabolites and ratios`. Furthermore, the manuscript contains no main-text tables summarizing the top associations, instrument counts ($n_{\text{SNP}}$), $F$-statistics, Cochran's $Q$, or MR-Egger intercepts.
* **Remediation:** Correct `1440` to `1400` on Line 76 and include a consolidated main-text table reporting the full quantitative statistics (including domain-wide FDR $q$-values) for the highlighted traits.

---

## 4. Quantitative Rubric Scoring

| Rubric Dimension | Score | Max | Forensic Justification |
| :--- | :---: | :---: | :--- |
| **1. Methodological & Statistical Rigor** | **0.5** | **3.5** | Fatal multiple-testing error: divides $\alpha = 0.05$ by 4 MR estimators ($P < 0.0125$) while testing $6,742$ exposures, yielding 81 hits that match the $\sim 84$ false positives expected by pure chance under the null; relies on $P < 5 \times 10^{-6}$ / $10^{-5}$ *trans* instruments without *cis*-filtering or colocalization. |
| **2. Claim-to-Evidence Alignment** | **0.4** | **2.5** | Claims "strong causal evidence" for 81 multi-omics factors (including ASTL at $P = 0.009$ and BIRC3 at $P \sim 10^{-3}$) when zero traits survive study-wide or domain-wide multiple-testing correction; triple-counts the nested *Bifidobacterium* clade. |
| **3. Data Integrity & Biological Plausibility** | **0.8** | **2.0** | Promoting oocyte zona-pellucida protease ASTL in sex-combined adult plasma aptamer data at $P = 0.009$ as a novel preeclampsia drug target lacks biological and genetic specificity. |
| **4. Reproducibility & Data Integrity** | **0.7** | **2.0** | Public data sources are cited, but main text lacks any quantitative tables, contains an internal count discrepancy (`1400` vs. `1440` CLSA traits), and does not provide analysis scripts. |
| **Scientific Core Score** | **1.7** | **8.0** | Sum of Rigor + Claims + Biology. |
| **Total Composite Score** | **2.4** | **10.0** | **Fundamentally Invalid** (24 / 100 equivalent). |
