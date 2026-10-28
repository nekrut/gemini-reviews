# Review of PMC3395634 (PMID:22807683)

**Manuscript Title:** Detecting individual sites subject to episodic diversifying selection  
**Authors:** Murrell B, Wertheim JO, Moola S, Weighill T, Scheffler K, Kosakovsky Pond SL.  
**Journal / Preprint:** *PLoS Genet* (2012; `PMC3395634` / `PMID:22807683` / `10.1371/journal.pgen.1002764`)  
**Calibration Study Cohort:** Cohort B — Validated Control (`B19` | Double-Blinded as `ANON_08`)  
**Overall Score:** **9.1 / 10.0** (Exemplary)  
* **Score Breakdown:** Rigor: 3.3/3.5 | Claims: 2.3/2.5 | Biology: 1.8/2.0 | Reproducibility: 1.7/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript introduces the Mixed Effects Model of Evolution (MEME), a codon-based phylogenetic likelihood framework designed to detect episodic and pervasive diversifying positive selection at individual codon sites without requiring *a priori* specification of foreground branches. At each site, MEME estimates a site-specific synonymous substitution rate ($\alpha$, a fixed effect) and treats the branch-specific nonsynonymous substitution rate ($\beta$) as a two-category random effect ($\beta^- \le \alpha$ with weight $q^-$ and unrestricted $\beta^+$ with weight $q^+ = 1 - q^-$), marginalizing over all $2^B$ branch assignments in $O(B)$ operations via Felsenstein's pruning algorithm with branch-level mixture transition matrices $P_b(t_b) = q^- e^{Q(\beta^-)t_b} + (1 - q^-) e^{Q(\beta^+)t_b}$. Using parametric bootstrap simulations across empirical TreeBase topologies and 16 benchmark protein-coding alignments ($N = 17\text{ to }476$ taxa), the authors calibrate the non-standard boundary likelihood ratio test (LRT) statistic against a $\chi^2_1 / \chi^2_2$ mixture distribution, compare Type I error and power against Fixed Effects Likelihood (FEL), evaluate Empirical Bayes (EB) branch-site localization, and demonstrate that MEME identifies 237 positively selected sites across the 16 datasets compared to 63 found by FEL (including 56 sites where FEL inferred overall purifying selection because episodic bursts were masked by strong background constraint).

This is an exemplary methodological and empirical contribution. The mathematical derivation showing that independent branch-level random effects factorize cleanly inside Felsenstein's pruning recursion is exact, the simulation design tests both worst-case neutral nulls ($\omega = 1$ across all branches) and composite nulls, and the authors provide a remarkably candid assessment of the "selection inference uncertainty principle" (showing via simulation in Figure S2/S3 why Empirical Bayes identification of individual branches at a single site has high false-positive rates on neutral backgrounds and should only be used for data exploration). Only minor modeling caveats exist: (1) MEME assumes that single-nucleotide substitutions are the only instantaneous codon transitions ($q_{ij} = 0$ when $\delta(i,j) > 1$), which can yield false positives when multinucleotide mutations (tandem substitutions on a single branch) mimic a high-$\beta^+$ burst on a single short branch; and (2) branch lengths $t_b$ and nucleotide substitution parameters $\theta$ are fixed at their global MG94xGTR values from Stage 1 without propagating uncertainty. Addressing how multinucleotide hits or extreme single-branch outliers affect $\beta^+$ in the Discussion will make the work even stronger.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Marginalizing over $2^B$ independent branch-level $\omega$ configurations is exact and computationally tractable via mixture transition matrices in Felsenstein's pruning algorithm: [Well Supported].**  
  Equations (1) and (2) rigorously establish that when branch category assignments $C_b \in \{1 \dots K\}$ are independent across branches, the sum over $K^B$ configurations commutes with the post-order tree traversal by replacing each branch transition probability matrix $e^{Q_b t_b}$ with the mixture $\sum_{k=1}^K q_k e^{Q(\omega_k) t_b}$.

* **MEME controls Type I error under the worst-case neutral null ($\omega^- = \omega^+ = 1$) and achieves substantially higher power than FEL when selection is episodic ($q^+ \in \{0.10, 0.25, 0.50\}$): [Well Supported].**  
  Because testing $\beta^+ = \alpha$ under the null leaves $q^+$ unidentifiable when $\beta^- = \beta^+ = \alpha$ and places $\beta^-$ on the boundary $\beta^- \le \alpha$, standard Wilks' theorem regularity conditions fail. The authors calibrate the asymptotic null distribution via parametric bootstrap (Figure S1, Text S1) as a $\chi^2$ mixture, verify Type I error across sample sizes ($N = 16\text{ to }500$ taxa) and TreeBase divergences (Tables S1–S2), and demonstrate in Table 1 that when $10\%$ of branches experience diversifying selection ($\omega^+ \in \{4, 12, 36\}$) against a purifying background ($\omega^- \in \{0, 0.2, 0.4\}$), FEL has near-zero power ($0.00\text{--}0.04$) whereas MEME achieves up to $99\%$ power.

