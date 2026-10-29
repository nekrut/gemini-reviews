# Blinded Review: SP_ANON_029
**Composite Score:** 7.9 / 10.0 (Rigor: 2.6/3.5 | Claims: 2.1/2.5 | Biology: 1.5/2.0 | Reproducibility: 1.7/2.0)
**Bias Category:** Non-Independence of Multi-Assay Studies & Right-Censoring Truncation in Fold-Change Summaries
**Verdict:** Accept (Minor Revision)
**Study Modality:** Dry-Lab Secondary Cohort/Database Re-Analysis
**Technology Maturity:** Mature/Classical
**Epistemic Stage:** Translational/Preclinical/Biomarker

---

### 1. Executive Summary
This PRISMA-compliant systematic review synthesizes *in vitro* neutralizing susceptibility data from 51 studies (comprising 58 distinct experimental assays published or preprinted through April 11, 2022) evaluating 8 clinically authorized and 6 clinical-stage anti-SARS-CoV-2 monoclonal antibodies (mAbs) and combinations against Omicron subvariants BA.1, BA.1.1, and BA.2. By compiling $\text{IC}_{50}$ values and fold-reductions relative to ancestral wild-type (WT) strains across pseudovirus and authentic live-virus assays, the authors quantify both variant-specific escape profiles (e.g., complete resistance of BA.1/BA.2 to bamlanivimab/etesevimab, restored activity of cilgavimab against BA.2 reducing tixagevimab/cilgavimab loss from 86-fold in BA.1 to 5.4-fold in BA.2, and retained activity of bebtelovimab at 1.0-fold) and substantial inter-laboratory assay variance (where ~20% of measurements deviate $>4$-fold from the mAb median).

---

### 2. Methodological & Statistical Audit
* **Right-Censoring Truncation Distortion in Fold-Change Calculations:** Across the 51 compiled studies, laboratories used different maximum antibody concentrations when testing resistant variants, reporting non-neutralizing outcomes as $>1,000\text{ ng/mL}$, $>5,000\text{ ng/mL}$, or $>10,000\text{ ng/mL}$. In the Methods ("Data extraction and analysis"), the authors state that both $>1,000\text{ ng/mL}$ and $>10,000\text{ ng/mL}$ were recoded as a flat $10,000\text{ ng/mL}$ to compute fold-reductions and geometric/non-parametric medians. While pragmatic, this ceiling imputation introduces an artificial dependency between a study's wild-type $\text{IC}_{50}$ and its maximum achievable fold-reduction: an assay with a high WT $\text{IC}_{50}$ of $50\text{ ng/mL}$ capped at $10,000\text{ ng/mL}$ is truncated at a 200-fold reduction, whereas an assay with a WT $\text{IC}_{50}$ of $2\text{ ng/mL}$ reaches a 5,000-fold reduction for the exact same complete loss of activity.
* **Pooling Non-Independent Assays in Non-Parametric Tests:** Seven included studies performed two parallel assays (e.g., pseudovirus and authentic virus, or two target cell lines), and several studies shared underlying experimental datasets (e.g., Westendorf21, FDA22, and Zhou21 for bebtelovimab). Treating all 58 assay-level observations as statistically independent in Wilcoxon rank-sum tests and IQR calculations mildly underestimates variance, though a mixed-effects sensitivity check on log-transformed uncensored values would easily address this.
* **Minor Text and Figure Caption Cross-Reference Errors:**
  1. In the Figure 4 caption, the text states *"Each of the IC50s of the control virus is connected by a line to the IC50s of the Omicron BA.1 variant"*, whereas Figure 4 exclusively plots the **Omicron BA.2** variant (Figure 3 plotted BA.1).
  2. On line 125 of the Results ("Clinical-stage mAbs"), the text cites *"Fig. 4J, L to R"* for regdanvimab and clinical-stage mAbs, whereas panel 4J is CIL/TIX and regdanvimab starts at panel 4K (*"Fig. 4K to R"*).

---

### 3. Biological / Experimental Grounding & Claim Proportionality
* **Claim:** *Substantial inter-assay variability (~20% of $\text{IC}_{50}$s and fold-reductions deviating $>4$-fold from the median, and 2.6-fold higher WT $\text{IC}_{50}$s in authentic vs. pseudovirus assays) necessitates aggregating multiple independent studies rather than relying on single-lab preprints to guide clinical mAb policy.* **[Well Supported]** — The systematic comparison across 58 assays (Table 2, Figures 2–4) provides an essential quantitative benchmark of assay noise in viral neutralization testing.
* **Claim:** *Bebtelovimab and cilgavimab/tixagevimab retain potent in vitro activity against BA.2 relative to achievable serum concentrations ($C_{\max}$), whereas sotrovimab suffers a median 17-fold reduction against BA.2.* **[Well Supported]** — Contextualizing median *in vitro* $\text{IC}_{50}$s against clinical pharmacokinetic parameters (Table 1) grounds the virological data in realistic clinical dosing regimes.

---

### 4. Reproducibility & Data Completeness
* **Open Database and Curation Pipeline:** Exemplary data transparency. Every extracted $\text{IC}_{50}$ value, viral construct detail, cell line, assay readout, and analysis script is publicly available in the Stanford Coronavirus Antiviral & Resistance Database (CoV-RDB) GitHub repository (`[GITHUB_REPO_REDACTED]`) and Supplementary Data tables.
