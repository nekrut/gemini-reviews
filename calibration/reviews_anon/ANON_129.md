# Review of ANON_129

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **5.4 / 10.0** (Mixed / Salvageable)  
* **Score Breakdown:** Rigor: 1.5/3.5 | Claims: 1.2/2.5 | Biology: 1.2/2.0 | Reproducibility: 1.5/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript examines the variation in raw codon usage frequencies across 1,484 complete proteobacterial genomes from RefSeq, focusing on both whole-genome coding sequences and a subset of 12 highly expressed housekeeping genes. By evaluating the standard deviation (SD) and 10th–90th percentile range of unnormalized codon frequencies across species, the authors classify codons into "variable" and "low variability" groups. They then compare 25 high-GC ($>67\%$) and 25 low-GC ($<32\%$) proteobacterial genomes using Roary and Scoary, identifying an enrichment of tRNA anticodon modification genes—most notably `tsaB`/`tsaE` ($\text{t}^6\text{A}$ synthesis), `gluQ`/`tgt` (GluQ synthesis), `tilS` ($\text{k}^2\text{C}$ synthesis), and `tusE`/`mnmA` ($\text{s}^2\text{U}$ synthesis)—and subsequently screen all 1,484 genomes via RPSBlast against CDD motifs to test associations between gene presence, codon usage, genomic GC%, and genome size. All Perl scripts, genome accessions, and supplementary tables are publicly archived in an institutional repository (DOI: `10.34691/UCHILE/AYDRZL`).

While the comparative curation of 1,484 proteobacterial genomes and the biological focus on tRNA anticodon loop modifications ($\text{t}^6\text{A}$, GluQ, $\text{s}^2\text{U}$) are valuable, the study's core quantitative conclusions rest on three methodological flaws: (1) using unnormalized raw codon frequencies and unscaled standard deviations, which confounds amino acid composition shifts across GC gradients and floor effects of rare codons with synonymous codon preference; (2) treating 1,484 phylogenetically related species as statistically independent observations in Wilcoxon and Kruskal–Wallis tests without phylogenetic comparative controls; and (3) circularly selecting candidate genes (`tsaB`, `gluQ`) by screening extreme High- vs. Low-GC genomes and then testing those same genes for an "impact" on GC% and GC-correlated codon usage without controlling for endosymbiont genome reduction. All three issues can be resolved computationally using the authors' existing dataset.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **A specific subset of codons (such as `AAC`, `CGA`, `AGG`, and `GGA`) is restricted to a narrow range of usage frequencies across proteobacteria independent of genomic GC%: [Fragile].**  
  Because the authors analyze raw genomic codon frequencies (codons per 100 total codons) rather than relative synonymous codon usage (RSCU) and quantify dispersion using raw standard deviation (Figures 1–2), two mathematical artifacts drive this observation. First, for rare codons such as `CGA`, `AGG`, `AGA`, `ATA`, and `CTA`, mean usage is close to zero ($0.1\%\text{–}0.4\%$) across almost all bacteria (e.g., `CGA` is universally avoided due to the purine–purine wobble clash with inosine in $\text{tRNA}^{\text{Arg}}_{\text{ICG}}$); because frequencies cannot be negative, a near-zero mean mathematically forces a small raw SD (floor effect), even when relative fold variation across species is large. Second, for `AAC` vs. `AAT` (Asn), both codons have `A` at positions 1 and 2 (`AAY`). As genomic GC% increases from 25% to 75%, total proteome Asn usage drops sharply while the synonymous fraction of `AAC` rises; the product of a falling amino acid frequency and a rising synonymous proportion cancels out, keeping raw `AAC` frequency nearly flat around 1.5–2.0% and producing a near-zero slope against GC% (Figure 5). Computing RSCU immediately reveals that `AAC` vs. `AAT` preference varies strongly with GC%.

