# Blinded Review: SP_ANON_035
**Composite Score:** 8.2 / 10.0 (Rigor: 2.8/3.5 | Claims: 2.1/2.5 | Biology: 1.7/2.0 | Reproducibility: 1.6/2.0)
**Bias Category:** Low Post-Burnin MCMC Sample Counts in Specific Phylogeographic GLM Panels & Geographic Sampling Gaps
**Verdict:** Accept (Minor Revision)
**Study Modality:** Dry-Lab Secondary Cohort/Database Re-Analysis
**Technology Maturity:** Mid-Stage High-Throughput
**Epistemic Stage:** Clinical/Epidemiological Observational

---

### 1. Executive Summary
This global phylodynamic study analyzes 1,282 newly sequenced whole genomes of Respiratory Syncytial Virus (RSV-A and RSV-B) from the prospective INFORM-RSV clinical surveillance study (2017–2020 across 17 countries) combined with 1,180 publicly available GenBank genomes ($N=2,462$ total). Using maximum-likelihood phylogenetic genotyping, Bayesian Skygrid demographic reconstruction, posterior predictive tree-shape neutrality tests (Fu & Li's $D_F$ and trunk proportion), codon-level selection inference (HyPhy FUBAR, MEME, and BEAST Renaissance Counting), normalized Shannon entropy of geographic clustering, and discrete-trait Bayesian Generalized Linear Model (GLM) phylogeography, the authors demonstrate that global RSV-A and RSV-B dispersal is primarily driven by international air passenger volume, that multiple genotypes co-circulate globally with rapid spatial mixing (except for a geographically restricted RSV-A lineage in South Africa), and that positive diversifying selection is heavily concentrated in the attachment glycoprotein G (21 sites in RSV-A, 18 in RSV-B) with minimal episodic selection in the fusion protein F.

---

### 2. Methodological & Statistical Audit
* **Rigorous Integration of Sample-Size Controls in Bayesian GLM Phylogeography:** Discrete-trait phylogeographic GLMs are notoriously vulnerable to uneven sequence sampling across countries. The authors explicitly address this by fitting parallel GLMs with and without origin and destination sequence sample sizes as covariates (Figure 2A–F), demonstrating that air passenger flux remains the single dominant, statistically supported predictor of viral lineage migration between countries even after controlling for sampling intensity.
* **Posterior Predictive Tree-Shape Neutrality Testing:** Rather than inferring selection solely from $dN/dS$, the authors use posterior predictive simulation under a neutral skygrid coalescent process (`TreeStat2`) to compare empirical vs. simulated distributions of Fu & Li's $D_F$ and trunk proportion (Table 2), providing independent genealogical evidence of non-neutral lineage turnover in both RSV-A and RSV-B.
* **Small Post-Burnin MCMC Sample Sizes in Specific GLM Panels (Figure 2 Caption):** In the caption to Figure 2, the authors note that the posterior violin distributions for the GLM coefficients are based on $n=507$ (panel A), $n=535$ (panel B), $n=45,002$ (panel C), $n=45,002$ (panel D), $n=452$ (panel E), and $n=452$ (panel F) post-burnin MCMC states. While subsampling a long, well-mixed BEAST chain to ~450–500 logged states is acceptable *if* the Effective Sample Size (ESS) is $\ge 200$, the stark 100-fold difference in logged states between panels C/D ($45,002$) and panels A/B/E/F ($452\text{–}535$) is unexplained, and exact ESS values for the GLM indicators and coefficients should be reported in the Methods.
* **Geographic Ascertainment Gaps and Genotype Threshold Asymmetry:** Because INFORM-RSV and GenBank lacked contemporaneous whole-genome sequences from major population centers (e.g., India, China, and most of sub-Saharan Africa outside South Africa and Kenya), the GLM estimates a counterintuitive negative coefficient for origin country population size in RSV-B (reflecting low sequence representation from the world's most populous nations). Additionally, applying a uniform patristic distance cutoff splits the dominant ON1-derived RSV-A clade (A23) into 25 sub-genotypes while splitting the analogous BA-derived RSV-B clade (B6) into only 2 genotypes, reflecting slower baseline substitution/diversification in RSV-B rather than a difference in epidemiological lineage structure.

---

### 3. Biological / Experimental Grounding & Claim Proportionality
* **Claim:** *Global spatial dissemination of both RSV-A and RSV-B is strongly predicted by human air travel volume, leading to high geographic intermixing of genotypes across continents.* **[Well Supported]** — Consistently supported by Bayesian GLM inclusion probabilities, positive log-conditional effect sizes across temporal and subsampled sensitivity analyses (Figure 2), and normalized Shannon entropy $>0.80$ in almost all sampled countries (Table 1).
* **Claim:** *Positive selection across the RSV genome is concentrated in the mucin-like hypervariable regions of the G glycoprotein, whereas the vaccine/mAb target F protein is highly conserved with only 1–3 sites showing episodic selection.* **[Well Supported]** — Concordant across FUBAR (pervasive selection), MEME (episodic selection), and Bayesian Renaissance Counting (Figure 3, Table 3).

---

### 4. Reproducibility & Data Completeness
* **Sequence and Metadata Availability:** All 1,282 newly sequenced INFORM-RSV genomes are deposited in GenBank (accessions listed in Supplementary Data), and the full metadata and accession tables for the combined 2,462-genome dataset are provided.
* **Software Documentation:** All tools (IQ-TREE, TempEst, BEAST v1.10, BEAGLE, HyPhy FUBAR/MEME, TreeStat2) and prior specifications are thoroughly documented.
