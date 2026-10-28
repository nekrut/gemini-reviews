# Empirical Calibration & Literature Error Estimation (`N = 200` Study)

> **Executive Two-Paragraph Summary**
>
> Can an automated AI forensic reviewer detect fatal scientific flaws at the time of publication—and if we calibrate its sensitivity and specificity on ground-truth papers, what fraction of the broader computational biology and genomics literature is actually broken? To test this, we conducted a double-blinded forensic audit of 200 full-text manuscripts (stripped of titles, author names, affiliations, journals, and dates, and isolated from any post-publication commentary) across three cohorts: (A) 50 studies later retracted or formally refuted under post-publication scrutiny (e.g., contaminated cancer/placental/fetal microbiomes, flawed SARS-CoV-2 origin/clock claims, alignment-artifact selection scans, and confounded GWAS/clinical models), (B) 50 subfield- and genre-matched validated controls (43 replicated empirical discovery studies plus 7 foundational methods benchmarks), and (C) a stratified random "wild" sample of 100 unscrutinized papers across five subfields (20 each in molecular evolution, viral evolution, statistical genetics/GWAS, cancer/microbiome, and transcriptomics/ML). Using a standardized 7-pillar forensic rubric on a 1–10 scale, the double-blinded reviewer separated validated controls (Cohort B: mean 8.64, median 8.85; empirical controls alone: mean 8.64, median 9.00; 100% specificity at <5.5 and 96% at <6.5) from known invalid studies (Cohort A: mean 4.42, median 4.10) with an ROC-AUC of 0.969 (0.967 against empirical controls alone). On the 45 Cohort A papers whose flaws were internal to the manuscript's own methods, data, or tables (rather than hidden inside external consortium summary statistics like GIANT GWAS), the reviewer achieved 73.3% sensitivity (33/45) at a strict failure threshold (<5.0) and 86.7% sensitivity (39/45) for major flaws (<6.5), while paired comparison against unblinded reviews (r = 0.91) showed a mean +0.20-point shift when identifying metadata were visible (N=75 pairs; mean |Δ| = 0.70); the shift is +0.36 in low-prestige Cohort A and +0.33 in high-prestige Cohort B, so it is not prestige-specific (+0.15 excluding the version-mismatched ANON_26 pair).
>
> Applying this calibrated double-blinded reviewer to the 100 unscrutinized "wild" papers (Cohort C: mean 5.47, median 5.40) yielded a direct smoking-gun failure rate of 43.0% (±8.5% stratified 95% CI) at <5.0, 53.0% (±9.1%) at <5.5, and a major methodological flaw rate of 70.0% (±8.3%) at <6.5—corresponding to Rogan-Gladen sensitivity-adjusted prevalence estimates of 58.6%–65.2% for fatal invalidation and 79.8%–86.8% for major methodological flaws. Every wild paper flagged as failing contained concrete, human-verifiable defects directly in its text, equations, or tables: examples included main-text claims that reversed the sign of the survival and knockdown figures in the Results section, paper-mill templates that forgot to edit "Gastric cancer (GC)" out of a lung cancer study while discussing genes absent from their own formula, circular GWAS feature selection prior to cross-validation on the same individuals, omitted subject random intercepts `(1 | Subject_ID)` in repeated-measures `lme4` models producing pseudoreplicated p-values of 1e-17, and misreading HyPhy output table row indices (`1..11`) as amino acid coordinates. Failure rates in the wild literature followed a stark monotonic gradient across both discipline and citation tier: mechanistic, model-based fields (molecular evolution: mean 6.90, 5% fatal failure; viral evolution: mean 5.97, 35% failure) were substantially more rigorous than associative high-dimensional pipelines (statistical genetics: mean 5.37, 40% failure; cancer/microbiome: mean 4.78, 60% failure; transcriptomics/ML: mean 4.33, 75% fatal failure and 90% major flaws), while fatal failure rates tripled from highly cited papers (19.4% for ≥25 citations) to mid-cited (48.6% for 5–24 citations) and low-cited/uncited papers (58.8% fatal failure and 94.1% major flaws for 0–4 citations).

---

## 1. Study Protocol & Ground-Truth Selection Criteria

### 1.1 Three-Cohort Design (`50 + 50 + 100 = 200` Full-Text Manuscripts)
All 200 manuscripts were retrieved as full-text JATS XML / HTML (including all main-text sections, equations, tables, and figure captions) from PubMed Central (`Europe PMC`) across five core domains: **Molecular Evolution**, **Viral Evolution**, **Statistical Genetics / GWAS**, **Cancer & Microbiome**, and **Transcriptomics / Computational Biology ML**.

1. **Cohort A — Known Invalid / Refuted under Scrutiny ($N = 50$):**
   Every manuscript in Cohort A has an independent, citable post-publication documentary record (`retraction` or peer-reviewed `refutation`) establishing that its headline quantitative claim failed:
   * **Category A-I (Analytical / Data / Contamination Retractions):** Papers formally retracted in PMC due to methodological errors, batch/genotyping artifacts, train-test data leakage, or sequence contamination (excluding pure image-duplication fraud).
   * **Category A-II (Peer-Reviewed Forensic Refutations):** Named targets of peer-reviewed rebuttals ("Matters Arising", "Technical Comments", or forensic re-analyses) across low-biomass microbiomes (*Poore et al. 2020*, *Aykut et al. 2019*, *Aagaard et al. 2014*, *Mishra et al. 2021*, *Rackaityte et al. 2020*), viral origin/clock/recombination claims (*Amendola et al. 2022*, *Tang et al. 2020*, *Forster et al. 2020*, *Kumar et al. 2021*, *Xia 2020*, *Ji et al. 2020*, *Desingu et al. 2022*), alignment/sequencing-error positive selection scans (*Bakewell et al. 2007*, *Hughes et al. 2008*), and GWAS/ecological confounding (*Turchin et al. 2012*, *Berg & Coop 2014*, *Field et al. 2016*, *Lippert et al. 2017*, *Escobar et al. 2020*).
   * **Internal ($N=45$) vs. Upstream ($N=5$) Defect Locus:** Cohort A papers are stratified a priori into **Internal Flaws** ($N=45$, where the defect resides in the paper's own design, equations, statistical tests, or tables) vs. **Upstream Consortium / Mathematical Congruence Flaws** ($N=5$, e.g., where the paper's estimator is mathematically sound, but an external summary-statistic dataset it consumed—such as GIANT height GWAS—had unadjusted stratification only provable years later with individual-level UK Biobank genotypes).

2. **Cohort B — Subfield- & Genre-Matched Validated Controls ($N = 50$):**
   To prevent genre confounding (e.g., comparing noisy empirical biology papers in Cohort A against pure software/algorithm papers in Cohort B), Cohort B was matched by subfield and paper genre:
   * **43 Replicated Empirical Discovery & Forensic Benchmark Studies** (e.g., cross-cohort colorectal cancer metagenomics by *Wirbel et al. 2019*, *Thomas et al. 2019*, *Zeller et al. 2014*; low-biomass negative-control studies by *de Goffau et al. 2019*, *Salter et al. 2014*, *Kennedy et al. 2023*, *Gihawi et al. 2023*; within-sibship and biobank GWAS by *Howe et al. 2022*, *Yengo et al. 2022*, *Sohail et al. 2019*, *Berg et al. 2019*; 48-replicate RNA-seq and scRNA-seq pseudoreplication benchmarks by *Schurch et al. 2016*, *Squair et al. 2021*, *Zimmerman et al. 2021*; and replicated viral/evolutionary studies by *Starr et al. 2020*, *Martin et al. 2021*, *Korber et al. 2020*, *Pekar et al. 2022*, *Worobey et al. 2022*, *Dudas et al. 2017*, *Gire et al. 2014*, *Enard et al. 2016*).
   * **7 Foundational Calibrated Methods Benchmarks** (`MEME`, `BUSTED`, `HyPhy 2.5`, `IQ-TREE 2`, `Nextstrain`, `DESeq2`, `LDSC`).

3. **Cohort C — Stratified "Wild" Literature Sample ($N = 100$):**
   Drawn programmatically from Europe PMC Open Access (`seed = 20261027 / 20261030`) across the 5 subfields (**20 papers per subfield**, stratified across High $\ge 25$, Mid $5\text{--}24$, and Low $0\text{--}4$ citations), excluding all papers in Cohorts A and B and any retracted articles.

---

### 1.2 Double-Blinded De-Identification Protocol & Token Cost
* **Mandatory De-Identification (`ANON_01`–`ANON_200`):** Before running the 7-Pillar Audit, a deterministic preprocessor strips the manuscript Title, Author Names, Affiliations, Correspondence headers, Journal Name, Publication Year, DOI, and PMCID/PMID (`[REDACTED FOR BLINDED REVIEW]`). The reviewer operates in an air-gapped workspace without web search (`search_web` disabled) and evaluates only the internal methodological, mathematical, statistical, biological, and table merits at $t_0$.
* **Empirical Token & API Cost Footprint ($N = 200$):**
  * **Rubric & System Prompt ([`REVIEW_TEMPLATE.md`](REVIEW_TEMPLATE.md)):** $\sim 2,400$ tokens ($9.7\text{ KB}$).
  * **Extracted Full-Text Manuscript + Tables:** Mean $\sim 12,200$ tokens ($48.7\text{ KB}$; median $11,000$ tokens).
  * **Reasoning + Written 3-Section Review:** Mean $\sim 4,900$ tokens ($\sim 2,000$ thinking $+ 2,900$ output tokens / $11.5\text{ KB}$).
  * **Total Cost per Review:** **$\sim 19,500$ tokens** ($\approx \$0.035\text{--}\$0.07$ per paper in stateless Pro API mode, or $\sim \$0.10$ per paper in multi-paper cached agentic loops).

---

# Empirical Results: Power of Agentic Peer Review & Literature Error Estimation

## 1. Executive Summary

Across **75 full-text manuscripts** evaluated with identifying metadata visible (`reviews_identified/`) using the standardized 7-Pillar Forensic Review Protocol ([`REVIEW_TEMPLATE.md`](REVIEW_TEMPLATE.md)):

| Metric / Estimator | Cohort A: Known Invalid / Refuted ($N=25$) | Cohort B: Validated Controls ($N=25$) | Cohort C: Stratified Wild Sample ($N=25$) |
| :--- | :---: | :---: | :---: |
| **Mean Overall Score (/10.0)** | **4.62** ($\pm 2.07$) | **8.58** ($\pm 0.63$) | **5.36** ($\pm 2.02$) |
| **Median Score (IQR)** | **4.1** ($3.1\text{--}5.7$) | **8.6** ($8.1\text{--}9.0$) | **5.3** ($3.8\text{--}7.5$) |
| **Score Range** | $1.8 \text{ -- } 8.3$ | $7.4 \text{ -- } 9.5$ | $1.8 \text{ -- } 8.8$ |
| **Mean Methodological Rigor (/3.5)** | 1.32 | 2.96 | 1.61 |
| **Mean Claim Support (/2.5)** | 1.06 | 2.17 | 1.30 |
| **Mean Biology & Integrity (/2.0)** | 1.03 | 1.76 | 1.25 |
| **Mean Reproducibility (/2.0)** | 1.21 | 1.70 | 1.21 |
| **Strict Failure Rate ($S < 5.0$)** | **68.0%** ($17/25$) | **0.0%** ($0/25$) | **44.0%** ($11/25$) |
| **Major Flaw Rate ($S < 6.5$)** | **80.0%** ($20/25$) | **0.0%** ($0/25$) | **72.0%** ($18/25$) |

---

## 2. Diagnostic Classifier Calibration (Cohort A vs. Cohort B)

* **ROC-AUC (Cohort B > Cohort A):** **$0.9560$** (Mann-Whitney $U = 597.5 / 625$, two-sided $p = 2.8 \times 10^{-8}$) (de-identified phase-1 reviews: ROC-AUC = 0.927).
* **Zero False-Positive Rate on Validated Controls ($\widehat{\text{Sp}} = 100\%$):** Every single paper in Cohort B ($25/25$) scored $\ge 7.4/10.0$ (`Strong / Sound` or `Exemplary`). Even though the reviewer identifies constructive methodological caveats in every paper, it never misclassifies a sound, validated paper as `Flawed / Overstated` ($<5.0$) or `Mixed / Salvageable` ($<7.0$).
* **What $t_0$ Single-Paper Forensic Review Catches vs. Misses in Cohort A:**
  * **Internally Detectable Flaws ($20/20 = 100\%$ caught as $<6.5$; $17/20 = 85\%$ scored $<5.0$):** Whenever the flaw resides in the manuscript's own study design, equations, statistical tests, ecological/batch confounding, circular feature selection, or table inconsistencies (`A01`–`A06`, `A08`–`A10`, `A12`–`A18`, `A20`–`A23`), the blinded agentic review independently flags the exact fatal defect from the $t_0$ text and tables alone.
  * **Upstream Consortium / Deep Mathematical Non-Identifiability Flaws ($5/25$ scored $\ge 7.0$):** The 5 Cohort A papers that scored $\ge 7.0$ (`A07` van Dorp 2020, `A11` Field 2016 SDS, `A19` Nejman 2020, `A24` Berg & Coop 2014, `A25` Rabosky 2014 BAMM) illustrate the exact theoretical boundary of single-paper $t_0$ review:
    1. **Upstream Summary-Statistic Corruption (`A11` Field 2016, `A24` Berg & Coop 2014):** Both papers developed mathematically sound population-genetic estimators but applied them to external GIANT consortium GWAS summary statistics that contained hidden population stratification—a flaw that could only be proven in 2019 using individual-level UK Biobank genotypes (`B17`, `B18`).
    2. **Cross-Lab Database Artifacts (`A07` van Dorp 2020):** Identifying that specific recurrent mutations in early GISAID genomes were lab-specific sequencing errors required cross-referencing submitting-lab metadata across the global phylogeny (`B10` Turakhia et al. 2020).
    3. **Infinite Congruence-Class Non-Identifiability (`A25` Rabosky 2014):** Proving that extant time-calibrated phylogenies cannot uniquely identify diversification histories ($\lambda(t), \mu(t)$) required the mathematical equivalence-class theorem proved six years later by Louca & Pennell (2020).

---

## 3. Sample Estimators of Flawed Research in the Wild (Cohort C)

Because $\widehat{\text{Sp}} = 1.000$ ($25/25$) across all cutoffs up to $7.0$, the Rogan-Gladen prevalence estimator simplifies to $\hat{\pi}_{\text{true}} = \min(1, \hat{p}_{\text{obs}} / \widehat{\text{Se}})$, and the raw observed rate $\hat{p}_{\text{obs}}$ is a lower bound only if true Sp = 1 (exact 95% CI for Sp with 25/25: [86.3%, 100%]):

| Failure Threshold Definition | Calibration Sensitivity ($\widehat{\text{Se}}$) | Calibration Specificity ($\widehat{\text{Sp}}$) | Wild Observed Failure Rate ($\hat{p}_{\text{obs}}$) | Rogan-Gladen True Prevalence ($\hat{\pi}_{\text{true}}$) |
| :--- | :---: | :---: | :---: | :---: |
| **Strict Fatal Invalidation ($S < 5.0$)** | $68.0\%$ ($17/25$) | $100.0\%$ ($25/25$) | **$44.0\%$ ($11/25$)** | **$64.7\%$** |
| **Substantive Failure ($S < 5.5$)** | $72.0\%$ ($18/25$) | $100.0\%$ ($25/25$) | **$52.0\%$ ($13/25$)** | **$72.2\%$** |
| **Major Methodological Flaw ($S < 6.0$)** | $76.0\%$ ($19/25$) | $100.0\%$ ($25/25$) | **$68.0\%$ ($17/25$)** | **$89.5\%$** |
| **Any Major Pillar Violation ($S < 6.5$)** | $80.0\%$ ($20/25$) | $100.0\%$ ($25/25$) | **$72.0\%$ ($18/25$)** | **$90.0\%$** |

### Stratified Breakdown of Cohort C (Wild Literature Sample)

