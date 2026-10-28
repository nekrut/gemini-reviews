# Review of ANON_154

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **7.5 / 10.0** (Strong / Sound)  
* **Score Breakdown:** Rigor: 2.5/3.5 | Claims: 2.0/2.5 | Biology: 1.8/2.0 | Reproducibility: 1.2/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This study investigates the spatial, temporal, ecological, immunological, and genetic dynamics of Nipah virus (NiV) in its reservoir host, *Pteropus medius* bats, across Bangladesh between 2006 and 2012. The authors combine a cross-sectional survey of eight bat colonies inside and outside the human "Nipah belt" ($n = 883$ serology; $2,088$ individual bats tested by RT-PCR), a 6-year quarterly longitudinal serological and virological survey of a colony complex in Faridpur ($n = 2,789$ total captures across studies; $2,345$ microchipped bats with $56$ recaptures), satellite telemetry on 14 collared bats in Faridpur and Cox's Bazar, Bayesian generalized linear modeling (GLM) of individual serostatus predictors, generalized additive models (GAMs) and age-structured compartmental ($M\text{-}S\text{-}I\text{-}R$) differential equation models of longitudinal serodynamics, and phylogenetic analysis of partial (224-nt) and near-complete (1,720-nt) N-gene sequences. They demonstrate that NiV circulates year-round both inside and outside the Nipah belt, that juvenile seroprevalence consistently declines over the first year due to waning maternal antibodies (~17.6 weeks), that adult seroprevalence exhibits multiannual non-seasonal fluctuations (31%–82%) with direct mark-recapture evidence of adult seroreversion, that *P. medius* foraging and roosting ranges are relatively localized, and that an eastern colony (Cumilla) harbors a divergent Malaysia-clade NiV strain (~81%–83% nucleotide identity to Faridpur strains).

This is a substantial, logistically demanding field and laboratory investigation that resolves key questions regarding whether human NiV seasonality and geographic restriction in Bangladesh are driven by reservoir absence outside the Nipah belt (they are not) or by multiyear herd-immunity cycles interacting with human date-palm-sap harvesting. However, the mechanistic modeling conclusions—specifically the strong preference for density-dependent over frequency-dependent transmission ($\Delta\text{AIC} = 20.0$) and recrudescence over immigration ($\Delta\text{AIC} = 3.76$)—are over-interpreted given that an over-parameterized deterministic ODE model was fitted to only 18 quarterly seroprevalence timepoints from a single declining colony, and the printed ODE equations in the Methods contain multiple mathematical errors that violate mass conservation. In addition, Table 1 contains summation and labeling errors, and neither the underlying serological/telemetry data nor the R modeling scripts are deposited in a public repository.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **NiV circulates in *P. medius* populations throughout Bangladesh (both inside and outside the Nipah belt) and across seasons without a fixed annual cycle: [Well Supported].**  
  Cross-sectional serology confirms anti-NiV IgG across all eight sampled districts with no difference in odds of seropositivity inside vs. outside the Nipah belt ($\text{OR} = 1.2$, 95% HPDI: $0.47\text{--}3.1$), viral RNA is detected inside (Faridpur, Rajbari, Thakurgaon) and outside (Cumilla) the belt across multiple months (Feb, May, Jun, Nov, Jan, Mar), and a cyclic annual GAM fits the 6-year Faridpur adult seroprevalence series substantially worse than an acyclic spline ($\Delta\text{AIC} > 10$).

* **Juvenile serodynamics are driven by maternal antibody inheritance and loss over the first year of life, whereas adult immunity wanes over multiyear timescales: [Well Supported].**  
  Mother–pup serostatus is concordant in 39/41 seropositive dams and 32/39 seronegative dams, yearling seroprevalence declines monotonically across cohorts from June to the following spring (Fig. 3B), and mark-recapture data directly document 10 seroconversions and 9 seroreversions in free-ranging bats, with a mean interval of 588 days (range: 124–1,082 days) between positive and negative tests in adults.

