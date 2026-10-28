# Review of ANON_04

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **2.3 / 10.0** (Fundamentally Invalid)  
* **Score Breakdown:** Rigor: 0.4/3.5 | Claims: 0.4/2.5 | Biology: 0.5/2.0 | Reproducibility: 1.0/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript surveys genome-wide GC content and CpG dinucleotide relative abundance ($I_{CpG} = P_{CpG} / (P_C P_G)$) across complete *Betacoronavirus* ($n = 927$ with host labels) and *Alphacoronavirus* genomes ($\ge 27,000\text{ nt}$) to infer the intermediate host and tissue environment in which SARS-CoV-2 evolved. Observing that SARS-CoV-2, BatCoV RaTG13 ($I_{CpG} = 0.40875$), and pangolin-derived sarbecoviruses (EPI_ISL_410721, $I_{CpG} = 0.3929$) have the lowest $I_{CpG}$ values among *Betacoronavirus* genomes, and noting that canine coronavirus (CCoV, an *Alphacoronavirus*) has a similarly low $I_{CpG}$, the author hypothesizes that the ancestor of SARS-CoV-2 and RaTG13 infected the intestine of a canid (feral dog), underwent rapid ZAP-driven CpG depletion ($\text{CpG} \rightarrow \text{UpG}$), and subsequently transmitted to humans and/or back to bats and pangolins. Supplementary Excel tables of genome-wide $I_{CpG}$ values are referenced.

While the descriptive observation that the SARS-CoV-2 / RaTG13 / pangolin-CoV clade exhibits lower genome-wide $I_{CpG}$ than SARS-CoV-1 and MERS-CoV is empirically true, the evolutionary and biological conclusions drawn from it are fundamentally invalid. The manuscript contains zero statistical tests, no phylogenetic comparative controls for lineage non-independence, and no gene-by-gene or codon-position analyses of CpG distribution. Worse, its central narrative—that the common ancestor of SARS-CoV-2, bat RaTG13, and pangolin CoVs evolved in a dog's intestine because an unrelated *Alphacoronavirus* (CCoV) happens to fall in a similar bivariate $(GC\%, I_{CpG})$ region—contradicts its own empirical data in at least four ways: (1) bat coronaviruses are already predominantly enteric (RaTG13 itself was isolated from a bat fecal swab, line 35), negating any need to invoke a dog intestine to explain enteric tropism; (2) human *Betacoronavirus* HKU1 has an even lower $I_{CpG}$ and GC% than SARS-CoV-2 (Group 1 in Fig. 1) despite being a strictly human respiratory pathogen; (3) the author offers zero data showing that canine intestines express higher ZAP levels than bat intestines or human lungs; and (4) suggesting that a canid intestinal virus spread back into wild *Rhinolophus affinis* bats (RaTG13) and Malayan pangolins (line 41) is biologically and ecologically implausible. Salvaging any valid component of this work would require stripping all speculative canine-origin claims and replacing visual scatterplot cherry-picking with formal phylogenetic comparative modeling and sliding-window mutational analyses.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **SARS-CoV-2, BatCoV RaTG13, and pangolin sarbecoviruses share lower genome-wide $I_{CpG}$ (~0.39–0.41) than SARS-CoV-1 and most other *Betacoronavirus* lineages: [Well Supported].**  
  The raw dinucleotide counts across the 927 *Betacoronavirus* genomes (Figs. 1–2 and line 37) accurately reflect a shared ancestral reduction in $I_{CpG}$ and GC% across the SARS-CoV-2-related *Sarbecovirus* subclade (including bat RaTG13 and pangolin CoV EPI_ISL_410721).

* **Low $I_{CpG}$ in BatCoV RaTG13 and SARS-CoV-2 could not have evolved in *Rhinolophus* bats and indicates evolution in a non-bat mammalian host tissue with high ZAP expression: [Methodologically Flawed].**  
  This claim fails on both phylogenetic and empirical grounds (Pillars 2, 3, 5, and 6):
  1. *Ignoring phylogenetic shared ancestry and unsampled bat diversity:* BatCoV RaTG13 (from *Rhinolophus affinis*) and pangolin-CoV (EPI_ISL_410721) both possess $I_{CpG} \approx 0.39\text{--}0.41$ (lines 19, 37). Because RaTG13 and SARS-CoV-2 diverge by 4% across the genome (~1,200 nucleotide substitutions, corresponding to decades of evolution in bats), the low-$I_{CpG}$ compositional signature is an ancestral feature of the *Sarbecovirus* sub-lineage circulating in *Rhinolophus* bats, not a recent post-bat host-jump acquisition. Claiming that this feature "likely is not in *Rhinolophus* bats" when the virus possessing it (RaTG13) was literally sampled from a wild *Rhinolophus* bat fecal swab in 2013 is circular.
  2. *No ZAP expression data across hosts or tissues:* Throughout the manuscript (Abstract, lines 17, 19, 41), the author asserts that digestive tissues and canid intestines have higher ZAP (*ZC3H12A* / *ZC3HAV1*) expression than respiratory tissues or bat tissues. However, not a single measurement or citation of ZAP mRNA or protein expression across tissues or species is provided (Fig. 3C plots *ACE2*, not ZAP).
  3. *Conflating C$\rightarrow$U deamination with $\text{CpG}\rightarrow\text{UpG}$ selection:* In line 41, the author claims selection against CpG caused "many $\text{CpG} \rightarrow \text{UpG}$ mutations leading to reduced genomic $I_{CpG}$ and GC%." In reality, C$\rightarrow$U transitions in single-stranded RNA viruses are driven primarily by host APOBEC cytidine deaminases and oxidative/replication biases (which mutate $\text{CpG} \rightarrow \text{UpG}$ on the plus strand and $\text{CpG} \rightarrow \text{CpA}$ via minus-strand deamination), and No mutational spectrum analysis is performed to verify whether $\text{CpG}\rightarrow\text{UpG}$ actually occurred.

