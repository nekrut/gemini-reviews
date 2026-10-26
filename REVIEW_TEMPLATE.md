# Scientific Peer Review Template & Diagnostic Guide

This guide provides a standardized, fast-turnaround peer review protocol, 1–10 quantitative scoring rubric, and Markdown template for quantitative biology, evolutionary genomics, statistical modeling, bioinformatics, and epidemiology manuscripts.

The goal is to produce **human-scale, direct, technically rigorous reviews** that avoid filler while auditing methodology, mathematical and statistical validity, biological plausibility, and reproducibility.

---

## PART 1: THE 7-PILLAR RAPID AUDIT CHECKLIST

Before writing, audit the manuscript against these seven diagnostic pillars:

1. **Scope, Framing & Causal Claims:** Do the title and abstract claim causal drivers, mechanistic proof, or broad generality when the analysis only performs descriptive clustering, observational correlation, or a narrow case study?
2. **Data Provenance, Sampling Bias & Leakage:** Are there ascertainment biases, temporal/spatial skew, unacknowledged filtering rules, contamination/sequencing artifacts, lookahead bias, or post-hoc circularity (selecting hypotheses or thresholds after inspecting the data)?
3. **Model Specification & Internal Consistency:** Do the mathematical, statistical, or evolutionary models match the data-generating process? Are core assumptions (conditional independence, stationarity, panmixia, parameter identifiability, prior vs. likelihood separation) violated or mutually contradictory across sections?
4. **Statistical Support, Power & Uncertainty Propagation:** Are $p$-values, Bayes factors, confidence/credible intervals, or model selection criteria (AIC/BIC) properly calibrated? Is uncertainty propagated across all stages of multi-step pipelines? Do the authors conflate failing to reject a null hypothesis (due to low power or small sample size) with evidence for the null?
5. **Baselines, Controls & Symmetric Hypothesis Testing:** Are competing models or hypotheses evaluated under symmetric constraints, matched sample sizes, and realistic null simulations? Do Tables and Supplements actually support the model chosen in the main text?
6. **Biological & Physical Plausibility:** Do inferred rates, effect sizes, and mechanistic narratives respect known biophysical, molecular, evolutionary, or epidemiological constraints?
7. **Reproducibility & Technical Sanity Checks:** Are raw data and executable code publicly available? Audit equations, check that numbers in the main text match tables and supplementary text, and scan for broken figure/table cross-references, mislabeled axes, and truncated or inaccurate citations.

---

## PART 2: PROSE & STYLE RULES (ANTI-LLM TROPE MANDATE)

* **Direct and proportional:** Keep total length proportional to the manuscript's substance. State strengths and flaws plainly without theatrical adjectives (*"groundbreaking," "tour de force," "pivotal," "crucial," "compelling"*).
* **No LLM filler or syntactic cliches:** Avoid *"delve into," "tapestry," "landscape," "it is worth noting," "importantly," "not only... but also," "serves as a testament,"* and formulaic compliment sandwiches.
* **Concrete and verifiable:** Anchor every critique to specific sections, equations, tables, figures, or parameter values in the manuscript.

---

## PART 3: THE 1–10 QUANTITATIVE SCORING RUBRIC

Every reviewed manuscript receives an **Overall Score (1.0 – 10.0)** computed as the sum of four diagnostic sub-scores mapped to the 7 Pillars:

1. **Methodological & Statistical Rigor (0.0 – 3.5 pts | Pillars 3, 4, 5):** Model specification, internal consistency, calibration of $p$-values/Bayes factors/AIC, uncertainty propagation across multi-step pipelines, and symmetric baseline/null controls.
2. **Claim-to-Evidence Alignment (0.0 – 2.5 pts | Pillars 1, 5):** Correspondence between title/abstract/discussion claims and what was formally tested; proportion of core claims that are *Well Supported* vs. *Fragile/Overstated/Methodologically Flawed*.
3. **Data Integrity & Biological Plausibility (0.0 – 2.0 pts | Pillars 2, 6):** Data provenance, handling of ascertainment/sampling skew, absence of leakage or post-hoc circularity, contamination controls, and adherence to biophysical, molecular, and epidemiological constraints.
4. **Reproducibility & Technical Execution (0.0 – 2.0 pts | Pillar 7):** Public availability of raw data and executable code, mathematical accuracy of equations, numerical consistency between main text and tables/supplements, and clean figures/references.

