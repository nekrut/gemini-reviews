# Review of FEXP_ANON_014

**Overall Score:** **8.2 / 10.0** (Strong / Sound) | **Scientific Core Score:** **6.4 / 8.0**  
* **Score Breakdown:** Rigor: 2.6/3.5 | Claims: 2.0/2.5 | Biology: 1.8/2.0 | Reproducibility: 1.8/2.0

---

## 1. Blinded Metadata Perception
* **Anonymized Manuscript ID:** `FEXP_ANON_014`
* **Perceived Domain & Design:** Zoonotic viral phylodynamics, spatial epidemiology, and wildlife disease management; 16-year retrospective observational study (2003–2018) combining livestock rabies passive surveillance ($n = 1,029$ outbreaks across 68 districts in southern Peru), 205 farmer bite-incidence surveys, Bayesian zero-inflated Poisson state-space modeling, multiplex whole-genome sequencing ($n = 319$ N-gene sequences and $n = 290$ Lineage 3 complete genomes), and continuous phylogeographic branch-velocity modeling (`BEAST` + `Seraphim`).
* **Blinding Integrity:** Double-blind review maintained; evaluated strictly on internal mathematical, statistical, phylogeographic, and epidemiological merits at $t_0$.

---

## 2. Executive Summary & Editorial Verdict

This study evaluates whether anticoagulant ("vampiricide") culling of common vampire bats (*Desmodus rotundus*) across three regions of southern Peru (`AAC`: Apurímac, Ayacucho, and Cusco; 23,665 bats treated in 39 districts between 2014 and 2016) reduced vampire bat rabies virus (`VBR`) spillover to livestock or slowed spatial viral spread. Combining farmer questionnaires (showing lower perceived bite rates in culled districts), a Bayesian hierarchical zero-inflated Poisson (ZIP) state-space model fit to 16 years of monthly district-level outbreaks ($n = 1,029$), and continuous phylogeographic reconstructions of 290 newly generated complete `VBR` Lineage 3 genomes, the authors find that: (1) preventive culling did not significantly increase the probability of a district remaining rabies-free ($\alpha_3 = -0.35$, 95% CrI $[-0.95, 0.25]$); (2) reactive culling over the prior 6 months was positively associated with subsequent outbreak counts in already-infected districts ($\beta_4 = 0.089$, 95% CrI $[0.056, 0.12]$); and (3) phylogenetic branches originating or terminating in culled districts exhibited $37\%\text{–}41\%$ higher spatial dispersal velocity ($14.4\text{ vs. }10.2\text{ km/year}$ at origin; $14.3\text{ vs. }10.4\text{ km/year}$ at destination) in `Seraphim` general linear models across 1,000 posterior trees.

**Editorial Verdict: Minor Revision (Strong / Sound).** This is an ambitious, unusually thorough, and methodologically rich integration of longitudinal epidemiological surveillance and whole-genome continuous phylogeography, supported by public deposition of 597 viral sequences and Dryad code/data (`10.5061/dryad.bcc2fqz99`). However, three mathematical and inferential issues require revision: (1) **the state-space model equations in Materials and Methods (lines 100, 102, and 104) are mathematically corrupted**—overloading $z_{i,t}$ on both sides of $z_{i,t} \sim \text{Bernoulli}(1 - z_{i,t})$, applying a $\log$ link to the binary outcome $z_{i,t}$ in line 102, and writing $\text{logit}(O_{i,t}) = \beta_{0,i} + \dots$ in line 104 for a Poisson count process $O_{i,t}$ whose intensity rate $r_{i,t}$ requires a $\log$ link; (2) **confounding by indication (reverse causality) in observational reactive culling**, where intense emerging epizootic waves simultaneously trigger government culling campaigns and exhibit higher outbreak momentum and faster spatial advance; and (3) **post-selection inference bias (`stepAIC`)** when reporting branch-velocity regression coefficients conditional on retention by automated stepwise AIC selection across 1,000 posterior trees.

### Assessment of Specific Claims
* **Claim 1 (Peruvian `VBR` outbreaks in `AAC` from 1997 to 2016 were driven predominantly [94.7%] by a single monophyletic viral lineage [Lineage 3] spreading at a weighted branch velocity of $9.6\text{ km/year}$ [95% CrI $8.4\text{–}11.3$]): [Well Supported].**  
  The multiplex PCR whole-genome sequencing of 290 `L3` isolates exhibits strong clock-like evolution (`TempEst` $R^2 = 0.62$, slope $3.16 \times 10^{-4}\text{ subs/site/year}$), and the Cauchy relaxed random walk continuous phylogeographic model in `BEAST` is strongly favored over gamma and lognormal diffusion models ($\text{BF} = 36.8$ and $52.8$).
