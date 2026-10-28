# Review of OOD_ANON_19

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **7.8 / 10.0** (Strong / Sound)  
* **Score Breakdown:** Rigor: 2.8/3.5 | Claims: 2.0/2.5 | Biology: 1.6/2.0 | Reproducibility: 1.4/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This computational biophysics study benchmarks three perturbation schemes within Multisite $\lambda$-Dynamics (implemented in CHARMM v49a1 with the BLaDE GPU engine and Adaptive Landscape Flattening [ALF]) for calculating relative protein–DNA binding free energy changes ($\Delta\Delta G_b$) of the WRKY1-N transcription factor domain (PDB: `6J4E`, extended to a 34-bp DNA duplex) upon mutating its cognate W-box motif (`GGTCAA`) to nonspecific sequences (`GATAAA`, `GGTCCG`, and `GGACAA`). The authors compare (1) scaling each base-pair mutation with a single coupling parameter (`1λ`), (2) scaling each individual base with its own parameter (`2λ`), and (3) coupling the two base $\lambda$ variables with a quadratic intersite bias (`coupled 2λ`). Across five replicate 100 ns production trajectories (following iterative ALF flattening), they demonstrate that the `1λ` per base-pair scheme achieves the fastest bias convergence, highest transition rates ($\sim 0.5\text{--}1.0\text{ ns}^{-1}$), and lowest statistical uncertainty ($\pm 0.2\text{ kcal/mol}$), converging to $\Delta\Delta G_b = 5.6 \pm 0.2\text{ kcal/mol}$ for `GGTCAA` $\to$ `GATAAA` in $\sim 460\text{ ns}$ total sampling ($\sim 115\text{ ns}$ per sequence). Applying `1λ` to `GGACAA` and `GGTCCG` correctly ranks the experimental binding affinities, and the authors critically investigate why computed $\Delta\Delta G_b$ values overestimate experimental values by testing a rotated nonspecific binding conformation taken from a $10\ \mu\text{s}$ MD trajectory ($\Delta\Delta G_b = 0.4 \pm 0.2\text{ kcal/mol}$). Example CHARMM/BLaDE scripts are publicly provided on GitHub.

This is a technically sound, well-executed, and transparently reported methodological study. The thermodynamic cycle, implicit $\lambda$ constraints, hybrid nucleobase topology with zero net charge change, and multi-trajectory convergence diagnostics are rigorously designed, and the authors provide a remarkably candid biophysical analysis of why 100 ns alchemical simulations overestimate $\Delta\Delta G_b$ when mutated DNA sequences remain trapped in the "recognition" binding mode rather than relaxing into the microsecond-timescale rotated "search" mode. The primary technical deficiencies are formatting omissions in the manuscript text—Equations 1–5 and Tables 2 and 3 are missing their rendered mathematical expressions/numerical entries in the main document—and the small validation set size (three target mutants in a single transcription factor system), which makes the high-throughput screening claim preliminary.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **The single-$\lambda$ per base-pair (`1λ`) perturbation scheme outperforms uncoupled `2λ` and `coupled 2λ` in convergence speed, transition frequency, and statistical precision: [Well Supported].**  
  By tracking end-state transition rates ($\lambda_c > 0.99$) and $\Delta G$ stability across four sequential production stages (5, 20, 20, and 100 ns $\times$ 5 independent trajectories; Figures 2, 3, and Table 1), the authors demonstrate that `1λ` avoids high-energy Watson–Crick mismatch intermediates, maintains steady transition rates ($\sim 0.5\text{ ns}^{-1}$ bound, $1.0\text{ ns}^{-1}$ unbound), and reaches convergence within $460\text{ ns}$ total simulation time ($\Delta\Delta G_b = 5.6 \pm 0.2\text{ kcal/mol}$), whereas `2λ` requires $1,210\text{ ns}$ ($\Delta\Delta G_b = 6.1 \pm 0.4\text{ kcal/mol}$) and `coupled 2λ` suffers from state dilution across noncanonical mismatched intermediates ($\Delta\Delta G_b = 5.5 \pm 0.8\text{ kcal/mol}$).

* **Multisite $\lambda$-Dynamics (`1λ`) accurately ranks the relative binding free energies ($\Delta\Delta G_b$) of WRKY W-box mutants (`GATAAA`, `GGTCCG`, `GGACAA`) and intermediate single-base mutants: [Moderately Supported].**  
  While the text (lines 178–202) describes the relative ranking of `GATAAA`, `GGTCCG`, and `GGACAA` (as well as single-site intermediates `GATCAA`, `GGTAAA`, `GGTCAG`, and `GGTCCA`) and notes agreement with experimental affinity ordering and prior $4\ \mu\text{s}$/sequence steered MD simulations, the actual numerical cells of **Table 2** and **Table 3** (and the mathematical formulas in **Equations 1–5**) are missing from the formatted manuscript text. Furthermore, rank-ordering 3 mutants (6 permutations, $1/6 = 16.7\%$ chance probability) is a small benchmark for establishing general predictive power.