* **The presence of tRNA modification genes (`tsaB`, `gluQ`, `tusE`) significantly alters codon usage frequencies across proteobacteria: [Overstated].**  
  In Figure 3, the authors split the 1,484 genomes by the presence or absence of `tsaB`, `gluQ`, `tilS`, and `tusE` and apply standard two-sample Wilcoxon–Mann–Whitney tests ($p < 0.00005$). This treats 1,484 tips of a phylogenetic tree as independent samples (phylogenetic pseudoreplication). In proteobacteria, losses of `tsaB`, `tsaE`, `gluQ`, and `tusE` are heavily concentrated in a few clades of obligate endosymbionts and intracellular parasites (e.g., *Buchnera*, *Wigglesworthia*, *Rickettsiales*) that share common ancestry, small genomes ($<2\text{ Mbp}$), and extreme AT-biased mutational drift. Without phylogenetic generalized least squares (PGLS) or phylogenetically independent contrasts, shared lineage effects and background genomic GC% confound the direct effect of the modification enzyme on individual codons.

* **Genes involved in $\text{t}^6\text{A}$ (`tsaB`) and GluQ (`gluQ`) formation impact the GC content of proteobacterial genomes: [Methodologically Flawed].**  
  The title of Figure 4 (*"Genes involved in $\text{t}^6\text{A}$ and GluQ formation impact the GC content in proteobacterial genomes"*) makes a causal claim that is undermined by circular variable selection and confounding by genome reduction. In Section 2.2, `tsaB` and `gluQ` were explicitly discovered by running Scoary on 25 extreme high-GC ($>67\%$) versus 25 extreme low-GC ($<32\%$) genomes. Re-testing those exact genes for an association with GC% in Figure 4 is statistically circular. Moreover, as shown in Supplementary Figure 17, `tsaB` and `gluQ` absence occurs almost exclusively in reduced genomes ($<2\text{ Mbp}$), where loss of DNA repair enzymes and Muller's ratchet independently drive both gene loss and AT bias. Removing only the 7 smallest genomes ($\le 400$ CDS, Supplementary Figures 19–22) leaves dozens of reduced endosymbiont/intracellular genomes ($0.5\text{–}2.0\text{ Mbp}$) in the dataset.

* **Low variability of codon usage is independent of cognate tRNA gene copy number: [Moderately Supported].**  
  The tRNAscan-SE 2.0 survey across the 1,484 genomes (Supplementary Figure 24) usefully confirms that most proteobacteria completely lack $\text{tRNA}^{\text{Asn}}_{\text{ATT}}$ and rely on $\text{tRNA}^{\text{Asn}}_{\text{GTT}}$ to decode both `AAC` and `AAT`. However, the interpretation that `AAC` and `AAT` respond differently to $\text{tRNA}^{\text{Asn}}_{\text{GTT}}$ copy number again requires controlling for total Asn amino acid frequency across the GC% spectrum.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Decouple Amino Acid Composition and Floor Effects from Synonymous Codon Variability
* **WHY:** Raw codon usage frequency ($f_c$) is the product of amino acid frequency ($f_{aa}$) and synonymous preference ($p_{c|aa}$). When an amino acid is encoded by AT-rich first/second codon positions (like Asn `AAY` or Lys `AAR`), $f_{aa}$ declines steeply with increasing genomic GC%, which masks the rise in G/C-ending synonymous preference ($p_{\text{AAC}|\text{Asn}}$) and creates an artificial "flat slope" and low raw SD. Simultaneously, universally rare codons (`CGA`, `AGG`, `ATA`) have low raw SD simply because their mean is near zero.
* **WHAT:** Recompute Figure 1, Figure 2, and Figure 5 alongside Relative Synonymous Codon Usage (RSCU) and Coefficient of Variation ($\text{CV} = \text{SD} / \text{mean}$).
* **HOW:** Using Supplementary Tables 7 and 8, calculate $\text{RSCU}_{i,j} = \frac{X_{i,j}}{\frac{1}{n_i}\sum_{j=1}^{n_i} X_{i,j}}$ for each synonymous family $i$, as well as $\text{CV} = \text{SD}/\mu$ for raw frequencies. Add a side-by-side heat table in Figure 2 and slope plot in Figure 5 comparing raw frequency SD/slopes against RSCU SD/slopes so readers can see exactly which "low variability" codons are driven by amino-acid-level GC shifts (`AAC`), which are driven by universal mean rarity (`CGA`, `AGG`), and which remain invariant after synonymous normalization.

