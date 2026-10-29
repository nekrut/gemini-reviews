<Blinded Review: TIME_ANON_0708>
OVERALL_SCORE: 3.2/10
VERDICT: FAILED
ESTIMATED_DECADE: 2000s
**Composite Score:** 3.2 / 10.0 (Rigor: 0.8/3.5 | Claims: 0.9/2.5 | Biology: 0.8/2.0 | Reproducibility: 0.7/2.0)
**Bias Category:** Statistical/Design
**Verdict:** Reject (Fundamental Flaws)
**Study Modality:** Wet-Lab Primary Experimental
**Technology Maturity:** Mature/Classical
**Epistemic Stage:** Clinical/Observational

---

### SUMMARY
### 1. Executive Summary
This immunogenetics study reports sequence-based typing (SBT) of the *HLA-A* locus (exons 2, 3, and 4) in $N = 161$ unrelated Northern Chinese Han individuals from Shanxi, Beijing, and Shenyang. Using PCR amplification and Sanger sequencing analyzed with `MatchTools` and `MT Navigator`, the authors report 74 genotypes and 36 *HLA-A* alleles across 14 serological specificities, led by `A*110101` ($GF = 0.2360$), `A*24020101` ($GF = 0.1646$), `A*020101` ($GF = 0.1553$), and `A*3303` ($GF = 0.1180$). They also report population forensic parameters ($H = 0.8705$, $PIC = 0.8491$, $DP = 0.6014$, and $PPE = 0.9475$) and claim that the population conforms to Hardy-Weinberg equilibrium ($P > 0.05$).

### STRENGTHS
- **Use of IHWG Reference Panel Controls and Exon 2–4 Sequencing:** Including the International Histocompatibility Working Group (IHWG) SBT reference cell panel as positive controls and sequencing exons 2, 3, and 4 resolves 10 distinct `HLA-A*02` subtypes (`A*020101`, `A*0207`, `A*0203`, `A*0206`, `A*0205`, etc.) that low-resolution serological or SSP typing cannot distinguish.

### WEAKNESSES & METHODOLOGICAL AUDIT
### 2. Methodological & Statistical Audit
- **Severe Contradiction Between Reported Homozygosity ($56 / 161 = 34.8\%$) and Claimed Hardy-Weinberg Equilibrium ($P > 0.05$):**
  1. In Results (line 41), the authors report expected heterozygosity $H = 1 - \sum P_i^2 = 0.8705$, which corresponds to an expected homozygosity of $1 - 0.8705 = 0.1295$ ($12.95\%$, or $20.8$ individuals out of $161$).
  2. Yet in the Discussion (line 50), the authors state: *"Fifty-six individuals were homozygous at the HLA-A locus."*
  3. Having $56 / 161 = 34.78\%$ homozygotes (observed heterozygosity $H_{\text{obs}} = 105 / 161 = 65.22\%$) when expected homozygosity under Hardy-Weinberg proportions is $12.95\%$ ($H_{\text{exp}} = 87.05\%$) represents a massive heterozygote deficit ($\chi^2 = 68.1$, $P < 10^{-15}$; inbreeding coefficient $F_{IS} = 0.251$)!
  4. This directly refutes the claim in Results line 36 (`"Hardy-Weiburg [sic] equilibrium test: The exact test showed that Northern Chinese Han population is in the Hardy-Weinberg equilibrium for HLA-A gene (P>0.05)"`) and strongly suggests substantial **PCR allele dropout** (where only one allele amplified with the single `AF`/`AR` primer pair and heterozygotes were misclassified as homozygotes: *"samples containing one allele were considered homozygous and that allele was counted twice"*, line 81).
- **Mathematically Incorrect Formulae and Swapped Numerical Values for `DP` and `PPE`:**
  1. In Materials and Methods (line 83), the authors write the exact same formula for Discrimination Power ($DP = 1 - \sum_{i=1}^n P_i^2$) as for Expected Heterozygosity ($H = 1 - \sum_{i=1}^n P_i^2$), instead of the correct genotype-based formula $DP = 1 - \sum_{k} G_k^2$.
  2. They also write an invalid formula for Probability of Paternity Exclusion: $PPE = \sum_{i=1}^n P_i (1 - P_i)^4$ and a garbled formula for $PIC$ ($\sum_{i-1}^n P_i^2 - \sum_{I=1}^n \sum_{j=i+1}^n 2 p^2 p_j^2$, missing subscript $i$ on $p_i^2$).
  3. Worse still, in both the Abstract (line 7) and Results (line 41), they report `DP = 0.6014` and `PPE = 0.9475`. For a locus with 36 alleles and $H = 0.8705$, the true Discrimination Power ($DP$) is $\sim 0.95 - 0.97$ and the Probability of Paternity Exclusion ($PPE$) is $\sim 0.60 - 0.74$; the authors transposed the numerical values of `DP` and `PPE`!
- **Missing Primary Data Tables (`Table 1` and `Table 2`) and `Figure 1`:** Although referenced in the text, `Table 1` (the list of all 36 alleles and their frequencies), `Table 2` (IHWG panel results), and `Figure 1` are completely absent from the manuscript file.

### 3. Biological / Experimental Grounding & Claim Proportionality
- **Claim 1 (Identification of major *HLA-A* subtype rankings in Northern Chinese Han, with `A*110101`, `A*24020101`, `A*020101`, and `A*3303` as the top four alleles): `[Moderately Supported]`** — Broadly consistent with known Northern Han HLA distributions, though allele frequencies are distorted by the unaddressed excess of called homozygotes ($56/161$).
- **Claim 2 (The sample is in Hardy-Weinberg equilibrium and has $DP = 0.6014$ and $PPE = 0.9475$): `[Methodologically Flawed]`** — Directly contradicted by the 34.8% observed vs. 13.0% expected homozygosity and by the transposed/corrupted `DP` and `PPE` formulas.

### 4. Reproducibility & Data Completeness
- **Missing Allele Frequency Table:** While PCR and sequencing primer sequences (`AF`, `AR`, and exon 2–4 primers) are reported in line 71, the full table of 36 allele counts and 74 genotype counts (`Table 1`) is omitted from the text.
</Blinded Review: TIME_ANON_0708>
