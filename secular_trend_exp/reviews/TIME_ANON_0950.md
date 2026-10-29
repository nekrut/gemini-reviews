<Blinded Review: TIME_ANON_0950>
**Composite Score:** 5.2 / 10.0 (Rigor: 1.6/3.5 | Claims: 1.3/2.5 | Biology: 1.3/2.0 | Reproducibility: 1.0/2.0)
**Bias Category:** Statistical/Design
**Verdict:** Major Revision
**Study Modality:** Wet-Lab Primary Experimental
**Technology Maturity:** Mid-Stage High-Throughput
**Epistemic Stage:** Basic/Mechanistic Discovery

OVERALL_SCORE: 5.2/10
VERDICT: CAVEATS
ESTIMATED_DECADE: 2020s

---

### 1. Executive Summary / SUMMARY
This study investigates the timing and host DNA double-strand break (DSB) repair pathway dependencies of de novo hepatitis B virus (HBV) DNA integration using a replication-deficient reporter virus (`HBV-Zeo`, in which the PreS1/PreS2/S ORF is replaced by a transthyretin-driven Zeocin-resistance cassette) infecting `HepG2-NTCP` cells followed by 25-day Zeocin selection (`0.5 mg/mL` or `250 µg/mL`). Quantifying colony formation ($\sim 20$ colonies per $1.5 \times 10^5$ infected cells, $\sim 1/7,500$) and confirming $1$–$2$ integrated copies per cell across 106 clones by `EcoRI` ddPCR normalized to `RNase P`, the authors apply `0.4 Gy` X-ray irradiation across a post-infection time course (`0` to `76 hpi`) and report a $2$–$3$-fold increase in integration colonies when cells are irradiated between `16` and `52 hpi`, followed by a drop at `76 hpi`. They then test small-molecule inhibitors of `POLQ`/MMEJ (`ART558`), `ATR`/HR (`AZD6738`, `VE822`), and `DNA-PKcs`/NHEJ (`NU7441`) in a "pre-integration" window (`-24 to 0 hpi`) versus a "co-integration" window (`4 to 72 hpi`), concluding that MMEJ (`POLQ`) mediates early HBV integration while `ATR` inhibition increases integration. However, the manuscript suffers from severe internal contradictions between the Abstract, Results, Discussion, and Figure legends regarding the `ATR` inhibitor effect sizes, normalization denominators, and direction of effect.

### 2. Methodological & Statistical Audit / STRENGTHS & WEAKNESSES & METHODOLOGICAL AUDIT

#### STRENGTHS
- **Clean Single-Round Integration Reporter (`HBV-Zeo`) with Entry Control:** Using `Myrcludex B` entry blockade (which reduces Zeocin-resistant colonies to zero) and validating $1$–$2$ copies/cell by ddPCR in 106 single-cell clones cleanly isolates first-round input viral DNA integration from ongoing intracellular replication.
- **High-Resolution X-Ray DSB Time Course (Fig. 2):** Pulsing `0.4 Gy` X-ray irradiation across 12 time points (`0, 15 min, 1, 2, 4, 8, 12, 16, 20, 28, 52, 76 hpi`) while verifying invariant total intracellular HBV DNA by digital PCR (Fig. 2B) provides compelling kinetic evidence that input viral DNA becomes available as a nuclear integration substrate at `16–52 hpi` (coincident with nuclear import and cccDNA formation), refuting the 15-minute integration claim from prior woodchuck models.