* **Across 16 empirical datasets, episodic positive selection is widespread and frequently masked by purifying selection in constant-$\omega$ site models: [Well Supported].**  
  Table 2 shows that across the 16 empirical alignments, MEME detects 51 of the 63 FEL-positive sites (with the remaining 12 having borderline MEME $p = 0.04\text{--}0.07$), plus 130 FEL-neutral sites ($M^+F^0$) and 56 FEL-negative sites ($M^+F^-$). The detailed case studies—such as vertebrate rhodopsin codon 210 ($\Delta\log L = 32.5$, $p < 0.0001$, where FEL infers $\omega < 1$ with $p = 0.017$ because $86\%$ of branches have $\beta^- = 0$ while $14\%$ diversify) and the resolution of the Yokoyama et al. (2008) taxon-sampling paradox (Table S20)—provide compelling biological validation.

* **Empirical Bayes (EB) identification of specific positively selected branches at a single site has limited power and high false-discovery risk on neutral backgrounds ("selection inference uncertainty principle"): [Well Supported].**  
  Rather than overselling the Empirical Bayes branch-site posterior (Equations in Section "Detecting individual branches"), the authors explicitly test it under simulation (Figures S2–S3, line 152) and show that when background branches evolve neutrally, $\ge 1$ background branch is falsely flagged ($\text{EBF} \ge 20$) at $52\%$ of sites, properly warning users to treat branch-level EBFs strictly as exploratory.

* **Vulnerability of unrestricted $\beta^+$ on a single very short branch ($q^+ \approx 1/B$) to multinucleotide substitutions or alignment/sequencing artifacts: [Moderately Supported].**  
  In the instantaneous rate matrix (line 36), codon substitutions requiring $>1$ nucleotide change have instantaneous rate $0$. Consequently, if a single codon undergoes a simultaneous double or triple nucleotide mutation along a short branch $t_b \ll 1$ (or contains a localized alignment/sequencing error on a terminal branch), the model can only explain 2–3 nonsynonymous nucleotide changes on a branch of length $t_b \approx 0.001$ by assigning that branch to $\beta^+$ with an extreme rate estimate (e.g., $\omega^+ = 6,726$ as seen at rhodopsin site 273 in line 205), producing a large LRT statistic from a single branch event. While this does not invalidate the model under its stated single-nucleotide Markov assumptions, discussing the sensitivity of MEME to single-branch multi-nucleotide hits is important for practitioners.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Discuss the Sensitivity of MEME to Single-Branch Multinucleotide Substitutions (Tandem Mutations) and Terminal-Branch Artifacts
* **WHY:** Because the codon model restricts instantaneous transitions to single nucleotides ($\delta(i,j) = 1$), a single branch carrying a 2- or 3-nucleotide change within the same codon along a short branch $t_b \rightarrow 0$ forces the likelihood of the single-rate null ($\beta^+ \le \alpha$) toward $O(t_b^4)$ or $O(t_b^6)$, whereas the alternative model can set $\beta^+ \propto 1/t_b$ (e.g., $\omega^+ > 1,000$) with weight $q^+ = 1/B$ to absorb the event on that single branch, generating a significant LRT from a single mutational event.
* **WHAT:** Add a brief paragraph in the Discussion noting that when $q^+$ corresponds to a single branch ($q^+ \approx 1/B$) and $\hat{\omega}^+$ is extremely large (as at rhodopsin site 273 where the 95% CI reaches $\omega^+ = 6,726$), the signal can be driven by a single branch carrying multiple nonsynonymous substitutions, which may reflect either an intense selective burst, a simultaneous multinucleotide mutation, or a sequencing/alignment error.
* **HOW:** Recommend in the practical guidelines (Discussion) that users inspect the Empirical Bayes branch count (`EBF > 20`) or require $\ge 2$ branches supporting $\beta^+ > \alpha$ when screening noisy or low-divergence alignments where multinucleotide mutations or terminal sequencing errors may occur.

#### 2. Explicitly State the Mixture Weights and Degrees of Freedom of the Calibrated Null Distribution in the Main Text
* **WHY:** In the current PDF-to-text conversion of the manuscript, several inline mathematical expressions (including the exact $\chi^2$ mixture formula in lines 79, 231, and 246) were stripped during XML/HTML rendering, leaving blanks where the mixture weights and $\chi^2$ degrees of freedom appear.
* **WHAT & HOW:** Ensure that the exact asymptotic mixture formula for the MEME LRT $p$-value mapping—specifically $0.33 \chi^2_0 + 0.30 \chi^2_1 + 0.37 \chi^2_2$ (or the exact two-component $\chi^2_1$ and $\chi^2_2$ mixture weights used in HyPhy)—is printed explicitly in plain text/LaTeX in Section "The MEME test for episodic diversifying selection" (line 79) and the Figure S1 legend (line 246).

#### 3. Technical, Mathematical, and Editorial Cleanup
* **WHY:** A few minor typographical errors and broken cross-references appear in the text and tables.
* **WHAT & HOW:**
  * **Table 2 spelling typo (line 178):** *"Mamallian -globin"* $\rightarrow$ *"Mammalian $\beta$-globin"*.
  * **Broken supplementary table reference in line 222:** The text cites *"see Text S1 and Table 23"*—change *"Table 23"* to *"Table S21"* (corresponding to the H3N2 subset table described at line 292/354).
  * **Encoding artifact in Figure 2 caption (line 203):** Remove the stray character `Ê` in *"black –Ê no information"* $\rightarrow$ *"black – no information"*.
  * **Duplicate typo in Figure S2 caption (lines 248, 310):** *"according the the value"* $\rightarrow$ *"according to the value"*.
