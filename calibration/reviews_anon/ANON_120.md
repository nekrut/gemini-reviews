# Review of ANON_120

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **6.3 / 10.0** (Mixed / Salvageable)  
* **Score Breakdown:** Rigor: 1.9/3.5 | Claims: 1.6/2.5 | Biology: 1.5/2.0 | Reproducibility: 1.3/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This genomic epidemiology study investigates the emergence, reassortment, and spatial spread of highly pathogenic (HP) and low pathogenic (LP) avian influenza A/H7N9 in Guangdong province during the fifth epidemic wave (2016–2017). Through longitudinal surveillance of 34,106 environmental and poultry swabs across retail and wholesale live poultry markets (LPMs) in 21 prefecture-level cities (January 2016–August 2017), the authors detected 7,008 influenza A-positive samples (including 251 HP and 1,002 LP H7N9 positives) and sequenced complete genomes for 58 HP A/H7N9, 19 LP A/H7N9, and 220 A/H9N2 egg-passaged isolates. Combining these 297 newly generated genomes (deposited in GISAID; Supplementary Table S1) with 1,371 publicly available H7N9 genomes and poultry import records (5.5 billion birds), they perform maximum-likelihood (IQ-TREE) and Bayesian molecular clock / discrete phylogeographic (BEAST v1.8) analyses, define 180 eight-segment genotypes, and compare HA multibasic cleavage site motifs (V1–V7) and mammalian adaptation markers between environmental and human isolates.

The surveillance dataset and 297 whole-genome sequences represent a substantial empirical contribution that clearly demonstrates the co-circulation of three H7N9 lineages in Guangdong during Wave 5 (13% local Pearl River Delta LP, 23% newly imported Yangtze River Delta LP, and 64% YRD-derived Clade C-1 HP) and the pervasive replacement of PRD internal gene cassettes by imported YRD and local H9N2 segments. However, the manuscript's quantitative rigor and biological interpretations are weakened by: (1) contradictory geographic region definitions between Sections 2.4 and 2.5 and incomplete BEAST model specifications; (2) unadjusted comparisons of HA cleavage site variants (V1 vs. V3) and mammalian adaptive mutations (PB2 E627K/D701N, NA R292K) between human and LPM isolates that overlook geographic confounding, within-host human selection, and 2–3 passages in embryonated chicken eggs; and (3) arithmetic errors in Table 2 where column percentages exceed $100\%$ ($104.5\%$ and $102.2\%$). Addressing these statistical, methodological, and tabular issues will substantially strengthen the paper.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **During the fifth wave in Guangdong, HP A/H7N9 (Clade C-1) evolved from third/fourth-wave YRD-lineage LP viruses and co-circulated with local PRD-lineage LP (13%) and newly imported YRD-lineage LP (23%) viruses: [Well Supported].**  
  The phylogenetic topologies across all eight segments (Figs. 3–4, Supplementary Figs. S1–S3) and longitudinal LPM RT-PCR data (Table 1, pinpointing the earliest HP detection to Heyuan on 7 November 2016 prior to the first human case report) provide strong support for the origin of Clade C-1 HP H7N9 and the extensive internal-gene reassortment driven by poultry imports.

* **Genotype comparisons (15 of 19 fifth-wave HP genotypes present in Guangdong, 12 unique to Guangdong) indicate high local reassortment and limited outward spread of Guangdong-specific HP genotypes: [Moderately Supported].**  
  The eight-segment clade constellation analysis (180 genotypes total, 59 in Wave 5) documents extensive local reassortment with YRD-lineage LP and H9N2 internal genes. However, inferred migration directionality rests on discrete phylogeography in BEAST v1.8 (Section 2.5), for which key model parameters (clock model, coalescent prior, BSSVS Bayes factor support, and sensitivity to the 71% oversampling of Guangdong HP genomes relative to other provinces) are not reported, and the geographic grouping of Chinese provinces changes inconsistently between Section 2.4 and Section 2.5.

* **Differences in HA cleavage-site variant frequencies between LPMs (49.6% V1, 43.4% V3) and humans (93.7% V1, 2.1% V3) suggest the V1 motif facilitates poultry replication and human infection: [Fragile].**  
  First, no formal statistical test or confidence interval is provided for the V1 vs. V3 human-to-LPM comparison. Second, as shown in Figure 5 and Section 3.5, V1 circulated broadly across northern, eastern, western, and central Guangdong (matching the geographic distribution of human cases), whereas V3 was geographically restricted to central and eastern cities; without stratifying by prefecture/city and sampling month, geographic founder effects confound the association between the V1 motif and human infection.

* **Specific amino acid substitutions (HA G186I, Q226L/H; NA R292K; PB2 E627K, D701N) are exclusively found in human HP A/H7N9 and absent from environmental LPM isolates: [Moderately Supported].**  
  Table 2 accurately catalogs the absence of PB2 E627K/D701N, NA R292K, and HA Q226L in the 58 environmental sequences versus their presence in 4–35% of human sequences. However, the biological interpretation omits two crucial confounders: (1) all LPM swabs were blindly passaged for 2–3 generations in 9–10-day-old embryonated chicken eggs before sequencing (Section 2.2), a procedure known to rapidly select against mammalian receptor-binding (HA 226L) and polymerase (PB2 627K) variants present as minority populations in environmental swabs; and (2) NA R292K (oseltamivir resistance) and PB2 E627K/D701N routinely emerge *de novo* within infected patients during clinical course and antiviral treatment rather than reflecting the infecting LPM inoculum.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Reconcile Regional Definitions and Report Full BEAST Phylogeographic Specifications
