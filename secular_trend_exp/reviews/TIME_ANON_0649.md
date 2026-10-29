<Blinded Review: TIME_ANON_0649>
**Composite Score:** 6.9 / 10.0 (Rigor: 2.2/3.5 | Claims: 1.6/2.5 | Biology: 1.6/2.0 | Reproducibility: 1.5/2.0)
**Bias Category:** Statistical/Design
**Verdict:** Minor Revision
**Study Modality:** Wet-Lab Primary Experimental
**Technology Maturity:** Mature/Classical
**Epistemic Stage:** Basic/Mechanistic Discovery

OVERALL_SCORE: 6.9/10
VERDICT: CAVEATS
ESTIMATED_DECADE: 2020s

---

### 1. Executive Summary / SUMMARY
This experimental virology study uses reverse genetics to evaluate the functional impact of five non-synonymous amino acid substitutions (`prM A123V`, `NS1 G894A`, `NS2B M1404I`, `NS3 M2074L`, and `NS3 H2086Y`, plus the `NS3 M2074L/H2086Y` double mutant) identified across contemporary epidemic Zika virus (`ZIKV`) isolates relative to the ancestral Asian strain `ZIKV/Macaca mulatta/Malaysia/P6-740/[YEAR]`. Using an intron-stabilized infectious cDNA clone of the epidemic strain `ZIKV/Homo sapiens/PRI/PRVABC59/[YEAR]` (`pACNR1811`), the authors rescued six mutant viruses containing reversions to the ancestral `P6-740` residues (`Mutants 123, 894, 1404, 2074, 2086, and 2074/2086`) alongside cloned wild-type `PRVABC59` (`WT`). They characterized multi-step growth kinetics in mammalian (`Vero`) and mosquito (`C6/36`) cells via `4G2` flow cytometry and plaque assays, virulence and lethality in adult male and female $Ifnar1^{-/-}$ `A129` mice ($n=6$/group), maternal-fetal pathogenesis in pregnant `A129` dams infected at embryonic day 4.5 (`E4.5`) and necropsied at `E14.5`, viral RNA burdens across maternal and fetal tissues via RT-qPCR, and in vivo genetic stability across 16–18 tissues per mutant via Sanger sequencing. While the reverse genetics system (`pACNR1811`) and the multi-tissue in vivo reversion screen (revealing frequent `V123A` reversion in `Mutant 123`) are substantial experimental strengths, the manuscript suffers from unadjusted multiple pairwise $t$-tests, pseudoreplication of fetal measurements across maternal litters (most severely for `Mutant 123`, where all viable embryos came from a single surviving litter), and a direct contradiction between the Results and Discussion regarding `Mutant 894` replication in Vero cells.

### 2. Methodological & Statistical Audit / STRENGTHS, WEAKNESSES & METHODOLOGICAL AUDIT

#### Key Strengths
- **Intron-stabilized infectious clone engineering and multi-host evaluation:** Inserting a cryptic-promoter-disrupting intron at nucleotide `2956` (`NS1`) of `PRVABC59` in low-copy `pACNR1811` allowed stable propagation in *E. coli* and clean site-directed mutagenesis of six single/double variants, tested across both vertebrate (`Vero`, `A129` mice) and mosquito (`C6/36`) systems.
- **Systematic in vivo Sanger sequencing for reversion (`Table 2`):** Sequencing 16–18 maternal and fetal tissue isolates per mutant virus at necropsy (`E14.5` or death) uncovered that `Mutant 123` (`prM V123`) reverted back to the epidemic `A123` residue in 7/18 tissues (including brain, spleen, uterus, ovary, and embryo head), whereas `Mutant 1404` reverted in 1/17 tissues and the remaining four mutants (`894, 2074, 2086, 2074/2086`) were 100% genetically stable in vivo.

#### Methodological Weaknesses & Audit Findings
1. **Pseudoreplication of Embryo Morphometrics Across Maternal Litters (`Fig. 4B–C`):**
   - In the pregnant dam experiment (`E4.5` infection $\rightarrow$ `E14.5` necropsy, $n=6$ dams per group), fetal survival (`Fig. 4A`), embryo head diameter (`Fig. 4B`), and crown-rump-to-head ratio (`Fig. 4C`) were compared against `WT` and `PBS`.
   - Crucially, the authors note in line 116 that for `Mutant 123`, *"of the 6 pregnant females that were infected by mutant 123, only one female had viable embryos on E14.5."* Consequently, every single data point for `Mutant 123` in `Fig. 4B` and `Fig. 4C` comes from a **single maternal litter** ($N=1$ dam), yet the authors treated individual embryos within that litter as independent replicates in pairwise Student's $t$-tests to claim significant differences in embryo head diameter (`Fig. 4B`) and crown-rump ratio (`Fig. 4C`). In developmental and reproductive toxicology/virology, the pregnant dam (litter) is the experimental unit; treating littermates as independent observations without a hierarchical linear mixed model inflates Type I error.