* ***P. medius* exhibits localized home ranges in Bangladesh, while N-gene sequences reveal stable local genotypes in Faridpur alongside a divergent Malaysia-clade strain in eastern Bangladesh (Cumilla): [Well Supported].**  
  Satellite telemetry ($n = 14$) and mark-recapture across the 80 $\text{km}^2$ Faridpur roost complex show localized foraging radii (18.7 km and 10.8 km) and $<5\%$ home-range overlap across 310 km. Eleven 224-nt N-gene sequences from Faridpur over 6 years are identical, whereas two sequences from Cumilla share only 80.8%–82.6% identity with Faridpur strains and cluster with the Malaysian clade (supported by the 1,720-nt analysis in SI Appendix Fig. S5).

* **Local NiV transmission dynamics are governed by density-dependent transmission rather than frequency-dependent transmission, and viral maintenance is driven by recrudescence rather than immigration: [Fragile].**  
  These conclusions rest on fitting a deterministic age-structured $M\text{-}S\text{-}I\text{-}R$ ODE system to ~18 quarterly seroprevalence observations from a single colony where roost counts declined monotonically from ~300 to 185 bats. Because colony size declined secularly over the 6-year window rather than oscillating repeatedly, any secular change in transmission intensity or assay baseline is confounded with colony size $N(t)$. Moreover, the model comparison favoring recrudescence over immigration yields $\Delta\text{AIC} = 3.76$ (a log-likelihood difference of 1.88), which is weak support when observation error in roost counts, binomial overdispersion from clustered mist-netting, and multiple free transmission parameters ($\beta_{JJ}, \beta_{AJ}, \beta_{AA}, \beta_{JA}, \tau, \lambda, \Delta$) are considered. Finally, the ODE system printed in the Methods (line 49 of the Methods section) contains several algebraic errors that break population conservation.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Correct the Mathematical Errors in the Age-Structured MSIR Differential Equations
* **WHY:** The ODE system printed in the Methods (page/line 49 of the second section) contains four mathematical errors that violate mass balance and dimensional consistency:
  1. In $dR_J/dt = \gamma I_J - \mu_J S_J - \mu_J R_J - b N_A(t-52)\frac{R_J}{N_J}(1-\mu_J)^{52}$, the term $-\mu_J S_J$ subtracts susceptible juvenile mortality from the recovered juvenile compartment.
  2. In $dI_A/dt = S_A(\beta_{AA}I_A + \beta_{JA}I_J) - \gamma I_J - \mu_A I_A + \dots$, adult recovery is proportional to juvenile infecteds ($-\gamma I_J$) instead of adult infecteds ($-\gamma I_A$).
  3. In $dM_J/dt = b_A(t-5)\frac{R_A}{N_A} - \lambda M_J - \mu_J M_J - b N_A(t-52)\frac{R_A}{N_A}(1-\mu_J)^{52}\lambda^{52}$, the birth rate symbol changes from $b N_A(t-5)$ to $b_A(t-5)$, the maturation survival factor raises the rate $\lambda$ to the 52nd power ($\lambda^{52}$) instead of $(1-\lambda)^{52}$ or $e^{-52\lambda}$, and there is no corresponding maturation inflow term into $S_A$ or $R_A$.
  4. In the text immediately below the equations (line 53), $\tau$ is described as "(S to R)" instead of "(R to S)".
* **WHAT & HOW:** Audit the actual R code used to integrate the ODEs to verify whether these errors were typographical mistakes in typesetting the manuscript or bugs in the executed R script. If they were in the R script, re-run the maximum-likelihood fits and profile likelihoods with the corrected mass-conserving equations; if typographical, fix the equations in the Methods and deposit the exact R script publicly.

