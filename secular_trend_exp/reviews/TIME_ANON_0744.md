<Blinded Review: TIME_ANON_0744>
**Composite Score:** 7.3 / 10.0 (Rigor: 2.4/3.5 | Claims: 1.9/2.5 | Biology: 1.6/2.0 | Reproducibility: 1.4/2.0)
**Scientific Core Score:** 5.9 / 8.0
**Bias Category:** Statistical/Design
**Verdict:** Minor Revision
**Study Modality:** Hybrid Computational + Wet-Lab
**Technology Maturity:** Mature/Classical
**Epistemic Stage:** Basic/Mechanistic Discovery

OVERALL_SCORE: 7.3/10
VERDICT: PASS
ESTIMATED_DECADE: 2020s

---

### 1. Executive Summary (SUMMARY)
This phylogeographic and demographic study investigates the evolutionary history of the East Asian Tertiary relict shrub/tree *Lindera obtusiloba* across 24 populations ($n = 90$ individuals: 45 in Northeast Asia `NEA` and 45 in South/East Asia `SEA`) by sequencing 27 nuclear low-copy genes (`nLCGs`, `13,285 bp` total) and integrating Bayesian clustering (`STRUCTURE`), species-tree divergence dating (`*BEAST`), isolation-with-migration coalescent modeling (`IMa2`), 15-scenario approximate Bayesian computation (`msABC`), ancestral area reconstruction (`BioGeoBEARS`), and ecological niche modeling (`MaxEnt`, `ENMTools`, and partial Mantel isolation-by-environment `IBE` tests). The authors uncover a deep mid-Pleistocene (~600–800 ka) north–south split into reciprocally monophyletic `NEA` and `SEA` lineages with negligible gene flow ($2Nm < 0.02$), 2–3-fold higher genetic diversity and $N_e$ in `SEA` than `NEA`, West–East subclustering within both regions ($K = 4$), and niche divergence along temperature gradients. The authors thoughtfully conclude that none of the three simple origin hypotheses (High-Latitude Origin `HLO`, Low-Latitude Origin `LLO`, or Vicariance `VCO`) alone fully explains the data, favoring long-term dual refugia with asymmetric demographic persistence. Minor limitations include very small within-population sample sizes ($n = 2–6$, modal $n = 3$) for population-level $F_{ST}$ and partial Mantel tests, and minor typographical errors in text/figure labels.

### 2. Methodological & Statistical Audit (STRENGTHS & WEAKNESSES & METHODOLOGICAL AUDIT)
**Strengths:**
- **Multi-Locus Coalescent & ABC Framework:** Upgrading from prior single-locus cpDNA and 6-microsatellite markers to 27 unlinked nuclear coding regions (`13.3 kb`) across 24 populations enables multi-locus coalescent inference in `*BEAST`, `IMa2`, and `msABC` (comparing 6 split and 9 vicariance demographic models with 2,000,000 simulations per model).
- **Balanced, Non-Dogmatic Hypothesis Evaluation:** Rather than forcing a single narrative when different methods highlight different aspects of the history (`msABC` favoring `SEA` [`PP = 0.46`] or `NEA` [`PP = 0.34`] split models with founder bottlenecks, while `*BEAST` and `BioGeoBEARS` show reciprocal monophyly and dual refugia), the authors transparently synthesize the evidence and acknowledge the statistical resolution limits of 13 kb of neutral sequence (`lines 180–186, 202`).
- **Reciprocal Niche Background Tests (`Figure 5b–c`):** Uses `ENMTools` with 1,000 pseudoreplicates sampled from 0.5° dispersal buffer zones rather than simple uncalibrated overlap metrics (`Schoener's D` and `Hellinger's I`) to test niche divergence against regional habitat availability.

