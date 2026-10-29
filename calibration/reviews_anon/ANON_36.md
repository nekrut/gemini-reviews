# Review of ANON_36

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **8.0 / 10.0** (Strong / Sound) | **Scientific Core Score:** **6.8 / 8.0**  
* **Score Breakdown:** Methodological Rigor: 2.9/3.5 | Claim-Evidence Alignment: 2.1/2.5 | Biological Plausibility: 1.8/2.0 | Reproducibility: 1.2/2.0  
* **Score Breakdown (Compact):** Rigor: 2.9/3.5 | Claims: 2.1/2.5 | Biology: 1.8/2.0 | Reproducibility: 1.2/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript uses experimental evolution in *Methylobacterium extorquens* AM1 to investigate how bacterial populations recover from severe fitness defects caused by recoding a single essential metabolic gene (*fae*, encoding formaldehyde-activating enzyme, 186 codons) with six distinct synonymous codon schemes (AF, AR, RN, VA, CO, and AC, carrying 46–150 synonymous substitutions). Propagating 8–10 replicate populations per recoded ancestor at two effective population sizes ($N_e$ differing by 5- to 50-fold) for 60–250 generations on methylamine minimal medium, the authors observe rapid, highly parallel fitness recovery driven in 48 of 55 populations by single point mutations in the 5′ coding region (the first 14 codons) or immediate upstream noncoding region of *fae*. Four of the nine evolved coding mutations are themselves synonymous (including an identical synonymous mutation fixed across all 8 AF populations). Allelic exchange ("snp" reconstructions in the ancestral chromosome and "bkg" replacements in evolved clones) proves that these single mutations are necessary and sufficient for the fitness gain. Through qPCR, anti-FLAG western blotting, enzyme activity assays, N-terminal FLAG-insert rescues, and an engineered library of 37 plasmid-borne point mutants spanning the predicted 5′ minimum folding energy (MFE) and anti-Shine–Dalgarno (anti-SD) affinity space, the authors show that neither 5′ MFE nor anti-SD affinity predicts the fitness effect of point mutations, and that cross-swapping evolved mutations into alternate *fae* alleles reveals strong intragenic epistasis.

This is a well-controlled experimental evolution study that pairs evolutionary repeatability across two independent laboratories with scarless chromosomal allelic reconstructions and systematic mechanistic falsification (testing 37 engineered mutations selected from the corners of the MFE / anti-SD prediction space plus 12 intragenic cross-swaps). The primary limitations are: (1) the plasmid-based testing of the 37 engineered point mutants and 12 cross-swaps uses an inducible tetracycline promoter (`pLC291` induced with 100 ng/ml anhydrotetracycline) that alters the 5′ UTR sequence relative to the native chromosomal *fae* transcript used in the MFE calculations ($-50$ to $+50\text{ bp}$); (2) the initial adaptive walk for the lethal AF and AC ancestors required transient succinate + methylamine co-supplementation, which complicates quantitative comparisons of evolutionary repeatability across population sizes; and (3) raw growth rate, qPCR, western blot, and sequencing data tables are not deposited in an open repository (`[ACCESSION_REDACTED in scrubbed input]`).

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Single point mutations in the 5′ N-terminal region (first 14 codons) or upstream region of *fae*—including four synonymous mutations—repeatedly fix under strong positive selection and are sufficient to restore fitness: [Well Supported].**  
  Scarless chromosomal allelic exchange placing 10 evolved SNPs individually into their respective ancestral backgrounds ("snp" strains, Figure 3A) and replacing the evolved *fae* allele with the ancestral allele in evolved clones ("bkg" strains, Supplementary Figure S4A) provides direct causal proof that single synonymous and nonsynonymous point mutations drive the 20% to $>75\%$ growth rate recovery without requiring genomic background mutations. Furthermore, running the large and small $N_e$ evolution experiments in two different laboratories on different continents rules out cross-contamination as the source of parallel fixation.

* **Neither predicted 5′ mRNA minimum folding energy (MFE) nor internal anti-Shine–Dalgarno (anti-SD) binding affinity is sufficient to predict the fitness impact of 5′ point mutations in *fae*: [Well Supported].**  
  Rather than stopping at a post-hoc correlation on the 9 evolved coding mutations (which all fell in quadrants decreasing either MFE or anti-SD affinity, Figure 5B–D), the authors prospectively engineered and assayed 37 point mutations across WT, AF, VA, and AC chosen to maximize or minimize MFE and anti-SD affinity (Figure 5E–J), alongside sensitivity checks across folding temperatures, dangling-end parameters, and full 16S rRNA tails (Supplementary Figures S11–S13). The complete absence of correlation ($R^2 \approx 0$) convincingly falsifies simple 5′ MFE and anti-SD pausing models as general predictors in this system.

