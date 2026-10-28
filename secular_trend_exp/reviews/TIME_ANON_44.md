# Blinded Review: TIME_ANON_44
**Composite Score:** 2.8 / 10.0 (Rigor: 0.6/3.5 | Claims: 0.7/2.5 | Biology: 0.7/2.0 | Reproducibility: 0.8/2.0)
**Bias Category:** Ascertainment Confounding, Deduplication Bias & Basic Unit/Coordinate Errors
**Verdict:** Reject
**Study Modality:** Dry-Lab Secondary Cohort/Database Re-Analysis
**Technology Maturity:** Mature/Classical
**Epistemic Stage:** Clinical/Epidemiological Observational

---

### 1. Executive Summary

This manuscript downloads 579 complete SARS-CoV-2 genome sequences collected in the United States over an 11-week period (19 January to 15 April `[YEAR]`) from NCBI GenBank, removes identical ("redundant") sequences and sequences containing ambiguous bases, and analyzes the remaining 196 unique sequences relative to the Wuhan-Hu-1 reference genome (`NC_045512`). The authors construct a maximum-likelihood tree in MEGA-X, divide the genome into six 5-kb segments, compute weekly "mutation frequencies" (defined as total nucleotide or amino acid differences from Wuhan-Hu-1 divided by the number of retained sequences in that week), and catalog amino acid variants across viral proteins. Based on these counts, the authors conclude that the viral mutation rate increased sharply in weeks 7–10, that ORF8 and Helicase (nsp13) have the highest mutation rates, and that proteins with zero observed mutations (nsp7, nsp9, nsp10, nsp11, E, ORF6, ORF7b) are evolutionarily conserved due to essential functions in promoting local host inflammation.

The manuscript is fundamentally invalid due to elementary methodological, mathematical, and virological errors. First, removing identical sequences ("redundancy removal" reducing 579 genomes to 196 unique haplotypes) before computing weekly mutation frequencies destroys the denominator of population frequency calculations and guarantees an artificial inflation of per-sequence divergence. Second, the authors conflate cumulative phylogenetic distance from the root (`NC_045512`) with the weekly *de novo* mutation rate, mistaking the introduction of European Clade 20A/20C lineages (`D614G` + `P323L` + `Q57H` + `T85I`) into the US for an acceleration in the intrinsic viral mutation rate. Third, the authors fail to normalize mutation counts by gene or protein length when comparing across ORFs, falsely concluding that short genes (such as the 13-amino-acid nsp11 or 75-aa Envelope) are under stronger purifying selection than the 1,945-aa nsp3 simply because they had zero mutations in 196 genomes. Fourth, the manuscript contains pervasive factual, coordinate, and arithmetic errors (e.g., stating twice that the SARS-CoV-2 genome is `29,903 kb`—nearly 30 megabases—instead of `29,903 bp`, contradicting Table 1 in the Abstract/Text regarding ORF6 mutations, and misassigning nsp1 coding mutations to the untranslated "Leader" region).

---

### 2. Methodological & Statistical Audit

* **Fatal Denominator Bias from Deduplication ("Redundancy Removal") Prior to Frequency Estimation:**
  In Section 2.1, the authors state that out of 579 complete US genomes, *"Using Jal view visualization, redundant sequences were identified which were removed from the analysis... 196 unique SARS-CoV-2 genome sequences remained to use for mutational analysis."* In Section 2.2, weekly "mutation frequency" is computed as the total number of mutations divided by the number of retained unique sequences in that week. Because identical wild-type or dominant-clade genomes are collapsed into a single sequence while every singleton variant (or sequencing error) is retained as a separate sequence, deduplication systematically biases the sample toward rare/erroneous variants and makes the weekly ratio a function of sampling depth rather than true population allele frequency or evolutionary rate.

* **Conflation of Cumulative Root-to-Tip Divergence and Lineage Introductions with Weekly Mutation Rate:**
  In Section 2.2 and Figure 2, the authors observe that the average number of differences from `NC_045512` per sequence was low in weeks 1–5 (January–February, when early US cases were direct introductions of ancestral Wuhan/Clade 19A/19B strains with 1–3 substitutions) and increased sharply in weeks 6–9 (March, when the US epidemic was seeded by European Clade 20A/20C strains carrying the linked haplotype `C241T`, `C1059T` [nsp2 T85I], `C3037T`, `C14408T` [RdRp P323L], `A23403G` [S D614G], `G25563T` [ORF3a Q57H], plus WA1/Clade 19B `C17747T` and `A17858G` [Helicase P504L/Y541C]). Counting cumulative substitutions from the ancestral reference in each week measures root-to-tip molecular clock accumulation (~2 substitutions/month) plus founder-lineage replacement—not an increase in the weekly mutation rate of the virus.

