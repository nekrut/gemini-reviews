# Review of PMC7196762 (PMID:32269081)

**Manuscript Title:** Phylogenetic network analysis of SARS-CoV-2 genomes  
**Authors:** Forster P, Forster L, Renfrew C, Forster M.  
**Journal / Preprint:** *Proc Natl Acad Sci U S A* (2020; `PMC7196762` / `PMID:32269081` / `10.1073/pnas.2004999117`)  
**Calibration Study Cohort:** Cohort A — Known Invalid / Refuted (`A03` | Double-Blinded as `ANON_45`)  
**Overall Score:** **2.4 / 10.0** (Fundamentally Invalid)  
* **Score Breakdown:** Rigor: 0.6/3.5 | Claims: 0.4/2.5 | Biology: 0.5/2.0 | Reproducibility: 0.9/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript applies a character-based median-joining and Steiner parsimony network algorithm (implemented in the shareware package Network 5011CS) to 160 complete human SARS-CoV-2 genomes sampled up to March 4, 2020 from GISAID, using the bat coronavirus isolate BatCoVRaTG13 (96.2% nucleotide identity) as an outgroup root. The authors partition the 100 distinct human viral haplotypes into three clusters designated A, B, and C, infer that cluster A represents the ancestral human SARS-CoV-2 genome based on outgroup attachment to RaTG13, observe geographic differences in cluster frequencies across East Asia, Europe, and the Americas, and conclude that ancestral type B required further mutations to spread outside East Asia due to founder effects or "immunological or environmental resistance against this type outside Asia." They further claim that the network reconstructs person-to-person infection routes and can be used to trace and quarantine undocumented COVID-19 infection sources.

The study's core evolutionary and epidemiological conclusions are invalidated by three fundamental methodological flaws: (1) rooting an intraspecific parsimony network of 160 nearly identical human viral genomes (spanning 229 total mutations) with a distantly diverged bat virus (~1,150 nucleotide differences) without a probabilistic substitution model or molecular clock is dominated by long-branch homoplasy and contradicts the temporal sampling record; (2) attributing geographic cluster frequencies in 160 early convenience-sampled genomes to host "immunological or environmental resistance" ignores extreme travel and sequencing ascertainment bias; and (3) inferring direct transmission directionality and positive selection from unweighted parsimony networks and recurrent sequencing artifacts (such as np11083) overreaches the resolution of the data. Re-analyzing the alignment with time-calibrated maximum-likelihood or Bayesian phylogenetics and removing unsupported claims of host resistance and source contact tracing are required.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Cluster A is the ancestral human SARS-CoV-2 type based on outgroup rooting with BatCoVRaTG13: [Methodologically Flawed].**  
  Median-joining networks are unweighted parsimony heuristics designed for closely related intraspecific haplotypes free of saturation and long-branch attraction. BatCoVRaTG13 differs from human SARS-CoV-2 by 3.8% (~1,150 nucleotide substitutions across the 29,742 nt alignment window), whereas the 160 human genomes differ from one another by only a few substitutions (total parsimony length 229 across the entire human network). Because human types A and B are separated by only two nucleotide substitutions (positions 8782 and 28144, one of which is a C/T transition prone to rampant coronavirus hypermutation), matching the state of RaTG13 at those two sites over an unmodeled ~1,150-mutation branch has high probability of random homoplasy. Moreover, this outgroup rooting ignores collection dates: the earliest December 2019 genomes from Wuhan (including the reference Wuhan-Hu-1) belong to cluster B, whereas cluster A genomes were sampled later.

* **Ancestral type B did not spread outside East Asia without first mutating due to founder effects or immunological or environmental resistance outside Asia: [Overstated].**  
  The dataset comprises just 160 human genomes unevenly sampled from early travel-linked cases and regional clusters prior to March 4, 2020. No statistical test of geographic structure, migration rate, or selection is performed. Proposing "immunological or environmental resistance against this type outside Asia" to explain why a specific early haplotype in a tiny, convenience-sampled dataset was predominantly sequenced in China conflates early epidemic seeding and testing ascertainment with host biological resistance.

