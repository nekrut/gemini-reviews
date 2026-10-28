# Blinded Review: SP_ANON_150
**Composite Score:** 9.0 / 10.0 (Rigor: 3.1/3.5 | Claims: 2.3/2.5 | Biology: 1.9/2.0 | Reproducibility: 1.7/2.0)
**Bias Category:** None (Methodologically Sound)
**Verdict:** Accept (Minor Revision)
**Study Modality:** Dry-Lab Theory/Methods/Simulation
**Technology Maturity:** Mature/Classical
**Epistemic Stage:** Basic/Mechanistic Discovery

---

### 1. Executive Summary
This study investigates the evolutionary origins of the two human herpes simplex viruses, HSV-1 and HSV-2, to determine why humans are the only primate species known to harbor two distinct simplex viruses. Using a 12-glycoprotein concatenated alignment (7,566 nt) and a broader 74-sequence glycoprotein B (`UL27` / gB, 2,283 nt) alignment across primate simplex viruses, the authors show that standard nucleotide substitution models ($\text{GTR}+\Gamma_4$ in BEAST and `r8s`) severely underestimate deep internal branch lengths due to synonymous substitution saturation under strong purifying selection, yielding tMRCA estimates (HSV-1/ChHV ~9.1–10.4 Ma and HSV-2/ChHV ~2.7–3.4 Ma) that reject all ten parsimonious codivergence, duplication, and cross-species transmission scenarios ($P < 0.0001$). By introducing a step-up $\text{AIC}_c$-controlled branch-site random effects likelihood (BSREL) codon model coupled with penalized likelihood relaxed clock dating (`r8s`) and Latin Hypercube Sampling Importance Resampling (LHC-SIR), the authors show that accounting for heterogeneous purifying selection expands deep internal branches by up to 3.15-fold. Under BSREL, the HSV-1/ChHV split dates to 6.2 Ma (95% CI 5.6–7.4 Ma), matching the *Homo–Pan* host divergence ($P = 0.506$), whereas HSV-2 diverged from chimpanzee herpesvirus (ChHV) around 1.6 Ma (95% CI 1.4–2.1 Ma; $P < 0.0001$ against 6 Ma), supporting cross-species transmission from an ancestor of *Pan troglodytes* into an extinct *Homo* lineage.

The manuscript is a compelling demonstration of how purifying selection distorts deep viral molecular clocks and validates its BSREL dating pipeline against independent *Macaca* host divergence nodes. Minor issues are limited to the two-stage decoupling of branch-length estimation and clock smoothing, and two numerical transcription typos in the text and Table 3.

---

### 2. Methodological & Statistical Audit
* **Step-Up cAIC BSREL Regularization for Branch Length Estimation:** Standard 3-class BSREL overparameterizes short branches where few substitutions occur, leading to unstable point estimates of branch lengths. The authors' step-up procedure—adding $dN/dS$ mixture classes to branches ordered by length only when justified by $\text{AIC}_c$—prevents variance inflation on short branches while allowing long internal branches (7 of 9 having $\ge 95\%$ weight in the $\omega = 0$ class) to expand appropriately for synonymous saturation.
* **Positive Control Validation on Independent Host Speciation Nodes:** Rather than judging the model solely by whether it fits the target *Homo–Pan* node, the authors evaluate external test nodes in Table 3: BSREL recovers the *Macaca* MHV-1 crown tMRCA at 2.1 Ma (95% CI 1.8–2.8 Ma vs. published host divergence 2.2–2.5 Ma, where $\text{GTR}+\Gamma_4$ overestimated 3.7 Ma) and the *M. fuscata / M. mulatta* split at 2.0 Ma (95% CI 1.6–2.5 Ma vs. 1.7 Ma host split, where $\text{GTR}+\Gamma_4$ gave 3.3 Ma), and demonstrates leave-one-out calibration robustness across all four subsets of three internal calibrations (HSV-1/ChHV 5.7–6.5 Ma; HSV-2/ChHV 1.5–1.7 Ma).
* **Two-Stage Decoupling of Substitution Model and Penalized Likelihood Clock:** Because codon BSREL cannot be run natively inside BEAST, the authors pass ML branch lengths into `r8s` (where the cross-validated smoothing parameter shifts from $\lambda = 3.2$ under $\text{GTR}+\Gamma_4$ to $\lambda = 100$ under BSREL) and perform 1-d.f. LRTs inside `r8s` (Table 2). While the `r8s` LRT treats point-estimate branch lengths as fixed Poisson counts without propagating BSREL parameter uncertainty into the test statistic itself, the 500-replicate LHC-SIR intervals in Table 3 propagate substitution-model variance and confirm that the 95% intervals for HSV-1/ChHV (5.6–7.4 Ma) and HSV-2/ChHV (1.4–2.1 Ma) are non-overlapping.
* **Sensitivity to an Outlier Terminal Branch:** The authors transparently note an outlier branch-length expansion on a short HVP-2 terminal branch (Figure 5C) and verify that replacing it with the $\text{GTR}+\Gamma_4$ length leaves all tMRCA estimates and LRT conclusions unchanged.

---

### 3. Biological / Experimental Grounding & Claim Proportionality
* **Codivergence of HSV-1 at the *Homo–Pan* Split (~6.2 Ma) and Zoonotic Acquisition of HSV-2 (~1.6 Ma) [Well Supported]:** The combination of topological placement `(HSV-1, (HSV-2, ChHV))` and selection-corrected molecular dating cleanly separates the ten candidate scenarios in Figures 2–3, ruling out ape viral duplication and HSV-1 cross-species transmission while placing the HSV-2/ChHV split between the *Pan troglodytes / Pan paniscus* divergence (~2.2 Ma) and *P. troglodytes* subspecies diversification (~1.0 Ma).
* **Confirmation of CeHV-2 as a Baboon Virus [Well Supported]:** Both models place the CeHV-2/HVP-2 split (~1.9 Ma under BSREL) within the crown radiation of *Papio* (~2 Ma) rather than at the *Chlorocebus–Papio* divergence (11.6 Ma).
* **Testable Prediction for Undiscovered Gorilla and Bonobo Simplex Viruses [Well Supported]:** The authors articulate falsifiable phylogenetic predictions for future primate viral surveillance (Figure 3E).

---

### 4. Reproducibility & Data Completeness
* **Data & Input Availability:** Alignments, BEAST XML files, and `r8s` configuration files are all provided in the Supplementary Material.
* **Numerical Typos to Correct:**
  1. In the Results text (paragraph 8), the inferred substitution rate is written as *"1 × 10 − 8 (8.1 × 10 − 7 –1.2 × 10 − 8 ) substitutions per site per year."* The lower bound `8.1 × 10 − 7` is a typo for `8.1 × 10 − 9` (since $8.1 \times 10^{-7}$ is 81-fold higher than the point estimate $1 \times 10^{-8}$).
  2. In Table 3, row 2 (`HSV-2/ChHV` under `GTR + Γ 4`), the tMRCA and confidence interval are printed as `2.7 (2.9–2.9)`, where the point estimate lies outside the degenerate interval (likely a typo for `2.7 (2.5–2.9)`).
