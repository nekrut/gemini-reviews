# Blinded Review: SP_ANON_027
**Composite Score:** 7.8 / 10.0 (Rigor: 2.7/3.5 | Claims: 2.0/2.5 | Biology: 1.6/2.0 | Reproducibility: 1.5/2.0)
**Bias Category:** Surveillance Ascertainment Circularity (Genotype Availability & Testing Cascade)
**Verdict:** Minor Revision
**Study Modality:** Dry-Lab Secondary Cohort/Database Re-Analysis
**Technology Maturity:** Mid-Stage High-Throughput
**Epistemic Stage:** Clinical/Epidemiological Observational

---

### 1. Executive Summary
This study leverages 65,736 HIV-1 *pol* genotypes from the New York City Department of Health and Mental Hygiene (DOHMH) surveillance registry (diagnosed 2005–2017; 9,854 clustered individuals across 2,705 molecular transmission clusters inferred via HIV-TRACE at $\text{TN93} \le 0.015$) to evaluate quantitative schemes for prioritizing up to 500 individuals per month for public health intervention. Using strictly prospective, monthly rolling-window backtesting from January 2007 through January 2015, the authors compare random allocation, individual-level LASSO logistic regression, and cluster-growth heuristics. They show that prioritizing clusters by past 12-month growth divided by the square root of cluster size ($\Delta N / \sqrt{N}$) yields 0.149 newly diagnosed genetically linked cases per prioritized case over the following 12 months (compared to 0.011 for random individuals and 0.076 for random clustered individuals) and avoids the secular performance decay observed when prioritizing purely by total cluster growth ($\Delta N$).

---

### 2. Methodological & Statistical Audit
* **Rigorous Prospective Rolling-Window Validation (Zero Lookahead Leakage):** A standout methodological feature of this study is its strict adherence to temporal availability in longitudinal backtesting. At each monthly evaluation step $t$ (97 rolling windows from 2007 to 2015), transmission networks, LASSO regression weights, and historical growth metrics are trained solely on surveillance data reported up to month $t-12$ and applied to data at month $t$ to predict new links diagnosed in $[t, t+12]$. This completely avoids retrospective lookahead bias.
* **Analytical Insight into Cluster Size Scaling ($\Delta N / \sqrt{N}$):** Prioritizing clusters by raw historical growth ($\Delta N$) progressively selects giant, aging clusters whose per-capita yield of new linked cases decays sharply over time (Figure 3B). Scaling growth by $\sqrt{N}$ (or $N$) appropriately normalizes for the number of cases that must be intervened upon in a cluster under a fixed monthly public health budget (500 cases/month), maintaining stable prospective yield across an 8-year horizon.
* **Surveillance Ascertainment Circularity:** In a molecular surveillance registry, observing a "new genetically linked case" requires two sequential events: (1) an undiagnosed individual must get tested for HIV, and (2) a clinician must order a baseline drug-resistance genotype (which occurred for only 62.6% of NYC HIV diagnoses during the study period). As the authors candidly note in the Discussion, young White MSM in Manhattan had substantially higher rates of early testing, care engagement, and resistance genotyping than Black or Hispanic heterosexuals or PWID in outer boroughs (e.g., Staten Island vs. Manhattan odds ratio = 0.67). Consequently, the outcome metric ("new linked genotyped diagnoses in the next 12 months") conflates true biological transmission incidence with rapid diagnostic ascertainment and partner testing cascades within well-resourced sexual networks.
* **Table 1 Typographical Error:** In Table 1, under Borough of residence for the Bronx, the number of clustered individuals is printed as `2751 (2.3)`. Since $2,751 / 13,551 = 20.30\%$, `2.3` is a typographical omission of the zero in `20.3%`.

---

### 3. Biological / Experimental Grounding & Claim Proportionality
* **Claim:** *Cluster-level prioritization using past growth normalized by $\sqrt{\text{cluster size}}$ outperforms individual-level demographic/clinical LASSO models and remains stable over time.* **[Well Supported]** — Demonstrated across 97 rolling monthly cohorts (Figure 3B, Table 2), where $\Delta N / \sqrt{N}$ achieves 0.149 new links per prioritized person vs. 0.128 for individual-level LASSO, and combining both reaches 0.152.
* **Claim:** *Prioritizing fast-growing molecular clusters targets active viral transmission.* **[Moderately Supported]** — Because genetically linked diagnoses within 12 months include delayed diagnoses of older infections, cluster growth captures a mixture of recent transmission and active case-finding/testing waves. The authors discuss this distinction with commendable nuance.

---

### 4. Reproducibility & Data Completeness
* **Software Availability:** The network clustering tool (`HIV-TRACE`, `[GITHUB_REPO_REDACTED]`) and LASSO modeling framework (`glmnet`) are publicly available and standard.
* **Data Privacy Constraints:** Raw HIV-1 *pol* sequences and patient-level demographic records cannot be publicly released due to legal public health confidentiality mandates for surveillance registries, which is appropriately documented in the Ethics Statement.
