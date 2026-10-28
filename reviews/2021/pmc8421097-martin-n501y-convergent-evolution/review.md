# Review of PMC8421097 (10.1016/j.cell.2021.09.003)

**Manuscript Title:** The emergence and ongoing convergent evolution of the SARS-CoV-2 N501Y lineages  
**Authors:** Darren P. Martin, Steven Weaver, Houriiyah Tegally, James Emmanuel San, Stephen D. Shank, Eduan Wilkinson, Alexander G. Lucaci, Jennifer Giandhari, Sureshnee Naidoo, Yeshnee Pillay, Lavanya Singh, Richard J. Lessells, Ravindra K. Gupta, Joel O. Wertheim, Anton Nekrutenko, Ben Murrell, Gordon W. Harkins, Philippe Lemey, Oscar A. MacLean, David L. Robertson, Tulio de Oliveira, Sergei L. Kosakovsky Pond  
**Journal / Preprint:** *Cell* (2021, Vol. 184, pp. 5189–5200.e7; `PMC8421097` / `10.1016/j.cell.2021.09.003`)  
**Calibration Study Cohort:** Cohort B — Genre-Matched Validated Control (`B01` | Double-Blinded as `ANON_18`)  
**Overall Score:** **8.3 / 10.0** (Strong / Sound — Blinded Calibration Score; Initial Unblinded Pilot Score: **8.6 / 10.0**, Strong / Sound)  
* **Blinded Score Breakdown (`ANON_18`):** Rigor: 2.7/3.5 | Claims: 2.0/2.5 | Biology: 1.8/2.0 | Reproducibility: 1.8/2.0  
* **Initial Unblinded Pilot Score Breakdown:** Rigor: 3.1/3.5 | Claims: 2.0/2.5 | Biology: 1.7/2.0 | Reproducibility: 1.8/2.0  
> **Provenance Note ([Issue #9](https://github.com/spond/gemini-reviews/issues/9)):** This entry was one of the two initial pre-protocol unblinded pilot reviews (`8.6 / 10.0`) before the $N=200$ double-blinded calibration study (`calibration/reviews_anon/ANON_18.md`, where it scored `8.3 / 10.0`). To maintain a single canonical score source across `index.json` and `calibration/results_200.json`, the metadata and header now report the blinded calibration score (`8.3 / 10.0`) alongside the initial unblinded pilot score (`8.6 / 10.0`).

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

Martin et al. analyze the selective processes associated with the emergence and subsequent evolution of the three SARS-CoV-2 N501Y Variants of Concern—Alpha (B.1.1.7 / V1), Beta (B.1.351 / V2), and Gamma (P.1 / V3)—across >1,000,000 GISAID genomes collected through June 1, 2021. Using an open-source comparative genomics workflow (`COVID-19 Galaxy`, `bealign` codon alignment, three-stage haplotype deduplication/binomial error-filtering/`tn93-cluster` compression, `RapidNJ` and `raxml-ng` tree inference, and internal-branch `FEL`, `MEME`, and `SLAC` codon models in `HyPhy v2.5.31` via `RASCL`), the authors evaluate sliding 90-day global windows alongside clade-specific alignments. They report an inflection in November 2020 in the internal-branch-length-normalized density of positively and negatively selected sites across `S`, `nsp2`, and `nsp6`, identify 151 codons under positive selection along internal branches of V1/V2/V3 trees (including 28 non-signature sites with inter-lineage convergence, permutation $p \le 0.002$), validate fitness predictions out-of-sample by showing that 29 convergent mutations more than doubled in intra-lineage frequency between March 15 and June 1, 2021, and define a 35-site "501Y meta-signature." De-identified alignments, summary files, and interactive notebooks are publicly available via Zenodo (`10.5281/zenodo.5149112`), GitHub, and ObservableHQ.

The analytical pipeline establishes a rigorous standard for large-scale viral phylodynamics: restricting $d_N/d_S$ tests to internal branches (`--branches Internal`) suppresses terminal-branch sequencing artifacts and intra-host deleterious mutations, normalizing selected-site counts by internal tree length (`subs/site`) controls for sample-size growth, and splitting pre-March 15 phylogenetic discovery from post-March 15 frequency trajectories avoids lookahead leakage. Four modeling and framing issues nonetheless warrant attention: (1) retaining the clade-defining basal stem branch in the foreground of lineage-specific `MEME`/`FEL` analyses introduces circular ascertainment bias for signature mutations; (2) global $2\times 2$ contingency tables comparing pre- vs. post-March 15 allele frequencies do not stratify by country, leaving frequency ratios ($RR(M)$) vulnerable to geographic sampling shifts; (3) the evolutionary forecast that diverse SARS-CoV-2 lineages are converging toward a single 35-site 501Y fitness summit is contradicted by the simultaneous global sweep of B.1.617.2 (Delta), which matches only 1 of 35 meta-signature sites; and (4) the discussion proposes live-virus in-vitro co-infection and recombination passaging of V1, V2, and V3 under immune sera without addressing dual-use biosafety risks. All four points can be addressed through stratified re-analysis and text revisions.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Late-2020 Global Shift in Selective Pressures on SARS-CoV-2 Genes: Well Supported.**  
  In Figure 2A–B and Figure S1, tracking 90-day sliding windows from March 2020 to April 2021 and normalizing the count of `FEL`-selected sites ($p \le 0.01$) per kilobase per unit of internal tree length (excluding trees with $<0.5$ subs/site) demonstrates that the November 2020 rise in positive selection across `S`, `nsp2`, and `nsp6` is not an artifact of expanding sequence volume.

* **Internal-Branch Positive Selection & Inter-Lineage Convergence at 28 Non-Signature Sites: Well Supported.**  
  Restricting `MEME` and `FEL` to internal branches removes singleton errors and dead-end intra-host variants, and the authors explicitly exclude overlapping reading frames in `ORF3a` and `N` (Figure S1, STAR Methods page 14). Permutation tests conditioned on shared variable sites reject random overlap of positively selected non-signature sites across all three lineage pairs ($p < 0.001$ for V1/V2, $p = 0.002$ for V1/V3, $p = 0.002$ for V2/V3; page 7), and 18/28 sites independently show global `FEL` selection ($p < 0.05$, Figure S2).

* **Lineage-Specific Positive Selection at Clade-Defining Signature Sites (22/37 Sites): Moderately Supported / Ascertainment-Biased.**  
  As noted by the authors on page 5, V1, V2, and V3 were originally defined by the cluster of non-synonymous substitutions along their basal stem branches, and those basal branches were retained inside the foreground branch set tested by `MEME` and `FEL`. Conditioning clade definition on a set of basal amino acid changes and then including that basal branch in a $d_N/d_S$ test inflates the likelihood ratio test statistic for signature sites.

* **Out-of-Sample Corroboration via Post-March 15, 2021 Frequency Doubling (29/65 Sites): Moderately Supported.**  
  Testing mutations identified from internal branches prior to mid-March 2021 against intra-lineage frequency doubling ($RR(M) > 2.0$, Bonferroni-corrected $\chi^2$ test) between March 15 and June 1, 2021 (Table S2) avoids temporal data leakage. However, pooling sequences globally into a single unstratified $2\times 2$ table per lineage exposes $RR(M)$ to geographic confounding (Simpson's paradox) whenever sub-lineages carrying mutation $M$ circulate in countries whose share of global sequencing changes between the two periods.

* **Forecast of Broad Convergence onto the 35-Site "501Y Meta-Signature" Fitness Peak: Overstated.**  
  While sub-lineages within V1, V2, V3, B.1.526, and B.1.620 accumulated up to 10–16 meta-signature mutations through June 1, 2021 (Figure 5, Table S4), Table S3 and page 9 show that B.1.617.2 (Delta)—which was rapidly displacing V1, V2, and V3 globally by June 2021—has a modal match of just 1/35 meta-signature sites (maximum 3/35). This indicates that SARS-CoV-2 evolves on a multi-peak fitness surface where alternative mutation combinations (such as Spike L452R + T478K + P681R) can outcompete the 501Y trajectory.

* **Proposal for In-Vitro Live-Virus Co-Infection and Recombination of V1, V2, and V3 Under Immune Sera: Fragile / Unaddressed Biosafety Risk.**  
  On page 10, the authors propose replicated laboratory co-infections of live V1, V2, and V3 viruses in the presence of convalescent or vaccinee sera to select recombinant chimeras combining immune evasion, cell entry, and replication advantages. Proposing forward selection of replication-competent chimeric Variants of Concern without discussing gain-of-function / dual-use biosafety constraints is inappropriate.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Exclude Basal Stem Branches from Lineage-Specific `MEME`/`FEL` Foreground Tests
* **WHY:** Retaining the clade-defining basal branch in the foreground of V1, V2, and V3 `MEME`/`FEL` analyses (page 5) guarantees at least one non-synonymous substitution on a trunk branch at every signature site, biasing site-level $p$-values downward.
* **WHAT:** Separate selection acting *within* each clade after its emergence from the substitutions that defined the basal stem of the clade.
* **HOW:** Re-run `HyPhy` `MEME` and `FEL` on the V1, V2, and V3 `raxml-ng` trees with the foreground branch set (`--branches`) restricted strictly to descendant internal branches *above* the clade root (excluding the stem branch connecting V1/V2/V3 to the pre-October 2020 background), and update Figure 3 and Table S1 to indicate which of the 22 signature sites remain significant ($p \le 0.05$) from intra-clade recurrent substitutions alone.

#### 2. Stratify Pre/Post-March 15 Frequency Ratio Tests by Country/Region
* **WHY:** Unstratified global $2\times 2$ contingency tables (STAR Methods, "Calculating mutation frequency changes", page 15) can yield $RR(M) > 2.0$ purely from shifts in national sequencing proportions between pre-March 15 and March 15 – June 1, 2021.
* **WHAT:** Control for geographic sampling skew when testing whether convergent mutations increased in frequency within V1, V2, and V3.
* **HOW:** Group sequences by country (or major region: UK, continental Europe, USA, South Africa, Brazil) and compute a Cochran-Mantel-Haenszel (CMH) stratified common odds ratio and Bonferroni-adjusted $p$-value for each of the 65 sites in Table S2.

#### 3. Reconcile the Figure 3 Evolutionary Viability Metric with the `PRIME` Citation in STAR Methods
* **WHY:** The Figure 3 caption (page 6) states that amino acid block colors represent "model-based predictions of the probable evolutionary viability of the observed amino acid substitutions based on the numbers of times these substitutions have been observed in related coronaviruses that infect other host species," whereas STAR Methods (page 14) states this was computed "using the PRIME method `http://hyphy.org/w/index.php/PRIME` with default settings." In `HyPhy`, `PRIME` models physicochemical property-informed $d_N/d_S$ rate variation rather than outgroup amino acid frequency/exchangeability scoring.
* **WHAT:** Provide the exact mathematical definition and outgroup alignment used to compute the amino acid viability categories ("unprecedented", "highly unusual", "common") in Figure 3.
* **HOW:** Update STAR Methods (page 14) to specify the exact sarbecovirus/betacoronavirus reference alignment, the substitution or profile model executed in `HyPhy`, and the numerical thresholds that map log-odds or counts to white, red, and green blocks in Figure 3.

#### 4. Temper the Single-Peak Convergence Forecast and Replace the Live-Virus Recombination Proposal
* **WHY:** The minimal overlap between B.1.617.2 (Delta, modal match 1/35) and the 501Y meta-signature (page 9) shows that adaptive evolution is not restricted to a single 501Y peak, and breeding live V1/V2/V3 recombinants under immune selection (page 10) poses biosafety hazards.
* **WHAT:** Frame the 35-site meta-signature as a local adaptive trajectory conditional on the N501Y epistasis background, and recommend safe experimental alternatives.
* **HOW:** Revise the concluding section ("Where is the evolution of the 501Y lineages headed?", pages 8–10) to contrast the 501Y epistasis peak with competing non-501Y trajectories (such as B.1.617.2), and replace the live-virus co-infection passage proposal with combinatorial pseudovirus neutralization assays and deep mutational scanning (DMS).

#### 5. Technical, Mathematical, and Editorial Cleanup
* **WHY:** Several typographical errors in figure captions, site coordinates, and author names should be corrected.
* **WHAT & HOW:**
  * **Figure 4 caption (page 8):** Change `"between January and June 2001"` to `"between January and June 2021"`.
  * **Wild-type vs. mutant state typo (page 8 & STAR Methods page 15):** Change `"K417N/K"` to `"K417N/T"` (K is the ancestral reference amino acid; N and T are the convergent V2 and V3 mutations).
  * **Gene/site label typos:** On page 6, change `"S/655, S/681, A/701, and S/716"` to `"S/655, S/681, S/701, and S/716"`. On page 7, change `"Heicase/590I"` to `"Helicase/590I"` and `"ORF3/171L"` to `"ORF3a/171L"`.
  * **Figure 5 caption (page 9):** Change `"138HY"` to `"138H/Y"`.
  * **Author list & Lead Contact (pages 1 and 12):** Correct `"Anton Nekturenko"` to `"Anton Nekrutenko"`, and in Lead Contact correct `"Tulio de Oliviera"` to `"Tulio de Oliveira"`.
  * **Table S1 caption vs. STAR Methods method name:** Table S1 caption (page 18) and Figure 4 caption (page 8) refer to `"IFEL"`, whereas the main text (page 4) and STAR Methods (pages 13–14) state that `"FEL"` restricted to `--branches Internal` was used. Standardize the terminology to `"internal-branch FEL"`.
