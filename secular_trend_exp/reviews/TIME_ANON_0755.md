<Blinded Review: TIME_ANON_0755>
**Composite Score:** 5.6 / 10.0 (Rigor: 1.8/3.5 | Claims: 1.5/2.5 | Biology: 1.2/2.0 | Reproducibility: 1.1/2.0)
**Bias Category:** Algorithmic/Model
**Verdict:** Major Revision
**Study Modality:** Dry-Lab Secondary Cohort/Database
**Technology Maturity:** Mid-Stage High-Throughput
**Epistemic Stage:** Basic/Mechanistic Discovery

OVERALL_SCORE: 5.6/10
VERDICT: CAVEATS
ESTIMATED_DECADE: 2020s

---

### 1. Executive Summary / SUMMARY
This comparative plant genomics study surveys the origin and expansion of the R2R3-MYB transcription factor family across Archaeplastida and Chromista using 33 complete genomes (4 rhodophytes, 16 chlorophytes, 7 charophytes, and 6–7 embryophytes totaling 541 R2R3-MYB proteins) supplemented by 191 transcriptomes from the One Thousand Plant Transcriptomes (1KP) project. Using `HMMER 3.0` (`PF00249`) and maximum-likelihood phylogenetics (`PhyML`, `IQ-TREE`, and `FastTree`) restricted to the 102-amino-acid R2 and R3 repeats, combined with exon–intron phase mapping, the authors classify R2R3-MYB genes into three evolutionary subgroups (I, II, and III) and 22 clades, proposing that Subgroup III originated in the common ancestor of land plants (preserving a conserved phase-1/phase-2 two-intron structure) and underwent two major expansions. While the integration of newly sequenced charophyte genomes (*Klebsormidium nitens*, *Chara braunii*, *Spirotaenia*, *Coleochaete*, *Mesostigma*, *Chlorokybus*) provides useful resolution at the streptophyte-embryophyte transition, the study is weakened by severe phylogenetic under-information (inferring deep multi-kingdom trees of 541+ taxa from just 102 aligned amino acid sites), internal inconsistencies in species and gene counts in Table 1, and purely narrative "birth-and-death" expansion claims lacking formal gene-tree/species-tree reconciliation or duplication/loss modeling.

### 2. Methodological & Statistical Audit / STRENGTHS & WEAKNESSES

#### STRENGTHS
- **Broad Taxonomic Sampling Across Charophyte Lineages:** Including seven charophyte genomes alongside 191 1KP algal and bryophyte transcriptomes bridges the sampling gap between chlorophytes and embryophytes, demonstrating that Subgroup II emerged in streptophyte algae whereas canonical Subgroup III is restricted to embryophytes.
- **Orthogonal Validation via Intron Position and Phase:** Overlaying splice-site phases (phase 1 and phase 2 introns within the R2R3 coding domain) onto the sequence-based clades provides independent structural corroboration for the monophyly of Subgroup III across bryophytes, lycophytes, and angiosperms.

