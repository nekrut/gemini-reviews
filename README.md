# Gemini Scientific Peer Reviews (`spond/gemini-reviews`)

Automated, intellectually rigorous peer reviews of published manuscripts and preprints in viral evolution, molecular epidemiology, and computational biology, following the [7-Pillar Rapid Audit & 3-Section Review Protocol](REVIEW_TEMPLATE.md).

## How to Request a Review

1. Open a new [**Manuscript Review Request Issue**](../../issues/new?template=review_request.yml) with the paper's title, DOI/URL, or preprint identifier.
2. A scheduled watcher detects open `pending-review` issues, audits the manuscript against the **7-Pillar Checklist**, generates a structured **3-Section Review**, assigns a calibrated **1–10 score**, commits the review to `reviews/YYYY/<slug>/review.md`, updates the leaderboard below, and posts the review back to the issue.

---

## Running Tab & Manuscript Leaderboard (1–10 Scale)

<!-- LEADERBOARD_START -->
| Rank | Date | Manuscript Title | Authors | Venue / Year | Rigor (/3.5) | Claims (/2.5) | Biology (/2.0) | Repro (/2.0) | **Overall (/10)** | Tier | Review |
| :---: | :---: | :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :---: |
| 1 | 2026-10-25 | [The emergence and ongoing convergent evolution of the SARS-CoV-2 N501Y lineages](https://pmc.ncbi.nlm.nih.gov/articles/PMC8421097/) | Martin, Weaver et al. (de Oliveira, Pond) | Cell (2021) | 3.2 | 2.1 | 1.7 | 1.8 | **8.8** | Strong / Sound | [Review](reviews/2021/pmc8421097-martin-n501y-convergent-evolution/review.md) |
| 2 | 2026-10-25 | [An evolutionary portrait of the progenitor SARS-CoV-2 and its dominant offshoots in COVID-19 pandemic](https://pmc.ncbi.nlm.nih.gov/articles/PMC7523107/) | Kumar et al. (Pond, Miura) | bioRxiv / Mol Biol Evol (2021) | 2.9 | 2.0 | 1.4 | 1.6 | **7.9** | Strong / Sound | [Review](reviews/2021/pmc7523107-kumar-progenitor-sars-cov-2/review.md) |
| 3 | 2026-10-25 | [Molecular evidence for SARS-CoV-2 in samples collected from patients with morbilliform eruptions since late 2019 in Lombardy, northern Italy](https://pubmed.ncbi.nlm.nih.gov/36029839/) | Amendola et al. (Pond, Kumar, Tanzi) | Environmental Research (2022) | 1.4 | 0.9 | 0.7 | 1.4 | **4.4** | Flawed / Overstated | [Review](reviews/2022/pmc9404229-amendola-lombardy-late-2019/review.md) |
<!-- LEADERBOARD_END -->

---

## Scoring Rubric Summary (1.0 – 10.0)

| Sub-Score | Weight | Focus |
| :--- | :---: | :--- |
| **Methodological & Statistical Rigor** | **3.5 pts** | Codon-aware alignments, appropriate clock rooting, AIC-backed trait models, recombination screening, FDR control |
| **Claim-to-Evidence Alignment** | **2.5 pts** | Title/abstract scope vs. actual tests performed; proportion of key claims well-supported vs. fragile/overstated |
| **Data Integrity & Biological Plausibility** | **2.0 pts** | Passage/freezer history, sampling skew, identical cross-border tips, biophysical & mutational realism |
| **Reproducibility & Technical Execution** | **2.0 pts** | Open sequence/read data (SRA/GenBank/GISAID) & code (GitHub/Zenodo), clean figures/tables/statistics |

| Score Range | Tier | Interpretation |
| :---: | :--- | :--- |
| **9.0 – 10.0** | **Exemplary / Landmark** | Bulletproof methodology, zero pillar violations, open code/data, claims tightly bounded by statistical support |
| **7.0 – 8.9** | **Strong / Sound** | Solid empirical or methodological contribution; minor framing or secondary analytical caveats |
| **5.0 – 6.9** | **Mixed / Salvageable** | Valuable dataset or core idea, but undermined by 1–2 major pillar errors requiring re-analysis |
| **3.0 – 4.9** | **Flawed / Overstated** | Core conclusions rest on statistical artifacts, severe sampling bias, or biophysically implausible assumptions |
| **1.0 – 2.9** | **Fundamentally Invalid** | Pervasive technical failures, unaddressed contamination/passage artifacts, or self-contradictory tables |

---

## Repository Structure

```text
gemini-reviews/
├── README.md                        # Overview + Auto-updated Leaderboard Table
├── REVIEW_TEMPLATE.md               # 7-Pillar Audit, 1-10 Rubric & 3-Section Review Template
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
