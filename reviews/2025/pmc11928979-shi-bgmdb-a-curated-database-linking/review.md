# Review of PMC11928979 (PMID:40123802)

**Manuscript Title:** BGMDB: A curated database linking gut microbiota dysbiosis to brain disorders  
**Authors:** Shi K, He Q, Zhao P, Li L, Liu Q, Wu Z, Wang Y, Dong H, Yu J.  
**Journal / Preprint:** *Comput Struct Biotechnol J* (2025; `PMC11928979` / `PMID:40123802` / `10.1016/j.csbj.2025.02.034`)  
**Calibration Study Cohort:** Cohort C — Wild Literature Sample (`C67` | Double-Blinded as `ANON_115`)  
**Overall Score:** **4.3 / 10.0** (Flawed / Overstated)  
* **Score Breakdown:** Rigor: 1.2/3.5 | Claims: 1.1/2.5 | Biology: 1.1/2.0 | Reproducibility: 0.9/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript presents the Brain Disease Gut Microbiota Database (BGMDB), a web-based repository (`http://bgmdb.online/bgmdb`) built with Spring Boot and Apache Tomcat that aggregates literature-curated associations among gut microbial taxa, human brain disorders, neurotransmitters, and encephalic regions (Brodmann areas). By querying PubMed, Web of Science, and existing microbiome databases (MicroPhenoDB, Peryton, gutMDisorder, MiKG4MD, MMiKG, and gutMGene), the authors curated 1,419 associations spanning 609 microbial entries and 43 brain disorders from 1,445 articles, alongside 184 tripartite links across six neurotransmitter systems. Neither the underlying curation tables nor the database source code are deposited in a permanent archival repository.

While consolidating scattered literature on gut-brain axis associations into a searchable interface is a potentially useful service for neuro-gastroenterology researchers, the manuscript is undermined by ad hoc quantitative scoring, biological misinterpretations in its application case studies, and unarchived data infrastructure. Specifically, the proposed "Association Strength" metric ($AS_{e_{ij}}$) relies on cumulative journal impact factor as a primary weight ($w_2 = 0.3$) and leaves its mathematical transformations underspecified; the curation protocol excludes "conflicting results" without objective criteria or recording the direction of microbial abundance changes; and the case studies mischaracterize basic MeSH hierarchy lookups and cross-study taxon co-occurrences as "mining homologous brain disorders" and "investigating microbial symbiosis." Resolving these issues requires replacing the impact-factor heuristic with transparent evidence grading, recording effect directionality and host species, correcting the biological terminology in the case studies, and depositing the complete database dump and code in an open archive.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **BGMDB provides 1,419 experimentally validated associations across 609 gut microbiota species/taxa and 43 brain disorders: [Moderately Supported].**  
  The authors integrate records from 1,445 articles and six public databases using MeSH and NCBI Taxonomy normalization. However, Table 1 reveals a taxonomic discrepancy: although the table header and row label refer to "Microbial Species (Total: 609)," only 122 entries are actually at the species level, whereas 338 are higher taxonomic ranks (Kingdom through Genus) and 149 are labeled "Other." Furthermore, Section 2.1 notes that the authors "excluded highly uncertain or conflicting results" during manual curation without specifying quantitative inclusion thresholds, sample-size cutoffs, whether animal model and human clinical studies are separated, or whether directionality (enrichment vs. depletion in disease) is retained.

* **The Association Strength indicator ($AS_{e_{ij}}$, Equation 1) reliably quantifies the confidence level of microbe–disease associations: [Methodologically Flawed].**  
  Equation 1 defines $AS_{e_{ij}} = w_1 SN_{e_{ij}} + w_2 SF_{e_{ij}} + w_3 SRD_{e_{ij}} + w_4 SD_{e_{ij}}$ with weights $w_1 = 0.5$ (publication count), $w_2 = 0.3$ (cumulative journal impact factor), $w_3 = 0.1$ (raw data availability), and $w_4 = 0.1$ (existing database inclusion). Weighting cumulative journal impact factor ($30\%$ of the score) conflates journal citation metrics with experimental rigor, sample size, and statistical effect size. In addition, the text states that "$\log_{10}$ and Sigmoid transformation are carried out on $SN_{e_{ij}}$ and $SF_{e_{ij}}$" without writing the composite functional form in Equation 1, specifying whether the sigmoid is applied to $\log_{10}(x)$, or addressing how single-publication entries ($\log_{10}(1) = 0$, $\sigma(0) = 0.5$) are scaled relative to binary indicators $SRD_{e_{ij}}, SD_{e_{ij}} \in \{0,1\}$.

* **BGMDB enables the identification of "homologous brain disorders" sharing gut microbiota profiles (Section 4.3.1): [Overstated].**  
  In Section 4.3.1 and Figure 5, the authors claim that BGMDB identifies "homologous brain diseases," but the actual operation described is simply browsing the static MeSH category tree ("Alzheimer's disease is classified under Central Nervous System Diseases... Neurotic Anorexia, Anxiety Disorder, Bipolar Disorder, and others fall within the same category"). Displaying standard MeSH ontology siblings does not constitute computational mining of microbiota-driven disease homology.

