<Blinded Review: TIME_ANON_0682>
**Composite Score:** 4.8 / 10.0 (Rigor: 1.5/3.5 | Claims: 1.1/2.5 | Biology: 1.0/2.0 | Reproducibility: 1.2/2.0)
**Bias Category:** Statistical/Design
**Verdict:** Major Revision
**Study Modality:** Hybrid Computational + Wet-Lab
**Technology Maturity:** Mid-Stage High-Throughput
**Epistemic Stage:** Clinical/Observational

OVERALL_SCORE: 4.8/10
VERDICT: CAVEATS
ESTIMATED_DECADE: 2010s

---

### 1. Executive Summary / SUMMARY
This candidate-gene genetic association study evaluates whether common single nucleotide polymorphisms (SNPs) in `CACNA1C` (encoding the $\alpha_{1\text{C}}$ subunit of the L-type voltage-gated calcium channel $\text{Ca}_v1.2$) are associated with autism spectrum disorder (ASD) in a Han Chinese family cohort using the transmission disequilibrium test (`FBAT` and `Haploview`). In Stage 1 (discovery), the authors genotyped 18 tagging SNPs across `CACNA1C` using the Sequenom MassARRAY iPLEX platform in 239 nuclear trios ($717$ individuals), finding no statistically significant associations (`Table 1`), with two completely linked SNPs (`rs1006737` and `rs4765905`, $r^2 = 1.0$, $\text{MAF} = 0.066$) showing nominal trends ($p = 0.071$ and $p = 0.096$). In Stage 2, the authors genotyped only `rs1006737` and `rs4765905` in an additional 314 trios and analyzed the pooled sample of 553 trios ($1,659$ individuals), reporting nominal over-transmission of the major `G` allele for both SNPs ($Z = 2.105$, unadjusted $p = 0.035$; `Table 2`) and significant two-marker haplotype association (`G-G` $p = 0.030$, `A-C` $p = 0.023$, global $p = 0.046$, permutation $p = 0.027$; `Table 3`). Forensic statistical auditing reveals several major methodological weaknesses: (1) `Table 1` omits one of the 18 SNPs (`17` SNPs listed); (2) the independent replication cohort of 314 trios is never reported separately, and exact algebraic subtraction of `Table 1` from `Table 2` proves that the association in the 314 new trios was **statistically null** ($Z = -1.195, p = 0.232$); (3) single-SNP $p$-values ($p = 0.035$) were never corrected for testing 18 SNPs (where Bonferroni $\alpha \approx 0.0029$), while the 10,000-permutation correction was applied *only* within the cherry-picked 2-SNP haplotype block ($r^2 = 1.0$); and (4) the putative autism risk allele (`G`) is the **opposite allele** to the established European psychiatric GWAS risk allele (`A`).

### 2. Methodological & Statistical Audit / WEAKNESSES & METHODOLOGICAL AUDIT
- **Forensic Decomposition of Stage 1 (239 Trios) vs. Stage 2 (314 Added Trios) Proves Replication Failure:**
  - The authors selected `rs1006737` and `rs4765905` from the 239-trio discovery screen solely because they had the lowest $p$-values ($p = 0.071$ and $p = 0.096$), added 314 trios, and then reported **only the combined 553-trio statistics** ($Z = 2.105, p = 0.035$ in `Table 2`) without testing whether the 314 added trios independently replicated the signal.
  - Because `FBAT` additive score statistics $U = S - E(S)$ and their variances $\text{Var}(S)$ sum linearly across independent nuclear families, we can compute the exact test statistic in the 314 replication trios (`553 - 239 = 314` trios; `124 - 56 = 68` informative heterozygous families for `rs1006737`):
    - **Stage 1 (239 trios, `Table 1`):** $S_A = 23.0$, $E(S_A) = 30.0$, $U_1 = -7.0$, $\text{Var}(S_1) = 15.00 \implies Z_1 = -7.0 / \sqrt{15.00} = -1.807$ ($p = 0.071$).
    - **Pooled Stage 1 + 2 (553 trios, `Table 2`):** $S_A = 53.0$, $E(S_A) = 65.0$, $U_{\text{total}} = -12.0$, $\text{Var}(S_{\text{total}}) = 32.50 \implies Z_{\text{total}} = -12.0 / \sqrt{32.50} = -2.105$ ($p = 0.035$).
    - **Independent Stage 2 Replication Cohort (314 trios alone):**
      $$S_{A,2} = 53.0 - 23.0 = 30.0, \quad E(S_{A,2}) = 65.0 - 30.0 = 35.0, \quad \text{Var}(S_2) = 32.50 - 15.00 = 17.50$$
      $$Z_{\text{Stage 2}} = \frac{30.0 - 35.0}{\sqrt{17.50}} = \frac{-5.0}{4.1833} = -1.195 \quad (\text{two-tailed } p = 0.232)$$
  - Thus, the independent replication cohort of 314 trios did **not** show a significant association ($p = 0.232$), and pooling Stage 1 + Stage 2 without adjusting for the interim selection of the top hit out of 18 SNPs inflates Type I error.
