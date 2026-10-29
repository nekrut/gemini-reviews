# Review of FEXP_ANON_067

**Overall Score:** **3.6 / 10.0** (Flawed / Overstated) | **Scientific Core Score:** **2.6 / 8.0**  
* **Score Breakdown:** Rigor: 1.0/3.5 | Claims: 0.8/2.5 | Biology: 0.8/2.0 | Reproducibility: 1.0/2.0

---

## 1. Blinded Metadata Perception
* **Perceived Subfield & Study Design:** Genomic Drug Target Prioritization / Cis-eQTL Mendelian Randomization, Bayesian Colocalization, Summary-data-based MR (SMR), Phenome-Wide Association Study (PheWAS), Molecular Docking, and Two-Step Epigenetic Mediation MR in bronchiectasis.
* **Data Sources:** Blood cis-eQTLs from the eQTLGen Consortium ($N = 31,684$; 2,525 druggable genes), bronchiectasis GWAS from FinnGen R11 ($2,597$ cases and $372,627$ controls), blood mQTLs from GoDMC, and druggability/compound annotations from DSigDB, PubChem, and PDB.
* **Perceived Venue Tier:** Specialized respiratory or translational genomics journal (multi-stage bioinformatic pipeline manuscript).

---

## 2. Executive Summary & Editorial Verdict

This manuscript screens 2,525 druggable genes with blood cis-eQTLs in eQTLGen against bronchiectasis in FinnGen R11 ($2,597$ cases, $372,627$ controls) using two-sample Mendelian randomization (MR), followed by Bayesian colocalization (`coloc`), SMR/HEIDI testing, UK Biobank PheWAS lookup, DSigDB compound enrichment, molecular docking, and two-step mQTL-eQTL-bronchiectasis mediation MR. The authors identify 10 genes passing $\text{FDR} < 0.05$ in primary IVW MR, prioritize *VRK2* as their sole "Tier 1" drug target ($\text{OR}_{\text{MR}} = 1.36, P = 2.17 \times 10^{-6}$; $\text{PP.H4} = 0.784$; $\text{OR}_{\text{SMR}} = 2.18, P = 3.63 \times 10^{-3}$), dock five DSigDB compounds to *VRK2* (PDB: `9FET`), and report that DNA methylation at `cg21568453` mediates 54% of its protective effect on bronchiectasis via *VRK2* expression.

**Editorial Verdict: Reject / Major Re-analysis Required (Flawed / Overstated).** While the multi-step integration of colocalization and SMR/HEIDI is better structured than a bare two-sample MR screen, the primary discovery pipeline rests on a fundamental statistical flaw: clumping cis-eQTLs at a liberal linkage disequilibrium threshold ($r^2 < 0.1$) and feeding $6\text{--}33$ correlated cis-SNPs per gene into standard unadjusted `TwoSampleMR` IVW (which assumes $r^2 = 0$). This double-counting of correlated variants within the same cis-locus artificially deflates standard errors and inflates test statistics—which is why none of the 10 genes reach genome-wide significance in single-variant SMR (where *ACVR2A* collapses from $P_{\text{IVW}} = 9.92 \times 10^{-8}$ to $P_{\text{SMR}} = 0.549$, and *VRK2* drops from $P_{\text{IVW}} = 2.17 \times 10^{-6}$ to $P_{\text{SMR}} = 3.63 \times 10^{-3}$, which fails multiple-testing correction across 2,525 genes). Furthermore, the drug prediction and docking section includes blatant bioinformatic curation failures (proposing industrial **Phenol** as a candidate drug and docking **Bosutinib** twice under both its generic name and its DSigDB assay title `"SKI-606 Kinome Scan"`, without reporting any binding energies in Table 3), and the two-step cis-mQTL/cis-eQTL mediation analysis does not account for shared cis-LD between mQTL and eQTL instruments.