* **BGMDB reveals "microbial symbiosis in brain diseases" such as shared *Pseudomonas* presence in stroke and Alzheimer's disease (Section 4.3.2): [Methodologically Flawed].**  
  Section 4.3.2 and Figure 6 equate the observation that two disorders (stroke and Alzheimer's disease) are independently associated with the same bacterial genus (*Pseudomonas*) or that multiple taxa (*Coriobacteriaceae*, *Staphylococcus*) appear under one disease with "microbial symbiosis." In microbial ecology, symbiosis refers to direct biological interaction (mutualism, commensalism, or parasitism) between co-occurring organisms within a shared habitat, which cannot be inferred merely from separate literature reports associating taxa with the same clinical diagnosis.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Replace the Impact-Factor Heuristic with an Evidence-Based Confidence Score
* **WHY:** Journal impact factor is a journal-level bibliometric mean that does not measure study design quality, statistical power, or replication fidelity, and the mathematical form of the $\log_{10}$/sigmoid transformation in Equation 1 is currently unimplementable as written.
* **WHAT:** Reformulate Equation 1 to score study-level evidentiary features (e.g., human clinical cohort vs. animal model, sample size $N$, presence of causal/interventional validation such as fecal microbiota transplantation, and directional consistency across studies) and write out the exact mathematical equations.
* **HOW:** Since the authors already extracted "experiment type, design, sample size" for each entry (Section 3.1), replace $SF_{e_{ij}}$ with a sample-size and study-design term, explicitly write the composite transformation $\tilde{x} = [1 + \exp(-k(\log_{10}(x) - x_0))]^{-1}$ with exact parameter values, and report the distribution of resulting $AS_{e_{ij}}$ scores across the 1,419 associations.

#### 2. Document Curation Criteria and Retain Conflicting/Directional Associations
* **WHY:** Omitting conflicting studies introduces confirmation bias into a reference database, especially in microbiome research where taxonomic shifts frequently vary across cohorts and geography.
* **WHAT:** Retain conflicting literature reports in the database, explicitly annotate the direction of change (increased vs. decreased abundance in cases relative to controls) and host organism (human vs. rodent model), and report inter-curator agreement statistics.
* **HOW:** Add a `Direction` column (`Up` / `Down` / `Altered`) and a `Host_Model` column to the association schema, include discordant studies rather than discarding them, and modify the association confidence score to penalize directional discordance (e.g., multiplying by $|n_{\text{up}} - n_{\text{down}}| / (n_{\text{up}} + n_{\text{down}})$).

#### 3. Correct Biological Terminology and Perform Quantitative Disease-Similarity Clustering
* **WHY:** Calling MeSH ontology browsing "mining homologous brain diseases" (Section 4.3.1) and calling shared disease-taxon links "microbial symbiosis" (Section 4.3.2) misrepresents basic database lookups as ecological or evolutionary findings.
* **WHAT:** Rename Sections 4.3.1 and 4.3.2 to accurately reflect ontology navigation and shared taxon queries, and compute an actual quantitative similarity metric between disorders based on their curated microbial profiles.
* **HOW:** Using the $43 \times 609$ disease–taxon incidence matrix, compute pairwise Jaccard or cosine similarity indices (with Fisher's exact test $p$-values and Benjamini–Hochberg FDR correction) to identify brain disorder pairs that share statistically significant microbial overlap beyond chance.

#### 4. Reconcile Taxonomic Ranks and Deposit Full Archival Data
* **WHY:** Table 1 labels 609 entries as "Microbial Species" when only 122 are species and 149 are "Other," and relying solely on an institutional/cloud web URL (`http://bgmdb.online/bgmdb`) risks link rot and prevents offline reproducibility.
* **WHAT:** Clarify the "Other" taxonomic category in Table 1 (e.g., strain-level, operational taxonomic units, or unranked clades) and deposit the complete CSV tables and web application code in a permanent repository.
* **HOW:** Upload the 1,419 disease-microbiota associations, 184 tripartite neurotransmitter records, and Brodmann area mappings to Zenodo or Figshare with a persistent DOI, and update Table 1 to label the row "Microbial Taxa (609)" with an explicit breakdown of the 149 "Other" entries.

#### 5. Technical, Mathematical, and Editorial Cleanup
* **WHY:** Typographical errors and incomplete sentences in the Methods detract from technical clarity.
* **WHAT & HOW:**
  1. **Section 2.1, Paragraph 1:** Fix the imperative fragment *"Utilize MeSH terms and their synonyms to expand the search scope..."* to *"We utilized MeSH terms and their synonyms..."*.
  2. **Section 2.1, Paragraph 3:** Fix the duplicated phrase *"Log 10 and Sigmoid transformation are carried out on SN eij and SF eij carried out on each entry."*
  3. **Section 2.1, Paragraph 4:** Replace the full-width Chinese comma (`，`) in *"MiKG4MD database [17] ，MMiKG [18]"* with a standard English comma.
  4. **Section 3.1, Paragraph 1:** Insert a period or line break after the inline subheading *"Database Structure and Content"* before *"BGMDB provides..."*.
