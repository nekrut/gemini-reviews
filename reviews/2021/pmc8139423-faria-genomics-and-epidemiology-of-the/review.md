# Review of PMC8139423 (PMID:33853970)

**Manuscript Title:** Genomics and epidemiology of the P.1 SARS-CoV-2 lineage in Manaus, Brazil  
**Authors:** Faria NR, Mellan TA, Whittaker C, Claro IM, Candido DDS, Mishra S, Crispim MAE, Sales FCS, Hawryluk I, McCrone JT, Hulswit RJG, Franco LAM, Ramundo MS, de Jesus JG, Andrade PS, Coletti TM, Ferreira GM, Silva CAM, Manuli ER, Pereira RHM, Peixoto PS, Kraemer MUG, Gaburo N, Camilo CDC, Hoeltgebaum H, Souza WM, Rocha EC, de Souza LM, de Pinho MC, Araujo LJT, Malta FSV, de Lima AB, Silva JDP, Zauli DAG, Ferreira ACS, Schnekenberg RP, Laydon DJ, Walker PGT, Schlüter HM, Dos Santos ALP, Vidal MS, Del Caro VS, Filho RMF, Dos Santos HM, Aguiar RS, Proença-Modena JL, Nelson B, Hay JA, Monod M, Miscouridou X, Coupland H, Sonabend R, Vollmer M, Gandy A, Prete CA, Nascimento VH, Suchard MA, Bowden TA, Pond SLK, Wu CH, Ratmann O, Ferguson NM, Dye C, Loman NJ, Lemey P, Rambaut A, Fraiji NA, Carvalho MDPSS, Pybus OG, Flaxman S, Bhatt S, Sabino EC.  
**Journal / Preprint:** *Science* (2021; `PMC8139423` / `PMID:33853970` / `10.1126/science.abh2644`)  
**Calibration Study Cohort:** Cohort B — Validated Control (`B12` | Double-Blinded as `ANON_32`)  
**Overall Score:** **8.3 / 10.0** (Strong / Sound)  
* **Score Breakdown:** Rigor: 2.9/3.5 | Claims: 2.0/2.5 | Biology: 1.8/2.0 | Reproducibility: 1.6/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript characterizes the emergence, molecular evolution, and epidemiological dynamics of SARS-CoV-2 lineage P.1 during the late-2020 COVID-19 resurgence in Manaus, Brazil. Combining 184 newly sequenced viral genomes from Manaus (November–December 2020) with 962 background Brazilian genomes, SIVEP-Gripe severe acute respiratory infection (SARI) hospitalization and mortality records, ANAC air-travel data, and RT-PCR cycle threshold (Ct) series ($n = 942$), the authors identify P.1 as a monophyletic descendant of B.1.1.28 carrying 17 non-synonymous/indel lineage-defining changes (including Spike K417T, E484K, and N501Y). A local molecular clock model estimates the P.1 tMRCA at November 15, 2020 (95% BCI: October 6 – November 24, 2020) with an accelerated evolutionary rate along its stem branch ($\text{BF} = 6.04$). Fitting a two-category Bayesian semi-mechanistic renewal model to daily mortality and genomic lineage frequencies, the authors estimate that P.1 is 1.7- to 2.4-fold more transmissible (50% BCI; median 2.0) and evades 21 to 46% of prior non-P.1 infection immunity (50% BCI; median 32%). Sequence accessions, Ct data files, and sensitivity tables are provided.

The study integrates genomic surveillance, phylogenetic dating, clinical RT-PCR confounding controls, and dynamical modeling to address why a severe second epidemic wave occurred in a population with high first-wave attack rates. Notably, the authors properly test and report that the apparent association between P.1 infection and lower Ct values disappears once symptom-to-sampling delay is controlled for ($P = 0.15$ and $P = 0.12$), and they explicitly display the joint-posterior collinearity between transmissibility and immune evasion (Figure 4A). The primary limitations are: (1) reporting 50% Bayesian credible intervals in the Abstract without labeling them as 50% intervals (where readers assume 95% intervals by convention); (2) attributing mortality dynamics in the transmission model without separating intrinsic P.1 virulence from acute healthcare system collapse in Manaus; and (3) including low-coverage partial genomes (25–75% coverage) in lineage frequency fits without reporting coverage-stratified sensitivity checks.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Lineage P.1 emerged in or near Manaus around mid-November 2020 (median November 15; 95% BCI October 6 – November 24, 2020) following accelerated stem-branch evolution: [Well Supported].**  
  The monophyly of P.1 (posterior probability = 1.00) nested within Manaus B.1.1.28 isolates, the root-to-tip vertical offset (Figure S8), and the local clock Bayes factor ($\text{BF} = 6.04$) provide consistent support for rapid stem-branch accumulation of 17 amino acid mutations prior to epidemic expansion.

* **Eight of the 10 lineage-defining Spike mutations in P.1 (including K417T, E484K, and N501Y) reflect diversifying positive selection and convergent adaptation: [Well Supported].**  
  Independent emergence of K417T/N, E484K, and N501Y across geographically distinct lineages (B.1.351, B.1.1.7) alongside site-level codon selection analyses (Table S1, Figure S14) and established biophysical data on hACE2 binding and antibody neutralization strongly support adaptive convergence.

