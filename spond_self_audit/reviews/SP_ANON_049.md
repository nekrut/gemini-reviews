# Blinded Review: SP_ANON_049
**Composite Score:** 8.8 / 10.0 (Rigor: 2.8/3.5 | Claims: 2.2/2.5 | Biology: 1.8/2.0 | Reproducibility: 2.0/2.0)
**Bias Category:** None (Methodologically Sound)
**Verdict:** Accept
**Study Modality:** Dry-Lab Theory/Methods/Simulation
**Technology Maturity:** Mature/Classical
**Epistemic Stage:** Basic/Mechanistic Discovery

---

### 1. Executive Summary
This application note describes Datamonkey 2.0 (`datamonkey-js`) and its companion visualization suite HyPhy Vision (`hyphy-vision`), representing a complete architectural rewrite of the Datamonkey web server for molecular evolutionary and natural selection analysis. Built entirely in JavaScript (`Node.js`, `React`, `D3.js`, `Bootstrap`, `Webpack`), the platform decouples the user-facing model-view-controller web application from a dedicated High-Performance Computing (HPC) Job Provisioner that interfaces with cluster schedulers (such as Torque) via a lightweight Redis and WebSockets publish-subscribe protocol. All analyses emit self-contained monolithic JSON result files that can be rendered interactively in the browser via HyPhy Vision—either hosted on Datamonkey 2.0 or run standalone on local HyPhy output at `vision.hyphy.org`. The initial release provides curated, recombination- and synonymous-rate-variation-aware workflows for eight core methods: SLAC, FEL, FUBAR, MEME, aBSREL, RELAX, BUSTED, and GARD.

The software architecture is clean, modular, and well-suited to asynchronous long-running scientific computing tasks, and both the server infrastructure and standalone visualization engine are fully open-source on GitHub. As a short web-server announcement paper, its only notable limitation is the absence of quantitative performance, latency, or scalability benchmark tables comparing the new architecture against the legacy server or quantifying dataset size limits across the eight supported methods.

---

### 2. Methodological & Statistical Audit
* **Decoupled Publish-Subscribe HPC Architecture:** Separating the web front-end from the HPC Job Provisioner and communicating job state transitions via Redis/WebSockets publish-subscribe notifications (Fig. 1) avoids the server load and latency of client HTTP polling while allowing multiple backend compute clusters to be attached transparently.
* **Monolithic JSON Provenance & Standalone Visualization:** Standardizing all HyPhy statistical outputs into a single self-contained JSON document (storing input metadata, fitted branch lengths, substitution rate distributions, likelihood ratio test statistics, $p$-values, and site-level Bayes factors/posteriors) directly improves computational reproducibility, as a single archival file preserves the complete statistical record of an analysis and can be re-inspected client-side in `hyphy-vision` without re-running the cluster job.
* **Absence of Quantitative Scaling / Operational Metrics:** While the text notes qualitatively that the queue handles "tens to hundreds jobs with average wait times of only a few minutes" and states alignment size guidelines for some methods (e.g., $>1,000$ sequences for SLAC/FUBAR, $<30$ sequences where FEL may outperform MEME), providing a summary table of maximum supported alignment dimensions (taxa $\times$ codons), median runtime scaling, and client browser memory limits for rendering large trees in `hyphy-vision` would make the operational specifications more concrete.

---

### 3. Biological / Experimental Grounding & Claim Proportionality
* **Curated Statistical Decision Guidance:** The summary of the eight available methods (lines 75–91) accurately distinguishes pervasive vs. episodic selection, site-level (SLAC, FEL, FUBAR, MEME) vs. branch-level (aBSREL, RELAX) vs. gene-wide (BUSTED) hypothesis tests, and emphasizes two critical biological confounders in coding-sequence evolution: phylogenetic incongruence from recombination (partitioned via GARD) and site-to-site synonymous substitution rate variation.
* **Claim Proportionality:** All architectural and usability claims are straightforward and proportional to the software contribution.

---

### 4. Reproducibility & Data Completeness
* **Open-Source Availability:** The full web application (`[GITHUB_REPO_REDACTED]`) and standalone visualization engine (`[GITHUB_REPO_REDACTED]`) are publicly available under open-source licenses alongside the live public web services (`http://www.datamonkey.org` and `http://vision.hyphy.org`).
