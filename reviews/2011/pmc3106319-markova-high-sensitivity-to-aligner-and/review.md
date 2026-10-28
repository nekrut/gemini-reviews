# Review of PMC3106319 (PMID:21393387)

**Manuscript Title:** High sensitivity to aligner and high rate of false positives in the estimates of positive selection in the 12 Drosophila genomes  
**Authors:** Markova-Raina P, Petrov D.  
**Journal / Preprint:** *Genome Res* (2011; `PMC3106319` / `PMID:21393387` / `10.1101/gr.115949.110`)  
**Calibration Study Cohort:** Cohort B — Validated Control (`B50` | Double-Blinded as `ANON_156`)  
**Overall Score:** **8.3 / 10.0** (Strong / Sound)  
* **Score Breakdown:** Rigor: 2.9/3.5 | Claims: 2.1/2.5 | Biology: 1.8/2.0 | Reproducibility: 1.5/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript systematically evaluates how multiple sequence alignment (MSA) software choice affects genome-wide inferences of positive selection under site-specific codon models (`PAML codeml` models M1a/M2a and M7/M8). Using the GLEAN-R reconciled consensus ortholog set from the 12 *Drosophila* Genomes Consortium (6,698 12-species single-copy orthologs and 8,563 6-species *melanogaster*-group orthologs), the authors compare six alignment programs—AMAP, ClustalW, MUSCLE, ProbCons, T-Coffee, and codon-aware PRANK (`-codon`)—across multiple stringency thresholds (95% and 99% BEB posterior probability; gene-level LRT with $\chi^2_2$, Bonferroni, and Storey's FDR $q$-values), post-alignment filtering strategies (`cleandata=1` gap removal, divergence-based masking, and column trimming), and downstream Gene Ontology (GO) enrichment analyses (FatiGO). Through visual inspection of 128 gene alignments and automated proximity checks, the authors show that aligner choice dramatically alters both the count and identity of genes inferred to be under positive selection (with all five standard aligners agreeing on only 22% of genes under M7/M8 at the 95% cutoff), that 85% of inferred positively selected sites lie within 10 codons of an indel and 61%–85% fall in intrinsically disordered regions (IUPred), and that 48%–82% of visually inspected candidates (and 50%–55% even with PRANK or masked/trimmed 6-species alignments) involve misaligned non-homologous codons due to exon-border annotation errors or fast-evolving indel-rich regions.

This is a thorough, consequential forensic audit of a widely used comparative genomics paradigm, demonstrating that treating heuristic MSAs as ground truth in genome-wide PAML scans produces pervasive false positives that corrupt downstream biological conclusions (such as GO term enrichments and spatial clustering of selected sites). The main limitations are: (1) the headline "false positive rates of 48%–82%" rely on unblinded, qualitative visual inspection of a modest subsample of genes ($n = 83$ for the five standard aligners, $n = 20$ for PRANK, $n = 25$ for masked *melanogaster*-group genes), where visually ambiguous alignments in genuinely fast-evolving disordered regions are categorized as false positives of positive selection; (2) the five standard aligners were run on amino acid sequences and back-threaded to codons, whereas PRANK was run directly in `-codon` mode, confounding the algorithmic effect of phylogeny-aware gap placement with codon vs. protein alignment space; and (3) PAML gene-level LRT $p$-values were computed using a conservative $\chi^2_2$ reference distribution rather than the correct boundary mixture distribution, distorting the $p$-value distribution fed into Storey's FDR procedure.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Aligner choice strongly alters the number, identity, and downstream GO enrichment of genes inferred to evolve under positive selection in genome-wide PAML site-model scans: [Well Supported].**  
  Across 6,698 12-species orthologs under M7/M8 (95% BEB cutoff), gene counts range from 468 (PRANK) and 817 (AMAP) to 1,290 (T-Coffee), with 36% of candidate genes detected by only a single aligner and only 22% shared across the five non-PRANK aligners (Figure 2, Table 1). Even among the top 100 genes ranked by LRT statistic, average pairwise overlap between aligners is only 54%, and significant level-3 Biological Process GO terms vary from 1 (AMAP) to 15 (MUSCLE).

* **Standard post-alignment quality controls—such as removing all gapped columns (`cleandata=1`), restricting to closely related species (*melanogaster* group), or applying divergence masking and trimming—do not eliminate aligner sensitivity or misalignment artifacts: [Well Supported].**  
  Removing gaps (`cleandata=1`) still leaves gene counts varying nearly fourfold across aligners (Table 1e,f) and introduces ~30% newly significant genes not called in the full alignment. In the 6-species *melanogaster* group, Consortium masking and trimming reduce total positives by 60%–80%, yet visual inspection of 25 genes significant at 1% FDR still identifies 12/25 (48%) as driven by misaligned codons.

* **Sites inferred to be under positive selection are heavily concentrated near indels, exon boundaries, and intrinsically disordered regions: [Well Supported].**  
  Automated genome-wide screens across all 6,698 12-species alignments confirm that ~85% of inferred positively selected sites lie within 10 amino acids of an indel transition, 35%–41% of candidate genes have a selected site within 15 amino acids of an annotated exon border, and 61%–85% of selected sites fall within IUPred-predicted disordered regions (score $\ge 0.5$, compared to 45%–50% background expectation).

* **Codon-aware PRANK substantially reduces false positives while retaining true positives, but still suffers from a 50%–55% false positive rate, and 48%–82% of positive selection calls across all aligners are false positives: [Moderately Supported].**  
  PRANK (`-codon`) reduces the number of genes called under positive selection by 43%–77% relative to the other five aligners while recovering all 8 visually validated true-positive genes from the 83-gene inspection set. However, the exact false-positive percentages (48%–82% and 50%–55%) are derived from unblinded visual scoring of small subsamples ($n = 20$ random PRANK genes; $n = 25$ masked 6-species genes) where "presence of runs of divergent sites at the protein level or of gaps that were placed differently by the five aligners" was used to label sites as misaligned false positives. Because genuine adaptive diversification in disordered, indel-prone regions also produces divergent runs and aligner disagreement, visual ambiguity in an alignment is proof of *unreliable codon homology*, not proof that $\omega \le 1$ across the true evolutionary history of that region.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Separate "Unreliable Alignment / Non-Homologous Codons" from "Absence of Positive Selection" and Formalize Visual Scoring Criteria
* **WHY:** In the Abstract and Results, the authors equate visually ambiguous alignments ("runs of divergent sites at the protein level or of gaps that were placed differently by the five aligners") with "false positives" of positive selection. Because aligner disagreement is one of the criteria used to define a site as a false positive, evaluating aligner consistency against this visual standard introduces circularity, and genuinely fast-evolving adaptive regions with indels are automatically scored as false positives.
* **WHAT:** Reframe the 48%–82% (and 50%–55% PRANK) figures as the *proportion of positive selection calls compromised by unreliable codon alignment or misannotation*, and report an objective, reproducible quantitative metric alongside the visual inspection.
* **HOW:** Formalize the visual inspection categories (`M`, `~M`, `OK`) with explicit quantitative rules (e.g., T-Coffee CORE score threshold, local window amino acid identity $< X\%$, or gap shift across aligners) so that the classification can be executed programmatically across all 6,698 genes, and blind the human scorer to which aligner generated the alignment when comparing PRANK (`n = 20`) against the other five aligners (`n = 83`).

#### 2. Decouple Codon vs. Amino-Acid Alignment Space in the PRANK Comparison
* **WHY:** AMAP, ClustalW, MUSCLE, ProbCons, and T-Coffee were run on translated amino acid sequences and back-threaded into codons via BioPerl, whereas PRANK was run directly on nucleotide triplets using `-codon` (Methods, line 30). Thus, the comparison confounds PRANK's phylogeny-aware gap-opening algorithm with codon-level vs. amino-acid-level alignment scoring.
* **WHAT:** Run PRANK in amino-acid mode (`+F` with back-translation to codons) on a subset of genes (or the 83 visually inspected genes) to determine how much of PRANK's reduction in false positives stems from its evolutionary gap placement versus direct codon-model scoring.
* **HOW:** Align the 83-gene inspection set (or the full 12-species set) using `prank -translate` / amino-acid mode with back-threading, run PAML M7/M8, and compare the resulting gene and site counts against `prank -codon` and the five amino-acid aligners.

#### 3. Correct the Null Distribution Used for Storey's FDR $q$-Value Estimation
* **WHY:** In the Methods (line 41), the authors state that $p$-values for M1a/M2a and M7/M8 were computed from $\chi^2_2$, producing a U-shaped $p$-value histogram that required bootstrap estimation of $\pi_0$. Because the null hypothesis fixes the boundary parameter ($p_1 = 0$ or $\omega_s = 1$), a large fraction of strictly purifying genes have $\text{LRT} = 0$ ($p = 1.0$), creating a point mass at $p = 1$ that violates the continuous uniform null assumption of Storey's $q$-value estimator and inflates $\hat{\pi}_0$.
* **WHAT:** Compute FDR $q$-values after accounting for the point mass at $\text{LRT} = 0$ (or by using the standard mixture distribution / filtering out $\text{LRT} = 0$ genes into the null proportion).
* **HOW:** Re-calculate the $p$-values and $q$-values in Tables 2 and 3 using either the empirical simulation null from the *Drosophila* 12 Genomes Consortium or by setting $\pi_0$ via the continuous interior $p$-value distribution ($p \in (0, 1)$) following Pounds and Cheng (2006) for discrete/boundary-inflated one-sided tests.

#### 4. Benchmark the Proposed Neighborhood-$\omega$ Filter Across All Six Aligners
* **WHY:** In the Discussion (line 9 of the second section), the authors briefly mention a promising heuristic filter on the *melanogaster*-group unmasked T-Coffee alignments: requiring all codons within $\pm 10$ sites of a candidate site to have PAML $\omega \le 0.5$ and $\omega + \text{SE} \le 1.0$, which reduced false positives to 3/25 (12%). However, this filter is introduced only as an anecdote in the Discussion rather than evaluated systematically in the Results.
* **WHAT & HOW:** Apply this $\pm 10$-codon neighborhood-$\omega$ filter across all six aligners (including PRANK) on both the 6-species and 12-species datasets, and add a summary table reporting the resulting gene counts and cross-aligner overlap percentages (analogous to Figure 2 and Table 1).
