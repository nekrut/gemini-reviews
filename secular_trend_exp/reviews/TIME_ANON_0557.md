<Blinded Review: TIME_ANON_0557>
OVERALL_SCORE: 5.6/10
VERDICT: CAVEATS
ESTIMATED_DECADE: 2010s
**Composite Score:** 5.6 / 10.0 (Rigor: 1.5/3.5 | Claims: 1.3/2.5 | Biology: 1.4/2.0 | Reproducibility: 1.4/2.0)
**Bias Category:** Statistical/Design
**Verdict:** Major Revision
**Study Modality:** Hybrid Computational + Wet-Lab
**Technology Maturity:** Mid-Stage High-Throughput
**Epistemic Stage:** Clinical/Observational

---

### 1. Executive Summary / SUMMARY
This candidate-gene genetic association study examines 54 SNPs across four host genes (*TGFB2*, *HMOX1*, *CD36*, and *ICAM1*, plus sickle-cell control *HBB* `rs334`) in 749 Angolan children (`130` cerebral malaria [CM], `158` severe non-cerebral malaria [SnC], `142` uncomplicated malaria [UM], and `319` uninfected controls [UIF]), supplemented by family-based transmission disequilibrium tests (`TRANSMIT` in mother-child pairs: `105` CM, `115` SnC, `109` UM) and quantitative RT-PCR of peripheral blood leukocyte *HMOX1* mRNA in a subset of `42` CM patients. The authors report that single SNPs and reconstructed haplotypes in *TGFB2* and *HMOX1* are specifically associated with progression from malaria infection to cerebral malaria (`CM vs SnC` and `CM vs UM`), and that the protective *HMOX1c* haplotype (`A-G-T-A-G`) is associated with lower peripheral blood *HMOX1* mRNA expression in CM patients. However, forensic audit of the statistical pipeline and tables reveals severe methodological flaws: (1) circular two-step SNP selection prior to haplotype permutation testing; (2) single-marker $p$-values (`0.015–0.047`) that do not survive multiple-testing correction across 54 SNPs $\times$ 3 control groups; (3) transmission disequilibrium test (TDT) results in Table 4 that actually show **zero** association in CM mother-child pairs ($p=0.65$ and $p=0.54$) while misinterpreting under-transmission in SnC/UM controls as validation of CM risk; and (4) numerical and methodological discrepancies in the text.

### 2. STRENGTHS
- **Clinically Stratified Case-Control Phenotyping:** Rather than lumping all severe malaria cases together or comparing cerebral malaria solely against healthy population controls, the study separates Cerebral Malaria (`CM`, $n=130$) from Severe Non-Cerebral Malaria (`SnC`, severe malarial anemia and/or hyperparasitemia without coma, $n=158$), Uncomplicated Malaria (`UM`, $n=142$), and Uninfected Controls (`UIF`, $n=319$).
- **Positive Genetic Control (*HBB* `rs334` HbS):** Including the sickle-cell variant `rs334` confirms expected strong protection against all clinical malaria phenotypes compared to uninfected controls ($\text{OR} = 0.21\text{–}0.24$, $p = 10^{-7}\text{ to }10^{-10}$, Figure S1), validating sample phenotyping and genotyping quality (`Sequenom iPLEX MassARRAY`).

### 3. WEAKNESSES & METHODOLOGICAL AUDIT (Methodological & Statistical Audit)
- **Circular Two-Step SNP Pre-Selection Invalidates Haplotype Permutation $p$-Values (`Pcorrec`):**
  - The authors genotyped 54 SNPs (`18 TGFB2`, `7 HMOX1`, `19 CD36`, `9 ICAM1`, `1 HBB`) and ran unadjusted single-SNP logistic regressions across three pairwise comparisons (`CM vs UIF`, `CM vs UM`, `CM vs SnC` — over 150 marginal tests). In Table 1, virtually all reported single-SNP $p$-values for *TGFB2* and *HMOX1* are marginal ($p = 0.015\text{ to }0.047$) and **none** would survive Bonferroni or Benjamini-Hochberg FDR correction across the 53 candidate SNPs (except possibly `rs1342586` at $p=0.0029$ in `CM vs UM`).
  - Crucially, to construct the haplotypes in Figure 2 and Tables 2–3, the authors selected **only** the SNPs that already achieved $p < 0.05$ in the `CM vs SnC` single-SNP analysis (`8 TGFB2 SNPs` and `5 HMOX1 SNPs`) and then ran 1,000-label permutations in `Haploview` on those cherry-picked SNPs to obtain `Pcorrec = 0.035` and `Pcorrec = 0.036`!
  - Pre-filtering markers based on their marginal association with the case-control label in the exact same dataset, and then permuting labels only during the second-stage haplotype test (without repeating the SNP-selection step inside each permutation), is a classic "double-dipping" / circular selection error that severely inflates Type I error.
