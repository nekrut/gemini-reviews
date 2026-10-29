# Forensic Review of FEXP_ANON_036

**Manuscript ID:** `FEXP_ANON_036`  
**Overall Score:** **4.1 / 10.0** (Flawed / Overstated) | **Scientific Core Score:** **2.6 / 8.0**  
* **Score Breakdown:** Rigor: 0.9/3.5 | Claims: 0.8/2.5 | Biology: 0.9/2.0 | Reproducibility: 1.5/2.0

---

## 1. Blinded Metadata Perception

* **Perceived Subfield:** Plant Organellar Genomics / Mitochondrial Synonymous Codon Usage Analysis (Asphodelaceae: *Hemerocallis citrina*).
* **Study Design:** Descriptive bioinformatic analysis of 28 protein-coding genes (8,850 codons) from the previously sequenced mitochondrial genome of *Hemerocallis citrina* Baroni (`MZ726801.1`–`MZ726803.1`), paired with RSCU hierarchical clustering and 16-gene maximum likelihood phylogenetic reconstruction across 15 monocot species.
* **Primary Methods:** CodonW v1.4.2 and EMBOSS Cusp/Chips indices (GC1, GC2, GC3, GCall, GC3s, ENC, CAI, CBI, Fop, RSCU), Pearson correlation matrix, ENC-plot, neutrality plot regression, PR2 bias plot, $\Delta\text{RSCU}$ extreme-10% ENC split for "optimal codons," SPSS v25 squared-Euclidean RSCU clustering, and MEGA 7 Tamura-Nei ML phylogeny.

---

## 2. Executive Summary & Editorial Verdict

This manuscript characterizes synonymous codon usage statistics across 28 protein-coding sequences (8,850 total codons) extracted from the mitochondrial genome of daylily (*Hemerocallis citrina* Baroni) and compares its genome-wide RSCU profile and 16-gene mitochondrial phylogeny with 14 other monocot mitogenomes. The authors report that the *H. citrina* mitogenome is moderately A/T-rich ($\text{GCall} = 43.59\%$, $\text{GC3} = 39.05\%$, $\text{GC3s} = 36.04\%$) with weak overall codon bias ($\text{mean ENC} = 53.89$, range $39.34\text{--}60.01$). Based on an ENC-plot, a PR2 plot, and a neutrality plot regression across the 28 genes ($r = -0.1755, P > 0.05$, slope $= -0.1038$), they conclude that mutational pressure accounts for 10.38% of codon usage bias while natural selection is the decisive factor (89.62%), define 22 "optimal codons" via an extreme 10% ENC split, and argue that RSCU clustering reflects monocot evolutionary relationships.

**Editorial Verdict: Reject / Major Overhaul Required (Flawed / Overstated).** While the underlying NCBI mitogenome accessions are publicly available and the basic nucleotide composition tables are straightforward, the analytical pipeline applies automated bacterial/nuclear codon-bias heuristics that are statistically and biologically invalid for a 28-gene land plant mitogenome: (1) partitioning the top and bottom 10% of 28 genes by ENC defines "high-expression" and "low-expression" groups consisting of just $N \approx 3$ short genes (~443 codons total in the low-ENC group, where multiple amino acid codons have zero observations due to finite gene length), without any transcriptomic expression data or correction for C-to-U mitochondrial RNA editing; (2) interpreting a non-significant GC12-vs-GC3 regression slope ($-0.1038, P > 0.05$) across 28 genes on a single uniform-GC organelle chromosome as quantitative proof that "mutation pressure accounted for only 10.38%" and natural selection accounted for ~90% is a mathematical fallacy; and (3) the manuscript contains a corrupted Wright (1990) ENC equation and probability-fraction errors in the text describing Table 3.

### Specific Conclusions and Assessment of Support

* **The *H. citrina* mitogenome exhibits weak overall codon usage bias ($\text{mean ENC} = 53.89$) and a compositional preference for A/T-ending synonymous codons ($\text{GC3s} = 36.04\%$): [Well Supported].**  
  Direct tabulations across the 28 protein-coding genes (8,850 codons; Tables 1 and 2) confirm standard land-plant mitochondrial A/T enrichment at third codon positions and high ENC values ($>50$ in 21 of 28 genes).
* **Natural selection is the decisive factor shaping *H. citrina* mitochondrial CUB, with mutation pressure accounting for only 10.38% based on the neutrality plot slope ($-0.1038$): [Methodologically Flawed].**  
  Regressing GC12 on GC3 across $N = 28$ genes residing on the same mitochondrial genome yields $r = -0.1755$ ($P > 0.05$). Because all 28 genes share virtually the same background mitochondrial mutational environment ($\text{GC3} \in [29.9\%, 44.4\%]$ except for the maturase gene `matR` at $56.8\%$), there is no wide mutational GC gradient across genes to produce a unit slope under neutrality. Equating $|b| = 0.1038$ from a statistically non-significant negative slope to "10.38% mutation pressure and 89.62% natural selection" is statistically invalid.
