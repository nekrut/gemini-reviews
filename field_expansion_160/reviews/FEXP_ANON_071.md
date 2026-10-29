# Review of FEXP_ANON_071

**Overall Score:** **7.5 / 10.0** (Strong / Sound) | **Scientific Core Score:** **5.9 / 8.0**  
* **Score Breakdown:** Rigor: 2.5/3.5 | Claims: 1.8/2.5 | Biology: 1.6/2.0 | Reproducibility: 1.6/2.0

---

## 1. Blinded Metadata Perception
* **Perceived Subfield & Study Design:** Multi-Omics Cardiovascular Genetics & Drug Target Discovery / Proteome-Wide and Phenome-Wide Bidirectional Mendelian Randomization (MR), Multivariable MR (`MRBEE`), Multi-Trait Bayesian Colocalization (`HyPrColoc`), and Single-Nucleus RNA-seq Integration.
* **Data Sources:** UK Biobank Pharma Proteomics Project (UKB-PPP; 2,940 Olink proteins in $46,595$ individuals, including $34,557$ European and $262$ East Asian participants), FinnGen Olink validation cohort ($N = 1,225$), 19 cardiovascular disease (CVD) and 128 phenome-wide GWASs from UKB + FinnGen ($N = 449,000$ EUR) and Biobank Japan ($N = 179,000$ EAS; Sakaue et al.), GTEx v8 eQTLs (49 tissues), and human left ventricular snRNA-seq from 42 donors (`SCP1303`: 11 DCM, 15 HCM, 16 non-failing; Chaffin et al.).
* **Perceived Venue Tier:** High-tier multidisciplinary or translational biomedical journal.

---

## 2. Executive Summary & Editorial Verdict

This study conducts a bidirectional proteome-wide Mendelian randomization (MR) screen across 2,940 circulating plasma proteins (from the UKB-PPP resource) and 19 cardiovascular diseases (CVDs) in European and East Asian cohorts, supplemented by pQTL validation in FinnGen Olink ($N = 1,225$), pleiotropy-robust sensitivity estimators (`MR-PRESSO`, `GSMR2` HEIDI-outlier), bias-corrected multivariable MR (`MRBEE`), multi-trait Bayesian colocalization (`HyPrColoc` across plasma pQTLs, 49 GTEx tissue eQTLs, and CVD GWASs), a phenome-wide MR scan across 128 diseases, and donor-level pseudobulk single-nucleus RNA-seq analyses in 42 human left ventricular biopsies (DCM, HCM, and non-failing hearts). Forward MR identifies 218 proteins associated with at least one CVD at Bonferroni significance ($106$ using *cis*-pQTLs only; $182$ using *cis*- + *trans*-pQTLs), of which 102 replicate at $\text{FDR} < 5\%$ using FinnGen Olink pQTLs. Reverse MR identifies 15 disease-driven protein biomarkers (including *NPPB* for dilated cardiomyopathy and 5 East Asian-specific signals), with only 2 proteins (*LGALS4*, *MMP12*) overlapping between forward and reverse MR.

**Editorial Verdict: Minor-to-Moderate Revision (Strong / Sound).** This is a well-executed, methodologically thorough multi-omics investigation that separates *cis*-only from *cis*+*trans* instruments, enforces strict Bonferroni thresholds in discovery, applies `MRBEE` to address shared *trans*-pQTL pleiotropy, uses `HyPrColoc` across 49 tissues, and properly aggregates snRNA-seq counts into donor-level TMM/limma-voom pseudobulks (avoiding cell-level pseudoreplication). Nevertheless, four substantive methodological and biological caveats should be addressed: (1) the "FinnGen Olink replication" replaces the exposure pQTLs with FinnGen Olink ($N = 1,225$) but retains the *same* discovery CVD outcome GWAS (UKB + FinnGen meta-analysis), making it an exposure-instrument replication rather than a fully independent outcome replication; (2) the headline novel target *BTN3A2* (alongside *BTN2A1*) resides at `6p22.2` in the extended Major Histocompatibility Complex (MHC) Class I region, requiring explicit conditioning on extended HLA/MHC linkage disequilibrium; (3) the Asian forward-MR arm uses an underpowered UKB-PPP East Asian sample ($N = 262$) paired with an "all-Asian" UK Biobank LD reference ($N = 2,783$, predominantly South Asian) that mismatches East Asian (Biobank Japan) LD structure; and (4) primary univariable IVW uses a relatively permissive $R^2 < 0.1$ ($500\text{ kb}$) clumping threshold without LD-matrix adjustment.

