<Blinded Review: TIME_ANON_0447>
**Composite Score:** 5.6 / 10.0 (Rigor: 1.7/3.5 | Claims: 1.5/2.5 | Biology: 1.4/2.0 | Reproducibility: 1.0/2.0)
**Bias Category:** Algorithmic/Model
**Verdict:** Major Revision
**Study Modality:** Hybrid Computational + Wet-Lab
**Technology Maturity:** Mature/Classical
**Epistemic Stage:** Basic/Mechanistic Discovery

OVERALL_SCORE: 5.6/10
VERDICT: CAVEATS
ESTIMATED_DECADE: 2000s

---

### 1. Executive Summary (SUMMARY)
This phylogeographic study examines 14 extant populations ($N=79\text{--}88$ individuals) of the steppic land snail *Trochoidea geyeri* across France and Germany using mitochondrial 16S rDNA ($\sim 356\text{ bp}$, 31 haplotypes) and nuclear ITS-1 ($525\text{--}527\text{ bp}$, 6 haplotypes) sequences. Combining statistical parsimony (TCS), Templeton's Nested Clade Analysis (NCA), maximum-likelihood coalescent migration estimation (`Migrate 1.2.4`), and divergence dating (Nei's net divergence $d_A$ and `Genetree 8.3`), the authors infer an ancestral origin in Provence, range expansion to the Causse de Larzac and subsequently to Germany, and pre-Last Glacial Maximum divergence of the German clade ($180 \pm 108\text{ ka}$ via Nei's distance; $232 \pm 36.6\text{ ka}$ via `Genetree`), concluding that *T. geyeri* persisted in northern cryptic periglacial refugia during the Pleistocene. While the concordance between mitochondrial 16S and nuclear ITS-1 major clades is informative, the study suffers from over-reliance on single-locus NCA inference keys (known to have high false-positive rates for range expansion vs. fragmentation), an algebraically inverted divergence-time equation in the Methods, missing Table 1 and ESS row in Table 2b, placeholder GenBank accession numbers (`XXXX-XXXX`), and circular parameter chaining across `Fluctuate`, `Migrate`, and `Genetree`.

### 2. Methodological & Statistical Audit (STRENGTHS & WEAKNESSES & METHODOLOGICAL AUDIT)
#### Strengths
* **Comprehensive Geographic Coverage of Extant Range with Dual Markers:** The authors sampled all 14 known extant populations across Provence, Causse de Larzac, and Germany and sequenced both a faster-evolving mitochondrial locus (16S rDNA) and a nuclear locus (ITS-1), demonstrating reciprocal monophyly of the four major 3-step clades across both markers.
* **Explicit Consideration of Ghost/Extinct Source Populations:** In the Discussion (Section "Northern cryptic refugia?", point 2), the authors explicitly evaluate the alternative hypothesis that German populations were colonized postglacially from an extinct population in northeast France or Belgium rather than surviving *in situ* in Germany.

#### Weaknesses & Methodological Audit
* **Algebraic Error in the Divergence Time Equation and Unpropagated Rate Uncertainty:** On line 212, the Methods state that divergence time between clades was computed as:
  $$t = (d_{xy} - 0.5(d_x + d_y)) \times \text{substitution rate}$$
  Dimensionally, net divergence $d_A = d_{xy} - 0.5(d_x + d_y)$ (in substitutions per site) must be **divided** by $(2 \times \mu)$ (or divided by the pairwise divergence rate), not multiplied by the substitution rate. Inspecting Table 4 for clades 3-3 and 3-4: $d_{xy} = 0.016$, $d_x = 0.006$, $d_y = 0.007$, so $d_A = 0.016 - 0.0065 = 0.0095$. Dividing $0.0095$ by the stated rate of $0.056\text{ substitutions/site/Myr}$ yields $0.170\text{ Myr}$ ($\approx 180\text{ ka}$ in Table 4), confirming that the text formula is written upside-down and that the authors treated $0.056$ as a pairwise divergence rate ($2\mu$) here, whereas on line 137/214 they plug $\mu = 0.056$ into $N_e = \theta / (2m\mu)$. Furthermore, the fossil calibration ($3.2 \pm 0.5\text{ Ma}$ from unpublished data) and substitution rate ($0.056 \pm 0.011$) rest on unpublished sequences from *Cernuella* and *Candidula*.
* **Extreme Rate Heterogeneity ($\alpha = 0.0079$) Ignored in Parsimony Network and Infinite-Sites Coalescent Modeling:** The authors report a gamma shape parameter $\alpha = 0.0079$ for 16S rDNA (line 34), indicating extreme site-to-site rate heterogeneity where mutations concentrate at a tiny fraction of hypervariable sites. Yet they apply statistical parsimony (assuming no homoplasy up to 8 steps) and `Genetree` (which strictly requires the infinite-sites model with zero homoplasy).
* **Over-Reliance on Nested Clade Analysis (NCA) and Unchecked `Migrate` Assumptions:** NCA is treated as an "objective statistical analysis" to infer detailed historical scenarios (long-distance colonization of MVR from MVS, STB from Albion, MUN from SHZ in Table 3) from $n=3\text{--}9$ snails per site without independent demographic model testing or coalescent simulations showing that NCA can distinguish these scenarios. In `Migrate`, pooling structured populations (LAR1–3, MVR+MVS) and running a full 11-population migration matrix (110 directional migration parameters plus 11 $\theta$ parameters) on only 37 total variable sites across two loci severely over-parameterizes the likelihood surface.
* **Table Omissions and Internal Inconsistencies:**
  1. **Table 1 is completely missing** from the manuscript despite being cited on lines 82 and 186 for sampling site coordinates and sample sizes.
  2. **Table 2b omits population `ESS`** (which has 5 individuals in Table 2a, haplotype 31, but is missing its row in the ITS-1 subtable, leaving haplotype `n6` with zero entries in Table 2b!).
  3. **Figure 5 is cited on line 167** ("as it should be expected if a recolonisation occurred from the South (Fig. 5)"), but the manuscript only has 4 figures (Figures 1–4).
  4. **Table 3b** reports `$p$-value < 0.000` for Clades nested in 2-2 (mathematically impossible; should be `< 0.001`).

### 3. Biological / Experimental Grounding & Claim Proportionality
* **Claim 1: *T. geyeri* shows deep phylogeographic structure with reciprocal monophyly between Provence, Causse de Larzac, and Germany across mitochondrial and nuclear markers `[Well Supported]`.** Both 16S rDNA and ITS-1 independently recover the same four major regional clades with zero shared haplotypes between regions.
* **Claim 2: The divergence between German and southern French populations predates the Last Glacial Maximum ($17\text{--}25\text{ ka}$), supporting survival in northern periglacial refugia `[Moderately Supported]`.** Even accounting for clock calibration uncertainty and a 2-fold factor between lineage substitution rate and pairwise divergence rate, the net sequence divergence ($d_A \approx 1.0\%$) and nuclear ITS-1 sorting strongly argue against a post-Holocene ($<10\text{ ka}$) colonization from extant southern populations.
* **Claim 3: Fine-scale directional colonization routes among individual peaks and plateaus inferred by NCA and `Migrate` `[Overstated]`.** Inferring specific point-to-point colonizations (e.g., SHZ $\to$ MUN, MVS $\to$ MVR) from $n=5\text{--}9$ individuals per site and an over-parameterized 11-population `Migrate` run exceeds the information content of two short ribosomal fragments.

### 4. Reproducibility & Data Completeness
* **Placeholder Accession Numbers:** Line 191 states "Sequences were deposited in GenBank (Accession nos. XXXX-XXXX)," leaving the raw sequences unretrievable by accession ID.
* **Missing Table 1 and Truncated Table 2b:** The omission of Table 1 (locality coordinates and sample sizes) and the missing `ESS` row in Table 2b (where haplotype `n6` should appear) directly impair data completeness.
</Blinded Review: TIME_ANON_0447>