#### WEAKNESSES & METHODOLOGICAL AUDIT
- **Severe Phylogenetic Signal-to-Noise Limitation (102 Sites for $>540$ Taxa):** The ML phylogenies (`PhyML`, `IQ-TREE`, `FastTree`) are reconstructed from only **102 amino acid sites** spanning the R2 and R3 repeats across 541 sequences (and even more in the 1KP tree). Reconstructing 540+ branches and deep Precambrian nodes (rhodophytes vs. chlorophytes vs. streptophytes) from a 102-residue alignment is notoriously underpowered and prone to long-branch attraction and substitution saturation. Crucially, the manuscript text does not report the actual bootstrap support values for the defining backbone nodes (Subgroup I vs. I-D+II+III, Subgroup II+III, and the 22 clades), merely asserting that they are "well-supported."
- **Internal Table & Count Inconsistencies:**
  1. In the Results ("Three Subgroups of the R2R3-MYB Gene Family"), the text states: *"included four red algae (rhodophytes), 16 green algae (chlorophytes), and six charophytes (charophytes) (Table 1). Seven land plant species... were selected... including... Oryza sativa, and Arabidopsis thaliana (Table 1)."* However, **Table 1 lists 7 charophytes** (*Chlorokybus*, *Mesostigma*, *Klebsormidium*, *Coleochaete*, *Spirotaenia*, *Chara*, *Entransia*) and **only 6 land plants—*Arabidopsis thaliana* is completely omitted from Table 1!**
  2. Summing the `Total` column in Table 1 across the 32 listed species yields $3\times 4 + (3+5+8+8+5+4+4+4+1+4+7+8+4+4+7+11) + (6+2+17+9+7+8+1) + (21+48+33+16+51+105) = 12 + 87 + 50 + 274 = 423$ genes. Even adding the 126 *Arabidopsis thaliana* genes mentioned in the text ($423 + 126 = 549$), the total does not match the **541 R2R3-MYB proteins** claimed in the Methods and Results!
  3. In the Discussion, the authors write: *"(for example, over 80% of members in rice, Arabidopsis, and tea are distributed in subgroups III: Table 1)"*—yet tea (*Camellia sinensis*) is never analyzed in the paper or present in Table 1, and in *Arabidopsis* the text on line 106 explicitly stated that 93 out of 126 (**73.8%**, not $>80\%$) belong to Subgroup III.
- **No Formal Gene Family Evolution / Birth-and-Death Modeling:** Despite claiming a *"highly unbalanced pattern of birth and death evolution"* in the Abstract, the authors perform no formal birth-death rate estimation (`CAFE`, `Notung`, or `ALE` gene-tree/species-tree reconciliation) and do not correct for incomplete transcriptome assembly in the 1KP data or whole-genome duplication (WGD) events in angiosperms and mosses (*Physcomitrella patens*).
- **Strict HMM Filtering Bias Against Divergent Algal Homologs:** Requiring *only* two MYB domains separated by $<20$ aa with bit score $\ge 35$ against `PF00249` (which is heavily trained on seed plant MYBs) risks systematically under-counting divergent algal 2R-MYB proteins or misclassifying partial transcriptome contigs from 1KP where a third repeat was truncated.

### 3. Biological / Experimental Grounding & Claim Proportionality
- **Claim 1:** *Subgroup III R2R3-MYB genes with conserved phase-1/phase-2 introns are specific to land plants and expanded from ~15 ancestral clades in the embryophyte common ancestor.* `[Moderately Supported]` — Supported by the presence of bryophyte and tracheophyte sequences across the 15 III-A to III-O clades and shared intron phasing, though exact ancestral counts are sensitive to phylogenetic rooting and long-branch placement.
- **Claim 2:** *Subgroup III originated from Subgroup II before the split between land plants and charophytes, and experienced a first major expansion before the origin of land plants.* `[Methodologically Flawed]` — Internally contradictory: Table 1 shows **zero** Subgroup III genes in any of the 7 charophyte species, yet the Abstract and Discussion claim the first expansion of Subgroup III occurred *"before the origin of land plants"* and *"before the split between the land plants and charophytes"*, which would require all 15 clades to have been lost independently across every charophyte lineage or to have evolved on the embryophyte stem branch *after* splitting from charophytes.
- **Claim 3:** *The expansion of Subgroup III R2R3-MYBs drove the morphological and metabolic adaptation of land plants to terrestrial environments.* `[Overstated]` — Correlative evolutionary narrative without functional, expression, or selection ($dN/dS$) analyses.

### 4. Reproducibility & Data Completeness
- **Data & Accession Completeness:** The manuscript states that the 541 gene IDs and sequences are in Supplementary Table S1 and Supplementary Files 1–3, but exact genome assembly versions/builds for the 33 species and the specific 191 1KP sample codes are not listed in the main text.
- **Software Parameters:** `HMMER 3.0` (`PF00249`, Pfam 23.0, bit score $\ge 35$, inter-domain distance $<20$ aa), `MUSCLE v3.8.31`, `ProtTest` (`LG+G`), `PhyML 3.0`, and `IQ-TREE` (`-TEST -bb 1000`) are specified, though `FastTree` version and parameters are omitted, and tree files (Newick) are not deposited in TreeBASE or Dryad.
</Blinded Review: TIME_ANON_0755>
