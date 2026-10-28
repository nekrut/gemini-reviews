# Review of PMC7166400 (PMID:31994738)

**Manuscript Title:** The 2019-new coronavirus epidemic: Evidence for virus evolution  
**Authors:** Benvenuto D, Giovanetti M, Ciccozzi A, Spoto S, Angeletti S, Ciccozzi M.  
**Journal / Preprint:** *J Med Virol* (2020; `PMC7166400` / `PMID:31994738` / `10.1002/jmv.25688`)  
**Calibration Study Cohort:** Cohort A — Known Invalid / Refuted (`A38` | Double-Blinded as `ANON_94`)  
**Overall Score:** **2.3 / 10.0** (Fundamentally Invalid)  
* **Score Breakdown:** Rigor: 0.5/3.5 | Claims: 0.6/2.5 | Biology: 0.6/2.0 | Reproducibility: 0.6/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This short report presents a preliminary phylogenetic, selection, and homology-modeling analysis of 15 early SARS-CoV-2 (`2019-nCoV`) whole-genome sequences alongside 5 SARS-CoV, 2 MERS-CoV, and 5 bat SARS-like coronavirus genomes ($N = 27$ total). The authors construct a maximum-likelihood whole-genome phylogeny in `MEGA-X` (`GTR+G+I`), run Fast Unconstrained Bayesian Approximation (`FUBAR`) on the `Datamonkey` server to test for selection in the N, S, E, and M coding regions, and build `SWISS-MODEL` homology models of the `2019-nCoV` Nucleocapsid (N; template PDB `2jw8.1`) and Spike (S; template PDB `6acc.1`) proteins. They report that `2019-nCoV` clusters with the 2015 bat SARS-like coronavirus isolate `MG772934.1`, claim "significant ($P < .05$) pervasive episodic selection" at sites 380 and 410 (or 409) in N and sites 536 and 644 in S, and argue that these mutations and structural differences explain cross-species transmission from bats to humans and lower pathogenicity relative to SARS-CoV.

While the whole-genome phylogeny correctly places `2019-nCoV` within the *Sarbecovirus* subgenus near bat SARS-like coronavirus `MG772934.1` (and separate from MERS-CoV), the evolutionary selection and structural modeling analyses contain fundamental methodological and factual errors that invalidate the main conclusions. Specifically, the authors mischaracterize `FUBAR` (a Bayesian pervasive selection method that outputs posterior probabilities, not frequentist $P$-values or "episodic" selection), conflate nucleotide positions with amino acid positions, contradict themselves within the same paragraph regarding which amino acids occupy positions 380 and 409/410 of the N protein, and misinterpret fixed inter-clade divergence across highly divergent betacoronaviruses (including MERS-CoV) as ongoing positive selection in `2019-nCoV`. Furthermore, the N protein homology model uses a partial C-terminal domain NMR template (`2jw8.1`, covering only ~118 of 419 residues, `GMQE = 0.17`) that does not even span residue 380. Complete re-analysis using codon-aware sarbecovirus alignments, branch-site selection models, and full-length structural templates is required.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Maximum-likelihood whole-genome phylogenetic analysis shows that `2019-nCoV` clusters within *Sarbecovirus* (clade IIa) closely related to bat SARS-like coronavirus `MG772934.1` and distinct from SARS-CoV and MERS-CoV: [Well Supported].**  
  The phylogenetic grouping of the 15 early `2019-nCoV` genomes with bat SARS-like coronavirus `MG772934.1` (`bat-SL-CoVZC45`) relative to SARS-CoV and MERS-CoV is consistent with basic coronavirus taxonomy, although aligning whole genomes across distinct subgenera (*Merbecovirus* MERS-CoV vs. *Sarbecovirus* SARS-CoV/2019-nCoV) in `BioEdit` without codon-aware partitioning introduces substantial non-homologous alignment regions.