#### A. By Subfield ($n = 5$ per stratum)
| Subfield Stratum | Mean Score | Strict Failure ($S < 5.0$) | Major Flaw ($S < 7.0$) | Primary Smoking-Gun Failure Modes Observed |
| :--- | :---: | :---: | :---: | :--- |
| **Molecular Evolution** | **7.52** | $0/5$ ($0\%$) | $2/5$ ($40\%$) | Uncalibrated AlphaFold RMSD comparisons on ancestral reconstructions (`C10`); unadjusted IDR enrichment (`C09`) |
| **Viral Evolution** | **6.32** | $0/5$ ($0\%$) | $3/5$ ($60\%$) | Cross-reactivity & overclaimed spillover frequency from $2/2000$ low-titer sera (`C04`); statistical power failure (`C05`) |
| **Statistical Genetics / GWAS** | **5.68** | $2/5$ ($40\%$) | $3/5$ ($60\%$) | **In-sample GWAS feature-selection data leakage** before cross-validation (`C18`, `C19`); unadjusted pleiotropy p-values (`C20`) |
| **Cancer & Microbiome** | **3.78** | $4/5$ ($80\%$) | $5/5$ ($100\%$) | Cross-BioProject batch confounding (`C12`), antibiotic confounding in MDR-TB (`C13`), cage pseudoreplication (`C15`), ML leakage (`C11`) |
| **Transcriptomics & CompBio ML** | **3.52** | $5/5$ ($100\%$) | $5/5$ ($100\%$) | Direct text-vs-table sign reversals (`C25`), circular feature selection on tiny GEO cohorts (`C21`, `C24`), pseudoreplication (`C22`, `C23`) |

#### B. By Citation Velocity Tier
| Citation Tier | $N$ | Mean Score | Strict Failure ($S < 5.0$) | Major Flaw ($S < 7.0$) | Interpretation |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **High ($\ge 25$ citations)** | 9 | **6.52** | $3/9$ (**33.3%**) | $3/9$ (**33.3%**) | Strong bimodal split: rigorous high-impact studies (`C01`, `C02`, `C06`, `C07`, `C16`, `C17` scoring $7.5\text{{--}}8.8$) vs. heavily cited flawed microbiome/ML papers (`C11`, `C12`, `C21` scoring $2.7\text{{--}}4.6$) |
| **Mid ($5\text{{--}}24$ citations)** | 10 | **4.69** | $6/10$ (**60.0%**) | $9/10$ (**90.0%**) | High prevalence of circular ML pipelines, unadjusted confounding, and ecological overreach |
| **Low ($0\text{{--}}4$ citations)** | 6 | **4.75** | $2/6$ (**33.3%**) | $6/6$ (**100.0%**) | None of the uncited/low-cited wild papers met the `Strong / Sound` ($\ge 7.0$) threshold |

---

## 4. Complete 75-Paper Ledger & Links to Individual Reviews

### Cohort A: Known Invalid / Refuted ($N = 25$)
| ID | PMCID | Venue (Year) | Domain | Rigor | Claims | Bio | Repro | **Overall** | Tier | Review |
| :---: | :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :---: |
| `A01` | `PMC9404229` | *Environ Res* (2022) | Viral Evolution | 1.2/3.5 | 0.8/2.5 | 0.7/2.0 | 1.4/2.0 | **4.1** | Flawed / Overstated | [Review](calibration/reviews_identified/PMC9404229.md) |
| `A02` | `PMC7107875` | *Natl Sci Rev* (2020) | Viral Evolution | 1.2/3.5 | 1.0/2.5 | 1.1/2.0 | 1.2/2.0 | **4.5** | Flawed / Overstated | [Review](calibration/reviews_identified/PMC7107875.md) |
| `A03` | `PMC7196762` | *Proc Natl Acad Sci U S A* (2020) | Viral Evolution | 0.8/3.5 | 0.6/2.5 | 0.7/2.0 | 1.1/2.0 | **3.2** | Flawed / Overstated | [Review](calibration/reviews_identified/PMC7196762.md) |
| `A04` | `PMC7184484` | *Mol Biol Evol* (2020) | Molecular Evolution | 0.7/3.5 | 0.5/2.5 | 0.6/2.0 | 1.2/2.0 | **3.0** | Flawed / Overstated | [Review](calibration/reviews_identified/PMC7184484.md) |
| `A05` | `PMC7138088` | *J Med Virol* (2020) | Molecular Evolution | 0.4/3.5 | 0.3/2.5 | 0.3/2.0 | 0.8/2.0 | **1.8** | Fundamentally Invalid | [Review](calibration/reviews_identified/PMC7138088.md) |
| `A06` | `PMC9349972` | *J Med Virol* (2022) | Viral Evolution | 0.6/3.5 | 0.6/2.5 | 0.6/2.0 | 0.7/2.0 | **2.5** | Fundamentally Invalid | [Review](calibration/reviews_identified/PMC9349972.md) |
| `A07` | `PMC7199730` | *Infect Genet Evol* (2020) | Viral Evolution | 2.5/3.5 | 2.0/2.5 | 1.6/2.0 | 1.8/2.0 | **7.9** | Strong / Sound | [Review](calibration/reviews_identified/PMC7199730.md) |
| `A08` | `PMC7428442` | *Sci Total Environ* (2021) | Viral Epidemiology | 0.9/3.5 | 0.7/2.5 | 1.0/2.0 | 1.0/2.0 | **3.6** | Flawed / Overstated | [Review](calibration/reviews_identified/PMC7428442.md) |
| `A09` | `PMC8529295` | *Tumori* (2021) | Viral Epidemiology | 0.7/3.5 | 0.5/2.5 | 0.6/2.0 | 0.8/2.0 | **2.6** | Fundamentally Invalid | [Review](calibration/reviews_identified/PMC8529295.md) |
| `A10` | `PMC7276232` | *J Biomed Sci* (2020) | Viral Evolution | 0.9/3.5 | 0.7/2.5 | 0.9/2.0 | 1.0/2.0 | **3.5** | Flawed / Overstated | [Review](calibration/reviews_identified/PMC7276232.md) |
| `A11` | `PMC5182071` | *Science* (2016) | Population Genomics | 2.9/3.5 | 1.9/2.5 | 1.6/2.0 | 1.7/2.0 | **8.1** | Strong / Sound | [Review](calibration/reviews_identified/PMC5182071.md) |
| `A12` | `PMC7267315` | *Int J Clin Pract* (2020) | Viral Epidemiology | 0.4/3.5 | 0.4/2.5 | 0.6/2.0 | 0.7/2.0 | **2.1** | Fundamentally Invalid | [Review](calibration/reviews_identified/PMC7267315.md) |
| `A13` | `PMC7375454` | *J Hum Genet* (2020) | Viral Genomics | 0.7/3.5 | 0.7/2.5 | 0.7/2.0 | 1.0/2.0 | **3.1** | Flawed / Overstated | [Review](calibration/reviews_identified/PMC7375454.md) |
| `A14` | `PMC7247990` | *Int J Infect Dis* (2020) | Viral Epidemiology | 0.4/3.5 | 0.8/2.5 | 0.6/2.0 | 0.7/2.0 | **2.5** | Fundamentally Invalid | [Review](calibration/reviews_identified/PMC7247990.md) |
| `A15` | `PMC7395502` | *Proc Natl Acad Sci U S A* (2020) | Epidemiology / Stats | 1.2/3.5 | 1.2/2.5 | 1.0/2.0 | 1.4/2.0 | **4.8** | Flawed / Overstated | [Review](calibration/reviews_identified/PMC7395502.md) |
| `A16` | `PMC7500457` | *Nature* (2020) | Cancer Microbiome | 0.8/3.5 | 0.6/2.5 | 0.7/2.0 | 1.2/2.0 | **3.3** | Flawed / Overstated | [Review](calibration/reviews_identified/PMC7500457.md) |
| `A17` | `PMC6858566` | *Nature* (2019) | Cancer Microbiome | 1.1/3.5 | 1.0/2.5 | 1.1/2.0 | 0.9/2.0 | **4.1** | Flawed / Overstated | [Review](calibration/reviews_identified/PMC6858566.md) |
| `A18` | `PMC9567272` | *Cell* (2022) | Cancer Microbiome | 1.2/3.5 | 1.0/2.5 | 0.8/2.0 | 1.4/2.0 | **4.4** | Flawed / Overstated | [Review](calibration/reviews_identified/PMC9567272.md) |
| `A19` | `PMC7757858` | *Science* (2020) | Cancer Microbiome | 2.5/3.5 | 2.0/2.5 | 1.7/2.0 | 1.8/2.0 | **8.0** | Strong / Sound | [Review](calibration/reviews_identified/PMC7757858.md) |
| `A20` | `PMC5617305` | *Proc Natl Acad Sci U S A* (2017) | Statistical Genetics | 1.6/3.5 | 1.1/2.5 | 1.4/2.0 | 1.1/2.0 | **5.2** | Mixed / Salvageable | [Review](calibration/reviews_identified/PMC5617305.md) |
| `A21` | `PMC6613792` | *Nat Med* (2019) | Statistical Genetics | 1.5/3.5 | 1.3/2.5 | 1.3/2.0 | 1.6/2.0 | **5.7** | Mixed / Salvageable | [Review](calibration/reviews_identified/PMC6613792.md) |
| `A22` | `PMC3261167` | *PLoS One* (2012) | Statistical Genetics | 1.3/3.5 | 1.2/2.5 | 1.3/2.0 | 1.0/2.0 | **4.8** | Flawed / Overstated | [Review](calibration/reviews_identified/PMC3261167.md) |
| `A23` | `PMC3480734` | *Nat Genet* (2012) | Population Genomics | 2.0/3.5 | 1.5/2.5 | 1.5/2.0 | 1.4/2.0 | **6.4** | Mixed / Salvageable | [Review](calibration/reviews_identified/PMC3480734.md) |
| `A24` | `PMC4125079` | *PLoS Genet* (2014) | Population Genomics | 2.8/3.5 | 2.1/2.5 | 1.7/2.0 | 1.7/2.0 | **8.3** | Strong / Sound | [Review](calibration/reviews_identified/PMC4125079.md) |
| `A25` | `PMC3935878` | *PLoS One* (2014) | Macroevolution / Stats | 2.7/3.5 | 2.0/2.5 | 1.6/2.0 | 1.7/2.0 | **8.0** | Strong / Sound | [Review](calibration/reviews_identified/PMC3935878.md) |

### Cohort B: Validated / Stress-Tested Controls ($N = 25$)
| ID | PMCID | Venue (Year) | Domain | Rigor | Claims | Bio | Repro | **Overall** | Tier | Review |
| :---: | :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :---: |
| `B01` | `PMC8421097` | *Cell* (2021) | Viral Evolution | 3.1/3.5 | 2.0/2.5 | 1.7/2.0 | 1.8/2.0 | **8.6** | Strong / Sound | [Review](calibration/reviews_identified/PMC8421097.md) |
| `B02` | `PMC8135569` | *Mol Biol Evol* (2021) | Viral Evolution | 2.6/3.5 | 1.9/2.5 | 1.4/2.0 | 1.6/2.0 | **7.5** | Strong / Sound | [Review](calibration/reviews_identified/PMC8135569.md) |
| `B03` | `PMC7990310` | *PLoS Biol* (2021) | Viral Evolution | 2.6/3.5 | 1.9/2.5 | 1.7/2.0 | 1.7/2.0 | **7.9** | Strong / Sound | [Review](calibration/reviews_identified/PMC7990310.md) |
| `B04` | `PMC7332439` | *Cell* (2020) | Viral Evolution | 2.6/3.5 | 2.1/2.5 | 1.8/2.0 | 1.6/2.0 | **8.1** | Strong / Sound | [Review](calibration/reviews_identified/PMC7332439.md) |
| `B05` | `PMC7810038` | *Science* (2020) | Viral Evolution | 3.1/3.5 | 2.1/2.5 | 1.8/2.0 | 1.5/2.0 | **8.5** | Strong / Sound | [Review](calibration/reviews_identified/PMC7810038.md) |
| `B06` | `PMC9348752` | *Science* (2022) | Viral Evolution | 3.1/3.5 | 2.1/2.5 | 1.8/2.0 | 1.8/2.0 | **8.8** | Strong / Sound | [Review](calibration/reviews_identified/PMC9348752.md) |
| `B07` | `PMC9348750` | *Science* (2022) | Viral Epidemiology | 2.8/3.5 | 2.1/2.5 | 1.8/2.0 | 1.8/2.0 | **8.5** | Strong / Sound | [Review](calibration/reviews_identified/PMC9348750.md) |
| `B08` | `PMC8942855` | *Nature* (2022) | Viral Evolution | 3.0/3.5 | 2.2/2.5 | 1.7/2.0 | 1.7/2.0 | **8.6** | Strong / Sound | [Review](calibration/reviews_identified/PMC8942855.md) |
| `B09` | `PMC7610519` | *Nat Microbiol* (2020) | Viral Genomics | 2.8/3.5 | 2.3/2.5 | 1.8/2.0 | 1.6/2.0 | **8.5** | Strong / Sound | [Review](calibration/reviews_identified/PMC7610519.md) |
| `B10` | `PMC7721162` | *PLoS Genet* (2020) | Viral Genomics | 3.2/3.5 | 2.3/2.5 | 1.9/2.0 | 1.9/2.0 | **9.3** | Exemplary | [Review](calibration/reviews_identified/PMC7721162.md) |
| `B11` | `PMC8128288` | *Science* (2021) | Viral Epidemiology | 3.2/3.5 | 2.3/2.5 | 1.8/2.0 | 1.6/2.0 | **8.9** | Strong / Sound | [Review](calibration/reviews_identified/PMC8128288.md) |
| `B12` | `PMC8139423` | *Science* (2021) | Viral Epidemiology | 3.0/3.5 | 2.1/2.5 | 1.9/2.0 | 1.6/2.0 | **8.6** | Strong / Sound | [Review](calibration/reviews_identified/PMC8139423.md) |
| `B13` | `PMC9161372` | *Science* (2022) | Viral Evolution | 2.9/3.5 | 2.1/2.5 | 1.7/2.0 | 1.6/2.0 | **8.3** | Strong / Sound | [Review](calibration/reviews_identified/PMC9161372.md) |
| `B14` | `PMC10506532` | *Virus Evol* (2023) | Viral Evolution | 3.3/3.5 | 2.4/2.5 | 1.9/2.0 | 1.9/2.0 | **9.5** | Exemplary | [Review](calibration/reviews_identified/PMC10506532.md) |
| `B15` | `PMC5712493` | *Nature* (2017) | Viral Evolution | 3.1/3.5 | 2.3/2.5 | 1.9/2.0 | 1.7/2.0 | **9.0** | Exemplary | [Review](calibration/reviews_identified/PMC5712493.md) |
| `B16` | `PMC10653788` | *mBio* (2023) | Cancer Microbiome | 3.4/3.5 | 2.4/2.5 | 1.9/2.0 | 1.6/2.0 | **9.3** | Exemplary | [Review](calibration/reviews_identified/PMC10653788.md) |
| `B17` | `PMC6428571` | *Elife* (2019) | Population Genomics | 3.3/3.5 | 2.4/2.5 | 1.8/2.0 | 1.9/2.0 | **9.4** | Exemplary | [Review](calibration/reviews_identified/PMC6428571.md) |
| `B18` | `PMC6428572` | *Elife* (2019) | Population Genomics | 3.3/3.5 | 2.4/2.5 | 1.9/2.0 | 1.8/2.0 | **9.4** | Exemplary | [Review](calibration/reviews_identified/PMC6428572.md) |
| `B19` | `PMC3395634` | *PLoS Genet* (2012) | Molecular Evolution | 3.3/3.5 | 2.3/2.5 | 1.8/2.0 | 1.6/2.0 | **9.0** | Exemplary | [Review](calibration/reviews_identified/PMC3395634.md) |
| `B20` | `PMC4408417` | *Mol Biol Evol* (2015) | Molecular Evolution | 3.2/3.5 | 2.2/2.5 | 1.7/2.0 | 1.7/2.0 | **8.8** | Strong / Sound | [Review](calibration/reviews_identified/PMC4408417.md) |
| `B21` | `PMC8204705` | *Mol Biol Evol* (2020) | Molecular Evolution | 2.5/3.5 | 2.0/2.5 | 1.7/2.0 | 1.9/2.0 | **8.1** | Strong / Sound | [Review](calibration/reviews_identified/PMC8204705.md) |
| `B22` | `PMC7182206` | *Mol Biol Evol* (2020) | Molecular Evolution | 2.5/3.5 | 2.0/2.5 | 1.5/2.0 | 1.4/2.0 | **7.4** | Strong / Sound | [Review](calibration/reviews_identified/PMC7182206.md) |
| `B23` | `PMC6247931` | *Bioinformatics* (2018) | Viral Genomics | 2.5/3.5 | 2.0/2.5 | 1.6/2.0 | 1.8/2.0 | **7.9** | Strong / Sound | [Review](calibration/reviews_identified/PMC6247931.md) |
| `B24` | `PMC4302049` | *Genome Biol* (2014) | Transcriptomics / Stats | 3.2/3.5 | 2.3/2.5 | 1.8/2.0 | 1.9/2.0 | **9.2** | Exemplary | [Review](calibration/reviews_identified/PMC4302049.md) |
| `B25` | `PMC8922736` | *Genome Biol* (2022) | Transcriptomics / Stats | 2.3/3.5 | 2.0/2.5 | 1.6/2.0 | 1.5/2.0 | **7.4** | Strong / Sound | [Review](calibration/reviews_identified/PMC8922736.md) |