**Weaknesses & Minor Flaws:**
- **Very Small Per-Population Sample Sizes ($n = 2$ to $6$) for Population-Level $F_{ST}$ and Partial Mantel `IBE` Tests (`Table 1`, `line 110`):** Although the regional sample sizes are well balanced ($n = 45$ in `SEA`, $n = 45$ in `NEA`) and well suited for regional coalescent analyses (`IMa2`, `msABC`, `*BEAST` on $K=4$ clusters), 15 of the 24 individual populations have only $n = 2$ (`NI`) or $n = 3$ individuals (`Table 1`). Computing population-level pairwise $F_{ST}$ across 24 populations with $n = 2–3$ diploid individuals per population for the partial Mantel `IBE` test (`r = 0.22, P = 0.01`, `line 159`) is subject to high sampling variance; moreover, Mantel and partial Mantel tests are known to exhibit elevated Type I error rates under spatial autocorrelation compared with distance-based redundancy analysis (`dbRDA`) or generalized dissimilarity modeling (`GDM`).
- **Indirect Substitution Rate Calibration (`line 87`):** Because no direct nuclear fossil calibration was used for the `*BEAST` and `IMa2` runs, the nuclear substitution rate ($4.58 \times 10^{-9}$ substitutions/site/year) was scaled from a previously estimated cpDNA rate using a generic 16:3 nuclear-to-cpDNA ratio (`line 87`), propagating wide rate uncertainty (`95% HPD: 1.66–12.69 x 10^-9`).
- **Typographical Errors in Text and Figure Legends:**
  1. In Results (`line 141`), the `IMa2` 95% HPD interval for coalescence time is written as `"798.61 ka (95% HPD: 577.16–96.49 ka)"`, where `96.49 ka` is a typo for **`996.49 ka`** (correctly shown in `Table 3`, `line 150`).
  2. In the `Figure 3` caption (`line 154`), the population size labels are duplicated as `"N_SEA' and N_SEA'"` and `"N_SEA and N_SEA"` instead of `N_SEA'`/`N_NEA'` and `N_SEA`/`N_NEA`.

### 3. Biological / Experimental Grounding & Claim Proportionality
- **Claim 1:** *Lindera obtusiloba is divided into two deeply divergent, reciprocally monophyletic lineages (NEA and SEA) that diverged during the mid-Pleistocene (~600–800 ka) with minimal subsequent gene flow, and further subdivided into West and East subclusters within each region.* `[Well Supported]` — Consistently supported by `STRUCTURE` ($K = 2$ and $K = 4$), `*BEAST` (`PP > 0.95`), pairwise $F_{ST}$ (`0.75–0.79` between regions), and `IMa2` ($2Nm < 0.02$).
- **Claim 2:** *SEA harbors 2–3 times higher genetic diversity and effective population size than NEA, and both regions served as long-term dual refugia.* `[Well Supported]` — Supported by nucleotide diversity (`3.52 vs. 1.96 x 10^-3`), allelic richness (`12.04 vs. 6.06`), `IMa2`/`msABC` $N_e$ estimates, and LGM ecological niche projections (`Figure 4`).
- **Claim 3:** *Populations in NEA and SEA have undergone adaptive ecological divergence driven by temperature (`PC2`).* `[Moderately Supported]` — Niche differentiation (`Figure 5`) is clear, but inferring genetic adaptation from 27 neutral loci via partial Mantel correlation (`r = 0.22, P = 0.01`) is indirect and appropriately caveated by the authors as requiring future genome-wide adaptation scans (`lines 11, 202`).

### 4. Reproducibility & Data Completeness
- **Strengths:** All newly generated nuclear gene sequences are deposited in GenBank (`MF152421–MF152590`), herbarium voucher numbers (`BNU23236–23259`) and exact GPS coordinates for all 24 populations are listed in `Table 1`, and software versions and priors (`BEAST 2.4`, `IMa2`, `msABC`, `BioGeoBEARS 1.1.1`) are thoroughly documented.
- **Weaknesses:** Input alignment files and `msABC` simulation scripts are not hosted in an external repository (referenced as `supporting file 1`).
</Blinded Review: TIME_ANON_0744>