### Assessment of Specific Conclusions
* **Claim 1: Forward MR identifies 218 causal protein candidates for 19 CVDs (106 via *cis*-pQTLs, 182 via *cis*+*trans*-pQTLs), with 102 replicating at $\text{FDR} < 5\%$ using FinnGen Olink pQTLs and 32 colocalizing ($\text{PP} > 0.8$) via `HyPrColoc`:** `[Well Supported]`  
  The discovery pipeline uses stringent Bonferroni control ($P < 1.74 \times 10^{-7}$ for *cis*-only; $P < 1.27 \times 10^{-7}$ for *cis*+*trans*), recovers established clinical targets (*PCSK9*, *ANGPTL3*, *LPA*, *ECE1*), and corroborates multi-SNP signals with `MR-PRESSO`, `GSMR2`, `MRBEE` ($R^2 < 0.01$), and `HyPrColoc`. Caveat: the FinnGen Olink validation tests independent pQTL estimates against the same outcome summary statistics, and primary univariable IVW clumped at $R^2 < 0.1$ may slightly inflate precision for multi-SNP *cis* loci that did not colocalize.
* **Claim 2: Forward and reverse MR identify largely non-overlapping sets of proteins (218 causal targets vs. 15 consequence biomarkers; only *LGALS4* and *MMP12* overlap), recovery of *NPPB* as a DCM consequence biomarker:** `[Well Supported]`  
  Identifying *NPPB* (encoding preproBNP) in reverse MR specifically as a consequence of dilated cardiomyopathy (and confirming its cardiomyocyte-specific upregulation in DCM snRNA-seq, Fig. 6B) provides a compelling positive control demonstrating that bidirectional MR successfully separates downstream clinical biomarkers from upstream causal drivers.
* **Claim 3: *BTN3A2* (and *BTN2A1*) are novel protective causal drug targets for ischemic stroke acting via $\text{V}\gamma 9\text{V}\delta 2$ T-cell immunomodulation:** `[Fragile]`  
  *BTN3A2* and *BTN2A1* are located adjacent to one another in the butyrophilin cluster at `6p22.2` within the extended MHC Class I region, which harbors complex, long-range linkage disequilibrium spanning megabases and dense local gene pleiotropy. Without conditional analysis adjusting for neighbouring MHC/HLA alleles and *BTN2A1*/*BTN3A1*/*BTN3A3* expression—and without ruling out epitope cross-reactivity among the highly homologous BTN3A paralogs on the Olink platform—attributing the `6p22.2` stroke signal specifically to *BTN3A2* protein agonism remains tentative.
* **Claim 4: Single-cell pseudobulk integration prioritizes *PAM*, *LPL*, *NPPB*, and *FURIN* with cell-type-specific enrichment and differential expression in human cardiomyopathy:** `[Well Supported]`  
  The authors appropriately construct donor-by-cell-type pseudobulk profiles across the 42 left ventricular samples (`SCP1303`), normalize via `edgeR` TMM, and test differential expression using `limma-voom` adjusted for age and sex at $\text{FDR}_{\text{BH}} < 0.01$.

---

## 3. Forensic Defect Inventory

