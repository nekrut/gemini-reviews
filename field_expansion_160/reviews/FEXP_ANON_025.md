# Review of FEXP_ANON_025

**Overall Score:** **8.3 / 10.0** (Strong / Sound) | **Scientific Core Score:** **6.4 / 8.0**  
* **Score Breakdown:** Rigor: 2.8/3.5 | Claims: 2.0/2.5 | Biology: 1.6/2.0 | Reproducibility: 1.9/2.0

---

## 1. Blinded Metadata Perception

* **Manuscript ID:** `FEXP_ANON_025`
* **Perceived Research Domain:** Bacterial population genetics and molecular evolution (Hill–Robertson interference, homologous recombination, and adaptive protein evolution in *Rhizobium leguminosarum*).
* **Study Design:** Comparative population genomic analysis of 3,086 vertically inherited core protein-coding genes (3,091,179 bp; 334,040 bi-allelic SNPs) across 196 isolates belonging to five sympatric genospecies (`gsA–gsE`) of the *Rhizobium leguminosarum* species complex sampled from *Trifolium repens* root nodules.
* **Primary Methods:** Orthology inference and HGT filtering (`Prokka` v1.12, `Proteinortho` v5.16b, `ClustalO` v1.2.0, phylogenetic introgression score $\le 3$, $\pi < 0.1$), transition/transversion ($\kappa$) and site counting (`Yang & Nielsen 2000` / `Biopython`), folded site frequency spectrum (SFS) and Distribution of Fitness Effects (DFE) modeling (`GRAPES` with `GammaZero` model and demographic nuisance parameters), intragenic recombination estimation (Pearson's $r^2$, Lewontin's $D'$, and `ClonalFrameML` $R/\theta$), and nonparametric gene-shuffling permutation tests (200 replicates).

---

## 2. Executive Summary & Editorial Verdict

This manuscript tests whether intraspecific homologous recombination increases the efficacy of natural selection and the proportion of adaptive amino acid substitutions ($\alpha$) in natural prokaryotic populations, as predicted by Hill–Robertson selective interference theory. Analyzing 3,086 core genes free of recent interspecies horizontal gene transfer (HGT) across five closely related species (`gsA–gsE`) of the *Rhizobium leguminosarum* complex, the authors estimate the distribution of fitness effects (DFE), $\alpha$, the adaptive substitution rate ($\omega_a$), and the nonadaptive substitution rate ($\omega_{na}$) across all 20 pairwise focal–outgroup ("mirror") species combinations using `GRAPES` on folded synonymous and nonsynonymous SFSs. Across species, $\alpha$ ranges from $0.07$ to $0.39$ and ranks concordantly with species-wide recombination levels and purifying selection efficacy ($\pi_N/\pi_S$). Within species (for `gsA`, `gsB`, `gsC`, and `gsE`), partitioning genes into tertiles of intragenic recombination ($r^2$, validated with $D'$ and `ClonalFrameML` $R/\theta$) demonstrates that higher recombination is associated with higher $\alpha$, driven roughly equally by an increase in $\omega_a$ and a decrease in $\omega_{na}$. Raw sequencing reads (`PRJNA510726`), custom Python analysis pipelines (`GitHub`), and orthologous alignments/SNP matrices (`FigShare`) are all openly available.

This is a well-designed, rigorous population genomic study that carefully adapts eukaryotic DFE-$\alpha$ inference (`GRAPES` with folded SFS and demographic nuisance parameters) to a bacterial species complex while controlling for interspecies introgression, outgroup choice ("mirror" species design), and recombination metric choice ($r^2$, $D'$, and $R/\theta$). A few methodological caveats and minor reporting inconsistencies merit attention: (1) the authors do not test whether GC-biased gene conversion (gBGC)—which is linked to bacterial homologous recombination and can mimic positive selection by driving fixation of $AT \to GC$ nonsynonymous variants—contributes to the elevated $\omega_a$ in high-recombination genes; (2) filtering for $\ge 10$ non-singleton segregating sites per gene to compute $r^2$ removes $62\%\text{–}92\%$ of core genes in lower-diversity species (`gsB`, `gsD`, `gsE`), introducing a gene-length/polymorphism ascertainment filter; (3) strong population structure in `gsC` (French vs. UK/Danish strains) can inflate intragenic $r^2$ via the two-locus Wahlund effect at geographically differentiated loci; and (4) there are two minor numerical/terminological slips in the text (species sample sizes summing to 192 rather than 196 on line 32, and variable SNP counts labeled as total expected synonymous/nonsynonymous sites on line 127).

### Specific Assessment of Core Claims

* **The proportion of adaptive amino acid substitutions ($\alpha$) ranges from $0.07$ to $0.39$ across the five *Rhizobium* species and correlates positively with species-level recombination:** **[Moderately Supported].**  
  The "mirror" species design across all 20 focal–outgroup pairs (Table 1) demonstrates high consistency across outgroups, and both $\alpha$ and $\pi_N/\pi_S$ track the species ranking of LD decay (`gsC > gsA > gsE > gsB > gsD`). Support at the interspecies level is necessarily moderated by the small number of species ($N = 5$), the tiny sample size of `gsD` ($n = 5$ strains, where the folded SFS has only two frequency bins: singletons and doubletons), and the confounding between long-term $N_e$ ($\pi$) and population-scaled recombination ($\rho = 2N_e r$).

* **Within species, genes with higher homologous recombination rates exhibit higher $\alpha$, driven both by higher adaptive substitution rates ($\omega_a$) and lower nonadaptive substitution rates ($\omega_{na}$):** **[Well Supported].**  
  The intraspecific positive relationship between recombination and $\alpha$ (and opposing trends of $\omega_a$ and $\omega_{na}$; Figs. 2 and 3) is replicated across four species (`gsA`, `gsB`, `gsC`, `gsE`), confirmed by 200 permutation tests (Fig. S7), and shown to be robust across three distinct estimators of recombination ($r^2$, $D'$, and `ClonalFrameML` $R/\theta$; Figs. S9–S12). While GC-biased gene conversion (gBGC) is an unmodeled potential contributor to $\omega_a$, the simultaneous decrease in $\omega_{na}$ directly supports a reduction in Hill–Robertson interference and more efficient purifying selection.

* **Differences in $\alpha$ across genomic compartments (chromosome, chromids Rh01 and Rh02, plasmid Rh03) are not statistically significant after downsampling to equal gene counts:** **[Well Supported].**  
  Downsampling the chromosome (`2,550` genes), `Rh01` (`288` genes), and `Rh02` (`160` genes) to match the smallest compartment (`Rh03`, `88` genes; Table 2) is a symmetric control for sample size, and the authors appropriately conclude that overlapping confidence intervals preclude claiming compartment-specific differences.

---

## 3. Forensic Defect Inventory

### Defect 1: Unassessed Contribution of GC-Biased Gene Conversion (gBGC) to $\omega_a$ in High-Recombination Genes (Pillar 3 & Pillar 5)
* **Location:** Results and discussion (lines 66–71, Figure 3).
* **Diagnostic Finding:** In bacteria as in eukaryotes, homologous recombination repair of heteroduplex DNA is often biased toward GC alleles (gBGC; Lassalle et al. 2015). Because gBGC acts like positive selection on $AT \to GC$ mutations (increasing their fixation probability relative to SFS expectations) and is concentrated in high-recombination genes, gBGC can artificially inflate $\alpha$ and $\omega_a$ in the highest recombination tertile even in the absence of adaptive protein evolution.
* **Remediation:** Discuss gBGC as a potential confounder of $\omega_a$ or perform a sensitivity check restricting the SFS and divergence counts to GC-conservative transversions ($A \leftrightarrow T$ and $G \leftrightarrow C$) to verify that the increase in $\alpha$ and $\omega_a$ across recombination tertiles is not driven by $AT \to GC$ fixation bias.

### Defect 2: Polymorphism Ascertainment Bias ($\ge 10$ Non-Singleton SNPs) and Subpopulation Structure Effects on Intragenic $r^2$ (Pillar 2 & Pillar 3)
* **Location:** Results lines 39, 41, 59 and Figure 1c–d.
* **Diagnostic Finding:**
  1. **Gene retention skew:** Requiring $\ge 10$ non-singleton SNPs per gene to calculate $r^2$ retains $\sim 80\%$ of core genes in `gsA` (`2,453/3,086`) and `gsC` (`2,537/3,086`), but drops retention to $37.6\%$ in `gsE` (`1,161`), $25.0\%$ in `gsB` (`770`), and $8.3\%$ in `gsD` (`257`). Because `ClonalFrameML` ($R/\theta$) does not require excluding singletons or enforcing a 10-SNP per-gene cutoff in the same way as pairwise $r^2$, it is unclear whether the `ClonalFrameML` analyses (Figs. S9–S12) were restricted to the same subset of $\ge 10$-SNP genes or run on all 3,086 core genes.
  2. **Population structure in `gsC`:** As noted in line 41 (and Fig. 1d / Fig. S4), `gsC` has pronounced population structure driven by French vs. UK/Danish isolates. While `GRAPES` demographic nuisance parameters adjust the 1D SFS, two-locus LD ($r^2$ and $D'$) computed across a structured sample is elevated at loci with high inter-deme allele frequency differentiation ($F_{ST}$), potentially confounding intragenic recombination rate with geographic differentiation.
* **Remediation:** Clarify whether `ClonalFrameML` tertiles were built on all 3,086 genes or only the $\ge 10$-SNP subset, and note that in `gsC` computing $r^2$ within the largest homogeneous geographic subpopulation (e.g., excluding the divergent French deme) would avoid two-locus Wahlund inflation of $r^2$.

### Defect 3: Minor Numerical and Terminological Discrepancies in Strain Counts and Site Counts (Pillar 7)
* **Location:** Results line 32 and Material and Methods line 127.
* **Diagnostic Finding:**
  1. **Strain count sum (`192` vs. `196`):** Line 32 states: *"Across all five species (196 strains, gsA: 32, gsB: 32, gsC: 112, gsD: 5, gsE: 11)"*. However, $32 + 32 + 112 + 5 + 11 = 192$ strains, leaving 4 of the 196 strains unaccounted for in the per-species breakdown.
  2. **Variable SNPs vs. total sites wording:** In the section *"Transition Transversion Rate Bias (Kappa) and Expected Number of Synonymous and Nonsynonymous Sites"* (line 127), the authors write: *"A total of 284,742 synonymous, 49,298 nonsynonymous sites were counted"*. Notice that $284,742 + 49,298 = 334,040$, which is the exact number of **variable sites (SNPs)** reported in line 32 (*"3,086 genes (total alignment length: 3091179 bp) and 334040 variable sites"*), whereas the total expected number of synonymous ($L_{ps}$) and nonsynonymous ($L_{pn}$) sites across the $3,091,179\text{ bp}$ alignment is $\sim 3.09 \times 10^6$ (with $L_{pn} > L_{ps}$).
* **Remediation:** Reconcile the per-species isolate counts in line 32 so that they sum to 196 (or explain why 4 strains were unassigned), and change *"sites"* to *"variable sites (SNPs)"* in line 127 alongside reporting the total alignment-wide $L_{ps}$ and $L_{pn}$ denominators.

---

## 4. Quantitative Rubric Scoring

| Rubric Dimension | Score | Max | Diagnostic Justification |
| :--- | :---: | :---: | :--- |
| **1. Methodological & Statistical Rigor** | **2.8** | **3.5** | Rigorous DFE-$\alpha$ estimation (`GRAPES` with folded SFS, AIC model selection, demographic nuisance parameters), symmetric "mirror" species design, 3 orthogonal recombination metrics ($r^2, D', R/\theta$), permutation testing, and sample-size-matched compartment controls; minor deductions for unassessed gBGC confounding and $\ge 10$-SNP gene filtering skew in low-diversity species. |
| **2. Claim-to-Evidence Alignment** | **2.0** | **2.5** | Claims are well calibrated to the core genome analysis, and limitations regarding the accessory genome, demographic structure, and compartment statistical power are explicitly and accurately discussed. |
| **3. Data Integrity & Biological Plausibility** | **1.6** | **2.0** | Careful exclusion of interspecies HGT/introgression (`introgression score <= 3`, $\pi < 0.1$) ensures valid vertical SFS/divergence comparisons in the core genome. |
| **4. Reproducibility & Data Integrity** | **1.9** | **2.0** | Exemplary open science: raw reads in INSDC (`PRJNA510726`), custom code on GitHub (`izabelcavassim/Popgen_bacteria`), and full alignments/SNP matrices on FigShare (`10.6084/m9.figshare.11568894.v5`); 0.1 deduction for the 192 vs. 196 strain sum and line 127 SNP vs. site wording slip. |
| **Total Composite Score** | **8.3** | **10.0** | **Strong / Sound** (Scientific Core Score: **6.4 / 8.0**) |
