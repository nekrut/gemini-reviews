# Blinded Review: SP_ANON_072
**Composite Score:** 8.6 / 10.0 (Rigor: 3.0/3.5 | Claims: 2.3/2.5 | Biology: 1.5/2.0 | Reproducibility: 1.8/2.0)
**Bias Category:** None (Methodologically Sound)
**Verdict:** Accept
**Study Modality:** Dry-Lab Secondary Cohort/Database Re-Analysis
**Technology Maturity:** Mature/Classical
**Epistemic Stage:** Translational/Preclinical/Biomarker

## 1. Executive Summary
This manuscript is a data descriptor and reproducible computational workflow accompanying a primary investigation of HIV-1 *gag* and *gp41* evolution in patients experiencing virological failure on boosted protease inhibitor (PI, $n = 41$) or non-nucleoside reverse transcriptase inhibitor (NNRTI, $n = 20$) regimens. It provides two distinct resources: (1) curated global one-per-person ART-naive amino acid prevalence profiles for full-length *gag* ($N = 5,338$ sequences curated from 7,550 LANL records) and *gp41* ($N = 4,242$ sequences curated from 7,489 LANL records), filtered for frameshifts, large deletions, APOBEC3G/F hypermutation (via a Poisson local false discovery rate model), and excessive unusual mutations ($\le 0.1\%$ prevalence); and (2) paired pre- and post-therapy clinical alignments together with open-source HyPhy v2.3.2 batch files (`pairwise-estimator-dnds.bf`, `run-fel.sh`, `run-meds.sh`) and R scripts for computing pairwise $dN/dS$ ratios, site-specific purifying selection (FEL), and episodic directional selection (MEDS).

The dataset curation, technical validation, and computational packaging are exemplary. The APOBEC3G/F statistical filter (`LocFDRPois`), inter- vs. intra-subtype genetic distance validation, and comparison against an independent 2012 *gag* amino acid profile (92.9% site-level concordance) are rigorously documented. Only minor methodological nuances—such as the two-pass empirical threshold used to filter sequences with multiple "unusual" mutations and the stripping of insertions prior to codon-model inference—warrant brief notation.

## 2. Methodological & Statistical Audit

### 2.1 Rigorous Quality Control and APOBEC3G/F Hypermutation Filtering
- Retrieving all LANL HIV Sequence Database sequences from PI-naive individuals and selecting a single sequence per patient yielded 7,550 *gag* and 7,489 *gp41* sequences. The authors apply a transparent, multi-stage QC pipeline:
  1. Removal of sequences with stop codons, frameshifts, premature terminations, or long deletions ($\ge 20$ amino acids in *gag* or $\ge 15$ amino acids in *gp41*).
  2. Identification of 159 signature APOBEC3G/F mutations in *gag* and 107 in *gp41* (defined as $\text{G}\to\text{A}$ changes occurring at $\le 0.1\%$ prevalence in G-to-A dinucleotide contexts that were enriched $>5$-fold in hypermutated reference sequences).
  3. Fitting a zero-inflated/two-component Poisson mixture model (`LocFDRPois` in R `locfdr`, with penalty $\lambda = 3$) to the per-sequence count of APOBEC mutations. This principled statistical threshold demonstrated that sequences carrying $\ge 3$ APOBEC signature mutations had an estimated local FDR $< 0.024$ (97.6% posterior probability of true APOBEC hypermutation), resulting in the removal of 91 *gag* and 219 *gp41* sequences.