### 1. [Major] Extended MHC (`6p22.2`) Linkage Disequilibrium Confounding for Headline Target *BTN3A2* and *BTN2A1*
* **Location:** Abstract (Line 5), Results (Line 109, Figure 3), and Discussion (Lines 154, 157–161).
* **Defect:** The manuscript highlights *BTN3A2* (alongside *BTN2A1*) as its flagship novel therapeutic target for ischemic stroke. However, *BTN3A2* (`chr6:26,365,387–26,378,326`, GRCh38) and *BTN2A1* (`chr6:26,457,904–26,476,620`) reside less than $100\text{ kb}$ apart inside the extended MHC Class I region on chromosome `6p22.2`. First, within a $\pm 1\text{ Mb}$ *cis*-pQTL window (Line 35), the *cis*-instruments for *BTN3A2* and *BTN2A1* physically overlap and tag shared extended MHC haplotypes (which also encompass *HFE*, histone cluster genes, and *BTN3A1*/*BTN3A3*). Second, standard *cis*-MR Guidelines frequently exclude or flag the extended MHC (`chr6:25–34 Mb`) because long-range LD violates instrumental variable exclusion restrictions. Third, *BTN3A2* shares $>90\%$ extracellular sequence identity with *BTN3A1* and *BTN3A3*, creating a known risk of affinity-proteomics cross-reactivity.
* **Remediation:** Perform conditional/multivariable *cis*-MR (`MRBEE` or `GCTA-COJO` + `HyPrColoc`) jointly modeling *BTN3A2*, *BTN2A1*, *BTN3A1*, *BTN3A3*, and classical HLA/MHC markers at `6p22.2` to determine whether *BTN3A2* and *BTN2A1* represent a single shared MHC haplotype signal, and explicitly note the `6p22.2` extended-MHC location as a caveat in the Discussion.

### 2. [Major] Sub-Continental LD Mismatch ($N = 2,783$ All-Asian UKB Reference) and Severe Underpowering ($N = 262$ EAS) in Asian Forward-MR
* **Location:** Experimental Section "Forward-MR" and "Reverse-MR" (Lines 35, 44) and Discussion (Line 15).
* **Defect:** In Line 35, the authors state that UKB-PPP included $262$ East Asian (`EAS`), $920$ Central/South Asian (`CSA`), and $308$ Middle Eastern participants, and that *"LD was calculated based on a randomly selected subset of Caucasian (n = 10 000) or all Asian (n = 2783) participants in the UK Biobank for Europeans and Asians, respectively."* In the UK Biobank, "all Asian" ($N = 2,783$) is overwhelmingly South Asian (Indian, Pakistani, Bangladeshi; $>80\%$). Using a predominantly South Asian genotype panel to compute LD clumping and proxy selection ($R^2 > 0.7$) for an East Asian pQTL dataset ($N = 262$) paired with an East Asian outcome cohort (Biobank Japan, $N = 179,000$) conflates South Asian and East Asian LD structures.
* **Remediation:** Restrict the Asian LD reference panel strictly to East Asian (`EAS`) individuals (e.g., 1000 Genomes EAS or UK Biobank genetically inferred EAS) rather than pooling South and East Asians, and clarify in the Results/Abstract that all 5 Asian signals arose from Reverse-MR (Biobank Japan exposure) due to the tiny $N = 262$ sample size in UKB-PPP EAS Forward-MR.

### 3. [Moderate] Partial Circularity in "FinnGen Olink Replication" and $R^2 < 0.1$ Primary Clumping
* **Location:** Experimental Section "Forward-MR" (Lines 35, 37) and Results (Line 104).
* **Defect:**
  1. In the replication analysis (Line 37), the authors replace the UKB-PPP exposure pQTLs with FinnGen Olink pQTLs ($N = 1,225$) but test them against the *same* CVD outcome summary statistics (the UKB + FinnGen meta-analysis from Sakaue et al.). Because the outcome GWAS is unchanged (and actually overlaps with the FinnGen Olink cohort), this validates the pQTL exposure instruments in an independent cohort but does not constitute an independent outcome replication.
  2. Primary univariable IVW clumped instruments at $R^2 < 0.1$ within $500\text{ kb}$ without accounting for inter-variant LD correlations in the IVW variance estimator (whereas `MRBEE` properly used $R^2 < 0.01$).
* **Remediation:** State explicitly that the FinnGen Olink analysis replicates the pQTL exposure instruments against the same outcome meta-GWAS, and verify that all 106 *cis*-only candidate proteins remain Bonferroni-significant when clumped at $R^2 < 0.001$ or when evaluated using LD-adjusted generalized IVW.

### 4. [Minor] Find-and-Replace Typo in Figure 4 Caption and Missing Citation Brackets
* **Location:** Experimental Section (Lines 30, 49, 89) and Figure 4 Caption (Line 122).
* **Defect:**
  1. In the Figure 4 legend (Line 122), the abbreviation `SAP` (Stable angina pectoris) is printed as `SAP: Supplemental Table angina pectoris`—an obvious automated regex replacement artifact where `"ST"` or `"Stable"` was replaced with `"Supplemental Table"`.
  2. Lines 30, 49, and 89 contain unclosed citation brackets: `median weighted 24 ]`, `MR-PRESSO 26 ]`, `MRBEE 29 ]`, `DrugCentral Postgres v14.5 36 ]`, `GWAS Catalog 37 ]`, `ClinVar 38 ]`, `ClinGen 39 ]`.
* **Remediation:** Fix `SAP: Stable angina pectoris` in the Figure 4 caption and restore the missing opening brackets `[` for citations 24, 26, 29, 36, 37, 38, and 39.

---

## 4. Quantitative Rubric Scoring

| Rubric Dimension | Score | Max | Forensic Justification |
| :--- | :---: | :---: | :--- |
| **1. Methodological & Statistical Rigor** | **2.5** | **3.5** | Strong multi-layered design (Bonferroni discovery threshold, *cis* vs. *cis*+*trans* stratification, `MRBEE` multivariable MR, `GSMR2`/`MR-PRESSO`, `HyPrColoc` across 49 tissues, and proper donor-level pseudobulk `limma-voom` snRNA-seq); deductions for pooling South/East Asians in the $N=2,783$ LD panel, $R^2 < 0.1$ unadjusted primary clumping, and shared outcome GWAS in replication. |
| **2. Claim-to-Evidence Alignment** | **1.8** | **2.5** | Claims are well-calibrated and thoroughly contextualized; main deduction is for promoting *BTN3A2* and *BTN2A1* as independent stroke targets without addressing their physical adjacency ($<100\text{ kb}$) in the extended MHC Class I region (`6p22.2`). |
| **3. Data Integrity & Biological Plausibility** | **1.6** | **2.0** | Strong biological integration across plasma proteomics, GTEx bulk tissues, and cardiac single-nucleus transcriptomics, including positive controls (*PCSK9*, *ANGPTL3*, *LPA*, *NPPB*). |
| **4. Reproducibility & Data Integrity** | **1.6** | **2.0** | All public repositories (AWS `ukbppp`, GWAS Catalog accessions, Broad Single Cell Portal `SCP1303`) and software packages are clearly documented; minor deductions for the regex typo in Figure 4 (`Supplemental Table angina pectoris`) and missing bracket typos. |
| **Scientific Core Score** | **5.9** | **8.0** | Sum of Rigor + Claims + Biology. |
| **Total Composite Score** | **7.5** | **10.0** | **Strong / Sound** (75 / 100 equivalent). |
