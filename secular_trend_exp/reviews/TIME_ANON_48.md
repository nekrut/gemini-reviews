# Blinded Review: TIME_ANON_48
**Composite Score:** 7.5 / 10.0 (Rigor: 2.7/3.5 | Claims: 2.0/2.5 | Biology: 1.5/2.0 | Reproducibility: 1.3/2.0)
**Bias Category:** None (Methodologically Sound)
**Verdict:** Minor Revision
**Study Modality:** Dry-Lab Theory/Methods/Simulation
**Technology Maturity:** Mature/Classical
**Epistemic Stage:** Translational/Preclinical/Biomarker

---

### 1. Executive Summary

This methodological biostatistics manuscript extends two genetic model-robust association tests—the Maximin Efficiency Robust Test (`MERT`) and the maximum test (`MAX` over recessive $x=0$, additive $x=1/2$, and dominant $x=1$ Cochran–Armitage trend scores)—to family-based case-control studies where cases and/or controls are biologically related. Building on the variance-covariance adjustment of Slager and Schaid (which accounts for identity-by-descent [IBD] allele sharing among relatives) and the independent-sample robust tests of Freidlin et al., the authors derive the inter-model correlation matrix $\text{Corr}(Z_{x_0}, Z_{x_1})$ under family correlation, formulate $Z_{\text{MERT}}$ and $Z_{\text{MAX}}$ for both biallelic and multiallelic markers, evaluate empirical Type I error and power across 20,000 simulated datasets (80 affected sib-pairs vs 160 unrelated controls), and illustrate the method on Collaborative Study on the Genetics of Alcoholism (COGA / GAW14) pedigree data for SNP `rs1037475` ($N = 609$ cases and $261$ controls across 143 families).