### Cohort C: Stratified Wild Literature Sample ($N = 25$)
| ID | PMCID | Venue (Year) | Domain | Cite Tier (Cites) | Rigor | Claims | Bio | Repro | **Overall** | Tier | Review |
| :---: | :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- | :---: |
| `C01` | `PMC11305400` | *Cell Rep* (2024) | Viral Evolution | High (>=25) (40) | 2.5/3.5 | 1.9/2.5 | 1.7/2.0 | 1.6/2.0 | **7.7** | Strong / Sound | [Review](calibration/reviews_identified/PMC11305400.md) |
| `C02` | `PMC12313522` | *Nat Microbiol* (2025) | Viral Evolution | High (>=25) (49) | 2.5/3.5 | 1.9/2.5 | 1.7/2.0 | 1.6/2.0 | **7.7** | Strong / Sound | [Review](calibration/reviews_identified/PMC12313522.md) |
| `C03` | `PMC8011692` | *Emerg Microbes Infect* (2021) | Viral Evolution | Mid (5-24) (15) | 1.5/3.5 | 1.0/2.5 | 1.2/2.0 | 1.4/2.0 | **5.1** | Mixed / Salvageable | [Review](calibration/reviews_identified/PMC8011692.md) |
| `C04` | `PMC11682804` | *Emerg Infect Dis* (2025) | Viral Evolution | Mid (5-24) (14) | 1.9/3.5 | 1.3/2.5 | 1.5/2.0 | 1.1/2.0 | **5.8** | Mixed / Salvageable | [Review](calibration/reviews_identified/PMC11682804.md) |
| `C05` | `PMC11281702` | *Viruses* (2024) | Viral Evolution | Low (0-4) (0) | 1.4/3.5 | 1.4/2.5 | 1.3/2.0 | 1.2/2.0 | **5.3** | Mixed / Salvageable | [Review](calibration/reviews_identified/PMC11281702.md) |
| `C06` | `PMC7105384` | *Elife* (2020) | Molecular Evolution | High (>=25) (42) | 2.7/3.5 | 2.2/2.5 | 1.8/2.0 | 1.6/2.0 | **8.3** | Strong / Sound | [Review](calibration/reviews_identified/PMC7105384.md) |
| `C07` | `PMC10431346` | *Virus Evol* (2022) | Molecular Evolution | High (>=25) (68) | 3.0/3.5 | 2.3/2.5 | 1.8/2.0 | 1.7/2.0 | **8.8** | Strong / Sound | [Review](calibration/reviews_identified/PMC10431346.md) |
| `C08` | `PMC11040004` | *Nucleic Acids Res* (2024) | Molecular Evolution | Mid (5-24) (11) | 2.9/3.5 | 2.1/2.5 | 1.8/2.0 | 1.8/2.0 | **8.6** | Strong / Sound | [Review](calibration/reviews_identified/PMC11040004.md) |
| `C09` | `PMC11431564` | *Genes (Basel)* (2024) | Molecular Evolution | Mid (5-24) (6) | 1.9/3.5 | 1.4/2.5 | 1.4/2.0 | 1.2/2.0 | **5.9** | Mixed / Salvageable | [Review](calibration/reviews_identified/PMC11431564.md) |
| `C10` | `PMC11228553` | *Front Bioinform* (2024) | Molecular Evolution | Low (0-4) (0) | 1.9/3.5 | 1.5/2.5 | 1.2/2.0 | 1.4/2.0 | **6.0** | Mixed / Salvageable | [Review](calibration/reviews_identified/PMC11228553.md) |
| `C11` | `PMC10901987` | *Front Microbiol* (2024) | Cancer & Microbiome | High (>=25) (47) | 1.3/3.5 | 1.1/2.5 | 1.0/2.0 | 1.2/2.0 | **4.6** | Flawed / Overstated | [Review](calibration/reviews_identified/PMC10901987.md) |
| `C12` | `PMC6680985` | *Microorganisms* (2019) | Cancer & Microbiome | High (>=25) (36) | 0.9/3.5 | 0.7/2.5 | 0.9/2.0 | 1.1/2.0 | **3.6** | Flawed / Overstated | [Review](calibration/reviews_identified/PMC6680985.md) |
| `C13` | `PMC9509681` | *Infect Drug Resist* (2022) | Cancer & Microbiome | Mid (5-24) (9) | 0.4/3.5 | 0.4/2.5 | 0.5/2.0 | 0.5/2.0 | **1.8** | Fundamentally Invalid | [Review](calibration/reviews_identified/PMC9509681.md) |
| `C14` | `PMC9008261` | *Front Cell Infect Microbiol* (2022) | Cancer & Microbiome | Mid (5-24) (21) | 0.8/3.5 | 0.7/2.5 | 1.0/2.0 | 0.9/2.0 | **3.4** | Flawed / Overstated | [Review](calibration/reviews_identified/PMC9008261.md) |
| `C15` | `PMC12354945` | *Cancer Res Commun* (2025) | Cancer & Microbiome | Low (0-4) (3) | 1.6/3.5 | 1.4/2.5 | 1.2/2.0 | 1.3/2.0 | **5.5** | Mixed / Salvageable | [Review](calibration/reviews_identified/PMC12354945.md) |
| `C16` | `PMC7617604` | *N Engl J Med* (2025) | Statistical Genetics | High (>=25) (66) | 2.5/3.5 | 2.0/2.5 | 1.6/2.0 | 1.4/2.0 | **7.5** | Strong / Sound | [Review](calibration/reviews_identified/PMC7617604.md) |
| `C17` | `PMC12120081` | *Nat Commun* (2025) | Statistical Genetics | High (>=25) (26) | 2.5/3.5 | 2.0/2.5 | 1.6/2.0 | 1.7/2.0 | **7.8** | Strong / Sound | [Review](calibration/reviews_identified/PMC12120081.md) |
| `C18` | `PMC11711298` | *Plant Genome* (2025) | Statistical Genetics | Mid (5-24) (6) | 0.8/3.5 | 0.9/2.5 | 1.2/2.0 | 0.9/2.0 | **3.8** | Flawed / Overstated | [Review](calibration/reviews_identified/PMC11711298.md) |
| `C19` | `PMC11610249` | *Front Plant Sci* (2024) | Statistical Genetics | Mid (5-24) (7) | 1.0/3.5 | 0.9/2.5 | 1.0/2.0 | 0.9/2.0 | **3.8** | Flawed / Overstated | [Review](calibration/reviews_identified/PMC11610249.md) |
| `C20` | `PMC12409340` | *Int J Chron Obstruct Pulmon Dis* (2025) | Statistical Genetics | Low (0-4) (1) | 1.7/3.5 | 1.4/2.5 | 1.3/2.0 | 1.1/2.0 | **5.5** | Mixed / Salvageable | [Review](calibration/reviews_identified/PMC12409340.md) |
| `C21` | `PMC11662780` | *J Transl Med* (2024) | Transcriptomics & CompBio | High (>=25) (39) | 0.6/3.5 | 0.5/2.5 | 0.8/2.0 | 0.8/2.0 | **2.7** | Fundamentally Invalid | [Review](calibration/reviews_identified/PMC11662780.md) |
| `C22` | `PMC12622556` | *Adv Sci (Weinh)* (2025) | Transcriptomics & CompBio | Mid (5-24) (5) | 1.2/3.5 | 1.1/2.5 | 1.1/2.0 | 1.1/2.0 | **4.5** | Flawed / Overstated | [Review](calibration/reviews_identified/PMC12622556.md) |
| `C23` | `PMC10676521` | *Bioinform Adv* (2023) | Transcriptomics & CompBio | Mid (5-24) (7) | 1.2/3.5 | 1.0/2.5 | 1.1/2.0 | 0.9/2.0 | **4.2** | Flawed / Overstated | [Review](calibration/reviews_identified/PMC10676521.md) |
| `C24` | `PMC12043589` | *Front Cell Dev Biol* (2025) | Transcriptomics & CompBio | Low (0-4) (1) | 0.8/3.5 | 0.7/2.5 | 0.7/2.0 | 1.1/2.0 | **3.3** | Flawed / Overstated | [Review](calibration/reviews_identified/PMC12043589.md) |
| `C25` | `PMC12174135` | *Front Cell Dev Biol* (2025) | Transcriptomics & CompBio | Low (0-4) (2) | 0.7/3.5 | 0.7/2.5 | 0.8/2.0 | 0.7/2.0 | **2.9** | Fundamentally Invalid | [Review](calibration/reviews_identified/PMC12174135.md) |

---

---

## 5. Complete De-Identification & Prestige-Bias Experiment (All 75 Papers, `ANON_01`–`ANON_75`)

All 75 manuscripts across Cohorts A, B, and C were stripped of Titles, Author Names, Affiliations, Journal Names, Publication Years, DOIs, and PMCIDs/PMIDs (`papers_anon/ANON_01.md`–`ANON_75.md`) and independently reviewed under double-blinded rules (`reviews_anon/ANON_01.md`–`ANON_75.md`).

### A. Paired Identified vs. De-Identified Summary across All 3 Cohorts ($N = 75$)

| Metric | Cohort A: Invalid ($N=25$) | Cohort B: Validated ($N=25$) | Cohort C: Wild Sample ($N=25$) | All 75 Papers Combined |
| :--- | :---: | :---: | :---: | :---: |
| **Identified Mean / Median** | **4.62** / **4.10** | **8.58** / **8.60** | **5.36** / **5.30** | **6.19** / **6.40** |
| **De-Identified Mean / Median** | **4.26** / **3.80** | **8.25** / **8.50** | **5.44** / **5.40** | **5.98** / **6.10** |
| **Mean Paired Shift ($\Delta = S_{\text{anon}} - S_{\text{id}}$)** | **$-0.36$** | **$-0.33$** | **$+0.08$** | **$-0.20$** (Mean $|\Delta| = 0.70$) |
| **Paired Correlation ($r$)** | $r = 0.8156$ | $r = 0.7019$ | **$r = 0.9256$** | **$r = 0.9104$** |
| **De-Identified Rate $< 5.0$** | **68.0%** ($17/25$) | **4.0%** ($1/25$, `B02`) | **40.0%** ($10/25$) | — |
| **De-Identified Rate $< 5.5$** | **68.0%** ($17/25$) | **4.0%** ($1/25$, `B02`) | **52.0%** ($13/25$) | — |
| **De-Identified Rate $< 6.5$** | **80.0%** ($20/25$) | **8.0%** ($2/25$) | **72.0%** ($18/25$) | — |

### B. De-Identified Rogan-Gladen Prevalence Estimators in Cohort C ($N = 25$)

| Failure Threshold Definition | De-Identified Sensitivity ($\widehat{\text{Se}}_{\text{anon}}$) | De-Identified Specificity ($\widehat{\text{Sp}}_{\text{anon}}$) | Wild De-Identified Failure Rate ($\hat{p}_{\text{obs, anon}}$) | De-Identified Rogan-Gladen Prevalence ($\hat{\pi}_{\text{true, anon}}$) |
| :--- | :---: | :---: | :---: | :---: |
| **Strict Fatal Invalidation ($S < 5.0$)** | $68.0\%$ ($17/25$) | $96.0\%$ ($24/25$) | **$40.0\%$ ($10/25$)** | **$56.2\%$** *(or **$58.8\%$** w/ `B02` reclassified)* |
| **Substantive Failure ($S < 5.5$)** | $68.0\%$ ($17/25$) | $96.0\%$ ($24/25$) | **$52.0\%$ ($13/25$)** | **$75.0\%$** *(or **$76.5\%$** w/ `B02` reclassified)* |
| **Major Methodological Flaw ($S < 6.0$)** | $76.0\%$ ($19/25$) | $92.0\%$ ($23/25$) | **$64.0\%$ ($16/25$)** | **$82.4\%$** |
| **Any Major Pillar Violation ($S < 6.5$)** | $80.0\%$ ($20/25$) | $92.0\%$ ($23/25$) | **$72.0\%$ ($18/25$)** | **$88.9\%$** |

### C. Complete 75-Paper Paired Ledger (Identified vs. De-Identified)