### Assessment of Specific Conclusions
* **Claim 1: Ten druggable genes are significantly associated with bronchiectasis at $\text{FDR} < 0.05$ in genome-wide cis-MR:** `[Methodologically Flawed]`  
  All 10 genes were identified using standard unadjusted IVW across $6\text{--}33$ cis-SNPs clumped at $r^2 < 0.1$ within a $10,000\text{ kb}$ window (Table 1). Standard IVW in `TwoSampleMR` treats all instruments as independent; Residual LD ($0 < r^2 < 0.1$) among $15\text{--}33$ SNPs in a single cis-locus severely inflates Type I error. When evaluated via SMR (which uses the top cis-eQTL and thus avoids LD double-counting, Table 2), *ACVR2A* ($P_{\text{SMR}} = 0.549$) and *CASP9* ($P_{\text{SMR}} = 0.452$) are completely null, three genes (*ACLY*, *SOD2*, *SRPK1*) have `NA` SMR results, and the remaining five genes have nominal $P_{\text{SMR}}$ between $2.91 \times 10^{-3}$ and $1.79 \times 10^{-2}$—none of which survive FDR or Bonferroni correction across 2,525 tested genes.
* **Claim 2: *VRK2* is a validated Tier 1 causal drug target for bronchiectasis supported by MR, colocalization ($\text{PP.H4} = 0.784$), and SMR ($P = 3.63 \times 10^{-3}$):** `[Fragile]`  
  While *VRK2* shows moderate colocalization ($\text{PP.H4} = 0.784$) and passes the HEIDI test ($P_{\text{HEIDI}} = 0.295$), its single-instrument SMR association ($P = 3.63 \times 10^{-3}$) does not survive multiple-testing correction across the 2,525 screened genes, and the analysis relies exclusively on whole-blood eQTLs rather than lung or airway epithelial tissue.
