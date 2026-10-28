# Peer Review: ANON_176

**Overall Score:** **6.5 / 10.0** (Mixed / Salvageable)
* **Score Breakdown:** Rigor: 2.1/3.5 | Claims: 1.6/2.5 | Biology: 1.5/2.0 | Reproducibility: 1.3/2.0

---

## 1. Executive Summary & Synthesis

This manuscript reports a genome-wide association study (GWAS) of four post-slaughter carcass traits—carcass weight (CW), ribeye area (REA), marbling score (MS), and backfat thickness (BFT)—in 13,241 commercial Black Angus steers. Low-density genotypes from the Illumina BovineSNP50 BeadChip (39,583 QC-passed autosomal SNPs) were imputed to 6,508,513 whole-genome sequence (WGS) variants (`Beagle v5.2` $\text{DR}^2 \ge 0.8$, mean $\text{DR}^2 = 0.946$) using 128 purebred Angus WGS individuals from the 1000 Bull Genomes Project (`PRJEB42783`), and single-SNP mixed linear model association tests (`GCTA`) identified 2,028 genome-wide significant associations ($P < 7.68 \times 10^{-9}$) distributed across 13 genomic regions on eight chromosomes (`BTA6, 7, 11, 13, 14, 17, 20, 29`).

The large single-breed commercial sample size ($N = 13,241$), stringent Bonferroni significance threshold ($0.05 / 6,508,513 = 7.68 \times 10^{-9}$), conditional lead-SNP analysis on BTA7 (`Fig. S8`), and principal component sensitivity checks (`Fig. S9`) provide solid statistical support for the primary major-effect QTLs on BTA7 (~90.1 Mb, pleiotropic for CW, REA, MS, and BFT near *CAST*/*PCSK1*/*ELL2*), BTA20 (`3.9–5.7 Mb` for CW and REA near *STC2*), and BTA6 (`37.05–38.09 Mb` near *LCORL*/*NCAPG*). However, the manuscript is marred by several numerical and reporting errors between the text and tables, a dimensional unit error for BFT in Table 1, omission of estimated trait heritabilities ($h^2$) and variance components ($\sigma_a^2, \sigma_e^2$), and an over-interpretation of single-SNP marginal explained genetic variance (`EGV%`) across correlated SNPs and low-MAF (`MAF = 0.01`) imputed variants.

---

## 2. Claim-by-Claim Evaluation

* **Claim 1:** *Imputed WGS GWAS ($N = 13,241$, 6.51M SNPs) identifies 13 genome-wide significant genomic regions ($P < 7.68 \times 10^{-9}$) associated with CW, REA, MS, and BFT, including a major pleiotropic locus at ~90.1 Mb on BTA7 affecting all four traits.* — **[Well Supported]**
  * **Evidence & Critique:** The primary association signals on BTA7 (`88.24–91.63 Mb`, lead SNP `BTA7:90155240`, $P = 2.02 \times 10^{-29}$ for CW, $P = 1.99 \times 10^{-31}$ for REA, $P = 1.65 \times 10^{-21}$ for MS, $P = 1.38 \times 10^{-15}$ for BFT) and BTA20 (`3.90–5.70 Mb`, lead SNP `BTA20:4869191`, $P = 1.56 \times 10^{-29}$ for CW) are highly significant and backed by a conditional analysis fitting `BTA7:90155240` as a fixed covariate (`Fig. S8`), which completely ablates the surrounding 3.4 Mb signal and confirms that a single underlying QTL haplotype drives the BTA7 peak. However, the **Abstract (`line 16`) swaps the significant SNP counts for MS and REA**: Line 16 states *"842, **745**, **340**, and 101 SNPs... were significantly associated with CW, **MS**, **REA**, and BFT, respectively"*, whereas Results (`line 171`) and Table 2 (`lines 192–203`) show that **745** SNPs (`741 + 2 + 2`) are associated with **REA** and **340** SNPs (`247 + 1 + 45 + 3 + 41 + 2 + 1`) are associated with **MS**.

* **Claim 2:** *Individual lead SNPs explain up to 6.46% of additive genetic variance (`EGV%`) for CW, 7.60% for REA, 5.44% for MS, and 3.84% for BFT, and "collectively" account for a substantial portion of additive genetic variance (Abstract line 18, Table 3).* — **[Overstated]**
  * **Evidence & Critique:** In Equation (3) (`line 84`), $\text{EGV}_{i,j}\% = \frac{2 p_i q_i \beta_{i,j}^2}{\sigma_{a,j}^2} \times 100$, where $\beta_{i,j}$ is taken from a **single-SNP marginal linear mixed model** (`Equation 1`) without joint multi-locus fitting and without correcting for the Beavis effect (winner's curse). First, the authors never report the denominator $\sigma_{a,j}^2$ or the narrow-sense heritability $h^2 = \sigma_a^2 / (\sigma_a^2 + \sigma_e^2)$ anywhere in the manuscript! Back-calculating $\sigma_a^2$ from Table 3 ($2 p q \beta^2 / \text{EGV}$) yields $\sigma_{a,\text{CW}}^2 \approx 246.1\text{ kg}^2$ ($h_{\text{CW}}^2 \approx 246.1 / 37.76^2 = 0.173$), $\sigma_{a,\text{REA}}^2 \approx 0.409\text{ in}^4$ ($h_{\text{REA}}^2 \approx 0.409 / 1.586^2 = 0.163$), $\sigma_{a,\text{MS}}^2 \approx 3,661$ ($h_{\text{MS}}^2 \approx 3,661 / 117.75^2 = 0.264$), and $\sigma_{a,\text{BFT}}^2 \approx 0.0156$ ($h_{\text{BFT}}^2 \approx 0.0156 / 0.26^2 = 0.231$). Second, for rare imputed variants with `MAF = 0.01` (`BTA6:37632189` with $|\beta| = 12.51\text{ kg}$ and `BTA14:22911258` with $|\beta| = 11.76\text{ kg}$ in Table 3), single-SNP marginal effect estimates at $P < 7.68 \times 10^{-9}$ are subject to substantial upward selection bias (winner's curse) and genotype dosage uncertainty. Third, summing or combining marginal single-SNP `EGV%` across correlated SNPs within or across loci overstates joint variance explained compared to fitting all 13 lead SNPs simultaneously or partitioning variance with a regional GRM.

* **Claim 3:** *Functional annotation identifies novel candidate genes including `RAD50`, `ELL2`, `PCSK1`, and `CAST` on BTA7 and `STC2` on BTA20.* — **[Moderately Supported]**
  * **Evidence & Critique:** The candidate genes located near the lead imputed SNPs (`CAST`, `PCSK1`, `ELL2` on BTA7; `STC2` on BTA20; `LCORL`/`NCAPG` region on BTA6; `PLAG1`/`XKR4` region on BTA14) are biologically plausible and consistent with prior cattle growth/carcass literature. However, because LD extends over 1–3.4 Mb in purebred Angus (as demonstrated by the 3.4 Mb span ablated by conditioning on a single SNP in `Fig. S8`), proximity of the top imputed intergenic/intronic SNP (`BTA7:90155240`, located 80 kb downstream of `ELL2`) cannot distinguish causal regulatory variants from tagging SNPs without multi-breed fine-mapping or eQTL colocalization.

---

## 3. Technical & Methodological Critique

### Major Flaws & Numerical Discrepancies

1. **Dimensional Unit Error for Backfat Thickness (BFT) in Table 1 vs. Methods:**
   * In `Methods: Animal and phenotypes` (`line 45`), the four traits are defined with units: *"carcass weight (CW, kg), ribeye area (REA, $\text{in}^2$), marbling (MS, score), and back fat thickness (BFT, **mm**)."*
   * However, in Table 1 (`line 59`), `BFT` has **Mean = 0.731, Min = 0.064, Max = 1.976, SD = 0.26**, and in Table 3 (`line 230`), the lead SNP effect on BFT is $|\beta| = 0.036$.
   * In commercial grain-fed Black Angus steers slaughtered at ~404 kg carcass weight, subcutaneous 12th-rib backfat thickness is **0.731 inches** ($\approx 18.6\text{ mm}$), not $0.731\text{ mm}$! Note that `REA` is already reported in US imperial units ($\text{in}^2$, mean $13.71\text{ in}^2$), confirming that BFT was recorded in **inches** (`in`), not millimeters (`mm`).

2. **Multiple Internal Numerical Contradictions Between Main Text and Tables:**
   * **Abstract SNP counts swapped between MS and REA (`line 16` vs. `line 171` & `Table 2`):** Abstract line 16 reports `745` SNPs for `MS` and `340` SNPs for `REA`, whereas Results line 171 and Table 2 report `745` SNPs for `REA` and `340` SNPs for `MS`.
   * **BTA6 CW SNP count (`line 166` vs. `Table 2` & `line 359`):** Results line 166 states *"A novel region on BTA6 (at 38.09–37.05 Mb) containing **48** significant SNPs associated with CW (Fig. 1)"*, whereas Table 2 (`line 188`) and Discussion (`line 359`) state there are **20** significant SNPs in that BTA6 region (and the regional interval `38.09–37.05 Mb` is written backwards in both Line 166 and Table 2, giving a negative span unless written `37.05–38.09 Mb`).
   * **BTA14 region span (`line 363` vs. `Table 2`):** Discussion line 363 states *"The significant SNPs located on BTA14 (n = 108) fall into a **90.41 Kb** region (22.90–23.80 Mb)"*, whereas $23.80\text{ Mb} - 22.90\text{ Mb} = \mathbf{901.41\text{ Kb}}$ (`0.90 Mb`), as reported in Table 2 (`line 190`).
   * **Misnumbered Figure Citations (`lines 166–180`):** Line 166 cites `(Fig. 3)` for `MS`, whereas Figure 2 is `MS` and Figure 3 is `BFT`. Line 171 cites `(Fig. 2)` for `REA`, whereas Figure 4 is `REA` and Figure 2 is `MS`. Line 176 cites `(Fig. 3)` for `MS` (should be `Fig. 2`), and Line 180 cites `(Fig. 4)` for `BFT` (should be `Fig. 3`).

3. **Proximal Contamination in GRM Construction and Missing Variance Component Reporting:**
   * In `Methods: Genome-wide association study` (`lines 75–81`), the genomic relationship matrix $G$ is constructed from all 39,583 autosomal 50K SNPs and fit in `y = Xb + ss + Zu + e` rather than using Leave-One-Chromosome-Out (`GCTA --mlma-loco`). Including SNPs on the same chromosome as the tested variant `ss` in the random polygenic effect $u$ causes proximal contamination (double-fitting the QTL in both fixed and random effects), which conservatively deflates test statistics. Furthermore, the manuscript omits a heritability and genetic/phenotypic correlation table ($\sigma_a^2, \sigma_e^2, h^2, r_g, r_p$) across the four traits.

4. **Incomplete Data Availability (Missing Summary Statistics):**
   * The `Data availability` statement (`line 466`) only references the public 1000 Bull Genomes Project accession (`PRJEB42783`) used as the imputation panel. Neither the full GWAS summary statistics (`CHR, BP, REF, ALT, MAF, DR2, BETA, SE, P`) across the 6.51M SNPs nor the underlying phenotype/genotype data are deposited, limiting meta-analysis and fine-mapping reuse.

---

## 4. Constructive Recommendations

1. **Correct All Text-to-Table and Figure-Callout Errors:**
   * Swap `745` and `340` in the Abstract (`line 16`) so that `REA = 745` and `MS = 340` match Table 2.
   * Change `48 significant SNPs` (`line 166`) to `20 significant SNPs` on BTA6, reverse `38.09–37.05` to `37.05–38.09` in Line 166 and Table 2, and change `90.41 Kb` (`line 363`) to `901.41 Kb`.
   * Fix the figure citations in Lines 166–180 so that `CW = Fig. 1`, `MS = Fig. 2`, `BFT = Fig. 3`, and `REA = Fig. 4`.
   * Correct the unit of `BFT` in Line 45 and Table 1 from `mm` to `inches (in)`.
2. **Report Heritabilities ($h^2$), Variance Components ($\sigma_a^2, \sigma_e^2$), and Joint Multi-Locus Variance Explained:** Add $\sigma_a^2$, $\sigma_e^2$, and $h^2 \pm \text{SE}$ for each trait to Table 1, and report the joint additive genetic variance explained when all 13 lead SNPs are fitted simultaneously in a single multi-SNP model alongside the marginal single-SNP `EGV%` in Table 3.
3. **Report Imputation Accuracy ($\text{DR}^2$) for Lead SNPs in Table 3:** Add the Beagle $\text{DR}^2$ value for each of the 13 lead SNPs in Table 3, especially for the two rare (`MAF = 0.01`) imputed variants on BTA6 (`37,632,189 bp`) and BTA14 (`22,911,258 bp`).
4. **Deposit Full GWAS Summary Statistics:** Archive the complete genome-wide summary statistics for all 6,508,513 tested SNPs across the four traits in a public repository (e.g., EBI GWAS Catalog, Dryad, or Figshare).
