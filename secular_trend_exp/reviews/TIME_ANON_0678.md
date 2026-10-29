<Blinded Review: TIME_ANON_0678>
**Composite Score:** 8.1 / 10.0 (Rigor: 2.7/3.5 | Claims: 2.2/2.5 | Biology: 1.7/2.0 | Reproducibility: 1.5/2.0)
**Bias Category:** None (Methodologically Sound)
**Verdict:** Minor Revision
**Study Modality:** Hybrid Computational + Wet-Lab
**Technology Maturity:** Mid-Stage High-Throughput
**Epistemic Stage:** Translational/Preclinical/Biomarker

OVERALL_SCORE: 8.1/10
VERDICT: PASS
ESTIMATED_DECADE: 2010s

---

### 1. Executive Summary / SUMMARY
This quantitative genetics and genomic mapping study estimates the heritability of host resistance (binary survival) to Salmonid Alphavirus 3 (SAV3, the causative agent of Pancreas Disease) and maps quantitative trait loci (QTL) across two large, independent commercial Atlantic salmon (*Salmo salar*) breeding cohorts: `POP 1` ($n=5,558$ freshwater fry from 218 full-sib / 83 paternal half-sib families exposed via a waterborne cohabitation/shedder bath challenge; overall mortality $75\%$) and `POP 2` ($n=4,946$ PIT-tagged seawater post-smolts from 284 full-sib / 120 paternal half-sib families challenged via intraperitoneal injection; overall mortality $70\%$). Pedigree-based animal and sire-dam generalized linear mixed models (`ASReml`) reveal moderate-to-high heritability for survival in both environments (observed binary scale $h^2 = 0.34$ and liability scale $h^2 \approx 0.50$ in `POP 1`; observed $h^2 = 0.23\text{--}0.26$ and liability $h^2 \approx 0.40$ in `POP 2`). A two-stage microsatellite/SNP linkage scan in `POP 1` ($n=1,273$ offspring) followed by a genome-wide 6K Illumina SNP array linkage scan and `GRAMMAS` (`GenABEL`) family-adjusted GWAS in `POP 2` ($n=1,182$ offspring, 4,178 informative SNPs) independently discover and replicate a major QTL on the distal end of Chromosome 3 (linkage group 12, explaining $5.4\%$ of within-family survival variance in `POP 1` and up to $22.9\%$ in `POP 2`, with two genome-wide significant SNPs `ESTV_18493_1052` and `ESTNV_29410_233` at $p_{\text{adj}} < 0.01$). Replicating the exact same QTL across two distinct populations, life stages (freshwater fry vs. seawater post-smolts), and infection routes (cohabitation vs. IP injection) provides strong validation for marker-assisted selection.

### 2. Methodological & Statistical Audit / WEAKNESSES & METHODOLOGICAL AUDIT
- **Asymmetric Genotyping Platforms for Parentage Assignment Between Survivors and Mortalities in `POP 1`:**
  - Because `POP 1` fry were too small ($2.9\text{ g}$) to be individually PIT-tagged prior to communal challenge, parentage assignment was performed post-challenge using DNA molecular markers (Line 216). However, the authors genotyped all 1,388 **survivors** using **9 microsatellites** (`FAP 95%`), whereas they genotyped 1,663 **mortalities** using **69 SNPs** (`FAP 99%`).
  - This differential genotyping platform between cases (mortalities) and controls (survivors) created two downstream artifacts:
    1. A substantial disparity in successful pedigree assignment rates between survivors ($90.3\%$ assigned) and mortalities ($71.9\%$ assigned; Line 69), which required simulating ungenotyped mortalities by random proportional sampling to reconstruct cohort heritability.
    2. When the selected `POP 1` QTL mapping subset ($n=1,273$) was subsequently genotyped on the 69-SNP panel, **28% of the genotyped survivors had to be discarded** due to Mendelian inheritance incompatibilities and genotype quality failures (`Line 236`), because those survivors had originally been assigned to families using only the 9 microsatellites (which had lower exclusion power than the 69 SNPs used for the mortalities)!
  - Fortunately, `POP 2` fish were individually PIT-tagged prior to challenge (100% known pedigree without marker assignment bias) and genotyped uniformly on the 6K Illumina SNP array, completely eliminating this bias in the replication cohort.
- **Confounding of Common Environment / Full-Sib Family Effects ($c^2$) in Variance Component Models:**
  - In `POP 1`, Models 1.1 and 1.2 yielded identical log-likelihoods ($\Delta\text{LogL} = 0$, Table 1) when fitting a common full-sib family effect ($c^2 = 0.02\text{--}0.04$), and in `POP 2`, fitting $c^2$ reduced the estimated additive genetic variance by roughly half (from $h^2_{01} = 0.26$ in Model 2.1 to $h^2_{01} = 0.13$ with $c^2 = 0.06$ in Model 2.1 when $c^2$ is included, Table 2), indicating partial confounding between non-additive/rear-tank full-sib effects and additive genetic effects in the half-sib design.

### 3. Biological / Experimental Grounding & Claim Proportionality / STRENGTHS
- **[Well Supported] Independent Cross-Population and Cross-Challenge Replication of the Chromosome 3 SAV3 Resistance QTL:** Identifying the exact same distal Chromosome 3 region (`42–49 cM`) via both half-sib linkage mapping and `GRAMMAS` mixed-model GWAS across two different year-classes, developmental stages (fry vs. post-smolt), and challenge routes (waterborne cohabitation vs. IP injection) is a gold-standard validation in quantitative genetics.
- **[Well Supported] Concordance Between Linkage Mapping (`GridQTL`) and Family-Adjusted GWAS (`GRAMMAS`):** Showing that the top genome-wide significant SNP (`ESTV_18493_1052` at $48\text{ cM}$) co-localizes with the dam-based linkage peak ($49\text{ cM}$) and that fitting `ESTV_18493_1052` as a fixed cofactor collapses the Chromosome 3 QTL test statistic from $F = 20.6$ to $F = 6.9$ (below genome-wide significance) confirms that the SNP tags the primary QTL in `POP 2`.
- **[Well Supported] Consistency Across Linear, Logit, and Probit Mixed Models:** Evaluating binary survival across linear (`IDEN`), logit (`LOGIT`), and probit threshold (`PROBIT`) models alongside first- vs. second-half mortality periods demonstrates that heritability estimates are robust to model specification.

### 4. Reproducibility & Data Completeness
- **Reproducibility Assessment:** Statistical mixed models (`ASReml`), linkage mapping formulas (`GridQTL`, $1 - (RSS_{\text{full}}/RSS_{\text{reduced}})$), and `GenABEL` (`GRAMMAS` + 10,000 permutations) are thoroughly documented. Flanking sequences, BLAST hits, and dbSNP accession numbers (`ss181359483` / `ESTV_18493_1052` and `ss181357766` / `ESTNV_29410_233`) for the two genome-wide significant Chromosome 3 markers are provided in Table 5 and Supplemental File 1.
</Blinded Review: TIME_ANON_0678>