* **Claim 3: DSigDB and molecular docking identify five viable therapeutic compounds targeting *VRK2* (WZ3105, Flavopiridol, Bosutinib, Phenol, and SKI-606 Kinome Scan):** `[Methodologically Flawed]`  
  This automated bioinformatic lookup was not critically vetted: (1) **Phenol** (`PubChem ID 996`) is a caustic, toxic simple carbolic acid ($C_6H_5OH$) used as a laboratory reagent/disinfectant, not a systemic kinase inhibitor for bronchiectasis; (2) **"SKI-606 Kinome Scan"** (`PubChem ID 20072150`) is the DSigDB gene-set name for an assay of **SKI-606**, which is the developmental code name for **Bosutinib** (already listed as #3 in Table 3)—so the authors docked the same drug twice; and (3) Table 3 omits all docking binding affinities ($\text{kcal/mol}$).
* **Claim 4: DNA methylation at `cg21568453` causally reduces bronchiectasis risk with 54% of the effect mediated by *VRK2* expression ($\beta_{\text{indirect}} = -0.064, P = 0.0055$):** `[Fragile]`  
  In a cis-locus, mQTLs for a CpG site (`cg21568453`) and eQTLs for its target gene (*VRK2*) typically tag the same underlying cis-regulatory haplotype in linkage disequilibrium. Running two-step univariable IVW without multivariable MR adjustment or three-way colocalization (`mQTL`–`eQTL`–`GWAS` `moloc`/`hyprcoloc`) conflates pleiotropic cis-LD with causal mediation. Moreover, the manuscript fails to report the step-1 $\beta$, step-2 $\beta$, total effect $\beta$, or instrument counts for the mediation analysis.

---

## 3. Forensic Defect Inventory

### 1. [Critical] False-Positive Inflation from Unadjusted LD ($r^2 < 0.1$) in Multi-SNP Cis-MR
* **Location:** Section "Instrumental variables (IVs) selection" (Line 27), Table 1 (Lines 75–120), and Table 2 (Lines 137–153).
* **Defect:** The authors clump cis-eQTLs at $r^2 < 0.1$ within $10,000\text{ kb}$, yielding up to 33 SNPs per gene, and apply standard `TwoSampleMR` IVW without incorporating an LD correlation matrix. Because cis-SNPs with $0.001 < r^2 < 0.1$ within a single gene locus are non-independent, unadjusted IVW underestimates the variance of the pooled estimator. This is directly exposed in Table 2 by comparing the multi-SNP IVW $P$-values against the single-top-SNP SMR $P$-values:
  * *ACVR2A*: $\text{OR}_{\text{MR}} = 1.54, P_{\text{MR}} = 9.92 \times 10^{-8}$ (15 SNPs) vs. $\text{OR}_{\text{SMR}} = 1.04, P_{\text{SMR}} = 0.549$ (null).
  * *CASP9*: $\text{OR}_{\text{MR}} = 0.79, P_{\text{MR}} = 2.32 \times 10^{-6}$ (25 SNPs) vs. $\text{OR}_{\text{SMR}} = 0.87, P_{\text{SMR}} = 0.452$ (null) and $\text{PP.H4} = 0.033$.
  * *VRK2*: $\text{OR}_{\text{MR}} = 1.36, P_{\text{MR}} = 2.17 \times 10^{-6}$ (20 SNPs) vs. $\text{OR}_{\text{SMR}} = 2.18, P_{\text{SMR}} = 3.63 \times 10^{-3}$.
* **Remediation:** Either clump strictly at $r^2 < 0.001$ (or use the top independent cis-eQTL via Wald ratio / SMR) or use generalized IVW / PCA-IVW (`MendelianRandomization::mr_ivw` with `cor = ld_matrix`) that explicitly accounts for inter-SNP linkage disequilibrium, and recompute FDR across all 2,525 genes.

### 2. [Major] Unvetted DSigDB Artifacts, Duplicate Docking of Bosutinib/SKI-606, and Missing Affinity Scores in Table 3
* **Location:** Section "Molecular docking" (Line 62), Section "Drug prediction and molecular docking" (Lines 159–173), and Table 3.
* **Defect:**
  1. **Duplicate compound / assay name confusion:** Table 3 lists both `Bosutinib` (`PubChem ID 5328940`) and `SKI-606 Kinome Scan` (`PubChem ID 20072150`). SKI-606 is the preclinical synonym for Bosutinib, and `"SKI-606 Kinome Scan"` is the name of a kinase profiling gene-set entry in DSigDB, not a distinct drug molecule.
  2. **Biologically implausible compound:** Table 3 lists `Phenol` (`PubChem ID 996`, $MW = 94.11\text{ g/mol}$) as one of the "top five potential chemical compounds" for treating bronchiectasis. Phenol is a nonspecific protein denaturant/disinfectant that produces meaningless low-molecular-weight docking poses.
  3. **Missing quantitative docking metrics & software contradiction:** Line 62 states that docking was performed with **AutoDock Vina 1.2.3**, whereas Line 159 states that docking was performed with **AutoDock 4.2.6**. Worse, Table 3 ("Docking results between top five small molecules and VRK2") contains zero docking results (no binding energies in $\text{kcal/mol}$, no inhibition constants $K_i$, and no interacting residue lists), reporting only the PDB ID and PubChem IDs.
* **Remediation:** Remove non-drug entries (`Phenol`) and duplicate assay synonyms (`SKI-606 Kinome Scan`), clarify whether AutoDock Vina 1.2.3 or AutoDock 4.2.6 was executed, and report the actual calculated binding energies ($\text{kcal/mol}$) and active-site coordinates in Table 3.

### 3. [Major] Text-Table Contradiction Regarding Tier 3 Classification and Truncation of Table 1
* **Location:** Table 1 (Lines 84–120) and Section "Colocalization analysis and SMR test" (Lines 137–154).
* **Defect:**
  1. Line 154 states: *"Four genes (CASP9, ACLY, SOD2, and SRPK1) that were not included in either the colocalization analysis or the SMR test were classified into tier 3 (Table 2)."* However, Table 2 explicitly shows `PPH4` colocalization values for all four of these genes (`0.033`, `0.615`, `0.191`, and `0.304`), and shows completed SMR and HEIDI results for `CASP9` ($\text{OR} = 0.87, P = 0.452, P_{\text{HEIDI}} = 0.116$). Thus, `CASP9` failed both colocalization and SMR rather than being omitted, and `ACLY`, `SOD2`, and `SRPK1` failed colocalization ($\text{PPH4} < 0.75$).
  2. Formatted Table 1 (Lines 84–120) is truncated mid-way through `SOD2` (missing `SOD2` Weighted mode, `TNFRSF4`, `XCL2`, and `SRPK1`), while the entire unformatted contents of Table 1 and Table 2 are duplicated inline inside the body text at Lines 75 and 137.
* **Remediation:** Correct the description of Tier 2 and Tier 3 classification criteria in Line 154 to match Table 2, explain why SMR returned `NA` for *ACLY*, *SOD2*, and *SRPK1*, and fix the formatting/truncation of Table 1.

### 4. [Major] Incomplete Reporting and Cis-LD Confounding in Two-Step Epigenetic Mediation MR
* **Location:** Section "Mediated MR Analysis..." (Line 67) and Section "The methylation of cg21568453..." (Line 176).
* **Defect:** The authors report only the product-of-coefficients indirect effect ($\beta = -0.064, P = 0.0055$) and proportion mediated ($0.54$, 95% CI: $0.16\text{--}0.92$) without reporting the total effect of `cg21568453` on bronchiectasis, the step-1 effect of `cg21568453` on *VRK2*, the step-2 effect used in the product, or how standard errors were propagated (e.g., Delta method vs. bootstrap). Because `cg21568453` is a cis-CpG site in *VRK2*, its mQTL instruments are in cis-LD with *VRK2* eQTL instruments, violating the exclusion restriction of two-step MR unless tested via multivariable MR and multi-trait colocalization.
* **Remediation:** Report full summary statistics (SNPs, $r^2$ clumping, $\beta_{\text{total}}$, $\beta_1$, $\beta_2$, SEs, and Delta-method $P$-values) for both steps of the mediation analysis, and perform three-trait colocalization (`mQTL` + `eQTL` + `Bronchiectasis`) alongside MVMR adjusting for direct cis-effects.

---

## 4. Quantitative Rubric Scoring

| Rubric Dimension | Score | Max | Forensic Justification |
| :--- | :---: | :---: | :--- |
| **1. Methodological & Statistical Rigor** | **1.0** | **3.5** | Liberal $r^2 < 0.1$ clumping in unadjusted `TwoSampleMR` IVW inflates significance across correlated cis-SNPs; single-variant SMR $P$-values fail multiple-testing correction; two-step cis-mediation lacks MVMR/colocalization adjustment for shared cis-LD. |
| **2. Claim-to-Evidence Alignment** | **0.8** | **2.5** | Claims 10 FDR-significant druggable genes when SMR/coloc refute 9 of them and *VRK2* only reaches $P_{\text{SMR}} = 3.63 \times 10^{-3}$; Tier 3 description in text contradicts Table 2; docking claims are unsupported by quantitative affinity metrics. |
| **3. Data Integrity & Biological Plausibility** | **0.8** | **2.0** | Proposes caustic industrial `Phenol` as a candidate drug and docks `Bosutinib` twice (under `Bosutinib` and `"SKI-606 Kinome Scan"`); relies solely on blood eQTLs without lung/bronchial tissue validation. |
| **4. Reproducibility & Data Integrity** | **1.0** | **2.0** | Contradiction between AutoDock Vina 1.2.3 (Methods) and AutoDock 4.2.6 (Results); Table 3 omits all docking scores; formatted Table 1 is truncated after `SOD2`; mediation step-1 and total effect estimates are omitted. |
| **Scientific Core Score** | **2.6** | **8.0** | Sum of Rigor + Claims + Biology. |
| **Total Composite Score** | **3.6** | **10.0** | **Flawed / Overstated** (36 / 100 equivalent). |