The mathematical derivations, asymptotic distributions, simulation design, and real-data numerical calculations are sound and internally consistent. The primary limitations are: (1) in the COGA application, `rs1037475` was pre-selected via an unadjusted backward-selection logistic regression on the same dataset prior to applying the family-adjusted trend tests (introducing post-selection winner's curse into the illustrative $p$-values); (2) the simulation study evaluates correlated cases (affected sib-pairs) against independent controls but does not simulate pedigrees containing both related cases and related controls in the same family; and (3) several inline mathematical expressions in the Methods text were dropped during document formatting/typesetting and must be restored.

---

### 2. Methodological & Statistical Audit

* **Verification of Mathematical Derivations and Numerical Consistency:**
  The formulation of the score statistic $U(\mathbf{x}) = \mathbf{x}'[(1-\phi)\mathbf{r} - \phi\mathbf{s}]$ and its IBD-adjusted variance-covariance matrix $\text{Var}[U(\mathbf{x})] = \mathbf{x}'\boldsymbol{\Sigma}\mathbf{x}$ properly generalizes the Cochran–Armitage trend test to correlated pedigree members. Auditing the numerical values reported in the *Application* section against Table 3 (`Case: 153 NN, 278 NM, 178 MM [R=609]`; `Control: 69 NN, 141 NM, 51 MM [S=261]`):
  - In Table 3, the risk homozygote `MM` frequency is $178/609 = 29.23\%$ in cases vs $51/261 = 19.54\%$ in controls, while the heterozygote `NM` + `MM` dominant frequency is $456/609 = 74.88\%$ in cases vs $192/261 = 73.56\%$ in controls. This explains why the recessive test ($Z_{x=0} = 2.89, p = 0.004$) and additive test ($Z_{x=1/2} = 2.02, p = 0.043$) are significant while the dominant test ($Z_{x=1} = 0.40, p = 0.69$) is null.
  - Using the reported extreme-model correlation $\rho_0 = \text{Corr}(Z_0, Z_1) = 0.334$, the MERT statistic is:
    $$Z_{\text{MERT}} = \frac{Z_0 + Z_1}{\sqrt{2(1 + \rho_0)}} = \frac{2.89 + 0.40}{\sqrt{2(1 + 0.334)}} = \frac{3.29}{1.6334} = 2.0142 \approx 2.01$$
    with two-sided asymptotic $p = 2(1 - \Phi(2.014)) = 0.0440$, matching the authors' reported `ZMERT = 2.01 with p-value = 0.044` to the last decimal place.
  - Likewise, $Z_{\text{MAX}} = \max(|Z_0|, |Z_{\text{MERT}}|, |Z_1|) = 2.89$ yields an empirical $p = 0.009$ (1,000,000 replicates), which appropriately lies between the single-model $p = 0.004$ and the Bonferroni bound $3 \times 0.004 = 0.012$.

* **Post-Selection Inference in the COGA Real-Data Illustration:**
  In the *Application* section, the authors state: *"Without adjusting for family structure, a logistic regression with backward selection of SNPs from the Illumina dataset near the ADH genes indicated that SNP marker rs1037475 was a significant predictor. Here we applied the association tests to case-control data... for this SNP marker."* Selecting the top SNP via unadjusted backward stepwise regression on the same sample and subsequently computing marginal $p$-values (`p = 0.044` for MERT, `p = 0.009` for MAX) without accounting for the number of candidate SNPs screened in the *ADH3* region does not control the region-wide Type I error rate. While acceptable as a single-marker methodological demonstration on GAW14 benchmark data, this caveat should be explicitly noted.

* **Simulation Scope Limited to Unrelated Controls and Known IBD:**
  In Table 2, the simulation study generates 160 cases as 80 affected sib-pairs (with theoretical prior IBD probabilities $\pi_0 = 1/4, \pi_1 = 1/2, \pi_2 = 1/4$) and 160 unrelated controls. However, in real family datasets like COGA (Table 3, where 609 cases come from 143 families and 261 controls come from 111 families within the same 143 pedigrees), cases and controls are negatively correlated across the $(1-\phi)\mathbf{r} - \phi\mathbf{s}$ contrast due to within-family discordant relative pairs ($\text{Cov}(\mathbf{r}, \mathbf{s}) \neq \mathbf{0}$). Extending the simulation to include discordant sib-pairs or multi-generational pedigrees with both cases and controls would better match the COGA application.

* **Multiallelic Extension Formulation (`MERT` and `MAX` over $K-1$ Alleles):**
  In the section *The trend tests with multiple alleles*, the authors define $Z_j = U_j / \sigma_j$ for alleles $j = 1, \dots, K-1$ for a fixed score vector $\mathbf{x}_j$, and suggest applying MERT and MAX across the $K-1$ alleles. Note that for a multiallelic marker under unknown mode of inheritance, there are two distinct sources of uncertainty: which allele(s) confer risk, and what the dominance parameter $x \in [0, 1]$ is. Taking MERT (a linear sum of the two least-correlated allele statistics) across different alleles at a multiallelic locus is less interpretable than an omnibus $\chi^2_{K-1}$ test or a MAX test over both alleles and genetic models.

---

### 3. Biological / Experimental Grounding & Claim Proportionality

* **Claim that `MERT` and `MAX` Protect Against Mode-of-Inheritance Misspecification in Family Case-Control Studies: `[Well Supported]`**
  Table 2 clearly demonstrates that while single-model trend tests lose substantial power under misspecification (e.g., $Z_{x=0}$ drops from $0.80$ power under a recessive model to $0.18$ under a dominant model, and $Z_{x=1}$ drops from $0.80$ to $0.26$ under a recessive model), `MAX` maintains $0.73\text{--}0.76$ power and `MERT` maintains $0.64\text{--}0.77$ power across all three models while holding empirical Type I error at exactly $0.05$.

* **Claim that `MAX` Outperforms `MERT` When $\rho_0$ is Small: `[Well Supported]`**
  In both the simulation study and the COGA dataset ($\rho_0 = 0.334 < 0.75$), `MAX` achieves higher power and stronger significance than `MERT`, consistent with the theoretical efficiency properties established by Freidlin et al.

---

### 4. Reproducibility & Data Completeness

* **Strengths:** The simulation parameters ($K = 0.1$, $p = 0.3$, $N_{\text{cases}} = 160$, $N_{\text{controls}} = 160$, 20,000 replicates, $RR_1$ and $RR_2$ values) and the full $2 \times 3$ genotype contingency table for COGA SNP `rs1037475` (Table 3) are completely specified.
* **Editorial & Formatting Deficiencies (Missing Inline Equations):**
  Several inline equations in the *Methods* section were stripped during document conversion and appear as blank spaces before punctuation:
  1. Line 24: `and .` (missing $\sum_{j=0}^2 p_j = \sum_{j=0}^2 q_j = 1$).
  2. Line 34: `where ,` (missing $U(\mathbf{x}) = \sum_{j=0}^2 x_j [(1-\phi)r_j - \phi s_j]$) and `it can be shown that ,` (missing $\text{E}[U(\mathbf{x})] = 0$).
  3. Line 38–40: missing $\sum_{i=1}^R \mathbf{y}_i$, $\sum_{j=1}^S \mathbf{z}_j$, and the explicit matrix display equation for $\text{Var}[U(\mathbf{x})]$.
  4. Line 49–50: `Let the variance-covariance matrix .` (missing $\boldsymbol{\Sigma} = \text{Var}[(1-\phi)\mathbf{r} - \phi\mathbf{s}]$ and the display equation for $\text{Corr}(Z_{\mathbf{x}_0}, Z_{\mathbf{x}_1})$).
  5. Line 60: `and we have = Var(Uj)` (missing $\sigma_j^2$) and `and .` (missing $\text{Cov}(U_j, U_k) = \mathbf{x}_j'\boldsymbol{\Sigma}\mathbf{x}_k$).
  Restoring these LaTeX/MathML equations is essential for a self-contained methods paper.
