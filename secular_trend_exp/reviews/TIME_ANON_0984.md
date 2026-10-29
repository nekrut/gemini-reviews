<Blinded Review: TIME_ANON_0984>
**Composite Score:** 6.6 / 10.0 (Rigor: 2.0/3.5 | Claims: 1.7/2.5 | Biology: 1.3/2.0 | Reproducibility: 1.6/2.0)
**Bias Category:** Algorithmic/Model
**Verdict:** Major Revision
**Study Modality:** Hybrid Computational + Wet-Lab
**Technology Maturity:** Mid-Stage High-Throughput
**Epistemic Stage:** Translational/Preclinical/Biomarker

OVERALL_SCORE: 6.6/10
VERDICT: CAVEATS
ESTIMATED_DECADE: 2020s

---

### 1. Executive Summary / SUMMARY
This agricultural genomics and breeding study evaluates five seed nutritional traits—total protein, sulfur-containing amino acids (SAAs), dietary fiber, total starch, and protein digestibility (PDg)—predicted via attenuated total reflectance Fourier-transform mid-infrared (ATR-FT-MIR) spectroscopy across 267 genotyped accessions of the USDA Pea Single Plant Plus Collection (*Pisum sativum* L.) grown over 3 years at two USDA-certified organic farms in South Carolina (`RAWL20`, `CLEM21`, `CLEM22`). Using 54,315 imputed biallelic SNPs ($\text{MAF} \ge 0.05$, missingness $\le 20\%$), the authors characterize population structure via `ADMIXTURE` ($K = 10$) and PCA, estimate Bayesian phenotypic BLUPs (`rstanarm::stan_lmer`), and conduct multi-model GWAS in `GAPIT v3` (`GLM`, `MLM`, `CMLM`, `SUPER`, `MLMM`, `FarmCPU`, `BLINK`) at a Bonferroni threshold of $p < 0.05 / 54,315 = 9.21 \times 10^{-7}$ ($-\log_{10} p = 6.036$). They report 17 lead marker-trait associations (MTAs) for protein, SAA, and PDg—highlighting a proximal chromosome 5 cluster ($61.7\text{--}78.5\ \text{Mb}$) associated with both protein and SAA—and identify 44 genes in local LD blocks. While the multi-year organic field trial and open GitHub repository are commendable, the manuscript suffers from severe bioinformatic metric misreporting in Table 1 (reporting average heterozygosity of $\mathbf{0.883}$ in a self-pollinating, single-plant-descent inbred crop!), reliance on unadjusted `GLM` hits for several chromosome 5 claims, and chemical cross-prediction artifacts in FT-MIR partial least squares (PLS) predictions (where PDg took only 4 discrete values with $H^2 = 0.00$, yet `S6LG2_102304910` is claimed to explain $29.34\%$ of PDg variance).

### 2. Methodological & Statistical Audit / STRENGTHS & WEAKNESSES

#### STRENGTHS
- **Multi-year organic field evaluation of 267 diverse USDA germplasm accessions:** Testing 267 accessions across 3 environments (`RAWL20`, `CLEM21`, `CLEM22`) under authentic organic management provides actionable phenotypic baselines for low-input pulse breeding.
- **Open science and code availability:** All R scripts and data are publicly deposited in a dedicated GitHub repository (`[GITHUB_REPO_REDACTED]`), and full marker coordinates, MAF, PVE, and LD intervals are transparently tabulated in Table 2.

