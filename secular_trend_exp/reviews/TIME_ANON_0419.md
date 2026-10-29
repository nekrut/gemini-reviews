<Blinded Review: TIME_ANON_0419>
**Composite Score:** 8.2 / 10.0 (Rigor: 2.9/3.5 | Claims: 2.2/2.5 | Biology: 1.6/2.0 | Reproducibility: 1.5/2.0)
**Bias Category:** None (Methodologically Sound)
**Verdict:** Minor Revision
**Study Modality:** Hybrid Computational + Wet-Lab
**Technology Maturity:** Mid-Stage High-Throughput
**Epistemic Stage:** Basic/Mechanistic Discovery

OVERALL_SCORE: 8.2/10
VERDICT: PASS
ESTIMATED_DECADE: 2000s

---

### 1. Executive Summary (SUMMARY)
This quantitative genetics study revisits the genetic architecture of 40 generations of bidirectional selection for 56-day juvenile body weight in the Virginia Tech High-Weight (HWS, $1522 \pm 36\text{ g}$) and Low-Weight (LWS, $181 \pm 5.4\text{ g}$) White Plymouth Rock chicken lines using an $F_2$ intercross ($n = 874$ hatched, $n = 795$ at day 56). By upgrading the previous sparse microsatellite map to a combined 434-marker linkage map (316 Illumina GoldenGate SNPs + 118 microsatellites spanning 2954 cM across 28 autosomes and 1 linkage group, covering ~93% of the physical assembly), the authors perform 1D Haley-Knott interval mapping (`QTLExpress`), 2D genome-wide epistatic interaction scans, and a selective sweep scan using 11,275 working SNPs (4,777 polymorphic) in 15 HWS and 13 LWS parental birds. They confirm that marginal single-locus QTL effects are small (1.5–4.4% of $F_2$ residual variance), reinforce the central hub role of `Growth9` on chromosome 7 in a multi-locus epistatic network (9 of 15 unique epistatic pairs involve `Growth9`, accounting for a 314 g difference when combined with `Growth4`, `Growth6`, and `Growth12`), and show that $F_{ST}$ and homozygosity within QTL intervals barely exceed the genome-wide background ($F_{ST} = 0.38$ vs. $0.33$) except at `Growth1` on Chr 1 ($3.5\text{ Mb}$ sweep fixed in LWS), indicating selection acted primarily on standing epistatic variation.

### 2. Methodological & Statistical Audit (WEAKNESSES & METHODOLOGICAL AUDIT)
- **Model Specification Sensitivity (Omission of Full-Sib Family Fixed Effect):** Unlike their earlier marginal QTL analyses (`Park et al.` and `Jacobsson et al.`), the authors omitted $F_2$ full-sib family (75 families) as a fixed effect in the primary scan, resulting in the loss of 6 previously reported QTLs (`Growth2`, `3`, `8`, `10`, `11`, `13`). Commendably, in the Discussion they explicitly re-run the model *with* family included as a fixed effect and demonstrate that `Growth2` ($F: 5.4 \to 6.3$), `Growth3` ($F: 4.5 \to 6.0$), and `Growth8` ($F: <6.0 \to 9.3$, genome-wide significant) are recovered when accounting for between-family variance, whereas `Growth10`, `11`, and `13` remain non-significant (likely false positives in the original map). However, absorbing family variance into the residual in the primary scan demonstrably reduced statistical power for main effects.
- **Internal Nomenclature Typo in Discussion:** In the first paragraph of the Discussion (line 216), the text states: `"Only five loci, Growth1, 4, 6, 9 and 10, reached genome-wide significance for at least one body-weight or growth trait (Table 3)."`. Looking at Table 3, the five genome-wide significant (`*`) loci are `Growth1`, `Growth4`, `Growth6`, `Growth9`, and **`Growth12`** (on Chr 20)—not `Growth10` (which is absent from Table 3 and later listed among the non-replicated loci).
- **Epistatic Network Conditioning and Multiple Testing:** Permutation thresholds for both 1D scans ($F > 9$ for 5% genome-wide, $F > 6$ for suggestive) and 2D epistatic scans (5% joint randomization + 1% epistatic parameter randomization test) are rigorously implemented. Filtering $F_2$ birds for genotype probability $>0.70$ across all 4 network loci ($n=727/795$ retained) avoids regression dilution when visualizing the 314 g conditional effect in Figure 4.

### 3. Biological / Experimental Grounding & Claim Proportionality (STRENGTHS)
- `[Well Supported]` Demonstration that replacing error-prone microsatellites with GoldenGate SNPs contracts inflated linkage map lengths to 2954 cM while sharpening the `Growth9` peak on chromosome 7.
- `[Well Supported]` Validation of strong genetic background dependence (capacitation/epistasis): `Growth4`, `Growth6`, and `Growth12` HWS alleles produce zero additive weight gain in `Growth9` `LL` or `HL` backgrounds, but yield a $+314\text{ g}$ gain in the `Growth9` `HH` background.
- `[Well Supported]` Population genetic inference from the 13k SNP panel that 40 generations of intense divergent selection from a 7-way cross founder population primarily shifted standing variation on short haplotype blocks (mean 1 polymorphic SNP per 210 kb is too sparse to capture narrow standing-variation sweeps), with a single clear $3.5\text{ Mb}$ selective sweep (`173.4–176.9 Mb` on Chr 1, `Growth1`) reaching 98% homozygosity in LWS.

### 4. Reproducibility & Data Completeness
Map distances (Kosambi cM) and physical coordinates (Mb) for all 434 markers are provided in Additional File 1, and all 25 significant two-locus genotype-phenotype interaction surfaces are provided in Additional File 2. Phenotypic sample sizes, means, SDs, and ranges across all 10 traits are complete in Table 1.
</Blinded Review: TIME_ANON_0419>
