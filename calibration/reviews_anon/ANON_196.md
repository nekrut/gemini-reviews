# Review of ANON_196

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **9.2 / 10.0** (Exemplary)  
* **Score Breakdown:** Rigor: 3.1/3.5 | Claims: 2.3/2.5 | Biology: 1.9/2.0 | Reproducibility: 1.9/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript investigates the genome-wide impact of viruses on adaptive protein evolution across humans and mammals. The authors manually curated 1,256 host proteins that physically interact with viral proteins, RNA, or DNA (virus-interacting proteins, VIPs) from low-throughput virology studies, embedded within a set of 9,861 orthologous coding sequences conserved across 24 mammalian genomes. Combining polymorphism data from humans (1000 Genomes African populations) and non-human great apes (Great Ape Genome Project) with divergence across 24 mammals, the authors show that: (1) VIPs experience 21–25% stronger purifying selection (lower $p_N/p_S$) than non-VIPs across virtually all Gene Ontology (GO) categories, partly reflecting their role as broadly expressed protein-protein interaction hubs; (2) despite this heightened constraint, VIPs exhibit a marked excess of adaptive nonsynonymous substitutions in the human lineage under both the classic McDonald-Kreitman (MK) test ($\alpha = 0.19$ vs. $-0.02$, $P = 2 \times 10^{-5}$) and a modified low-frequency asymptotic MK test ($\alpha = 27\%$ vs. $\sim 9\%$), accounting for nearly 30% of all adaptive amino acid substitutions in the conserved human proteome; (3) across the 24-mammal phylogeny, branch-site tests (HyPhy `BS-REL` and `BUSTED`) matched for purifying selection reveal a 2-fold to 6-fold excess of positive selection in VIPs across mammalian clades and non-immune housekeeping functions, with Hepatitis C Virus (which lacks known close non-human mammalian relatives) serving as a natural negative control; and (4) an in-depth structural and phylogenetic analysis of the non-immune coronavirus receptor aminopeptidase N (`ANPEP`) across 84 mammals (`MEME` + PDB `4FYQ`) demonstrates strong enrichment of episodic positive selection at the viral contact interface, including 11 independent parallel losses of the host-tropism N-glycosylation motif (`NX[ST]` at porcine residue 736 / human 739). All alignments, VIP curation tables, SLiM simulation outputs, and `BS-REL`/`BUSTED` statistics are publicly archived on Dryad (`10.5061/dryad.fs756`).

This is an ambitious, carefully controlled, and highly transparent evolutionary genomics study. The authors anticipate and test a wide range of potential confounders (GC content, CDS length, recombination rate, RNA and protein tissue expression breadth/level, Biogrid PPI degree, synteny conservation, and GO functional categories) and validate their modified asymptotic MK estimator using forward population genetic simulations (`SLiM`). The main methodological caveats—literature ascertainment bias in how intensively human genes are studied in low-throughput virology, one-at-a-time rather than simultaneous multivariate covariate matching, and an ad-hoc "permutation with a target average" algorithm that matches $p_N/p_S$ indirectly via $d_N$—do not overturn the central conclusions and can be addressed with straightforward supplementary checks.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Viruses preferentially interact with evolutionarily constrained host proteins ($p_N/p_S$ 21% lower in humans and 25% lower in great apes) across functional categories (Fig. 3): [Well Supported].**  
  The reduction in $p_N/p_S$ holds across all 10 major human viruses and 124 of 162 GO biological processes ($77\%$), and persists after matching for GC content, sequence length, recombination rate, GTEx RNA expression, Human Proteome Map protein expression, and GO category. Controlling for Biogrid PPI degree reduces the $p_N/p_S$ gap from 25% to 13%, showing that hub status partially—but not completely—explains the stronger purifying selection on VIPs.

* **VIPs—especially the 80% without known antiviral or immune functions—account for ~30% of adaptive amino acid substitutions in the conserved human proteome (Fig. 4): [Well Supported].**  
  In the human lineage, non-immune VIPs show $\alpha = 0.26$ vs. $0.02$ in non-VIPs ($P = 3 \times 10^{-7}$) under the classic DAF $> 10\%$ MK test. To overcome downward bias from slightly deleterious variants and high-frequency SFS mispolarization, the authors fit a logarithmic asymptotic MK curve over $\text{DAF} \in [0, 0.5]$ (validated by `SLiM` simulations under bottlenecks, expansions, and varying selection coefficients in Supplementary file 1G), estimating $\alpha = 27\%$ (512/1,897 substitutions) in VIPs vs. $\sim 9\%$ (1,293/14,370) in non-VIPs ($512 / (512 + 1293) = 28.4\%$ of adaptive substitutions).

* **VIPs experience a 2- to 6-fold excess of recurrent positive selection across the mammalian phylogeny, except for VIPs interacting exclusively with HCV (Figs. 5–6): [Well Supported].**  
  Using `BS-REL` and `BUSTED` across 44 mammalian branches (restricted to 9,338 synteny-verified orthologs), VIPs show elevated proportions of positively selected codons across primates, glires, cetartiodactyls, and carnivores/horses (Fig. 5D). Crucially, the 109 VIPs interacting with HCV—the only major human virus among the top 10 lacking known close mammalian relatives—show no excess adaptation across mammals (Fig. 5B), providing an internal biological specificity control against generic gene-level confounders.