| Cohort ID | Anon ID | PMCID | Venue (Year) | Identified Score | De-Identified Score | Shift ($\Delta$) | De-Identified Review |
| :---: | :---: | :---: | :--- | :---: | :---: | :---: | :---: |
| `A01` | `ANON_37` | `PMC9404229` | *Environ Res* (2022) | **4.1** (Flawed / Overstated) | **2.5** (Fundamentally Invalid) | `-1.60` | [Anon Review](calibration/reviews_anon/ANON_37.md) |
| `A02` | `ANON_19` | `PMC7107875` | *Natl Sci Rev* (2020) | **4.5** (Flawed / Overstated) | **3.8** (Flawed / Overstated) | `-0.70` | [Anon Review](calibration/reviews_anon/ANON_19.md) |
| `A03` | `ANON_45` | `PMC7196762` | *Proc Natl Acad Sci U S A* (2020) | **3.2** (Flawed / Overstated) | **2.4** (Fundamentally Invalid) | `-0.80` | [Anon Review](calibration/reviews_anon/ANON_45.md) |
| `A04` | `ANON_04` | `PMC7184484` | *Mol Biol Evol* (2020) | **3.0** (Flawed / Overstated) | **2.3** (Fundamentally Invalid) | `-0.70` | [Anon Review](calibration/reviews_anon/ANON_04.md) |
| `A05` | `ANON_01` | `PMC7138088` | *J Med Virol* (2020) | **1.8** (Fundamentally Invalid) | **2.2** (Fundamentally Invalid) | `+0.40` | [Anon Review](calibration/reviews_anon/ANON_01.md) |
| `A06` | `ANON_12` | `PMC9349972` | *J Med Virol* (2022) | **2.5** (Fundamentally Invalid) | **3.3** (Flawed / Overstated) | `+0.80` | [Anon Review](calibration/reviews_anon/ANON_12.md) |
| `A07` | `ANON_31` | `PMC7199730` | *Infect Genet Evol* (2020) | **7.9** (Strong / Sound) | **6.6** (Mixed / Salvageable) | `-1.30` | [Anon Review](calibration/reviews_anon/ANON_31.md) |
| `A08` | `ANON_05` | `PMC7428442` | *Sci Total Environ* (2021) | **3.6** (Flawed / Overstated) | **5.5** (Mixed / Salvageable) | `+1.90` | [Anon Review](calibration/reviews_anon/ANON_05.md) |
| `A09` | `ANON_13` | `PMC8529295` | *Tumori* (2021) | **2.6** (Fundamentally Invalid) | **1.6** (Fundamentally Invalid) | `-1.00` | [Anon Review](calibration/reviews_anon/ANON_13.md) |
| `A10` | `ANON_39` | `PMC7276232` | *J Biomed Sci* (2020) | **3.5** (Flawed / Overstated) | **4.3** (Flawed / Overstated) | `+0.80` | [Anon Review](calibration/reviews_anon/ANON_39.md) |
| `A11` | `ANON_14` | `PMC5182071` | *Science* (2016) | **8.1** (Strong / Sound) | **8.1** (Strong / Sound) | `+0.00` | [Anon Review](calibration/reviews_anon/ANON_14.md) |
| `A12` | `ANON_28` | `PMC7267315` | *Int J Clin Pract* (2020) | **2.1** (Fundamentally Invalid) | **1.8** (Fundamentally Invalid) | `-0.30` | [Anon Review](calibration/reviews_anon/ANON_28.md) |
| `A13` | `ANON_02` | `PMC7375454` | *J Hum Genet* (2020) | **3.1** (Flawed / Overstated) | **3.4** (Flawed / Overstated) | `+0.30` | [Anon Review](calibration/reviews_anon/ANON_02.md) |
| `A14` | `ANON_43` | `PMC7247990` | *Int J Infect Dis* (2020) | **2.5** (Fundamentally Invalid) | **2.1** (Fundamentally Invalid) | `-0.40` | [Anon Review](calibration/reviews_anon/ANON_43.md) |
| `A15` | `ANON_35` | `PMC7395502` | *Proc Natl Acad Sci U S A* (2020) | **4.8** (Flawed / Overstated) | **3.2** (Flawed / Overstated) | `-1.60` | [Anon Review](calibration/reviews_anon/ANON_35.md) |
| `A16` | `ANON_16` | `PMC7500457` | *Nature* (2020) | **3.3** (Flawed / Overstated) | **4.6** (Flawed / Overstated) | `+1.30` | [Anon Review](calibration/reviews_anon/ANON_16.md) |
| `A17` | `ANON_38` | `PMC6858566` | *Nature* (2019) | **4.1** (Flawed / Overstated) | **4.2** (Flawed / Overstated) | `+0.10` | [Anon Review](calibration/reviews_anon/ANON_38.md) |
| `A18` | `ANON_11` | `PMC9567272` | *Cell* (2022) | **4.4** (Flawed / Overstated) | **5.8** (Mixed / Salvageable) | `+1.40` | [Anon Review](calibration/reviews_anon/ANON_11.md) |
| `A19` | `ANON_06` | `PMC7757858` | *Science* (2020) | **8.0** (Strong / Sound) | **7.2** (Strong / Sound) | `-0.80` | [Anon Review](calibration/reviews_anon/ANON_06.md) |
| `A20` | `ANON_21` | `PMC5617305` | *Proc Natl Acad Sci U S A* (2017) | **5.2** (Mixed / Salvageable) | **4.4** (Flawed / Overstated) | `-0.80` | [Anon Review](calibration/reviews_anon/ANON_21.md) |
| `A21` | `ANON_17` | `PMC6613792` | *Nat Med* (2019) | **5.7** (Mixed / Salvageable) | **2.1** (Fundamentally Invalid) | `-3.60` | [Anon Review](calibration/reviews_anon/ANON_17.md) |
| `A22` | `ANON_27` | `PMC3261167` | *PLoS One* (2012) | **4.8** (Flawed / Overstated) | **2.4** (Fundamentally Invalid) | `-2.40` | [Anon Review](calibration/reviews_anon/ANON_27.md) |
| `A23` | `ANON_03` | `PMC3480734` | *Nat Genet* (2012) | **6.4** (Mixed / Salvageable) | **7.4** (Strong / Sound) | `+1.00` | [Anon Review](calibration/reviews_anon/ANON_03.md) |
| `A24` | `ANON_20` | `PMC4125079` | *PLoS Genet* (2014) | **8.3** (Strong / Sound) | **9.1** (Exemplary) | `+0.80` | [Anon Review](calibration/reviews_anon/ANON_20.md) |
| `A25` | `ANON_24` | `PMC3935878` | *PLoS One* (2014) | **8.0** (Strong / Sound) | **6.2** (Mixed / Salvageable) | `-1.80` | [Anon Review](calibration/reviews_anon/ANON_24.md) |
| `B01` | `ANON_18` | `PMC8421097` | *Cell* (2021) | **8.6** (Strong / Sound) | **8.3** (Strong / Sound) | `-0.30` | [Anon Review](calibration/reviews_anon/ANON_18.md) |
| `B02` | `ANON_26` | `PMC8135569` | *Mol Biol Evol* (2021) | **7.5** (Strong / Sound) | **3.3** (Flawed / Overstated) | `-4.20` | [Anon Review](calibration/reviews_anon/ANON_26.md) |
| `B03` | `ANON_07` | `PMC7990310` | *PLoS Biol* (2021) | **7.9** (Strong / Sound) | **8.4** (Strong / Sound) | `+0.50` | [Anon Review](calibration/reviews_anon/ANON_07.md) |
| `B04` | `ANON_10` | `PMC7332439` | *Cell* (2020) | **8.1** (Strong / Sound) | **8.6** (Strong / Sound) | `+0.50` | [Anon Review](calibration/reviews_anon/ANON_10.md) |
| `B05` | `ANON_36` | `PMC7810038` | *Science* (2020) | **8.5** (Strong / Sound) | **9.0** (Exemplary) | `+0.50` | [Anon Review](calibration/reviews_anon/ANON_36.md) |
| `B06` | `ANON_25` | `PMC9348752` | *Science* (2022) | **8.8** (Strong / Sound) | **8.5** (Strong / Sound) | `-0.30` | [Anon Review](calibration/reviews_anon/ANON_25.md) |
| `B07` | `ANON_41` | `PMC9348750` | *Science* (2022) | **8.5** (Strong / Sound) | **8.5** (Strong / Sound) | `+0.00` | [Anon Review](calibration/reviews_anon/ANON_41.md) |
| `B08` | `ANON_22` | `PMC8942855` | *Nature* (2022) | **8.6** (Strong / Sound) | **7.9** (Strong / Sound) | `-0.70` | [Anon Review](calibration/reviews_anon/ANON_22.md) |
| `B09` | `ANON_29` | `PMC7610519` | *Nat Microbiol* (2020) | **8.5** (Strong / Sound) | **8.4** (Strong / Sound) | `-0.10` | [Anon Review](calibration/reviews_anon/ANON_29.md) |
| `B10` | `ANON_40` | `PMC7721162` | *PLoS Genet* (2020) | **9.3** (Exemplary) | **9.1** (Exemplary) | `-0.20` | [Anon Review](calibration/reviews_anon/ANON_40.md) |
| `B11` | `ANON_49` | `PMC8128288` | *Science* (2021) | **8.9** (Strong / Sound) | **8.9** (Strong / Sound) | `+0.00` | [Anon Review](calibration/reviews_anon/ANON_49.md) |
| `B12` | `ANON_32` | `PMC8139423` | *Science* (2021) | **8.6** (Strong / Sound) | **8.3** (Strong / Sound) | `-0.30` | [Anon Review](calibration/reviews_anon/ANON_32.md) |
| `B13` | `ANON_46` | `PMC9161372` | *Science* (2022) | **8.3** (Strong / Sound) | **7.2** (Strong / Sound) | `-1.10` | [Anon Review](calibration/reviews_anon/ANON_46.md) |
| `B14` | `ANON_09` | `PMC10506532` | *Virus Evol* (2023) | **9.5** (Exemplary) | **9.2** (Exemplary) | `-0.30` | [Anon Review](calibration/reviews_anon/ANON_09.md) |
| `B15` | `ANON_50` | `PMC5712493` | *Nature* (2017) | **9.0** (Exemplary) | **8.8** (Strong / Sound) | `-0.20` | [Anon Review](calibration/reviews_anon/ANON_50.md) |
| `B16` | `ANON_15` | `PMC10653788` | *mBio* (2023) | **9.3** (Exemplary) | **9.4** (Exemplary) | `+0.10` | [Anon Review](calibration/reviews_anon/ANON_15.md) |
| `B17` | `ANON_33` | `PMC6428571` | *Elife* (2019) | **9.4** (Exemplary) | **9.1** (Exemplary) | `-0.30` | [Anon Review](calibration/reviews_anon/ANON_33.md) |
| `B18` | `ANON_34` | `PMC6428572` | *Elife* (2019) | **9.4** (Exemplary) | **9.2** (Exemplary) | `-0.20` | [Anon Review](calibration/reviews_anon/ANON_34.md) |
| `B19` | `ANON_08` | `PMC3395634` | *PLoS Genet* (2012) | **9.0** (Exemplary) | **9.1** (Exemplary) | `+0.10` | [Anon Review](calibration/reviews_anon/ANON_08.md) |
| `B20` | `ANON_48` | `PMC4408417` | *Mol Biol Evol* (2015) | **8.8** (Strong / Sound) | **8.6** (Strong / Sound) | `-0.20` | [Anon Review](calibration/reviews_anon/ANON_48.md) |
| `B21` | `ANON_44` | `PMC8204705` | *Mol Biol Evol* (2020) | **8.1** (Strong / Sound) | **8.1** (Strong / Sound) | `+0.00` | [Anon Review](calibration/reviews_anon/ANON_44.md) |
| `B22` | `ANON_47` | `PMC7182206` | *Mol Biol Evol* (2020) | **7.4** (Strong / Sound) | **8.3** (Strong / Sound) | `+0.90` | [Anon Review](calibration/reviews_anon/ANON_47.md) |
| `B23` | `ANON_42` | `PMC6247931` | *Bioinformatics* (2018) | **7.9** (Strong / Sound) | **7.8** (Strong / Sound) | `-0.10` | [Anon Review](calibration/reviews_anon/ANON_42.md) |
| `B24` | `ANON_23` | `PMC4302049` | *Genome Biol* (2014) | **9.2** (Exemplary) | **8.8** (Strong / Sound) | `-0.40` | [Anon Review](calibration/reviews_anon/ANON_23.md) |
| `B25` | `ANON_30` | `PMC8922736` | *Genome Biol* (2022) | **7.4** (Strong / Sound) | **5.5** (Mixed / Salvageable) | `-1.90` | [Anon Review](calibration/reviews_anon/ANON_30.md) |
| `C01` | `ANON_52` | `PMC11305400` | *Cell Rep* (2024) | **7.7** (Strong / Sound) | **7.7** (Strong / Sound) | `+0.00` | [Anon Review](calibration/reviews_anon/ANON_52.md) |
| `C02` | `ANON_64` | `PMC12313522` | *Nat Microbiol* (2025) | **7.7** (Strong / Sound) | **8.2** (Strong / Sound) | `+0.50` | [Anon Review](calibration/reviews_anon/ANON_64.md) |
| `C03` | `ANON_60` | `PMC8011692` | *Emerg Microbes Infect* (2021) | **5.1** (Mixed / Salvageable) | **5.3** (Mixed / Salvageable) | `+0.20` | [Anon Review](calibration/reviews_anon/ANON_60.md) |
| `C04` | `ANON_58` | `PMC11682804` | *Emerg Infect Dis* (2025) | **5.8** (Mixed / Salvageable) | **6.1** (Mixed / Salvageable) | `+0.30` | [Anon Review](calibration/reviews_anon/ANON_58.md) |
| `C05` | `ANON_62` | `PMC11281702` | *Viruses* (2024) | **5.3** (Mixed / Salvageable) | **4.5** (Flawed / Overstated) | `-0.80` | [Anon Review](calibration/reviews_anon/ANON_62.md) |
| `C06` | `ANON_68` | `PMC7105384` | *Elife* (2020) | **8.3** (Strong / Sound) | **6.3** (Mixed / Salvageable) | `-2.00` | [Anon Review](calibration/reviews_anon/ANON_68.md) |
| `C07` | `ANON_59` | `PMC10431346` | *Virus Evol* (2022) | **8.8** (Strong / Sound) | **9.0** (Exemplary) | `+0.20` | [Anon Review](calibration/reviews_anon/ANON_59.md) |
| `C08` | `ANON_73` | `PMC11040004` | *Nucleic Acids Res* (2024) | **8.6** (Strong / Sound) | **8.5** (Strong / Sound) | `-0.10` | [Anon Review](calibration/reviews_anon/ANON_73.md) |
| `C09` | `ANON_54` | `PMC11431564` | *Genes (Basel)* (2024) | **5.9** (Mixed / Salvageable) | **6.5** (Mixed / Salvageable) | `+0.60` | [Anon Review](calibration/reviews_anon/ANON_54.md) |
| `C10` | `ANON_69` | `PMC11228553` | *Front Bioinform* (2024) | **6.0** (Mixed / Salvageable) | **5.2** (Mixed / Salvageable) | `-0.80` | [Anon Review](calibration/reviews_anon/ANON_69.md) |
| `C11` | `ANON_57` | `PMC10901987` | *Front Microbiol* (2024) | **4.6** (Flawed / Overstated) | **5.9** (Mixed / Salvageable) | `+1.30` | [Anon Review](calibration/reviews_anon/ANON_57.md) |
| `C12` | `ANON_71` | `PMC6680985` | *Microorganisms* (2019) | **3.6** (Flawed / Overstated) | **2.5** (Fundamentally Invalid) | `-1.10` | [Anon Review](calibration/reviews_anon/ANON_71.md) |
| `C13` | `ANON_63` | `PMC9509681` | *Infect Drug Resist* (2022) | **1.8** (Fundamentally Invalid) | **2.1** (Fundamentally Invalid) | `+0.30` | [Anon Review](calibration/reviews_anon/ANON_63.md) |
| `C14` | `ANON_66` | `PMC9008261` | *Front Cell Infect Microbiol* (2022) | **3.4** (Flawed / Overstated) | **5.5** (Mixed / Salvageable) | `+2.10` | [Anon Review](calibration/reviews_anon/ANON_66.md) |
| `C15` | `ANON_74` | `PMC12354945` | *Cancer Res Commun* (2025) | **5.5** (Mixed / Salvageable) | **5.4** (Mixed / Salvageable) | `-0.10` | [Anon Review](calibration/reviews_anon/ANON_74.md) |
| `C16` | `ANON_56` | `PMC7617604` | *N Engl J Med* (2025) | **7.5** (Strong / Sound) | **7.2** (Strong / Sound) | `-0.30` | [Anon Review](calibration/reviews_anon/ANON_56.md) |
| `C17` | `ANON_65` | `PMC12120081` | *Nat Commun* (2025) | **7.8** (Strong / Sound) | **8.3** (Strong / Sound) | `+0.50` | [Anon Review](calibration/reviews_anon/ANON_65.md) |
| `C18` | `ANON_75` | `PMC11711298` | *Plant Genome* (2025) | **3.8** (Flawed / Overstated) | **4.0** (Flawed / Overstated) | `+0.20` | [Anon Review](calibration/reviews_anon/ANON_75.md) |
| `C19` | `ANON_55` | `PMC11610249` | *Front Plant Sci* (2024) | **3.8** (Flawed / Overstated) | **4.1** (Flawed / Overstated) | `+0.30` | [Anon Review](calibration/reviews_anon/ANON_55.md) |
| `C20` | `ANON_67` | `PMC12409340` | *Int J Chron Obstruct Pulmon Dis* (2025) | **5.5** (Mixed / Salvageable) | **5.6** (Mixed / Salvageable) | `+0.10` | [Anon Review](calibration/reviews_anon/ANON_67.md) |
| `C21` | `ANON_72` | `PMC11662780` | *J Transl Med* (2024) | **2.7** (Fundamentally Invalid) | **2.8** (Fundamentally Invalid) | `+0.10` | [Anon Review](calibration/reviews_anon/ANON_72.md) |
| `C22` | `ANON_61` | `PMC12622556` | *Adv Sci (Weinh)* (2025) | **4.5** (Flawed / Overstated) | **4.4** (Flawed / Overstated) | `-0.10` | [Anon Review](calibration/reviews_anon/ANON_61.md) |
| `C23` | `ANON_53` | `PMC10676521` | *Bioinform Adv* (2023) | **4.2** (Flawed / Overstated) | **4.2** (Flawed / Overstated) | `+0.00` | [Anon Review](calibration/reviews_anon/ANON_53.md) |
| `C24` | `ANON_70` | `PMC12043589` | *Front Cell Dev Biol* (2025) | **3.3** (Flawed / Overstated) | **3.2** (Flawed / Overstated) | `-0.10` | [Anon Review](calibration/reviews_anon/ANON_70.md) |
| `C25` | `ANON_51` | `PMC12174135` | *Front Cell Dev Biol* (2025) | **2.9** (Fundamentally Invalid) | **3.5** (Flawed / Overstated) | `+0.60` | [Anon Review](calibration/reviews_anon/ANON_51.md) |

---

## 6. Full 200-Paper Double-Blinded De-Identified Study ($N_A = 50, N_B = 50, N_C = 100$)

Scaling the double-blinded (`ANON_01`–`ANON_200`) cohort design to **200 full-text manuscripts** (50 Known Invalid/Refuted in Cohort A, 50 Genre-Matched Validated Controls in Cohort B [43 empirical biological discovery studies + 7 foundational methods benchmarks], and 100 Stratified Wild Papers in Cohort C [20 per subfield]):

### A. 200-Paper Cohort Summary

| Metric / Estimator | Cohort A: Known Invalid ($N=50$) | Cohort A: Internal Flaws ($N=45$) | Cohort B: All Validated ($N=50$) | Cohort B: Empirical Only ($N=43$) | Cohort C: Wild Sample ($N=100$) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Mean Score (/10.0)** | **4.42** ($\pm 1.97$) | **4.09** ($\pm 1.75$) | **8.64** ($\pm 0.84$) | **8.64** ($\pm 0.87$) | **5.47** ($\pm 1.78$) |
| **Median Score** | **4.10** | **3.80** | **8.85** | **9.00** | **5.40** |
| **ROC-AUC vs. Cohort A** | — | — | **0.9688** | **0.9672** | — |
| **Strict Failure ($S < 5.0$)** | **66.0%** ($33/50$) | **73.3%** ($33/45$) | **0.0%** ($0/50$) | **0.0%** ($0/43$) | **43.0%** ($43/100$) |
| **Substantive Failure ($S < 5.5$)** | **66.0%** ($33/50$) | **73.3%** ($33/45$) | **0.0%** ($0/50$) | **0.0%** ($0/43$) | **53.0%** ($53/100$) |
| **Moderate/Major Flaw ($S < 6.0$)** | **76.0%** ($38/50$) | **84.4%** ($38/45$) | **2.0%** ($1/50$) | **2.3%** ($1/43$) | **61.0%** ($61/100$) |
| **Any Major Violation ($S < 6.5$)** | **80.0%** ($40/50$) | **86.7%** ($39/45$) | **4.0%** ($2/50$) | **4.7%** ($2/43$) | **70.0%** ($70/100$) |