- **Absence of Experiment-Wide Multiple Testing Correction:**
  - Eighteen tagging SNPs across `CACNA1C` were tested (`Line 39`). Even accounting for LD among the 18 tagging SNPs ($\sim 15\text{--}16$ independent effective tests), the experiment-wide significance threshold is $\alpha \approx 0.003$. The pooled unadjusted $p = 0.035$ in `Table 2` falls an order of magnitude short of experiment-wide significance.
  - Furthermore, the permutation test (`n = 10,000`, `Table 3`) was applied **only** to the 2-marker haplotype constructed from `rs1006737` and `rs4765905`. Because `rs1006737` and `rs4765905` are in complete linkage disequilibrium ($r^2 = 1.0$, `Line 109`), they form a single redundant biallelic block (`G-G` frequency $0.937$, `A-C` frequency $0.062$). Permuting labels within a single pre-selected 2-SNP block corrects only for the 2 haplotypes inside that block (which is why the permutation $p = 0.025\text{--}0.027$ is virtually identical to the unadjusted $p = 0.023\text{--}0.030$), completely ignoring the 16 other SNPs that were screened and discarded!
- **Missing 18th SNP in `Table 1` and Coordinate Discrepancy:**
  - The Abstract, Methods (`Line 39`), and Results (`Line 57`) repeatedly state that **18 SNPs** spanning `2,011,392 bp to 2,668,602 bp` on chromosome 12 were genotyped and analyzed in 239 trios. However, `Table 1` ("Results of family-based association test between 18 SNPs in CACNA1C and autism in 239 trios") contains **only 17 SNPs**, ending at `rs216008` (`2,611,971 bp`). The 18th SNP at `2,668,602 bp` is completely missing from `Table 1` without explanation.
  - Also, `Line 39` contains a typo for `rs4765905` (written as `rs476590`), and the permutation $p$-value for the `rs1006737-rs4765905` haplotype is reported as `p = 0.027` in the Abstract (`Line 7`) and `Table 3` (`Line 115`), but as `p = 0.025` in the Results text (`Line 109`).
- **Severely Underpowered Study Design for Low-MAF Variants ($\text{MAF} = 0.063$):**
  - As the authors acknowledge (`Line 59`), because `rs1006737` and `rs4765905` have a low minor allele frequency in Han Chinese ($\text{MAF} = 0.063$, compared to $0.33\text{--}0.36$ in Europeans), only 124 of the 553 families ($22.4\%$) had a heterozygous parent informative for TDT transmission. Even under an unrealistically large assumed relative risk of $\text{RR} = 1.5$ (whereas Psychiatric Genomics Consortium GWAS odds ratios for `rs1006737` are $\text{OR} \approx 1.08\text{--}1.15$), power in 553 trios was only $58\%$ (`Line 59`), and for a realistic $\text{OR} = 1.15$ power at $\alpha = 0.003$ is $< 5\%$.

### 3. Biological / Experimental Grounding & Claim Proportionality / STRENGTHS
- **[Well Supported] Family-Based Trio Design and Diagnostic Rigor:** Using a family-based TDT/FBAT design across 553 parent-offspring trios eliminates false positives from population stratification, and clinical phenotyping was rigorously conducted by two senior psychiatrists using DSM-IV, ABC ($>53$), and CARS ($>35$) criteria while excluding Asperger syndrome, Rett syndrome, fragile X, tuberous sclerosis, and karyotypic abnormalities. Genotyping quality control (10% blind re-genotyping with $>99\%$ concordance, HWE and Mendelian error checks) is also solid.
- **[Fragile] Claim of Association Between `CACNA1C` (`rs1006737`/`rs4765905`) and Autism in Han Chinese:** Given that the unadjusted $p = 0.035$ does not survive multiple-testing correction for 18 SNPs, fails to reach significance in the 314 replication trios ($p = 0.232$), and involves an allelic reversal (`G` risk allele vs. `A` risk allele in schizophrenia/bipolar GWAS), the claimed association is statistically fragile and likely a false positive or winner's curse artifact.

### 4. Reproducibility & Data Completeness
- **Reproducibility Assessment:** Summary FBAT counts ($S$, $E(S)$, $\text{Var}(S)$, $Z$, $p$) are transparently reported in `Tables 1–3` (allowing exact forensic verification of the Stage 2 replication statistics), except for the omission of the 18th SNP from `Table 1`. Supporting tables (`S1–S7 Tables`) are referenced in the text as external links.
</Blinded Review: TIME_ANON_0682>
