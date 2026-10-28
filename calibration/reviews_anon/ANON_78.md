# Review of ANON_78

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **2.3 / 10.0** (Fundamentally Invalid)  
* **Score Breakdown:** Rigor: 0.5/3.5 | Claims: 0.6/2.5 | Biology: 0.6/2.0 | Reproducibility: 0.6/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript reports a genome-wide association study (GWAS) of eight physiological and agronomic traits—flag leaf area (FLA), cell membrane thermostability (CMT), canopy temperature at vegetative (CTV) and grain-filling (CTG) stages, days to heading (DH), days to maturity (DM), 1000-grain weight (TGW), and grain yield per plant (GYP)—in a panel of 96 spring bread wheat (*Triticum aestivum* L.) genotypes grown under normal field and plastic-tunnel heat stress ($>40^\circ\text{C}$ applied at anthesis) over two seasons (2018–19 and 2019–20). Genotyping was performed using the Illumina 90K Infinium SNP array (32,141 polymorphic SNPs mapped), population structure was inferred via STRUCTURE ($K=4$), and association mapping was conducted in GAPIT using a compressed mixed linear model (CMLM). The authors report 320 marker–trait associations (MTAs; 169 under normal and 151 under heat-stress conditions) at $-\log_{10} P \ge 3$ and highlight several putative pleiotropic SNPs across the A, B, and D genomes.

Despite addressing an important breeding target, the manuscript contains fatal mathematical, statistical, and biological inconsistencies that invalidate its quantitative conclusions: (1) the phenotypic correlation matrix reported in Table 1 is mathematically impossible (non-positive-semidefinite, with determinant $\det(R) = -0.729 < 0$ for the triad of DH, DM, and GYP); (2) the reported phenotypic means in the Results (e.g., normal bread wheat TGW of $73\text{ g}$, and vegetative canopy temperature dropping from $35^\circ\text{C}$ under normal conditions to $27^\circ\text{C}$ under heat stress even though heat stress was not applied until anthesis) are biologically and physically implausible; (3) the GWAS uses an uncalibrated threshold ($P \le 10^{-3}$, misdescribed in Methods as Bonferroni-adjusted) across 32,141 SNPs and 16 trait–environment scans ($>514,000$ tests), where ~514 false-positive MTAs are expected by chance alone—exceeding the 320 MTAs reported; and (4) single-SNP phenotypic variance explained (PVE) values of 13%–41% each across 12–30 SNPs per trait sum to $300\%\text{--}800\%$ of total variance, indicating that total mixed-model $R^2$ (including kinship and population structure) was misreported as individual marker $R^2$. Re-verifying the raw phenotypic spreadsheets and completely re-running the statistical and GWAS pipelines from raw data are required.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Physiological and yield traits exhibit strong positive phenotypic correlations in both normal and heat-stressed environments (Abstract, Results line 84, Table 1): [Methodologically Flawed].**  
  The Pearson correlation coefficients reported in Table 1 violate the Cauchy–Schwarz / positive-semidefiniteness condition required of any valid correlation matrix computed from real data. Specifically, under normal conditions, Table 1 reports $r(\text{DH}, \text{DM}) = 0.77$, $r(\text{DH}, \text{GYP}) = 0.68$, and $r(\text{DM}, \text{GYP}) = -0.45$. For any three variables with $r_{XY} = 0.77$ and $r_{XZ} = 0.68$, $r_{YZ}$ must mathematically be at least $r_{XY}r_{XZ} - \sqrt{(1 - r_{XY}^2)(1 - r_{XZ}^2)} = 0.5236 - 0.4678 = +0.056$; the reported value of $-0.45$ yields a $3 \times 3$ correlation matrix determinant of $\det(R) = -0.729 < 0$ (and similarly $\det(R) = -0.573 < 0$ for DH, DM, and TGW, as well as under heat stress). Additionally, Table 1 reports a strong *positive* correlation between canopy temperature (CTV, CTG) and grain yield ($r = 0.61\text{--}0.71$), whereas in wheat physiology, cooler canopies (lower CT) reflect superior stomatal conductance and vascular capacity under heat stress and correlate negatively with heat-stressed yield loss.

