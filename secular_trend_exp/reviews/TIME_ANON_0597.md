<Blinded Review: TIME_ANON_0597>
**Composite Score:** 4.5 / 10.0 (Rigor: 1.3/3.5 | Claims: 1.1/2.5 | Biology: 0.9/2.0 | Reproducibility: 1.2/2.0)
**Bias Category:** Statistical/Design
**Verdict:** Major Revision
**Study Modality:** Wet-Lab Primary Experimental
**Technology Maturity:** Mature/Classical
**Epistemic Stage:** Clinical/Observational

OVERALL_SCORE: 4.5/10
VERDICT: CAVEATS
ESTIMATED_DECADE: 2010s

---

### 1. Executive Summary (SUMMARY)
This case-control candidate-gene association study (`TIME_ANON_0597`) genotypes 7 single nucleotide polymorphisms (SNPs) in the promoter (`-986 G>A`, `-602 G>A`, `-557 A>G`, `-64 A>C`, `-4 A>G`) and exon 8 (`+6359 C>T`, `+6424 G>T`) of the ficolin-2 (*FCN2*) gene by PCR and direct Sanger sequencing in 282 Chinese Han patients with pulmonary tuberculosis (TB) and 254 healthy controls from Zhejiang Province, China. Overall allele frequencies for all 7 SNPs (`P = 0.62` to `0.947`, Table 1) and all 4 major haplotypes (`Global P = 0.934`, Table 3) show zero association with pulmonary TB. However, because three tightly linked SNPs (`-557 A>G`, `-64 A>C`, and `+6424 G>T`, $r^2 > 0.80, D' = 1.0$) had 3 homozygous minor-allele carriers (`GG`, `CC`, `TT`) in the TB group compared to 10–11 in the control group (uncorrected $P = 0.037, 0.038, 0.024$), the authors conclude that these three SNPs are recessive protective factors against pulmonary TB.

A forensic audit reveals that these claimed associations are statistical artifacts of uncorrected multiple testing across 5 inheritance models and small-cell sparse counts ($n = 3$ cases) where the 95% confidence intervals in Table 1 actually cross $1.00$ (`0.073–1.003` and `0.074–1.008`), compounded by undisclosed missing genotypes in Table 1, non-monotonic heterozygote vs. homozygote odds ratios, and unmeasured serum Ficolin-2 protein levels.

### 2. Methodological & Statistical Audit (WEAKNESSES & METHODOLOGICAL AUDIT)
* **Complete Absence of Multiple Testing Correction Across 7 SNPs and 5 Inheritance Models, and 95% Confidence Intervals Crossing Unity in Table 1:**
  - The authors test 7 SNPs across allelic, genotypic, and 5 genetic inheritance models (codominant, dominant, recessive, overdominant, log-additive) plus haplotype tests without applying Bonferroni, Benjamini-Hochberg FDR, or permutation correction.
  - Every allelic test is completely null ($P = 0.620$ to $0.947$), and the global haplotype test is completely null ($P = 0.934$).
  - The only nominal p-values below $0.05$ occur in the rare homozygous minor genotypes of the 3 linked SNPs (`-557 GG`: $10$ controls vs $3$ cases, $P = 0.037$; `-64 CC`: $10$ controls vs $3$ cases, $P = 0.038$; `+6424 TT`: $11$ controls vs $3$ cases, $P = 0.024$).
  - Crucially, look at the 95% confidence intervals reported by the authors themselves in Table 1 (lines 71 and 74):
    - `-557 A>G` (`GG` vs `AA`): $\text{OR} = 0.271$, **$95\%\text{ CI} = 0.073\text{--}1.003$** (crosses $1.0$!).
    - `-64 A>C` (`CC` vs `AA`): $\text{OR} = 0.272$, **$95\%\text{ CI} = 0.074\text{--}1.008$** (crosses $1.0$!).
    - Because the cases cell has only $n = 3$ observations, the asymptotic chi-square approximation is anti-conservative (Fisher's exact test yields $P = 0.049$ and $P = 0.048$), and after correcting for even the 5 inheritance models tested per LD block (effective number of independent SNP blocks $\approx 4$, total model tests $\approx 20$), none of the p-values ($0.01\text{--}0.047$) approach statistical significance ($\alpha_{\text{Bonf}} \approx 0.0025$).
* **Biologically Implausible Non-Monotonicity Between Heterozygotes and Homozygotes:**
  - For all three claimed "protective" variants (`-557 A>G`, `-64 A>C`, `+6424 G>T`), heterozygous carriers (`AG`, `AC`, `GT`) actually occur at **higher** frequency in pulmonary TB patients ($36.2\%\text{--}37.0\%$) than in healthy controls ($31.9\%\text{--}33.1\%$, $\text{OR} = 1.111\text{ to }1.153$), while only the rare homozygotes ($1.0\%$ vs $4.0\%$) are lower. Because the heterozygote excess cancels out the homozygote deficit, the overall minor allele frequencies are virtually identical between TB patients and controls ($0.191$ vs $0.204$, $P = 0.620\text{--}0.701$).
* **Undisclosed Missing Genotypes in Table 1 (Genotype Counts Do Not Sum to $N = 254$ and $N = 282$):**
  - Table 1 states `control group (n = 254)` and `pulmonary TB group (n = 282)`. However, summing the reported genotype counts in Table 1 reveals undisclosed genotyping dropouts across amplicons:
    - In Controls: `-986 G/A` ($224+27+2 = 253$), `-602 G/A` ($247+6+0 = 253$), and `-557 A/G` ($160+83+10 = 253$) sum to **253**; `-64 A/C` ($158+83+10 = 251$) and `-4 A/G` ($226+24+1 = 251$) sum to **251**; only `+6359 C/T` and `+6424 G/T` sum to **254**.
    - In Patients: `-64 A/C` ($174+104+3 = 281$) and `-4 A/G` ($255+25+1 = 281$) sum to **281**, while the other 5 SNPs sum to **282**.
* **No Serum Ficolin-2 Measurements in the Study Cohort and Contradictory Mechanistic Speculation:**
  - Under the misleading heading `"Correlation Analysis"` (line 87) and Table 2, the authors did not measure serum Ficolin-2 protein levels in any of their 536 participants; instead, Table 2 merely tabulates qualitative words (`Higher`, `Lower`, `NS`, `ND`) from 7 prior literature papers.
  - Furthermore, the biological interpretation in the Discussion is internally contradictory: the Introduction (line 18) states that Ficolin-2 activates the lectin complement pathway to cause *"direct elimination of the pathogen"* (and notes in line 20 that low Ficolin-2 predisposes to respiratory infections and leprosy), yet to rationalize why genotypes associated with *lower* Ficolin-2 (`-557 GG`, `-64 CC`, `+6424 TT`) appeared less frequently in TB patients, the Discussion (line 134) pivots to arguing that lower Ficolin-2 protects against TB by reducing complement-mediated macrophage entry, while simultaneously citing that the `+6424 T` allele *enhances* GlcNAc binding!
* **Editorial Errors:**
  - The entire Abstract is duplicated verbatim twice at the top of the manuscript (lines 7 and 9), and in Materials and Methods (line 41), the `-602` SNP site is misprinted as `"-642 sites"`.

### 3. Biological / Experimental Grounding & Claim Proportionality (STRENGTHS)
* **`[Well Supported]` Characterization of *FCN2* allele frequencies and linkage disequilibrium structure in a Southeast Chinese Han cohort ($N = 536$):**
  - The genotyping by direct Sanger sequencing across 536 individuals accurately documents the minor allele frequencies and strong LD block uniting `-557 A>G`, `-64 A>C`, and `+6424 G>T` in the Chinese Han population, matching East Asian reference data.
* **`[Overstated]` Claim that `-557 A>G`, `-64 A>C`, and `+6424 G>T` are protective genetic factors for pulmonary TB that provide a novel strategy for TB prevention:**
  - Based on $n = 3$ vs $10\text{--}11$ homozygotes with uncorrected $P = 0.024\text{--}0.038$, 95% CIs crossing $1.0$, null allelic and haplotype tests ($P > 0.60$), and no replication cohort or serum protein measurements.

### 4. Reproducibility & Data Completeness
* **Adequate Primer and Genotype Count Reporting (`1.2 / 2.0`):**
  - All 3 PCR primer pairs, thermal cycling conditions, rsIDs, and genotype/haplotype count tables are reported in the text. However, individual-level clinical covariates (age, sex, smear/culture positivity status) and sequence trace files are not deposited in a public repository.
</Blinded Review: TIME_ANON_0597>