* **Human SARS-CoV-2 genomes are under evolutionary selection with parallel adaptive mutations, making character-based median-joining networks the method of choice: [Methodologically Flawed].**  
  The Abstract asserts that the 160 genomes are "under evolutionary selection in their human hosts, sometimes with parallel evolution events... making character-based phylogenetic networks the method of choice." No test of natural selection (e.g., $dN/dS$ or site-level selection modeling) is conducted anywhere in the manuscript. Worse, the Figure 1 caption notes that network reticulations "are mainly caused by recurrent mutations at np11083"—a well-documented homoplasic site adjacent to a poly-U tract prone to Nanopore/Illumina sequencing and assembly errors rather than adaptive convergent evolution.

* **The median-joining network faithfully traces infection routes and can identify undocumented COVID-19 sources for quarantine: [Overstated].**  
  SARS-CoV-2 accumulates roughly one substitution every two weeks (~24–25 substitutions/year), whereas its epidemiological serial interval is 4–5 days. Consequently, identical viral haplotypes are shared by dozens or hundreds of epidemiologically unlinked individuals, and an uncalibrated parsimony network cannot resolve who infected whom or identify undocumented index cases for quarantine in the absence of contact-tracing metadata.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Replace Outgroup Parsimony Rooting with Time-Calibrated Likelihood or Bayesian Phylogenetic Inference
* **WHY:** Attaching a ~1,150-mutation outgroup (BatCoVRaTG13) to an unweighted median-joining network ignores transition/transversion rate asymmetry, C$\to$U hypermutation, site-rate heterogeneity, and tip sampling dates, yielding an unreliable root placement.
* **WHAT:** Infer the root position and posterior rooting probabilities using a probabilistic nucleotide substitution model that incorporates tip collection dates.
* **HOW:** Fit a time-calibrated phylogeny to the 160 human SARS-CoV-2 genomes using IQ-TREE + TreeTime or BEAST under a GTR+$\Gamma$ (or HKY+$\Gamma$) substitution model with tip dates from GISAID metadata. Compare the log-likelihood and root posterior probabilities of a clade B root vs. a clade A root, and report the statistical uncertainty around the root state rather than fixing it via unweighted parsimony distance to RaTG13.

#### 2. Mask Known Homoplasic/Artifactual Sites (Including np11083) and Test Formally for Selection
* **WHY:** Treating recurrent mutations at error-prone sites like np11083 and unweighted multi-nucleotide indels (up to 24 nt coded as single steps) as genuine evolutionary reticulations distorts the network topology and falsely implies adaptive parallel evolution.
* **WHAT:** Repeat the network and tree reconstructions after masking known problematic/homoplasic positions, and remove unsubstantiated claims of positive selection unless supported by formal codon-model tests.
* **HOW:** Mask position 11083 and terminal UTR regions, re-estimate the phylogeny/network, and count how many reticulations remain; if claiming adaptive evolution, run a codon-level selection test (e.g., FEL or MEME in HyPhy) on the coding regions of the 160 genomes and report the resulting $p$-values.

#### 3. Quantify Sampling Bias and Remove Speculation About Immunological or Environmental Resistance
* **WHY:** With only 160 genomes collected across 82 laboratories under heterogeneous travel-screening criteria, regional frequency differences between clusters A, B, and C reflect founder events and testing ascertainment rather than host immunological or environmental barriers.
* **WHAT:** Tabulate the sample counts by country and travel history, and delete the claim of "immunological or environmental resistance against this type outside Asia."
* **HOW:** Add a breakdown table showing how many of the 160 sequences in clusters A, B, and C were sampled from returned travelers vs. community transmission in each region, and revise the Abstract to attribute geographic differences solely to early stochastic founder effects and sampling skew.

#### 4. Reframe Claims Regarding Direct Transmission Tracing
* **WHY:** Because SARS-CoV-2 mutates more slowly than it transmits from person to person, genomic identity or single-mutation proximity in a global database of 160 sequences cannot establish direct person-to-person transmission or pinpoint specific undocumented individuals for quarantine.
* **WHAT:** Temper the Abstract and main text claims regarding transmission route reconstruction.
* **HOW:** Revise the final sentence of the Abstract to state that genomic epidemiology can identify broad regional introductions and travel-linked clusters when combined with contact-tracing records, rather than claiming the network alone can identify undocumented infection sources for quarantine.