#### WEAKNESSES & METHODOLOGICAL AUDIT
- **Severe Internal Contradictions in `ATR` Inhibitor Results and Normalization Artifact (Abstract vs. Results vs. Discussion):**
  1. **Unexplained Discrepancy in Fold-Change Numbers:** The Abstract states: *"suppression of homologous recombination (HR) via ATR inhibitors significantly enhances integration rates (2.4–2.8-fold)"*. However, those numbers (`2.4–2.8-fold`) never appear anywhere in the Results! Instead, Results line 120 reports that the ratio of co-integration to pre-integration treatment for `VE822` is **$9.62 \pm 2.13$-fold ($p < 0.0001$)** and for `AZD6738` is **$1.33 \pm 0.34$-fold ($p = 0.27$, non-significant!)**.
  2. **Division-by-Near-Zero Normalization Artifact (Fig. 3E vs 3F):** In Results line 118 and Fig. 3E, pre-integration treatment (`-24 to 0 hpi`) with `AZD6738` and `VE822` nearly *abolished* colony formation compared to untreated controls (`mean clone number AZD6738: 0; VE822: 1.0 vs untreated cell: 13.7`). In Fig. 3F (line 120), the authors compute "normalized" integration rates by dividing the co-integration colony rate by the pre-integration treatment control! Because pre-integration `VE822` killed/blocked almost all colonies (`1.0` vs `13.7`), dividing the co-integration value by the collapsed pre-integration baseline artificially inflates the `VE822` ratio to `9.62-fold` (and for `AZD6738`, dividing by a mean clone number of `0` is mathematically undefined!). Looking at the unnormalized absolute colony counts in Fig. 3E, co-integration `AZD6738` is *lower* than untreated controls.
  3. **Direct Self-Contradiction Between Results and Discussion:** Results line 118 states: *"When comparing untreated cells to cells treated with DNA repair inhibitors at pre-integration timepoints, we found that inhibition of the ATR significantly reduced colony formation compared to untreated controls (mean clone number AZD6738: 0; VE822: 1.0 vs untreated cell: 13.7)."* Yet Discussion line 133 states the exact opposite: *"(a) ATR inhibition significantly increased integration rates when applied at pre-integration timepoints"*!
- **Contradiction Between Text and Figure 3 Caption on `dPCR` vs `HBeAg` Assays:**
  - Results line 116 states: *"For the pre-integration treatment, we quantified HBeAg secretion... For the co-integration treatment, we measured total intracellular HBV DNA levels"*.
  - Figure 3 caption (line 108) states the exact opposite: *"(C) Assessment of viral infection at pre-integration treatment time-points was measured by dPCR of total intracellular HBV DNA, while (D) viral infection at co-integration treatment time-points was measured by HBeAg secretion."*
- **Multiple Additional Text/Table Errors:**
  - Table 2 title and line 69 state that primers/probes for `HBx` are listed in Table 2, but Table 2 only lists `Zeo-R` and `RNaseP`; the `HBx` primer/probe sequences are completely missing.
  - Line 71 defines `HBeAg` as *"Secreted Hepatitis E Antigen (HBeAg)"* instead of Hepatitis B e-antigen.
  - Line 22 describes the virus as a *"replication-competent reporter virus"* whereas lines 7, 30, and 127 state it is *"replication-deficient"*.
  - Line 32 lists Zeocin selection at `0.5 mg/mL` (`500 µg/mL`) and `100 µM` Myrcludex B, whereas line 79 and Fig. 1A legend state `100 mM` Myrcludex B and `250 µg/mL` Zeocin.
  - Line 44 states pre-integration inhibitors were applied *"for 24 h prior to HBV-Zeo infection, and at 72 h post-infection (hpi)"*, contradicting line 112 (`-24 to 0 hpi`).

### 3. Biological / Experimental Grounding & Claim Proportionality
- **Claim 1:** Input HBV DNA integration occurs predominantly within a 16–52 hpi (12–76 hpi) window post-infection, coinciding with nuclear entry/cccDNA formation rather than within 15 minutes of infection. `[Well Supported]`
- **Claim 2:** Pharmacological inhibition of `POLQ` (`ART558`) during the 4–72 hpi window suppresses HBV integration colony formation to ~17% of controls, implicating MMEJ. `[Moderately Supported]` — Supported by `ART558` treatment, though genetic `POLQ` knockout and junction sequencing under `ART558` were not performed.
- **Claim 3:** `ATR` inhibition (`AZD6738`, `VE822`) enhances HBV integration by 2.4–2.8-fold (or 9.62-fold). `[Methodologically Flawed]` — Confounded by severe pre-integration cytotoxicity/entry arrest (`0` and `1.0` colonies) used as the denominator in Fig. 3F, non-significance of `AZD6738` in Fig. 3F ($p=0.27$), and contradictory numbers between the Abstract (`2.4–2.8-fold`) and Results (`9.62-fold` / `1.33-fold`).

### 4. Reproducibility & Data Completeness
- **Missing Primer Sequences:** `HBx` dPCR primer and probe sequences referenced in Table 2 are omitted from Table 2.
- **Data Availability:** "Data will be made available on request" with no raw colony count tables provided in the main text.
</Blinded Review: TIME_ANON_0950>