2. **Unadjusted Multiple Pairwise Student's $t$-Tests:**
   - The Statistical Analysis section (line 65) states: *"Differences in raw values among different groups were compared using the Student's t-test. P values < 0.05 were considered significant."* Across 6 mutant groups + `WT` + `PBS`, 5 time points in growth curves (`Fig. 2`), 4 tissues (`Fig. 3D`, `Fig. 4D`), and multiple morphometric readouts, performing dozens of uncorrected two-sample $t$-tests without one-way/two-way ANOVA and Dunnett's or Holm-Bonferroni correction substantially inflates false-positive findings (such as the sporadic single-tissue RT-qPCR asterisks in `Fig. 3D` and `Fig. 4D`).
3. **Direct Contradiction Between Results and Discussion on `Mutant 894` Growth in Vero Cells:**
   - In the Results section (line 87), the authors state: *"Mutants 123 and 894 grew similarly as WT virus in Vero cells, but grew significantly faster in C6/36 insect cells, both in terms of percentage of infected cells and viral yields in the culture supernatants."*
   - In the Discussion section (line 153), the authors contradict this: *"Mutant 894 also grew more quickly in Vero and C6/36 cells as compared to WT, and showed higher uterus viral load..."*
4. **Absence of a Non-Pregnant Female Control Group in the Sex-Comparison Claims:**
   - The authors compare male `A129` mice (`Fig. 3A–D`) directly to pregnant female `A129` mice (`Fig. 3E–G`, `Fig. 4D`) and discuss sex- and pregnancy-related differences in viral replication (lines 110–113, 146–149), but non-pregnant age-matched female `A129` mice were not included to separate the effect of biological sex from the immunosuppressive state of pregnancy.

### 3. Biological / Experimental Grounding & Claim Proportionality
- **Claim 1:** Reversion of epidemic `PRVABC59` `prM A123` to ancestral `V123` (`Mutant 123`) increases replication in `C6/36` mosquito cells (`~1.5 log`), increases severe fetal resorption (`5/6` dams with zero viable embryos at `E14.5`), and experiences strong in vivo selective pressure to revert back to `A123` in `7/18` mouse tissues. `[Well Supported]` — The high rate of in vivo reversion (`V123 -> A123`) in mice combined with superior growth of `V123` in mosquito `C6/36` cells provides compelling evidence of a host-cycling fitness trade-off at `prM` residue 123.
- **Claim 2:** `NS3 M2074L` (`Mutant 2074`) and `NS3 M2074L/H2086Y` (`Mutant 2074/2086`) exhibit reduced replication in both `Vero` and `C6/36` cells, while `H2086Y` (`Mutant 2086`) restores growth in `C6/36` cells. `[Well Supported]`
- **Claim 3:** Specific mutant viruses (`Mutant 123`, `Mutant 1404`) significantly alter embryo head diameter and crown-rump-to-head ratio (`microcephaly`-like morphometrics) at `E14.5`. `[Fragile]` — Confounded by maternal litter effects ($N=1$ surviving litter for `Mutant 123`), unadjusted $t$-tests, and severe maternal weight loss/morbidity in `Ifnar1-/-` dams.

### 4. Reproducibility & Data Completeness
- **Strengths:** Infectious clone architecture (`Fig. 1`), accession numbers of the 8 reference `ZIKV` strains (`Table 1`), mutation coordinates (`Table 2`), viral rescue yields, flow cytometry antibody (`4G2`), RT-qPCR kit (`Luna Universal Probe One-Step`), and IACUC approval (`160303`) are clearly documented.
- **Deficiencies:** Primer and probe sequences used for the RT-qPCR viral load standard curve (`log10 viral RNA copies/g`) and for the in vivo Sanger sequencing amplicons are not listed.
</Blinded Review: TIME_ANON_0649>
