<Blinded Review: TIME_ANON_0558>
OVERALL_SCORE: 8.2/10
VERDICT: PASS
ESTIMATED_DECADE: 2010s
**Composite Score:** 8.2 / 10.0 (Rigor: 3.0/3.5 | Claims: 2.0/2.5 | Biology: 1.5/2.0 | Reproducibility: 1.7/2.0)
**Bias Category:** None (Methodologically Sound)
**Verdict:** Minor Revision
**Study Modality:** Dry-Lab Theory/Methods/Simulation
**Technology Maturity:** Mature/Classical
**Epistemic Stage:** Basic/Mechanistic Discovery

---

### 1. Executive Summary / SUMMARY
This theoretical statistical genetics and quantitative genomics study derives a general mathematical formulation for partitioning multi-allelic haplotype genotypic values ($g_{ij}$) at a haplotype block with $h$ alleles into $h-1$ non-redundant additive effects ($\alpha_h = (\alpha_{1h}, \dots, \alpha_{1,h-1})'$) and $h(h-1)/2$ non-redundant dominance effects ($\delta_h$), together with explicit incidence matrices ($W_{\alpha h}$ and $W_{\delta h}$) that map individual genotypes to these reduced parameter vectors under Hardy-Weinberg equilibrium (HWE). Building on this exact factorization ($g = 1\mu + W_{\alpha h}\alpha_h + W_{\delta h}\delta_h$), the authors define multi-allelic haplotype additive ($A_h$) and dominance ($D_h$) genomic relationship matrices across $b$ haplotype blocks, integrate them with single-SNP additive ($A_s$) and dominance ($D_s$) matrices into a comprehensive four-variance-component linear mixed model ($y = X\beta + g_{\alpha h} + g_{\delta h} + g_{\alpha s} + g_{\delta s} + e$), and present two algebraically equivalent estimation frameworks for GBLUP and EM/AI-GREML: Model-I (Conditional Expectation [CE], which inverts the $q \times q$ phenotypic covariance matrix $V$ and is computationally optimal when individuals $q < \text{parameters } m$) and Model-II (Mixed Model Equations [QM], which solves a system of order $c + n_\alpha + n_\delta$ without inverting singular genomic relationship matrices when $q > m$). The derivations are verified analytically and numerically on a 4-allele system (`Tables 1–2`).

### 2. STRENGTHS
- **Exact Generalization of Classical Quantitative Genetics to Multi-Allelic Haplotypes:** Whereas standard SNP-based GBLUP/GREML models treat markers as biallelic (`1` additive and `1` dominance parameter per locus), multi-SNP haplotype blocks are inherently multi-allelic ($h$ haplotypes per block). By expressing all $h$ allelic effects relative to reference allele $A_h$ ($\alpha_{ih} = \alpha_i - \alpha_h = a_i - a_h$) and all $h(h+1)/2$ dominance deviations in terms of the $h(h-1)/2$ heterozygous dominance effects $\delta_{ij} = g_{ij} - \frac{1}{2}(g_{ii} + g_{jj})$, the authors eliminate redundancy in the design matrices while preserving the exact Kempthorne/Falconer orthogonal variance partition $\sigma_g^2 = \sigma_\alpha^2 + \sigma_\delta^2$ under HWE.
- **Step-by-Step Numerical Verification (`Tables 1–2`):** Every vector, incidence matrix ($T_{\alpha h}, T_{\delta h}, K_a, K_d$), substitution effect ($\alpha_{ij}$), breeding value ($a_{ij}$), dominance deviation ($d_{ij}$), and variance component ($\sigma_g^2 = 98.9289 = \sigma_a^2 [57.6489] + \sigma_d^2 [41.2800]$) is explicitly worked out and verified on a 4-allele example, making the linear algebra transparent and auditable.
- **Computational Duality Avoiding Inversion of Singular Relationship Matrices:** Both the CE formulation (inverting $V = \sum \sigma_i^2 G_i + \sigma_e^2 I_q$, which is positive-definite as long as $\sigma_e^2 > 0$) and the revised QM mixed-model equations ($\tilde{u}_i = G_i \hat{u}_i^*$) avoid inverting singular genomic relationship matrices $G_i$ when $q > n_\alpha$ or when duplicate genotypes exist, while automatically adapting computational complexity to $\min(q, m)$.

### 3. WEAKNESSES & METHODOLOGICAL AUDIT (Methodological & Statistical Audit)
- **Strict Dependence on Hardy-Weinberg Equilibrium (HWE) and Linkage Equilibrium Across Blocks:**
  - The orthogonality of additive breeding values and dominance deviations ($\text{Cov}(a_{ij}, d_{ij}) = 0$) and the exact expressions for $\mu, a_i$, and $d_{ii}$ in Equations `(1)–(8)` rely strictly on HWE genotype frequencies ($P_{ii} = p_i^2$, $P_{ij} = 2p_i p_j$). In real breeding populations, admixed cohorts, or inbred/selected lines, departures from HWE (non-zero inbreeding coefficient $f$) and linkage disequilibrium between adjacent haplotype blocks introduce covariance between additive and dominance effects and across blocks, so $\sigma_\alpha^2 + \sigma_\delta^2$ no longer equals the total genetic variance.
- **Breakdown of Dominance Parameterization Under Rare Haplotypes and Missing Homozygotes:**
  - In a haplotype block of $k$ SNPs, there can be up to $h = 2^k$ distinct haplotypes, many of which occur at low frequency ($p_i < 0.05$). Consequently, homozygotes $A_i A_i$ ($P_{ii} = p_i^2$) and rare heterozygotes $A_i A_j$ are frequently unobserved in finite samples.
  - Because the parameterization in Equations `(4)–(6)` defines $\delta_{ij} = g_{ij} - \frac{1}{2}(g_{ii} + g_{jj})$ and $d_{ii} = -\sum_{j \ne i} 2p_j(1-p_i)\delta_{ij} + \dots$, missing homozygotes or unestimable $\delta_{ij}$ pairs cause rank deficiency in $W_{\delta h}$. While the authors briefly propose ad-hoc workarounds in Section "Rare haplotypes, missing genotypic values" (grouping rare haplotypes into a composite allele, dropping dominance from the model, or substituting mid-heterozygote values), pooling distinct rare haplotypes violates the biological rationale of haplotype modeling, and no simulation is provided to test the stability of $\hat{\sigma}_{\delta h}^2$ when $h$ is large.
- **Absence of Empirical or Simulated Data Benchmarks:**
  - Beyond the 4-allele single-locus numerical verification in Tables 1–2, the paper contains no simulation or real-data application comparing the proposed multi-allelic haplotype + SNP models (`Model-I`/`Model-II`) against standard biallelic SNP GBLUP/GREML or pseudo-SNP haplotype coding (which the authors note is deferred to companion studies).

### 4. Biological / Experimental Grounding & Claim Proportionality
- **Claim 1:** *For a haplotype block with $h$ alleles under HWE, all $h(h+1)/2$ genotypic values can be exactly factored into $h-1$ additive substitution effects and $h(h-1)/2$ heterozygous dominance effects such that $\sigma_g^2 = \sigma_\alpha^2 + \sigma_\delta^2$.* — `[Well Supported]` by exact algebraic derivation and numerical verification (Equations `1–19`, Tables `1–2`).
- **Claim 2:** *Model-I (CE) and Model-II (QM) yield identical GBLUP and GREML estimates while avoiding inversion of singular genomic relationship matrices and minimizing matrix dimension.* — `[Well Supported]` by standard linear mixed-model matrix identities (Equations `34–65`).
- **Claim 3:** *Combining haplotype additive/dominance and single-SNP additive/dominance variance components improves genomic prediction accuracy when functional regions are known.* — `[Moderately Supported]` theoretically, as empirical validation is left to future work.

### 5. Reproducibility & Data Completeness
- **Mathematical Completeness:** All equations, incidence matrix constructions (`Equations 15–19`), EM-GREML (`Equations 52–59`), and AI-GREML (`Equations 60–65`) update formulas, together with the complete 4-allele toy dataset in Tables 1–2, are self-contained and reproducible.
</Blinded Review: TIME_ANON_0558>