#### WEAKNESSES & METHODOLOGICAL AUDIT
- **Biologically impossible "Average Heterozygosity = 0.883" in Table 1 for inbred pea lines:**
  - *Pisum sativum* is a strictly cleistogamous (self-pollinating) diploid species ($>99\%$ selfing), and the USDA Pea Single Plant Plus Collection (PSPPC) was specifically derived by single-plant selfed descent (`Holdsworth et al.`), meaning true observed heterozygosity ($H_{\text{obs}}$) across SNPs is near zero ($<0.02\text{--}0.05$).
  - Yet **Table 1** and Results/Discussion (lines 117, 133, 180) report *"overall average heterozygosity was 0.88 and varied from 0.73 (subpopulation 8) to 0.89 (subpopulations 4 and 5)"* and interpret this as *"indicating relatively high genetic variability within the PSP germplasm."*
  - Under Hardy-Weinberg or inbreeding, even a randomly mating population cannot have an average biallelic SNP heterozygosity above $2p(1-p) \le 0.50$! The authors ran `vcftools --het`, which outputs `O(HOM)` and `E(HOM)` (the **proportion of homozygous sites**, typically $\sim 0.88$ in selfed lines), and mistakenly reported the **homozygosity** proportion (or $1 - H_{\text{obs}}$) as "average heterozygosity."
  - Furthermore, in Table 1, Subpopulation 1 ($n = 10$) and Subpopulation 10 ($n = 81$) have identical values to three decimal places across all three columns ($\pi = 1.023$, Tajima's $D = 0.436$, Het $= 0.843$), which is a copy-paste error from row 1 into row 10.
- **Inclusion of unadjusted `GLM` false positives in the Chromosome 5 "hotspot":**
  - The authors state in Methods (line 96) that `GAPIT` BIC model selection determined that the VanRaden kinship matrix ($K$) was required to control for the strong population structure ($K = 10$ subpopulations). However, one of the 7 models run by `GAPIT` (`GLM` with 0 PCs and no kinship matrix) has **zero control for population structure or kinship**!
  - In **Table 2**, 6 of the 17 reported peak SNPs—including **4 of the 7 SNPs in the headline Chromosome 5 hotspot** (`S5LG3_61677899`, `S5LG3_65187310`, `S5LG3_75020967`, `S5LG3_75020977`) as well as `S3LG5_434614474` and `S4LG4_416335390`—were detected **exclusively by `GLM`** and failed to reach significance in any mixed model (`MLM`, `CMLM`, `MLMM`, `FarmCPU`, `BLINK`)! Reporting naive `GLM` hits (no PCs, no kinship) in a structured diversity panel ($K = 10$) as valid MTAs inflates false positives driven by subpopulation stratification.
- **FT-MIR spectroscopic calibration artifacts and zero-heritability GWAS (`PDg` and `Fiber`):**
  - All five nutritional traits were not chemically assayed across the trial plots, but predicted from mid-infrared (ATR-FT-MIR) flour spectra via PLS chemometric models. Because FT-MIR spectra predict multiple traits from overlapping amide and carbohydrate absorption bands, the strong correlations among predicted protein, fiber, and PDg ($r = 0.59\text{--}0.68$) partly reflect shared spectral loadings.
  - Most strikingly, the authors report in line 109 that broad-sense heritability ($H^2$) for total fiber and PDg was **zero** ($H^2 = 0.00$), and that *"PDg data were grouped at four discrete values"*, yet in Table 2 (`No. 16`, `S6LG2_102304910`) they claim a GWAS hit explaining **$29.34\%$ of the phenotypic variance (PVE)** of PDg! A single SNP cannot genuinely explain $29.3\%$ of phenotypic variance for a trait whose total genetic variance ($H^2$) is $0.00$; this is a classic `BLINK`/`GLM` PVE estimation artifact on a discrete/non-normal BLUP distribution.
- **Selection bias in Year 3 (`CLEM22`):** In Year 3 (`CLEM22`), only 101 of the 297 accessions were planted, specifically pre-selected *"based on their previously measured protein concentration and agronomic adaptation"*, and plot seeding density was increased nearly 5-fold ($50 \to 240$ seeds/plot). Truncation selection on the response variable (protein) in `CLEM22` biases variance component estimates when fitting a joint random-effects model with $G \times E$ forced to zero (line 79: *"Genotype-by-environment was zero and not included"*).

### 3. Biological / Experimental Grounding & Claim Proportionality
- **Claim that the USDA PSPPC panel partitions into 10 subpopulations with moderate linkage decay:** `[Well Supported]` — Consistent with prior genomic characterization of the PSPPC (`Holdsworth et al.`, `Powers et al.`).
- **Claim that `S5LG3_65228308`, `S5LG3_68426550`, and `S5LG3_78533957` on Chromosome 5 and `S2LG1_292238595` on Chromosome 2 are associated with SAA and protein content:** `[Moderately Supported]` — These specific loci were supported across structure-corrected multi-locus models (`BLINK`, `FarmCPU`, `MLMM`), though low trait heritability ($H^2 = 0.13\text{--}0.21$) and indirect FT-MIR phenotyping warrant wet-chemistry (HPLC amino acid / Dumas nitrogen) validation.
- **Claim that average heterozygosity across the inbred pea diversity panel is $0.883$:** `[Methodologically Flawed]` — Confuses homozygosity (`vcftools` `O(HOM)`) with heterozygosity ($H_{\text{obs}}$ cannot exceed $0.50$ for biallelic SNPs and is $<0.05$ in selfed pea accessions), plus a duplicate copy-paste row for Subpopulations 1 and 10 in Table 1.
- **Claim that `S6LG2_102304910` explains $29.34\%$ of protein digestibility (PDg) variation:** `[Methodologically Flawed]` — Contradicts the trait's reported broad-sense heritability of $H^2 = 0.00$ and 4-value discrete FT-MIR quantization.

### 4. Reproducibility & Data Completeness
Reproducibility is high: the authors provide a public GitHub repository (`[GITHUB_REPO_REDACTED]`), cite the public VCF source (`Powers et al.`) and reference genome (`Cameor v1a` on PulseDB), and specify all software versions (`VCFtools v0.1.17`, `Beagle v5.4`, `ADMIXTURE v1.3.0`, `GAPIT v3`, `PLINK`) and command flags.
</Blinded Review: TIME_ANON_0984>
