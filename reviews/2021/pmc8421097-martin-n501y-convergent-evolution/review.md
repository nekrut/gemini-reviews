# Review of PMC8421097 (10.1016/j.cell.2021.09.003)

**Manuscript Title:** The emergence and ongoing convergent evolution of the SARS-CoV-2 N501Y lineages  
**Authors:** Darren P. Martin, Steven Weaver, Houriiyah Tegally, James Emmanuel San, Stephen D. Shank, Eduan Wilkinson, Alexander G. Lucaci, Jennifer Giandhari, Sureshnee Naidoo, Yeshnee Pillay, Lavanya Singh, Richard J. Lessells, Ravindra K. Gupta, Joel O. Wertheim, Anton Nekrutenko, Ben Murrell, Gordon W. Harkins, Philippe Lemey, Oscar A. MacLean, David L. Robertson, Tulio de Oliveira, Sergei L. Kosakovsky Pond  
**Journal / Venue:** *Cell* (2021, Vol. 184, pp. 5189–5200.e7) (ID / DOI: `PMC8421097` / `10.1016/j.cell.2021.09.003`)  
**Overall Score:** **8.8 / 10.0** (Strong / Sound — Near-Exemplary)  
* **Score Breakdown:** Rigor: 3.2/3.5 | Claims: 2.1/2.5 | Biology: 1.7/2.0 | Reproducibility: 1.8/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

Martin et al. investigate the evolutionary forces underlying the near-simultaneous late-2020 emergence of the three SARS-CoV-2 N501Y Variants of Concern—Alpha (B.1.1.7 / V1), Beta (B.1.351 / V2), and Gamma (P.1 / V3)—across >1,000,000 GISAID genomes through June 1, 2021. Deploying an open-source, high-throughput comparative genomics workflow (`COVID-19 Galaxy`, `bealign` codon-aware alignment, three-stage haplotype deduplication/error-filtering/`tn93-cluster` compression, `RapidNJ`/`raxml-ng` tree reconstruction, and internal-branch `FEL`, `MEME`, `SLAC`, and `PRIME` selection analyses in `HyPhy v2.5.31` via the `RASCL` framework), the authors evaluate sliding 90-day global windows alongside clade-specific datasets. They demonstrate that the emergence of the 501Y lineages coincided in November 2020 with a sharp global inflection in the tree-length-normalized density of positively and negatively selected codon sites, identify 151 sites under positive selection along internal branches of V1/V2/V3 trees (including statistically significant inter-lineage convergence at 28 non-signature sites, $p \le 0.002$), validate fitness predictions prospectively by showing that 29 convergent mutations more than doubled in intra-lineage frequency between March 15 and June 1, 2021, and synthesize a 35-site "501Y meta-signature" tracked across interactive ObservableHQ notebooks and Zenodo archives.

This paper is a tour de force of large-scale molecular evolutionary surveillance: restricting $d_N/d_S$ inference to internal branches (`--branches Internal`), normalizing selected-site density by internal branch length (subs/site) to control for sample-size inflation, and pairing retrospective phylogenetic selection signals (pre-March 2021) with prospective out-of-sample allele frequency trajectories (March–June 2021) establish a gold-standard template for real-time pathogen phylodynamics. A few methodological and interpretive tensions warrant refinement: (1) retaining the basal clade-defining branches in the V1/V2/V3 lineage-specific `MEME`/`FEL` runs introduces an ascertainment bias for signature mutations; (2) the manuscript's central evolutionary forecast—that future dominant variants (and lineages like B.1.620/B.1.621) are converging on the 501Y fitness peak—underestimates competing non-501Y fitness peaks ( specifically B.1.617.2 / Delta, which was already sweeping globally by June 2021) and includes a potentially hazardous proposal for in-vitro live-virus recombination passaging; and (3) a few minor method-reference inconsistencies (`PRIME` vs. compositional scoring, unadjusted site-level `FEL`/`MEME` nominal $p$-thresholds) and text typos should be cleaned up.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Late-2020 Global Shift in the SARS-CoV-2 Selective Landscape: Well Supported.**  
  By tracking sliding 90-day windows from March 2020 to April 2021 and normalizing the number of `FEL`-detected positively and negatively selected sites per kilobase per unit of internal tree length (filtering out gene trees with $<0.5$ subs/site), the authors convincingly show that the November 2020 surge in positive selection across `S`, `nsp2`, and `nsp6` is not a mere sample-size artifact, but reflects a genuine shift from early neutral drift (plus D614G/P323L) to multi-locus adaptive evolution.