### B. Prevalence Estimators & 95% Confidence Intervals ($N = 200$)

| Failure Threshold | Sensitivity ($\widehat{\text{Se}}_{\text{all}}$ / $\widehat{\text{Se}}_{\text{int}}$) | Specificity ($\widehat{\text{Sp}}$) | Wild Observed Rate $\hat{p}_{\text{obs}}$ (Stratified 95% CI) | Rogan-Gladen $\hat{\pi}_{\text{true}}$ (All A [bootstrap 95% CI]$^{\dagger}$ / Internal A) |
| :--- | :---: | :---: | :---: | :---: |
| **Strict Fatal Invalidation ($S < 5.0$)** | $66.0\%$ / $73.3\%$ | $100.0\%$ ($50/50$) | **43.0%** ($\pm 8.5\% \implies [34.5\%, 51.5\%]$) | **65.2%** ($[47.3\%, 87.9\%]$) / **58.6%** |
| **Substantive Failure ($S < 5.5$)** | $66.0\%$ / $73.3\%$ | $100.0\%$ ($50/50$) | **53.0%** ($\pm 9.1\% \implies [43.9\%, 62.1\%]$) | **80.3%** ($[61.3\%, 100\%]$) / **72.3%** |
| **Major Methodological Flaw ($S < 6.0$)** | $76.0\%$ / $84.4\%$ | $98.0\%$ ($49/50$) | **61.0%** ($\pm 8.7\% \implies [52.3\%, 69.7\%]$) | **79.7%** ($[63.1\%, 100\%]$) / **71.6%** |
| **Any Major Pillar Violation ($S < 6.5$)** | $80.0\%$ / $86.7\%$ | $96.0\%$ ($48/50$) | **70.0%** ($\pm 8.3\% \implies [61.7\%, 78.3\%]$) | **86.8%** ($[70.7\%, 100\%]$) / **79.8%** |

$^{\dagger}$ Percentile-bootstrap 95% intervals (5000 reps; Cohorts A, B and C resampled jointly; clipped to $[0, 1]$; `python3 -I scripts/rg_bootstrap.py`, seed 20261028). Intervals include Sp uncertainty (exact 95% CI for Sp with 50/50: [92.9%, 100%]).

### C. Stratified Breakdown of the 100 Wild Papers (`Cohort C`)

#### 1. By Subfield ($n = 20$ papers per subfield)
| Subfield ($n=20$) | Mean Score | Median Score | Strict Failure ($S < 5.0$) | Major Flaw ($S < 6.5$) |
| :--- | :---: | :---: | :---: | :---: |
| **Molecular Evolution** | **6.90** | **6.50** | **5.0%** ($1/20$) | **45.0%** ($9/20$) |
| **Viral Evolution** | **5.97** | **6.35** | **35.0%** ($7/20$) | **55.0%** ($11/20$) |
| **Statistical Genetics / GWAS** | **5.37** | **5.40** | **40.0%** ($8/20$) | **75.0%** ($15/20$) |
| **Cancer & Microbiome** | **4.78** | **4.60** | **60.0%** ($12/20$) | **85.0%** ($17/20$) |
| **Transcriptomics & CompBio ML** | **4.33** | **4.20** | **75.0%** ($15/20$) | **90.0%** ($18/20$) |

#### 2. By Citation Velocity Tier ($N = 100$)
| Citation Tier | $n$ | Mean Score | Median Score | Strict Failure ($S < 5.0$) | Major Flaw ($S < 6.5$) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **High ($\ge 25$ citations)** | 31 | **6.59** | **6.60** | **19.4%** ($6/31$) | **41.9%** ($13/31$) |
| **Mid ($5\text{--}24$ citations)** | 35 | **5.31** | **5.20** | **48.6%** ($17/35$) | **71.4%** ($25/35$) |
| **Low ($0\text{--}4$ citations)** | 34 | **4.62** | **4.50** | **58.8%** ($20/34$) | **94.1%** ($32/34$) |

### D. Complete 200-Paper De-Identified Ledger (`ANON_01`–`ANON_200`)

