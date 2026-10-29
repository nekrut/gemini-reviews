<Blinded Review: TIME_ANON_0962>
**Composite Score:** 5.4 / 10.0 (Rigor: 1.7/3.5 | Claims: 1.3/2.5 | Biology: 1.2/2.0 | Reproducibility: 1.2/2.0)
**Bias Category:** Statistical/Design
**Verdict:** Major Revision
**Study Modality:** Hybrid Computational + Wet-Lab
**Technology Maturity:** Mature/Classical
**Epistemic Stage:** Clinical/Observational

OVERALL_SCORE: 5.4/10
VERDICT: CAVEATS
ESTIMATED_DECADE: 2020s

---

### 1. Executive Summary / SUMMARY
This case-control immunogenetics study investigates the association between high-resolution allelic polymorphisms of the seven functional `KIR` genes on the `KIR A` haplotype (`KIR2DL1`, `KIR2DL3`, `KIR2DL4`, `KIR3DL1`, `KIR3DL2`, `KIR3DL3`, and `KIR2DS4`) and their cognate `HLA-A`, `-B`, and `-C` class I ligands with acute lymphoblastic leukemia (`ALL`, $N = 318$) and acute myeloid leukemia (`AML`, $N = 336$) compared against unrelated healthy blood donors ($N = 306$) in the Chinese Southern Han population (`Shenzhen Blood Center`). Using `PCR-SBT` (`AlleleSEQR` for exons 2–4 of `HLA-A/-B/-C` and exon-wide Sanger sequencing for `KIR` genes assigned via `Assign 4.7.1` against `IPD-KIR Release 2.13/2.15`), the authors stratify subjects into `KIR AA` (Controls $N = 167$, ALL $N = 155$, AML $N = 162$) and `KIR Bx` (Controls $N = 139$, ALL $N = 163$, AML $N = 174$) genotypes.

The authors report that among `KIR AA` individuals: (1) `KIR3DL3*001` tends to be protective against AML (`8.4%` vs. `1.3%`, $p = 0.004, P_c = 0.06$), whereas `KIR3DL3*009` is associated with increased AML risk (`29.3%` vs. `47.1%`, $p = 0.001, P_c = 0.016$), attributed to a transmembrane missense polymorphism at codon 300 (`KIR3DL3_N300H`, `AAC > CAC`); (2) `HLA-C2` is protective against AML (`31.1%` vs. `17.9%`, $p = 0.005, P_c = 0.01$); and (3) combinations of strong inhibitory `KIR` alleles with cognate `HLA` ligands (`KIR2DL1*00201 + C2` in ALL, $p = 0.01$; `KIR2DL1*00302 + C2`, $p = 0.008$, `KIR2DL3*00201 + C1`, $p = 0.03$, and `KIR3DL1*00501 + Bw4 80I`, $p = 0.008$ in AML) are protective, whereas in `KIR Bx` individuals, `KIR2DL1*004 + C2` is associated with ALL risk (`0%` vs. `5.5%`, $p = 0.01$).

While the high-resolution exon-wide `KIR` sequencing dataset across 960 individuals is substantial, forensic statistical audit of `Table 2` and `Table 3` reveals **major errors in odds ratio (`OR`) calculations for zero-cell rows, denominator mismatches in `KIR3DL3` carrier percentages, and absence of multiple-testing correction in the `KIR–HLA` interaction analysis (`Table 3`)**.

### 2. Methodological & Statistical Audit / STRENGTHS & WEAKNESSES & METHODOLOGICAL AUDIT

#### Major Statistical & Arithmetic Flaws
1. **Inverted / Mathematically Invalid Odds Ratios (`OR < 1`) for Risk Alleles with `0` Control Carriers in `Table 2` and `Table 3`:**
   - Look at `2DL1*069` in `Table 2` (`KIR AA` group):
     - Healthy controls: `0 / 167 (0%)`
     - ALL patients: `5 / 155 (3.2%)`, reported **`OR = 0.97 (95% CI: 0.94–1.00)`**, $P = 0.06$
     - AML patients: `6 / 162 (3.7%)`, reported **`OR = 0.96 (95% CI: 0.93–0.99)`**, $P = 0.04$
   - Look at `2DL1*004 + C2` in `Table 3` (`KIR Bx` group):
     - Healthy controls: `0 / 139 (0%)`
     - ALL patients: `9 / 163 (5.5%)`, reported **`OR = 0.94 (95% CI: 0.91–0.98)`**, $P = 0.01$
     - AML patients: `6 / 174 (3.4%)`, reported **`OR = 0.97 (95% CI: 0.94–0.99)`**, $P = 0.07$
   - **Audit:** In all four of these comparisons, the allele/interaction is **absent (`0%`) in controls** and **present (`3.2%–5.5%`) in leukemia cases**—meaning it is a **susceptibility/risk factor** ($\text{OR} = \infty$, or with Haldane-Anscombe $0.5$ continuity correction, $\text{OR} \approx 12.2$ to $18.1$!). How did the authors get $\text{OR} = 0.968$ (`150/155`), $\text{OR} = 0.963$ (`156/162`), $\text{OR} = 0.945$ (`154/163`), and $\text{OR} = 0.966$ (`168/174`)? Because when ` IBM SPSS Statistics 20` encounters a zero cell (`a = 0`) in a $2 \times 2$ crosstab, SPSS does not output an Odds Ratio; instead, the authors copied the **"Relative Risk for Cohort (Allele = Negative)"** column ($1 - \text{case carrier rate}$, i.e., $150/155 = 0.968$, $156/162 = 0.963$, $154/163 = 0.945$, $168/174 = 0.966$) and misreported it as an **Odds Ratio (`OR < 1`)** in `Table 2` and `Table 3` while simultaneously claiming in the text that these alleles confer **susceptibility**!