* **Claim 2 (Vampiricide culling failed to halt rabies persistence in endemic districts and preventive culling did not significantly increase the probability of zero outbreaks [$\alpha_3 = -0.35$, 95% CrI $[-0.95, 0.25]$]): [Well Supported].**  
  Both raw spatiotemporal outbreak trajectories (`Fig. 1D`) and the Bayesian ZIP state-space model demonstrate persistent viral circulation throughout historically affected valleys despite treating $>23,000$ bats.
* **Claim 3 (Reactive culling exacerbated local outbreak incidence [$\beta_4 = 0.089$, 95% CrI $[0.056, 0.12]$] and accelerated spatial viral dispersal velocity by $37\%\text{–}41\%$): [Fragile].**  
  Because culling was not randomized—and reactive culling was specifically deployed in districts experiencing intense epizootic emergence—positive associations between culling and subsequent outbreak counts or phylogenetic branch velocity are vulnerable to **confounding by indication (reverse causality)**. In the ZIP count model (line 104), controlling only for a single 1-month linear lag $O_{i,t-1}$ does not fully absorb multi-month nonlinear epizootic wave acceleration. Similarly, in the `Seraphim` velocity GLMs (line 42 of chunk 2), coding culling as a coarse **district-level binary indicator** while fast-moving epizootic wavefronts trigger district culls means that fast viral spread can cause reactive culling rather than culling causing fast viral spread.

---

## 3. Forensic Defect Inventory

1. **Pillar 2 & 3 Violation — Mathematically Corrupted Equations in the Bayesian ZIP State-Space Model Specification (Methods Lines 96–104):**  
   Inspect the formal mathematical specification of the epidemiological model in lines 96–104:
   * **Line 96:** $O_{i,t} \sim \text{Poisson}(r_{i,t} \cdot (1 - z_{i,t}))$, where $O_{i,t}$ is the latent outbreak count, $r_{i,t}$ is the Poisson intensity rate, and $z_{i,t} \in \{0, 1\}$ is the zero-inflation binary indicator.
   * **Line 100:** $z_{i,t} \sim \text{Bernoulli}(1 - z_{i,t})$. This is mathematically invalid: the random variable $z_{i,t}$ appears on both the left-hand side (as the realized binary draw) and the right-hand side (as the success probability parameter $p_{i,t}$).
   * **Line 102:** $\log(z_{i,t}) = \alpha_1 \frac{\sum_{\ldots} \exp(-\alpha_3 C_{j,t-1}) O_{j,t-1}}{n_i} + \alpha_2 O_{i,t-1}$. Taking the logarithm of a binary variable $z_{i,t} \in \{0, 1\}$ yields $-\infty$ whenever $z_{i,t} = 0$! Clearly, the left-hand side is supposed to be $\log(p_{i,t})$ (or $-\Lambda_{i,t}$ where $1 - p_{i,t} = \exp(-\Lambda_{i,t})$ so that $p_{i,t} \in (0,1]$).
   * **Line 104:** $\text{logit}(O_{i,t}) = \beta_{0,i} + \beta_1 L_{i,t} + \beta_2 S_t + \beta_3 O_{i,t-1} + \beta_4 C_{i,[t-1:t-m]} + \beta_5 V_{i,[t-1:t-12]}$. This equation contains two compounding errors: (i) the left-hand side puts the realized integer count $O_{i,t}$ inside the link function instead of the Poisson mean parameter $r_{i,t}$, and (ii) it applies a $\text{logit}(\cdot)$ link instead of a $\log(\cdot)$ link! Because $O_{i,t}$ (and $r_{i,t}$) can exceed 1, $\text{logit}(x) = \log(x/(1-x))$ is undefined for all $x \ge 1$.
2. **Pillar 1 & 4 Violation — Observational Confounding by Indication in Reactive Culling ($\beta_4 > 0$ and Branch Velocity Elevation):**  
   Government culling campaigns in Peru during 2014–2016 were targeted to districts experiencing severe livestock mortality spikes. When an invading rabies wavefront enters a naïve, high-suitability valley, outbreak counts accelerate over several consecutive months and phylogenetic lineages disperse rapidly along the valley corridor. Because reactive culling is triggered by the onset of these intense multi-month waves, conditioning only on the prior month's outbreak count $O_{i,t-1}$ (in the ZIP model) or on coarse 10-km average annual outbreak counts (in the `Seraphim` GLM) leaves residual confounding by local epizootic momentum.
3. **Pillar 2 Violation — Post-Selection Inference Bias (`stepAIC`) in Posterior Tree Branch-Velocity Regressions (Methods Line 40 of Chunk 2; Fig. 4C–D):**  
   To evaluate drivers of branch velocity across 1,000 posterior trees, the authors run backward stepwise AIC selection (`stepAIC`) on each tree independently and report *"the effect sizes of each variable, conditional on being retained by model selection"* (line 40 of chunk 2). Conditioning parameter estimates on Passing an AIC selection threshold (`stepAIC`) truncates the sampling distribution near zero and induces classic post-selection ("winner's curse") upward bias in the reported mean/CrI of $\beta$. Fitting the full multivariable GLM across all 1,000 posterior trees without stepwise variable dropping provides unbiased unconditional posterior effect sizes.