* **`FUBAR` analysis identifies statistically significant ($P < .05$) "pervasive episodic selection" at sites 380 and 410 (or 409) of the N region and sites 536 and 644 of the S region: [Methodologically Flawed].**  
  This analysis fails on four levels:
  1. **Statistical metric:** `FUBAR` (Murrell et al., 2013) is a Bayesian hierarchical method that computes posterior probabilities ($\Pr(\beta > \alpha \mid \text{data})$), typically called at $\ge 0.90$; it does not compute frequentist $P$-values ($P < .05$), nor does it test for *episodic* selection (which requires `MEME` or `aBSREL`).
  2. **Coordinate and residue self-contradiction:** In Results line 52, the authors refer to `"two sites (380th and 410th nucleotide position... On the 380th aminoacidic position...)"`, conflating nucleotide and codon coordinates. Worse, line 52 first states that at N position 380 there is `"a glutamine residue instead of an asparagine residue"` and at position 410 `"a threonine residue instead of an alanine residue"`, and then two sentences later states the exact opposite: that at position 409 there is `"glutamine instead of an asparagine residue"` and at position 380 `"a threonine residue instead of an alanine"`.
  3. **Taxonomic scope and $dS$ saturation:** Running a site-level codon model across an alignment combining MERS-CoV, SARS-CoV, bat sarbecoviruses, and 15 virtually identical `2019-nCoV` genomes violates synonymous substitution stationarity and mistakes deep inter-species divergence for adaptive evolution within `2019-nCoV`.
  4. **Arithmetic inconsistency in site counts:** In line 52, 6 negatively selected sites in N are described as `"six sites (14%)"` (which would imply the N gene is only $6 / 0.14 = 43$ codons long, whereas `2019-nCoV` N is 419 codons long!).

* **Homology modeling of the N protein (using template `2jw8.1`) and S protein (using template `6acc.1`) reveals structural differences—including an absent $\alpha$-helix at N residue 380 and two novel $\beta$-sheets (`401:KYR` and `440:LND`) in S—that explain bat-to-human transmission and lower pathogenicity: [Methodologically Flawed].**  
  First, PDB `2jw8.1` is an NMR structure of the SARS-CoV N C-terminal dimerization domain spanning only residues 248–365 (~28% of the 419-residue protein), which explains the extremely poor global model quality (`GMQE = 0.17`, `QMEAN = -2.43`, line 58). Because `2jw8.1` terminates at residue 365, it does not cover residue 380 (which resides in the intrinsically disordered C-terminal tail); any visual difference around residue 380 in `SWISS-MODEL`/`PyMOL` is an unmodeled boundary artifact. Second, inferring "enhanced pathogenicity than the bat-like SARS coronavirus but lower pathogenicity than SARS coronavirus" (line 81) from unvalidated static homology models of single amino acid differences has no biophysical or experimental basis.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Re-Run Codon Selection Analyses Using Proper Branch-Site Models on a *Sarbecovirus*-Only Alignment
* **WHY:** `FUBAR` estimates site-wide pervasive $\omega = dN/dS$ across an entire tree and outputs Bayesian posterior probabilities, not $P$-values. Including MERS-CoV saturates $dS$, and including 15 nearly identical human `2019-nCoV` sequences provides no information on the specific branch leading to `2019-nCoV`.
* **WHAT:** Restrict the codon alignments of S, N, E, and M to *Sarbecovirus* sequences (excluding MERS-CoV and duplicate identical human isolates) and use `MEME` or `aBSREL` in `HyPhy`/`Datamonkey` to test the branch leading to `2019-nCoV`.
* **HOW:** Generate in-frame codon alignments for each ORF using `MACSE` or `MAFFT` on translated protein sequences back-translated to codons. Run `FUBAR` (reporting sites with posterior probability $\ge 0.90$ for pervasive selection) and `MEME` (reporting sites with likelihood ratio test $P < 0.05$ for episodic diversifying selection along the `2019-nCoV` stem branch).

