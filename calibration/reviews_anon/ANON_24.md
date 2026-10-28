# Review of ANON_24

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **6.2 / 10.0** (Mixed / Salvageable)  
* **Score Breakdown:** Rigor: 1.9/3.5 | Claims: 1.7/2.5 | Biology: 1.5/2.0 | Reproducibility: 1.1/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript introduces `BAMM` (Bayesian Analysis of Macroevolutionary Mixtures), a reversible-jump Markov Chain Monte Carlo (rjMCMC) framework and C++ software package that models heterogeneity in speciation and extinction rates across time-calibrated phylogenies of extant species under a compound Poisson process. Within each macroevolutionary regime, speciation rate is allowed to vary exponentially through time ($\lambda(t) = \lambda_0 e^{zt}$) while extinction rate ($\mu$) remains constant. The author evaluates `BAMM` across 3,000 simulated phylogenies spanning six scenarios—constant-rate birth–death (`CR`), a two-process exponential shift (`exp2`), and two- to five-process diversity-dependent radiations (`DD2`–`DD5`)—comparing its regime-count recovery and branch-specific rate accuracy against the stepwise AIC method `MEDUSA`, followed by an empirical application to an 87-species cetacean phylogeny. The C++ codebase (`www.bamm-project.org`) and simulated trees (`Dryad doi:10.5061/dryad.hn1vn`) are publicly available.

Relaxing the assumption of time-constant diversification within macroevolutionary regimes is a valuable conceptual advance, and the author candidly reports poor variance explained ($r^2 = 0.10\text{--}0.16$) and upward bias for extinction rate estimates. However, the manuscript is undermined by three significant methodological and presentation problems: (1) the likelihood differential equations for the lineage extinction probability $E(t)$ omit the compound Poisson transition rate $\Lambda$ on unobserved extinct side-branches and improperly pass $E_0$ across point rate shifts along observed branches; (2) the simulation benchmark against `MEDUSA` omits the constant-rate (`CR`) results for `MEDUSA` from Figures 4, 6, 7, and 8 and lacks a multi-process constant-rate control where `MEDUSA`'s model assumptions hold; and (3) all 15 numbered mathematical equations (`(1)`–`(15)`) are missing from the manuscript text. Addressing the $E(t)$ boundary-condition formulation, adding symmetric constant-rate multi-process benchmarks, and restoring the missing equations are essential before the method's statistical properties can be considered fully validated.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Claim 1: The compound Poisson process rjMCMC likelihood accurately models arbitrary mixtures of diversification regimes across branches. [Methodologically Flawed]**  
  In *Materials and Methods* (lines 138–173), the author computes branch likelihoods by discretizing the BiSSE/FitzJohn differential equations for $D(t)$ (probability of observing the descendant clade) and $E(t)$ (probability that a lineage alive at time $t$ goes extinct before the present). Two mathematical inconsistencies arise in this formulation. First, at a transition point $\xi_i$ on an observed branch, the author sets the initial condition $E_0$ for the ancestral parent segment (governed by regime $\Phi_{\text{parent}}$) equal to the terminal value $E(\xi_i)$ of the descendant segment (governed by regime $\Phi_i$). However, an unobserved side-branch budding off the parent branch *above* $\xi_i$ evolves under $\Phi_{\text{parent}}$, not under the downstream shift $\Phi_i$ that occurred specifically at $\xi_i$ on the surviving lineage. Propagating $E(\xi_i)$ rootwards along the parent branch assigns the descendant regime's extinction probability to ancestral side-lineages. Second, the differential equation for $E(t)$ (Eq. 11) completely omits the compound Poisson shift rate $\Lambda$, implicitly assuming that rate shifts can only occur on the observed surviving tree branches and never on unobserved lineages that later go extinct.

* **Claim 2: BAMM inference of the number of diversification regimes is robust to the prior $\gamma$ on the Poisson transition rate $\Lambda$ and avoids overfitting on constant-rate trees. [Fragile]**  
  In Figure 3A–C (and lines 225, 234–237), when `BAMM` is applied to 500 single-process constant-rate (`CR`) trees under priors $\gamma = 5$ and $\gamma = 10$, the maximum a posteriori (MAP) model is biased toward a two-process model ($M_1$, containing a false rate shift). The author argues that this overfitting is benign because the true single-process model ($M_0$) retains a posterior probability $>0.05$ (or $>0.10$ in Fig. 3F). In Bayesian model selection, a true null model having posterior probability as low as $0.05\text{--}0.15$ means the posterior odds / Bayes factor strongly favors a nonexistent rate shift whenever $\gamma \ge 5$. Similarly, in the empirical cetacean dataset (chunk 2, line 22), changing $\gamma$ from $1$ to $10$ shifts the MAP estimate from 2 processes to 4 processes.

* **Claim 3: BAMM substantially outperforms MEDUSA in estimating regime numbers and branch-specific speciation rates. [Moderately Supported]**  
  Across the five time-varying and diversity-dependent scenarios (`exp2`, `DD2`–`DD5`), `BAMM` recovers the true number of regimes and branch-specific speciation slopes far more accurately than `MEDUSA` (Figs. 4 vs. 7 and Figs. 6 vs. 8). However, this comparison is asymmetric by construction: `exp2` and `DD2`–`DD5` all feature strong temporal declines or changes in speciation rate within clades, which `BAMM` explicitly parameterizes ($\lambda(t) = \lambda_0 e^{zt}$) and standard `MEDUSA` ($z = 0$) does not. Although the author states that `MEDUSA` was run on all 3,000 trees including the 500 `CR` trees (line 212), the `CR` results are omitted from Figures 4, 6, 7, and 8, and no multi-process *constant-rate* simulation scenario (`CR2`–`CR5`) was included to benchmark `BAMM` vs. `MEDUSA` when rates are time-homogeneous within clades.

