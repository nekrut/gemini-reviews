# Scientific Peer Review Template & Diagnostic Guide for Viral Evolution

This guide provides a standardized, fast-turnaround peer review protocol, 1–10 quantitative scoring rubric, and Markdown template for journals such as *Virus Evolution*, *PLOS Pathogens*, *PLOS Biology*, *Nature*, *Science*, *Journal of Virology*, *Molecular Biology and Evolution*, and *Bioinformatics*, as well as preprints (*bioRxiv*, *medRxiv*).

The goal is to produce **human-scale, punchy, intellectually rigorous reviews** that avoid unnecessary walls of text while directly auditing methodology, statistical support, and biological plausibility.

---

## PART 1: THE 7-PILLAR RAPID AUDIT CHECKLIST

Before writing, scan the manuscript against these seven diagnostic pillars:

1. **Scope & Framing:** Does the title claim "drivers," "transmission," or "fitness" when the study only performs descriptive phylogenetics or coarse clustering?
2. **Data & Passage History:** Are historic isolates passaged in cell lines/eggs or stored frozen for decades (which decouples calendar year from divergence)? Are tip states heavily skewed (e.g. 75% from one region)?
3. **Alignment & Trees:** Is alignment codon-aware? Are trees midpoint-rooted on ancient, rate-heterogeneous clades? Are there massive comb polytomies?
4. **Molecular Clock (TempEst):** Did the authors fall into the "pooling trap" (regressing root-to-tip distance across deeply divergent serotypes that split centuries ago)? If the clock fails, do they falsely blame "purifying selection"?
5. **Trait Models & ASR:** Is the geography artificially collapsed (e.g., "USA vs. Outside USA")? Does the model selection table (AIC/BIC) actually support the model used (e.g. ARD vs SYM/ER)? Were identical cross-border tips improperly discarded?
6. **Segmented Biology & Recombination:** For segmented arboviruses or recombining coronaviruses/retroviruses, are authors claiming segments "fly at different speeds" or ignoring mosaic breakpoints? (Outer capsid mixing vs. internal backbone conservation is serotype introgression via reassortment, not segment flight velocity).
7. **Technical Sanity Checks:** Check for negative scale bars, swapped supplemental table labels, software typos ("MAAFT"), and permutation floor p-values ($1/N$).

---

## PART 2: THE 1–10 QUANTITATIVE SCORING RUBRIC

Every reviewed manuscript receives an **Overall Score (1.0 – 10.0)** computed as the sum of four diagnostic sub-scores:

1. **Methodological & Statistical Rigor (0.0 – 3.5 pts):** Are evolutionary/statistical models appropriate (codon-aware alignments, proper clock rooting, AIC-backed trait models, recombination screening, proper multiple-testing/FDR control)?
2. **Claim-to-Evidence Alignment (0.0 – 2.5 pts):** Do the title, abstract, and conclusions match what was actually tested? What proportion of key claims in Section 2 are *Well Supported* vs. *Overstated/Fragile/Artifactual*?
3. **Data Integrity, Sampling & Biological Plausibility (0.0 – 2.0 pts):** Proper handling of passage history, sampling skew, identical sequences, recombination/reassortment, and mutational/biophysical realism.
4. **Reproducibility & Technical Execution (0.0 – 2.0 pts):** Raw data/code availability (SRA/GenBank/GISAID/GitHub/Zenodo), absence of technical glitches (negative scale bars, permutation floor artifacts, mislabeled tables).

### Calibration Tiers
| Score | Tier | Diagnostic Interpretation |
| :---: | :--- | :--- |
| **9.0 – 10.0** | **Exemplary / Landmark** | Bulletproof methodology, zero pillar violations, open code/data, claims tightly bounded by statistical support. |
| **7.0 – 8.9** | **Strong / Sound** | Solid empirical or methodological contribution; minor framing overreach or secondary analytical caveats easily fixed in text. |
| **5.0 – 6.9** | **Mixed / Salvageable** | Valuable dataset or core idea, but undermined by 1–2 major pillar errors (e.g., TempEst pooling trap, unsupported ARD trait model) requiring re-analysis. |
| **3.0 – 4.9** | **Flawed / Overstated** | Core conclusions rest on statistical artifacts, severe sampling bias, or biophysically implausible assumptions. |
| **1.0 – 2.9** | **Fundamentally Invalid** | Pervasive technical failures, unaddressed contamination/passage artifacts, or claims contradicted by the paper's own tables. |

---

## PART 3: THE 3-SECTION CONCISE REVIEW TEMPLATE

