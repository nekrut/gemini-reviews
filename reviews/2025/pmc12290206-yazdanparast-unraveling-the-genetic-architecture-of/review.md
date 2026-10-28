# Review of PMC12290206 (PMID:40439358)

**Manuscript Title:** Unraveling the Genetic Architecture of Obesity in Childhood Cancer Survivors: Insights from Recent GWAS Studies  
**Authors:** Yazdanparast M, Vafapour M, Nezameslami R, Nezameslami A, Neamatzadeh H.  
**Journal / Preprint:** *Asian Pac J Cancer Prev* (2025; `PMC12290206` / `PMID:40439358` / `10.31557/apjcp.2025.26.5.1477`)  
**Calibration Study Cohort:** Cohort C — Wild Literature Sample (`C84` | Double-Blinded as `ANON_125`)  
**Overall Score:** **1.8 / 10.0** (Fundamentally Invalid)
* **Score Breakdown:** Rigor: 0.4/3.5 | Claims: 0.4/2.5 | Biology: 0.5/2.0 | Reproducibility: 0.5/2.0

**Executive Verdict:**
This brief communication ("Letter") purports to examine the genetic basis of obesity in childhood cancer survivors (CCS) using genome-wide association study (GWAS) data. Forensically auditing the text reveals severe internal contradictions, fabricated or nonsensical methodological descriptions, and statistical threshold violations. Most notably, the manuscript simultaneously claims to be a non-empirical literature synthesis (*"This letter aims to synthesize findings from recent studies"*; Ethics Statement: *"This article does not involve any studies with human participants"*) and an original empirical bioinformatics analysis (*"We analyzed the genetic basis of obesity in childhood cancer survivors... Genome-wide genotype data were generated using Illumina SNP chips"*), while claiming to extract patient BMI and waist circumference data from the **Genomics of Drug Sensitivity in Cancer (GDSC)** project—which is an *in vitro* cancer cell line drug screening resource, not a clinical cohort of childhood cancer survivors. Furthermore, four of the five SNPs reported as genome-wide significant fail the manuscript's own stated significance threshold ($P < 5 \times 10^{-8}$).

---

## Section 2: Audit of Key Claims

1. **Claim 1:** *"We analyzed the genetic basis of obesity in childhood cancer survivors using data from recent GWAS. This involved genetic data from large, publicly available biobanks and consortia, such as the Children's Oncology Group and the Genomics of Drug Sensitivity in Cancer project. The cohorts included childhood cancer survivors of European ancestry, with obesity defined by body mass index (BMI) and waist circumference measurements. Genome-wide genotype data were generated using Illumina SNP chips, with imputation performed against the 1000 Genomes Project reference panel."* (Section: Paragraph 3, lines 27–32)
   * **Tag:** `[Methodologically Flawed]`
   * **Evidence & Audit:** This methods description is factually invalid on multiple levels:
     1. **Non-existent clinical phenotype in GDSC:** The Genomics of Drug Sensitivity in Cancer (GDSC) database comprises *in vitro* human cancer cell lines screened with anti-cancer compounds; it contains no childhood cancer survivors, no longitudinal clinical follow-up, and no human BMI or waist circumference measurements.
     2. **Internal contradiction with Ethics and Data statements:** Despite claiming in the first person (*"We analyzed... Genome-wide genotype data were generated..."*), no dataset accession numbers, sample sizes ($N$), allele frequencies, effect sizes ($\beta$ or odds ratios), or software pipelines are reported anywhere in the text, and the five SNPs listed in Paragraphs 5–7 are simply copied from a single published study (Ref. [2]: Wilson et al., 2015, *Cancer*, St. Jude Lifetime Cohort).

2. **Claim 2:** *"SNPs associated with obesity were identified through logistic regression models, adjusting for age, sex, and treatment exposures (e.g., cranial irradiation), with a significance threshold of $p < 5 \times 10^{-8}$ for genome-wide significance."* (Section: Paragraph 3, lines 32–34; Paragraphs 5–7, lines 38–50)
   * **Tag:** `[Methodologically Flawed]`
   * **Evidence & Audit:** Immediately after defining genome-wide significance at $P < 5 \times 10^{-8}$, the text reports five obesity-associated SNPs:
     * `rs12073359` ($P = 5 \times 10^{-6}$) — **100-fold above the stated threshold** ($5 \times 10^{-6} > 5 \times 10^{-8}$).
     * `rs4971486` ($P = 8 \times 10^{-8}$) — **fails the stated threshold** ($8 \times 10^{-8} > 5 \times 10^{-8}$).
     * `rs12646911` ($P = 1 \times 10^{-6}$) — **20-fold above the stated threshold** ($1 \times 10^{-6} > 5 \times 10^{-8}$).
     * `rs140236920` ($P = 1 \times 10^{-7}$) — **2-fold above the stated threshold** ($1 \times 10^{-7} > 5 \times 10^{-8}$).
     * `rs35669975` ($P = 3 \times 10^{-8}$) — the only variant meeting $P < 5 \times 10^{-8}$.
     Presenting four suggestive loci with $P \in [8 \times 10^{-8}, 5 \times 10^{-6}]$ as having met a $P < 5 \times 10^{-8}$ selection criterion is a direct mathematical contradiction.

