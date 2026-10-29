<Blinded Review: TIME_ANON_0791>
**Composite Score:** 5.4 / 10.0 (Rigor: 1.5/3.5 | Claims: 1.2/2.5 | Biology: 1.2/2.0 | Reproducibility: 1.5/2.0)
**Bias Category:** Statistical/Design
**Verdict:** Major Revision
**Study Modality:** Wet-Lab Primary Experimental
**Technology Maturity:** Mature/Classical
**Epistemic Stage:** Translational/Preclinical/Biomarker

OVERALL_SCORE: 5.4/10
VERDICT: CAVEATS
ESTIMATED_DECADE: 2020s

---

### 1. Executive Summary (SUMMARY)
This study surveys coding region polymorphisms of the shadow of prion protein gene (*SPRN*, encoding Sho) by direct Sanger sequencing of a 628-bp amplicon in 235 Hanwoo (Korean native beef) and 212 Korean Holstein (dairy) cattle. The authors identify seven polymorphisms: three nonsynonymous SNPs (`c.110G>C` G37A, `c.125C>T` A42V, `c.128G>A` R43K), three synonymous SNPs (including novel `c.231G>A` A77A, `c.288A>G` E96E, `c.360G>A` G120G), and a 12-bp alanine-rich insertion/deletion (`c.199_210delGCCGCGGCGGGG` / `67_70delAAAG`). They report linkage disequilibrium ($D'$) and haplotype frequencies (`Haploview 4.2`), score coding variants with `PROVEAN`, and compare the frequency of the 12-bp deletion in healthy Korean cattle against a literature report of Polish cattle with atypical BSE. While the primary genotyping of 447 cattle is straightforward, the study's central interpretative claims—that Hanwoo cattle have "more potential susceptible genetic features" for atypical BSE than Holstein cattle and that all seven polymorphisms are in "strong LD" ($D' = 1.0$)—rest on fundamental statistical and population-genetic fallacies.

### 2. Methodological & Statistical Audit (STRENGTHS, WEAKNESSES & METHODOLOGICAL AUDIT)
**Strengths:**
* **Direct Resequencing in a Large Breed Cohort ($N=447$):** Complete open reading frame (432 bp) Sanger sequencing with $Q > 40$ base-calling across 235 Hanwoo and 212 Holstein cattle provides a clean catalog of allele and genotype frequencies in two major livestock breeds.

**Weaknesses & Methodological Audit:**
* **Fallacious Inference of "BSE Susceptibility" from Failure to Reject the Null Hypothesis Against $n=1$ Carrier:** In Figure 2 and Results/Discussion, the authors compare the 12-bp deletion frequency in healthy Hanwoo ($21/235$ heterozygotes, $9.0\%$) and healthy Holstein ($0/212$, $0\%$) against a literature sample of Polish atypical BSE cattle (in which, as noted in the Introduction, the 12-bp deletion was found in **only one case** of L-type atypical BSE). Because Fisher's exact test between Polish atypical BSE cattle and Hanwoo yields $P = 0.4405$ (non-significant), whereas Polish atypical BSE vs. Holstein yields $P = 0.0275$, the authors conclude that *"Hanwoo cattle showed more potential susceptible distribution in the genotype and allele frequencies of the 12-bp insertion/deletion polymorphisms of the SPRN gene than Holstein cattle."* This violates two basic principles of statistical genetics:
  1. Failing to reject the null hypothesis ($P = 0.44$) against a tiny external sample with 1 carrier does not establish equivalence or disease susceptibility.
  2. Hanwoo and Holstein have divergent breed ancestry; a $4.5\%$ allele frequency difference between healthy breeds (in a country with zero reported BSE cases) reflects neutral breed population structure rather than TSE susceptibility.
* **Artifactual $D' = 1.0$ Linkage Disequilibrium Claims on Singleton and Ultra-Rare Variants:** In Table 2, the authors report $D' = 1.0$ across nearly all pairs and conclude that *"all other polymorphisms showed strong LDs with D' values > 0.9."* However, in Table 1, `c.110G>C` is a **singleton** observed in 1 chromosome out of 894 ($p = 0.0011$), `c.125C>T` and `c.128G>A` are present in only 3 chromosomes ($p = 0.0034$), and `c.231G>A` in 5 chromosomes ($p = 0.0056$). For any pair of rare variants where the double-minor allele haplotype is unobserved in a sample of $N=447$ (expected count $< 0.05$), Lewontin's $|D'|$ is mathematically forced to $1.0$ ($|D/D_{\max}| = p_A p_B / p_A p_B = 1.0$), whereas the squared correlation $r^2$ is near $0.000$. Reporting $D'$ without $r^2$ for rare alleles creates a misleading impression of tight physical linkage disequilibrium.
* **Unexplained Hardy–Weinberg Equilibrium Violation in Holstein `c.360G>A`:** In Table 1, `c.360G>A` in Holstein shows 169 `G/G`, 33 `G/A`, and 10 `A/A` (HWE $P < 0.001$; ~3-fold excess of homozygotes over the 3.3 expected), which is noted without checking for PCR allelic dropout (e.g., polymorphisms under primer binding sites) or herd stratification.

### 3. Biological / Experimental Grounding & Claim Proportionality
* **Claim 1 (Identification of 7 *SPRN* coding polymorphisms in Korean cattle, including novel synonymous SNP `c.231G>A` and breed-specific allele frequency differences): `[Well Supported]`** — Directly supported by Sanger sequencing electropherograms and contingency table tests across 447 animals.
* **Claim 2 (All 7 polymorphisms exhibit strong linkage disequilibrium [$D' > 0.9$]): `[Methodologically Flawed]`** — Artifact of computing $D'$ on singleton/ultra-rare alleles ($n=1, 3, 5$) without reporting $r^2$.
* **Claim 3 (Hanwoo cattle have a more "susceptible" *SPRN* genetic distribution for atypical BSE than Holstein cattle): `[Overstated]`** — Unsupported extrapolation from a cross-breed frequency difference and a non-significant $P$-value against a single Polish atypical BSE carrier.
* **Claim 4 (`c.110G>C` [G37A] is a deleterious candidate factor in TSE pathogenesis): `[Fragile]`** — Observed as a single heterozygote in 1 of 447 cattle ($0.1\%$ allele frequency) and evaluated solely by a sequence-homology `PROVEAN` score ($-4.635$) with no biochemical or functional assay.

### 4. Reproducibility & Data Completeness
* **Good Methodological Transparency:** PCR primers (`5'-TGAGATCTCCTTCTCCGTCC-3'` and `5'-GAGGTGTCACAGCTTCAGG-3'`), reference GenBank accession (`JQ811202.1` / Gene ID `616266`), cycling parameters, and complete genotype/allele/haplotype count tables are fully reported in the manuscript.
</Blinded Review: TIME_ANON_0791>