2. **Denominator Discrepancy in `KIR3DL3` Carrier Percentages in `Table 2`:**
   - In `Table 2`, the column headers explicitly state that the `KIR AA` sample sizes are: `Control (N = 167)`, `ALL patients (N = 155)`, and `AML patients (N = 162)`.
   - For `2DL1*00201`, `2DL1*069`, and `2DL3*00201`, the percentages match these denominators: e.g., in ALL (`N = 155`), $34 / 155 = 21.9\%$, $5 / 155 = 3.2\%$, $33 / 155 = 21.3\%$; in AML (`N = 162`), $31 / 162 = 19.1\%$, $6 / 162 = 3.7\%$, $29 / 162 = 17.9\%$.
   - However, for `3DL3*001` and `3DL3*009` in the exact same `Table 2`:
     - In ALL (`N = 155`): `5 (3.8%)` and `59 (44.7%)`. Yet $5 / 155 = 3.23\%$ (not $3.8\%$) and $59 / 155 = 38.06\%$ (not $44.7\%$). Instead, $5 / 132 = 3.79\%$ and $59 / 132 = 44.70\%$!
     - In AML (`N = 162`): `2 (1.3%)` and `72 (47.1%)`. Yet $72 / 162 = 44.44\%$ (not $47.1\%$). Instead, $2 / 153 = 1.31\%$ and $72 / 153 = 47.06\%$!
   - Thus, 23 ALL patients ($155 - 132$) and 9 AML patients ($162 - 153$) had missing `KIR3DL3` genotypes without any footnote or disclosure in `Table 2`.
3. **Lack of Multiple Testing Correction ($P_c$) in `Table 3` and Non-Independence from `HLA-C2` Main Effect:**
   - In `Table 2`, the authors apply Bonferroni correction ($P_c$), which eliminates significance for `2DL1*00201` ($P = 0.04 \to P_c = 0.41$) and `2DL3*00201` ($P = 0.03 \to P_c = 0.50$).
   - However, in `Table 3` (*KIR–HLA interactions*), no Bonferroni correction ($P_c$) column is reported at all! Across dozens of tested `KIR allele + HLA ligand` pairs in `Supplementary Tables S7–S8`, unadjusted $P$-values of $0.008$, $0.01$, and $0.03$ do not survive Bonferroni correction for the number of allele-ligand combinations tested.
   - Furthermore, for `2DL3*00201 + C1` in `Table 3`, the carrier counts (`Control = 47 [28.1%]`, `ALL = 33 [21.3%]`, `AML = 29 [17.9%]`, $P = 0.03$) are **100% identical** to the marginal `2DL3*00201` allele counts in `Table 2` (`47`, `33`, `29`, where $P_c = 0.50$ was non-significant!), because nearly all Chinese Han `KIR AA` individuals carry at least one `HLA-C1` allele. Similarly, the `2DL1*00302 + C2` decrease in AML (`30.5%` vs. `17.9%`, $P = 0.008$) simply mirrors the marginal `HLA-C2` frequency difference (`31.1%` vs. `17.9%`, $P = 0.005$) since `2DL1*003` is present in >89% of all subjects.

#### Strengths
1. **High-Resolution Exon-Wide `KIR` and `HLA` Genotyping:** Full-exon sequencing of 7 functional `KIR` genes alongside 4-digit `HLA-A`, `-B`, `-C` `PCR-SBT` across 960 subjects (identifying 28 novel `KIR` alleles verified by TA cloning) is a substantial technical effort in a notoriously repetitive locus.

### 3. Biological / Experimental Grounding & Claim Proportionality
- **Claim 1:** `KIR3DL3*009` and the transmembrane `KIR3DL3_H300` allotype are associated with increased susceptibility to AML in Chinese Southern Hans ($P = 0.001, P_c = 0.016$). `[Moderately Supported]` — Statistically survives Bonferroni correction within the `KIR3DL3` locus, though no functional expression (`KIR3DL3` or `HHLA2`) or cytotoxicity validation was performed, and 23 ALL / 9 AML samples had undisclosed missing `KIR3DL3` calls in `Table 2`.
- **Claim 2:** Specific `KIR–HLA` interactions (`2DL1*00201+C2`, `2DL1*00302+C2`, `2DL3*00201+C1`, `3DL1*00501+Bw4 80I`, and `2DL1*004+C2`) significantly protect against or predispose to ALL/AML. `[Overstated]` — `Table 3` omits multiple-testing correction ($P_c$), conflates marginal `HLA-C2` and `2DL3*00201` frequencies with epistatic interaction, and misreports SPSS cohort relative risks (`0.94–0.97`) as Odds Ratios for zero-count cells.

### 4. Reproducibility & Data Completeness
- **Data Completeness:** Summary counts are given in `Tables 1–3` and `Supplementary Tables S1–S8`, though GenBank/IPD accession numbers for the 28 novel `KIR` alleles are not listed in the main text.
- **Required Corrections:** Replace the invalid `OR < 1` values (`0.94–0.97`) for zero-control rows in `Table 2` and `Table 3` with Haldane-corrected Odds Ratios, disclose the true denominators ($N = 132$ and $N = 153$) for `KIR3DL3` in `Table 2`, and apply multiple-testing correction ($P_c$) to `Table 3`.
</Blinded Review: TIME_ANON_0962>
