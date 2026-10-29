<Blinded Review: TIME_ANON_0703>
OVERALL_SCORE: 8.3/10
VERDICT: PASS
ESTIMATED_DECADE: 2020s
**Composite Score:** 8.3 / 10.0 (Rigor: 2.9/3.5 | Claims: 2.2/2.5 | Biology: 1.8/2.0 | Reproducibility: 1.4/2.0)
**Bias Category:** None (Methodologically Sound)
**Verdict:** Minor Revision
**Study Modality:** Dry-Lab Theory/Methods/Simulation
**Technology Maturity:** Mid-Stage High-Throughput
**Epistemic Stage:** Basic/Mechanistic Discovery

---

### SUMMARY
### 1. Executive Summary
This molecular evolution and comparative genomics study investigates when the gene duplication producing the eukaryotic general recombinase `Rad51` and the meiosis-specific recombinase `DMC1` from an ancestral archaeal `RadA` occurred during eukaryogenesis. Leveraging the curated `EukProt v3` Comparative Set (196 eukaryotic species spanning proposed roots including Discoba and Metamonada) and 156 archaeal genomes/MAGs (70 Euryarchaeota, 30 DPANN, 32 Asgard archaea, and 24 TACK), the authors use profile HMM searches (`HMMER` / `AMOEBAE`), alignment trimming (`MAFFT` + `BMGE` / `trimAl`), and maximum-likelihood phylogenetics (`IQ-TREE2` with site-heterogeneous empirical profile mixture models `LG+C20+G+F` and `LG+C60+G+F`, evaluated with both 1,000 ultrafast bootstraps and 100 standard non-parametric bootstraps). They identify an independent `RadA` duplication within Asgard archaea (specifically well-supported in Heimdallarchaea and Gerdarchaea) and demonstrate across three taxon-sampling/outgroup designs that eukaryotic `Rad51` and `DMC1` consistently form a monophyletic eukaryotic clade excluding all sampled Asgard archaeal `RadA` paralogs. They conclude that the `Rad51`/`DMC1` duplication occurred along the eukaryotic stem lineage after divergence from known Asgard archaea and prior to LECA.

### STRENGTHS
- **Appropriate Use of Site-Heterogeneous Profile Mixture Models (`LG+C20+G+F`, `LG+C60+G+F`):** Deep archaeal-eukaryotic phylogenetics is notoriously susceptible to long-branch attraction (LBA) and compositional heterogeneity; using `C20`/`C60` empirical profile mixture models in `IQ-TREE2` alongside both non-parametric (NP) and ultrafast (UFBoot) bootstrapping and explicit pruning of `RadB` paralogs and rogue long-branch sequences reflects strong phylogenetic practice.
- **Sensitivity Testing Across Outgroup Subsampling Schemes:** Testing the monophyly of `[Rad51 + DMC1]` against (i) all archaea (`Fig. S3`), (ii) Asgard archaea only (`Fig. 2`), and (iii) only the closest sister clade of Asgard archaeal `RadA` (`Fig. 3b / Fig. S4`) confirms that the eukaryotic stem duplication topology is not an artifact of distant outgroup rooting.
- **Exemplary Claim Calibration and Caveat Transparency:** The Discussion explicitly lays out the three key epistemic limitations of the study: (1) potential future discovery of an unsampled Asgard lineage closer to eukaryotes than known Heimdallarchaeota, (2) the possibility that meiotic functionality partially evolved in a pre-duplicated `RadA` ancestor, and (3) that `Rad51`/`DMC1` is a single component of a multi-protein meiotic apparatus.

### WEAKNESSES & METHODOLOGICAL AUDIT
### 2. Methodological & Statistical Audit
- **Lack of Formal Topology Hypothesis Testing (e.g., AU Test):** While standard non-parametric bootstrap (>50%) and UFBoot (>80%) supports are shown on the ML trees, explicitly reporting an Approximately Unbiased (AU) topology test comparing the unconstrained ML tree (eukaryotic-specific `Rad51`/`DMC1` duplication) against a constrained tree forcing eukaryotic `Rad51` and `DMC1` tosegregate with the two Asgard archaeal `RadA` paralog clades (`Fig. 1`) would directly quantify the log-likelihood rejection of a pre-eukaryotic duplication.
- **Alignment Trimming Consistency (`BMGE` vs. `trimAl -gappyout`):** The eukaryotic-only tree (`Fig. S1`) was trimmed with `BMGE` (default entropy settings) and fit with `Q.insect+R7` (an insect nuclear matrix selected by unconstrained `ModelFinder`), whereas the archaeal and combined trees were trimmed with `trimAl -gappyout` and fit with `LG+C20/C60+G+F`. Using `Q.insect` on pan-eukaryotic recombinases is benign because `ModelFinder` simply picks the best-fitting empirical matrix, but restricting `ModelFinder` to general matrices (`LG`, `WAG`, `JTT`) or `C20/C60` across all analyses would be more uniform.

### 3. Biological / Experimental Grounding & Claim Proportionality
- **Claim 1 (Both `Rad51` and `DMC1` were present in LECA, including newly sampled deep metamonads such as *Barthelona* sp. PAP020, whereas *Anaeramoeba ignava* retains `Rad51` but lacks detectable `DMC1`): `[Well Supported]`** — Directly demonstrated by the pan-eukaryotic `EukProt v3` survey and phylogeny.
- **Claim 2 (Certain Asgard archaea, notably Heimdallarchaea and Gerdarchaea, harbor an independent lineage-specific duplication of `RadA`): `[Well Supported]`** — Strongly supported in `Fig. 1` (NP/UFBoot 70/95 and 98/100).
- **Claim 3 (The duplication producing eukaryotic `Rad51` and `DMC1` occurred after the divergence of the eukaryotic stem lineage from currently sampled Asgard archaea): `[Well Supported]`** — Robustly supported across all three combined phylogenetic analyses (`Figs. 2–3`, `Figs. S3–S4`) and framed with appropriate caveats.

### 4. Reproducibility & Data Completeness
- **Data and Pipeline Transparency:** Public data sources (`EukProt v3`, `UniProt`, `GenBank`, `JGI`), seed accessions (`CAG38796`, `CAG30372.1`), `AMOEBAE` GitHub repository, software versions (`MAFFT v7.520`, `trimAl v1.2rev59`, `IQ-TREE2 v2.3.6`), alignment lengths (`313`, `286`, `307`, `306`, `329` aa), and substitution models are fully specified; depositing the untrimmed/trimmed FASTA alignments and Newick tree files in Zenodo/Figshare would further streamline reuse.
</Blinded Review: TIME_ANON_0703>