4. **Pillar 5 Violation — Spatial Resolution Mismatch Between District-Level Culling and Point-Level Phylogenetic Nodes (Methods Line 42 of Chunk 2):**  
   While livestock density, terrain ruggedness, and sampling intensity were extracted within a $10\text{-km}$ buffer around each inferred internal node's coordinates, culling was coded as a **district-level binary indicator**. Because Peruvian districts vary substantially in area and internal phylogenetic node coordinates carry continuous spatial uncertainty (95% HPD polygons), assigning district-level binary culling status to point estimates of internal nodes introduces spatial misclassification error.

---

## 4. Quantitative Rubric Scoring

| Rubric Dimension | Score | Max | Forensic Justification |
| :--- | :---: | :---: | :--- |
| **1. Methodological & Statistical Rigor** | **2.6** | **3.5** | Strong combination of Bayesian state-space epidemiological modeling, 290-genome Cauchy continuous phylogeography, and randomization controls; penalized for corrupted link/variable equations in Methods lines 100–104, conditional `stepAIC` selection bias, and confounding by indication. |
| **2. Claim-to-Evidence Alignment** | **2.0** | **2.5** | Claims that culling failed to eliminate viral circulation are strongly supported; claims that reactive culling causally exacerbated outbreaks and accelerated viral velocity require stronger caveats regarding reverse causality (epizootic intensity triggering reactive culling). |
| **3. Data Integrity & Biological/Behavioral Plausibility** | **1.8** | **2.0** | Exemplary integration of vampire bat ecology, custom `primalscheme` multiplex whole-genome sequencing, and field surveillance across 16 years. |
| **4. Reproducibility & Data Integrity** | **1.8** | **2.0** | Complete sequence deposition (`MW428990–MW429308`, `MW439040–MW439317`) and public Dryad repository (`10.5061/dryad.bcc2fqz99`); minor deduction for the corrupted mathematical equations in lines 100–104. |
| **Total Composite Score** | **8.2** | **10.0** | **Strong / Sound** (Scientific Core Score: **6.4 / 8.0**) |

---

### Constructive and Doable Suggestions for Improvement

1. **Correct the Corrupted Mathematical Equations in the ZIP State-Space Model (Lines 96–104):**  
   * **WHY:** Writing $z_{i,t} \sim \text{Bernoulli}(1 - z_{i,t})$ (line 100), $\log(z_{i,t}) = \dots$ (line 102), and $\text{logit}(O_{i,t}) = \dots$ (line 104) is mathematically undefined and misrepresents the actual `JAGS` code.  
   * **WHAT & HOW:** Introduce a distinct symbol $p_{i,t} \in (0,1)$ for the zero-inflation probability so that $z_{i,t} \sim \text{Bernoulli}(p_{i,t})$ with $\log(1 - p_{i,t}) = -\Lambda_{i,t}$ (or $\text{logit}(p_{i,t}) = \dots$), and replace $\text{logit}(O_{i,t})$ in line 104 with $\log(r_{i,t}) = \beta_{0,i} + \beta_1 L_{i,t} + \dots$ matching the Poisson intensity rate $r_{i,t}$ defined in line 96.
2. **Report Unconditional Full-Model Posterior GLM Effect Sizes Alongside `stepAIC`-Conditioned Estimates:**  
   * **WHY:** Summarizing $\beta$ coefficients only across the subset of posterior trees in which a variable survived `stepAIC` selection (line 40 of chunk 2) inflates effect sizes away from zero.  
   * **WHAT & HOW:** In Figure 4C–D (or Table S2), report the unconditional posterior mean and 95% credible interval of each standardized coefficient across all 1,000 posterior trees from the full multivariable GLM without `stepAIC` pruning.
3. **Test Sensitivity of the Reactive Culling Effect ($\beta_4$) to Multi-Month Epizootic Wave Momentum (Distributed Lags $O_{i,t-2}, O_{i,t-3}$ or Pre-Cull Trend Falsification):**  
   * **WHY:** To distinguish whether reactive culling truly worsens outbreaks ($\beta_4 > 0$) versus whether culling is simply deployed during the rising phase of large multi-month epizootic waves (confounding by indication).  
   * **WHAT & HOW:** Add a falsification ("lead") covariate testing whether future culling $C_{i,[t+1:t+3]}$ also "predicts" current outbreaks $O_{i,t}$ (which diagnoses reverse causality / targeting of rising waves), and include second-order autoregressive terms ($O_{i,t-2}$ or the local growth rate $O_{i,t-1} - O_{i,t-2}$) in the count model.