* **22 "optimal codons" were identified in *H. citrina* mtDNA for optimizing exogenous gene expression, and mt gene expression is universally low ($\text{mean CAI} = 0.17$): [Methodologically Flawed].**  
  First, CodonW computes CAI, CBI, and Fop against a built-in *Escherichia coli* (or yeast) nuclear/bacterial reference set by default; reporting $\text{CAI} = 0.12\text{--}0.21$ as evidence that "mt gene expression [is] relatively low in *H. citrina*" (line 70) is biologically meaningless because core oxidative phosphorylation genes (`cox1`, `atp1`, `cob`) are among the most highly transcribed genes in plant cells. Second, defining "optimal codons" by taking the extreme 10% of 28 genes ordered by ENC selects just 3 short genes (`rps13` [117 codons], `ccmB` [207 codons], `nad3` [119 codons]), where ENC is depressed by small-sample finite-length bias (confirmed by the positive correlation between ENC and codon count in Fig. 1) rather than translational selection, and where codons like `GCG` and `UGC` have $\text{RSCU}_{\text{High}} = 0$ simply because they do not occur in those 3 short genes. Third, plant mitochondrial transcripts undergo pervasive C-to-U RNA editing prior to translation, which was ignored.
* **Concatenated 16-gene ML phylogeny places *H. citrina* (Asphodelaceae) in a well-supported Asparagales clade with *Asparagus officinalis*, *Chlorophytum comosum*, and *Allium* species, whereas RSCU clustering only partially tracks phylogeny: [Moderately Supported].**  
  The 16-gene mitochondrial ML phylogeny (Fig. 8) accurately recovers the expected Asparagales topology, and the authors appropriately note that RSCU Euclidean clustering (Fig. 7) misplaces distant monocots such as *Spirodela polyrrhiza* and splits Poaceae (*Zea mays* vs. *Oryza sativa*).

---

## 3. Forensic Defect Inventory

### 1. Invalid Extreme-10% ENC Split ($N \approx 3$ Short Genes) and Default *E. coli* CAI Reference (Pillars 3, 4 & 6)
* **WHY:** In Section "Analysis of RSCU and putative optimal codons" (line 199), selecting the top and bottom 10% of 28 genes ordered by ENC yields only $2.8 \approx 3$ genes per group. The three lowest-ENC genes in Table 2 are `rps13` (117 codons, ENC 39.34), `ccmB` (207 codons, ENC 44.91), and `nad3` (119 codons, ENC 48.69)—totaling only 443 codons across all 20 amino acids! With ~443 codons, rare amino acids (e.g., Cys) are represented by only a handful of residues, producing $\text{RSCU}_{\text{High}} = 0.00$ for `UGC` and `GCG` (Table 3) purely from small-sample noise. Furthermore, ordering genes by DNA ENC assumes that low ENC reflects high translational expression, whereas in Table 2 the core respiratory subunits (`atp1`, `cox1`, `cox3`, `cob`) have intermediate-to-high ENC (52.75–56.44) and the lowest ENC values occur in the shortest genes (causing the artifactual positive correlation between ENC and codon count in Fig. 1). Finally, inferring "low mt gene expression" from CodonW's default *E. coli* CAI (0.12–0.21, line 70) is invalid for plant mitochondria.
* **WHAT:** Remove the claim that $\text{CAI} = 0.17$ indicates low mitochondrial gene expression, and either replace the 3-gene ENC split with experimentally measured RNA-seq transcript abundance (and C-to-U edited mRNA sequences) or explicitly caveat Table 3 as a descriptive difference between the lowest-ENC and highest-ENC genes after controlling for gene length.
* **HOW:** Re-compute CAI/Fop using high-expression *H. citrina* mitochondrial respiratory genes (`cox1`, `cox2`, `cox3`, `atp1`, `atp6`, `cob`) as the organism-specific reference set, and test whether $\Delta\text{RSCU}$ between respiratory chain genes and ribosomal/maturase genes is statistically significant via a $2\times 2$ contingency $\chi^2$ or Fisher's exact test per codon family rather than an uncalibrated $\Delta\text{RSCU} > 0.08$ cutoff on 3 short genes.

