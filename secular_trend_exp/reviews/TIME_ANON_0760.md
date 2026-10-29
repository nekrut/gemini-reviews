<Blinded Review: TIME_ANON_0760>
**Composite Score:** 4.5 / 10.0 (Rigor: 1.4/3.5 | Claims: 1.5/2.5 | Biology: 0.8/2.0 | Reproducibility: 0.8/2.0)
**Bias Category:** Statistical/Design
**Verdict:** Major Revision
**Study Modality:** Dry-Lab Secondary Cohort/Database
**Technology Maturity:** Mature/Classical
**Epistemic Stage:** Clinical/Observational

OVERALL_SCORE: 4.5/10
VERDICT: CAVEATS
ESTIMATED_DECADE: 1990s

---

### 1. Executive Summary / SUMMARY
This brief statistical genetics workshop paper (from Genetic Analysis Workshop 11, analyzing the Collaborative Study on the Genetics of Alcoholism [COGA] dataset of 1,614 individuals in 143 multiplex pedigrees ascertained for $\ge 3$ members with alcohol dependence) applies parametric two-disease-locus linkage and heterogeneity analysis (`TLINKAGE` and `HOMOG`) to four candidate microsatellite markers (`D1S1595`, `D6S1006`, `D7S1797`, and `D15S642`) previously flagged by single-locus scans. Testing five symmetric diallelic two-locus penetrance architectures (dominant/dominant, dominant/recessive, recessive/dominant, recessive/recessive, and modified dominant/dominant with fixed phenocopy rate $0.05$) across unspecified grids of allele frequencies and penetrances, the authors report LOD $< 0.2$ for `D1S1595` and `D6S1006`, and heterogeneity LOD (`HLOD`) scores of $1.8$ ($\alpha = 10\%$ linked families) for `D7S1797` and $4.47$ ($\alpha = 20\%$ linked families) for `D15S642`—virtually identical to single-locus `HLOD` scores ($2.0$ and $4.29$, respectively). While the negative conclusion (that two-locus modeling offers no gain over single-locus `HLOD` and detects no epistatic interaction among these four markers) is candidly stated, the methodological execution is flawed: despite claiming to investigate "pair-wise genetic epistasis of these loci," the authors actually ran **two-disease-locus / one-marker-locus** analyses ($\text{LOD}(\theta_1, \theta_2 = 0.5)$) rather than joint two-marker linkage analyses ($\text{LOD}(\theta_1, \theta_2)$), and failed to adjust `HLOD` thresholds for maximizing over five genetic models, a grid of penetrances/allele frequencies, and the heterogeneity parameter $\alpha$.

### 2. Methodological & Statistical Audit / STRENGTHS & WEAKNESSES

#### STRENGTHS
- **Direct Single-Locus vs. Two-Locus HLOD Comparison:** Benchmarking the maximized two-locus `HLOD` directly against the single-locus `HLOD` on the exact same pedigrees (Table 1: $4.47$ vs. $4.29$ at `D15S642`; $1.8$ vs. $2.0$ at `D7S1797`) transparently demonstrates that adding an unlinked second disease locus adds no explanatory power.

#### WEAKNESSES & METHODOLOGICAL AUDIT
- **Fundamental Mismatch Between Claimed "Pair-Wise Epistasis" and Executed One-Marker Model:** Both the Abstract (*"investigated... pair-wise genetic epistasis of these loci"*) and Discussion (*"There are no gene $\times$ gene interactions between D7S1797 and D15S642 and other postulated disease loci"*) claim to test epistatic interactions between the candidate markers. However, as stated in the Methods (line 31–33) and Results (line 46), the authors only ran **two-disease-locus / one-marker-locus** analyses:
  $$\text{LOD}(\theta) = \log_{10} \frac{L(\theta, 0.5)}{L(0.5, 0.5)}$$
  where the second disease locus is fixed as **completely unlinked ($\theta_2 = 0.5$) to any marker**! In a one-marker analysis where the second trait locus is an ungenotyped latent locus segregating independently across the pedigree, `TLINKAGE` cannot test whether `D7S1797` and `D15S642` interact with *each other*; doing so requires a **two-disease-locus / two-marker-locus** likelihood $L(\theta_1, \theta_2)$ conditioned simultaneously on genotypes at both `D7S1797` and `D15S642`.
- **Unpenalized Maximization Over Model Space (MMOD / Max-HLOD Inflation):** The authors state that *"A wide range of penetrance values and allele frequencies on the disease loci were carried out in the TLINKAGE program for each of the five models"*, and then passed the family-level LOD scores into `HOMOG` to maximize over the linked-family proportion $\alpha$, reporting only *"the results of the highest HLOD scores"* in Table 1.
  1. Maximizing LOD over multiple inheritance models, a grid of allele frequencies, a grid of penetrances, *and* the admixture parameter $\alpha$ (`HLOD`) invalidates the standard 1-df $\frac{1}{2}\chi^2_0 + \frac{1}{2}\chi^2_1$ asymptotic distribution cited on line 35 (even a standard `HLOD` with fixed genetic parameters has a 2-parameter mixture distribution under the null, and maximizing over a grid of penetrance/frequency models adds further degrees of freedom).
  2. Markers `D1S1595`, `D6S1006`, `D7S1797`, and `D15S642` were pre-selected *from the exact same COGA dataset* because they had high single-locus scores in prior GAW11 analyses (`[10]`), creating double-dipping ascertainment bias.
- **Boundary Estimate $\hat{\theta} = 0.0$ with Low $\hat{\alpha}$ ($10\%\text{--}20\%$):** In Table 1, both reported `HLOD` peaks occur at $\theta = 0.0$ with only $10\%$ (15/143) or $20\%$ (31/143) of pedigrees linked. In parametric linkage analysis of complex traits without true major-gene Mendelian segregation, `HOMOG` routinely absorbs pedigree-specific non-segregation into $1 - \hat{\alpha}$ (80–90% unlinked families) while driving $\hat{\theta} \to 0$ on the small subset of families that happen to share alleles by chance.
- **Missing Parameter Reporting:** The exact grid of disease allele frequencies ($p_1, p_2$) and penetrance values ($f_{ij}$) searched—and the specific parameter values that achieved the maximum `HLOD` of $4.47$ and $1.8$ in Table 1—are never reported anywhere in the paper!

### 3. Biological / Experimental Grounding & Claim Proportionality
- **Claim 1:** *Two-disease-locus modeling does not improve linkage detection over single-locus modeling for `D1S1595`, `D6S1006`, `D7S1797`, and `D15S642` in the COGA dataset.* `[Well Supported]` — Directly shown by the near-equality of single-locus and two-locus `HLOD` values in Table 1 and near-zero LODs on chromosomes 1 and 6.
- **Claim 2:** *Neither `D7S1797` nor `D15S642` interacts epistatically with other disease loci.* `[Methodologically Flawed]` — A one-marker `TLINKAGE` run ($\theta_2 = 0.5$) only integrates over an unlinked latent background locus under symmetric penetrance constraints; it does not test pairwise marker-by-marker epistasis between `D7S1797` and `D15S642`.

### 4. Reproducibility & Data Completeness
- **Severe Omission of Model Parameters:** While the COGA GAW11 dataset and software (`TLINKAGE`, `HOMOG`) are standard for the era, the manuscript omits the exact penetrance matrices, disease allele frequency grids, COGA diagnostic definition used (e.g., DSM-III-R/Feighner definite vs. probable), and the maximizing parameter values for Table 1, making exact numerical replication impossible.
</Blinded Review: TIME_ANON_0760>