- **Misinterpretation of Mother-Child TDT Results (`TRANSMIT`, Table 4) and Numerical Typo in Abstract:**
  - The authors claim in the Abstract and Results that the TDT *"corroborated"* the association of `TGFB2c` and `HMOX1c` haplotypes with Cerebral Malaria.
  - However, inspection of **Table 4** shows that in **Cerebral Malaria (`CM`, $n=105$ pairs)**—the actual disease group of interest—there is **no significant distortion of transmission whatsoever**:
    - `TGFB2c` in CM: Observed = `20.0`, Expected = `18.93`, $\chi^2 = 0.207$, **$p = 0.65$**.
    - `HMOX1c` in CM: Observed = `42.22`, Expected = `39.77`, $\chi^2 = 0.377$, **$p = 0.54$**.
    - `HMOX1a` in CM: Observed = `63.22`, Expected = `64.61`, $\chi^2 = 0.092$, **$p = 0.76$**.
  - Instead, the authors point to significant **under-transmission** of `TGFB2c` in the **SnC** group (Obs `5.31` vs. Exp `10.17`, $p = 0.0384$) and of `HMOX1c` in the **UM** group (Obs `33.24` vs. Exp `44.91`, **$p = 0.0036$** in Table 4, which is misquoted as **`p = 0.036`** in the Abstract and Line 104!). Because a family-based TDT in SnC or UM children tests Mendelian segregation from heterozygous mothers to SnC/UM offspring—not a comparison against CM—finding null Mendelian transmission in CM ($p=0.54\text{–}0.65$) does **not** confirm that these haplotypes cause cerebral malaria.
- **Methodological Error and Uncontrolled Cell-Composition Confounding in *HMOX1* eQTL Analysis (Table 5):**
  - In Materials and Methods ("Statistical Analysis", Line 183), the authors state: *"Quantitative Trait Locus (QTL) analysis was used to test the marginal association of candidate SNPs in the HMOX1 gene and the duallog2 ratios calculated to evaluate the HMOX1 gene expression in CM patients. Analysis was performed by the **logistic regression** model implemented in the Plink Package."*
  - A quantitative trait ($\Delta\Delta C_t$ gene expression) cannot be modeled as the dependent variable in a binary logistic regression; Table 5 actually reports continuous linear regression outputs (`BETA` and $t$-statistic `STAT` with asymptotic $p$-values `0.025–0.068`, unadjusted for multiple testing across 7 SNPs and 4 haplotypes).
  - Furthermore, peripheral blood *HMOX1* mRNA was extracted from whole blood (`PAXgene`) of `42` comatose CM children without adjusting for differential leukocyte subset counts (monocytes/neutrophils vs. lymphocytes), which vary dramatically during acute severe malaria and strongly confound whole-blood *HMOX1* transcript levels.

### 4. Biological / Experimental Grounding & Claim Proportionality
- **Claim 1:** *Sickle-cell trait (`HBB rs334`) strongly protects Angolan children against cerebral, severe non-cerebral, and uncomplicated malaria.* — `[Well Supported]` by highly significant odds ratios ($\text{OR} \approx 0.2$, $p \le 10^{-7}$).
- **Claim 2:** *Specific haplotypes in TGFB2 and HMOX1 significantly determine susceptibility to cerebral malaria vs. non-cerebral malaria, corroborated by family-based TDT.* — `[Methodologically Flawed]` / `[Overstated]`; single-SNP associations do not survive multiple-testing correction, haplotype permutation tests suffer from circular SNP pre-selection, and the TDT in CM families is completely null ($p=0.54\text{–}0.65$).
- **Claim 3:** *The HMOX1c haplotype directly downregulates HMOX1 transcription in CM patients ($p=0.022$).* — `[Fragile]`; nominal unadjusted $p=0.022$ in $n=42$ whole-blood samples without leukocyte differential adjustment.

### 5. Reproducibility & Data Completeness
- **Genotyping & Primer Details:** The complete list of 54 `rs` SNP IDs, gene coordinates, and qRT-PCR primers (*HMOX1* and *ACTB*) are provided in the text and Table S2.
- **Data Availability:** Summary genotype and haplotype frequency tables are included in the manuscript and supplementary files, though individual-level genotype/phenotype files are not deposited in a public repository.
</Blinded Review: TIME_ANON_0557>