### 2. Fallacious Interpretation of a Non-Significant Negative Neutrality Slope ($-0.1038$) (Pillars 3 & 4)
* **WHY:** In Section "Cause analysis of codon usage preference" (line 91), the OLS regression of GC12 on GC3 across the 28 genes gives $r = -0.1755$ ($P > 0.05$) and a negative slope of $-0.1038$. When the linear regression is statistically indistinguishable from zero ($P > 0.05$) and has a *negative* sign, taking the absolute value of the point estimate ($|-0.1038| = 10.38\%$) to claim that "the mutation pressure effect accounted for only 10.38%" and natural selection accounted for the remaining 89.62% is mathematically baseless. Moreover, in Wright's ENC-plot analysis (line 83), the authors report that 15 of 28 genes (53.57%) have an ENC ratio within $[-0.05, +0.05]$—meaning over half the genes lie within 5% of the expected compositional curve!
* **WHAT:** Retract the quantitative claim that mutation pressure accounts for 10.38% of CUB and that natural selection is the decisive factor (89.62%).
* **HOW:** Report the 95% confidence interval for the neutrality regression slope (which spans zero), note that narrow intra-mitogenomic GC3 variation ($30\%\text{--}44\%$ across 27 of 28 genes) and small gene lengths ($101\text{--}673$ codons) account for the scatter around the expected ENC curve, and conclude that weak compositional bias ($\text{GC3s} = 36.04\%, \text{mean ENC} = 53.89$) is the primary feature of the *H. citrina* mitogenome.

### 3. Corrupted Wright (1990) Equation and Fraction Denominator Errors (Pillar 7)
* **WHY:**
  1. In Section "ENC-plot analysis" (line 184), the equation for expected ENC is written as `ENC expected = 2 + GC3s + 29 GC3s + 1 - GC3s 2`, missing the division operator, the square on the first $\text{GC3s}^2$ term, and parentheses around $(1 - \text{GC3s})^2$.
  2. In Section "Determination of RSCU values and putative optimal codons" (line 109), the authors state: *"22 optimal codons were identified... In the preferred codons, 19 codons ended with A (7/19) or T (12/19), while only three codons ended with G (2/3) or C (1/3)."* The fractions `7/19`, `12/19`, `2/3`, and `1/3` use the subgroup counts (19 and 3) rather than the total number of optimal codons (22) as the denominator.
  3. In Data Availability (lines 246, 259), the species name is misspelled as *"Hemerocallis citrine"* and *"Apostasia shenzhenic a"*.
* **WHAT & HOW:** Fix the equation in line 184 to $\text{ENC}_{\text{expected}} = 2 + \text{GC3s} + \frac{29}{\text{GC3s}^2 + (1 - \text{GC3s})^2}$; change the fractions in line 109 to `7/22`, `12/22`, `2/22`, and `1/22`; and correct the species spelling in the Data Availability section.

---

## 4. Quantitative Rubric Scoring

| Rubric Dimension | Score | Max | Forensic Justification |
| :--- | :---: | :---: | :--- |
| **1. Methodological & Statistical Rigor** | **0.9** | **3.5** | Standard descriptive codon tabulations and 16-gene ML tree, but severely compromised by defining "optimal codons" from the extreme 10% ($N \approx 3$ short genes, ~443 codons) of 28 genes without expression data, using default *E. coli* CAI reference weights, and interpreting a non-significant negative neutrality slope ($-0.1038, P > 0.05$) as 10.38% mutation / 89.62% selection. |
| **2. Claim-to-Evidence Alignment** | **0.8** | **2.5** | Claims that natural selection is the decisive factor in *H. citrina* mtDNA CUB, that mt gene expression is low ($\text{CAI}=0.17$), and that the 22 codons represent translationally optimal codons for genetic engineering are unsupported by the data. |
| **3. Data Integrity & Biological Plausibility** | **0.9** | **2.0** | Authentic NCBI mitogenome data (`MZ726801.1`–`MZ726803.1`), but ignores plant mitochondrial C-to-U RNA editing, polycistronic transcription, and finite-length bias in short ribosomal genes (`rps13`, `nad3`, `rps14` with 101–119 codons). |
| **4. Reproducibility & Data Integrity** | **1.5** | **2.0** | All 15 monocot NCBI accessions and software versions (CodonW v1.4.2, MAFFT v7.4.0, MEGA 7, SPSS 25.0) are clearly documented; deducted 0.5 pts for the corrupted Wright (1990) equation in line 184 and denominator/spelling typos in lines 109 and 246. |
| **Scientific Core Score** | **2.6** | **8.0** | Sum of Rigor + Claims + Biology (`0.9 + 0.8 + 0.9`). |
| **Total Composite Score** | **4.1** | **10.0** | **Flawed / Overstated** (`0.9 + 0.8 + 0.9 + 1.5`). |