* **320 significant MTAs (169 in normal and 151 in heat-stressed conditions) and individual SNPs explaining up to 41.09% (or 73.86%) of phenotypic variance were identified (Abstract, Results lines 117–206, Table 3): [Methodologically Flawed].**  
  First, the Methods (line 76) state that significance was set at $10^{-3}$ "after Bonferroni adjustment ($P = 1/n$, $n = \text{total numbers of SNPs}$)," while line 117 states both "$P \le 0.0001$" and "$-\log_{10}(p) \le 3$." With $n = 32,141$ SNPs, $1/n = 3.11 \times 10^{-5}$ ($-\log_{10} P \ge 4.51$) and family-wise $\alpha = 0.05$ requires $P \le 1.56 \times 10^{-6}$ ($-\log_{10} P \ge 5.81$). At an unadjusted $P \le 10^{-3}$ across 32,141 SNPs and 16 trait–environment combinations ($514,256$ tests), the expected number of false positives under the global null is ~514, which exceeds the 320 MTAs found. Second, in $N = 96$ accessions, 19 to 30 SNPs per trait are each reported to explain 18%–39% of phenotypic variance (summing to $>500\%$ of total trait variance). This occurs because GAPIT reports the full CMLM model $R^2$ (dominated by the $Q$ and $K$ matrices) alongside each SNP rather than the partial $\Delta R^2$ attributable to the SNP itself.

* **Pleiotropic loci on chromosomes 4B, 6B, 7B, 5A, 1B, and 3D simultaneously regulate phenology, canopy temperature, and grain yield across environments (Abstract, Results lines 206, Discussion lines 17–22): [Overstated].**  
  Beyond the uncalibrated $P \le 10^{-3}$ threshold, the identities and chromosomal locations of the claimed pleiotropic markers contradict one another across sections: the Abstract (line 8) places `Kukri_rep_c87210_361`, `D_GA8KES401BNLTU_253`, and `Tdurum_contig1015_131` on chromosomes "5A, 1B, and 3D at the positions 243.59cM, 77.82cM and 292.51cM," whereas Results (line 206) and Discussion (line 17) assign those same three positions to chromosomes "1B, 5A and 3D" in reversed order.

* **Six wheat genotypes (G1, G6, G11, G16, G21, and G39) consistently rank as the top heat-tolerant lines across all eight traits (Discussion line 214, Table 2): [Fragile].**  
  Table 2 lists the exact same six genotypes (permuted in order) as the top six performers out of 96 accessions for every single trait in both normal and heat-stressed environments, including opposite-direction traits such as CTV, CTG, DH, DM, TGW, and GYP. Worse, in Table 2 under Heat Stress for both CMT (line 224) and GYP (line 230), genotype **G6 is listed twice** in the top-six ranking ("G11 followed by G6, G39, G6, G21 and G1" and "G21 followed by G11, G6, G39, G6 and G16"), omitting G16 and G1 respectively.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Audit Raw Phenotypic Data and Re-compute Summary Statistics, Heritability, and Correlation Matrices
* **WHY:** The correlation matrix in Table 1 is mathematically impossible ($\det(R) < 0$), the reported mean TGW of $73\text{ g}$ (line 84) is biologically implausible for hexaploid bread wheat, CTV drops from $35^\circ\text{C}$ (normal) to $27^\circ\text{C}$ (heat stress) before heat stress was even applied at anthesis, and the heritability formula (line 57) multiplies rather than divides by $n_y$ and $n_r$.
* **WHAT:** Re-compute all trait means, variance components, broad-sense heritabilities ($H^2$), and Pearson correlation matrices directly from the raw replicate-level plant measurements, and deposit the raw phenotype table in Supporting Information.
* **HOW:** Fix the heritability formula in line 57 to:
  $$H^2 = \frac{\sigma_g^2}{\sigma_g^2 + \frac{\sigma_{g \times e}^2}{n_y} + \frac{\sigma_e^2}{n_y n_r}}$$
  Verify why DM correlations in Table 1 have negative signs while DH correlations with the same traits are strongly positive (checking whether a minus sign was erroneously typed or whether DM was reverse-coded). Check the raw weighing units for TGW ($73\text{ g}$) and verify the CTV and CTG thermometer logs. Also remove the erroneous claim on line 214 that high broad-sense heritability ($H^2$) indicates "additive genetic effect," as $H^2$ among inbred lines captures total genotypic variance (additive + epistatic).

