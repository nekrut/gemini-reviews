<Blinded Review: TIME_ANON_0661>
**Composite Score:** 7.6 / 10.0 (Rigor: 2.6/3.5 | Claims: 2.0/2.5 | Biology: 1.6/2.0 | Reproducibility: 1.4/2.0)
**Bias Category:** Statistical/Design
**Verdict:** Minor Revision
**Study Modality:** Hybrid Computational + Wet-Lab
**Technology Maturity:** Mid-Stage High-Throughput
**Epistemic Stage:** Translational/Preclinical/Biomarker

OVERALL_SCORE: 7.6/10
VERDICT: PASS
ESTIMATED_DECADE: 2010s

---

### 1. Executive Summary / SUMMARY
This study investigates candidate genes underlying maturity-corrected quantitative resistance (MCR) to *Phytophthora infestans* (late blight) in tetraploid potato (*Solanum tuberosum* L.). Building on a prior SuperSAGE transcriptomic screen that identified ~720 differentially expressed genes across bulked pools, the authors select 22 candidate genes and evaluate: (1) expression reproducibility via qRT-PCR (14 genes) and allele-specific pyrosequencing (8 genes) across 4 sets of RNA pools derived from 24 half-sib genotypes over 3 independent infection experiments; (2) association mapping of 131 SNPs across 11 candidate loci in an independent panel of 184 tetraploid cultivars (PIN184) using a Q+K mixed linear model (MLM); and (3) linkage analysis in two tetraploid half-sib families ($n=111$, SL1 and SL2). They validate reproducible expression patterns (>60% consistency) in 13 of 22 candidates, identify 9 SNPs in 7 genes associated with MCR or rAUDPC at $p < 0.01$ in PIN184, and identify 13 SNPs in 4 genes (notably *AspS* explaining up to 37% variance) linked to resistance in the half-sib families without pleiotropic linkage to plant maturity.

### 2. Methodological & Statistical Audit / WEAKNESSES & METHODOLOGICAL AUDIT
- **Multiple Testing in Association and Linkage Mapping:** The authors test 131 amplicon SNPs + 9 pyrosequencing SNPs across 3 traits (MCR, rAUDPC, PM) in PIN184 and 127 SNPs in the SL1+SL2 linkage families using an unadjusted nominal significance threshold of $p < 0.01$ (while applying Storey's $q$-value only to the pairwise LD $\chi^2$ tests). Under 140 SNPs, a nominal $p < 0.01$ threshold expects ~1.4 false positives per trait by chance; while *BCCP_SNP1381* ($p = 4.78 \times 10^{-5}$) and the *AspS* linkage markers ($p = 2.95 \times 10^{-8}$) easily survive Bonferroni/FDR correction, weaker associations such as *HPR_SNP4438* ($p = 0.0054$) and *Chp_SNP4844* ($p = 0.0055$) are marginal.
- **Circularity / Partial Overlap in RNA Pool Validation:** Eight of the 24 SL genotypes used to construct validation Pools_1–4 were previously included in the discovery SuperSAGE pools (A1, A2, B2). Thus, the expression validation in the SL pools is not fully independent of the discovery cohort, though testing across 3 new independent infection experiments and 4 distinct pooling criteria (field MCR, qRT-PCR pathogen biomass, growth chamber AUDPC, and *StAOS2* haplotype) mitigates technical noise.
- **Qualitative Sign-Test Definition of Reproducibility:** Expression "percent reproducibility" in Tables 3 and 4 is defined simply as the proportion of 18 or 36 pairwise R vs. S pool comparisons sharing the same directional sign as SuperSAGE, without formal mixed-effect ANOVA modeling of Pool $\times$ Timepoint $\times$ Experiment interactions.
- **Internal Table Audit:**
  - In Table 5, the allele frequency for `CCAP_SNP9879` is reported as `96/6`, which sums to 102% (a typographical error for `94/6` or `96/4`).
  - In Table 6, combined linkage ANOVA is performed across SL1 ($n=76$, Phy20 $\times$ Phy14) and SL2 ($n=35$, Phy20 $\times$ Phy16) without explicitly including a family main effect or interaction term in `lm(Trait ~ SNP_dosage)`, which can confound family-mean differences with marker dosage if allele frequencies differ between Phy14 and Phy16.

### 3. Biological / Experimental Grounding & Claim Proportionality / STRENGTHS
- **STRENGTHS:**
  - Thoughtful integration of transcriptomics (SuperSAGE), allele-specific pyrosequencing, tetraploid SNP dosage calling, Q+K association mapping (controlling for population structure with 241 SolCAP SNPs and SPAGeDi kinship), and biparental linkage mapping.
  - Crucial biological control for plant maturity (PM): by explicitly testing both MCR and PM, the authors demonstrate that the identified resistance-associated SNPs in *BCCP*, *DSD*, *PME*, *MPP*, *ACRE20*, and *AspS* do not associate with late maturity.
  - Insightful demonstration via genomic vs. cDNA pyrosequencing (Figures 5–6) that apparent "allele-specific expression" in bulked pools is largely driven by underlying genomic allele dosage differences between R and S pools rather than cis-regulatory imbalance alone.
- **Claim Evaluation:**
  - *Claim that 13 of 22 candidate genes show reproducible differential expression between R and S pools:* `[Well Supported]` — Supported across 3 biological replicate infection experiments and multiple resistance metrics.
  - *Claim that SNPs in BCCP, DSD, PME, MPP, and ACRE20 are associated with MCR in tetraploid cultivars:* `[Moderately Supported]` — Controlled for Q+K in $n=184$ cultivars, though nominal $p < 0.01$ is permissive for several loci except *BCCP* and *PME*.
  - *Claim that rare alleles at the AspS locus tag a major MCR QTL in the SL families:* `[Well Supported]` — Strong statistical support ($p \sim 10^{-8}$, $R^2 = 27\text{--}37\%$), with candid discussion that LD in F1 families cannot distinguish causal variation in *AspS* from a tightly linked gene.

### 4. Reproducibility & Data Completeness
- Good reporting of potato genome reference version (PGSC v4.03), locus IDs (Table 2), tag sequences, and experimental parameters. Primer sequences, trace genotypes, and numerical expression matrices are referenced in Supplemental Files S1–S8.
</Blinded Review: TIME_ANON_0661>