* **P.1 is 1.7- to 2.4-fold more transmissible and evades 21 to 46% of protective immunity from prior non-P.1 infection: [Moderately Supported].**  
  The two-category renewal model demonstrates that natural waning of immunity alone cannot jointly explain the rapid replacement of non-P.1 lineages (from 0% to 87% in ~7 weeks) and the magnitude of the second mortality wave across sensitivity analyses (Tables S5–S10). However, transmissibility and cross-immunity are only weakly identifiable separately from aggregate mortality and lineage proportions, forming a banana-shaped ridge in the joint posterior (Figure 4A). Furthermore, presenting the 50% BCIs (`1.7 to 2.4` and `54 to 79%` cross-immunity) in the Abstract without specifying that they are 50% (rather than 95%) credible intervals overstates the precision of the point estimates.

* **Infections after P.1 emergence carry a 1.2- to 1.9-fold (50% BCI) higher risk of mortality: [Fragile].**  
  As the authors note in the text (Section "Mathematical modeling of lineage P.1 epidemiological characteristics"), the January 2021 wave overwhelmed hospital capacity and oxygen supplies in Manaus. Because the Bayesian model uses SIVEP-Gripe SARI deaths to infer underlying infection incidence and infection fatality ratios under homogeneous mixing, transient spikes in hospital fatality rates due to healthcare collapse cannot be cleanly separated from intrinsic viral severity or reinfection susceptibility.

* **Lower RT-PCR Ct values in P.1 samples reflect epidemic growth phase confounding rather than proven higher peak viral load: [Well Supported].**  
  The authors' decision to re-test the unadjusted Ct reduction (1.43 cycles for E gene, $P = 0.029$; 1.91 cycles for N gene, $P = 0.01$; $n = 128\text{–}129$) while controlling for days from symptom onset to swab collection ($P = 0.15$ and $P = 0.12$; $n = 42$) is a sound control for epidemic-phase ascertainment bias.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Explicitly Label 50% Credible Intervals in the Abstract and Report Full 95% BCIs in the Main Text
* **WHY:** In the Abstract, reporting *"we estimate that P.1 may be 1.7- to 2.4-fold more transmissible and that previous (non-P.1) infection provides 54 to 79% of the protection"* without qualification leads readers to interpret these ranges as 95% credible intervals, whereas the main text reveals they are 50% BCIs (interquartile ranges).
* **WHAT:** Specify "50% Bayesian credible interval" directly in the Abstract and report the corresponding 95% BCIs alongside the 50% BCIs in the main text (lines 66 and 74).
* **HOW:** Extract the 2.5th and 97.5th percentiles of the marginal posteriors for relative transmissibility, cross-immunity, and relative mortality risk from the MCMC chains plotted in Figure 4A–B and insert them into the text and Abstract.

#### 2. Decouple Healthcare Strain from Intrinsic Mortality Risk in the Dynamical Model
* **WHY:** If the infection fatality rate (IFR) rose transiently in late December 2020 and January 2021 due to hospital and oxygen shortages in Manaus, assuming a constant baseline IFR for non-P.1 lineages forces the model to attribute excess deaths either to higher P.1 infection volume (inflating immune evasion/transmissibility) or higher P.1 intrinsic lethality.
* **WHAT:** Add a sensitivity analysis allowing a time-varying hazard multiplier on in-hospital SARI mortality shared across both P.1 and non-P.1 infections during peak hospital occupancy.
* **HOW:** Parameterize a piecewise or occupancy-indexed IFR scaling factor using the Manaus SARI hospitalization vs. death ratio from SIVEP-Gripe (Figure 1A), re-fit the Bayesian model, and report the resulting joint posterior for P.1 transmissibility and cross-immunity.

#### 3. Sensitivity Check on Partial Genomes (25–75% Coverage) in Lineage Proportions
* **WHY:** Of the 184 Manaus sequences generated, 41 had only 25–75% genome coverage (and 182 vs. 184 total genomes are cited across paragraphs on line 19 and line 27). Amplicon dropout in low-viral-load samples could differentially affect lineage assignment accuracy between P.1 and ancestral B.1.1.28 strains.
* **WHAT:** Verify that the logistic growth trajectory of P.1 frequency (Figure 3A, Table S4) is invariant to excluding partial genomes (<75% coverage).
* **HOW:** Re-fit the binomial logistic regression in Figure 3A restricting to the $n = 143$ near-complete and complete genomes ($\ge 75\%$ coverage), compare the inferred growth rate and emergence timing, and reconcile the $n = 184$ vs. $n = 182$ sequence count discrepancy in the text.

#### 4. Editorial Cross-Reference Fix in Figure 3
* **WHY:** Line 49 states that the logistic function fit in Figure 3A is *"quantifying the trend shown in Fig. 1C"*, whereas Figure 1C shows ANAC air travel passenger volume and Figure 1D shows the temporal lineage counts in Manaus.
* **WHAT & HOW:** Change `Fig. 1C` to `Fig. 1D` on line 49, and update the Figure 3B–C caption (line 55) so that panel B (time-period stratified Ct values for $n = 942$) and panel C (lineage-sequenced subsample Ct values) match their order of citation in the text (lines 49 and 57, which currently invert panels B and C).