3. **Claim 3:** *"Functional annotation of key SNPs was performed using bioinformatics tools to predict their impact on gene expression and regulatory networks... rs12073359 ($P = 5 \times 10^{-6}$) is associated with the RPL6P31 gene, which is involved in ribosomal protein synthesis... rs12646911 ($P = 1 \times 10^{-6}$) near the RNU6-649P gene... rs140236920 ($P = 1 \times 10^{-7}$) near the RPL36AP21 gene... rs35669975 ($P = 3 \times 10^{-8}$) associated with the PPIAP24 gene, which plays a role in protein folding and cellular stress responses."* (Section: Paragraphs 3, 5, 6, and 7)
   * **Tag:** `[Methodologically Flawed]`
   * **Evidence & Audit:** In standard HGNC human genome nomenclature, the suffix **`P`** followed by a number (`RPL6P31`, `RNU6-649P`, `RPL36AP21`, `PPIAP24`) designates an **unexpressed processed pseudogene** (e.g., *ribosomal protein L6 pseudogene 31*, *U6 small nuclear 649 pseudogene*, *ribosomal protein L36a pseudogene 21*, *peptidylprolyl isomerase A pseudogene 24*). None of these pseudogenes encode functional ribosomal proteins, spliceosomal RNAs, or cyclophilin chaperones; intergenic SNPs physically nearest to processed pseudogenes on linear genomic coordinates do not act by altering protein synthesis or protein folding via those pseudogenes.

4. **Claim 4:** *"Clinicians should consider incorporating genetic screening for identified variants into the survivorship care plans, enabling personalized risk assessments and early interventions."* (Section: Paragraph 8, lines 52–54)
   * **Tag:** `[Overstated]`
   * **Evidence & Audit:** Recommending clinical genetic screening in childhood cancer survivors based on five unvalidated, mostly suggestive ($P \sim 10^{-6}\text{--}10^{-8}$) non-coding variants near pseudogenes—without external replication, odds ratios, polygenic risk score calibration, or positive/negative predictive values—is clinically unsupported.

---

## Section 3: Technical Critique & Actionable Recommendations

### Major Methodological & Statistical Issues

1. **Fabricated/Hallucinated First-Person Methods and Misidentification of the GDSC Database (Pillar 1, Pillar 2, & Pillar 7):**
   * **Issue:** Paragraph 3 is written as if the authors executed an original GWAS across the Children's Oncology Group and the Genomics of Drug Sensitivity in Cancer (GDSC) project using Illumina arrays and 1000 Genomes imputation. Because no original analysis was performed and GDSC is a cell-line pharmacogenomics resource without human survivor anthropometrics, this section reads as synthetic/template-generated text.
   * **Remediation:** Completely remove the fabricated first-person methods in Paragraph 3. If the piece is intended as a commentary on published childhood cancer survivor GWAS (such as the St. Jude Lifetime Cohort study by Wilson et al. [2] and Sapkota et al.), state the exact cohort name, sample size ($N$), phenotype definitions, and statistical models of the cited primary papers accurately.

2. **Biological Misattribution of Processed Pseudogenes as Functional Protein-Coding Genes (Pillar 6):**
   * **Issue:** Attributing the functions of parent genes (*RPL6*, *RNU6*, *RPL36A*, *PPIA*) to intergenic processed pseudogenes (`RPL6P31`, `RNU6-649P`, `RPL36AP21`, `PPIAP24`) confuses linear nearest-feature genomic annotation with functional target genes.
   * **Remediation:** Replace the pseudogene functional claims with actual cis-eQTL, chromatin conformation (Hi-C/promoter capture), or regulome annotations showing which expressed protein-coding genes (e.g., *PROX1*, *FANCL*, or nearby hypothalamic/metabolic regulators) are regulated by these non-coding loci.

3. **Contradiction Between Stated $P < 5 \times 10^{-8}$ Threshold and Reported $P$-Values (Pillar 4):**
   * **Issue:** Four of the five variants reported have $P$-values between $8 \times 10^{-8}$ and $5 \times 10^{-6}$, violating the stated $P < 5 \times 10^{-8}$ cutoff.
   * **Remediation:** Explicitly distinguish between genome-wide significant loci ($P < 5 \times 10^{-8}$) and suggestive loci ($P < 10^{-5}$ or $10^{-6}$), and report the minor allele frequencies, odds ratios, and $95\%$ confidence intervals for each variant.