* **Failure to Normalize Mutation Counts by Gene Length (Poisson Expectation Ignored):**
  Throughout Sections 2.3 and 3, the authors compare raw counts of unique amino acid mutations per protein (Table 1, Figure 5) without dividing by protein length (number of codons). Across all 29 proteins in Table 1, there are 151 total unique amino acid mutations over $\sim 9,750$ codons, yielding an average density of $\lambda \approx 0.0155$ unique nonsynonymous mutations per amino acid residue. Under a uniform neutral Poisson process with $\lambda = 0.0155$:
  - **nsp11** (13 aa): expected mutations $= 0.20$, $P(X = 0) = e^{-0.20} = 81.9\%$.
  - **ORF7b** (43 aa): expected $= 0.67$, $P(X = 0) = 51.3\%$.
  - **ORF6** (61 aa): expected $= 0.95$, $P(X = 0) = 38.9\%$.
  - **Envelope (E)** (75 aa): expected $= 1.16$, $P(X = 0) = 31.3\%$.
  - **nsp7** (83 aa): expected $= 1.29$, $P(X = 0) = 27.6\%$.
  - **nsp9** (113 aa): expected $= 1.75$, $P(X = 0) = 17.4\%$.
  - **nsp10** (139 aa): expected $= 2.15$, $P(X = 0) = 11.6\%$.
  - **nsp3** (1,945 aa): expected $= 30.1$, observed $= 31$.
  Thus, observing 31 mutations in nsp3 and 0–1 mutations in tiny accessory/cofactor proteins is almost exactly what is expected by gene size alone, with zero statistical evidence for differential purifying selection or "absence of mutation."

* **Implausible Phylogenetic Log-Likelihood and Undefined Clustering Cutoff:**
  In Section 2.1, the authors report a maximum-likelihood tree of 197 nearly identical 29.9-kb SARS-CoV-2 genomes with a log-likelihood of `−2,497,132.35`. For an alignment of $L = 29,903$ almost invariant sites across 197 taxa, the exact site log-likelihood under Tamura–Nei is approximately $-L \ln(4) \approx -41,454$ (to $-45,000$). A log-likelihood of $-2.50 \times 10^6$ is off by a factor of $\sim 60$, indicating either a severely corrupted alignment (e.g., unaligned frameshifted sequences) or misreporting. Furthermore, clusters A–S are defined by an arbitrary *"minimum branch deviation (cut off 0.0005)"* ($0.0005 \times 29,903 \approx 15$ substitutions, which exceeds the entire tree depth of early SARS-CoV-2).

---

### 3. Biological / Experimental Grounding & Claim Proportionality

* **Direct Contradiction Between Text/Abstract and Table 1 on ORF6 and ORF10:**
  The Abstract, Results (Section 2.3), and Discussion (Section 3) repeatedly state that seven proteins—`NSP7, NSP9, NSP10, NSP11, Envelope, ORF6, and ORF7b`—*"did not accumulate any mutation"* / *"had no mutation frequency over the study period."* However, **Table 1** explicitly lists a mutation in **ORF6**: `V9F (27226G > T) [1]`, while **ORF10** (which has `No mutations` in Table 1) is omitted from the text's list of invariant proteins!

* **Misannotation of nsp1 Coding Mutations as "Leader" Protein and Nonsense Mutation Errors in Table 1:**
  In Table 1, row 1 is labeled `Leader` and lists `G82_V86del (509_523del...)`, `K141_F143del (686_694del...)`, `D75*E (490**T > A)`, `A117T (614G > A)`, `M1L (266A > T)`, and `L21S (327T > C)`. In coronavirus biology, the "leader" sequence is the 5' untranslated RNA leader (nt 1–265); nucleotides 266–805 encode **nsp1** (the host shutoff factor, 180 aa). Moreover, `M1L (266A > T)` mutates the start codon `ATG` of ORF1a/1ab, which is lethal to viral translation and represents a 5'-end sequencing/primer-trimming artifact rather than a viable viral mutation. Similarly, in **Spike** (Section 2.4), the authors claim all 16 mutations in Spike are nonsynonymous and show adaptive evolution, failing to check whether synonymous mutations were excluded by their protein-level lookup tool.

* **Gross Unit and Factual Errors Throughout the Manuscript:**
  1. In both the Introduction (Section 1) and Results (Section 2.2), the authors state that the SARS-CoV-2 genome has *"a size of 29,903 kb"* ($29.9\ \text{Mb}$, the size of a eukaryotic fungal genome, 1,000-fold larger than the actual $29,903\ \text{bp}$ / $29.9\ \text{kb}$ genome).
  2. In the Introduction, the authors cite a preprint claiming that SARS-CoV-2's receptor binding domain (RBD) and furin cleavage site arose via recent *"recombination"* that increased entry efficacy during COVID-19, and conflate the virus (`SARS-CoV-2`) with the disease (`COVID-19 virus`, `COVID19 proteins`).
  3. In the Discussion, the authors speculate that because nsp9 and nsp10 had no mutations and have been proposed to induce IL-6/IL-8, *"local inflammation is essential for SARS-CoV-2 propagation, as it retains these NSPs unaffected during the study period"*—an unfounded teleological leap from a small-sample null count in a 100-codon protein.

---

### 4. Reproducibility & Data Completeness

* **Strengths:** Supplementary Tables S1–S5 are described as listing the 196 NCBI accession numbers, collection dates, cluster assignments, and weekly variant calls.
* **Deficiencies:**
  1. The retrieval query URL given in Section 4.1 (`https://www.ncbi.nlm.nih.gov/nuccore/?term=COVID19`) is a generic keyword search rather than a reproducible taxonomy/completeness query.
  2. Alignment parameters, trimming boundaries (especially at the error-prone 5' and 3' UTRs), and how weekly bins (`W1`–`W11`) were defined across the 87-day window from 19 January to 15 April (which is 12.4 weeks, not 11 weeks!) are undocumented.
