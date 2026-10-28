# Review of PMC7721162 (PMID:33206635)

**Manuscript Title:** Stability of SARS-CoV-2 phylogenies  
**Authors:** Turakhia Y, De Maio N, Thornlow B, Gozashti L, Lanfear R, Walker CR, Hinrichs AS, Fernandes JD, Borges R, Slodkowicz G, Weilguny L, Haussler D, Goldman N, Corbett-Detig R.  
**Journal / Preprint:** *PLoS Genet* (2020; `PMC7721162` / `PMID:33206635` / `10.1371/journal.pgen.1009175`)  
**Calibration Study Cohort:** Cohort B — Validated Control (`B10` | Double-Blinded as `ANON_40`)  
**Overall Score:** **9.1 / 10.0** (Exemplary)  
* **Score Breakdown:** Rigor: 3.2/3.5 | Claims: 2.3/2.5 | Biology: 1.8/2.0 | Reproducibility: 1.8/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript investigates the prevalence and phylogenetic impact of systematic laboratory-associated sequencing and bioinformatic errors in public SARS-CoV-2 genome repositories, alongside methods for quantifying and visualizing topological instability across large viral phylogenies. Analyzing 31 Nextstrain builds between March 23 and April 30, 2020 (focusing on the April 19 dataset containing 3,246 variant sites across ~4,200 genomes) and the April 24, 2020 COG-UK phylogeny, the authors introduce automated algorithms to detect "extremal" homoplastic sites (exceptional parsimony score relative to $\log_2$ alternate allele count) and lab-associated variants (sites with parsimony score $\ge 4$ where $>80\%$ of alternate alleles originate from a single de-duplicated originating/submitting lab with Fisher's exact $p < 0.01$). They identify 16 strongly lab-associated variants that lack the biological $C \to U$ transition bias of genuine SARS-CoV-2 recurrent mutations ($1/16$ vs. $49\%$ genome-wide, $P < 0.0005$), significantly co-localize with ARTIC PCR primer binding sites ($P = 0.028$, permutation test) or Nanopore adapters/human rRNA reads, and distort local phylogenetic relationships as well as apparent back-mutation rates at other sites (confirmed via 81 synthetic error-injection experiments in IQ-TREE 2). In the second half of the paper, they develop an entropy-weighted matching split distance metric and a fast tanglegram node-rotation heuristic (`RotTrees`), showing that while daily Nextstrain topologies drift over time as sample composition changes (Mantel $r = -0.384, P = 4 \times 10^{-5}$), major backbone clades are stable across Nextstrain consensus, masked IQ-TREE 2, and COG-UK phylogenies. All software tools (`strain_phylogenetics`, `COVID-19-Lab-Specific-Bias-Filter`), UCSC Genome Browser tracks, and live VCF masking lists (`ProblematicSites_SARS-CoV2`) are publicly available.

This is a highly practical and rigorously validated methodological contribution that directly improved quality control across global SARS-CoV-2 genomic surveillance. The combination of forensic root-cause identification (linking specific recurrent variants to ARTIC primer coordinates, Oxford Nanopore adapter sequences at 24,389–24,390, and human rRNA misalignment at 22,802) and controlled synthetic error-addition experiments provides compelling proof of how non-random errors mimic convergent evolution or recombination. Only minor methodological caveats and text inconsistencies need attention—namely, reconciling the parsimony score cutoff (`>= 4` vs. `> 4`) between the Results and Methods sections, and addressing how tree-conditioned parsimony scores behave when strongly correlated multi-site errors collapse unrelated samples into a single clade with parsimony score $< 4$.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **A subset of highly recurrent variants in public SARS-CoV-2 assemblies are systematic laboratory or bioinformatic artifacts rather than genuine biological homoplasies: [Well Supported].**  
  The 16 flagged lab-associated variants (>80% of alternate alleles from a single lab, Fisher's exact $p < 0.01$) are severely depleted for the characteristic SARS-CoV-2 $C \to U$ mutational signature ($1/16$ vs. $42/50$ among non-lab-associated low-frequency recurrent sites, $P \approx 10^{-7}$), are significantly closer to ARTIC V3 primer binding sites than expected by chance ($P = 0.028$, 10,000 permutations; Figure 3), and trace in specific instances to Oxford Nanopore adapter sequence homology (`A24389C`/`G24390C`) or human rRNA read misincorporation (`C22802G`).

* **Lab-associated variants distort local clade topologies and induce spurious forward/backward homoplasies at unlinked biological sites: [Well Supported].**  
  Masking the 16 lab-associated variants improves the IQ-TREE 2 alignment fit, eliminates apparent back-mutations at genuine polymorphic sites such as `C14408U` (Figure 5), and repositions locally affected samples (Figure S2). Conversely, experimentally injecting single or paired synthetic errors into 10, 25, or 50 Australian or French genomes (54 single-site and 27 paired-site IQ-TREE 2 experiments; Figure 4) reproduces the empirical log-linear relationship between alternate allele count and parsimony score and increases the apparent parsimony score at other, unmanipulated sites in 50/54 experiments (by 2–44 events).

* **Recurrent mutations not associated with a single laboratory are predominantly driven by host-mediated $C \to U$ hypermutation purified by negative selection: [Well Supported].**  
  Among 50 bi-allelic, non-lab-associated recurrent sites with frequency $< 0.01$ and parsimony score $> 3$, 84% (42/50) are $C \to U$ transitions ($P = 3.66 \times 10^{-7}$), enriched in `5'-[U|A]C>U` sequence contexts ($P = 0.0501$), corroborated across multiple sequencing platforms (81.4%), unassociated with ARTIC primer proximity ($P = 0.785$), and skewed toward higher recurrence at synonymous than non-synonymous sites ($P = 0.0553$, Wilcoxon test; Figure 7B).

* **While daily Nextstrain topologies vary over time as sample sets change, major higher-level clades are consistent across Nextstrain consensus, masked ML, and COG-UK trees: [Well Supported].**  
  Using the normalized entropy-weighted matching split distance ($S_p(T, T')$) across 31 Nextstrain trees pruned to 468 shared tips, the authors demonstrate a temporal trajectory in MDS space correlated with sample overlap (Mantel $r = -0.384, P = 4 \times 10^{-5}$; Figure 10), while showing high Jaccard similarity for large clades ($\ge 200$ tips) and a low normalized distance ($S_p = 0.12$ across 4,172 tips; Figure 12C) between the error-masked phylogeny and the COG-UK backbone tree.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Mitigate Circular Tree Conditioning When Detecting Correlated Multi-Site Lab Errors
* **WHY:** As the authors demonstrate in their paired-error injection experiments (Figure 4C,F) and with the linked `A24389C`/`G24390C` Nanopore adapter artifact, when two or more correlated systematic errors are introduced simultaneously into a subset of sequences, maximum likelihood tree builders group the erroneous sequences together into a single artificial clade. Because the lab-bias filter pre-screens only sites with parsimony score $\ge 4$ (or $> 4$) conditioned on the unmasked tree, strongly correlated multi-site errors (or errors in low-diversity regional subtrees) can pull all affected samples into 1–3 clades, yielding a parsimony score $\le 3$ and escaping the initial parsimony filter.
* **WHAT:** Add a tree-independent pre-screen for linked/clustered lab-specific variants (e.g., pairs of variants within $< 50\text{ bp}$ or in high linkage disequilibrium $r^2 > 0.5$ where $>80\%$ of carriers come from a single submitting/originating lab) regardless of whether their initial tree-conditioned parsimony score exceeds 4.
* **HOW:** In `COVID-19-Lab-Specific-Bias-Filter`, compute the lab-proportion and Fisher's exact test across all non-singleton variants (parsimony score $\ge 2$) that either (a) lie within $\pm 15\text{ bp}$ of an ARTIC primer or (b) occur within $10\text{ bp}$ of another variant in the same samples, and flag them prior to initial tree construction.

#### 2. Account for Phylogenetic Autocorrelation (Local Transmission Chains) in the Lab-Association Fisher's Exact Test
* **WHY:** As noted in the Methods ("Discovery of lab-associated variants"), applying Fisher's exact test to allele counts by submitting lab assumes samples are independent. When a single regional laboratory sequences a dense local outbreak or transmission chain, genuine lineage-defining or locally recurrent mutations will be heavily enriched in that laboratory's submissions, potentially triggering a false-positive lab-association flag if the variant also experiences 2–3 genuine homoplasies elsewhere.
* **WHAT:** Replace the sample-level contingency count in Fisher's exact test with a clade-level (independent mutation event) count on the phylogeny.
* **HOW:** Instead of counting individual *tips* carrying the alternate allele per lab, count the number of independent *parsimony-inferred mutation events (subclades)* attributable to that lab versus all other labs, and flag a site when $>80\%$ of independent *emergence events* (rather than tip counts dominated by a single large local clade) occur in sequences from a single lab.

#### 3. Reconcile Parsimony Cutoff Inequalities and Typographical Details Between Text and Methods
* **WHY:** Inconsistent inequality signs (`>= 4` vs. `> 4` vs. `> 3`) across sections make it unclear whether parsimony score 4 is included in the lab-associated variant screen.
* **WHAT & HOW:**
  1. **Results ("SARS-CoV-2 data contains many lab-associated variants") vs. Methods ("Discovery of lab-associated variants"):** In Results, the text states *"we extracted the set of sites with parsimony score 4 or more"* (and cites `A24389C` as having a parsimony score of 4), whereas in Methods it states *"we first filtered variants with parsimony score greater than 4"*. Change `"greater than 4"` in the Methods to `"4 or greater ($\ge 4$)"` so that it matches the inclusion of `A24389C` (parsimony score = 4).
  2. **Methods ("A clade comparison method using branch splits"):** In the definition of the best-matching splits set, fix the typo in the first argument of `M(b,T’,T’)` to `M(b,T,T’)` (matching the next sentence `every reduced split in M(b,T,T’)`).
  3. **Results ("Improvements and updates..."):** Remove the duplicated word `here` in `"Here, we list here a few of the key improvements"`.
