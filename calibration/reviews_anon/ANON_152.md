# Forensic Scientific Peer Review: ANON_152

**Overall Score:** **5.8 / 10.0** (Mixed / Salvageable)
* **Score Breakdown:** Rigor: 1.7/3.5 | Claims: 1.3/2.5 | Biology: 1.5/2.0 | Reproducibility: 1.3/2.0

---

## 1. Executive Summary & Synthesis

This manuscript investigates the evolutionary origin of the SARS-CoV-2 Spike protein and its human ACE2 (hACE2) receptor-binding motif (RBM) through comparative sequence, recombination (`SimPlot v3.5.15`, `RIP`), selection (`SNAP`), and structural modeling (`Chimera`, `I-TASSER`, `ICM` on PDB `6M0J` and `2AJF`) analyses of 43 sarbecovirus genomes (including SARS-CoV-2 Wuhan-Hu-1, bat virus RaTG13, Guangdong pangolin CoV `Pan_SL-CoV_GD`, and Guangxi pangolin CoV `Pan_SL-CoV_GX`) and 6,400 early human SARS-CoV-2 sequences from GISAID. The authors report two primary findings: (1) while RaTG13 is closest to SARS-CoV-2 across most of the genome (96.1% nucleotide identity), `Pan_SL-CoV_GD` is substantially closer to SARS-CoV-2 within the RBM at the amino acid level (98.6% identity, differing by only 1 of 74 residues, Q498H, vs. 17 differences in RaTG13) and forms a localized phylogenetic cluster with SARS-CoV-2 between S-gene breakpoints, which the authors interpret as cross-species recombination transferring a pangolin CoV RBM into an RaTG13-like bat progenitor; and (2) strong purifying selection ($\omega = d_N/d_S \ll 1$) acts across sarbecovirus genomes, particularly in Spike S2 ($\omega = 0.013$) and structural proteins E and M, maintaining functional structural constraints even across divergent clades.

The structural comparisons of hACE2 interface contacts (positions 486, 493, 498, 501, and salt bridge K417–D30) and the empirical demonstration of localized genealogical discordance across the S1/RBM region are informative. However, the evolutionary inference and quantitative selection analyses exhibit three significant methodological limitations:

1. **Unidentifiable Directionality of RBM Recombination vs. Ancestral Lineage Sorting + Diversifying Selection:** The authors conclude that an RaTG13-like ancestor acquired its functional hACE2-binding RBM directly from a `Pan_SL-CoV_GD`-like pangolin donor (Abstract line 8, Results lines 43 and 51). However, within the RBM segment (nucleotides 22,553–23,128), the nucleotide divergence between SARS-CoV-2 and `Pan_SL-CoV_GD` is still substantial (**13.9%**, matching typical genome-wide synonymous divergence between their respective lineages), whereas their amino acid divergence is 1.4% (1/74 residues). A genuine recent cross-species recombination transfer of the RBM from `Pan_SL-CoV_GD` into the immediate ancestor of SARS-CoV-2 would reduce *synonymous* divergence ($d_S$) within the recombinant tract relative to flanking regions. Instead, as the authors' own `SNAP` cumulative plot (Fig. 3D) shows, synonymous substitutions accumulate steadily across the RBM between Wuhan-Hu-1 and `Pan_SL-CoV_GD`, while nonsynonymous substitutions plateau in Wuhan-Hu-1 vs. `Pan_SL-CoV_GD` and jump sharply in RaTG13. Thus, the data are equally (or better) explained by: (a) recombination in bat reservoirs where *RaTG13* acquired a divergent RBM from an non-ACE2-using bat sarbecovirus, or (b) ancestral retention of the hACE2-compatible RBM in the common ancestor of SARS-CoV-2 and `Pan_SL-CoV_GD` coupled with strong purifying selection on nonsynonymous sites and adaptive divergence along the RaTG13 branch. Without a formal coalescent time-tree (`BEAST`) or synonymous-divergence ($d_S$) breakpoint test, the direction and host polarity of the recombination event cannot be established.
2. **Flawed Pairwise `SNAP` (Nei-Gojobori) $d_N/d_S$ Averaging and Reciprocal $\omega$ Confusion:** To quantify purifying selection (Results line 56, Fig. 4B–C, Table S1), the authors compute pairwise Nei-Gojobori $d_N$ and $d_S$ in `SNAP` across non-independent tips of the phylogeny, filter out pairs with $d_S > 1$, and average the pairwise ratios. Pairwise averaging across a tree violates phylogenetic independence (pseudo-replicating internal branches), and the unweighted Nei-Gojobori estimator ignores transition/transversion rate bias ($\kappa$) and unequal codon frequencies—which severely biases $d_S$ downward and distorts $\omega$ in AT/transition-biased coronavirus genomes. Worse, in the Results ("Strong Purifying Selection Among SARS-CoV-2, Bat, and Pangolin Coronaviruses", line 56) and Fig. 4C, the authors define $\omega$ as the reciprocal ratio **$d_S/d_N$** (*"looking at all the dS/dN ratios ($\omega$), we observed that these ratios are much lower in the 5' end of the region, before codon 368... compared with the 3' end"*), directly inverting the standard definition $\omega = d_N/d_S$ used in Fig. 4B and Table S1.
3. **Synthetic Chimeric Assembly of `Pan_SL-CoV_GD/P1La` and Multiple Amino Acid / Accession Typos:** In the Methods (line 106), the reference genome `Pan_SL-CoV_GD/P1La` used throughout the recombination scans is constructed as an *in silico* hybrid merging partial sequences of `Pan_SL-CoV_GD/P1L` from one study (ref. 10) with raw SRA reads from a different study (BioProject `PRJNA573298`, mistyped as 8-digit `PRJNA5732983` on line 106). Splicing consensus sequences across distinct pangolin biological samples risks introducing artificial similarity shifts in `SimPlot`. Additionally, several key amino acid labels in the text and figure captions are inverted or misnumbered (e.g., line 43 reports *"L486F and Y493Q"* instead of F486L; Fig. 3C caption line 49 states *"H in RaTG13, bottom"* at residue 498, whereas RaTG13 carries Y498 and `Pan_SL-CoV_GD` carries H498; Discussion line 85 refers to *"conserved residue F498's hydrophobic interaction"* with hACE2 M82, which is actually F486).