* **The fitness benefit of evolved N-terminal coding mutations depends on intragenic epistatic interactions within the *fae* allele: [Moderately Supported].**  
  Testing 12 cross-swaps of evolved mutations into alternate recoded *fae* alleles (controlled for genomic background in a $\Delta fae$ strain, Figure 6) shows that mutations highly beneficial in VA or AC (e.g., three of four tested in AF) fail to rescue fitness in other *fae* alleles, whereas two swaps (`eAC1` into AF and `eAC3` into VA) confer even higher fitness than the natively evolved alleles. However, these cross-swaps were assayed on the inducible plasmid `pLC291` rather than in the native chromosomal locus, and the explanation for why VA populations never sampled `eAC3` (or the other beneficial engineered VA mutations in Figure 5F) despite single-nucleotide accessibility remains unresolved (e.g., mutational biases vs. clonal interference).

* **Evolved beneficial mutations rescue fitness by increasing translation efficiency or protein stability per transcript rather than altering metabolic regulation, even when changes in FAE protein levels are statistically undetectable: [Fragile].**  
  For strain VA, the 5-fold mRNA and 10-fold protein increases clearly support enhanced expression (Figure 3B–C, G). However, for evolved eAC and eAF strains, growth rate jumps from $0$ to near-WT ($\sim 0.15\text{ h}^{-1}$) while measured *fae* mRNA, FAE protein, and enzyme activity show near-zero, statistically non-significant changes relative to the ancestor (Figure 3B–D). Attributing this disconnect to "growth-dependent dilution" when all mRNA/protein harvests were actually performed after a 2-hour methylamine pulse in mid-log *succinate* cultures (where growth rates of ancestral and evolved strains are similar, Methods line 11) is internally inconsistent; the succinate-pulse assay specifically avoids differential growth dilution on methylamine, suggesting instead western blot / enzyme assay sensitivity limits or protein solubility/aggregation effects.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Reconcile the 5′ UTR Sequence Used in RNAfold MFE Calculations with the Plasmid Expression Vector `pLC291`
* **WHY:** In Figure 5, MFE is calculated on $100\text{ bp}$ windows spanning $-50$ to $+50\text{ bp}$ relative to the *fae* start codon (presumably using the native chromosomal upstream sequence), whereas the 37 engineered point mutants (Figure 5E–J) and 12 cross-swaps (Figure 6) were expressed from the anhydrotetracycline-inducible plasmid `pLC291`, which has a synthetic promoter/5′ UTR. Base-pairing between the $-50\text{ to }-1\text{ bp}$ 5′ UTR and the $+1\text{ to }+50\text{ bp}$ coding region differs between the native locus and `pLC291`.
* **WHAT:** Recompute the predicted MFE and ribosome binding site accessibility (e.g., Salis RBS Calculator $\Delta G_{\text{total}}$) using the exact 5′ UTR sequence transcribed from `pLC291` (and `pHC115` for Figure 4).
* **HOW:** Extract the transcription start site to $+50\text{ bp}$ sequence of `pLC291::fae` and `pHC115::fae`, run `RNAfold` and the RBS Calculator v2.0 on all 37 engineered mutants, and verify whether accounting for the plasmid 5′ UTR alters the MFE correlations in Figure 5I–J.

#### 2. Resolve the Growth-Dilution Argument vs. Succinate-Pulse Harvest Protocol for eAF and eAC
* **WHY:** On line 39, the text argues that *"growth-dependent dilution could be masking differences in protein production"* in eAC and eAF strains, yet the Methods Summary (line 11) states that for mRNA, protein, and enzyme assays, *"we grew cultures to mid-log phase in Hypho-succinate and induced fae expression with methylamine... After 2 h, we harvested cells"*. In succinate medium, ancestral AF/AC and evolved eAF/eAC strains grow at comparable rates, so methylamine-dependent growth dilution does not occur during a 2 h pulse in succinate.
* **WHAT:** Clarify the growth kinetics during the 2-hour methylamine induction in succinate medium and test whether non-linear Michaelis–Menten flux control (where a small increase in active FAE above zero relieves toxic formaldehyde accumulation) rather than growth dilution explains the step-function jump in growth rate.
* **HOW:** Fit a saturating hyperbolic (Monod/Michaelis–Menten) curve $g(E) = g_{\max} \frac{E}{K_m + E}$ to the growth rate versus enzyme activity data in Figure 3E–F, report the half-saturation constant $K_m$ as a percentage of WT FAE activity, and revise the discussion of growth dilution on line 39 to match the succinate-pulse experimental protocol.

#### 3. Fix Panel Cross-References and Deposit Underlying Numerical Datasets
* **WHY:** Minor figure cross-reference errors appear in the text, and raw numerical tables for the growth, qPCR, western blot, and MFE/anti-SD screens are not deposited in an external archive.
* **WHAT & HOW:**
  1. Line 55 (Figure 5 legend): Fix *"(from panels D–F)"* to *"(from panels E–H)"*.
  2. Line 62: Fix *"(figs. 5F and 6)"* to *"(figs. 5G and 6)"* (since panel 5F is strain VA and panel 5G is strain AC), and fix *"(fig. 5E and 5H)"* to *"(fig. 5F)"* (since VA is in panel 5F, whereas 5E is WT and 5H is AF).
  3. Deposit the raw plate-reader OD600 growth curves, qPCR $C_t$ values, western blot densitometry values, and FASTA sequences of all recoded and mutated *fae* alleles in Dryad or Zenodo.
