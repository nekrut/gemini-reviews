# Review of PMC7174922 (PMID:32321524)

**Manuscript Title:** Emerging SARS-CoV-2 mutation hot spots include a novel RNA-dependent-RNA polymerase variant  
**Authors:** Pachetti M, Marini B, Benedetti F, Giudici F, Mauro E, Storici P, Masciovecchio C, Angeletti S, Ciccozzi M, Gallo RC, Zella D, Ippodrino R.  
**Journal / Preprint:** *J Transl Med* (2020; `PMC7174922` / `PMID:32321524` / `10.1186/s12967-020-02344-6`)  
**Calibration Study Cohort:** Cohort A — Known Invalid / Refuted (`A39` | Double-Blinded as `ANON_136`)  
**Overall Score:** **3.6 / 10.0** (Flawed / Overstated)  
* **Score Breakdown:** Rigor: 1.0/3.5 | Claims: 0.8/2.5 | Biology: 0.8/2.0 | Reproducibility: 1.0/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript analyzes 220 complete SARS-CoV-2 genome sequences retrieved from GISAID between December 2019 and March 13, 2020 across Asia ($n = 71$), Oceania ($n = 15$), Europe ($n = 101$), and North America ($n = 33$) by aligning them against the Wuhan-Hu-1 reference genome (`NC_045512`). The authors catalog 13 recurrent variants (occurring $>10$ times in the dataset) across geographic regions and collection time windows, highlighting the co-occurrence of positions `3036` (`C3037T`), `14408` (`C14408T`, RdRp/nsp12 P323L), `23403` (`A23403G`, Spike D614G), and `28881` in Europe, and positions `17746` (`C17747T`), `17857` (`A17858G`), and `18060` (`C18060T`) in North America. Comparing post-February 9 genomes carrying the `14408` RdRp mutation ($n = 53$) against those without it ($n = 84$), they report a higher median number of point mutations per genome (3 vs. 1, Mann–Whitney $p < 0.001$) and conclude that the `14408` mutation is associated with an increased viral mutation rate and potential drug resistance. No list of the 220 GISAID accession IDs (`EPI_ISL_...`) or analysis scripts is provided.

While this early-pandemic descriptive survey accurately noted the geographic rise of the European B.1 lineage (`C3037T` + `C14408T` + `A23403G`) and the North American WA1 sublineage (`C17747T` + `A17858G` + `C18060T`), its central statistical and biological conclusion—that the `14408` RdRp mutation causes or is associated with an "overall increased mutation rate"—rests on a fundamental phylogenetic and algebraic artifact. Specifically, the authors count total nucleotide differences from the December 2019 Wuhan reference genome without subtracting the shared ancestral clade-defining mutations (`3036`, `14408`, `23403`) or accounting for phylogenetic non-independence. As the authors' own control analysis in the Results shows, conditioning on *any* derived clade marker—including synonymous mutations `3036` or `18060` in genomes lacking `14408`—yields the exact same median of 3–4 mutations ($p < 0.001$) simply because derived epidemic clades sampled in February–March 2020 are separated from the December 2019 root by 3–4 founder substitutions. In addition, the manuscript contains several gene annotation and coordinate errors (e.g., claiming position `11083` in `nsp6` is "outside the ORF sequence" and misassigning `17746`/`17857` to a non-existent `nsp143` instead of `nsp13` helicase) and numerical contradictions in reported ranges.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Distinct sets of linked SARS-CoV-2 mutations predominated in Europe (`3036`, `14408`, `23403`, `28881`) versus North America (`17746`, `17857`, `18060`) during February–March 2020: [Well Supported].**  
  Despite 1-bp coordinate shifts in the alignment (see Section 3 below), the descriptive frequency tracking across the 220 GISAID genomes (Figures 1–3) correctly captures the founder haplotypes that dominated early European transmission (Pangolin lineage B.1) and early Washington State/North American transmission (lineage A.1).

* **Viruses carrying the `14408` RdRp mutation have a significantly higher mutation rate than viruses lacking `14408` (median 3 vs. 1 point mutations, $p < 0.001$): [Methodologically Flawed].**  
  The comparison in Figure 4 and the Section *"Simultaneous occurrence of RdRp mutation with other mutations"* is invalidated by three compounding errors:
  1. **Inclusion of the conditioning mutation and linked founder haplotype:** Group 1 ($n = 53$) is defined by the presence of `14408`, which was co-inherited on a single ancestral branch alongside `3036` (`C3037T`) and `23403` (`A23403G`). Counting raw distance from the Wuhan root (`NC_045512`) includes `14408` itself ($+1$ by definition) plus its two co-inherited founder mutations ($+2$), automatically guaranteeing that nearly all Group 1 genomes have $\ge 3$ mutations from the root even if zero new mutations occurred after the B.1 founder event.
  2. **Phylogenetic pseudoreplication:** The 53 genomes in Group 1 are non-independent descendants of a single evolutionary branch; treating them as 53 independent observations in a Mann–Whitney test or Fisher's exact test violates statistical independence.
  3. **Refutation by internal synonymous controls:** One paragraph later, the authors perform the exact same Mann–Whitney test for genomes carrying `3036` (synonymous in `nsp3`), `23403` (`S`), `28881` (`N`), or the North American triad `17746`, `17857`, and `18060` (synonymous in `nsp14`, in genomes *without* the `14408` RdRp mutation), and find the exact same result: *"Genomes carrying mutations in positions 3036, 23403, 28881, 17746, 17857 and 18060 show a median of 3–4 mutations (range [2:5]), whereas genomes carrying none of them have a median of 1 or 2 mutations (range [0:3], p-value < 0.001)."* This demonstrates that having 3–4 differences from the Wuhan reference is a generic property of any derived lineage sampled in February–March 2020 (molecular clock accumulation over 2–3 months), not a mutator phenotype specific to `14408`.

