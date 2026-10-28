# Blinded Review: SP_ANON_144
**Composite Score:** 9.2 / 10.0 (Rigor: 3.2/3.5 | Claims: 2.3/2.5 | Biology: 1.9/2.0 | Reproducibility: 1.8/2.0)
**Bias Category:** None (Methodologically Sound)
**Verdict:** Accept (Minor Revision)
**Study Modality:** Hybrid Computational + Wet-Lab Functional Validation
**Technology Maturity:** Mid-Stage High-Throughput
**Epistemic Stage:** Basic/Mechanistic Discovery

---

### 1. Executive Summary
This manuscript investigates the dynamics and timing of replication-competent HIV-1 latent reservoir formation in nine subtype C-infected women from the CAPRISA 002 cohort in South Africa who remained untreated for an average of 4.5 years before initiating suppressive antiretroviral therapy (ART) for an average of 5.0 years. By combining Primer ID error-corrected Illumina MiSeq deep sequencing of longitudinal pre-ART plasma viral RNA (averaging 9 time points per participant across 5 genomic regions in `gag`, `nef`, and `env`) with barcoded near-full-length Pacific Biosciences SMRT sequencing of replication-competent outgrowth viruses (OGVs) recovered via quantitative viral outgrowth assays (QVOA), the authors date the reservoir entry of 132 unique OGVs using three phylogenetic methods (patristic distance, clade support, and phylogenetic placement). They find that a mean of 71% (median 78%) of unique OGVs are genetically closest to plasma variants circulating in the final year before ART initiation, supporting a dynamical model in which latently infected resting CD4+ T cells turn over rapidly during untreated infection and stabilize into a long-lived reservoir upon ART-mediated viral suppression.

This is a methodologically rigorous, well-controlled study that resolves prior discrepancies between defective proviral DNA studies and replication-competent virus persistence. Minor limitations are restricted to small sample sizes in a subset of participants and a post-hoc visual adjustment step for 7 high-variance OGVs.

---

### 2. Methodological & Statistical Audit
* **Error-Corrected Deep Sequencing and Clonal Deduplication:** The pairing of Primer ID template consensus sequencing for longitudinal pre-ART plasma RNA (which eliminates PCR resampling and corrects sequencing/RT errors) with barcoded full-length PacBio sequencing of QVOA supernatants (empirically benchmarked at 1 error per 50,000 bases on 8E5 control cells) sets a high technical standard. Deduplicating identical/1-bp-differing OGV clones before estimating reservoir entry distribution prevents high-frequency clonally expanded T-cell lineages from artificially skewing the timing distribution, and the authors explicitly test and confirm that clonal OGVs do not differ significantly in late-entry frequency from unique OGVs (Fisher's exact test $P = 0.33$).
* **Multi-Locus Ensemble Phylogenetic Dating:** Combining three distinct phylogenetic estimators (patristic distance, bootstrap clade support, and maximum-likelihood phylogenetic placement) across up to five genomic regions and weighting estimates by leave-one-out RNA time-point recovery accuracy (`tree support`) guards against single-locus stochasticity and intra-host recombination.
* **Post-Hoc Manual Reassignment of High-Variance OGVs:** For 25 of 132 unique OGVs where individual locus/method estimates had a standard deviation $> 1$ year, the authors visually inspected trees and manually revised the weighted median assignment for 6 OGVs (mostly in participant CAP206) and marked 1 OGV as ambiguous. While transparently documented in the Methods and Figure 4, replacing an automated estimator with visual lineage assignment for a subset of discordant sequences introduces a subjective step. Reporting the overall cohort mean/median (71% / 78%) both with and without the 6 manual reassignments would demonstrate that the headline conclusion is invariant to manual curation.
* **Mathematical Decay Model Comparison:** The two-compartment exponential decay comparison (176-week half-life pre- and post-ART vs. 2-week half-life pre-ART stabilizing to 176 weeks on ART; Figure 5B) provides a clear mechanistic baseline, though the 2-week pre-ART half-life is illustrative rather than formally fitted to the empirical entry distributions (which also display inter-patient heterogeneity, as in CAP217 and CAP302).

---

### 3. Biological / Experimental Grounding & Claim Proportionality
* **Majority of Replication-Competent Reservoir Variants Date to the Year Prior to ART Initiation [Well Supported]:** Across the 9 participants, 71% (mean) and 78% (median) of unique OGVs cluster with plasma RNA from the final year pre-ART, vs. only 4% from the first year post-transmission. Even in participants with lower OGV yields (e.g., CAP287, CAP288, CAP302 with 6–8 total OGVs), the cohort-wide skewness toward pre-ART variants is robust.
* **Absence of Ongoing Viral Evolution During 5 Years of Suppressive ART [Well Supported]:** All recovered OGVs fell within pre-ART phylogenetic clades without excess root-to-tip divergence, confirming that the inducible replication-competent reservoir is maintained by cellular longevity and clonal proliferation rather than ongoing rounds of replication on ART.
* **Proposed IL-7 / CD127 Memory Transition Mechanism [Moderately Supported]:** The hypothesis that ART-induced reductions in immune activation restore CD127 expression and IL-7 responsiveness during the effector-to-memory transition is biologically plausible and well grounded in cited immunology literature, and is appropriately framed in the Discussion as a testable model rather than a demonstrated mechanism within this study.

---

### 4. Reproducibility & Data Completeness
* **Open Code and Sequence Repositories:** Full custom pipelines for Primer ID processing (`MotifBinner2`), NGS filtering (`NGS_processing_pipeline`), codon alignment (`BioExt`), and multi-method OGV dating (`veg/ogv-dating`) are publicly available on GitHub, and PacBio OGV sequences are deposited in GenBank (`MN097551–MN097697`).
* **Minor Editorial Note:** Provide the pre-ART Illumina MiSeq SRA/BioProject accession numbers alongside the GenBank OGV accessions so that independent researchers can reproduce the full pre-ART longitudinal phylogenies from raw reads.
