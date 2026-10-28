# Forensic Peer Review: `ANON_18`

## 1. Executive Assessment & Calibration

**Overall Score:** **8.3 / 10.0** (Strong / Sound)
* **Score Breakdown:** Rigor: 2.7/3.5 | Claims: 2.0/2.5 | Biology: 1.8/2.0 | Reproducibility: 1.8/2.0

**Synthesis:** This manuscript presents a comprehensive evolutionary analysis of over 1,000,000 SARS-CoV-2 genome sequences sampled through June 2021, investigating the shift in global selective pressures coinciding with the emergence of the 501Y lineages (Alpha/B.1.1.7 [V1], Beta/B.1.351 [V2], and Gamma/P.1 [V3]) and testing for convergent positive selection within and across these lineages. The computational pipeline is well-engineered for pandemic-scale genomic data: it restricts phylogenetic selection inference (`FEL`, `MEME`, `SLAC`, `PRIME`) to internal tree branches to mitigate terminal sequencing errors and non-transmitted within-host variants, applies a binomial genotype error filter and three-stage clustering (`tn93-cluster`), and normalizes site-level selection counts per kilobase per unit of internal tree length. While the identification of a 35-site convergent "501Y meta-signature" is well supported by comparative sequence evidence and temporal frequency tracking, the post-March 15, 2021 frequency-doubling chi-square tests do not stratify by geographic country or sub-clade (leaving them partially susceptible to regional founder and sampling effects), and a speculative proposal in the Discussion to perform live-virus *in vitro* co-infection/recombination experiments across V1, V2, and V3 warrants removal on biosafety grounds.

---

## 2. Claim-by-Claim Audit

* **Claim 1:** "Global selective regimes on SARS-CoV-2 shifted sharply around November 2020, characterized by an inflection in positively selected (FEL/MEME) and negatively selected sites normalized per Kb per unit internal tree length." — **[Well Supported]**
  * **Audit:** Using 90-day sliding windows across non-identical deduplicated viral haplotypes and restricting `FEL` and `MEME` ($p \le 0.05$) strictly to internal phylogenetic branches, the authors control for terminal branch sequencing artifacts and normalize raw counts by gene length (Kb) and internal tree length (Figure 1B–C). Because sample size and tree topology still influence power even after dividing by internal tree length (as noted by the authors in the text when discussing the collapse of deep inter-clade branches during the V1 sweep in early 2021), the trends in Figure 1 correctly capture the macro-evolutionary transition from near-neutral genetic drift in early 2020 to diversifying/purifying selection in late 2020.

* **Claim 2:** "During ongoing divergence within V1, V2, and V3, 151 nonsynonymous sites experienced episodic or pervasive positive selection along internal branches, displaying statistically significant inter-lineage convergence at 28 non-signature sites ($p \le 0.002$, permutation test) and defining a 35-site 501Y meta-signature." — **[Well Supported]**
  * **Audit:** The permutation test (Table 1) conditions on the observed number of non-signature variable sites in each lineage (1,073 in V1; 291 in V2; 322 in V3) rather than total genome length, providing a conservative null distribution for pairwise and three-way site overlap ($p \le 0.0001$ for V1/V2/V3 overlap of positively selected sites). One methodological caveat—transparently acknowledged by the authors in the Results (`Signals of selection within the V1, V2 and V3 lineages`)—is that the basal clade-defining branches of V1, V2, and V3 were included in the lineage datasets, which boosts `MEME`/`FEL` signal at clade-defining signature positions if they also mutate once or twice elsewhere in the tree. However, Table 1 explicitly removes all signature sites before testing for convergence, confirming that the convergence signal is not an artifact of basal branch inclusion.

* **Claim 3:** "Convergent mutations at the 35 meta-signature sites confer a demonstrable transmission or fitness advantage, evidenced by 23/35 sites showing >2-fold frequency increases across V1, V2, and V3 between March 15, 2021 and June 1, 2021 ($p < 0.004$, $2\times 2$ $\chi^2$ test)." — **[Moderately Supported]**
  * **Audit:** Testing whether sites identified purely from pre-March 15, 2021 selection scans subsequently increase in frequency between March 15 and June 1, 2021 provides a clean prospective temporal validation without lookahead leakage. However, computing a pooled $2\times 2$ $\chi^2$ test on raw GISAID sequence counts within V1, V2, or V3 assumes independent multinomial sampling across a panmictic population. In reality, SARS-CoV-2 sequences are clustered in space and time, and changes in national sequencing volume (e.g., rapid expansion of sequencing in specific European, South American, or North American jurisdictions where a sub-lineage carrying `S/490`, `S/681`, or `ORF1a/1708D` happened to founder) can produce >2-fold global frequency shifts with tiny nominal $\chi^2$ $p$-values even under neutral geographic expansion.

* **Claim 4:** "In regions of high co-circulation of V1, V2, and V3, tracking recombinant viruses and conducting *in vitro* evolution experiments using serum/neutralizing antibodies on mixed cell-culture co-infections of V1, V2, and V3 would immediately reveal super-variant selective fitness." — **[Overstated]**
  * **Audit:** While genomic surveillance for natural recombinants is scientifically sound, the explicit proposal in the Discussion (page 9) to deliberately co-infect cell cultures with live V1 (Alpha), V2 (Beta), and V3 (Gamma) variants under neutralizing antibody selection to breed chimeric "super-variants" combining immune escape and heightened transmissibility constitutes a dual-use gain-of-function experiment of concern. It is unnecessary for validating the manuscript's bioinformatics findings and should be excised.

---

## 3. Concrete Suggestions for Improvement

1. **Account for Geographic Clustering in the Post-March 15, 2021 Frequency Trajectory Tests (`Claim 3`):**
   * Instead of unstratified global $2\times 2$ $\chi^2$ tests comparing pre-March 15 and post-March 15 GISAID counts, apply a Cochran-Mantel-Haenszel (CMH) test stratified by country/region, or require that the >2-fold frequency increase be replicated across at least two independent geographic regions or independent sub-clade origins within the phylogeny.

2. **Exclude Basal Clade-Defining Branches When Quantifying Strictly *Within-Lineage* Selection (`Claim 2`):**
   * In Figure 3 and the 151-site catalog, re-run `FEL`, `MEME`, and `PRIME` with only the strictly descendant internal branches of V1, V2, and V3 placed in the foreground (`--branches`), moving the basal clade-defining branches (`B.1.1.7`, `B.1.351`, `P.1` root stems) to the background partition. Report how many of the 23 selected signature sites remain significant strictly from recurrent/secondary mutations *within* each lineage.

3. **Remove the Proposal for *In Vitro* Multi-Variant Co-Infection/Recombination Selection Experiments (`Claim 4`):**
   * Delete the paragraph in the Discussion (page 9: *"To immediately understand the potential selective fitness of SARS-CoV-2 variants matching the 501Y meta-signature... evolution experiments using rigorously controlled in vitro systems..."*) proposing forced *in vitro* recombination of V1, V2, and V3 under immune selection, or restrict the recommendation to pseudovirus neutralization assays and passive genomic surveillance.

4. **Correct Typographical Errors in Figures and Text:**
   * **Figure 4 caption (appears twice on pages 7–8):** Correct *"between January and June **2001**"* to *"between January and June **2021**"*.
   * **Results (`Everything Everywhere All at Once`, page 7):** Correct `Heicase/590I` to `Helicase/590I`, `A/701` (page 6) to `S/701`, and `K417N/K` (page 8) to `K417N/T`.