### 2.2 Minor Circularity in the Two-Pass "Unusual Mutation" Filter
- In the final curation step, the authors define "unusual mutations" as amino acid variants with prevalence $\le 0.1\%$ in the post-APOBEC alignment, discard sequences containing $\ge 11$ unusual mutations in *gag* ($n = 39$) or $\ge 8$ in *gp41* ($n = 46$), and then recompute the final amino acid prevalence tables on the remaining 5,338 *gag* and 4,242 *gp41* sequences.
- While effective at catching low-quality Sanger traces or sequencing frameshifts that escaped earlier filters, defining unusual mutations relative to the unstratified global dataset (where subtypes C, B, CRF01_AE, and A comprise $>85\%$ of sequences, while rare subtypes D, F, G, H, J, K and rare CRFs each represent $<2\%$) means that divergent minor subtypes naturally carry more residues at $\le 0.1\%$ global prevalence. Fortunately, the authors also provide subtype-stratified amino acid prevalence columns for subtypes A, B, C, and CRF01_AE in `gagAAPrevalence.csv` and `gp41AAPrevalence.csv`.

### 2.3 Pairwise $dN/dS$, Selection Index, and Handling of Indels
- The HyPhy v2.3.2 script `pairwise-estimator-dnds.bf` uses the Muse-Gaut 94 (`MG94`) codon model combined with the general time-reversible (`REV`) nucleotide substitution matrix (`MG94xREV`) to estimate maximum-likelihood synonymous and nonsynonymous substitution rates on 2-taxon trees for each patient's paired pre- and post-treatment sequences.
- To account for the expected regression to the consensus (where rare baseline variants revert toward wild-type and common baseline variants mutate away), the authors define a Selection Index:
  $$\text{SI} = \log_{10}\left(\frac{p_{\text{pre}}}{p_{\text{post}}}\right)$$
  where $p_{\text{pre}}$ and $p_{\text{post}}$ are the naive population prevalences of the pre-therapy and post-therapy amino acids, respectively. By comparing patients failing boosted PIs ($n = 41$) against a control group failing NNRTIs ($n = 20$), the pipeline controls for background immune-driven diversification over time without requiring a matched untreated cohort.
- One structural limitation of standard codon substitution models (`MG94xREV`, `FEL`, `MEDS`) is that insertions relative to HXB2 must be stripped prior to alignment analysis. In HIV-1 *gag*, PTAP and PSAP motif duplications/insertions in the p6 late domain are well-known compensatory mechanisms during PI failure; stripping insertions omits these indel-mediated resistance pathways from the codon-model output, though they remain recoverable from the raw GenBank sequences.

## 3. Biological / Experimental Grounding & Claim Proportionality

### Claim Audit Summary
- **Claim 1:** *"Following quality control filtering, 5,338 gag sequences and 4,242 gp41 sequences were used to generate group M and subtype A, B, C and CRF01_AE amino acid profiles."* — **[Well Supported]**: Every stage of sequence attrition from LANL retrieval to the final profile tables is documented with exact counts and statistical criteria.
- **Claim 2:** *"Based on the resulting local false discovery rate (FDR) estimations, sequences with 3 or more APOBEC mutations had an estimated probability >97.6% (local FDR < 0.024) of having undergone APOBEC-mediated hypermutation."* — **[Well Supported]**: Directly grounded in the `LocFDRPois` empirical Bayes mixture model applied to the observed count distribution.
- **Claim 3:** *"Comparison with an earlier 2012 gag conservation profile showed 92.9% agreement in assigning positions to <1% vs. >=1% variability categories (35 of 496 positions differed, with median absolute prevalence difference of 0.35%)."* — **[Well Supported]**: Directly verified in the Technical Validation section, confirming high stability of the naive reference profiles across database growth.

## 4. Reproducibility & Data Completeness
- **Exemplary Open Science Standards:** All curated alignments, amino acid prevalence tables (`gagAAPrevalence.csv`, `gp41AAPrevalence.csv`), clinical pre/post-PI and pre/post-NNRTI paired sequences, HyPhy batch scripts (`pairwise-estimator-dnds.bf`, `run-fel.sh`, `run-meds.sh`), APOBEC filtering scripts, and R visualization scripts are publicly archived both in Dryad (Data Citation 1) and in a version-controlled GitHub repository (`[GITHUB_REPO_REDACTED]`), alongside GenBank accession numbers for all clinical sequences.