* **Parallel adaptive evolution and 11 independent losses of the N-glycosylation motif at the coronavirus binding interface of aminopeptidase N (`ANPEP`) across 84 mammals (Fig. 7): [Well Supported].**  
  Mapping `MEME` site-level episodic selection ($P \le 0.05$) onto the porcine ANPEP–TGEV/PRCV crystal structure (PDB `4FYQ`) shows sharp spatial decay of adaptive enrichment away from the 22-residue viral contact surface (Fig. 7C) and pinpoints recurrent adaptive substitutions at the first and third positions of the `NX[ST]` N-glycosylation consensus known experimentally to govern group I coronavirus host tropism.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Control for Literature Ascertainment Bias (PubMed Citation Depth per Gene) and Simultaneous Multivariate Confounders
* **WHY:** Because VIPs were curated by querying PubMed for `"[Gene Symbol] AND virus"` and inspecting low-throughput molecular biology papers, heavily studied human genes are much more likely to have a documented physical viral interaction than poorly studied genes. While the authors control for expression, PPI degree, length, GC content, recombination, and $p_N/p_S$ one covariate at a time, confounding factors can act jointly.
* **WHAT:** Test whether the excess of adaptation in VIPs (both human MK $\alpha$ and mammalian `BS-REL` selected codon proportion) holds when controlling for total PubMed citation count per gene and when matching multiple covariates simultaneously.
* **HOW:** For each of the 9,861 genes, record the total number of PubMed articles mentioning the HGNC symbol (independent of the word `"virus"`). Run a multiple regression or propensity-score matching model predicting VIP status from $\log(\text{PubMed count})$, $\log(\text{PPI degree} + 1)$, GTEx tissue breadth, CDS length, GC content, recombination rate, and great ape $p_N/p_S$, and verify that MK $\alpha$ and `BS-REL` adaptation remain significantly elevated in VIPs vs. propensity-matched non-VIPs.

#### 2. Replace or Benchmark the Ad-Hoc "Permutation with a Target Average" ($a = 0.7, X = 3$) Against Direct Stratified / Quantile Matching
* **WHY:** In Materials and Methods (*"Permutations with a target average"*, lines 88–100), to match VIPs and non-VIPs on great ape $p_N/p_S$, the authors sample non-VIPs by targeting a mammal-wide $d_N$ interval $[0.95 a \, d_{N(\text{vip})}, 1.05 a \, d_{N(\text{vip})}]$ while injecting a completely random gene every $X$ steps, tuning $a = 0.7$ and $X = 3$ by trial and error. Because $d_N$ is part of the `BS-REL` / `BUSTED` likelihood target, conditioning the non-VIP control pool on having 30% lower mammal-wide $d_N$ ($a = 0.7$) risks mechanically depleting high-$d_N$ adaptively evolving genes from the non-VIP control set.
* **WHAT:** Verify that the mammalian `BS-REL` / `BUSTED` adaptation excess holds when matching non-VIPs directly on great ape $p_N/(p_S + 1)$ quantiles (or synonymous polymorphism density $p_S$ + PPI degree + GTEx expression breadth, which predict constraint without using mammal-wide $d_N$).
* **HOW:** Divide all genes with $\ge 5$ great-ape polymorphic sites into 20 quantile bins of $p_N/(p_S + 1)$ (or match directly on PPI degree and tissue expression breadth), sample non-VIPs matching the exact bin distribution of VIPs without referencing mammal-wide $d_N$, and plot the resulting excess-of-adaptation curve alongside Fig. 5A (and alongside the conservative $d_N/d_S$-matched curve where $a = 0.97$, which already showed a 39% excess).

#### 3. Clarify the Contrast Between Immune VIPs in the Human MK Test vs. the Mammalian `BS-REL` Test
* **WHY:** In the human lineage classic MK test (Fig. 4B, line 117), immune VIPs ($n = 241$) show no excess adaptation over immune non-VIPs ($\alpha \approx 0.05$ for both), whereas across the 24-mammal phylogeny (Fig. 5C, line 164), immune VIPs show a strong (>100%) excess of adaptation over immune non-VIPs. This divergence between the two evolutionary timescales is striking and deserves explicit discussion.
* **WHAT & HOW:** Add a short paragraph in Results (line 164) or Discussion explaining why immune VIPs vs. immune non-VIPs differ between the human MK test and mammalian `BS-REL` (e.g., whether immune non-VIPs such as extracellular cytokines/receptors experience rapid positive selection or balancing selection in the recent human/great-ape lineage that inflates $p_N$ and depresses MK $\alpha$, whereas `BS-REL` measures episodic $d_N/d_S > 1$ across deep mammalian branches).

#### 4. Technical, Mathematical, and Editorial Cleanup
* **WHY:** Several minor numerical and cross-reference typos appear in the text.
* **WHAT & HOW:**
  * **Line 110:** The baseline non-VIP $\alpha$ without control is written inconsistently as `"−0.02 without control"` in five places and `"0.02 without control"` in six places within the same paragraph. Standardize to `−0.02` (matching line 106).
  * **Line 117:** Change `"Figure 2B"` to `"Figure 4B"`.
  * **Line 137:** Fix truncated $P$-value `"permutation test p<for VIPs and non-VIPs"` to `"p < 10^{-5} for VIPs and non-VIPs"`.
  * **Page 2, Line 17 (Materials and Methods header):** Fix typo `"Materials and Mmethods"` to `"Materials and Methods"`.
  * **Page 2, Line 100:** Fix `"in non-VIPs compared to non-VIPs"` (appears twice) to `"in non-VIPs compared to VIPs"`.
