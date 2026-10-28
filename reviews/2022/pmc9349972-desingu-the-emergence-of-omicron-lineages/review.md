# Review of PMC9349972 (PMID:35770368)

**Manuscript Title:** The emergence of Omicron lineages BA.4 and BA.5, and the global spreading trend  
**Authors:** Desingu PA, Nagarajan K.  
**Journal / Preprint:** *J Med Virol* (2022; `PMC9349972` / `PMID:35770368` / `10.1002/jmv.27967`)  
**Calibration Study Cohort:** Cohort A — Known Invalid / Refuted (`A06` | Double-Blinded as `ANON_12`)  
**Overall Score:** **3.3 / 10.0** (Flawed / Overstated)  
* **Score Breakdown:** Rigor: 0.8/3.5 | Claims: 0.7/2.5 | Biology: 0.9/2.0 | Reproducibility: 0.9/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This correspondence piece summarizes the global geographic distribution, temporal prevalence trends, and lineage-defining amino acid mutations of the SARS-CoV-2 Omicron BA.4, BA.5, and BA.5.1 sublineages through mid-June 2022. The authors compile summary statistics and mutation heatmaps directly from public web dashboards (`outbreak.info`, `cov-spectrum.org`, and `outbreakindia.com`), noting the replacement of BA.2 by BA.4 and BA.5 in South Africa, comparing mutation profiles across 10 viral proteins (Figure 1F–O), and attributing a June 2022 increase in daily COVID-19 cases in India to BA.4. No custom code, sequence accession lists, or processed data tables are provided beyond links to the interactive web portals.

As a descriptive surveillance summary, the manuscript is undermined by the absence of quantitative statistical modeling, severe ascertainment bias from equating raw GISAID sequence shares with geographic disease prevalence, inconsistent temporal cutoffs (mixing June 6, June 10, June 16, and June 18, 2022 across panels), and multiple factual and virological errors in the mutation analysis. Furthermore, the manuscript makes unsupported causal claims regarding BA.4 driving the June 2022 wave in India and self-contradictory immunological claims regarding BA.2 cross-protection. Salvaging the correspondence requires correcting the misannotated viral mutations and protein labels, normalizing sequence counts by national testing and sequencing volume, fitting formal logistic growth models with uncertainty intervals, and removing speculative claims that conflict with the cited neutralization literature.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **BA.4 and BA.5 are concentrated in South Africa, the United States, and Europe, with >80% of BA.5.1 restricted to Europe: [Methodologically Flawed].**  
  The authors report that 69.31% of BA.4 sequences (up to June 16, 2022) came from South Africa (31.24%), the US (27.05%), and the UK (11.02%), and >80% of BA.5 and BA.5.1 sequences (up to June 6, 2022) came from the US, South Africa, and Europe (Figure 1A–C). Dividing a country's submitted BA.4/BA.5 sequences by the global GISAID BA.4/BA.5 total reflects disparities in national genomic sequencing capacity and submission volume rather than true epidemiological prevalence. Moreover, the analysis uses shifting cutoff dates across lineages (June 16 for BA.4 vs. June 6 for BA.5 and BA.5.1 vs. June 10 for global prevalence) without accounting for GISAID submission lag.

* **BA.4 and BA.5 differ by exactly four amino acids—one each in ORF1a, ORF6, ORF7b, and N—and L452R was already present in Omicron B.1.1.529: [Methodologically Flawed].**  
  This mutational summary contains multiple factual errors:
  1. The text states that BA.4 carries `ORF7b-D61L` and that BA.4 and BA.5 differ in `ORF7b` as shown in "Figure 1F–O". In reality, Figure 1L plots **ORF7a** (not ORF7b), `D61L` is a mutation in **ORF6** (`ORF6:D61L`, present in BA.2 and BA.4 but absent in BA.5), and the BA.4-specific mutation in ORF7b is `ORF7b:L11F`.
  2. The text counts `OFR1a-DEL141/143` (a three-amino-acid deletion, $\Delta\text{K141–F143}$, in NSP1) as "one amino acid difference" and counts `DEL69/70` (a two-amino-acid deletion in Spike) as a single amino acid difference.
  3. The text claims that "mutations such as DEL69/70 and L452R are already present in the Omicron lineage B.1.1.529." While $\Delta\text{69/70}$ was present in BA.1 (B.1.1.529), `S:L452R` was *not* present in ancestral Omicron B.1.1.529, BA.1, BA.2, or BA.3.

* **The rise in COVID-19 cases in India between May 30 and June 17, 2022 was caused by the BA.4 lineage: [Overstated].**  
  The authors observe that reported daily cases in India rose from 2,338 on May 30 to 13,216 on June 17, 2022, and assert that "From these, it can be inferred that the BA.4 lineage is causing the increasing number of COVID-19 cases in India" (citing Supporting Information Figure 2C). No sample sizes, sequence counts, confidence intervals, or competing BA.2 sublineage proportions (e.g., BA.2.38 and BA.2.75, which expanded in India during this exact period) are reported, nor is any ecological or growth-rate regression performed to link BA.4 frequency to national case counts.

* **Antibodies from BA.2 infection and BA.2-based vaccines can be expected to protect against and control the spread of BA.4/BA.5: [Overstated].**  
  In the same paragraph where the authors cite studies showing that BA.4/BA.5 is 4–20-fold more resistant to monoclonal antibodies than BA.2 and evades neutralization via Spike RBD mutations `L452R` and `F486V`, they conclude that "since the spike protein is almost identical in the BA.2 and BA.4/BA.5 lineages, antibodies to the BA.2 infection can be expected to protect the BA.4/BA.5 lineages." Because the four Spike differences between BA.2 and BA.4/BA.5 (`DEL69/70`, `L452R`, `F486V`, and the `R493Q` reversion) are concentrated at immunodominant RBD epitopes specifically selected to escape BA.1/BA.2 neutralizing antibodies, sequence identity outside the RBD does not imply preserved neutralizing protection against infection and transmission.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Correct Factual Errors in Viral Protein Annotations and Lineage Mutations
