<Blinded Review: TIME_ANON_0956>
**Composite Score:** 8.2 / 10.0 (Rigor: 2.9/3.5 | Claims: 2.2/2.5 | Biology: 1.6/2.0 | Reproducibility: 1.5/2.0)
**Bias Category:** None (Methodologically Sound)
**Verdict:** Minor Revision
**Study Modality:** Hybrid Computational + Wet-Lab
**Technology Maturity:** Mature/Classical
**Epistemic Stage:** Basic/Mechanistic Discovery

OVERALL_SCORE: 8.2/10
VERDICT: PASS
ESTIMATED_DECADE: 2010s

---

### 1. Executive Summary / SUMMARY
This evolutionary genomics study tests whether the faster adaptive evolution of male-biased genes—previously well-documented in *Drosophila melanogaster*—holds in *Drosophila ananassae*, another member of the *melanogaster* group with distinct demographic history and sex-chromosome/recombination biology. The authors first construct a custom PCR-amplicon microarray (149 genes plus positive/negative controls) and hybridize three biological replicates (plus dye swaps; 12 hybridizations total) of male and female mRNA from an outbred Borneo population (`Klias` and `Tenom` isofemale lines), normalizing cDNA fluorescence against genomic DNA hybridizations and classifying sex-biased expression via Bayesian `BAGEL` (`FDR <= 10%`) combined with whole-genome microarray data from Zhang et al. (2007). They then sequence coding regions of 43 genes (15 male-biased, 15 female-biased, 13 unbiased in *D. ananassae*) across 12 inbred lines from a single ancestral-range population (`Bangkok, Thailand`) alongside two newly verified close sibling outgroup species within the *D. ananassae* subgroup (*D. atripex* and *D. phaeopleura*, confirmed via a 12-gene Bayesian phylogeny in `MrBayes`).

Using the maximum-likelihood McDonald-Kreitman (`MK`) framework of Eyre-Walker and Keightley (`DoFE`) with a polymorphism frequency cutoff ($\le 15\%$) to remove segregating slightly deleterious nonsynonymous mutations, the authors demonstrate two striking results: (1) ~59% of genes show conserved sex-biased expression between *D. melanogaster* and *D. ananassae*, and (2) while *D. ananassae* exhibits strong genome-wide adaptive protein evolution overall ($\alpha \approx 50\%\text{–}60\%$ vs. $\sim 45\%$ in *D. melanogaster*), male-biased genes in *D. ananassae* do **not** show higher rates of adaptive substitution ($\alpha = 43\%$) or $K_a/K_s$ ($0.109$) than female-biased ($\alpha = 60\%$, $K_a/K_s = 0.088$) or unbiased ($\alpha = 53\%$, $K_a/K_s = 0.133$) genes.

### 2. Methodological & Statistical Audit / STRENGTHS & WEAKNESSES & METHODOLOGICAL AUDIT

