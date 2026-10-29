<Blinded Review: TIME_ANON_0942>
**Composite Score:** 5.6 / 10.0 (Rigor: 1.8/3.5 | Claims: 1.4/2.5 | Biology: 1.3/2.0 | Reproducibility: 1.1/2.0)
**Bias Category:** Statistical/Design
**Verdict:** Major Revision
**Study Modality:** Hybrid Computational + Wet-Lab
**Technology Maturity:** Mature/Classical
**Epistemic Stage:** Basic/Mechanistic Discovery

OVERALL_SCORE: 5.6/10
VERDICT: CAVEATS
ESTIMATED_DECADE: 2000s

---

### 1. Executive Summary / SUMMARY
This study investigates mitochondrial DNA (mtDNA) variation and subspecies systematics in the endangered spur-thighed tortoise (*Testudo graeca*) by sequencing a 394-nt fragment of the mitochondrial 12S rRNA gene across 158 specimens and a 411-nt fragment of the mitochondrial D-loop in a subset of 22 individuals. Using Kimura 2-parameter Neighbor-Joining (NJ, 500 bootstraps) and Maximum Likelihood (`DNAML` v3.5c with fixed Ti/Tv = 2.0) on the concatenated 805-nt alignment, the authors resolve two primary mtDNA clades: a North African clade (*T. g. graeca* and *T. g. whitei*, haplotypes `Tg1`–`Tg5`) and a Middle Eastern/Turkish/Balkan clade (*T. g. terrestris* and *T. g. ibera*, haplotypes `Tg6`–`Tg7`), separated by an average $p$-distance of 0.014 (0.011 subst/site in 12S; 0.017 subst/site in D-loop). Despite acknowledging the absence of nuclear markers and widespread unknown geographic provenance among captive samples, the authors conclude by proposing to elevate *T. g. graeca* and *T. g. ibera* to full species status (*T. graeca* and *T. ibera*).

### 2. Methodological & Statistical Audit / STRENGTHS & WEAKNESSES & METHODOLOGICAL AUDIT

#### STRENGTHS
- **Non-Invasive Sampling Across Broad Haplogroups:** Oral mucosal swabbing of 158 tortoises yielded clean bidirectional Sanger sequences across 14 12S haplotypes and 13 D-loop haplotypes, establishing a clear matrilineal split between North African and Eastern Mediterranean lineages.
- **Transparent Reporting of Variable Sites:** Tables 1–3 explicitly list the exact nucleotide states at all polymorphic positions across all 12S and D-loop haplotypes.

#### WEAKNESSES & METHODOLOGICAL AUDIT
- **Internal Contradictions in Variable Site Counts and Haplotype Naming (Tables 1–3 vs Text):**
  1. Line 30 states: *"The 12S rRNA fragment amplified was 393–394 nucleotides in length... and 10 positions were variable (including a single nt deletion in one individual)."* However, Table 1 lists **13** nucleotide position columns (`15, 27, 85, 183, 194, 216, 219, 224, 244, 253, 326, 328, 339`), of which 12 are variable across `Tg1.0`–`Tg7.0` and position `216` has `G` in `Tg4.1/4.2` and `A` elsewhere! Thus the text count of "10 positions were variable" directly contradicts Table 1.
  2. In Table 3 (line 86), specimen `TGLM1` is listed as having 12S haplotype `Tg5.1`, which does not exist in Table 1 or Table 2 (only `Tg5.0` exists).
- **Severe Provenance Confounding (Captive Pet/Zoo Animals of Unknown Origin):** In Table 2, the majority of haplotypes (`Tg1.0`, `Tg2.0`, `Tg3.0`, `Tg3.1`, `Tg4.1`, `Tg4.2`, `Tg4.3`, `Tg5.0`, `Tg6.0`, `Tg6.1`, `Tg7.0`) include animals of `"Unknown"` provenance from zoos and private tortoise societies. Crucially, the entire `Tg3.0`/`Tg3.1` subclade ($n=6$), `Tg4.1` ($n=5$), `Tg4.3` ($n=1$), `Tg6.1` ($n=1$), and the sole `Tg7.0` individual sequenced for the D-loop (`703837` in Table 3) have unknown geographic origins (`?`). Inferring phylogeography and subspecies validity when key clades consist entirely of captive pets of unknown origin is a major design flaw.
- **Circular Molecular Clock Calibration:** In the "Dating of mitochondrial DNA lineages" section (line 123), the authors assume that *T. g. graeca* and *T. g. ibera* diverged in the middle Pleistocene ($\sim 1.0$–$1.8$ mya) to calculate a substitution rate of $0.6\%$–$1.1\%$ per Myr for 12S, and Simultaneously use mtDNA distances in the Abstract and Conclusion to claim *"a calculated divergence time in the early or middle Pleistocene"*. One cannot both assume a divergence time to calibrate the rate and claim to have calculated the divergence time from the same data without an independent calibration point.
- **Taxonomic Overreach from a Single Maternally Inherited Locus:** Proposing to elevate *T. g. graeca* and *T. g. ibera* to full species status (*T. graeca* and *T. ibera*) based on a 1.1% 12S / 1.7% D-loop divergence ($p$-distance = 0.014) in a single non-recombining locus—where only *one* *T. g. ibera* specimen (`703837`, of unknown geographic origin!) was included in the 805-nt concatenated D-loop+12S tree—is taxonomically premature.

### 3. Biological / Experimental Grounding & Claim Proportionality
- **Claim 1:** *Testudo graeca* mtDNA haplotypes split into two main maternal clades corresponding to North Africa (`Tg1`–`Tg5`) and the Eastern Mediterranean/Middle East (`Tg6`–`Tg7`). `[Well Supported]`
- **Claim 2:** Divergence between *T. g. graeca* and *T. g. ibera* occurred at a calculated time in the early or middle Pleistocene. `[Fragile]` — Relies on uncalibrated/circular substitution rate assumptions ($0.4\%$–$1.7\%$/Myr).
- **Claim 3:** *T. g. graeca* and *T. g. ibera* should be elevated to full species status (*T. graeca* and *T. ibera*), while most of the 15 proposed subspecies lack genetic support. `[Overstated]` — Only one `Tg7.0` (*T. g. ibera*) specimen of unknown origin was sequenced for the D-loop, many putative subspecies were not sampled in the wild across their type localities, and nuclear gene flow/introgression was not tested.

### 4. Reproducibility & Data Completeness
- **Sequences & Primers:** Primers (`12S-L01091`/`12S-H01478` and `myt001`/`myt003`) and variable sites (Tables 1 and 3) are provided in the text, and alignments are referenced as Supplementary Additional File 1, though GenBank accession numbers for the newly generated *T. graeca* sequences are not provided.
- **Phylogenetic Parameters:** Software versions (`MEGA`, `BioEdit` v4.7.8, `DNAML` v3.5c) and parameters (K2P, 500 NJ bootstraps, ML Ti/Tv = 2.0, no ML bootstraps) are clearly stated.
</Blinded Review: TIME_ANON_0942>