* **WHY:** Misidentifying `ORF6:D61L` as `ORF7b-D61L`, referencing `ORF7b` when Figure 1L plots `ORF7a`, and claiming `S:L452R` was present in ancestral Omicron B.1.1.529 misleads readers about SARS-CoV-2 evolutionary genetics.
* **WHAT:** Revise the text and Figure 1 panels to accurately report the lineage-defining mutations of BA.4, BA.5, and BA.5.1.
* **HOW:**
  * Replace "ORF7b-D61L" with `ORF6:D61L` (present in BA.2 and BA.4, reverted in BA.5) and `ORF7b:L11F` (present in BA.4).
  * Either add an `ORF7b` panel to Figure 1 or revise the text so it does not cite Figure 1F–O for `ORF7b` while omitting `ORF7a`.
  * Correct the statement on Spike mutations to specify that `DEL69/70` ($\Delta\text{H69/V70}$) was present in BA.1 and BA.3, whereas `L452R` and `F486V` were newly acquired in BA.4/BA.5 relative to BA.1/BA.2/BA.3 (alongside the reversion `R493Q`).
  * Refer to `ORF1a:DEL141/143` and `S:DEL69/70` as multi-residue deletions (spanning 3 and 2 amino acids, respectively) rather than single amino acid differences.

#### 2. Normalize Lineage Frequencies Within Countries and Standardize Collection Date Cutoffs
* **WHY:** Computing each country's share of total global BA.4 or BA.5 sequences on GISAID primarily measures national sequencing volume ( heavily weighted toward the US, UK, and South Africa), and mixing June 6, June 10, June 16, and June 18 cutoffs distorts cross-lineage comparisons.
* **WHAT:** Report within-country lineage proportions (number of BA.4 or BA.5 sequences in country $i$ divided by total SARS-CoV-2 sequences collected in country $i$ over the same time window) using a uniform collection-date cutoff that accounts for submission delay.
* **HOW:** Query `outbreak.info` or `cov-spectrum.org` using a uniform collection date window (e.g., May 1–May 31, 2022, allowing at least 2–3 weeks for sequence deposition prior to the June 18 download date), and report for each country: (a) total sequences $N_i$, (b) BA.4, BA.5, and BA.5.1 proportions $p_i = n_{i,\text{lineage}}/N_i$, and (c) 95% binomial confidence intervals.

#### 3. Quantify Lineage Growth Advantages and Re-evaluate the India Case Surge
* **WHY:** Visual inspection of raw prevalence curves without sample sizes or competing sublineage breakdowns cannot establish that BA.4 caused the June 2022 case increase in India.
* **WHAT:** Report the exact count of sequenced genomes and full Pango lineage breakdown in India during May–June 2022, and fit a multinomial or logistic growth model.
* **HOW:** Extract weekly sequence counts in India from GISAID / `cov-spectrum.org` for BA.2, BA.2.38, BA.2.75, BA.4, and BA.5 across May–June 2022. Fit a logistic growth model $\text{logit}(p(t)) = \alpha + s \cdot t$ to estimate the weekly growth advantage $s$ (with 95% confidence intervals) of BA.4 and BA.5 relative to BA.2, and temper the causal attribution of India's case surge to reflect the actual fraction of cases attributable to BA.4 versus emerging BA.2 sublineages.

#### 4. Align Immunological Claims with Cited Neutralization Data
* **WHY:** Claiming that BA.2 infection antibodies will protect against BA.4/BA.5 because their Spike proteins are "almost identical" contradicts the functional neutralization escape conferred by `L452R` and `F486V`.
* **WHAT:** Revise the penultimate paragraph to accurately reflect reduced neutralizing titers of BA.1/BA.2 convalescent sera against BA.4/BA.5.
* **HOW:** Remove or qualify the assertion that BA.2 infection antibodies can be expected to control BA.4/BA.5 spread, and clarify that while T-cell epitopes across Spike remain largely conserved, the RBD mutations `L452R` and `F486V` substantially reduce neutralizing antibody potency from prior BA.1 and BA.2 infections.

#### 5. Technical and Editorial Cleanup
* **WHY:** Typos in gene names, broken grammar, and incorrect dashboard URLs reduce clarity and reproducibility.
* **WHAT & HOW:**
  * **Main text (Paragraph 2, twice):** Correct the typo `OFR1a` and `OFR1a-DEL141/143` to `ORF1a` and `ORF1a-DEL141/143`.
  * **Figure 1 Caption (Panels D, E):** The caption states "Prevalence of different Omicron lineages in South Africa over the periods. The data were obtained from `https://outbreak.info/location-reports?loc=IND&pango`." Replace `loc=IND` (India) with `loc=ZAF` (South Africa).
  * **Main text (Paragraph 3):** Revise "monoclonal antibodies such as cilgavimab and Evusheld" to "monoclonal antibodies such as cilgavimab (a component of Evusheld, tixagevimab/cilgavimab)."
  * **Main text (Paragraph 3):** Fix the ungrammatical sentence "Furthermore, the Q493R (spike protein) mutation was found in all Omicron lineages, and sublineages are not found in the BA.4/BA.5 lineages" to "Furthermore, the Spike Q493R mutation present in BA.1, BA.2, and BA.3 reverted to the ancestral glutamine (Q493) in the BA.4 and BA.5 lineages."
