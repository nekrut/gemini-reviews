# Blinded Review: SP_ANON_023
**Composite Score:** 7.2 / 10.0 (Rigor: 2.5/3.5 | Claims: 1.7/2.5 | Biology: 1.6/2.0 | Reproducibility: 1.4/2.0)
**Bias Category:** Host-Codivergence Calibration Circularity in Molecular Clock Priors
**Verdict:** Minor Revision
**Study Modality:** Hybrid Computational + Wet-Lab Functional Validation
**Technology Maturity:** Mature/Classical
**Epistemic Stage:** Basic/Mechanistic Discovery

---

### 1. Executive Summary
This study combines wet-lab PCR amplification, cloning, and Sanger sequencing of 65 new avian haemosporidian mitochondrial genomes (~6 kb each) with 49 published genomes ($N=114$ total across four genera: *Leucocytozoon*, *Haemoproteus*, *Plasmodium*, and *Hepatocystis*) to reconstruct the deep phylogeny, divergence times, and selective regimes of malaria parasites and related haemosporidians. Using Bayesian (BEAST, MCMCTree) and maximum-likelihood (RelTime) relaxed clocks alongside an extended multi-clade HyPhy RELAX framework (incorporating site-to-site synonymous rate variation across *cytb*, *cox1*, and *cox3*), the authors establish widespread generic paraphyly, estimate that major avian haemosporidian clades radiated following the Cretaceous–Paleogene (K–Pg) boundary (~68.8 Ma), and demonstrate intensified purifying selection in avian/squamatan *Plasmodium* relative to mammalian *Plasmodium* and other genera.

---

### 2. Methodological & Statistical Audit
* **Circularity Between Host-Fossil Calibrations and Macroevolutionary Conclusions:** Because haemosporidian parasites lack a direct fossil record (apart from a single Miocene Dominican amber *Plasmodium dominicana* fossil at 15–20 Ma), the authors calibrate internal nodes using vertebrate host divergence times (e.g., Bovinae split 16–28.1 Ma, *Papio/Macaca* split 6–14.2 Ma, Lemuriformes biogeographic isolation 41.3–65 Ma, and in Scenarios 2/3, the Palaeognathae–Neognathae bird split at 56.8–86.8 Ma at the root). However, the phylogenetic topology itself proves rampant host-switching across avian and mammalian orders. Constraining parasite nodes with host divergence priors and subsequently concluding that avian haemosporidians radiated synchronously with post-K–Pg modern bird diversification introduces circularity: Scenario 1 (unconstrained root) yields a wider root Credible Interval (54.7–98.5 Ma) that overlaps pre-K–Pg origins, whereas Scenarios 2 and 3 force the root into the K–Pg window by prior specification.
* **Clock Model Discordance:** In MCMCTree analyses (Table S5, Figure S3), the independent-rates and autocorrelated-rates relaxed clock models yield only moderate correlation ($R^2 \approx 0.74$) and differ by up to ~40% in absolute node ages, highlighting substantial sensitivity to rate-prior assumptions across clades with different metabolic and transmission rates.
* **Rigorous Extension of Codon Selection Models:** The methodological extension of HyPhy RELAX to simultaneously fit group-specific selection intensity parameters ($k$) across multiple predefined parasite clades while modeling site-level synonymous rate variation ($\alpha_s$) is statistically sound and avoids false-positive selection signals driven by mutational/synonymous rate heterogeneity in AT-rich (~70% AT) mitochondrial genomes. The combined use of BUSTED, MEME, and multi-clade RELAX across all three protein-coding genes (*cytb*, *cox1*, *cox3*) provides a consistent picture of pervasive purifying selection ($\omega \approx 0.02\text{–}0.05$).

---

### 3. Biological / Experimental Grounding & Claim Proportionality
* **Claim:** *Traditional morphospecies genera (Leucocytozoon, Haemoproteus, Plasmodium) are paraphyletic, with Leucocytozoon (Akiba) caulleryi nesting inside Parahaemoproteus.* **[Well Supported]** — The 6-kb complete mtDNA phylogeny (Figure 1) resolves deep nodes with 1.0 Bayesian posterior probability and high ML bootstrap support, definitively refuting classical taxonomy based on gametocyte morphology and merogony site.
* **Claim:** *Avian/squamatan Plasmodium experiences significantly intensified purifying selection ($k = 4.67$ in cox1, $p < 0.0001$) compared to mammalian Plasmodium, driven by adaptation to diverse Culicidae mosquito vectors vs. Anopheles.* **[Moderately Supported / Speculative Mechanism]** — While the statistical shift in selection intensity $k$ on *cox1* and *cytb* is robustly estimated by multi-clade RELAX (Table 2), attributing this shift specifically to dipteran vector family breadth (Culicidae vs. Ceratopogonidae/Simuliidae/Anopheles) rather than vertebrate host body temperature (endothermic birds at 40–42°C vs. mammals at 37°C), metabolic rate, or effective population size ($N_e$) is an untested ecological hypothesis.
* **Claim:** *Modern avian haemosporidians originated and radiated after the K–Pg mass extinction alongside modern bird orders.* **[Fragile]** — Heavily contingent on secondary host-codivergence calibration priors in a system characterized by frequent host switching.

---

### 4. Reproducibility & Data Completeness
* **Data Availability:** All 65 newly sequenced mitochondrial genomes are deposited in GenBank under accessions `KY653752–KY653816`, with full host species, geographic origins, and voucher metadata listed in Table S1.
* **Missing Alignment and Script Archives:** The manuscript states that sequence alignments and tree files are "available from the authors upon request" rather than depositing the exact curated 6-kb alignment, BEAST/MCMCTree control files, and custom multi-clade RELAX HyPhy batch script in Dryad, Zenodo, or GitHub.
