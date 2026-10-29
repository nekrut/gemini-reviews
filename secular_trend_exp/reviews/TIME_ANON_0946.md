<Blinded Review: TIME_ANON_0946>
**Composite Score:** 8.5 / 10.0 (Rigor: 3.1/3.5 | Claims: 2.2/2.5 | Biology: 1.6/2.0 | Reproducibility: 1.6/2.0)
**Bias Category:** None (Methodologically Sound)
**Verdict:** Minor Revision
**Study Modality:** Hybrid Computational + Wet-Lab
**Technology Maturity:** Mid-Stage High-Throughput
**Epistemic Stage:** Basic/Mechanistic Discovery

OVERALL_SCORE: 8.5/10
VERDICT: PASS
ESTIMATED_DECADE: 2000s

---

### 1. Executive Summary / SUMMARY
This landmark population genetics study re-evaluates the widely cited hypothesis that the HIV-resistance allele `CCR5-Δ32` arose within the past ~700 years (range 275–1,875 y) in Europe and swept to 5%–14% frequency via strong recent positive selection (e.g., medieval plague or smallpox). The authors genotype `CCR5-Δ32`, two flanking microsatellites, and 70 SNPs spanning 837 kbp centromere-distal and 430 kbp centromere-proximal across 340 independent parent chromosomes from European-American (12 multigenerational CEPH/Coriell pedigrees, yielding 8 `Δ32` chromosomes), Yoruba (31 trios), and Han Chinese (30 trios) samples, augmented by 12 `Δ32/Δ32` homozygotes (24 additional `Δ32` chromosomes; 32 total). Comparing `CCR5` against two large empirical benchmarks—2,359 SNPs across 168 immunologic genes in the same 340 chromosomes and 63,149 SNPs on Chromosome 3 from HapMap Release 16—plus 1,000 coalescent neutral and partial-sweep simulations of 1-Mbp regions in 400 European-American chromosomes, the authors demonstrate three crucial methodological insights:
1. **Core Haplotype Disaggregation:** Collapsing all non-`Δ32` chromosomes into a single heterogeneous "super-haplotype" artificially inflates the relative extended haplotype homozygosity (`REHH`) of `Δ32` (5.96 distal, 20.22 proximal). When core variation at `CCR5` is resolved using 7 intragenic SNPs into 5 distinct core haplotypes, the distal `REHH` of `Δ32` drops to 1.92 (lower than two wild-type haplotypes at 6.77 and 3.29) and proximal `REHH` drops to 7.26.
2. **Empirical & Simulated Null Calibration:** Compared against frequency-matched (6%–10%) haplotypes in HapMap Chr 3 and 1,000 neutral coalescent simulations ($n=5,915$ matched haplotypes), neither `EHH` ($p = 0.49$ distal, $p = 0.15$ proximal), `REHH`, nor extended haplotype length (`EHL` = 0.470 cM; 88th percentile in HapMap, 64th percentile in neutral simulations) is statistically exceptional.
3. **Genetic Map Correction for Allele Age:** Re-mapping the two original microsatellites onto the revised Kong/deCODE genetic map reveals that their genetic separation is 0.18 cM (flanking `CCR5`) rather than 0.91 cM (both distal), increasing the microsatellite-based age estimate from 688 y to 7,000 y (95% CI: 2,900–15,750 y) and the 32-SNP age estimate to 5,075 y (95% CI: 3,150–7,800 y), consistent with ancient DNA detection in ~3,000-year-old European burials.

### 2. Methodological & Statistical Audit / STRENGTHS & WEAKNESSES & METHODOLOGICAL AUDIT

#### STRENGTHS
- **Identification of the Biallelic Collapsing Artifact in Long-Range Haplotype Tests (Fig. 2):** The demonstration that testing a single derived allele against the union of all ancestral haplotypes creates a spurious `REHH` signal—because multiple distinct wild-type backgrounds cancel out each other's homozygosity when pooled—is a major methodological contribution to statistical genetics.
- **Tri-Level Calibration (Pedigree Phasing, Empirical Genome Controls, Ascertainment-Matched Coalescent Simulations):** Unambiguous family trio/pedigree phasing (`Genehunter` + `PHASE`), empirical comparison against 168 immune genes and HapMap Chr 3, and explicit power simulations (showing 69% power at 400 chromosomes vs 30% at 120 chromosomes for a 700-year-old sweep to 8% frequency) make the statistical inference exceptionally rigorous.
- **Balanced Epistemic Framing:** The authors carefully state that compatibility with neutral coalescent expectations does not prove the absence of selection at `CCR5`, only that long-range LD, $F_{ST}$, heterozygosity, and derived allele frequency (DAF) do not reject neutrality or support a medieval (<1,000 y) origin.

#### WEAKNESSES & METHODOLOGICAL AUDIT
- **Ascertainment Bias in SNP Selection:** As the authors candidly acknowledge, selecting "double-hit" common SNPs from dbSNP/SNP Consortium biases the marker panel toward older shared polymorphisms, reducing sensitivity of site-frequency-spectrum statistics (heterozygosity, DAF, $F_{ST}$) compared to full resequencing.
- **Pooling Population-Ascertained `Δ32/Δ32` Homozygotes with Random Pedigree Chromosomes:** To boost the sample size of `Δ32` chromosomes from 8 (in the random European-American pedigrees) to 32, the authors added 24 chromosomes from 12 `Δ32/Δ32` individuals from the prior study. While they report running analyses on both datasets (`Table S2`) and matching the 32/400 frequency (8%) in simulations, combining selectively ascertained homozygotes with random chromosomes slightly alters the effective sample size of the non-`Δ32` background.

### 3. Biological / Experimental Grounding & Claim Proportionality
- **Claim 1:** Disaggregating the non-`Δ32` class into its 5 constituent core haplotypes eliminates the apparent centromere-distal `REHH` outlier signal and substantially reduces the centromere-proximal `REHH` signal at `CCR5`. `[Well Supported]`
- **Claim 2:** Using updated genetic maps (0.18 cM vs 0.91 cM microsatellite interval) and 32 flanking SNPs increases the estimated age of `CCR5-Δ32` from ~700 years to >5,000 years (5,075 y; 95% CI: 3,150–7,800 y). `[Well Supported]`
- **Claim 3:** The pattern of genetic variation and LD around `CCR5-Δ32` does not stand out relative to empirical genome-wide controls or neutral coalescent simulations. `[Well Supported]`

### 4. Reproducibility & Data Completeness
- **Mathematical & Algorithmic Clarity:** Explicit equations for Nei's heterozygosity, `EHH`, $\widetilde{\text{EHH}}$, `REHH`, and `all EHH` (marker breakdown) are provided, alongside `Genehunter`, `PHASE`, and `Sweep` software descriptions and complete SNP/haplotype tables (`Tables S1–S5`).
</Blinded Review: TIME_ANON_0946>