```markdown
# Review of [MANUSCRIPT_ID / DOI]

**Manuscript Title:** [INSERT FULL MANUSCRIPT TITLE]  
**Authors:** [INSERT AUTHOR LIST]  
**Journal / Venue:** [INSERT JOURNAL OR PREPRINT SERVER] (ID / DOI: [INSERT ID/DOI])  
**Overall Score:** **[X.X] / 10.0** ([Tier Name])  
* **Score Breakdown:** Rigor: [X.X]/3.5 | Claims: [X.X]/2.5 | Biology: [X.X]/2.0 | Reproducibility: [X.X]/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

[Paragraph 1: Concise summary of what was done. State dataset size, sequencing platforms, time span, geography, and core analytical tools used. Highlight raw data availability (SRA/GenBank) and reproducible code.]

[Paragraph 2: Clear bottom-line evaluation. Acknowledge empirical contributions. Highlight the primary methodological/statistical tensions. Conclude with an encouraging, actionable assessment (e.g., "requires no new wet-lab work, can be resolved through computational re-analysis and reframing").]

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **[Key Claim 1, e.g., Structural Co-adaptation / Feature Interaction]: [Well Supported / Moderately Supported / Fragile].**  
  [Briefly explain why: physical plausibility, metric consistency, or caveats like polytomies/matrix symmetrization.]

* **[Key Claim 2, e.g., Accessory Gene Autonomy / Modularity]: [Well Supported / Weakly Supported].**  
  [Briefly explain why: concordance across comparisons, alignment with non-structural biology.]

* **[Key Claim 3, e.g., Invariance of Proposed Metric or Backbone]: [Overstated / Supported].**  
  [Briefly explain why: e.g., coarse clade definitions masking intra-genogroup diversity and reassortment.]

* **[Key Claim 4, e.g., Directional Migration / Transition Rates (ASR)]: [Poorly Supported / Artifactual].**  
  [Briefly explain why: model selection contradiction in AIC tables, tip sampling bias, inappropriate tip filtering, or conflating reassortment introgression with physical dispersal.]

* **[Key Claim 5, e.g., Multi-Decade Persistence with Zero Mutation]: [Highly Questionable / Biophysically Implausible].**  
  [Briefly explain why: failure to account for laboratory passage history, archival freezer storage, or contamination.]

* **[Key Claim 6, e.g., Molecular Clock Failure Mechanism]: [Conceptually Invalid].**  
  [Briefly explain why: misdiagnosing the multi-clade pooling trap and passage arrest as "purifying selection".]

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. [Improvement 1, e.g., Reconcile Trait Model Selection with AIC]
* **WHY:** [Why the current analysis or text is methodologically/statistically flawed.]
* **WHAT:** [What specific change is needed in claims or figures.]
* **HOW:** [Exact, doable step: e.g., apply SYM/ER in R `fitMk`, re-plot figure with bidirectional arrows.]

#### 2. [Improvement 2, e.g., Re-integrate Excluded Identical Sequences]
* **WHY:** [Why removing cross-border identical sequences distorts the transmission signal.]
* **WHAT:** [Restore empirical signal of recent gene flow.]
* **HOW:** [Re-include tips in ASR; add $\epsilon = 10^{-6}$ to branch lengths if needed for polytomies.]

#### 3. [Improvement 3, e.g., Reframe Segment "Movement" as Serotype Introgression]
* **WHY:** [Viruses disperse as intact particles; segments do not travel independently.]
* **WHAT:** [Replace biologically flawed claim with established reassortment dynamics.]
* **HOW:** [Rewrite text to describe introgression of exotic capsids into endemic backbones.]

#### 4. [Improvement 4, e.g., Contextualize Persistence with Passage History]
* **WHY:** [Zero mutations over decades in an active RNA virus in the wild is biophysically implausible.]
* **WHAT:** [Prevent reader skepticism regarding field vs. archival dynamics.]
* **HOW:** [Audit laboratory records; explicitly attribute stasis to archival cold storage.]

#### 5. [Improvement 5, e.g., Correct the Molecular Clock Failure Explanation]
* **WHY:** [Purifying selection lowers rates but preserves a linear clock.]
* **WHAT:** [Provide a theoretically sound justification for omitting time-scaled models.]
* **HOW:** [Explain clock breakdown via multi-serotype pooling and passage arrest.]

#### 6. [Improvement 6, e.g., Retitle and Align Scope]
* **WHY:** [No ecological/selective drivers were tested; metric characters are largely invariant.]
* **WHAT:** [Match title and framing to actual findings.]
* **HOW:** [Adopt a descriptive title; present proposed code as an indexing shorthand.]

#### 7. [Improvement 7, e.g., Technical, Visual, and Supplementary Cleanup]
* **WHY:** [Graphical glitches and table mislabeling distract from data quality.]
* **WHAT & HOW:** [Fix negative scale bars; correct swapped supplemental tables; fix software typos; clarify permutation limits.]
```
