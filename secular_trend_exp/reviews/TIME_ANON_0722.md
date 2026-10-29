<Blinded Review: TIME_ANON_0722>
**Composite Score:** 6.3 / 10.0 (Rigor: 1.8/3.5 | Claims: 1.7/2.5 | Biology: 1.5/2.0 | Reproducibility: 1.3/2.0)
**Scientific Core Score:** 5.0 / 8.0
**Bias Category:** Statistical/Design
**Verdict:** Major Revision
**Study Modality:** Wet-Lab Primary Experimental
**Technology Maturity:** Mature/Classical
**Epistemic Stage:** Translational/Preclinical/Biomarker

OVERALL_SCORE: 6.3/10
VERDICT: CAVEATS
ESTIMATED_DECADE: 2020s

---

### 1. Executive Summary (SUMMARY)
This study evaluates the in vitro virucidal efficacy of 11 chemical disinfectants (ethanol, 2-propanol, sodium hypochlorite, acetic acid, hydrogen peroxide, caustic soda, phenol, potassium peroxymonosulfate, glutaraldehyde, formaldehyde, and benzalkonium chloride), each tested at three concentrations across three replicates ($n = 3$), against porcine transmissible gastroenteritis virus (TGEV, ATCC VR-1740) and porcine respiratory coronavirus (PRCV, ATCC VR-3379) in swine testis (ST) cells. The authors follow a quantitative suspension assay adapted from European Standard EN 14675 (30 min exposure at $10 \pm 1^\circ\text{C}$) under both low-level soiling ($3.0\text{ g/L}$ BSA) and high-level soiling ($10\text{ g/L}$ BSA $+ 10\text{ g/L}$ yeast extract) conditions, using a $\ge 4\ \log_{10}\text{TCID}_{50}/\text{mL}$ titer reduction threshold to define virucidal efficacy. They report that caustic soda ($1\%$–$3\%$), potassium peroxymonosulfate ($0.5\%$–$2\%$), and $80\%$ ethanol achieved $\ge 4\ \log_{10}$ reductions against both viruses under both soiling regimes, whereas sodium hypochlorite lost activity under high organic load and aldehydes/benzalkonium chloride could not be evaluated over a $4\ \log_{10}$ dynamic range due to persistent ST cell cytotoxicity even after Microspin S-400 HR gel filtration.

While the empirical screening dataset addresses a practical biosecurity gap in swine veterinary medicine, the manuscript suffers from multiple internal numerical inconsistencies in reported reagent concentrations, an physically impossible trypsin concentration in the Methods, an unexplained inverse dose-response anomaly for potassium peroxymonosulfate against PRCV, and improper application of parametric two-way ANOVA to right-censored (cytotoxicity-limited) and zero-variance boundary titers.

### 2. Methodological & Statistical Audit (STRENGTHS & WEAKNESSES & METHODOLOGICAL AUDIT)

#### Strengths
* **Standardized assay framework:** Testing across both clean ($3\text{ g/L}$ BSA) and dirty ($10\text{ g/L}$ BSA $+ 10\text{ g/L}$ yeast extract) interfering conditions at $10^\circ\text{C}$ for 30 min adheres to the veterinary virucidal suspension standard EN 14675 and demonstrates the marked organic-load quenching of sodium hypochlorite.
* **Explicit reporting of cytotoxicity limits:** The authors document the cytotoxicity of glutaraldehyde, formaldehyde, and benzalkonium chloride and evaluate viral titer loss across Microspin S-400 HR spin columns (Fig. 2).