### Calibration Tiers
| Score | Tier | Diagnostic Interpretation |
| :---: | :--- | :--- |
| **9.0 – 10.0** | **Exemplary** | Sound model specification, calibrated uncertainty, symmetric controls, open data/code, and claims strictly bounded by statistical support. |
| **7.0 – 8.9** | **Strong / Sound** | Solid methodological and empirical contribution; minor modeling caveats, unpropagated intermediate uncertainty, or secondary framing overreach. |
| **5.0 – 6.9** | **Mixed / Salvageable** | Useful dataset or core method, but undermined by 1–2 major pillar violations (e.g., circular conditioning, uncalibrated tests, or missing baselines) requiring re-analysis. |
| **3.0 – 4.9** | **Flawed / Overstated** | Core conclusions rest on statistical artifacts, severe ascertainment/contamination bias, or biologically implausible assumptions. |
| **1.0 – 2.9** | **Fundamentally Invalid** | Pervasive technical failures, unaddressed leakage/contamination, or claims directly contradicted by the manuscript's own tables. |

---

## PART 4: THE 3-SECTION CONCISE REVIEW TEMPLATE

```markdown
# Review of [MANUSCRIPT_ID]

**Manuscript Title:** [INSERT FULL MANUSCRIPT TITLE]  
**Authors:** [INSERT AUTHOR LIST]  
**Journal / Preprint:** [INSERT JOURNAL OR PREPRINT ID]  
**Overall Score:** **[X.X] / 10.0** ([Tier Name])  
* **Score Breakdown:** Rigor: [X.X]/3.5 | Claims: [X.X]/2.5 | Biology: [X.X]/2.0 | Reproducibility: [X.X]/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

[Paragraph 1: Concise summary of what was done. State the core scientific question, dataset size and provenance, mathematical/computational methods, and main quantitative findings. Note the availability of raw data and reproducible code.]

[Paragraph 2: Clear bottom-line evaluation. Acknowledge solid empirical or methodological contributions, then state the primary statistical, modeling, or biological limitations that affect the main conclusions. Conclude with a practical assessment of what is required to resolve them (e.g., whether issues can be addressed through computational re-analysis, formal uncertainty propagation, and reframing without new data generation).]

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **[Key Claim 1]: [Well Supported / Moderately Supported / Fragile / Overstated / Methodologically Flawed].**  
  [Briefly explain why: cite the specific evidence, model assumptions, sensitivity analyses, or mathematical/biological caveats.]

* **[Key Claim 2]: [Well Supported / Moderately Supported / Fragile / Overstated / Methodologically Flawed].**  
  [Briefly explain why: e.g., consistency across datasets/methods, or sensitivity to sampling bias, unmodeled confounders, or low statistical power.]

* **[Key Claim 3]: [Well Supported / Moderately Supported / Fragile / Overstated / Methodologically Flawed].**  
  [Briefly explain why: e.g., asymmetric hypothesis testing, unpropagated uncertainty, circular conditioning, or conflict with supplementary tables.]

* **[Key Claim 4]: [Well Supported / Moderately Supported / Fragile / Overstated / Methodologically Flawed].**  
  [Briefly explain why: e.g., biological plausibility, missing baseline comparisons, or contradiction between sections.]

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. [Actionable Improvement 1 — e.g., Correct Model Specification or Conditioning]
* **WHY:** [Why the current formulation, assumption, or test is statistically or biologically flawed.]
* **WHAT:** [What specific change is needed in the analysis, claims, or figures.]
* **HOW:** [Exact, doable implementation step using the authors' existing data and codebase.]

#### 2. [Actionable Improvement 2 — e.g., Propagate Uncertainty or Calibrate Power/FPR]
* **WHY:** [Why treating intermediate estimates as exact or relying on underpowered tests distorts the conclusion.]
* **WHAT:** [What sensitivity analysis, null simulation, or variance propagation should be added.]
* **HOW:** [Concrete procedure to compute and report the updated intervals, Bayes factors, or $p$-values.]

#### 3. [Actionable Improvement 3 — e.g., Control for Sampling Bias or Confounders]
* **WHY:** [How ascertainment, filtering, or sample-size mismatch biases the current result.]
* **WHAT:** [What subsampling, stratification, or baseline comparison is needed.]
* **HOW:** [Step-by-step description of how to run the control and update the relevant figure/table.]

#### 4. [Actionable Improvement 4 — e.g., Align Scope and Claims with Empirical Support]
* **WHY:** [Where the title, abstract, or discussion overreaches the quantitative evidence.]
* **WHAT:** [Which claims should be tempered or reframed.]
* **HOW:** [Specific textual revisions to bring the narrative in line with the supported results.]

#### 5. [Actionable Improvement 5 — Technical, Mathematical, and Editorial Cleanup]
* **WHY:** [Inconsistencies between text and tables, equation typos, and broken references undermine reader confidence.]
* **WHAT & HOW:** [Itemized list of exact page/line fixes for equations, table values, figure cross-references, and bibliography entries.]
```