#### 2. Correct the Self-Contradictory Residue and Coordinate Descriptions in the N and S Genes
* **WHY:** Conflating nucleotide positions with amino acid positions and stating two mutually contradictory amino acid substitutions for N position 380 within the same paragraph (line 52) makes it impossible to verify which sites were analyzed.
* **WHAT:** Map all reported positions strictly to `Wuhan-Hu-1` (`MN908947.3`) amino acid coordinates for each mature protein (N: 1–419 aa; S: 1–1273 aa) and remove the duplicated/contradictory text in Section 3.
* **HOW:** Tabulate the exact codon number, nucleotide coordinates in `MN908947.3`, reference amino acid in `MN908947.3`, `MG772934.1`, and `NC_004718.3` (SARS-CoV), synonymous rate $\alpha$, non-synonymous rate $\beta$, and posterior probability for each reported site. Also correct `"six sites (14%)"` in line 52 by dividing 6 by the actual number of codons in the N alignment ($6 / 419 = 1.4\%$).

#### 3. Restrict N Protein Structural Comparisons to the Template-Covered Domain (`248–365`)
* **WHY:** PDB `2jw8.1` covers only the C-terminal dimerization domain (residues 248–365) and has a whole-protein `GMQE` of 0.17; it cannot be used to model structural changes at position 380 or across the full-length 419-aa nucleocapsid protein.
* **WHAT:** Model the N protein N-terminal RNA-binding domain (NTD, e.g., PDB `2ofz` / `1ssk`) and C-terminal dimerization domain (CTD, PDB `2jw8`) separately, and remove structural claims for disordered regions outside template coverage (such as residue 380).
* **HOW:** Report template coverage ranges, local `QMEANDisCo` scores, and sequence identity for the N-NTD and N-CTD models separately, and verify that any highlighted secondary-structure differences in Figures 2 and 3 occur at residues with high local confidence rather than loop-building artifacts.

#### 4. Remove Unsupported Pathogenicity Claims and Uncritical Snake-Reservoir Speculation
* **WHY:** Sequence alignment and homology modeling cannot determine clinical severity or pathogenicity, and the codon-usage snake reservoir hypothesis (`Ji et al.`, cited in line 83) is an artifact of comparing viral dinucleotide composition against a limited vertebrate database.
* **WHAT:** Remove claims that N and S substitutions confer "lower pathogenicity than SARS coronavirus" (line 81) and remove or critically qualify the snake reservoir paragraph (line 83).
* **HOW:** Revise the Discussion (lines 81–85) to state solely that sequence differences in the S receptor-binding region distinguish `2019-nCoV` from SARS-CoV and `MG772934.1` and warrant experimental receptor-binding characterization.

#### 5. Technical and Editorial Cleanup
* **WHY:** The Abstract and Highlights contain numerous typographical errors and contradictory sequence counts.
* **WHAT & HOW:**
  1. **Sequence count contradiction (Abstract line 8 vs. Methods line 33):** The Abstract states `"using the 15 available whole genome sequences of 2019-nCoV, 12 whole genome sequences of 2019-nCoV, and 12 highly similar whole genome sequences"` (repeating `2019-nCoV` twice with 15 and 12), whereas the Methods state 15 `2019-nCoV` + 5 SARS + 2 MERS + 5 bat SARS-like = 27 sequences. Delete the duplicate `"12 whole genome sequences of 2019-nCoV,"` from the Abstract.
  2. **Spelling errors (Abstract and Highlights, lines 8–21, and Figure 2 caption, line 72):** Correct `"trasmitted"` to `"transmitted"` (line 8), `"epdiemic"` to `"epidemic"` (line 17), `"favured"` to `"favored"` (line 21), `"cross-sepcies tramsnimssion"` to `"cross-species transmission"` (line 21), `"and e positional difference"` to `"and a positional difference"` (line 72), and `"subgenuses"` to `"subgenera"` (line 79).
