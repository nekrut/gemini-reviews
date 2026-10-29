<Blinded Review: TIME_ANON_0278>
**Composite Score:** 1.8 / 10.0 (Rigor: 0.4/3.5 | Claims: 0.4/2.5 | Biology: 0.4/2.0 | Reproducibility: 0.6/2.0)
**Bias Category:** Statistical/Design
**Verdict:** Reject (Fundamental Flaws)
**Study Modality:** Wet-Lab Primary Experimental
**Technology Maturity:** Commodity/Hype-Cycle Template
**Epistemic Stage:** Translational/Preclinical/Biomarker

---

### 1. Executive Summary
This study reports candidate-gene Sanger sequencing of pooled and individual DNA samples from $N = 255$ Kele sows across three genes (*PAEP*, *KRT10*, and *BMP7*), claiming to identify nine intronic/exonic SNPs (`PAEP`: `g.1884992 T>C`, `g.1885125 G>C`, `g.1885158 G>A`; `KRT10`: `g.21643714 G>A`, `g.21643741 G>A`, `g.21644056 C>T`; `BMP7`: `g.57642402 C>T`, `g.57642555 A>C`, `g.57642525 T>G`) and associating their genotypes and diplotypes with five litter and birth-weight traits (TNB, NBA, NW, BW, LW). A forensic mathematical and cross-table audit reveals **catastrophic internal data integrity failures**: (1) mathematically impossible allele frequencies and expected heterozygosity ($H_e = 0.69 > 0.50$) for a biallelic SNP in Table 2; (2) copy-pasted *PAEP* SNP headers inside the *KRT10* linkage disequilibrium table (Table 6); (3) **swapped and mutually contradictory trait means and standard deviations** between identical homozygote groups in the single-SNP tables (Tables 9 & 11) and the diplotype tables (Tables 10 & 12); and (4) wildly inconsistent overall cohort means across rows of the exact same $N = 255$ animals. These pervasive numerical contradictions invalidate the empirical results.

### 2. Methodological & Statistical Audit
- **Forensic Audit 1 — Mathematically Impossible Allele Frequencies and $H_e = 0.69$ in Table 2 (Line 90):**
  - For a biallelic locus with allele frequencies $p$ and $q = 1 - p$, expected heterozygosity $H_e = 2pq = 2p(1-p)$ has an absolute mathematical maximum of **$0.500$** (attained at $p = q = 0.50$). Yet in Table 2 (row 1, `PAEP g.1884992 T>C`) and in the text on line 84, the authors report **$H_e = 0.69$**, which is mathematically impossible for any biallelic SNP.
  - Furthermore, the genotype counts reported in that exact row are `TT = 173`, `TC = 65`, `CC = 17` ($N = 255$ pigs, $2N = 510$ alleles). The actual allele counts are $T = 2(173) + 65 = 411$ ($p_T = 411/510 = 0.806$) and $C = 2(17) + 65 = 99$ ($q_C = 99/510 = 0.194$), which agrees with the haplotype sum in Table 3 ($H_1 + H_2 = 272 + 139 = 411$ `T` alleles; $H_3 = 99$ `C` alleles) and yields true $H_e = 2(0.806)(0.194) = 0.313$ and Hardy-Weinberg $\chi^2 = 8.95$ ($P = 0.0028 < 0.01$, violating HWE!). Yet Table 2 fabricates allele frequencies of `T = 0.65`, `C = 0.35`, `He = 0.69`, and claims HWE compliance ($\chi^2 = 3.04, P > 0.05$).