* **Internal-Branch Positive Selection & Non-Random Inter-Lineage Convergence (V1, V2, V3): Well Supported.**  
  Restricting `MEME` and `FEL` to internal phylogenetic branches rigorously filters out terminal-branch sequencing errors and intra-host deleterious dead-end mutations. The permutation test conditioned on shared variable sites ($p < 0.001$ for V1/V2, $p = 0.002$ for V1/V3 and V2/V3) provides solid statistical proof that the 28 convergent non-signature sites (18 of which are also globally selected) are driven by shared selective pressures rather than random mutational coincidence.

* **Lineage-Specific Positive Selection at Clade-Defining Signature Sites (22/37 Sites): Moderately Supported / Ascertainment-Biased.**  
  As the authors candidly acknowledge in the text, including the basal branch that defines each clade (V1, V2, V3) inside the foreground branch set tested by `MEME`/`FEL` biases the test toward detecting signature mutations, because the clade itself was ascertained on the presence of those exact basal non-synonymous substitutions. While convergent re-emergence *within* the other 501Y clades (e.g., L18F, P681H, H655Y, A701V, T716I arising on internal branches inside sister clades) is genuine, basal trunk substitutions should be separated from strictly intra-clade internal branches.

* **Prospective Validation via Post-March 15, 2021 Allele Frequency Doubling (29/65 Sites): Well Supported (with Spatial Confounding Caveats).**  
  Splitting the timeline at March 15, 2021 so that pre-March internal-branch selection signals are tested against March 15 – June 1, 2021 frequency changes (with Bonferroni correction across gene-wide mutations) is an elegant, leak-free validation design. However, raw global GISAID frequency ratios ($RR(M)$) within V1, V2, and V3 can be confounded by geographic founder effects and rapid shifts in country-level sequencing volume (e.g., a sub-clade carrying a neutral hitchhiking mutation expanding in a heavily sequenced country).

* **Prediction of Ongoing Convergence Toward a Single 35-Site "501Y Meta-Signature" Summit: Moderately Supported / Partially Overstated.**  
  Within V1, V2, V3, B.1.526, and B.1.620, progressive accumulation of up to 10–16 meta-signature mutations is well documented. However, framing the pandemic's trajectory around variants summiting this specific 501Y peak downplays the simultaneous explosive sweep of B.1.617.2 (Delta)—which the authors note has a modal match of only 1/35 meta-signature sites—demonstrating that SARS-CoV-2 occupies a rugged, multi-peak fitness landscape where orthogonal combinations (L452R + T478K + P681R) can outcompete the 501Y meta-signature before 501Y variants reach their local summit (though Omicron BA.1 later combined many 501Y meta-signature sites on a deeply divergent background).

* **Proposal for Replicated Live-Virus In-Vitro Passaging & Recombination of V1/V2/V3 under Immune Sera: Questionable Biosafety Framing.**  
  In the concluding paragraphs before Limitations, the authors propose co-infecting live V1, V2, and V3 viruses in the presence of convalescent/vaccine sera to generate and select recombinant immune-escape chimeras before they arise in nature. While scientifically aimed at surveillance forecasting, proposing forward passaging to breed multi-VOC recombinants that combine enhanced transmissibility and immune escape raises severe dual-use / gain-of-function biosafety concerns that are not adequately caveated.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Decouple Basal Trunk Branches from Strictly Intra-Clade Internal Branches in `RASCL` / `MEME` / `FEL`
* **WHY:** Including the basal clade-defining branch in the foreground branch set guarantees that signature mutations have at least one non-synonymous substitution on a long trunk branch, inflating their `MEME` episodic selection signal.
* **WHAT:** Distinguish selection acting *during the origin* of V1/V2/V3 from ongoing selection *within* V1/V2/V3 after their emergence.
* **HOW:** Re-run or stratify the lineage-specific `HyPhy` `FEL`/`MEME` analyses into: (a) strictly intra-clade internal branches (excluding the basal stem branch connecting V1, V2, or V3 to the pre-October 2020 background tree), and (b) the basal stem branch. Report how many of the 22 signature sites remain significant (`p <= 0.05`) purely from recurrent internal-branch substitutions *within* each clade.

#### 2. Stratify Pre/Post-March 15 Frequency Ratios ($RR(M)$) by Country or Region to Control for Sequencing Skew
* **WHY:** Pooling all global GISAID sequences into a single $2\times 2$ contingency table (before vs. after March 15, 2021) is vulnerable to Simpson's paradox: if Country A (where a sub-lineage with mutation $M$ was founded) ramps up sequencing relative to Country B after March 15, $RR(M)$ will exceed 2.0 even if mutation $M$ is selectively neutral within Country A.
* **WHAT:** Verify that the 29 mutations doubling in frequency are increasing *within* geographic regions rather than tracking shifting national sequencing shares.
* **HOW:** Compute a Cochran-Mantel-Haenszel (CMH) stratified odds ratio across the top sequencing countries/regions (e.g., UK, US, continental Europe, South Africa, Brazil) for the 65 candidate sites in Table S2.