* **Systematic overestimation of computed $\Delta\Delta G_b$ relative to experiment is driven by slow microsecond conformational relaxation from the specific "recognition" mode to the nonspecific "search" mode: [Well Supported].**  
  Rather than ignoring the systematic overestimation of $\Delta\Delta G_b$ in the 100 ns unrotated simulations, the authors perform a decisive control simulation starting from the rotated nonspecific WRKY–DNA structure observed after $10\ \mu\text{s}$ of equilibrium MD, showing that $\Delta\Delta G_b$ drops from $5.6 \pm 0.2\text{ kcal/mol}$ to $0.4 \pm 0.2\text{ kcal/mol}$. This directly demonstrates that the native sequence stabilizes the specific hydrogen-bonded recognition pose while nonspecific mutants favor the rotated state, and that standard 100 ns alchemical perturbations compute the vertical free energy difference within the unrelaxed recognition basin.

* **Scalability of the `1λ` Multisite $\lambda$-Dynamics protocol for high-throughput screening of TF–DNA binding sites: [Moderately Supported].**  
  The authors appropriately qualify their abstract claim in the Discussion (lines 204–208), noting that histogram-based state binning scales exponentially with the number of mutated base pairs ($N_s^M$) unless paired with a Potts-model estimator and that slow protein conformational rearrangements between specific and nonspecific binding modes remain a sampling bottleneck.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Restore the Missing Numerical Contents of Tables 2 and 3 and Equations 1–5
* **WHY:** In the current manuscript file, Equations 1–5 (lines 37, 53, 65, 73, 94) are blank table boxes, and Table 2 (line 181, *"Comparison of Experimental and Computed $\Delta\Delta G_b$ Values"*) and Table 3 (line 198, *"$\Delta\Delta G_b$ for Each Mutation"*) have headers/captions but no table rows, preventing readers from inspecting the exact computed versus experimental $\Delta\Delta G_b$ values for `GGACAA`, `GGTCCG`, and the single-base intermediates.
* **WHAT & HOW:** Insert the full LaTeX/Markdown equations for Equations 1–5 and populate all rows and columns (including $\pm$ bootstrap/replicate standard deviations across the 5 trajectories and experimental reference values from ref. 65) in Tables 2 and 3.

#### 2. Combine Specific and Nonspecific Conformational States via a Two-State Thermodynamic Cycle or Restraint-Release Estimate
* **WHY:** The authors show that $\Delta\Delta G_b$ is $5.6 \pm 0.2\text{ kcal/mol}$ in the specific recognition pose and $0.4 \pm 0.2\text{ kcal/mol}$ in the rotated $10\ \mu\text{s}$ nonspecific pose (line 191), and note that the true $\Delta\Delta G_b$ lies between these two limits depending on the conformational free energy difference $\Delta G_{\text{conf}}(\text{specific} \to \text{rotated})$ for the native and mutant sequences.
* **WHAT:** Write out the explicit two-state partition function combining the alchemical $\Delta\Delta G_b$ values in both poses with the conformational free energy penalty of rotation (available from the authors' prior umbrella sampling / steered MD study in ref. 54) to show how accounting for the two-state equilibrium brings the net computed $\Delta\Delta G_b$ into quantitative agreement with the experimental value ($\sim 2\text{--}3\text{ kcal/mol}$).
* **HOW:** Using $\Delta G_{\text{bind}}^{\text{eff}} = -k_B T \ln \left( e^{-\beta \Delta G_{\text{bind}}^{\text{spec}}} + e^{-\beta (\Delta G_{\text{bind}}^{\text{rot}} + \Delta G_{\text{conf}})} \right)$, plug in the computed $\Delta\Delta G_b^{\text{spec}} = 5.6\text{ kcal/mol}$ and $\Delta\Delta G_b^{\text{rot}} = 0.4\text{ kcal/mol}$ to illustrate the quantitative correction in Section "Estimating $\Delta\Delta G_b$ for Other Mutants".

#### 3. Report Uncertainties as the Standard Error of the Mean Across Independent Replicates Rather Than Correlated Time-Series Bootstrapping
* **WHY:** In Section "Flattening the Free Energy Landscape Using ALF" (line 112) and line 185, the authors note that uncertainties were calculated via WHAM bootstrapping, which underestimates error when MD frames are temporally correlated, whereas 5 independent trajectories were run per production stage.
* **WHAT:** Clarify whether the uncertainties in Table 1 ($\pm 0.2, \pm 0.4, \pm 0.8\text{ kcal/mol}$) and Tables 2–3 represent the standard deviation (or SEM) across the 5 independent 100 ns production trajectories ($\sqrt{\sigma_{\text{bound}}^2 + \sigma_{\text{unbound}}^2}$) or intra-trajectory WHAM bootstrap estimates, and report the inter-trajectory SD/SEM for all systems.
* **HOW:** Compute $\Delta G_{\text{bound}}^{(k)}$ and $\Delta G_{\text{unbound}}^{(k)}$ separately for each of the $k = 1,\dots,5$ trajectories in Production 4 and report the mean $\pm$ SD (and SEM $= \text{SD}/\sqrt{5}$) in Tables 1–3, alongside fixing the duplicate citation `68, 68` on line 187.