* **WHY:** Section 2.4 classifies 29 Chinese provinces into *six* regions (placing Henan in Central, Fujian in Eastern, Shanxi in Northern, and Gansu in North-Western China), whereas Section 2.5 classifies them into *seven* regions (moving Henan to Northern, Fujian to Southeastern, Gansu to Southwestern, and Shanxi to Northwestern China, while restricting Southern China to Guangdong alone). Furthermore, Section 2.5 omits the molecular clock model, coalescent prior, burn-in, ESS thresholds, and BSSVS Bayes factors.
* **WHAT:** Harmonize the regional classification scheme across epidemiological poultry-import and phylogeographic analyses, and report complete BEAST v1.8 model details and subsampling sensitivity checks.
* **HOW:** Use a single consistent regional mapping in both Sections 2.4 and 2.5, specify the clock model (e.g., uncorrelated lognormal relaxed clock), tree prior (e.g., Bayesian Skygrid), MCMC burn-in (e.g., 10%), minimum ESS ($>200$), and BSSVS Bayes factor support for inferred migration transitions, and verify that Guangdong's role as a sink/source is robust to downsampling the Guangdong HP sequences.

#### 2. Perform Geographically Stratified Testing for HA Cleavage Site Variants (V1 vs. V3)
* **WHY:** Comparing pooled province-wide counts of V1 (45/48 human vs. 57/115 LPM) and V3 (1/48 human vs. 50/115 LPM) ignores the fact that V3 was absent from northern and western Guangdong where many human cases occurred (Fig. 5).
* **WHAT:** Test whether the enrichment of V1 in human cases persists when restricted to or stratified by the specific prefecture-level cities and months where both V1 and V3 co-circulated in LPMs.
* **HOW:** Construct $2 \times 2$ contingency tables (V1 vs. V3 in human vs. LPM isolates) stratified by prefecture-level city (using the city-level data in Fig. 5) and compute a Cochran–Mantel–Haenszel stratified odds ratio and exact $p$-value, reporting the result in Section 3.5.

#### 3. Discuss Egg-Passage Selection and Within-Host Adaptation for Table 2 Markers
* **WHY:** Passaging LPM samples 2–3 times in embryonated chicken eggs (Section 2.2) imposes avian host selection prior to sequencing, while clinical neuraminidase inhibitor therapy and mammalian body temperature select for NA R292K and PB2 E627K/D701N within human patients.
* **WHAT:** Add an explicit discussion in Section 4 acknowledging that the absence of HA Q226L and PB2 E627K/D701N in LPM isolates and the presence of NA R292K in human isolates reflect within-host mammalian/drug selection and potential avian egg-passage filtering rather than differences in the circulating LPM virus pool.
* **HOW:** Insert a paragraph in Section 4 (following the discussion of Table 2 mutations on line 217) citing established literature on within-host emergence of PB2 E627K and NA R292K in H7N9 patients and egg-adaptation bias during virus isolation.

#### 4. Correct Arithmetic Errors and Sample-Size Mismatches in Table 2
* **WHY:** In Table 2, several percentage calculations exceed $100\%$ because the numerator exceeds the column sample size stated in the table footnotes.
* **WHAT & HOW:**
  1. **Table 2, row `PB2 | Q591K | Q` (line 192):** Currently reads `46 (104.5)` under `Human HPAI H7N9 | V1` because footnote `b` sets the V1 denominator to $n = 44$ while the count is $46$ (the total human PB2 sample size). Change the V1 count to `44 (100)` so it matches the V1 sample size ($n = 44$).
  2. **Table 2, row `NA | E119V` (lines 172–173):** Under `Human HPAI H7N9 | V1` ($n = 45$), `E` is listed as `45 (100)` and `V` as `1 (2.2)` (summing to $46/45 = 102.2\%$), whereas under `Total` ($n = 48$), `E` is `47 (97.9)` and `V` is `1 (2.1)`. Correct the V1 `E` count from `45 (100)` to `44 (97.8)`.

#### 5. Technical, Mathematical, and Editorial Cleanup
* **WHY:** Date inconsistencies and numerous typographical errors detract from the presentation.
* **WHAT & HOW:**
  1. **Section 3.1 (line 60):** Reconcile *"from January 2016–August 2017"* with *"isolated from LPMs and poultry from November 2016 to November 2017"* in the same paragraph.
  2. **Typographical fixes:** Correct *"nineteenwere"* $\to$ *"nineteen were"* (Section 2.2, line 30); *"twennty-nine"* $\to$ *"twenty-nine"* (Section 2.4, line 40); *"ffifty-nine"* $\to$ *"fifty-nine"* (Section 3.3, line 133); *"Data availiablility"* $\to$ *"Data availability"* (Section 5, line 227); *"Authors contributors"* $\to$ *"Author contributions"* (line 232); and *"Pathogenic Microbiolgy"* $\to$ *"Pathogenic Microbiology"* (lines 256–270).