---

## 2. Claim-by-Claim Audit

### Claim 1: SARS-CoV-2 acquired its functional hACE2-binding RBM via cross-species recombination from a `Pan_SL-CoV_GD`-like pangolin coronavirus into an RaTG13-like bat virus ancestor.
* **Support Level:** `[Overstated]`
* **Evidence & Technical Critique:**
  - While `SimPlot` (Fig. 2A), `RIP` (Fig. S2A), and localized ML trees (Fig. 1C, Fig. 2B) confirm that the RBM shows topological discordance relative to the rest of the Spike gene, topological clustering alone does not identify which lineage was the donor and which was the recipient.
  - Within the RBM (Fig. 1C), nucleotide divergence between Wuhan-Hu-1 and `Pan_SL-CoV_GD` remains 13.9% (indicating decades of evolutionary separation), and Fig. 3D shows high cumulative $d_S$ between Wuhan-Hu-1 and `Pan_SL-CoV_GD` across the RBM. This pattern is fully consistent with RaTG13 being the recombinant (having acquired a divergent bat RBM) or with ancestral polymorphism in bats combined with strong purifying selection preserving the ancestral amino acid sequence in both the SARS-CoV-2 and `Pan_SL-CoV_GD` lineages. Claiming unidirectional pangolin-to-bat/human transfer of the RBM overstates what similarity plots and amino acid identity can resolve.

### Claim 2: Strong purifying selection ($\omega = d_N/d_S$ from 0.013 in S2 to 0.145 across genes) operates across SARS-CoV-2, RaTG13, and pangolin CoVs, and within the RBD, purifying selection is stronger in the 3' RBM region (after codon 368) than in the 5' core region.
* **Support Level:** `[Fragile]`
* **Evidence & Technical Critique:**
  - Genome-wide purifying selection in sarbecoviruses is biologically indisputable, and the stark contrast between cumulative $d_S$ and $d_N$ across the RBM between Wuhan-Hu-1 and `Pan_SL-CoV_GD` (Fig. 3D) supports strong functional constraint on RBM residues.
  - However, relying on pairwise Nei-Gojobori `SNAP` averages across non-independent tips without branch-specific maximum-likelihood codon models (`PAML` `codeml` or `HyPhy` `BGM`/`BUSTED`/`FEL`/`RELAX`) is statistically flawed, and the text on line 56 + Fig. 4C confuses $d_S/d_N$ with $\omega = d_N/d_S$. Moreover, averaging pairwise ratios across deep clades where $d_S$ approaches saturation (arbitrarily truncating at $d_S > 1$) biases regional comparisons.