- **Forensic Audit 2 — Swapped Trait Means & SDs Between Single-SNP Tables (Tables 9 & 11) and Diplotype Tables (Tables 10 & 12):**
  - **In *PAEP* (Table 3, Table 9, Table 10):** Only three haplotypes exist (`H1 = TGG`, `H2 = TCA`, `H3 = CGG`). Therefore:
    - Every pig with diplotype `H2H2` (`TT-CC-AA`, $n = 37$) is *identically* the `CC (37)` homozygote group at `g.1885125 G>C` and the `AA (37)` homozygote group at `g.1885158 G>A`.
    - Every pig with diplotype `H3H3` (`CC-GG-GG`, $n = 17$) is *identically* the `CC (17)` homozygote group at `g.1884992 T>C`.
    - Yet when comparing Table 9 (single-SNP associations) with Table 10 (diplotype associations), the trait means and SDs of the $n = 17$ group and the $n = 37$ group are **completely swapped**:
      - In Table 9, `CC (17)` at `g.1884992` has `TNB = 8.50 ± 1.73`, `NBA = 7.50 ± 1.57`, `NW = 7.66 ± 0.80`, `BW = 6.00 ± 1.28`, `LW = 40.51 ± 10.33`, whereas in Table 10 those exact five means and SDs (`8.50 ± 1.73`, `7.50 ± 1.57`, `7.66 ± 0.80`, `6.00 ± 1.28`, `40.51 ± 10.33`) are assigned to **`H2H2 (37)`**!
      - Conversely, in Table 9, `CC (37)` at `g.1885125` has `TNB = 13.50 ± 2.74`, `NBA = 13.00 ± 2.19`, `NW = 10.03 ± 1.73`, `BW = 11.50 ± 1.64`, `LW = 60.58 ± 2.71`, whereas in Table 10 those exact five means and SDs (`13.50 ± 2.74`, `13.00 ± 2.19`, `10.03 ± 1.73`, `11.50 ± 1.64`, `60.58 ± 2.71`) are assigned to **`H3H3 (17)`**!
  - **In *KRT10* (Table 7, Table 11, Table 12):** The exact same fabrication/swap occurs!
    - At `g.21643714 G>A` (Table 11), `GG (200)` has `TNB = 7.90 ± 2.18, NBA = 6.20 ± 2.15, NW = 5.40 ± 1.43, BW = 1.20 ± 0.16, LW = 34.48 ± 6.53` and `AA (10)` has `9.01 ± 2.55, 6.76 ± 2.25, 5.79 ± 2.28, 1.18 ± 0.25, 36.20 ± 6.46`. In Table 12 (diplotypes), `H4H4 (10)` (`AA-GG-CC`, the exact same 10 pigs as `AA (10)`) is given the means of `GG (200)` (`7.90 ± 2.18, 6.20 ± 2.15, 5.40 ± 1.43, 1.20 ± 0.16, 34.48 ± 6.53`)!
    - Similarly, at `g.21643741 G>A` (Table 11), `GG (162)` has `10.4 ± 1.24, 6.91 ± 1.19, 6.13 ± 1.38, 1.32 ± 0.21, 38.67 ± 6.19`, which in Table 12 is pasted onto `H3H3 (15)` (`10.40 ± 1.24, 6.91 ± 1.19, 6.13 ± 1.38, 1.32 ± 0.21, 38.67 ± 6.19`)!
- **Forensic Audit 3 — Impossible Cohort Grand Means Across Rows of the Same 255 Sows:**
  - Every SNP in Tables 9, 11, and 13 partitions the exact same $N = 255$ sows. Therefore, the weighted average $\bar{Y} = \frac{1}{255}\sum n_i \bar{y}_i$ of any trait must be invariant across all SNPs.
  - Yet in Table 9, the weighted mean of `BW` (birth weight) across the 255 sows at `g.1884992` is $\frac{173(1.25) + 65(1.30) + 17(6.00)}{255} = 1.58\text{ kg}$ (note that a single-piglet birth weight of `6.00 kg` or `11.50 kg` is biologically absurd for a newborn piglet, where normal BW is $\sim 1.2\text{ kg}$ and litter weight LW is $\sim 8$–$10\text{ kg}$!), whereas at `g.1885125` in the very next row the weighted mean of `BW` is $\frac{153(1.13) + 65(1.27) + 37(11.50)}{255} = 2.67\text{ kg}$, and across all 255 sows in Table 11 (*KRT10* `g.21643714`) the weighted mean of `BW` is $1.18\text{ kg}$!
  - Similarly, in Table 11 (*KRT10*), the weighted mean of `TNB` across the 255 sows is $8.20$ at `g.21643714`, $9.78$ at `g.21643741`, and $9.03$ at `g.21644056`. It is mathematically impossible for the same 255 pigs to have different grand means across different columns of their genotype table.
- **Forensic Audit 4 — Copy-Paste Errors and Contradictory Cohort Description:**
  - **Table 6 (Line 159):** The column headers of the *KRT10* linkage disequilibrium matrix are `g.1884992 T>C | g.1885125 G>C | g.1885158 G>A` (the *PAEP* SNPs!), copy-pasted from Table 5.
  - **Methods Line 30 Contradiction:** States that the 255 Kele sows were *"multiparous sows (2–4 parities)... of the same age (450 days)... The first-parity reproductive data of 255 pigs were measured."* Sows with 2–4 parities cannot all be exactly 450 days old.
  - **Abstract Line 7 Typos:** Refers to `g.21648641 G>A` (instead of `g.21643741 G>A`) and repeats *"higher number of piglets born alive and number of piglets born alive"*.

### 3. Biological / Experimental Grounding & Claim Proportionality
- **Claim 1:** Nine SNPs and their diplotypes across *PAEP*, *KRT10*, and *BMP7* are significantly associated with litter size and piglet weight traits in Kele sows and can serve as molecular breeding markers. `[Methodologically Flawed]` — The genotype-trait and diplotype-trait summary statistics in Tables 2, 6, 9, 10, 11, 12, 13, and 14 are riddled with mathematical impossibilities, swapped group means, biologically impossible newborn piglet weights (`11.50 kg` per piglet), and inconsistent cohort grand means.

### 4. Reproducibility & Data Completeness
- **Strengths:** Primer sequences for *PAEP*, *KRT10*, and *BMP7* are listed in Table 1.
- **Limitations:** No raw individual-level genotype or phenotype dataset is provided, and the published summary tables fail basic arithmetic and algebraic conservation checks.
</Blinded Review: TIME_ANON_0278>
