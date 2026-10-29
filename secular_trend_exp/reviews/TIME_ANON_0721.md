<Blinded Review: TIME_ANON_0721>
**Composite Score:** 8.0 / 10.0 (Rigor: 2.7/3.5 | Claims: 2.0/2.5 | Biology: 1.6/2.0 | Reproducibility: 1.7/2.0)
**Bias Category:** Statistical/Design
**Verdict:** Minor Revision
**Study Modality:** Hybrid Computational + Wet-Lab
**Technology Maturity:** Mid-Stage High-Throughput
**Epistemic Stage:** Translational/Preclinical/Biomarker

OVERALL_SCORE: 8.0/10
VERDICT: PASS
ESTIMATED_DECADE: 2010s

---

### SUMMARY
### 1. Executive Summary
This large-scale transcriptomic study characterizes the landscape of known and novel long non-coding RNAs (lncRNAs) across 216 human skin biopsies—99 lesional psoriatic (`PP`), 27 paired uninvolved psoriatic (`PN`), and 90 normal control (`NN`) skin samples—sequenced by polyA+ RNA-seq (~40 million reads/sample; `GSE63980`). Using `TopHat v1.3.3` alignment, `Cufflinks v2.1.1` ab initio assembly, Ensembl v74 annotation, and stringent multi-step filtering (expression in $\ge 11$ samples, $\ge 2\text{ kb}$ distance from any known exon, 35-mer uniqueness and 75-mer alignability $\ge 0.9$, length $\ge 200\text{ bp}$, $\ge 216$ total reads, and non-coding verification via `TransDecoder` and `txCdsPredict`), the authors identify 4,022 skin-expressed lncRNAs: 2,942 previously annotated and 1,080 novel lncRNAs. Using `DESeq`, BodyMap 2.0 cross-tissue comparisons, ENCODE chromatin-state enhancer/promoter segmentation across nine cell lines, co-expression guilt-by-association ($r_s^2 \ge 0.5$), qRT-PCR validation in 18 independent biopsies (`6 PP, 6 PN, 6 NN`), and RNA-seq of `IL-17 + TNF`-stimulated primary human keratinocytes, they show that novel skin lncRNAs are enriched at the Epidermal Differentiation Complex (`EDC`, `1q21.3`), map closer to `NHEK`/`HMEC` ectodermal enhancers (`elncRNAs`), and are co-expressed with immune and lipid-metabolic genes dysregulated in psoriasis.

---

### STRENGTHS
- **Large Primary Clinical Cohort ($N = 216$) with Split-Cohort and Orthogonal qRT-PCR Validation:** Over 95% of novel lncRNAs discovered in the initial 174-sample subset replicated in the independent 42-sample subset, and top candidate lncRNAs (`G2608` in the `EDC`, `G25746`, and `G36220` at the `TNFAIP3` locus) were validated by qRT-PCR in 18 independent skin biopsies (`6 PP, 6 PN, 6 NN`).
- **Stringent Stepwise Artifact Filtering (`Table 1`):** Explicitly filters out pre-mRNA 5'/3' extension fragments ($<2\text{ kb}$ from known exons, removing $>50\%$ of raw intronic/interleaving candidates), low-mappability repeats, short fragments ($<200\text{ bp}$), and coding ORFs (`TransDecoder`/`txCdsPredict`).
- **Integrative Epigenomic (`ENCODE`) and Cytokine-Stimulation (`IL-17 + TNF`) Grounding:** Connects skin-expressed novel lncRNAs to ectodermal keratinocyte (`NHEK`) enhancer chromatin states and demonstrates significant enrichment of `IL-17 + TNF`-inducible keratinocyte lncRNAs among psoriasis-upregulated lncRNAs.

---

### WEAKNESSES & METHODOLOGICAL AUDIT
### 2. Methodological & Statistical Audit
- **Discovery Ascertainment Bias Inflates Apparent Skin-Specificity ($T_s$) and Differential Expression Rate (47% vs. 24%) of "Novel" vs. Annotated lncRNAs:** Because "novel" lncRNAs are defined by their absence from Ensembl v74 (which was heavily populated from multi-tissue normal reference panels such as BodyMap 2.0 and ENCODE) and are assembled de novo from a cohort consisting of 46% inflamed psoriatic lesions (`99/216 PP`), housekeeping and multi-tissue lncRNAs are systematically pre-classified as "annotated," leaving skin-restricted and psoriasis-induced transcripts enriched in the "novel" bin. Consequently, testing whether novel lncRNAs have higher skin specificity in BodyMap 2.0 ($p < 2.2 \times 10^{-16}$) or higher `PP vs. NN` differential expression ($47\%$ vs. $24\%$, Fisher's exact $p = 7 \times 10^{-103}$) partly reflects circular selection conditioning (as supported by the authors' own observation in the Discussion that conditioning annotated mRNAs and lncRNAs on high skin specificity $T_s > 0.4$ raises their DE proportions to 46% and 38%, respectively).
- **Unpaired Differential Expression Modeling of Paired `PP`/`PN` Samples and Unstranded PolyA+ Sequencing:** Although the 27 uninvolved (`PN`) biopsies were paired with 27 lesional (`PP`) biopsies from the same individuals, the `PN vs. PP` comparison was analyzed with `DESeq` (which lacks a paired multi-factor generalized linear model design, unlike `DESeq2` or `edgeR`) across all 99 `PP` vs. 27 `PN` samples. Furthermore, unstranded polyA+ RNA-seq misses non-polyadenylated lncRNAs and cannot determine strand orientation for mono-exonic novel intergenic lncRNAs that lack `GU/AG` splice junctions.
- **Bulk Tissue Cellularity Shifts Confound Co-Expression Functional Imputation:** Computing gene–lncRNA Spearman correlations ($r_s^2 \ge 0.5$) across pooled `NN` and `PP` biopsies conflates intracellular transcriptional co-regulation with massive cell-type proportion differences between normal and lesional skin (epidermal hyperplasia, dermal compression, and T-cell/myeloid infiltration).

### 3. Biological / Experimental Grounding & Claim Proportionality
- **Claim 1:** *"Over 1,000 novel skin-expressed lncRNAs are reproducibly detected in human skin biopsies, enriched in the Epidermal Differentiation Complex (1q21.3) and near keratinocyte enhancers (`elncRNAs`)."* — **[Well Supported]**. Backed by rigorous mappability/distance filtering, ENCODE `NHEK` chromatin segmentation, and independent cohort replication.
- **Claim 2:** *"Over 40% of novel lncRNAs are differentially expressed in psoriasis lesions and co-expressed with immune and lipid-metabolic pathways."* — **[Moderately Supported]**. Statistically robust at the bulk tissue level, though partly driven by discovery ascertainment in `PP` samples and bulk immune-infiltrate composition shifts.

### 4. Reproducibility & Data Completeness
- **Exemplary Data Availability and Primer Reporting:** All 216 skin RNA-seq and keratinocyte cytokine-stimulation datasets are publicly deposited in NCBI GEO under superseries `GSE63980` (`GSE54456` and `GSE63979`), and all qRT-PCR primer sequences are provided in the Materials and Methods.
</Blinded Review: TIME_ANON_0721>
