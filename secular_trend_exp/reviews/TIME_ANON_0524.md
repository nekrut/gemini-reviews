<Blinded Review: TIME_ANON_0524>
**Composite Score:** 4.6 / 10.0 (Rigor: 1.4/3.5 | Claims: 1.1/2.5 | Biology: 1.2/2.0 | Reproducibility: 0.9/2.0)
**Bias Category:** Algorithmic/Model
**Verdict:** Major Revision
**Study Modality:** Hybrid Computational + Wet-Lab
**Technology Maturity:** Mature/Classical
**Epistemic Stage:** Basic/Mechanistic Discovery

OVERALL_SCORE: 4.6/10
VERDICT: CAVEATS
ESTIMATED_DECADE: 2000s

---

### 1. Executive Summary / SUMMARY
This molecular evolution and comparative genomics study sequences the complete `16,498-bp` mitochondrial genome of a single Tibetan antelope (*Pantholops hodgsonii*) sampled from Qinghai Province, China, and performs phylogenetic, molecular clock, control-region tandem repeat, and codon-based selection analyses across pecoran ruminants. Using a 1,140-bp *cytochrome b* (*cytb*) dataset across 27 Caprinae/bovid taxa, neighbor-joining (NJ) phylogeny places *P. hodgsonii* as a sister lineage to Caprinae with an estimated divergence time of `2.25 Mya` based on a fixed *cytb* evolutionary rate (`0.056` per site per Myr). Furthermore, the authors run `PAML` (`codeml`) free-ratio branch models on 8 mitochondrial protein-coding genes (`>1,000 bp`: `ND1`, `ND2`, `ND4`, `ND5`, `COXI`, `COXII`, `COXIII`, `CYTB`) across 7 species (including two native Tibetan plateau mammals, *P. hodgsonii* and yak *Bos grunniens*, plus 5 lowland species: *Bos taurus*, *Ovis aries*, *Bubalus bubalis*, *Capra hircus*, and *Muntiacus reevesi*) and claim that `COXI` underwent adaptive positive selection for high-altitude hypoxia in *P. hodgsonii* and *B. grunniens*. However, the positive selection inference rests on a fundamental statistical-genetics misinterpretation of `codeml` free-ratio branch tests (confounding minor differences in purifying selection `N/S` ratios with positive Darwinian selection `ω > 1`), all figures and tables (`Figures 1–4`, `Tables 1–4`) are missing from the manuscript body, and no GenBank accession number is provided for the newly sequenced mitogenome.

### 2. STRENGTHS
- **Complete Mitochondrial Genome Sequencing of a High-Altitude Endemic Ruminant:** Sequencing the full `16,498-bp` circular mitogenome of *P. hodgsonii* (`13` protein-coding genes, `2` rRNAs, `22` tRNAs, and `1,069-bp` D-loop control region) provides a useful genomic resource for Caprinae systematics.
- **Comparative Control-Region Repeat Characterization:** Identifying the two `75-bp` tandem repeat units (`RS1` and `RS2`) in the 5' left domain of the *P. hodgsonii* control region and comparing their secondary structure stability across 9 pecoran species provides descriptive insight into ruminant D-loop evolution.

### 3. Methodological & Statistical Audit / WEAKNESSES & METHODOLOGICAL AUDIT
- **Fundamental Misuse of `PAML` Free-Ratio Branch Models and Fisher's Exact Test to Claim Positive Selection:** In Results (Lines 52–59) and Discussion (Lines 86–93), the authors run the `codeml` free-ratio model (`model = 1`) vs. the one-ratio model (`model = 0`) and apply Fisher's exact test to the inferred counts of nonsynonymous (`N`) and synonymous (`S`) changes (`N/S` values) between branches, claiming that *"COXI was found to have rapidly evolved, indicating that positive selection played an important role in the evolution of this gene"* (`p < 0.001`) in *P. hodgsonii* and *B. grunniens*. This is methodologically flawed on multiple levels:
  1. Rejection of the one-ratio model in favor of the free-ratio model (`2ΔL` LRT) only tests whether `ω` (`dN/dS`) is constant across all branches; it does *not* test for positive selection (`ω > 1`).
  2. In mammalian mitochondrial protein-coding genes (especially `COXI`), purifying selection is overwhelmingly strong (`ω` is typically `0.005–0.05`). A statistically higher `N/S` ratio on one terminal branch compared to another via Fisher's exact test (`p < 0.001`) does *not* imply `dN/dS > 1` (positive selection); it just as easily reflects relaxed purifying selection (e.g., demographic bottlenecks / reduced effective population size `Ne` in high-altitude endemics accumulating slightly deleterious mutations) or stochastic variance in small substitution counts.
  3. The authors never report the actual `dN/dS` (`ω`) values, nor do they perform a legitimate branch-site likelihood ratio test (`Model A` vs. `Model A null` with `ω2 = 1` fixed) to test whether any sites have `ω > 1`. In fact, the text admits (Line 59) that *"there are only three unique amino acid changes when compared with five other low-altitude ruminants"* in *P. hodgsonii* `COXI`.
- **Naive Single-Gene Molecular Clock Dating Without Calibration Uncertainty:** The divergence time (`2.25 Mya`) between *P. hodgsonii* and *Ovis aries* is calculated by dividing pairwise `HKY + I + G` genetic distance at a single locus (*cytb*) by a hardcoded literature constant (`0.056` per site per Myr) without fossil calibration priors, relaxed-clock modeling, or confidence/credibility intervals.
- **Omission of All Referenced Tables and Figures (`Figures 1–4`, `Tables 1–4`):** The manuscript text repeatedly cites `Figure 1–4` and `Table 1–4` (primers, genome organization, control region repeats, and `N/S` ratios), none of which are present in the document.

### 4. Biological / Experimental Grounding & Claim Proportionality
- **Claim 1:** The *P. hodgsonii* mitochondrial genome is `16,498 bp` long with conserved ruminant gene order and two `75-bp` tandem repeats in the control region. `[Well Supported]` — Standard mitogenome annotation and repeat identification (` tandem repeats finder v4.0`).
- **Claim 2:** *P. hodgsonii* is a sister taxon to Caprinae that diverged ~`2.25 Mya`. `[Moderately Supported]` — Sister placement to Caprinae is consistent with prior phylogenies, though single-locus *cytb* NJ dating without fossil calibration CIs is methodologically weak when the whole mitogenome was available.
- **Claim 3:** `COXI` evolved under positive selection in *P. hodgsonii* and *B. grunniens* as an adaptation to high-altitude hypoxia. `[Methodologically Flawed]` — Inferring positive selection from branch-to-branch differences in `N/S` counts without demonstrating `ω > 1` (or ruling out relaxed purifying selection and demographic history) is invalid, and no biochemical or structural evidence links the 3 amino acid differences in `COXI` to cytochrome *c* oxidase kinetics.

### 5. Reproducibility & Data Completeness
- **Missing GenBank Accession Number for the Focal Sequence:** While GenBank accessions are listed in Methods (Lines 35–39) for the 6 comparative species (`AY676873`, `NC_006853`, `AF010406`, `AY126697`, `NC_005044`, `AF527537`), no GenBank accession number is provided for the newly sequenced *P. hodgsonii* mitochondrial genome itself.
- **Missing Tables:** `Table 1` (primers) and `Tables 2–4` (annotations and `codeml` outputs) are absent from the manuscript text.
</Blinded Review: TIME_ANON_0524>