* **The `14408` (P323L) RdRp mutation may impair ExoN proofreading interaction and confer resistance to RdRp inhibitors (such as remdesivir, favipiravir, or simeprevir): [Overstated].**  
  The manuscript provides no biochemical, structural docking, or phenotypic assay data. Residue P323 in `nsp12` lies in the interface domain far from both the polymerase active site (targeted by nucleotide analogs like remdesivir and favipiravir) and the `nsp14` ExoN proofreading active site. While framing P323L as a hypothesis for future functional work is reasonable, stating in the Conclusions that *"one mutation in position 14408 is located within the RdRp protein and is associated with an overall increased mutation rate"* overstates a phylogenetic founder correlation as evidence of altered enzyme fidelity.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Test for Evolutionary Rate Differences Using Tip-to-Ancestor Branch Lengths rather than Root Distance
* **WHY:** Counting raw nucleotide differences from the December 2019 Wuhan reference genome confounds the age of a clade's founder haplotype (3–4 linked substitutions in both the European B.1 clade and the North American A.1 clade) and sampling date with the intrinsic per-replication mutation rate.
* **WHAT:** Measure the number of *post-founder* private mutations (or estimate tip-to-root regression slopes over calendar time) after subtracting the shared clade-defining founder haplotype.
* **HOW:** Reconstruct a maximum-likelihood phylogenetic tree of the 220 genomes (e.g., using `IQ-TREE` + `TreeTime` or `TempEst`). To test whether the `14408` (B.1) clade accumulates mutations faster than non-`14408` clades, either (a) compare the number of additional *singleton/private* mutations accumulated downstream of the `C3037T + C14408T + A23403G` ancestral node against the number of private mutations downstream of the North American `C17747T + A17858G + C18060T` ancestral node matched for collection date, or (b) test for a difference in the molecular clock slope (substitutions per site per year) between `14408`-positive and `14408`-negative lineages.

#### 2. Correct Nucleotide Coordinates and Gene/ORF Annotations Against `NC_045512.2`
* **WHY:** Clustal Omega alignment without anchoring to the exact `NC_045512.2` coordinate frame introduced a $-1\text{ bp}$ shift at several canonical sites, and several genes are misannotated in the Results.
* **WHAT & HOW:**
  * **Coordinate Offsets:** Verify and update the 1-bp shifted coordinates against the standard Wuhan-Hu-1 reference (`NC_045512.2`): `3036` $\to$ `3037` (`C3037T`, synonymous in `nsp3`), `17746` $\to$ `17747` (`C17747T`, P504L in `nsp13`), `17857` $\to$ `17858` (`A17858G`, Y541C in `nsp13`), and `26143` $\to$ `26144` (`G26144T`, G251V in `ORF3a`).
  * **Misannotation of Position `11083`:** In Results ("Identification of recurrent mutation hotspots"), correct the statement *"whereas one mutation (position 11083) was outside the ORF sequence"*—position `11083` (`G11083T`) lies inside coding `ORF1a` (`nsp6`, causing amino acid substitution L37F), not in a non-coding region.
  * **Misannotation of Positions `17746` and `17857`:** In the same paragraph, replace the typo *"17746 and 17857 nsp143"* with *"nsp13 (helicase)"* (in `NC_045512.2`, `nsp13` spans nucleotides 16,237–18,039, whereas `nsp14` begins at 18,040).
  * **Missing Amino Acid Change for Position `2891`:** Add the amino acid substitution for `2891` (`G2891A`, A58T in `nsp3` / `ORF1a`) to the list of non-synonymous changes in the Results, and change *"3 out of the 12 most frequent mutations"* to *"3 out of the 13 most frequent mutations"* (since 8 novel + 5 previously reported = 13 mutations).

#### 3. Reconcile Internal Numerical Contradictions and Provide GISAID Accession IDs
* **WHY:** The mutation count range reported for Group 2 in the Abstract, Results, and Figure 4 caption contradicts the detailed breakdown in the text, and GISAID terms of use and scientific reproducibility require listing the analyzed accession numbers.
* **WHAT & HOW:**
  * **Group 2 Range (`[0–3]` vs. `[0–6]`):** In the Abstract, Results, and Figure 4 caption, the authors state that viruses without the RdRp mutation have *"a median of 1 mutation [range: 0–3]"*, yet in the preceding paragraph (Results, *"Simultaneous occurrence of RdRp mutation..."*) they explicitly state that Group 2 contains *"9 genomes [with] four mutations (10.7%), 2 and 3 genomes [with] five and six mutations respectively (2.4% and 3.6%)."* Change `[range: 0–3]` to `[range: 0–6]` (or state clearly if `[0–3]` represents the interquartile/trimmed range).
  * **Figure 2 Caption vs. Text:** Change *"5 period subgroups"* in the Figure 2 caption to *"6 period subgroups"* to match the six date intervals listed in the sentence and main text.
  * **Background Reference [33]:** In the Discussion, *"Ponatinib [33]"* cites reference 33, which in the Results was cited for previously reported SARS-CoV-2 sequence hotspots (`[23–25, 33]`). Verify and fix the citation numbering.
  * **GISAID Accession Table:** Add a supplementary table listing the 220 GISAID `EPI_ISL` accession numbers, collection dates, and originating/submitting laboratories.