#### 2. Temper Claims on Recrudescence vs. Immigration and Density-Dependent Transmission
* **WHY:** A $\Delta\text{AIC}$ of $3.76$ between recrudescence and immigration in a deterministic model fitted to 18 timepoints (assuming pure binomial observation error without process noise or overdispersion) does not robustly distinguish constant per-recovered reactivation ($\Delta R_A$) from constant external force of infection. Similarly, inferring density dependence from a single colony whose size declined from 300 to 185 bats is vulnerable to ecological confounding.
* **WHAT:** Reframe the density-dependence and recrudescence findings in the Abstract and Discussion as model-generated hypotheses consistent with the Faridpur time series rather than definitive proof, and report parameter identifiability and overdispersion checks.
* **HOW:** Re-fit the competing MSIR models using a beta-binomial observation likelihood (to account for within-sampling-event clustering) and report the updated $\Delta\text{AIC}$ values, parameter correlation matrix, and profile likelihood intervals in SI Appendix Table S2.

#### 3. Address the Assay Transition and Luminex Cutoff Sensitivity in the Longitudinal Time Series
* **WHY:** The initial Faridpur timepoint (February 2006) was assayed by ELISA at Columbia University after heat inactivation, whereas subsequent 2007–2012 samples were gamma-irradiated and assayed by Luminex at AAHL using an arbitrary MFI $> 1,000$ cutoff. Including or excluding the initial high-seroprevalence 2006 point strongly influences the inferred initial condition and first decline cycle of the MSIR model.
* **WHAT:** Perform a sensitivity analysis of the GAM and MSIR model fits to the Luminex MFI cutoff and to the exclusion of the February 2006 ELISA point.
* **HOW:** Re-run the GAM and MSIR fits using alternative MFI cutoffs (e.g., $750$ and $1,250$, or a two-component log-normal mixture threshold) and excluding the February 2006 ELISA point, and verify that the three multiannual cycles and parameter estimates remain robust.

#### 4. Upgrade the Phylogenetic Reconstruction from Neighbor-Joining to Maximum Likelihood
* **WHY:** Figure 6 uses a Neighbor-Joining (NJ) distance tree with Tamura–Nei distances in Geneious, which is less rigorous than model-based Maximum Likelihood or Bayesian phylogenetic inference, especially when comparing divergent lineages (Cumilla vs. Nipah belt vs. Hendra outgroup).
* **WHAT & HOW:** Re-estimate the 224-nt and 1,720-nt N-gene trees using IQ-TREE or RAxML with formal substitution model selection and 1,000 bootstrap replicates, and report nucleotide substitution models and branch support values in Figure 6 and SI Appendix Fig. S5.

#### 5. Technical, Mathematical, and Editorial Cleanup
* **WHY:** Table 1 has arithmetic discrepancies and mislabeled columns, and data/code availability does not meet modern reproducibility standards.
* **WHAT & HOW:**
  * **Table 1 (Lines 43–75):**
    1. Two consecutive rows in the Faridpur longitudinal study (lines 59 and 60) are both labeled `Jul-08` (with 58 vs. 98 throat swabs and 74 vs. 99 urine samples). Correct the date of the second row (likely `Oct-08` or `Nov-08`).
    2. The column sum in the `Total` row (line 75) states `2,789` bats tested, `2,088` throat swabs tested, and `2,126` urine tested. However, summing the 27 rows in Table 1 yields `2,688` bats tested (a discrepancy of 101 bats) and `2,138` throat swabs tested (a discrepancy of 50 swabs). Furthermore, the main text (line 28) states "we detected NiV RNA in 11 of 2,088 individuals" and "oropharyngeal swabs, 0.15% (n = 1973)". Reconcile all denominators between the text and Table 1.
    3. Rename the column header `±95% CI` in Table 1 to `Upper 95% CI` (or report full `[Lower, Upper]` binomial confidence intervals), because `0.01 ± 0.10` and `0.005 ± 0.02` are upper bounds, not symmetric $\pm$ margins.
  * **Data and Code Deposition (Lines 60, 79):** Deposit the de-identified individual bat capture/serology table, the Faridpur longitudinal counts, the Argos telemetry coordinates, and the R scripts for the GAM and MSIR models in a permanent public repository (e.g., Zenodo, Dryad, or GitHub) rather than "available upon request."
