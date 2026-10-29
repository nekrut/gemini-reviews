<Blinded Review: TIME_ANON_0555>
OVERALL_SCORE: 8.1/10
VERDICT: PASS
ESTIMATED_DECADE: 1990s
**Composite Score:** 8.1 / 10.0 (Rigor: 2.6/3.5 | Claims: 2.1/2.5 | Biology: 1.9/2.0 | Reproducibility: 1.5/2.0)
**Bias Category:** Technical/Assay
**Verdict:** Minor Revision
**Study Modality:** Wet-Lab Primary Experimental
**Technology Maturity:** Mature/Classical
**Epistemic Stage:** Basic/Mechanistic Discovery

---

### 1. Executive Summary / SUMMARY
This cell-biological virology study investigates the spatiotemporal intracellular localization and transport of Tobacco Mosaic Virus (TMV) viral RNA (both plus-strand genomic vRNA and minus-strand replicative RNA) in synchronized tobacco BY-2 suspension protoplasts from 2 to 32 hours post-inoculation (hpi). Using strand-specific digoxigenin (DIG)- and fluorescein-labeled riboprobes for confocal fluorescence *in situ* hybridization (FISH) combined with indirect immunofluorescence against the viral 126/183-kDa replicase, movement protein (MP and `MP:GFP`), the luminal endoplasmic reticulum (ER) chaperone BiP, microtubules ($\alpha$-tubulin), and filamentous actin, alongside genetic dissection with a movement-protein-deficient TMV mutant (`vRNA-ΔM`, `pU3/1214-ΔM`) and pharmacological inhibitors (`Brefeldin A`, `oryzalin`, and `cytochalasin D`), the authors demonstrate that: (1) plus- and minus-strand TMV RNAs colocalize with the viral replicase and ER marker BiP in perinuclear bodies early in infection (`4–6 hpi`), and this initial perinuclear ER association is independent of MP; (2) during mid-stage infection (`8–16 hpi`), functional MP is required to coalesce vRNA and ER membranes into large irregular cytoplasmic bodies ("viroplasms" / X-bodies) and to align small vRNA-MP ribonucleoprotein puncta along cytoplasmic microtubules; and (3) at late stages (`18–32 hpi`), vRNA and MP accumulate in peripheral peripheral spots and surface protrusions in an MP-, ER/endomembrane (`Brefeldin A`-sensitive)-, and actin (`cytochalasin D`-sensitive)-dependent manner.

### 2. STRENGTHS
- **Direct Strand-Specific Detection of Viral RNA Combined with Dual-Label Confocal Microscopy:** Previous studies inferred vRNA localization indirectly from `MP:GFP` fluorescence. By establishing a riboprobe FISH protocol in plant protoplasts capable of resolving both plus-strand and minus-strand TMV RNA alongside protein markers (BiP, tubulin, replicase, and `MP:GFP`), this study directly links viral RNA replication complexes to cortical ER and cytoskeletal networks.
- **Clever Sequential GFP Imaging and Photobleaching Protocol (Figure 5):** Because protease/organic fixation during ISH destroys native `MP:GFP` fluorescence (and anti-GFP antibodies cross-reacted non-specifically after ISH), the authors imaged native `MP:GFP` fluorescence first in fixed cells, completely photobleached the GFP signal with blue excitation light (`450–490 nm`), and then performed fluorescein-labeled riboprobe FISH on the exact same relocated cells (`CellFinder` slides) to demonstrate precise colocalization of vRNA and `MP:GFP` across early, middle, and late stages.
- **Genetic Dissection of Movement Protein Function (`vRNA-ΔM`, Figure 8):** Comparing wild-type TMV (`U3/1214`) against the MP-deletion mutant (`vRNA-ΔM`) cleanly separates MP-independent steps (early perinuclear ER association of vRNA and replication complex formation) from MP-dependent steps (formation of large irregular mid-stage bodies, linear alignment of small puncta along microtubules, and peripheral plasma-membrane targeting/protrusions).
- **Rigorous Hybridization Specificity Controls:** The study includes mock-infected protoplasts, RNase A pre-digestion (which abolished plus-strand signal while partially sparing double-stranded replicative intermediates until heat denaturation), minus-probe controls, and single-channel bleed-through checks.

