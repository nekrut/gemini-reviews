<Blinded Review: TIME_ANON_0464>
**Composite Score:** 6.1 / 10.0 (Rigor: 1.9/3.5 | Claims: 1.7/2.5 | Biology: 1.2/2.0 | Reproducibility: 1.3/2.0)
**Bias Category:** Technical/Assay
**Verdict:** Major Revision
**Study Modality:** Wet-Lab Primary Experimental
**Technology Maturity:** Mature/Classical
**Epistemic Stage:** Basic/Mechanistic Discovery

OVERALL_SCORE: 6.1/10
VERDICT: CAVEATS
ESTIMATED_DECADE: 2010s

---

### 1. Executive Summary / SUMMARY
This experimental study screens a HeLa human cDNA Gal4 yeast two-hybrid (Y2H) library ($2 \times 10^6$ clones) using the nucleoprotein (NP) of a classical swine H1N1 influenza A virus (`A/Sw/NC/44173/00`) as bait in the Clontech Matchmaker Gold (`Y2HGold`/`Y187`) system. The screen isolated 17 positive prey clones representing 10 human host proteins (`PAICS`, `MSANTD3`, `FLJ30306`, `PA28B`, `KCTD9`, `ACOT13`, `TRA2B`, `SLC30A9`, `ATP1B1`, and `CKAP5`), none of which had previously been reported to bind Influenza A NP in Y2H screens, though several (`PAICS`, `PA28B`, `ACOT13`, `ATP1B1`, `CKAP5`) overlapped with genome-wide RNAi screens for influenza replication factors. The authors then compared the interaction strength of each prey against classical swine H1N1 NP (`Sw/NC/00`) versus seasonal human H3N2 NP (`A/Ca/07/04`) using qualitative spot dilutions on $\text{SD}{-}\text{Leu}{-}\text{Trp}{-}\text{His}$ agar at $30^\circ\text{C}$ and $37^\circ\text{C}$ (the natural body temperature of humans vs. $39^\circ\text{C}$ in pigs) and quantitative liquid ONPG $\beta$-galactosidase assays ($n \ge 8$ replicates). While the study includes proper positive (`pGBKT7-53`/`pGADT7-T`) and negative (`pGBKT7-Lam` and empty `pGBKT7`) Y2H controls and provides an honest discussion of Y2H false-positive and false-negative limitations, the entire work remains confined to heterologous yeast assays without a single co-immunoprecipitation, colocalization, or viral infection assay in mammalian cells, and half (5/10) of the recovered preys are partial cDNAs that may expose non-physiological binding surfaces.

### 2. Methodological & Statistical Audit / STRENGTHS & WEAKNESSES

#### STRENGTHS
- **Direct Comparative Evaluation Across Two Viral Lineages and Temperatures:** Testing both classical swine H1N1 (`Sw/NC/00`) and human H3N2 (`Ca/04`) NP baits side-by-side at $30^\circ\text{C}$ and $37^\circ\text{C}$ addresses a biologically relevant hypothesis regarding host adaptation and thermal stability of host-viral protein interactions.
- **Quantitative Reporter Assays with Explicit Negative Controls:** The liquid ONPG $\beta$-galactosidase assay was performed with at least 8 replicates per pair (`n >= 8`) alongside both human lamin C (`pGBKT7-Lam`) and empty bait vector controls (`17.1 ± 1.6` and `18.3 ± 1.7` Miller units), showing ~3-to-8-fold signal over background for the 10 candidates (`56.9` to `134.9` units).
- **Candid Discussion of Y2H Artifacts:** The Discussion transparently acknowledges that 50–70% of Y2H interactions can be false positives due to forced nuclear co-localization, absence of mammalian post-translational modifications, yeast bridging proteins, or misfolded partial cDNA fragments.