* **Digestive-tract coronaviruses systematically evolve lower $I_{CpG}$ than respiratory coronaviruses: [Overstated].**  
  The author cherry-picks two qualitative comparisons—camel Embecovirus HKU23 vs. MERS-CoV (line 23) and canine Alphacoronavirus CCoV vs. canine Betacoronavirus CRCoV (line 27)—without any statistical test or control for viral subgenus:
  1. *Taxonomic confounding (Pillar 3):* Camel HKU23 and canine CRCoV both belong to the species *Betacoronavirus 1* (*Embecovirus*), whereas MERS-CoV belongs to *Merbecovirus* and CCoV belongs to *Alphacoronavirus 1*. Comparing an *Alphacoronavirus* (CCoV) to a *Betacoronavirus* (CRCoV) in dogs mixes two different viral genera that diverged thousands of years ago and have different RNA-dependent RNA polymerase replication fidelities.
  2. *Direct contradiction within the author's own figures (Pillar 5):* In Figure 1, Group 1 is human coronavirus HKU1, which has the lowest GC% (~32%) and lowest $I_{CpG}$ (~0.37) on the entire plot—yet HKU1 is a strictly human *respiratory* virus. Conversely, bat SARS-CoV-1-related viruses (Group 3 in Fig. 1) are predominantly *enteric* in *Rhinolophus* bats (sampled from anal/fecal swabs) yet have relatively high $I_{CpG}$ (~0.50–0.60). A formal test across all 927 genomes stratifying by tissue tropism and controlling for viral phylogeny would immediately refute a universal enteric-low-$I_{CpG}$ rule.

* **Feral dogs (canids) served as the intermediate host where the ancestor of SARS-CoV-2 evolved low $I_{CpG}$ before transmitting to humans, bats, and pangolins: [Methodologically Flawed].**  
  Inferring that SARS-CoV-2 evolved in dog intestines (line 41) solely because CCoV (*Alphacoronavirus*) has a similar genome-wide $I_{CpG}$ and GC% is a textbook ecological and phylogenetic fallacy. By the exact same logic, Figure 3A shows that human *Alphacoronavirus* NL63 (line 35) and *Betacoronavirus* HKU1 (Fig. 1) also have extreme CpG deficiency, yet neither involves dogs. Furthermore, proposing that a virus recently acquired its low-GC genome in a dog's intestine and then "spread to other species" (i.e., back into wild Yunnan *Rhinolophus affinis* bats sampled in 2013 and smuggled Sunda pangolins; line 41) violates basic molecular clock and ecological constraints.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Control for Viral Phylogeny Using Phylogenetic Generalized Least Squares (PGLS) When Testing Tissue Tropism vs. $I_{CpG}$
* **WHY:** Viral genomes within the same subgenus (*Embecovirus*, *Merbecovirus*, *Sarbecovirus*, *Alphacoronavirus 1*) share $I_{CpG}$ and GC% by common descent. Comparing CCoV (*Alphacoronavirus*) to CRCoV (*Betacoronavirus*) or camel HKU23 (*Embecovirus*) to MERS-CoV (*Merbecovirus*) without phylogenetic correction treats hundreds of closely related isolates as independent data points and confounds viral genus with tissue tropism.
* **WHAT:** Perform a formal phylogenetic comparative analysis testing whether enteric vs. respiratory tropism or host taxon significantly predicts $I_{CpG}$ after accounting for the viral phylogeny.
* **HOW:** Reconstruct a maximum-likelihood phylogeny of representative unique *Alphacoronavirus* and *Betacoronavirus* species using the RdRp (Nsp12) or concatenated core replicase genes. Code each tip by primary tissue tropism (enteric vs. respiratory) and host order, and fit a PGLS regression (`gls` in R package `nlme` with `corPagel` or `corBrownian` from `ape`):
  $$I_{CpG} \sim \beta_0 + \beta_1 \text{Tropism} + \beta_2 \text{GC\%} + \epsilon, \quad \epsilon \sim \mathcal{N}(0, \sigma^2 \mathbf{V}_{\text{tree}})$$
  Report the phylogenetically corrected $\beta_1$ estimate and $p$-value.