#### Weaknesses & Methodological Audit
* **Statistical testing on right-censored cytotoxicity limits and zero-variance cells:** For glutaraldehyde, formaldehyde, and benzalkonium chloride, the reported reductions in Tables 1 and 2 (marked with `*`) are not measured residual viral reductions; they represent the lower limit of detection imposed by persistent cytotoxicity in lower dilution wells. In the Results (line 169; Fig. 5 and Fig. 6), the authors include these censored bounds in their two-way ANOVA + Tukey post-hoc tests, claiming statistically significant differences in virucidal activity for $0.5\%$ and $1\%$ glutaraldehyde ($p < 0.05$) between TGEV and PRCV, and for $0.5\%$ formaldehyde ($p < 0.01$) between low and high soiling. Furthermore, in Table 1 (`Glutaraldehyde C`), $0.1\%$ glutaraldehyde shows a higher apparent reduction ($3.5 \pm 0.50^*$) than $1\%$ and $0.5\%$ ($2.5 \pm 0.50^*$) purely because the $0.1\%$ solution was 10-fold less cytotoxic to the ST monolayer. Treating assay censoring limits as observed viral reductions invalidates those ANOVA comparisons. Additionally, numerous cells in Table 2 have $\text{SD} = 0.00$ across all three replicates because all wells reached the assay floor/ceiling, violating ANOVA homoscedasticity assumptions.
* **Unexplained inverse dose-response for potassium peroxymonosulfate:** In Table 2 (PRCV), potassium peroxymonosulfate at $2\%$ and $1\%$ yields reductions of $4.33 \pm 0.29$ (low soiling) and $4.00 \pm 0.00$ (high soiling), whereas the lowest concentration ($0.5\%$) yields a $1.0\ \log_{10}$ *greater* reduction of $5.33 \pm 0.29$ (low soiling) and $5.00 \pm 0.00$ (high soiling). Similarly, for PRCV treated with phenol (Table 2), $1.5\%$ phenol yields a $3.00 \pm 0.50$ reduction while $2\%$ phenol drops to $1.00 \pm 0.50$. Neither anomaly is explained (e.g., whether different control virus stock batches with different starting $\text{TCID}_{50}$ titers were used for those runs).
* **Internal inconsistencies in tested concentrations and omissions:**
  * *Formaldehyde:* Materials and Methods (line 26) states concentrations of `0.5%, 0.25% and 0,125%`; the Abstract and Tables 1–2 report `0.5%, 0.275%, 0.125%`; and the Results text (lines 104 and 152) states `0.5%, 0.275%, 1.125%`.
  * *2-propanol:* Materials and Methods (line 26) and Tables 1–2 list `80%, 60% and 40%`, whereas Results line 62 states `90%, 60% and 40%`. Moreover, 2-propanol is completely omitted from the Abstract despite being one of the 11 tested compounds.
  * *Phenol:* Materials and Methods (line 26) lists `1%, 1%, 5% and 2% phenol` (a typographical mangling of `1%, 1.5% and 2%`).
  * *Trypsin concentration:* Virus stock preparation (line 36) states `5 ml of virus growth medium supplemented with 1 g/ml trypsin was added`, which is $10^6$-fold too concentrated (likely intended as $1\ \mu\text{g/mL}$, cf. line 41).

### 3. Biological / Experimental Grounding & Claim Proportionality
* **Caustic soda ($1\%$–$3\%$), potassium peroxymonosulfate ($0.5\%$–$2\%$), and $80\%$ ethanol achieve $\ge 4\ \log_{10}$ inactivation of TGEV and PRCV under low and high soiling:** `[Well Supported]` — Directly supported by suspension titration across all replicates exceeding the EN 14675 $4\ \log_{10}$ threshold.
* **Organic matter markedly reduces the virucidal activity of sodium hypochlorite against TGEV and PRCV:** `[Well Supported]` — Reduction drops from $4.67 \pm 0.29$ to $0.50$–$3.67\ \log_{10}$ for TGEV and from $3.67 \pm 0.29$ to $1.00$–$2.33\ \log_{10}$ for PRCV under high soiling, consistent with oxidative quenching of free chlorine by BSA and yeast extract.
* **Statistically significant differences in virucidal efficacy between TGEV and PRCV or between soiling levels for glutaraldehyde and formaldehyde:** `[Methodologically Flawed]` — Derived from applying two-way ANOVA to right-censored cytotoxicity detection limits (`*`) rather than true viral inactivation endpoints.

### 4. Reproducibility & Data Completeness
Cell line (`ATCC CRL-1746`), viral strains (`ATCC VR-3379` and `VR-1740`), chemical suppliers, CAS numbers, and EN 14675 incubation parameters are clearly specified. However, baseline control viral titers ($\log_{10}\text{TCID}_{50}/\text{mL}$ before subtraction) are not tabulated in Tables 1 and 2, making it impossible to verify whether ceiling effects ($4.20$ vs $4.67$ vs $5.33\ \log_{10}$ maximum reductions) were driven by variations in the starting control virus titer across assay batches. The multiple typographical errors in chemical concentrations (`0.25%` vs `0.275%` vs `1.125%` formaldehyde; `80%` vs `90%` 2-propanol; `1 g/ml` trypsin) require correction.
</Blinded Review: TIME_ANON_0722>