#### WEAKNESSES & METHODOLOGICAL AUDIT
- **Complete Absence of Orthogonal Mammalian Validation:** Every experiment in the manuscript is conducted in *Saccharomyces cerevisiae*. There are no co-immunoprecipitation (Co-IP), pull-down, mammalian two-hybrid, immunofluorescence colocalization, or siRNA knockdown experiments in human or porcine cells infected with influenza A virus.
- **Half of the Identified Preys are Partial cDNAs (`Table 1`):** Five of the 10 preys (`PAICS`, `FLJ30306`, `PA28B`, `SLC30A9`, and `CKAP5`) lack complete open reading frames (`Complete ORF: No` in `Table 1`). Partial protein fragments frequently expose hydrophobic core residues that cause sticky or non-physiological interactions in Y2H screens, and the authors do not clone full-length ORFs for these 5 genes to verify whether the full-length human proteins still bind NP.
- **Bait Auto-Activation / Background Difference Between `Ca/04` and `Sw/NC/00` NP Not Tested:** In `Table 2` and `Figure 3`, the negative controls (`pGBKT7-Lam` + `pGADT7-T` and `pGBKT7` + `pGADT7-T`) use lamin or empty vector paired with SV40 Large T antigen, rather than testing `pGBKT7-Ca/04` + empty `pGADT7` and `pGBKT7-Sw/NC/00` + empty `pGADT7`. Notice that in `Table 2`, `Ca/04` NP yields numerically higher $\beta$-galactosidase units than `Sw/NC/00` NP for **all 10 preys** (10 out of 10!). Without measuring the basal transactivation and expression level (via Western blot in yeast) of `pGBKT7-Ca/04` vs. `pGBKT7-Sw/NC/00` paired with empty `pGADT7`, it is impossible to tell whether `Ca/04` NP genuinely binds human factors more strongly or simply has higher steady-state expression/auto-activation in yeast.
- **Lack of Hypothesis Testing in `Table 2` and `Figure 3`:** Although standard deviations are reported for $n \ge 8$ replicates in `Table 2`, no formal statistical tests ($t$-tests, ANOVA, or multiple-testing corrections) are performed to compare `Ca/04` vs. `Sw/NC/00` NP or each candidate against its respective bait-empty control.
- **Internal Textual and Unit Errors:**
  1. On line 95 (`Results`), the text twice refers to **`CKAP3`** ("except for PA28B and **CKAP3** interacting with Sw/NC/00 NP, growth is minimal at 37°C... Sw/NC/00 NP paired with PA28B and **CKAP3** grow significantly less well at 37°C"), whereas the gene in `Table 1`, `Table 2`, and `Figure 2` is **`CKAP5`** (cytoskeleton associated protein 5 / ch-TOG).
  2. On line 180 (`Materials and methods`), the ONPG protocol states: "Following a spin of 5 min at 2,200×g, **200 ml** of culture was placed into a 96 well plate and read at OD420," which is a $1000\times$ unit error for **`200 µl`**.

### 3. Biological / Experimental Grounding & Claim Proportionality
- **Claim 1:** *Ten human proteins from a HeLa cDNA library interact with classical swine H1N1 and human H3N2 NP in yeast two-hybrid assays.* `[Moderately Supported]` — Supported in yeast by growth on histidine-deficient media and ONPG $\beta$-galactosidase activity above lamin/empty controls, though 5/10 clones are truncated fragments and bait-alone auto-activation/expression controls (`pGBKT7-NP` + empty `pGADT7`) were omitted.
- **Claim 2:** *Five of the identified interactors (`PAICS`, `PA28B`, `ACOT13`, `ATP1B1`, `CKAP5`) were previously hits in genome-wide RNAi screens for influenza replication, supporting their biological relevance.* `[Moderately Supported]` — The cross-referencing against published RNAi screens is accurate and appropriately caveated, though direct physical interaction in mammalian cells remains unproven.
- **Claim 3:** *`PA28B` and `CKAP5` show reduced interaction with swine `Sw/NC/00` NP compared to human `Ca/04` NP at $37^\circ\text{C}$.* `[Fragile]` — Based solely on qualitative yeast spot growth at $37^\circ\text{C}$ (`Figure 2B`), whereas the quantitative ONPG assay (`Table 2`) was only conducted at $30^\circ\text{C}$ and showed higher signal for `Ca/04` NP across all 10 preys without Western blot normalization of bait expression.

### 4. Reproducibility & Data Completeness
- **Accession Numbers & Strain Identifiers:** GenBank accession numbers for all 10 human genes are listed in `Table 1`, and influenza strains (`A/Sw/NC/44173/00` and `A/Ca/07/04`) are specified, though the exact cDNA start/stop coordinates of the 5 partial ORF clones (`PAICS`, `FLJ30306`, `PA28B`, `SLC30A9`, `CKAP5`) are not reported.
- **Experimental Details:** Y2H transformation, media recipes, spot dilution volumes, and ONPG Miller unit equations (`1,000 × OD420 / (t × V × OD600)`) are clearly described.
</Blinded Review: TIME_ANON_0464>