#### Strengths
1. **Rigorous Control of Slightly Deleterious Polymorphisms and Population Structure:** Standard MK estimates of $\alpha$ are downward-biased when weakly deleterious nonsynonymous mutations segregate at low frequencies or when samples are pooled across structured populations. Here, the authors sequence 12 lines from a single panmictic ancestral-range population (`Bangkok, Thailand`), verify that `Tajima's D` is significantly more negative at nonsynonymous (`-0.78`) than synonymous (`-0.31`) sites (Wilcoxon signed-rank test, $P < 0.001$), and apply a $\le 15\%$ minor allele frequency cutoff before running the Eyre-Walker & Keightley (`DoFE`) multi-locus maximum-likelihood model.
2. **Phylogenetic Validation of Closer Outgroups (*D. atripex* and *D. phaeopleura*):** Because *D. melanogaster* is too diverged from *D. ananassae* ($K_s = 1.46$, saturated synonymous sites), the authors sequence two close sibling species (*D. atripex* and *D. phaeopleura*, $K_s \approx 0.25\text{–}0.27$), reconstruct a 12-gene Bayesian tree (`MrBayes`) confirming they form a sister clade (`PP = 1.00`) to *D. ananassae*, and cross-validate $\alpha$ across all three outgroups (`Table 3`).
3. **Genomic DNA Normalization of Two-Color Microarrays:** Normalizing cDNA hybridization intensity against genomic DNA hybridization on the same amplicon spots controls for probe length and GC/hybridization efficiency differences, enabling valid absolute expression comparisons in addition to male/female ratios.
4. **Exemplary Self-Criticism Regarding Ascertainment Bias and Platform Mixing:** In the Discussion, the authors transparently test whether ascertaining genes initially from *D. melanogaster* biased their conclusions. They explicitly show that male-biased genes selected for extreme male bias in *D. melanogaster* (mean 12.1-fold) exhibit a much lower mean expression ratio in *D. ananassae* (5.2-fold, $P = 0.005$) due to regression to the mean / evolutionary turnover, and that 60 of the 129 genes came from their gonad-enriched custom array while 69 came from Zhang et al.'s whole-fly array. They then re-test the subset of genes that remained male-biased in *both* species (`Table 4`), showing that even these conserved male-biased genes have higher $\alpha$ in *D. melanogaster* ($73\%\text{–}82\%$) than in *D. ananassae* ($32\%\text{–}43\%$).

#### Weaknesses & Minor Issues
1. **Typographical Error in Table 4 Header:** In `Table 4` (*Polymorphism and Divergence of Genes That Show Conserved Expression Bias between D. melanogaster and D. ananassae*), the four columns under *D. ananassae* are labeled `D_N^b`, `D_S^c`, `P_S^d`, and **`D_N^e`**, where footnote `e` reads `"Nonsynonymous polymorphism"`. The fourth column header (`D_N^e`) is a typographical error for **`P_N^e`** (matching `P_N^e` under the *D. melanogaster* columns). The numerical values (`27`, `48`, `29`) and the resulting $\alpha$ estimates (`0.43`, `0.62`, `0.58`) are calculated correctly from $1 - (D_S P_N)/(D_N P_S)$ (or the ML equivalent).
2. **Modest Per-Class Gene Sample Size ($n = 13\text{–}15$ loci per bias class):** With 43 sequenced loci split into three classes (15 male-biased, 15 female-biased, 13 unbiased), the 95% confidence intervals on $\alpha$ in `Table 3` and `Table 4` are wide (e.g., male-biased $\alpha = 0.43$, 95% CI `[-0.17, 0.72]` with *D. atripex*), limiting statistical power to detect moderate differences between classes within *D. ananassae*.

### 3. Biological / Experimental Grounding & Claim Proportionality
- **Claim 1:** Approximately 60% of examined genes maintain conserved sex-biased expression between *D. melanogaster* and *D. ananassae*, whereas ~40% have gained, lost, or reversed sex bias over ~15–20 Myr. `[Well Supported]`
- **Claim 2:** *D. ananassae* exhibits a high overall proportion of adaptive amino acid substitutions ($\alpha \approx 50\%\text{–}60\%$), driven by historical population expansion and weakly deleterious segregating nonsynonymous polymorphisms. `[Well Supported]`
- **Claim 3:** Unlike *D. melanogaster*, male-biased genes in *D. ananassae* do not exhibit elevated rates of adaptive protein evolution compared to female-biased or unbiased genes, potentially reflecting species differences in mating system, sexual selection, or ascertainment of extreme expression bias. `[Well Supported]` — Phrased with commendable caution and backed by stratified re-analyses.

### 4. Reproducibility & Data Completeness
- **Data Availability:** Fully compliant. Microarray data are deposited in NCBI GEO under accession `GSE19096`, and all newly generated DNA sequences across the 12 *D. ananassae* lines and outgroups are deposited in GenBank under accessions `FN546265–FN546780`.
- **Methodological Detail:** Full descriptions of fly strains, microarray normalization equations, `BAGEL` FDR thresholds, `DoFE` ML parameters, and `MrBayes` settings are provided.
</Blinded Review: TIME_ANON_0956>