#### 2. Analyze tissue- and species-specific *ZC3HAV1* (ZAP) Expression Empirically Rather Than Assuming Enteric Enrichment
* **WHY:** The manuscript repeatedly claims that low viral $I_{CpG}$ is driven by high ZAP expression in digestive tissues (lines 17, 19, 33, 41), but Fig. 3C plots only *ACE2* expression from Fagerberg et al. (2014)—not ZAP (*ZC3HAV1*).
* **WHAT:** Replace or supplement Fig. 3C with actual tissue-specific expression data for *ZC3HAV1* (ZAP) and *APOBEC3* family members from the exact same human (and, where available, mammalian/canine/bat) RNA-seq atlases.
* **HOW:** Extract the RPKM/TPM values for *ZC3HAV1* across the human tissues in Fagerberg et al. (2014) (Human Protein Atlas / GTEx) and plot lung vs. small intestine/duodenum/colon ZAP expression, testing whether digestive tissues actually express higher ZAP than respiratory/lymphoid tissues.

#### 3. Reconstruct Ancestral Branch-Specific Substitution Spectra Along the *Sarbecovirus* Phylogeny
* **WHY:** The author claims in line 41 that "rapid evolution of the virus, with many $\text{CpG} \rightarrow \text{UpG}$ mutations" occurred in a canid intestine. Because SARS-CoV-2, BatCoV RaTG13, and pangolin-CoV EPI_ISL_410721 all share $I_{CpG} \approx 0.39\text{--}0.41$ (lines 19, 37), any CpG depletion occurred on the internal ancestral branch leading to the (SARS-CoV-2, RaTG13, Pangolin-CoV) clade—or varies locally by recombinant genomic region (e.g., Spike vs. ORF1ab)—rather than on the terminal branch leading to SARS-CoV-2.
* **WHAT:** Perform ancestral sequence reconstruction across the *Sarbecovirus* alignment and map $I_{CpG}$ and $\text{CpG}\rightarrow\text{UpG}/\text{CpA}$ substitution counts onto specific internal and terminal branches, as well as across sliding genomic windows.
* **HOW:** Align SARS-CoV-2, RaTG13, pangolin CoVs, ZC45, ZXC21, and SARS-CoV-1. Reconstruct ancestral states at internal nodes using `iqtree -asr` or `baseml`, compute $I_{CpG}$ for each internal node and sliding 1-kb window, and report whether $I_{CpG}$ changed between the (SARS-CoV-2 + RaTG13) ancestor and SARS-CoV-2.

#### 4. Remove Unsupported Speculation About Canine Intermediate Hosts and Reverse Transmission to Bats
* **WHY:** Zero sequence, serological, epidemiological, or experimental evidence links canine enteric coronaviruses to the origin of SARS-CoV-2, and suggesting that a dog-adapted virus spread back into wild *Rhinolophus* bats (to become RaTG13 in 2013) and pangolins (line 41) is biologically untenable.
* **WHAT:** Remove the canine-origin hypothesis from the Abstract and Results/Discussion (lines 25–28, 41) and reframe the paper strictly as a comparative survey of CpG dinucleotide composition across coronaviruses.
* **HOW:** Revise the Abstract and concluding paragraphs (lines 41–43) to state that low $I_{CpG}$ is an ancestral property shared by the SARS-CoV-2, BatCoV RaTG13, and pangolin *Sarbecovirus* clade, and discuss both ZAP-mediated selection and APOBEC-mediated C$\rightarrow$U mutational bias as candidate evolutionary mechanisms.

#### 5. Technical, Mathematical, and Editorial Cleanup
* **WHY:** The manuscript contains a mathematical typo in the figure caption formula for $I_{CpG}$ and several spelling/citation errors.
* **WHAT & HOW:**
  * **Formula typo in Figure 1 caption (line 56):** The caption writes `ICpG(=PCpG/PCPG)` instead of $I_{CpG} = P_{CpG} / (P_C P_G)$—fix the denominator to show the product of mononucleotide frequencies $P_C \times P_G$ and state this equation explicitly in the main text.
  * **Methodological note on MAFFT in Figure 3 caption (line 58):** The caption states *"Genomes were aligned with MAFFT (Katoh et al. 2009) with the FFT-NS-2 option (more accurate than default)."* In MAFFT, `FFT-NS-2` is the fast progressive *default* method, whereas iterative refinement (`L-INS-i` / `FFT-NS-i`) is the more accurate option. Correct this description.
  * **Spelling typos:** Line 39: *"ABOBEC3G"* $\rightarrow$ *"APOBEC3G"*; Line 31: *"cells that expresses"* $\rightarrow$ *"cells that express"*.
