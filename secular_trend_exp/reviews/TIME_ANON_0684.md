<Blinded Review: TIME_ANON_0684>
**Composite Score:** 7.5 / 10.0 (Rigor: 2.4/3.5 | Claims: 2.0/2.5 | Biology: 1.6/2.0 | Reproducibility: 1.5/2.0)
**Bias Category:** Algorithmic/Model
**Verdict:** Minor Revision
**Study Modality:** Hybrid Computational + Wet-Lab
**Technology Maturity:** Mature/Classical
**Epistemic Stage:** Basic/Mechanistic Discovery

OVERALL_SCORE: 7.5/10
VERDICT: PASS
ESTIMATED_DECADE: 2000s

---

### 1. Executive Summary / SUMMARY
This systematic and molecular phylogenetic study reconstructs the evolutionary relationships of 69 species of social paper wasps across all four tribes of the subfamily Polistinae (Hymenoptera: Vespidae)—Polistini (33 species of *Polistes*), Epiponini (22 species), Mischocyttarini (7 species), and Ropalidiini (7 species)—by combining 95 adult/larval morphological and behavioral characters with 488 bp of mitochondrial `COI` DNA sequence, 311 bp of single-copy nuclear flanking sequence from three microsatellite loci (`Pbe216AAG`, `Pbe269bAAG`, `Pbe411AAT`), and 38–39 binary characters coding the presence/absence of substituted trinucleotide repeat motifs within those microsatellites. Using maximum parsimony (`PAUP* 4.0b10`, `Winclada`/`Nona` parsimony ratchet with 1,000 bootstrap replicates), the authors show that while morphology alone resolves subgenera/genera with poor species-level resolution and molecules alone resolve terminal species clades with weaker deep support, the combined "total evidence" dataset strongly supports the monophyly of New World *Polistes* (62% bootstrap) nested within a paraphyletic Old World *Polistes* grade (with *Polistes sensu stricto* basal at 92–98% bootstrap), supports the monophyly of individual *Polistes* subgenera (*Megapolistes* 99%, *Polistella* 93%, *Polistes s.s.* 92%, *Fuscopolistes* 99%, *Aphanilopterus* 96%, *Epicnemius* 70%), and supports the monophyly of Ropalidiini (83%), Mischocyttarini (95%), and Epiponini (90%), while finding the large swarm-founding genus *Polybia* unresolved/paraphyletic. This work provides a well-curated comparative framework for testing kin-selection and cyclical oligogyny hypotheses across social wasps.

### 2. Methodological & Statistical Audit / WEAKNESSES & METHODOLOGICAL AUDIT
- **Reciprocal Ingroup/Outgroup Rooting Without an External Non-Polistinae Outgroup:**
  - Rather than rooting the 69-species Polistinae dataset with an external outgroup from another vespid subfamily (such as Vespinae or Stenogastrinae), the authors split the tree into two reciprocally rooted analyses: Figures 1–3 root the 33 Polistini species using the 36 Mischocyttarini + Ropalidiini + Epiponini species as outgroups, whereas Figures 4–6 root the 36 Mischocyttarini + Ropalidiini + Epiponini species using the 33 Polistini species as outgroups (`Line 74`, `Line 153`).
  - While prior morphological cladistics established Polistini as the sister group to the remaining three tribes (`Figure 8`), reciprocal rooting along the internal branch connecting Polistini to `(Ropalidiini + Mischocyttarini + Epiponini)` assumes *a priori* that both halves are reciprocally monophyletic with respect to the root of Polistinae and leaves the basal branching order among Ropalidiini, Mischocyttarini, and Epiponini unresolved (`Figure 6`).
- **Homoplasy and Independence Concerns in Binary Coding of Microsatellite Repeat Motifs:**
  - In addition to the 311 bp of single-copy flanking regions, the authors coded 38–39 binary presence/absence characters representing specific point-mutated trinucleotide motifs (e.g., `GGA`, `AAA`, `TAA`, `GCA` substituting for `AAG` inside the tandem repeat array; `Line 158`). Because tandem microsatellite arrays undergo frequent replication slippage, unequal crossing-over, and recurrent point mutations, presence of an `AAA` or `GGA` triplet within a hypervariable repeat array across distantly related tribes diverged $>80\text{ Mya}$ carries a high risk of homoplasy and non-independence.
- **Unweighted Parsimony on Protein-Coding `COI` and Manual Alignment Tweaking (`Malign`):**
  - Sequence alignments were generated under parsimony alignment (`Malign` with a 3:1 change:gap ratio) followed by manual adjustment "by eye" (`Line 168`). Although the authors note (`Line 173`, `Line 175`) that excluding 3rd codon positions of `COI` or running Maximum Likelihood and Distance analyses did not conflict with the equal-weights parsimony topology, no explicit nucleotide substitution model (`GTR+I+G`), ML bootstrap values, or partitioned Bremer support/incongruence length difference (ILD) tests are shown.
- **Minor Arithmetic Discrepancy Between Text (`Line 158`) and `Table 2` (`Line 185`):**
  - In the Methods text (`Line 158`), the authors report a total of **932 characters**, consisting of `95` morphological + `488` COI + `311` microsatellite flanking + `38` repeat-region characters ($16 + 15 + 7 = 38$; $95 + 488 + 311 + 38 = 932$). However, `Table 2` (`Line 185`) lists `Total # of Characters` for `Repeat Region` as **39** (yielding a sum of $933$ characters).
  - Also, `Table 1` (`Lines 29–63`) is truncated in the published layout after *Mischocyttarus immarginatus* (showing 34 of the 69 species: the 32–33 *Polistes* and 2 *Mischocyttarus* species, omitting the remaining Epiponini and Ropalidiini rows).

### 3. Biological / Experimental Grounding & Claim Proportionality / STRENGTHS
- **[Well Supported] Complementarity of Nuclear Microsatellite Flanking Sequences, mtDNA `COI`, and Morphology:** The side-by-side comparison of bootstrap trees from morphology alone (`Figures 1, 4`), molecular data alone (`Figures 2, 5`), and combined total evidence (`Figures 3, 6`) transparently demonstrates how morphological characters stabilize deep tribal/subgeneric nodes while `COI` and nuclear microsatellite flanks resolve terminal species relationships.
- **[Well Supported] Monophyly of New World *Polistes* and Basal Paraphyly of Old World *Polistes*:** The combined phylogeny robustly supports New World colonization from Old World ancestors and resurrects monophyletic support for New World subgenera (*Fuscopolistes* 99%, *Aphanilopterus* 96%, *Epicnemius* 70%) that had previously been synonymized due to unresolved morphological trees.
- **[Well Supported] Phylogenetic Distribution of Cyclical Oligogyny Across Epiponini:** Mapping the 8 studied swarm-founding genera (*Parachartergus*, *Protopolybia*, *Brachygastra*, *Polybia*, *Agelaia*, *Synoeca*, *Metapolybia*) onto the Epiponini tree confirms that worker-enforced cyclical oligogyny spans the basal-most lineages of the tribe.

### 4. Reproducibility & Data Completeness
- **Reproducibility Assessment:** Excellent open-data practices for its era: all newly generated nuclear microsatellite sequences (`AF119623–AF119660`, `AF120355–AF120455`) and mitochondrial `COI` sequences (`AY382200–AY382265`) are deposited in GenBank, and the complete aligned character matrix is publicly deposited in `TreeBASE` under submission ID `SN1595`.
</Blinded Review: TIME_ANON_0684>