| Cohort ID | Anon ID | PMCID | Venue (Year) | Domain | Rigor | Claims | Bio | Repro | **Overall** | Tier | Review |
| :---: | :---: | :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :---: |
| `A01` | `ANON_37` | `PMC9404229` | *Environ Res* (2022) | Viral Evolution | 0.5/3.5 | 0.4/2.5 | 0.5/2.0 | 1.1/2.0 | **2.5** | Fundamentally Invalid | [Review](calibration/reviews_anon/ANON_37.md) |
| `A02` | `ANON_19` | `PMC7107875` | *Natl Sci Rev* (2020) | Viral Evolution | 0.9/3.5 | 0.7/2.5 | 0.9/2.0 | 1.3/2.0 | **3.8** | Flawed / Overstated | [Review](calibration/reviews_anon/ANON_19.md) |
| `A03` | `ANON_45` | `PMC7196762` | *Proc Natl Acad Sci U S A* (2020) | Viral Evolution | 0.6/3.5 | 0.4/2.5 | 0.5/2.0 | 0.9/2.0 | **2.4** | Fundamentally Invalid | [Review](calibration/reviews_anon/ANON_45.md) |
| `A04` | `ANON_04` | `PMC7184484` | *Mol Biol Evol* (2020) | Molecular Evolution | 0.4/3.5 | 0.4/2.5 | 0.5/2.0 | 1.0/2.0 | **2.3** | Fundamentally Invalid | [Review](calibration/reviews_anon/ANON_04.md) |
| `A05` | `ANON_01` | `PMC7138088` | *J Med Virol* (2020) | Molecular Evolution | 0.4/3.5 | 0.5/2.5 | 0.5/2.0 | 0.8/2.0 | **2.2** | Fundamentally Invalid | [Review](calibration/reviews_anon/ANON_01.md) |
| `A06` | `ANON_12` | `PMC9349972` | *J Med Virol* (2022) | Viral Evolution | 0.8/3.5 | 0.7/2.5 | 0.9/2.0 | 0.9/2.0 | **3.3** | Flawed / Overstated | [Review](calibration/reviews_anon/ANON_12.md) |
| `A07` | `ANON_31` | `PMC7199730` | *Infect Genet Evol* (2020) | Viral Evolution | 2.0/3.5 | 1.6/2.5 | 1.5/2.0 | 1.5/2.0 | **6.6** | Mixed / Salvageable | [Review](calibration/reviews_anon/ANON_31.md) |
| `A08` | `ANON_05` | `PMC7428442` | *Sci Total Environ* (2021) | Viral Epidemiology | 1.8/3.5 | 1.4/2.5 | 1.2/2.0 | 1.1/2.0 | **5.5** | Mixed / Salvageable | [Review](calibration/reviews_anon/ANON_05.md) |
| `A09` | `ANON_13` | `PMC8529295` | *Tumori* (2021) | Viral Epidemiology | 0.4/3.5 | 0.3/2.5 | 0.3/2.0 | 0.6/2.0 | **1.6** | Fundamentally Invalid | [Review](calibration/reviews_anon/ANON_13.md) |
| `A10` | `ANON_39` | `PMC7276232` | *J Biomed Sci* (2020) | Viral Evolution | 1.1/3.5 | 0.9/2.5 | 1.0/2.0 | 1.3/2.0 | **4.3** | Flawed / Overstated | [Review](calibration/reviews_anon/ANON_39.md) |
| `A11` | `ANON_14` | `PMC5182071` | *Science* (2016) | Population Genomics | 2.6/3.5 | 2.0/2.5 | 1.8/2.0 | 1.7/2.0 | **8.1** | Strong / Sound | [Review](calibration/reviews_anon/ANON_14.md) |
| `A12` | `ANON_28` | `PMC7267315` | *Int J Clin Pract* (2020) | Viral Epidemiology | 0.4/3.5 | 0.3/2.5 | 0.5/2.0 | 0.6/2.0 | **1.8** | Fundamentally Invalid | [Review](calibration/reviews_anon/ANON_28.md) |
| `A13` | `ANON_02` | `PMC7375454` | *J Hum Genet* (2020) | Viral Genomics | 0.9/3.5 | 0.8/2.5 | 0.7/2.0 | 1.0/2.0 | **3.4** | Flawed / Overstated | [Review](calibration/reviews_anon/ANON_02.md) |
| `A14` | `ANON_43` | `PMC7247990` | *Int J Infect Dis* (2020) | Viral Epidemiology | 0.4/3.5 | 0.6/2.5 | 0.6/2.0 | 0.5/2.0 | **2.1** | Fundamentally Invalid | [Review](calibration/reviews_anon/ANON_43.md) |
| `A15` | `ANON_35` | `PMC7395502` | *Proc Natl Acad Sci U S A* (2020) | Epidemiology / Stats | 0.7/3.5 | 0.7/2.5 | 0.8/2.0 | 1.0/2.0 | **3.2** | Flawed / Overstated | [Review](calibration/reviews_anon/ANON_35.md) |
| `A16` | `ANON_16` | `PMC7500457` | *Nature* (2020) | Cancer Microbiome | 1.1/3.5 | 0.9/2.5 | 1.0/2.0 | 1.6/2.0 | **4.6** | Flawed / Overstated | [Review](calibration/reviews_anon/ANON_16.md) |
| `A17` | `ANON_38` | `PMC6858566` | *Nature* (2019) | Cancer Microbiome | 1.1/3.5 | 1.0/2.5 | 1.1/2.0 | 1.0/2.0 | **4.2** | Flawed / Overstated | [Review](calibration/reviews_anon/ANON_38.md) |
| `A18` | `ANON_11` | `PMC9567272` | *Cell* (2022) | Cancer Microbiome | 1.6/3.5 | 1.3/2.5 | 1.2/2.0 | 1.7/2.0 | **5.8** | Mixed / Salvageable | [Review](calibration/reviews_anon/ANON_11.md) |
| `A19` | `ANON_06` | `PMC7757858` | *Science* (2020) | Cancer Microbiome | 2.3/3.5 | 1.9/2.5 | 1.4/2.0 | 1.6/2.0 | **7.2** | Strong / Sound | [Review](calibration/reviews_anon/ANON_06.md) |
| `A20` | `ANON_21` | `PMC5617305` | *Proc Natl Acad Sci U S A* (2017) | Statistical Genetics | 1.5/3.5 | 0.9/2.5 | 1.1/2.0 | 0.9/2.0 | **4.4** | Flawed / Overstated | [Review](calibration/reviews_anon/ANON_21.md) |
| `A21` | `ANON_17` | `PMC6613792` | *Nat Med* (2019) | Statistical Genetics | 0.4/3.5 | 0.3/2.5 | 0.5/2.0 | 0.9/2.0 | **2.1** | Fundamentally Invalid | [Review](calibration/reviews_anon/ANON_17.md) |
| `A22` | `ANON_27` | `PMC3261167` | *PLoS One* (2012) | Statistical Genetics | 0.7/3.5 | 0.5/2.5 | 0.5/2.0 | 0.7/2.0 | **2.4** | Fundamentally Invalid | [Review](calibration/reviews_anon/ANON_27.md) |
| `A23` | `ANON_03` | `PMC3480734` | *Nat Genet* (2012) | Population Genomics | 2.6/3.5 | 1.9/2.5 | 1.5/2.0 | 1.4/2.0 | **7.4** | Strong / Sound | [Review](calibration/reviews_anon/ANON_03.md) |
| `A24` | `ANON_20` | `PMC4125079` | *PLoS Genet* (2014) | Population Genomics | 3.2/3.5 | 2.3/2.5 | 1.9/2.0 | 1.7/2.0 | **9.1** | Exemplary | [Review](calibration/reviews_anon/ANON_20.md) |
| `A25` | `ANON_24` | `PMC3935878` | *PLoS One* (2014) | Macroevolution / Stats | 1.9/3.5 | 1.7/2.5 | 1.5/2.0 | 1.1/2.0 | **6.2** | Mixed / Salvageable | [Review](calibration/reviews_anon/ANON_24.md) |
| `A26` | `ANON_26` | `PMC8135569` | *Mol Biol Evol* (2021) | Viral Evolution | 0.9/3.5 | 0.6/2.5 | 0.7/2.0 | 1.1/2.0 | **3.3** | Flawed / Overstated | [Review](calibration/reviews_anon/ANON_26.md) |
| `A27` | `ANON_99` | `PMC4929217` | *Sci Transl Med* (2014) | Cancer & Microbiome | 1.0/3.5 | 0.9/2.5 | 0.8/2.0 | 1.3/2.0 | **4.0** | Flawed / Overstated | [Review](calibration/reviews_anon/ANON_99.md) |
| `A28` | `ANON_128` | `PMC8240556` | *Cell* (2021) | Cancer & Microbiome | 1.2/3.5 | 0.8/2.5 | 0.8/2.0 | 1.2/2.0 | **4.0** | Flawed / Overstated | [Review](calibration/reviews_anon/ANON_128.md) |
| `A29` | `ANON_97` | `PMC8110246` | *Nat Med* (2020) | Cancer & Microbiome | 2.3/3.5 | 1.7/2.5 | 1.5/2.0 | 1.8/2.0 | **7.3** | Strong / Sound | [Review](calibration/reviews_anon/ANON_97.md) |
| `A30` | `ANON_109` | `PMC1863478` | *Proc Natl Acad Sci U S A* (2007) | Molecular Evolution | 2.5/3.5 | 1.7/2.5 | 1.7/2.0 | 1.5/2.0 | **7.4** | Strong / Sound | [Review](calibration/reviews_anon/ANON_109.md) |
| `A31` | `ANON_180` | `PMC2837078` | *Immunogenetics* (2008) | Molecular Evolution | 1.3/3.5 | 1.0/2.5 | 1.2/2.0 | 1.0/2.0 | **4.5** | Flawed / Overstated | [Review](calibration/reviews_anon/ANON_180.md) |
| `A32` | `ANON_193` | `PMC8264168` | *Food Environ Virol* (2022) | Viral Epidemiology | 1.8/3.5 | 1.7/2.5 | 1.5/2.0 | 1.0/2.0 | **6.0** | Mixed / Salvageable | [Review](calibration/reviews_anon/ANON_193.md) |
| `A33` | `ANON_95` | `PMC7196402` | *Int J Antimicrob Agents* (2020) | Viral Epidemiology | 1.8/3.5 | 1.4/2.5 | 1.5/2.0 | 1.2/2.0 | **5.9** | Mixed / Salvageable | [Review](calibration/reviews_anon/ANON_95.md) |
| `A34` | `ANON_93` | `PMC7864798` | *Eur J Epidemiol* (2021) | Viral Epidemiology | 1.2/3.5 | 1.1/2.5 | 0.9/2.0 | 1.1/2.0 | **4.3** | Flawed / Overstated | [Review](calibration/reviews_anon/ANON_93.md) |
| `A35` | `ANON_111` | `PMC7859469` | *Environ Chem Lett* (2021) | Viral Evolution | 2.4/3.5 | 2.0/2.5 | 1.7/2.0 | 1.7/2.0 | **7.8** | Strong / Sound | [Review](calibration/reviews_anon/ANON_111.md) |
| `A36` | `ANON_195` | `PMC7077245` | *Viruses* (2020) | Viral Evolution | 2.1/3.5 | 1.7/2.5 | 1.6/2.0 | 1.3/2.0 | **6.7** | Mixed / Salvageable | [Review](calibration/reviews_anon/ANON_195.md) |
| `A37` | `ANON_177` | `PMC7106301` | *Infect Genet Evol* (2020) | Viral Evolution | 1.5/3.5 | 1.2/2.5 | 1.2/2.0 | 0.9/2.0 | **4.8** | Flawed / Overstated | [Review](calibration/reviews_anon/ANON_177.md) |
| `A38` | `ANON_94` | `PMC7166400` | *J Med Virol* (2020) | Viral Evolution | 0.5/3.5 | 0.6/2.5 | 0.6/2.0 | 0.6/2.0 | **2.3** | Fundamentally Invalid | [Review](calibration/reviews_anon/ANON_94.md) |
| `A39` | `ANON_136` | `PMC7174922` | *J Transl Med* (2020) | Viral Genomics | 1.0/3.5 | 0.8/2.5 | 0.8/2.0 | 1.0/2.0 | **3.6** | Flawed / Overstated | [Review](calibration/reviews_anon/ANON_136.md) |
| `A40` | `ANON_186` | `PMC7375210` | *Bull World Health Organ* (2020) | Viral Genomics | 1.7/3.5 | 1.4/2.5 | 1.3/2.0 | 1.3/2.0 | **5.7** | Mixed / Salvageable | [Review](calibration/reviews_anon/ANON_186.md) |
| `A41` | `ANON_152` | `PMC7458444` | *Sci Adv* (2020) | Viral Evolution | 1.7/3.5 | 1.3/2.5 | 1.5/2.0 | 1.3/2.0 | **5.8** | Mixed / Salvageable | [Review](calibration/reviews_anon/ANON_152.md) |
| `A42` | `ANON_139` | `PMC9488757` | *PLoS One* (2022) | Epidemiology / Stats | 2.4/3.5 | 2.2/2.5 | 1.5/2.0 | 1.2/2.0 | **7.3** | Strong / Sound | [Review](calibration/reviews_anon/ANON_139.md) |
| `A43` | `ANON_140` | `PMC7267326` | *EMBO Mol Med* (2020) | Epidemiology / Stats | 1.1/3.5 | 1.0/2.5 | 1.1/2.0 | 1.0/2.0 | **4.2** | Flawed / Overstated | [Review](calibration/reviews_anon/ANON_140.md) |
| `A44` | `ANON_78` | `PMC8759701` | *PLoS One* (2022) | Statistical Genetics | 0.5/3.5 | 0.6/2.5 | 0.6/2.0 | 0.6/2.0 | **2.3** | Fundamentally Invalid | [Review](calibration/reviews_anon/ANON_78.md) |
| `A45` | `ANON_91` | `PMC11999383` | *JMIR Form Res* (2025) | Statistical Genetics | 0.7/3.5 | 0.7/2.5 | 0.8/2.0 | 0.6/2.0 | **2.8** | Fundamentally Invalid | [Review](calibration/reviews_anon/ANON_91.md) |
| `A46` | `ANON_77` | `PMC4225573` | *BMC Neurol* (2013) | Transcriptomics & CompBio | 0.6/3.5 | 0.5/2.5 | 0.7/2.0 | 0.8/2.0 | **2.6** | Fundamentally Invalid | [Review](calibration/reviews_anon/ANON_77.md) |
| `A47` | `ANON_187` | `PMC9468935` | *Comput Math Methods Med* (2022) | Transcriptomics & CompBio | 0.8/3.5 | 0.7/2.5 | 0.8/2.0 | 0.7/2.0 | **3.0** | Flawed / Overstated | [Review](calibration/reviews_anon/ANON_187.md) |
| `A48` | `ANON_119` | `PMC12471436` | *J Pers Med* (2025) | Transcriptomics & CompBio | 0.9/3.5 | 1.0/2.5 | 1.0/2.0 | 0.8/2.0 | **3.7** | Flawed / Overstated | [Review](calibration/reviews_anon/ANON_119.md) |
| `A49` | `ANON_102` | `PMC12609430` | *Int J Mol Sci* (2025) | Transcriptomics & CompBio | 0.9/3.5 | 0.7/2.5 | 0.8/2.0 | 0.8/2.0 | **3.2** | Flawed / Overstated | [Review](calibration/reviews_anon/ANON_102.md) |
| `A50` | `ANON_173` | `PMC13107010` | *Acta Biochim Biophys Sin (Shanghai)* (2025) | Transcriptomics & CompBio | 0.5/3.5 | 0.5/2.5 | 0.5/2.0 | 0.7/2.0 | **2.2** | Fundamentally Invalid | [Review](calibration/reviews_anon/ANON_173.md) |
| `B01` | `ANON_18` | `PMC8421097` | *Cell* (2021) | Viral Evolution | 2.7/3.5 | 2.0/2.5 | 1.8/2.0 | 1.8/2.0 | **8.3** | Strong / Sound | [Review](calibration/reviews_anon/ANON_18.md) |
| `B02` | `ANON_141` | `PMC7418704` | *Cell* (2020) | Viral Evolution | 3.3/3.5 | 2.4/2.5 | 1.8/2.0 | 1.9/2.0 | **9.4** | Exemplary | [Review](calibration/reviews_anon/ANON_141.md) |
| `B03` | `ANON_07` | `PMC7990310` | *PLoS Biol* (2021) | Viral Evolution | 2.9/3.5 | 2.0/2.5 | 1.8/2.0 | 1.7/2.0 | **8.4** | Strong / Sound | [Review](calibration/reviews_anon/ANON_07.md) |
| `B04` | `ANON_10` | `PMC7332439` | *Cell* (2020) | Viral Evolution | 2.9/3.5 | 2.2/2.5 | 1.8/2.0 | 1.7/2.0 | **8.6** | Strong / Sound | [Review](calibration/reviews_anon/ANON_10.md) |
| `B05` | `ANON_36` | `PMC7810038` | *Science* (2020) | Viral Evolution | 3.3/3.5 | 2.2/2.5 | 1.9/2.0 | 1.6/2.0 | **9.0** | Exemplary | [Review](calibration/reviews_anon/ANON_36.md) |
| `B06` | `ANON_25` | `PMC9348752` | *Science* (2022) | Viral Evolution | 2.9/3.5 | 2.1/2.5 | 1.8/2.0 | 1.7/2.0 | **8.5** | Strong / Sound | [Review](calibration/reviews_anon/ANON_25.md) |
| `B07` | `ANON_41` | `PMC9348750` | *Science* (2022) | Viral Epidemiology | 2.9/3.5 | 2.0/2.5 | 1.8/2.0 | 1.8/2.0 | **8.5** | Strong / Sound | [Review](calibration/reviews_anon/ANON_41.md) |
| `B08` | `ANON_22` | `PMC8942855` | *Nature* (2022) | Viral Evolution | 2.6/3.5 | 2.1/2.5 | 1.8/2.0 | 1.4/2.0 | **7.9** | Strong / Sound | [Review](calibration/reviews_anon/ANON_22.md) |
| `B09` | `ANON_29` | `PMC7610519` | *Nat Microbiol* (2020) | Viral Genomics | 2.8/3.5 | 2.3/2.5 | 1.7/2.0 | 1.6/2.0 | **8.4** | Strong / Sound | [Review](calibration/reviews_anon/ANON_29.md) |
| `B10` | `ANON_40` | `PMC7721162` | *PLoS Genet* (2020) | Viral Genomics | 3.2/3.5 | 2.3/2.5 | 1.8/2.0 | 1.8/2.0 | **9.1** | Exemplary | [Review](calibration/reviews_anon/ANON_40.md) |
| `B11` | `ANON_49` | `PMC8128288` | *Science* (2021) | Viral Epidemiology | 3.1/3.5 | 2.2/2.5 | 1.9/2.0 | 1.7/2.0 | **8.9** | Strong / Sound | [Review](calibration/reviews_anon/ANON_49.md) |
| `B12` | `ANON_32` | `PMC8139423` | *Science* (2021) | Viral Epidemiology | 2.9/3.5 | 2.0/2.5 | 1.8/2.0 | 1.6/2.0 | **8.3** | Strong / Sound | [Review](calibration/reviews_anon/ANON_32.md) |
| `B13` | `ANON_46` | `PMC9161372` | *Science* (2022) | Viral Evolution | 2.3/3.5 | 1.7/2.5 | 1.6/2.0 | 1.6/2.0 | **7.2** | Strong / Sound | [Review](calibration/reviews_anon/ANON_46.md) |
| `B14` | `ANON_09` | `PMC10506532` | *Virus Evol* (2023) | Viral Evolution | 3.2/3.5 | 2.3/2.5 | 1.8/2.0 | 1.9/2.0 | **9.2** | Exemplary | [Review](calibration/reviews_anon/ANON_09.md) |
| `B15` | `ANON_50` | `PMC5712493` | *Nature* (2017) | Viral Evolution | 3.0/3.5 | 2.2/2.5 | 1.9/2.0 | 1.7/2.0 | **8.8** | Strong / Sound | [Review](calibration/reviews_anon/ANON_50.md) |
| `B16` | `ANON_15` | `PMC10653788` | *mBio* (2023) | Cancer Microbiome | 3.3/3.5 | 2.3/2.5 | 2.0/2.0 | 1.8/2.0 | **9.4** | Exemplary | [Review](calibration/reviews_anon/ANON_15.md) |
| `B17` | `ANON_33` | `PMC6428571` | *Elife* (2019) | Population Genomics | 3.3/3.5 | 2.3/2.5 | 1.8/2.0 | 1.7/2.0 | **9.1** | Exemplary | [Review](calibration/reviews_anon/ANON_33.md) |
| `B18` | `ANON_34` | `PMC6428572` | *Elife* (2019) | Population Genomics | 3.3/3.5 | 2.3/2.5 | 1.9/2.0 | 1.7/2.0 | **9.2** | Exemplary | [Review](calibration/reviews_anon/ANON_34.md) |
| `B19` | `ANON_08` | `PMC3395634` | *PLoS Genet* (2012) | Molecular Evolution | 3.3/3.5 | 2.3/2.5 | 1.8/2.0 | 1.7/2.0 | **9.1** | Exemplary | [Review](calibration/reviews_anon/ANON_08.md) |
| `B20` | `ANON_48` | `PMC4408417` | *Mol Biol Evol* (2015) | Molecular Evolution | 2.9/3.5 | 2.1/2.5 | 1.8/2.0 | 1.8/2.0 | **8.6** | Strong / Sound | [Review](calibration/reviews_anon/ANON_48.md) |
| `B21` | `ANON_44` | `PMC8204705` | *Mol Biol Evol* (2020) | Molecular Evolution | 2.5/3.5 | 1.9/2.5 | 1.8/2.0 | 1.9/2.0 | **8.1** | Strong / Sound | [Review](calibration/reviews_anon/ANON_44.md) |
| `B22` | `ANON_47` | `PMC7182206` | *Mol Biol Evol* (2020) | Molecular Evolution | 2.8/3.5 | 2.0/2.5 | 1.8/2.0 | 1.7/2.0 | **8.3** | Strong / Sound | [Review](calibration/reviews_anon/ANON_47.md) |
| `B23` | `ANON_42` | `PMC6247931` | *Bioinformatics* (2018) | Viral Genomics | 2.5/3.5 | 1.9/2.5 | 1.7/2.0 | 1.7/2.0 | **7.8** | Strong / Sound | [Review](calibration/reviews_anon/ANON_42.md) |
| `B24` | `ANON_23` | `PMC4302049` | *Genome Biol* (2014) | Transcriptomics / Stats | 3.0/3.5 | 2.3/2.5 | 1.7/2.0 | 1.8/2.0 | **8.8** | Strong / Sound | [Review](calibration/reviews_anon/ANON_23.md) |
| `B25` | `ANON_30` | `PMC8922736` | *Genome Biol* (2022) | Transcriptomics / Stats | 1.6/3.5 | 1.3/2.5 | 1.2/2.0 | 1.4/2.0 | **5.5** | Mixed / Salvageable | [Review](calibration/reviews_anon/ANON_30.md) |
| `B26` | `ANON_124` | `PMC7984229` | *Nat Med* (2019) | Cancer & Microbiome | 3.2/3.5 | 2.3/2.5 | 1.8/2.0 | 1.8/2.0 | **9.1** | Exemplary | [Review](calibration/reviews_anon/ANON_124.md) |
| `B27` | `ANON_192` | `PMC9533319` | *Nat Med* (2019) | Cancer & Microbiome | 3.1/3.5 | 2.2/2.5 | 1.9/2.0 | 1.9/2.0 | **9.1** | Exemplary | [Review](calibration/reviews_anon/ANON_192.md) |
| `B28` | `ANON_80` | `PMC4299606` | *Mol Syst Biol* (2014) | Cancer & Microbiome | 2.9/3.5 | 2.1/2.5 | 1.8/2.0 | 1.8/2.0 | **8.6** | Strong / Sound | [Review](calibration/reviews_anon/ANON_80.md) |
| `B29` | `ANON_189` | `PMC6707353` | *Science* (2018) | Cancer & Microbiome | 1.7/3.5 | 1.4/2.5 | 1.5/2.0 | 1.8/2.0 | **6.4** | Mixed / Salvageable | [Review](calibration/reviews_anon/ANON_189.md) |
| `B30` | `ANON_178` | `PMC5827966` | *Science* (2018) | Cancer & Microbiome | 2.0/3.5 | 1.5/2.5 | 1.6/2.0 | 1.4/2.0 | **6.5** | Mixed / Salvageable | [Review](calibration/reviews_anon/ANON_178.md) |
| `B31` | `ANON_199` | `PMC6697540` | *Nature* (2019) | Cancer & Microbiome | 3.4/3.5 | 2.5/2.5 | 2.0/2.0 | 1.9/2.0 | **9.8** | Exemplary | [Review](calibration/reviews_anon/ANON_199.md) |
| `B32` | `ANON_191` | `PMC4917942` | *Microbiome* (2016) | Cancer & Microbiome | 3.2/3.5 | 2.4/2.5 | 1.9/2.0 | 1.8/2.0 | **9.3** | Exemplary | [Review](calibration/reviews_anon/ANON_191.md) |
| `B33` | `ANON_150` | `PMC4228153` | *BMC Biol* (2014) | Cancer & Microbiome | 3.1/3.5 | 2.4/2.5 | 1.9/2.0 | 1.7/2.0 | **9.1** | Exemplary | [Review](calibration/reviews_anon/ANON_150.md) |
| `B34` | `ANON_123` | `PMC11333990` | *Nature* (2023) | Cancer & Microbiome | 2.7/3.5 | 2.2/2.5 | 1.9/2.0 | 1.5/2.0 | **8.3** | Strong / Sound | [Review](calibration/reviews_anon/ANON_123.md) |
| `B35` | `ANON_179` | `PMC9110300` | *Nat Genet* (2022) | Statistical Genetics | 3.3/3.5 | 2.3/2.5 | 1.9/2.0 | 1.9/2.0 | **9.4** | Exemplary | [Review](calibration/reviews_anon/ANON_179.md) |
| `B36` | `ANON_138` | `PMC9605867` | *Nature* (2022) | Statistical Genetics | 3.2/3.5 | 2.3/2.5 | 1.9/2.0 | 1.8/2.0 | **9.2** | Exemplary | [Review](calibration/reviews_anon/ANON_138.md) |
| `B37` | `ANON_145` | `PMC4918750` | *Nature* (2015) | Population Genomics | 3.0/3.5 | 2.2/2.5 | 1.8/2.0 | 1.8/2.0 | **8.8** | Strong / Sound | [Review](calibration/reviews_anon/ANON_145.md) |
| `B38` | `ANON_103` | `PMC6128408` | *Nat Genet* (2018) | Statistical Genetics | 2.9/3.5 | 2.0/2.5 | 1.8/2.0 | 1.8/2.0 | **8.5** | Strong / Sound | [Review](calibration/reviews_anon/ANON_103.md) |
| `B39` | `ANON_79` | `PMC4495769` | *Nat Genet* (2015) | Statistical Genetics | 3.3/3.5 | 2.4/2.5 | 1.9/2.0 | 1.8/2.0 | **9.4** | Exemplary | [Review](calibration/reviews_anon/ANON_79.md) |
| `B40` | `ANON_200` | `PMC4636487` | *Nat Med* (2015) | Transcriptomics & CompBio | 3.2/3.5 | 2.4/2.5 | 1.9/2.0 | 1.9/2.0 | **9.4** | Exemplary | [Review](calibration/reviews_anon/ANON_200.md) |
| `B41` | `ANON_126` | `PMC4944528` | *Science* (2016) | Transcriptomics & CompBio | 2.9/3.5 | 2.2/2.5 | 1.9/2.0 | 1.6/2.0 | **8.6** | Strong / Sound | [Review](calibration/reviews_anon/ANON_126.md) |
| `B42` | `ANON_81` | `PMC5878932` | *Cell* (2017) | Transcriptomics & CompBio | 3.0/3.5 | 2.3/2.5 | 1.9/2.0 | 1.8/2.0 | **9.0** | Exemplary | [Review](calibration/reviews_anon/ANON_81.md) |
| `B43` | `ANON_159` | `PMC4878611` | *RNA* (2016) | Transcriptomics & CompBio | 3.1/3.5 | 2.2/2.5 | 1.9/2.0 | 1.9/2.0 | **9.1** | Exemplary | [Review](calibration/reviews_anon/ANON_159.md) |
| `B44` | `ANON_98` | `PMC8479118` | *Nat Commun* (2021) | Transcriptomics & CompBio | 3.3/3.5 | 2.4/2.5 | 1.9/2.0 | 1.9/2.0 | **9.5** | Exemplary | [Review](calibration/reviews_anon/ANON_98.md) |
| `B45` | `ANON_83` | `PMC7854630` | *Nat Commun* (2021) | Transcriptomics & CompBio | 2.3/3.5 | 1.8/2.5 | 1.6/2.0 | 1.8/2.0 | **7.5** | Strong / Sound | [Review](calibration/reviews_anon/ANON_83.md) |
| `B46` | `ANON_84` | `PMC4431643` | *Science* (2014) | Viral Evolution | 3.2/3.5 | 2.3/2.5 | 1.9/2.0 | 1.8/2.0 | **9.2** | Exemplary | [Review](calibration/reviews_anon/ANON_84.md) |
| `B47` | `ANON_170` | `PMC4499780` | *Nature* (2015) | Viral Evolution | 3.1/3.5 | 2.3/2.5 | 1.9/2.0 | 1.8/2.0 | **9.1** | Exemplary | [Review](calibration/reviews_anon/ANON_170.md) |
| `B48` | `ANON_155` | `PMC5536180` | *Nature* (2017) | Viral Evolution | 3.1/3.5 | 2.3/2.5 | 1.8/2.0 | 1.8/2.0 | **9.0** | Exemplary | [Review](calibration/reviews_anon/ANON_155.md) |
| `B49` | `ANON_196` | `PMC4869911` | *Elife* (2016) | Molecular Evolution | 3.1/3.5 | 2.3/2.5 | 1.9/2.0 | 1.9/2.0 | **9.2** | Exemplary | [Review](calibration/reviews_anon/ANON_196.md) |
| `B50` | `ANON_156` | `PMC3106319` | *Genome Res* (2011) | Molecular Evolution | 2.9/3.5 | 2.1/2.5 | 1.8/2.0 | 1.5/2.0 | **8.3** | Strong / Sound | [Review](calibration/reviews_anon/ANON_156.md) |
| `C01` | `ANON_52` | `PMC11305400` | *Cell Rep* (2024) | Viral Evolution | 2.5/3.5 | 1.9/2.5 | 1.7/2.0 | 1.6/2.0 | **7.7** | Strong / Sound | [Review](calibration/reviews_anon/ANON_52.md) |
| `C02` | `ANON_64` | `PMC12313522` | *Nat Microbiol* (2025) | Viral Evolution | 2.8/3.5 | 2.0/2.5 | 1.8/2.0 | 1.6/2.0 | **8.2** | Strong / Sound | [Review](calibration/reviews_anon/ANON_64.md) |
| `C03` | `ANON_60` | `PMC8011692` | *Emerg Microbes Infect* (2021) | Viral Evolution | 1.7/3.5 | 1.2/2.5 | 1.2/2.0 | 1.2/2.0 | **5.3** | Mixed / Salvageable | [Review](calibration/reviews_anon/ANON_60.md) |
| `C04` | `ANON_58` | `PMC11682804` | *Emerg Infect Dis* (2025) | Viral Evolution | 1.9/3.5 | 1.5/2.5 | 1.6/2.0 | 1.1/2.0 | **6.1** | Mixed / Salvageable | [Review](calibration/reviews_anon/ANON_58.md) |
| `C05` | `ANON_62` | `PMC11281702` | *Viruses* (2024) | Viral Evolution | 1.2/3.5 | 1.1/2.5 | 1.1/2.0 | 1.1/2.0 | **4.5** | Flawed / Overstated | [Review](calibration/reviews_anon/ANON_62.md) |
| `C06` | `ANON_68` | `PMC7105384` | *Elife* (2020) | Molecular Evolution | 1.9/3.5 | 1.5/2.5 | 1.5/2.0 | 1.4/2.0 | **6.3** | Mixed / Salvageable | [Review](calibration/reviews_anon/ANON_68.md) |
| `C07` | `ANON_59` | `PMC10431346` | *Virus Evol* (2022) | Molecular Evolution | 3.1/3.5 | 2.3/2.5 | 1.9/2.0 | 1.7/2.0 | **9.0** | Exemplary | [Review](calibration/reviews_anon/ANON_59.md) |
| `C08` | `ANON_73` | `PMC11040004` | *Nucleic Acids Res* (2024) | Molecular Evolution | 2.8/3.5 | 2.1/2.5 | 1.8/2.0 | 1.8/2.0 | **8.5** | Strong / Sound | [Review](calibration/reviews_anon/ANON_73.md) |
| `C09` | `ANON_54` | `PMC11431564` | *Genes (Basel)* (2024) | Molecular Evolution | 2.1/3.5 | 1.6/2.5 | 1.5/2.0 | 1.3/2.0 | **6.5** | Mixed / Salvageable | [Review](calibration/reviews_anon/ANON_54.md) |
| `C10` | `ANON_69` | `PMC11228553` | *Front Bioinform* (2024) | Molecular Evolution | 1.5/3.5 | 1.2/2.5 | 1.1/2.0 | 1.4/2.0 | **5.2** | Mixed / Salvageable | [Review](calibration/reviews_anon/ANON_69.md) |
| `C11` | `ANON_57` | `PMC10901987` | *Front Microbiol* (2024) | Cancer & Microbiome | 1.7/3.5 | 1.3/2.5 | 1.4/2.0 | 1.5/2.0 | **5.9** | Mixed / Salvageable | [Review](calibration/reviews_anon/ANON_57.md) |
| `C12` | `ANON_71` | `PMC6680985` | *Microorganisms* (2019) | Cancer & Microbiome | 0.6/3.5 | 0.5/2.5 | 0.6/2.0 | 0.8/2.0 | **2.5** | Fundamentally Invalid | [Review](calibration/reviews_anon/ANON_71.md) |
| `C13` | `ANON_63` | `PMC9509681` | *Infect Drug Resist* (2022) | Cancer & Microbiome | 0.5/3.5 | 0.5/2.5 | 0.6/2.0 | 0.5/2.0 | **2.1** | Fundamentally Invalid | [Review](calibration/reviews_anon/ANON_63.md) |
| `C14` | `ANON_66` | `PMC9008261` | *Front Cell Infect Microbiol* (2022) | Cancer & Microbiome | 1.5/3.5 | 1.3/2.5 | 1.3/2.0 | 1.4/2.0 | **5.5** | Mixed / Salvageable | [Review](calibration/reviews_anon/ANON_66.md) |
| `C15` | `ANON_74` | `PMC12354945` | *Cancer Res Commun* (2025) | Cancer & Microbiome | 1.5/3.5 | 1.2/2.5 | 1.3/2.0 | 1.4/2.0 | **5.4** | Mixed / Salvageable | [Review](calibration/reviews_anon/ANON_74.md) |
| `C16` | `ANON_56` | `PMC7617604` | *N Engl J Med* (2025) | Statistical Genetics | 2.3/3.5 | 1.7/2.5 | 1.7/2.0 | 1.5/2.0 | **7.2** | Strong / Sound | [Review](calibration/reviews_anon/ANON_56.md) |
| `C17` | `ANON_65` | `PMC12120081` | *Nat Commun* (2025) | Statistical Genetics | 2.7/3.5 | 2.1/2.5 | 1.7/2.0 | 1.8/2.0 | **8.3** | Strong / Sound | [Review](calibration/reviews_anon/ANON_65.md) |
| `C18` | `ANON_75` | `PMC11711298` | *Plant Genome* (2025) | Statistical Genetics | 0.9/3.5 | 0.9/2.5 | 1.2/2.0 | 1.0/2.0 | **4.0** | Flawed / Overstated | [Review](calibration/reviews_anon/ANON_75.md) |
| `C19` | `ANON_55` | `PMC11610249` | *Front Plant Sci* (2024) | Statistical Genetics | 1.1/3.5 | 1.0/2.5 | 1.1/2.0 | 0.9/2.0 | **4.1** | Flawed / Overstated | [Review](calibration/reviews_anon/ANON_55.md) |
| `C20` | `ANON_67` | `PMC12409340` | *Int J Chron Obstruct Pulmon Dis* (2025) | Statistical Genetics | 1.6/3.5 | 1.3/2.5 | 1.3/2.0 | 1.4/2.0 | **5.6** | Mixed / Salvageable | [Review](calibration/reviews_anon/ANON_67.md) |
| `C21` | `ANON_72` | `PMC11662780` | *J Transl Med* (2024) | Transcriptomics & CompBio | 0.7/3.5 | 0.6/2.5 | 0.8/2.0 | 0.7/2.0 | **2.8** | Fundamentally Invalid | [Review](calibration/reviews_anon/ANON_72.md) |
| `C22` | `ANON_61` | `PMC12622556` | *Adv Sci (Weinh)* (2025) | Transcriptomics & CompBio | 1.2/3.5 | 1.1/2.5 | 1.2/2.0 | 0.9/2.0 | **4.4** | Flawed / Overstated | [Review](calibration/reviews_anon/ANON_61.md) |
| `C23` | `ANON_53` | `PMC10676521` | *Bioinform Adv* (2023) | Transcriptomics & CompBio | 1.2/3.5 | 0.9/2.5 | 1.2/2.0 | 0.9/2.0 | **4.2** | Flawed / Overstated | [Review](calibration/reviews_anon/ANON_53.md) |
| `C24` | `ANON_70` | `PMC12043589` | *Front Cell Dev Biol* (2025) | Transcriptomics & CompBio | 0.8/3.5 | 0.7/2.5 | 0.9/2.0 | 0.8/2.0 | **3.2** | Flawed / Overstated | [Review](calibration/reviews_anon/ANON_70.md) |
| `C25` | `ANON_51` | `PMC12174135` | *Front Cell Dev Biol* (2025) | Transcriptomics & CompBio | 1.0/3.5 | 0.8/2.5 | 1.0/2.0 | 0.7/2.0 | **3.5** | Flawed / Overstated | [Review](calibration/reviews_anon/ANON_51.md) |
| `C26` | `ANON_154` | `PMC7682340` | *Proc Natl Acad Sci U S A* (2020) | Viral Evolution | 2.5/3.5 | 2.0/2.5 | 1.8/2.0 | 1.2/2.0 | **7.5** | Strong / Sound | [Review](calibration/reviews_anon/ANON_154.md) |
| `C27` | `ANON_88` | `PMC7815831` | *Nat Commun* (2021) | Viral Evolution | 2.4/3.5 | 1.7/2.5 | 1.5/2.0 | 1.8/2.0 | **7.4** | Strong / Sound | [Review](calibration/reviews_anon/ANON_88.md) |
| `C28` | `ANON_106` | `PMC7542952` | *BMJ Open* (2020) | Viral Evolution | 2.3/3.5 | 2.1/2.5 | 1.7/2.0 | 1.6/2.0 | **7.7** | Strong / Sound | [Review](calibration/reviews_anon/ANON_106.md) |
| `C29` | `ANON_162` | `PMC8076962` | *JAMA Netw Open* (2021) | Viral Evolution | 1.1/3.5 | 1.0/2.5 | 1.3/2.0 | 0.9/2.0 | **4.3** | Flawed / Overstated | [Review](calibration/reviews_anon/ANON_162.md) |
| `C30` | `ANON_165` | `PMC7857414` | *Sci Transl Med* (2020) | Viral Evolution | 2.2/3.5 | 1.5/2.5 | 1.5/2.0 | 1.6/2.0 | **6.8** | Mixed / Salvageable | [Review](calibration/reviews_anon/ANON_165.md) |
| `C31` | `ANON_147` | `PMC10491582` | *Sci Rep* (2023) | Viral Evolution | 0.9/3.5 | 1.0/2.5 | 1.0/2.0 | 0.9/2.0 | **3.8** | Flawed / Overstated | [Review](calibration/reviews_anon/ANON_147.md) |
| `C32` | `ANON_120` | `PMC7758296` | *Virus Evol* (2020) | Viral Evolution | 1.9/3.5 | 1.6/2.5 | 1.5/2.0 | 1.3/2.0 | **6.3** | Mixed / Salvageable | [Review](calibration/reviews_anon/ANON_120.md) |
| `C33` | `ANON_137` | `PMC6852897` | *BMC Infect Dis* (2019) | Viral Evolution | 2.5/3.5 | 1.8/2.5 | 1.6/2.0 | 1.9/2.0 | **7.8** | Strong / Sound | [Review](calibration/reviews_anon/ANON_137.md) |
| `C34` | `ANON_158` | `PMC9227414` | *Viruses* (2022) | Viral Evolution | 1.1/3.5 | 1.0/2.5 | 1.1/2.0 | 1.0/2.0 | **4.2** | Flawed / Overstated | [Review](calibration/reviews_anon/ANON_158.md) |
| `C35` | `ANON_130` | `PMC10617345` | *Emerg Infect Dis* (2023) | Viral Evolution | 2.3/3.5 | 2.0/2.5 | 1.6/2.0 | 1.2/2.0 | **7.1** | Strong / Sound | [Review](calibration/reviews_anon/ANON_130.md) |
| `C36` | `ANON_190` | `PMC12329429` | *Geohealth* (2025) | Viral Evolution | 1.2/3.5 | 1.1/2.5 | 1.0/2.0 | 1.2/2.0 | **4.5** | Flawed / Overstated | [Review](calibration/reviews_anon/ANON_190.md) |
| `C37` | `ANON_110` | `PMC8697821` | *J Glob Infect Dis* (2021) | Viral Evolution | 1.0/3.5 | 0.9/2.5 | 1.0/2.0 | 0.9/2.0 | **3.8** | Flawed / Overstated | [Review](calibration/reviews_anon/ANON_110.md) |
| `C38` | `ANON_161` | `PMC11382104` | *New Microbes New Infect* (2024) | Viral Evolution | 0.5/3.5 | 0.8/2.5 | 1.1/2.0 | 0.8/2.0 | **3.2** | Flawed / Overstated | [Review](calibration/reviews_anon/ANON_161.md) |
| `C39` | `ANON_131` | `PMC12625292` | *BMC Public Health* (2025) | Viral Evolution | 2.1/3.5 | 1.7/2.5 | 1.2/2.0 | 1.8/2.0 | **6.8** | Mixed / Salvageable | [Review](calibration/reviews_anon/ANON_131.md) |
| `C40` | `ANON_92` | `PMC10871168` | *mSphere* (2023) | Viral Evolution | 2.0/3.5 | 1.5/2.5 | 1.5/2.0 | 1.4/2.0 | **6.4** | Mixed / Salvageable | [Review](calibration/reviews_anon/ANON_92.md) |
| `C41` | `ANON_194` | `PMC10513199` | *PLoS Pathog* (2023) | Molecular Evolution | 2.9/3.5 | 2.2/2.5 | 1.9/2.0 | 1.8/2.0 | **8.8** | Strong / Sound | [Review](calibration/reviews_anon/ANON_194.md) |
| `C42` | `ANON_104` | `PMC9314448` | *Nat Commun* (2022) | Molecular Evolution | 3.2/3.5 | 2.3/2.5 | 1.9/2.0 | 1.8/2.0 | **9.2** | Exemplary | [Review](calibration/reviews_anon/ANON_104.md) |
| `C43` | `ANON_121` | `PMC12129310` | *Cell Host Microbe* (2023) | Molecular Evolution | 3.0/3.5 | 2.2/2.5 | 1.9/2.0 | 1.8/2.0 | **8.9** | Strong / Sound | [Review](calibration/reviews_anon/ANON_121.md) |
| `C44` | `ANON_160` | `PMC9829393` | *Plant Biotechnol J* (2023) | Molecular Evolution | 2.0/3.5 | 1.4/2.5 | 1.5/2.0 | 1.6/2.0 | **6.5** | Mixed / Salvageable | [Review](calibration/reviews_anon/ANON_160.md) |
| `C45` | `ANON_118` | `PMC10765913` | *BMC Genomics* (2024) | Molecular Evolution | 1.8/3.5 | 1.5/2.5 | 1.2/2.0 | 1.3/2.0 | **5.8** | Mixed / Salvageable | [Review](calibration/reviews_anon/ANON_118.md) |
| `C46` | `ANON_151` | `PMC11727194` | *BMC Biol* (2025) | Molecular Evolution | 1.2/3.5 | 1.1/2.5 | 1.1/2.0 | 1.2/2.0 | **4.6** | Flawed / Overstated | [Review](calibration/reviews_anon/ANON_151.md) |
| `C47` | `ANON_127` | `PMC11783303` | *Mol Biol Evol* (2025) | Molecular Evolution | 2.7/3.5 | 2.0/2.5 | 1.7/2.0 | 1.7/2.0 | **8.1** | Strong / Sound | [Review](calibration/reviews_anon/ANON_127.md) |
| `C48` | `ANON_175` | `PMC12122422` | *Gigascience* (2025) | Molecular Evolution | 1.9/3.5 | 1.5/2.5 | 1.5/2.0 | 1.5/2.0 | **6.4** | Mixed / Salvageable | [Review](calibration/reviews_anon/ANON_175.md) |
| `C49` | `ANON_184` | `PMC11545642` | *BMC Plant Biol* (2024) | Molecular Evolution | 2.1/3.5 | 1.8/2.5 | 1.6/2.0 | 1.9/2.0 | **7.4** | Strong / Sound | [Review](calibration/reviews_anon/ANON_184.md) |
| `C50` | `ANON_133` | `PMC10448532` | *iScience* (2023) | Molecular Evolution | 2.4/3.5 | 2.0/2.5 | 1.6/2.0 | 1.5/2.0 | **7.5** | Strong / Sound | [Review](calibration/reviews_anon/ANON_133.md) |
| `C51` | `ANON_181` | `PMC12260425` | *Proc Natl Acad Sci U S A* (2025) | Molecular Evolution | 2.6/3.5 | 1.9/2.5 | 1.7/2.0 | 1.8/2.0 | **8.0** | Strong / Sound | [Review](calibration/reviews_anon/ANON_181.md) |
| `C52` | `ANON_143` | `PMC12473017` | *Microorganisms* (2025) | Molecular Evolution | 1.4/3.5 | 1.4/2.5 | 1.3/2.0 | 1.1/2.0 | **5.2** | Mixed / Salvageable | [Review](calibration/reviews_anon/ANON_143.md) |
| `C53` | `ANON_129` | `PMC11332805` | *Front Microbiol* (2024) | Molecular Evolution | 1.5/3.5 | 1.2/2.5 | 1.2/2.0 | 1.5/2.0 | **5.4** | Mixed / Salvageable | [Review](calibration/reviews_anon/ANON_129.md) |
| `C54` | `ANON_169` | `PMC11939762` | *Animals (Basel)* (2025) | Molecular Evolution | 1.4/3.5 | 1.4/2.5 | 1.3/2.0 | 1.2/2.0 | **5.3** | Mixed / Salvageable | [Review](calibration/reviews_anon/ANON_169.md) |
| `C55` | `ANON_153` | `PMC12732342` | *Genes (Basel)* (2025) | Molecular Evolution | 1.5/3.5 | 1.3/2.5 | 1.3/2.0 | 1.3/2.0 | **5.4** | Mixed / Salvageable | [Review](calibration/reviews_anon/ANON_153.md) |
| `C56` | `ANON_188` | `PMC10730209` | *Gut Microbes* (2024) | Cancer & Microbiome | 2.3/3.5 | 2.0/2.5 | 1.8/2.0 | 1.4/2.0 | **7.5** | Strong / Sound | [Review](calibration/reviews_anon/ANON_188.md) |
| `C57` | `ANON_112` | `PMC11191305` | *Microbiome* (2024) | Cancer & Microbiome | 1.5/3.5 | 1.4/2.5 | 1.5/2.0 | 1.1/2.0 | **5.5** | Mixed / Salvageable | [Review](calibration/reviews_anon/ANON_112.md) |
| `C58` | `ANON_90` | `PMC11291933` | *NPJ Biofilms Microbiomes* (2024) | Cancer & Microbiome | 2.6/3.5 | 2.0/2.5 | 1.6/2.0 | 1.8/2.0 | **8.0** | Strong / Sound | [Review](calibration/reviews_anon/ANON_90.md) |
| `C59` | `ANON_105` | `PMC11668851` | *Transl Psychiatry* (2024) | Cancer & Microbiome | 1.7/3.5 | 1.4/2.5 | 1.5/2.0 | 1.4/2.0 | **6.0** | Mixed / Salvageable | [Review](calibration/reviews_anon/ANON_105.md) |
| `C60` | `ANON_101` | `PMC10256650` | *Curr Microbiol* (2023) | Cancer & Microbiome | 1.1/3.5 | 1.0/2.5 | 1.0/2.0 | 1.2/2.0 | **4.3** | Flawed / Overstated | [Review](calibration/reviews_anon/ANON_101.md) |
| `C61` | `ANON_171` | `PMC11316369` | *Respir Res* (2024) | Cancer & Microbiome | 1.3/3.5 | 1.1/2.5 | 1.2/2.0 | 1.2/2.0 | **4.8** | Flawed / Overstated | [Review](calibration/reviews_anon/ANON_171.md) |
| `C62` | `ANON_100` | `PMC11755556` | *J Xenobiot* (2025) | Cancer & Microbiome | 1.2/3.5 | 1.1/2.5 | 1.1/2.0 | 1.3/2.0 | **4.7** | Flawed / Overstated | [Review](calibration/reviews_anon/ANON_100.md) |
| `C63` | `ANON_76` | `PMC12413070` | *Gut Microbes* (2025) | Cancer & Microbiome | 1.9/3.5 | 1.5/2.5 | 1.4/2.0 | 1.7/2.0 | **6.5** | Mixed / Salvageable | [Review](calibration/reviews_anon/ANON_76.md) |
| `C64` | `ANON_82` | `PMC11537008` | *Microbiol Spectr* (2024) | Cancer & Microbiome | 1.0/3.5 | 1.0/2.5 | 1.0/2.0 | 1.2/2.0 | **4.2** | Flawed / Overstated | [Review](calibration/reviews_anon/ANON_82.md) |
| `C65` | `ANON_132` | `PMC12234824` | *Sci Rep* (2025) | Cancer & Microbiome | 1.0/3.5 | 0.7/2.5 | 0.8/2.0 | 1.0/2.0 | **3.5** | Flawed / Overstated | [Review](calibration/reviews_anon/ANON_132.md) |
| `C66` | `ANON_148` | `PMC12697481` | *Bioinformation* (2025) | Cancer & Microbiome | 0.5/3.5 | 0.6/2.5 | 0.6/2.0 | 0.4/2.0 | **2.1** | Fundamentally Invalid | [Review](calibration/reviews_anon/ANON_148.md) |
| `C67` | `ANON_115` | `PMC11928979` | *Comput Struct Biotechnol J* (2025) | Cancer & Microbiome | 1.2/3.5 | 1.1/2.5 | 1.1/2.0 | 0.9/2.0 | **4.3** | Flawed / Overstated | [Review](calibration/reviews_anon/ANON_115.md) |
| `C68` | `ANON_142` | `PMC12070606` | *BMC Vet Res* (2025) | Cancer & Microbiome | 1.1/3.5 | 1.2/2.5 | 1.1/2.0 | 0.9/2.0 | **4.3** | Flawed / Overstated | [Review](calibration/reviews_anon/ANON_142.md) |
| `C69` | `ANON_197` | `PMC12647101` | *Front Microbiol* (2025) | Cancer & Microbiome | 1.1/3.5 | 1.0/2.5 | 1.0/2.0 | 1.4/2.0 | **4.5** | Flawed / Overstated | [Review](calibration/reviews_anon/ANON_197.md) |
| `C70` | `ANON_157` | `PMC12383627` | *Biology (Basel)* (2025) | Cancer & Microbiome | 1.0/3.5 | 0.9/2.5 | 0.9/2.0 | 1.2/2.0 | **4.0** | Flawed / Overstated | [Review](calibration/reviews_anon/ANON_157.md) |
| `C71` | `ANON_122` | `PMC11379490` | *Eur Heart J* (2024) | Statistical Genetics | 1.9/3.5 | 1.5/2.5 | 1.6/2.0 | 1.2/2.0 | **6.2** | Mixed / Salvageable | [Review](calibration/reviews_anon/ANON_122.md) |
| `C72` | `ANON_144` | `PMC10864389` | *Commun Biol* (2024) | Statistical Genetics | 2.1/3.5 | 1.6/2.5 | 1.4/2.0 | 1.5/2.0 | **6.6** | Mixed / Salvageable | [Review](calibration/reviews_anon/ANON_144.md) |
| `C73` | `ANON_198` | `PMC11367857` | *Hum Genomics* (2024) | Statistical Genetics | 1.4/3.5 | 1.3/2.5 | 1.4/2.0 | 1.5/2.0 | **5.6** | Mixed / Salvageable | [Review](calibration/reviews_anon/ANON_198.md) |
| `C74` | `ANON_116` | `PMC11410272` | *PLoS One* (2024) | Statistical Genetics | 2.8/3.5 | 2.1/2.5 | 1.7/2.0 | 1.4/2.0 | **8.0** | Strong / Sound | [Review](calibration/reviews_anon/ANON_116.md) |
| `C75` | `ANON_185` | `PMC11220366` | *J Cell Mol Med* (2024) | Statistical Genetics | 1.4/3.5 | 1.3/2.5 | 1.4/2.0 | 1.1/2.0 | **5.2** | Mixed / Salvageable | [Review](calibration/reviews_anon/ANON_185.md) |
| `C76` | `ANON_114` | `PMC11786572` | *BMC Plant Biol* (2025) | Statistical Genetics | 1.2/3.5 | 1.0/2.5 | 1.1/2.0 | 1.3/2.0 | **4.6** | Flawed / Overstated | [Review](calibration/reviews_anon/ANON_114.md) |
| `C77` | `ANON_134` | `PMC12189426` | *Animals (Basel)* (2025) | Statistical Genetics | 1.6/3.5 | 1.3/2.5 | 1.3/2.0 | 1.4/2.0 | **5.6** | Mixed / Salvageable | [Review](calibration/reviews_anon/ANON_134.md) |
| `C78` | `ANON_176` | `PMC12128320` | *Genet Sel Evol* (2025) | Statistical Genetics | 2.1/3.5 | 1.6/2.5 | 1.5/2.0 | 1.3/2.0 | **6.5** | Mixed / Salvageable | [Review](calibration/reviews_anon/ANON_176.md) |
| `C79` | `ANON_117` | `PMC12361393` | *Commun Biol* (2025) | Statistical Genetics | 1.2/3.5 | 1.1/2.5 | 1.2/2.0 | 1.0/2.0 | **4.5** | Flawed / Overstated | [Review](calibration/reviews_anon/ANON_117.md) |
| `C80` | `ANON_87` | `PMC11161523` | *Sci Rep* (2024) | Statistical Genetics | 1.3/3.5 | 1.0/2.5 | 1.1/2.0 | 1.1/2.0 | **4.5** | Flawed / Overstated | [Review](calibration/reviews_anon/ANON_87.md) |
| `C81` | `ANON_107` | `PMC12351922` | *Cardiovasc Diabetol* (2025) | Statistical Genetics | 1.5/3.5 | 1.3/2.5 | 1.3/2.0 | 1.1/2.0 | **5.2** | Mixed / Salvageable | [Review](calibration/reviews_anon/ANON_107.md) |
| `C82` | `ANON_149` | `PMC11165082` | *Front Plant Sci* (2024) | Statistical Genetics | 1.1/3.5 | 1.1/2.5 | 1.2/2.0 | 1.0/2.0 | **4.4** | Flawed / Overstated | [Review](calibration/reviews_anon/ANON_149.md) |
| `C83` | `ANON_182` | `PMC11238174` | *Front Med (Lausanne)* (2024) | Statistical Genetics | 0.9/3.5 | 0.7/2.5 | 0.9/2.0 | 0.8/2.0 | **3.3** | Flawed / Overstated | [Review](calibration/reviews_anon/ANON_182.md) |
| `C84` | `ANON_125` | `PMC12290206` | *Asian Pac J Cancer Prev* (2025) | Statistical Genetics | 0.4/3.5 | 0.4/2.5 | 0.5/2.0 | 0.5/2.0 | **1.8** | Fundamentally Invalid | [Review](calibration/reviews_anon/ANON_125.md) |
| `C85` | `ANON_135` | `PMC12729862` | *BMC Public Health* (2025) | Statistical Genetics | 1.9/3.5 | 1.5/2.5 | 1.5/2.0 | 1.3/2.0 | **6.2** | Mixed / Salvageable | [Review](calibration/reviews_anon/ANON_135.md) |
| `C86` | `ANON_167` | `PMC11221317` | *J Cell Mol Med* (2024) | Transcriptomics & CompBio | 1.3/3.5 | 1.0/2.5 | 1.2/2.0 | 0.9/2.0 | **4.4** | Flawed / Overstated | [Review](calibration/reviews_anon/ANON_167.md) |
| `C87` | `ANON_164` | `PMC11663015` | *Brief Bioinform* (2024) | Transcriptomics & CompBio | 1.3/3.5 | 1.2/2.5 | 1.0/2.0 | 1.3/2.0 | **4.8** | Flawed / Overstated | [Review](calibration/reviews_anon/ANON_164.md) |
| `C88` | `ANON_163` | `PMC12647882` | *Nat Commun* (2025) | Transcriptomics & CompBio | 1.9/3.5 | 1.5/2.5 | 1.6/2.0 | 1.6/2.0 | **6.6** | Mixed / Salvageable | [Review](calibration/reviews_anon/ANON_163.md) |
| `C89` | `ANON_113` | `PMC12291316` | *Cardiovasc Diabetol* (2025) | Transcriptomics & CompBio | 1.4/3.5 | 1.3/2.5 | 1.5/2.0 | 1.2/2.0 | **5.4** | Mixed / Salvageable | [Review](calibration/reviews_anon/ANON_113.md) |
| `C90` | `ANON_174` | `PMC11974051` | *Genome Biol* (2025) | Transcriptomics & CompBio | 2.6/3.5 | 2.1/2.5 | 1.6/2.0 | 1.6/2.0 | **7.9** | Strong / Sound | [Review](calibration/reviews_anon/ANON_174.md) |
| `C91` | `ANON_96` | `PMC11988464` | *Int J Mol Sci* (2025) | Transcriptomics & CompBio | 1.0/3.5 | 0.9/2.5 | 1.0/2.0 | 0.6/2.0 | **3.5** | Flawed / Overstated | [Review](calibration/reviews_anon/ANON_96.md) |
| `C92` | `ANON_108` | `PMC12241668` | *Front Immunol* (2025) | Transcriptomics & CompBio | 0.2/3.5 | 0.2/2.5 | 0.4/2.0 | 0.4/2.0 | **1.2** | Fundamentally Invalid | [Review](calibration/reviews_anon/ANON_108.md) |
| `C93` | `ANON_166` | `PMC11700820` | *Front Immunol* (2024) | Transcriptomics & CompBio | 1.0/3.5 | 1.0/2.5 | 1.0/2.0 | 0.8/2.0 | **3.8** | Flawed / Overstated | [Review](calibration/reviews_anon/ANON_166.md) |
| `C94` | `ANON_86` | `PMC12133857` | *Front Immunol* (2025) | Transcriptomics & CompBio | 0.5/3.5 | 0.4/2.5 | 0.6/2.0 | 0.7/2.0 | **2.2** | Fundamentally Invalid | [Review](calibration/reviews_anon/ANON_86.md) |
| `C95` | `ANON_146` | `PMC12499553` | *Biomol Biomed* (2025) | Transcriptomics & CompBio | 1.2/3.5 | 1.1/2.5 | 1.2/2.0 | 1.0/2.0 | **4.5** | Flawed / Overstated | [Review](calibration/reviews_anon/ANON_146.md) |
| `C96` | `ANON_172` | `PMC12467303` | *Biology (Basel)* (2025) | Transcriptomics & CompBio | 1.1/3.5 | 1.0/2.5 | 0.9/2.0 | 1.2/2.0 | **4.2** | Flawed / Overstated | [Review](calibration/reviews_anon/ANON_172.md) |
| `C97` | `ANON_89` | `PMC12185455` | *Front Immunol* (2025) | Transcriptomics & CompBio | 1.2/3.5 | 1.0/2.5 | 1.0/2.0 | 0.8/2.0 | **4.0** | Flawed / Overstated | [Review](calibration/reviews_anon/ANON_89.md) |
| `C98` | `ANON_183` | `PMC11663206` | *Cancer Immunol Immunother* (2024) | Transcriptomics & CompBio | 1.8/3.5 | 1.5/2.5 | 1.5/2.0 | 1.6/2.0 | **6.4** | Mixed / Salvageable | [Review](calibration/reviews_anon/ANON_183.md) |
| `C99` | `ANON_168` | `PMC12603141` | *Sci Rep* (2025) | Transcriptomics & CompBio | 1.4/3.5 | 1.5/2.5 | 1.4/2.0 | 1.6/2.0 | **5.9** | Mixed / Salvageable | [Review](calibration/reviews_anon/ANON_168.md) |
| `C100` | `ANON_85` | `PMC12623444` | *Commun Biol* (2025) | Transcriptomics & CompBio | 0.9/3.5 | 0.8/2.5 | 0.9/2.0 | 1.2/2.0 | **3.8** | Flawed / Overstated | [Review](calibration/reviews_anon/ANON_85.md) |