#### 2. Control for Phylogenetic Non-Independence and Background GC% / Genome Size
* **WHY:** Treating 1,484 proteobacterial genomes as independent observations in Wilcoxon (Figure 3) and Kruskal–Wallis (Figure 4) tests violates statistical independence because closely related species share both gene content and GC%. Furthermore, codon usage differences between `tsaB`+/$-$ or `gluQ`+/$-$ genomes in Figure 3 are heavily confounded by the fact that `tsaB`$-$ and `gluQ`$-$ genomes are AT-rich reduced genomes.
* **WHAT:** Perform phylogenetically controlled regression and GC%-matched (or genome-size-stratified) comparisons for the tRNA modification genes.
* **HOW:** Using the CVTree phylogeny already constructed in Section 4.3, run phylogenetic generalized least squares (`gls` with `corPagel` or `corBrownian` in the R package `nlme`/`ape`, or `phylolm`) modeling codon usage (or RSCU) as a function of enzyme presence (`tsaB`, `gluQ`, `tusE`) while including genomic GC% (or intergenic GC%) and $\log_{10}(\text{genome size})$ as covariates. In addition, repeat the boxplot comparisons in Figure 3 restricted to free-living proteobacteria with genome sizes $>2.5\text{ Mbp}$ and matched GC% ranges to demonstrate whether `gluQ` and `tsaB` alter GAC/GAT and AAT/AAC usage independently of genome reduction.

#### 3. Eliminate Circularity in the GC% Association Analysis and Temper Causal Language
* **WHY:** Selecting `tsaB` and `gluQ` because they had the lowest Scoary $p$-values in a comparison of 25 high-GC vs. 25 low-GC genomes (Section 2.2) and then testing whether those genes associate with GC% in the full cohort (Section 2.4, Figure 4) is circular, and stating that these genes *"impact the GC content"* (Figure 4 caption) overstates a cross-sectional correlation.
* **WHAT:** Exclude the 50 discovery genomes when evaluating GC% associations in Section 2.4, control for genome size, and replace causal phrasing in the Abstract and Figure 4.
* **HOW:** Re-run the Figure 4 analysis on the 1,434 validation genomes after stratifying by genome size ($<2\text{ Mbp}$ vs. $\ge 2\text{ Mbp}$), and revise the Figure 4 title to *"The presence of genes involved in $\text{t}^6\text{A}$ and GluQ formation is correlated with GC content and genome size in proteobacterial genomes."*

#### 4. Technical, Mathematical, and Editorial Cleanup
* **WHY:** Several amino acid labels and supplementary figure cross-references in the main text and figure captions are incorrect.
* **WHAT & HOW:**
  * **Figure 1 Caption (Section 2.1):** Correct *"The distribution of codon usages for Asp codons AAT and AAC (A,B)"* to *"Asn codons AAT and AAC (A,B)"* (`AAT` and `AAC` encode asparagine, not aspartate).
  * **Figure 5 Caption (Section 2.6):** Correct *"The slopes of linear regressions in plots of codon usages vs. GC% (Supplementary Figure 17)"* to *"Supplementary Figure 23"* (Supplementary Figure 17 shows genome size vs. tRNA modification genes, whereas Supplementary Figure 23 shows codon usage vs. GC%).
  * **Section 2.3 (paragraph 2):** Correct the incomplete sentence *"Finally, we analyzed the frequency of ATA usage in genomes where tilS ."* to *"in genomes lacking tilS."*
  * **Section 3 (Discussion, point 2):** Correct *"in cases such as Asn AAC or Arg CGC, this explanation is unlikely because other codons for the same amino acids do vary within a wide range"*—in Section 2.1, `CGC` is classified as a *Variable Codon* and `CGA`/`AGG` as *Low Variability Codons*, so `Arg CGC` here should be `Arg CGA`.