#### 2. Apply True Multiple-Testing Correction and Report Partial SNP $\Delta R^2$ in GAPIT
* **WHY:** An unadjusted $P \le 10^{-3}$ cutoff across 32,141 SNPs is not a Bonferroni adjustment and produces ratusan of false positives by chance; reporting total CMLM $R^2$ as single-SNP PVE inflates marker effects to 20%–41% in a panel of only $N=96$ lines.
* **WHAT:** Re-run or re-filter the GAPIT association results using Benjamini–Hochberg FDR ($q < 0.05$ or $q < 0.10$) or the suggestive Bonferroni threshold $P < 1/32,141 = 3.11 \times 10^{-5}$ ($-\log_{10} P \ge 4.51$), and report the partial variance explained by each SNP ($\Delta R^2 = R^2_{\text{model with SNP}} - R^2_{\text{model without SNP}}$).
* **HOW:** Extract the `Rsquare.of.Model.without.SNP` and `Rsquare.of.Model.with.SNP` columns from the GAPIT output files, compute their difference ($\Delta R^2 \times 100\%$) as the true SNP PVE in S4 and S5 Tables, and update all PVE ranges in the Results text. Clearly acknowledge that $N = 96$ genotypes provides limited statistical power to detect small-effect polygenic loci and increases susceptibility to the Beavis effect.

#### 3. Correct Pervasive Numerical and Chromosomal Contradictions Across the Text and Tables
* **WHY:** Numerous numbers, chromosome assignments, and counts disagree between adjacent sentences and tables, undermining reproducibility.
* **WHAT & HOW:** Reconcile the following specific errors:
  * **Line 117:** Fix `"-log10(p) <= 3"` to `"-\log_{10}(P) \ge 4.51"` (or the exact threshold used) and resolve the contradiction with `"P <= 0.0001"` (`-\log_{10} P \ge 4`) in the preceding sentence.
  * **Line 137:** The list of chromosomes for FLA under normal conditions (`2A, 3A, 5A, 3B, 4B, 7B, 1D, 3D and 5D`) omits `1A`, yet three sentences later `BS00045521_51` is reported on chromosome `1A` at $341.14\text{ cM}$.
  * **Line 160:** Change `"73.86%"` for `Tdurum_contig48049_705` to match `"37.86%"` in the preceding sentence; also fix `"Four SNPs observed on A-genome, sixteen from the B-genome and seven from D-genome"` ($4 + 16 + 7 = 27 \ne 24$ DH SNPs reported on line 160 and in Table 3).
  * **Line 168:** Resolve `"twenty-seven markers"` vs. `"These sixteen DM related markers"` in consecutive sentences.
  * **Line 183:** Add `DH (24)` to the heat-stress MTA list so it matches Table 3.
  * **Table 2 (lines 224, 230):** Remove the duplicate `G6` entries under Heat Stress for CMT and GYP and explain how the six genotypes were selected (e.g., whether traits were ranked only within `{G1, G6, G11, G16, G21, G39}` rather than across all 96 genotypes).
  * **Abstract (line 8) vs. Results (line 206):** Match the marker order (`Kukri_rep_c87210_361`, `D_GA8KES401BNLTU_253`) to their actual chromosomes (`5A` vs. `1B`) and cM positions.