* **Claim 4: Cetacean diversification is characterized by a two-regime history featuring a >6-fold burst and subsequent slowdown in the ancestral branch leading to Delphinidae. [Moderately Supported]**  
  The localization of a major rate shift along the stem/crown branches of Delphinidae (posterior probability $>0.975$ across three adjacent branches; Fig. 9B) is consistent with independent paleontological and `MEDUSA`-based analyses (Steeman et al.; Slater et al.) and remains stable across $\gamma \in [0.1, 10]$ (Fig. 10). However, as noted above, exact posterior odds ($44.6$ against $M_1$) and branch-rate credibility intervals are contingent on the approximate $E(t)$ calculation and fixed tree topology.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Correct the Extinction Probability $E(t)$ Boundary Conditions at Rate Shifts
* **WHY:** Passing $E(\xi_i)$ from a derived regime $\Phi_i$ rootwards into the ancestral regime $\Phi_{\text{parent}}$ along an observed branch wrongly assumes that unobserved side-lineages budding off above the shift $\xi_i$ inherit the downstream shift's extinction trajectory.
* **WHAT:** Decouple the extinction probability calculation $E_{\text{parent}}(t)$ of the ancestral regime from downstream point transitions $\xi_i$ when integrating $D(t)$ above $\xi_i$, and explicitly document the conditioning of the compound Poisson process on observed vs. unobserved branches.
* **HOW:** For any regime $\Phi_k$ governing a branch segment at time $t$, compute $E_k(t)$ by integrating Eq. (11) from the present ($t = 0$, where $E_k(0) = 1 - f$) to time $t$ strictly under the parameters $(\lambda_k(t), \mu_k)$ of regime $\Phi_k$, and use that regime-specific $E_k(t)$ inside the differential equation for $D(t)$ (Eqs. 10 and 13) along all segments belonging to $\Phi_k$. Re-run the `CR` prior sensitivity check (Fig. 3) to verify whether fixing $E_k(t)$ eliminates the MAP bias toward $M_1$ under $\gamma = 5$ and $\gamma = 10$.

#### 2. Add Multi-Process Constant-Rate Controls and Report `CR` Results for MEDUSA
* **WHY:** Evaluating `MEDUSA` exclusively on time-varying (`exp2`) and diversity-dependent (`DD2`–`DD5`) trees demonstrates that `MEDUSA` fails when its constant-rate assumption is violated, but does not compare `BAMM` and `MEDUSA` under symmetric conditions where within-regime rates are constant.
* **WHAT:** Report the already-computed `CR` (1-process) results for `MEDUSA` alongside `BAMM`, and simulate a multi-process constant-rate birth–death scenario (e.g., `CR2` and `CR3` with $z = 0$ in each regime) to compare both methods on equal footing.
* **HOW:** Add a panel to Figures 3/7 and 5/8 showing `MEDUSA`'s false-positive shift rate and speciation/extinction accuracy on the 500 `CR` trees, and run 500 simulations of a 3-process piecewise-constant birth–death model comparing `BAMM` (both unconstrained $z$ and constrained $z=0$) against `MEDUSA`.

#### 3. Use Bayes Factors Relative to the Prior Rather Than Raw MAP Regime Counts for Model Selection
* **WHY:** As shown in Figure 3A–C and the cetacean sensitivity analysis (chunk 2, line 22), the raw MAP model $M_k$ shifts upward as the prior mean $\gamma$ on the number of transitions increases from $0.1$ to $10$.
* **WHAT:** Recommend and report Bayes factors $\text{BF}_{k,0} = \frac{P(M_k \mid \text{data}) / P(M_0 \mid \text{data})}{\pi(M_k \mid \gamma) / \pi(M_0 \mid \gamma)}$ (which divide out the marginal prior model odds induced by $\gamma$) alongside MAP regime counts.
* **HOW:** Compute the analytical marginal prior distribution $\pi(M_k \mid \gamma) = \frac{\gamma^k}{(1 + \gamma)^{k+1}}$ (a geometric distribution resulting from a Poisson($\Lambda$) count mixed with an Exponential($1/\gamma$) hyperprior on $\Lambda$) and report the prior-corrected Bayes factors for the simulated and cetacean datasets.

#### 4. Technical, Mathematical, and Editorial Cleanup
* **WHY:** All 15 mathematical equations are missing from the manuscript text, preventing verification of the exact likelihood and rjMCMC acceptance formulas.
* **WHAT & HOW:**
  * **Equations (1) through (15) (Materials and Methods, lines 45, 62, 72, 82, 92, 102, 112, 122, 130, 142, 148, 156, 164, 189, 201):** Every equation table cell in the manuscript is completely empty (`| | (1) |`). Insert the full LaTeX/mathematical expressions for all 15 equations into the text.
  * **Subscript Typo (Materials and Methods, line 86):** Fix *"Variables $\nu_1, \nu_2, \nu_2$, and $\nu_3$ were sampled from the corresponding prior distributions for $\xi, \lambda_0, z$, and $\mu$"* to *"$\nu_1, \nu_2, \nu_3$, and $\nu_4$"*.
  * **Figure 4 Caption (Results, line 245):** Fix the duplicate word *"although **though** most analyses (80.4%) recovered"* to *"although most analyses (80.4%) recovered"*.
  * **Cross-Reference Error (Results, line 286):** In *"The number of processes inferred for each simulation scenario are shown in Figure 7 and can be compared to the corresponding BAMM results shown in Figure 3"*, change `"Figure 3"` (which shows only `CR`) to `"Figure 4"` (which shows `exp2` and `DD2`–`DD5`, as correctly noted two sentences later).