### Claim 3: Five critical RBM residues (F486, Q493, Q498/H498, N501, and RBD salt-bridge K417) stabilize the hACE2 interface in SARS-CoV-2 and `Pan_SL-CoV_GD`, whereas substitutions in RaTG13 (F486L, Q493Y, Q498Y, N501D) and `Pan_SL-CoV_GX` disrupt key hydrophobic and hydrogen-bonding networks.
* **Support Level:** `[Well Supported]`
* **Evidence & Technical Critique:**
  - The structural analysis of the crystal structure (`6M0J`) and comparative homology models (Fig. 3A–C) accurately identifies the physical interactions at the hACE2 interface: F486 inserting into the hydrophobic pocket formed by hACE2 L79, M82, and Y83; Q493 hydrogen-bonding with hACE2 K31 and E35; and Q498/H498 interacting with D38, Y41, Q42, and K353. The manuscript should, however, fix the text typos on lines 43, 49, and 85 where residue numbers and identities (F486 vs. F498; H498 in `Pan_SL-CoV_GD` vs. Y498 in RaTG13) are mislabeled.

### Claim 4: Early human SARS-CoV-2 evolution (6,400 GISAID genomes through April 2020) is dominated by rare variants except for the globally rising D614G substitution, and the furin cleavage site (681-PRRA-684) is completely conserved across human isolates.
* **Support Level:** `[Well Supported]`
* **Evidence & Technical Critique:**
  - The mutational frequency survey of the 6,400 early human Spike sequences (Fig. S4) accurately captures the rapid global sweep of D614G (`A23403G`) and the conservation of the polybasic S1/S2 cleavage motif among circulating clinical sequences in early 2020.

---

## 3. Concrete Actionable Recommendations

1. **Test Recombination Polarity Using Synonymous Divergence ($d_S$) and Coalescent Time-Trees:**
   - Formally run `RDP4`/`RDP5` (incorporating `3Seq`, `BOOTSCAN`, `MaxChi`, and `Chimaera` with multiple-testing correction) and estimate region-specific maximum-likelihood $d_S$ trees (or `BEAST` molecular clock trees on 3rd codon positions) separately for the non-recombinant Spike backbone and the RBM tract (nt 22,553–23,128).
   - Explicitly test whether the RBM discordant topology is driven by a recent coalescent node between SARS-CoV-2 and `Pan_SL-CoV_GD` (low $d_S$) or by recombinant divergence along the *RaTG13* lineage combined with purifying selection on amino acids in SARS-CoV-2 and `Pan_SL-CoV_GD`. Reframe the Abstract and Discussion to acknowledge that the donor/recipient directionality cannot be fixed to pangolin $\to$ bat/human without unsampled bat reservoir lineages.
2. **Replace Pairwise `SNAP` Averages with Phylogenetic Codon Substitution Models and Fix the $d_S/d_N$ Inversion:**
   - Replace pairwise Nei-Gojobori `SNAP` averages with maximum-likelihood codon models (`PAML` `codeml` or `HyPhy` `SLAC`/`FEL`/`RELAX`) fitted on each non-recombinant partition's phylogeny, accounting for transition/transversion bias ($\kappa$) and codon equilibrium frequencies.
   - Standardize $\omega = d_N/d_S$ throughout the manuscript and fix line 56 and Fig. 4C where $\omega$ is inconsistently defined as $d_S/d_N$.
3. **Validate Results Without the Chimeric `Pan_SL-CoV_GD/P1La` Consensus Assembly:**
   - Repeat the `SimPlot` and RBM tree analyses using only single-isolate, unmerged assemblies from individual studies (rather than splicing `Pan_SL-CoV_GD/P1L` with reads from `PRJNA573298`) to verify that no breakpoint artifacts were introduced by cross-sample chimerism.
4. **Correct Residue, Caption, and Accession Errors:**
   - Line 43: Change *"L486F"* to *"F486L"* (matching Wuhan-Hu-1 $\to$ RaTG13 polarity).
   - Line 49 (Fig. 3C caption): Correct *"H in RaTG13, bottom"* to state that H498 is in `Pan_SL-CoV_GD` (and Y498 is in RaTG13).
   - Line 62 (Fig. 4 caption): Fix typo *"Wuahn-Hu-1"* $\to$ *"Wuhan-Hu-1"*.
   - Line 85: Change *"conserved residue F498's hydrophobic interaction"* to *"conserved residue F486's hydrophobic interaction"*.
   - Line 106: Fix BioProject accession typo `PRJNA5732983` $\to$ `PRJNA573298`.
