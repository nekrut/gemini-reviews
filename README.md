# Gemini Scientific Peer Reviews (`spond/gemini-reviews`)

Direct, technically rigorous peer reviews of published manuscripts and preprints in quantitative biology, evolutionary genomics, statistical modeling, bioinformatics, and epidemiology, following the [7-Pillar Rapid Audit, Anti-LLM Trope Mandate, and 3-Section Review Protocol](REVIEW_TEMPLATE.md).

## How to Request a Review

1. Open a new [**Manuscript Review Request Issue**](../../issues/new?template=review_request.yml) with the paper's title, DOI/URL, or preprint identifier.
2. A scheduled watcher detects open `pending-review` issues, audits the manuscript against the **7-Pillar Checklist**, generates a structured **3-Section Review**, assigns a calibrated **1–10 score**, commits the review to `reviews/YYYY/<slug>/review.md`, updates the leaderboard below, and posts the review back to the issue.

---

## Running Tab & Manuscript Leaderboard (1–10 Scale)

<!-- LEADERBOARD_START -->
| Rank | Date | Manuscript Title | Authors | Venue / Year | Rigor (/3.5) | Claims (/2.5) | Biology (/2.0) | Repro (/2.0) | **Overall (/10)** | Tier | Review |
| :---: | :---: | :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :---: |
| 1 | 2026-10-25 | [The emergence and ongoing convergent evolution of the SARS-CoV-2 N501Y lineages](https://pmc.ncbi.nlm.nih.gov/articles/PMC8421097/) | Martin, Weaver et al. (de Oliveira, Pond) | Cell (2021) | 3.1 | 2.0 | 1.7 | 1.8 | **8.6** | Strong / Sound | [Review](reviews/2021/pmc8421097-martin-n501y-convergent-evolution/review.md) |
| 2 | 2026-10-25 | [An evolutionary portrait of the progenitor SARS-CoV-2 and its dominant offshoots in COVID-19 pandemic](https://pmc.ncbi.nlm.nih.gov/articles/PMC7523107/) | Kumar et al. (Pond, Miura) | bioRxiv / Mol Biol Evol (2021) | 2.6 | 1.9 | 1.4 | 1.6 | **7.5** | Strong / Sound | [Review](reviews/2021/pmc7523107-kumar-progenitor-sars-cov-2/review.md) |
| 3 | 2026-10-25 | [Molecular evidence for SARS-CoV-2 in samples collected from patients with morbilliform eruptions since late 2019 in Lombardy, northern Italy](https://pubmed.ncbi.nlm.nih.gov/36029839/) | Amendola et al. (Pond, Kumar, Tanzi) | Environmental Research (2022) | 1.2 | 0.8 | 0.7 | 1.4 | **4.1** | Flawed / Overstated | [Review](reviews/2022/pmc9404229-amendola-lombardy-late-2019/review.md) |
<!-- LEADERBOARD_END -->

---

## Scoring Rubric Summary (1.0 – 10.0)

| Sub-Score | Weight | Pillars | Focus |
| :--- | :---: | :---: | :--- |
| **Methodological & Statistical Rigor** | **3.5 pts** | Pillars 3, 4, 5 | Model specification, internal consistency, calibration of $p$-values/Bayes factors/AIC, uncertainty propagation, and symmetric baseline/null controls |
| **Claim-to-Evidence Alignment** | **2.5 pts** | Pillars 1, 5 | Correspondence between title/abstract/discussion claims and what was formally tested; proportion of claims *Well Supported* vs. *Fragile/Overstated/Methodologically Flawed* |
| **Data Integrity & Biological Plausibility** | **2.0 pts** | Pillars 2, 6 | Data provenance, handling of ascertainment/sampling skew, absence of leakage or circular conditioning, contamination controls, and biophysical/epidemiological realism |
| **Reproducibility & Technical Execution** | **2.0 pts** | Pillar 7 | Public availability of raw data and executable code, mathematical accuracy of equations, numerical consistency across text/tables/supplements, and clean references |

| Score Range | Tier | Diagnostic Interpretation |
| :---: | :--- | :--- |
| **9.0 – 10.0** | **Exemplary** | Sound model specification, calibrated uncertainty, symmetric controls, open data/code, and claims strictly bounded by statistical support |
| **7.0 – 8.9** | **Strong / Sound** | Solid methodological and empirical contribution; minor modeling caveats, unpropagated intermediate uncertainty, or secondary framing overreach |
| **5.0 – 6.9** | **Mixed / Salvageable** | Useful dataset or core method, but undermined by 1–2 major pillar violations (e.g., circular conditioning, uncalibrated tests, or missing baselines) requiring re-analysis |
| **3.0 – 4.9** | **Flawed / Overstated** | Core conclusions rest on statistical artifacts, severe ascertainment/contamination bias, or biologically implausible assumptions |
| **1.0 – 2.9** | **Fundamentally Invalid** | Pervasive technical failures, unaddressed leakage/contamination, or claims directly contradicted by the manuscript's own tables |

---

## Repository Structure

```text
gemini-reviews/
├── README.md                        # Overview + Auto-updated Leaderboard Table
├── REVIEW_TEMPLATE.md               # 7-Pillar Audit, Anti-LLM Style Rules, 1-10 Rubric & 3-Section Template
├── index.json                       # Machine-readable ledger of all reviewed papers & scores
├── .github/
│   └── ISSUE_TEMPLATE/
│       └── review_request.yml       # Structured Issue form for submitting papers to review
├── reviews/
│   └── YYYY/                        # Grouped by publication/preprint year
│       └── <slug>/
│           ├── review.md            # Generated Markdown peer review
│           └── metadata.json        # Structured scores, DOI, issue #, timestamp
└── scripts/
    ├── watch_issues.py              # Polls GitHub Issues for pending review requests
    └── update_leaderboard.py        # Rebuilds index.json and README.md table
```