### 3. WEAKNESSES & METHODOLOGICAL AUDIT (Methodological & Statistical Audit)
- **Absence of Quantitative Colocalization Metrics and Cell-Population Counts:**
  - All colocalization claims between vRNA and BiP, replicase, `MP:GFP`, or microtubules are presented as representative single-cell confocal micrographs without quantitative pixel-level overlap coefficients (e.g., Pearson's correlation or Manders' colocalization coefficients) or systematic scoring of $N$ protoplasts per time point and treatment condition (with the sole exception of noting in Line 106 that protrusions were seen on ~15% of protoplasts at late stages).
- **High-Dose Pharmacological Inhibitor Treatments Lack Viral RNA Accumulation Controls (Figure 9):**
  - Infected protoplasts were treated from `2 to 24 hpi` with high concentrations of `Brefeldin A` (`50 μg/ml`), `cytochalasin D` (`100 μM`), or `oryzalin` (`10 μM`), or for `2 h` late in infection (`16–18 hpi`). While the authors state in Line 216 that *"No significant reduction in the number of viable protoplasts was caused by these drug treatments"* (by visual inspection), they did not perform parallel Northern blots or quantitative RT-PCR on drug-treated protoplasts to verify whether chronic `22-h` exposure to `50 μg/ml` Brefeldin A or `100 μM` cytochalasin D suppressed overall viral RNA replication/translation rather than specifically blocking intracellular transport.
- **Inability to Directly Visualize Intact Actin Microfilaments After ISH:**
  - As candidly noted in Results (Line 196), the proteinase K / fixation regimen required for riboprobe penetration disrupted native actin cables, preventing direct dual-label colocalization of vRNA with intact F-actin structures and forcing reliance on `cytochalasin D` perturbation to infer actin involvement.

### 4. Biological / Experimental Grounding & Claim Proportionality
- **Claim 1:** *TMV plus- and minus-strand RNAs colocalize with the 126/183-kDa viral replicase and the ER marker BiP in perinuclear structures early in infection independently of the viral movement protein.* — `[Well Supported]` by strand-specific FISH, dual-label immunofluorescence (Figures 2, 4, 6), and the `vRNA-ΔM` mutant (Figure 8).
- **Claim 2:** *Functional movement protein (MP) is required to form large irregular mid-stage ER-derived bodies ("viroplasms"), align small vRNA puncta along microtubules, and transport vRNA to peripheral plasma-membrane protrusions.* — `[Well Supported]` by comparison of wild-type TMV vs. `vRNA-ΔM` (Figure 8) and dual-labeling with $\alpha$-tubulin (Figure 7) and `MP:GFP` (Figure 5).
- **Claim 3:** *Intracellular transport of vRNA to the cell periphery requires intact ER/endomembranes and F-actin, whereas microtubules are dispensable for peripheral targeting in single protoplasts.* — `[Moderately Supported]`; supported by `Brefeldin A`, `cytochalasin D`, and `oryzalin` phenotypes (Figure 9), though high inhibitor doses and lack of intact F-actin co-staining warrant caution.

### 5. Reproducibility & Data Completeness
- **Reagents & Constructs:** Plasmid constructs (`pU3/1214`, `pU3/1214-ΔM`, `pT-MfCP`, `pTMV-M:GfusBr`, riboprobe template `pE5-1` covering nt `5897–6395`), antibody sources and dilutions, and protoplast electroporation/infection and FISH/immunofluorescence protocols are described in full detail suitable for replication.
</Blinded Review: TIME_ANON_0555>
