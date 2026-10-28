# Blinded Review: SP_ANON_073
**Composite Score:** 7.8 / 10.0 (Rigor: 2.8/3.5 | Claims: 2.0/2.5 | Biology: 1.6/2.0 | Reproducibility: 1.4/2.0)
**Bias Category:** None (Methodologically Sound)
**Verdict:** Accept
**Study Modality:** Dry-Lab Theory/Methods/Simulation
**Technology Maturity:** Mature/Classical
**Epistemic Stage:** Basic/Mechanistic Discovery

## 1. Executive Summary
This brief correspondence ("Reply" / "Matters Arising") critiques a competing computational simulation model by Rosenbloom et al., who argued that the authors' previously reported temporal phylogenetic signal of ongoing HIV-1 replication in lymphoid tissue sanctuaries during suppressive combination antiretroviral therapy (cART) could be an artifact of pre-therapy positive selection coupled with the differential decay of latently infected cell cohorts after therapy initiation.

In a concise, population-genetically grounded rebuttal, the authors demonstrate that Rosenbloom et al.'s simulation produces a high false-positive rate (57%) only by assuming biologically implausible parameter regimes: (1) assigning a massive positive selection coefficient ($s = 0.2$ per beneficial mutation across 3% of the genome, nearly two orders of magnitude above empirical HIV-1 estimates of $s \approx 0.005$ genome-wide and $s \approx 0.03$ for strong CTL escape); (2) generating star-like/rake-like trees with mean internal branch lengths of ~1 substitution (3- to 5-fold lower than empirical intra-host HIV-1 phylogenies); (3) under-sampling sequences per timepoint ($n = 50$ vs. deep sequencing depth); and (4) yielding a testable counterfactual prediction—that longitudinal viral DNA during cART should evolve "backwards" toward early pre-therapy plasma RNA variants as short-lived, late-infected cell cohorts decay—which is directly contradicted by independent clinical studies showing that persistent DNA sequences cluster with late pre-therapy plasma variants.

Within the constraints of a short correspondence format, the authors' critique of the competing simulation's parameter realism and topological predictions is rigorous and convincing. However, as a brief reply containing no new primary data or simulation code of its own, it addresses only the artificiality of Rosenbloom et al.'s latent-decay model and does not independently resolve other methodological critiques of the original study (such as the short 6-month post-cART sampling window or potential deep-sequencing PCR error/compartmentalization confounders).

## 2. Methodological & Statistical Audit

### 2.1 Audit of Selection Coefficient Realism ($s = 0.2$ vs. Empirical HIV-1 Estimates)
- The central quantitative pillar of the rebuttal is the audit of Rosenbloom et al.'s parameterization of pre-therapy positive selection. In Rosenbloom et al.'s model, generating rapid turnover of viral lineages immediately prior to cART requires a beneficial selection coefficient of $s = 0.2$ across 3% of sites—meaning two simultaneous mutations confer a $(1 + 0.2)^2 = 1.44$ (44%) replicative fitness advantage per generation, and five mutations confer a $(1.2)^5 \approx 2.49$-fold advantage.
- The authors appropriately contrast this against empirical population-genetic measurements in HIV-1: during primary infection, strong cytotoxic T-lymphocyte (CTL) escape mutations exhibit mean selection coefficients around $s \approx 0.03$, falling to $s \approx 0.005$ across the viral genome during chronic infection.
- Crucially, the authors note that when Rosenbloom et al. lowered their selection parameter in sensitivity analyses to a more realistic regime ($s = 0.02$), the false-positive rate for detecting ongoing replication dropped nearly 3-fold, from 57% to 21%.

### 2.2 Topological Diagnostics: Internal Branch Lengths and "Backwards" vs. "Forward" Divergence
- The authors identify two diagnostic discrepancies between the latent-decay simulation and empirical HIV-1 data:
  1. **Tree Topology and Internal Branch Lengths:** Under extreme selective sweeps ($s = 0.2$), Rosenbloom et al.'s simulated phylogenies collapse into "rake-like" star topologies with an average internal branch length of just 1 nucleotide substitution, whereas the authors' empirical longitudinal datasets exhibit internal branch lengths 3- to 5-fold longer.
  2. **Directional Prediction of Latent Pool Decay:** If short-lived cells infected just before cART initiation carry the most evolved variants and decay rapidly upon cART initiation, while long-lived memory cells archived earlier in infection persist, the surviving proviral DNA pool sampled at 3–6 months post-cART must shift genetically *backward* toward early acute-phase plasma RNA sequences. The authors point out both that their Bayesian skyride coalescent analysis explicitly tested the directionality of sequence evolution (rejecting backward drift in favor of forward divergence) and that external longitudinal studies (e.g., Brodin et al.) confirm that long-term on-therapy DNA sequences closely match late pre-therapy plasma variants rather than early acute variants.

### 2.3 Scope Limitations Inherent to the Correspondence Format
- While the manuscript successfully shows that Rosenbloom et al.'s specific latent-cohort decay model requires unrealistic evolutionary parameters to mimic ongoing evolution, showing that *one* proposed null artifact model is poorly parameterized does not by itself prove that ongoing low-level replication occurs during suppressive cART. Other potential artifacts in 6-month longitudinal deep-sequencing studies—such as template resampling, PCR recombination/error inflation in 454 reads, and anatomical sampling variance across lymph node biopsies—remain outside the scope of this short reply.

## 3. Biological / Experimental Grounding & Claim Proportionality

### Claim Audit Summary
- **Claim 1:** *"Rosenbloom et al.'s main argument depends upon a single parameter—the mutational fitness effect ($s$)—taking an unrealistically high value ($s = 0.2$, whereas measured averages are between $s = 0.005$ and $s = 0.03$)."* — **[Well Supported]**: Directly verified from the parameterization of Rosenbloom et al.'s model and established empirical estimates of within-host HIV-1 selection coefficients.
- **Claim 2:** *"In fact, a sensitivity analysis given in the critique shows that when $s$ is lowered to a realistic range ($s = 0.02$), the rate of false positives drops threefold, from 57% to 21%."* — **[Well Supported]**: Accurately cites the sensitivity behavior of the competing simulation.
- **Claim 3:** *"Rosenbloom et al.'s model makes an important prediction: sequences sampled after the start of cART should become more similar to sequences sampled early in infection, before cART... This pattern is inconsistent with empirical observations."* — **[Well Supported]**: A sharp, falsifiable deduction from the differential decay hypothesis that aligns with independent longitudinal reservoir studies.

## 4. Reproducibility & Data Completeness
- Because this manuscript is a 65-line theoretical/methodological Reply to a published comment rather than a primary research article, it introduces no new datasets or custom software pipelines, and relies entirely on analytical audit of parameters and figures published in the exchange. All cited quantitative values ($s = 0.2$, $s = 0.02$, 57% vs. 21% FPR, 50 sequences per timepoint) are transparently stated and verifiable.