#### 3. Clarify the Figure 3 Evolutionary Viability Metric vs. `PRIME` Citation in STAR Methods
* **WHY:** The Figure 3 caption states that block colors indicate "model-based predictions of the probable evolutionary viability of the observed amino acid substitutions based on the numbers of times these substitutions have been observed in related coronaviruses that infect other host species," whereas STAR Methods ("Lineage-specific selection analyses") attributes this to `PRIME` (`http://hyphy.org/w/index.php/PRIME`). In `HyPhy`, `PRIME` tests property-informed physicochemical $d_N/d_S$ constraints, whereas scoring observed vs. expected amino acid states across a sarbecovirus/betacoronavirus outgroup alignment is an ancestral/compositional exchangeability profile (or `FADE`/profile log-odds score).
* **WHAT:** Ensure the exact mathematical model used to color the amino acid viability blocks in Figure 3 is accurately described.
* **HOW:** Specify in STAR Methods which sarbecovirus/betacoronavirus alignment was used, how ancestral/homologous states were tabulated, and what exact statistical thresholds define "unprecedented" (white), "highly unusual" (red), and "common" (green) substitutions.

#### 4. Harmonize Multiple-Testing & $p$-Value Thresholds Across Global (`FEL`) and Clade (`MEME`/`FEL`) Analyses
* **WHY:** Global sliding-window density plots use `FEL` $p \le 0.01$ (Figure 2A–B), lineage-specific selection and overlap tests use nominal `MEME`/`FEL` $p \le 0.05$ across ~10,000 codons (producing 151 sites), and frequency-doubling tests use gene-wide Bonferroni correction. Across 10,000 codons, a nominal $p \le 0.05$ threshold without false-discovery-rate (FDR) control can yield appreciable false positives if not cross-filtered by convergence.
* **WHAT:** Explicitly justify the multi-stage filtering architecture as a false-positive control mechanism.
* **HOW:** Add a brief note in "Quantification and statistical analysis" explaining that while single-clade `MEME`/`FEL` screens use a permissive nominal $p \le 0.05$ to maximize sensitivity on low-divergence trees, requiring independent inter-lineage convergence ($p \le 0.002$) plus out-of-sample Bonferroni-corrected frequency doubling ($RR > 2.0$) acts as a stringent composite filter against false positives.

#### 5. Temper the Live-Virus Co-Infection / Recombination Passaging Proposal
* **WHY:** Suggesting replicated laboratory co-infections of live V1, V2, and V3 viruses under immune serum selection to breed chimeric VOC recombinants with combined immune escape and enhanced replication poses substantial biosafety risks.
* **WHAT:** Reframe the experimental validation proposal toward safe, non-replicative or pseudotyped platforms.
* **HOW:** Replace the live-virus co-infection recommendation on page 10 with deep mutational scanning (DMS), combinatorial pseudovirus neutralization panels, or replicon systems, which can safely measure epistatic interactions among the 35 meta-signature mutations without generating replication-competent chimeric VOCs.

#### 6. Minor Technical & Typographical Corrections
* **WHY:** Small typographical slips in figures, tables, and author lists should be corrected for archival accuracy.
* **WHAT & HOW:**
  * **Figure 4 caption:** Fix `"between January and June 2001"` $\to$ `"between January and June 2021"`.
  * **Author list & Lead Contact:** Fix `"Anton Nekturenko"` $\to$ `"Anton Nekrutenko"`, and in Lead Contact fix `"Tulio de Oliviera"` $\to$ `"Tulio de Oliveira"`.
  * **Results text (page 6):** Fix `"A/701"` $\to$ `"S/701"` (`"S/655, S/681, A/701, and S/716"`).
  * **Results text (page 7):** Fix `"Heicase/590I"` $\to$ `"Helicase/590I"` and `"ORF3/171L"` $\to$ `"ORF3a/171L"`.
  * **Results text (page 8) & STAR Methods:** Fix `"K417N/K"` $\to$ `"K417N/T"` (K is the wild-type ancestral residue; N and T are the convergent V2 and V3 mutant states).
  * **Figure 5 caption:** Fix `"138HY"` $\to$ `"138H/Y"`.
