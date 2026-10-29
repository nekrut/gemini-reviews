</Agent System Instructions>
<Blinded Review: TIME_ANON_0776>
**Composite Score:** 6.5 / 10.0 (Rigor: 1.9/3.5 | Claims: 1.5/2.5 | Biology: 1.4/2.0 | Reproducibility: 1.7/2.0)
**Bias Category:** Algorithmic/Model
**Verdict:** Major Revision
**Study Modality:** Dry-Lab Theory/Methods/Simulation
**Technology Maturity:** Mid-Stage High-Throughput
**Epistemic Stage:** Basic/Mechanistic Discovery

OVERALL_SCORE: 6.5/10
VERDICT: CAVEATS
ESTIMATED_DECADE: 2020s

---

### 1. Executive Summary / SUMMARY
This computational biology manuscript introduces `PHACE`, a phylogeny-aware residue coevolution method that uses maximum-likelihood ancestral state reconstruction (ASR in `IQ-TREE` over `RAxML-NG` trees from the `PHACT` database) to score branch-level co-variation across protein multiple sequence alignments (MSAs). `PHACE` reduces each site to a 3-state amino acid alignment (`MSA1`: dominant amino acid, tolerable vs intolerable alternative sets based on an ancestral reconstruction tolerability score, and gaps) and a 2-state gap alignment (`MSA2`), computes branch-specific total change differences $dif_n(i)$, and combines them via a weighted concordance correlation coefficient (`WCCC`) adjusted by branch evolutionary rate weights $\omega_1(i)$ and non-parallel change weights $\omega_2(i)$. The authors benchmark `PHACE` against `CAPS`, `CoMap`, `DCA`, `GaussDCA`, `PSICOV`, and `MIp` across 652 human proteins with PDB structures ($<8\text{ \AA}$ $\text{C}_\beta\text{–C}_\beta$ contacts). While the phylogenetic decomposition of amino acid vs indel changes and open data/code release are commendable, the benchmark contains major methodological flaws: (1) per-protein ROC threshold optimization on the test structures for MCC evaluation, (2) running Potts models (`DCA`, `GaussDCA`, `PSICOV`) with `min_separation = 1` without stratifying by sequence separation ($|i-j| \ge 6, 12, 24$), which conflates trivial backbone neighbors with tertiary contacts, and (3) omitting modern pseudolikelihood Potts baselines (`plmDCA`, `CCMpred`, `GREMLIN`).

### 2. Methodological & Statistical Audit / STRENGTHS & WEAKNESSES

#### STRENGTHS
- **Explicit Phylogenetic Decomposition of Substitutions and Indels:** Separating amino acid exchanges (`MSA1`) from gap/indel events (`MSA2`) along fixed-branch-length ML trees (`IQ-TREE -blfix`) directly addresses phylogenetic non-independence (shared ancestry vs independent co-substitutions) and alignment gap artifacts that confound naive site-pair correlation metrics.
- **Strong Open Science and Reproducibility:** Source code, benchmark scripts (`GitHub`), and precomputed coevolution matrices for all 652 proteins (`Zenodo`) are publicly deposited with exact software flags documented.

#### WEAKNESSES & METHODOLOGICAL AUDIT
- **Oracle Threshold Selection on Test Proteins in MCC Benchmarking (`Figure 3A`):** In the "Comparison Metrics" section and Figure 3A caption, the authors state: *"we determined the best threshold per protein using ROC curves for MCC comparisons"* (while elsewhere mentioning a fixed `0.25` threshold selected on a subset). Choosing the binary classification threshold per protein by maximizing performance on that same protein's ground-truth PDB contact map is direct test-set data leakage, inflating the reported MCC distributions and invalidating threshold-dependent comparisons.
- **Unstratified Sequence Separation (`min_separation = 1`) Confounds Trivial Backbone Proximity with Coevolution:** Standard Potts models (`DCA`, `GaussDCA`, `PSICOV`) set `min_separation >= 5` or `6` by default because residues at $|i - j| \le 4$ are physically guaranteed to be within $<8\text{ \AA}$ along the polypeptide backbone regardless of coevolution, and strong local sequence correlations distort contact rankings. Here, the authors forced `min_separation = 1` for `GaussDCA` and `PSICOV` (and assigned a penalty score of $\min - 1$ to `N/A` pairs filtered by other tools) and evaluated precision (`Top-L/5`, `Top-L/2`, `Top-L`), ROC-AUC, and PR-AUC across **all** pairs without stratifying into short- ($6 \le |i-j| < 12$), medium- ($12 \le |i-j| < 24$), and long-range ($|i-j| \ge 24$) contacts as required by CASP/coevolution benchmarking standards.
- **Imputation Penalty Applied to Filtered Pairs (`min_score - 1`):** Assigning `min_score - 1` to any residue pair left `N/A` by a competing tool (e.g., `CAPS` or `CoMap`, which only report statistically significant coevolving pairs) artificially depresses the global ROC-AUC and PR-AUC of sparse predictors relative to dense scorers.
- **Omission of Standard Pseudolikelihood Potts Baselines (`CCMpred` / `plmDCA` / `GREMLIN`):** The benchmark compares against early message-passing/mean-field `DCA` (2011), `PSICOV` (2012), and `GaussDCA` (2014), omitting pseudolikelihood maximization with APC correction (`plmDCA`/`CCMpred`/`GREMLIN`), the standard sequence-based contact prediction baseline.
- **Stacked Heuristic Constants Without Ablation Analysis (and Missing Rendered Equations in Text):** The `PHACE` pipeline relies on numerous hard-coded thresholds ($0.5$ weight on $I_i$, $0.5$ tolerability cutoff, $0.9$ dominant AA frequency cutoff, gap masking $K = \max(2, \lfloor 0.05(N-N_g)\rfloor)$, $|dif_1 - dif_2| \ge 0.5 \implies \omega_2 = 1$, and zeroing out single-leaf amino acid changes) without an ablation table showing how each heuristic affects performance; additionally, the display equations in the "PHACE Algorithm" section are missing from the formatted text.

### 3. Biological / Experimental Grounding & Claim Proportionality
- **Claim 1:** *`PHACE` outperforms `DCA`, `GaussDCA`, `PSICOV`, `MIp`, `CAPS`, and `CoMap` in structural contact prediction across 652 human proteins.* `[Overstated]` — Because contacts were evaluated at `min_separation = 1` without sequence-separation stratification ($|i-j| \ge 6, 12, 24$), per-protein ROC thresholds were used in MCC plots, and `N/A` pairs were penalized with `min_score - 1`, superiority on genuine long-range tertiary contacts is not established.
- **Claim 2:** *Phylogeny-aware ASR scoring distinguishes independent co-substitutions on multiple branches from single-clade ancestral divergence.* `[Well Supported]` — Illustrated clearly by the `1A0S_1` (`163–164` vs `128–137`) and `1M9Z_1` phylogenetic tree examples (`Figure 4`).

### 4. Reproducibility & Data Completeness
- **Code & Data Availability:** Excellent availability of source code (`https://github.com/CompGenomeLab/PHACE`) and full 652-protein prediction matrices (`https://zenodo.org/records/14043199`), though the mathematical display formulas in the manuscript text need to be restored so readers do not have to reverse-engineer them from the codebase.
</Blinded Review: TIME_ANON_0776>
