# Blinded Review: SP_ANON_126

**Composite Score:** 7.6 / 10.0 (Rigor: 2.6/3.5 | Claims: 2.1/2.5 | Biology: 1.3/2.0 | Reproducibility: 1.6/2.0)
**Bias Category:** None (Methodologically Sound)
**Verdict:** Accept
**Study Modality:** Dry-Lab Theory/Methods/Simulation
**Technology Maturity:** Mature/Classical
**Epistemic Stage:** Basic/Mechanistic Discovery

---

## 1. Executive Summary

This brief Web Server issue application note summarizes five years of updates to the `Datamonkey` comparative evolutionary sequence analysis suite (`www.datamonkey.org`), detailing its hardware expansion to a 356-core cluster (`octamonkey`) and the integration of 12 statistical phylogenetic modules implemented in HyPhy (`PARRIS`, `iFEL`, `GA-branch`, `DEPS`, `TOGGLE`, `GARD`, `SCUEAL`, `CMS`, `EVOBLAST`, `ASR`, and `Spidermonkey`). The note provides a clear, accurate overview of the statistical models available on the server and their practical workflow integration (including automatic recombination screening via `GARD` prior to selection inference), fulfilling the scope of a two-page bioinformatics application note.

---

## 2. Methodological & Statistical Audit

* **Integration of Recombination-Aware Partitioning (`GARD`) into Selection Workflows:** A major methodological strength of the `Datamonkey` architecture compared to competing web servers of its era (`Selecton`, `PAML` portals) is its explicit handling of intragenic recombination. Allowing users to run `GARD` to infer recombination breakpoints and automatically pass partition-specific trees into site-level (`SLAC`, `FEL`, `iFEL`, `REL`, `PARRIS`, `DEPS`) and branch-level (`GA-branch`) codon models prevents the severe false-positive inflation caused by fitting a single phylogeny across recombinant alignments.
* **Absence of Internal Benchmarks or Runtime Profiling:** Because this is a concise 2-page software update summary, it contains no new simulation benchmarks, accuracy comparisons, or quantitative wall-clock scaling tables within the manuscript itself, relying entirely on citations to the primary methodological publications (Refs. 1–16) for statistical validation of each module.
* **Alignment Size Caps:** The note transparently specifies the computational limits imposed by the shared web queue (e.g., $\le 150$ sequences for `SLAC`, $\le 100$ for `FEL`/`iFEL`/`DEPS`, $\le 50$ for `REL`/`TOGGLE`, and $\le 25$ for `GA-branch`), alongside the option to download machine-readable HyPhy batch files for unconstrained local execution.

---

## 3. Biological / Experimental Grounding & Claim Proportionality

* **`[Well Supported]` Comprehensive Coverage of Site-, Branch-, and Property-Level Evolutionary Models:** The descriptions of the 12 newly added methods accurately reflect their mathematical formulations and biological domains of application (e.g., `iFEL` restricting selection inference to internal branches to avoid transient intra-host deleterious polymorphisms; `SCUEAL` performing reference-calibrated viral subtyping and recombinant breakpoint mapping; `Spidermonkey` inferring epistatic residue co-evolution via Bayesian graphical models).
* **`[Well Supported]` Usage and Throughput Claims:** The reported usage metrics (~120 jobs/day, >40,000 user datasets analyzed over 5 years) are factual operational summaries proportional to the paper's claims.

---

## 4. Reproducibility & Data Completeness

* **Software & Source Code Availability:** The web server is freely accessible without login requirements (`www.datamonkey.org`), all underlying model scripts are open-source components of the cross-platform `HyPhy` distribution (`www.hyphy.org`), and users can export complete self-contained job packages and visualization files (PostScript, SVG, CSV, Newick) for local replication.
