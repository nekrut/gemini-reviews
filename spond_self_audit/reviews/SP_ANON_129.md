# Blinded Review: SP_ANON_129

**Composite Score:** 8.4 / 10.0 (Rigor: 3.1/3.5 | Claims: 2.3/2.5 | Biology: 1.6/2.0 | Reproducibility: 1.4/2.0)
**Bias Category:** None (Methodologically Sound)
**Verdict:** Accept
**Study Modality:** Dry-Lab Theory/Methods/Simulation
**Technology Maturity:** Mature/Classical
**Epistemic Stage:** Basic/Mechanistic Discovery

---

## 1. Executive Summary

This concise correspondence/commentary provides a forensic phylogenetic and epidemiological refutation of Forster et al. (2020), who applied a distance-based median-joining network (MJN) rooted on the divergent bat sarbecovirus RaTG13 to 160 early SARS-CoV-2 genomes and claimed to identify three ancestral/adaptive human viral types ("A, B, and C"). The authors identify three fatal errors in Forster et al.'s study: (1) rooting an intraspecific parsimony network with a distantly related outgroup (~3.8% nucleotide divergence, >1,100 substitutions) without substitution-model correction, which caused catastrophic long-branch misrooting; (2) conflating single founder mutations with immunological or environmental adaptation; and (3) ignoring extreme geographic and temporal ascertainment bias in early GISAID submissions. Every point raised in this critique is mathematically and biologically sound.

---

## 2. Methodological & Statistical Audit

* **Outgroup Misrooting in Distance-Based Median-Joining Networks:** The authors pinpoint the exact mathematical failure mode of Forster et al.'s rooting strategy. Because `RaTG13` differs from SARS-CoV-2 by >1,100 nucleotides (compressed to 16–17 characters in Forster et al.'s filtered network), homoplasy and transitional saturation along the ~30–50 year branch separating `RaTG13` from SARS-CoV-2 randomize the polarization of the single T28144C (`ORF8` L84S) site separating Cluster A and Cluster B. As the authors note, this misrooting produced the chronological absurdity in Forster et al.'s network where the earliest Wuhan genome (`Wuhan/IPBCAMS-WH-01/2019`, collected December 24, 2019) was inferred to be a descendant of non-Chinese genomes sampled in Weeks 1–9 of 2020.
* **Neutral Founder Effects vs. Selection Inference:** The critique rightly highlights that Forster et al. performed zero formal tests of natural selection (e.g., $dN/dS$, branch-site likelihoods, or fitness assays) before claiming that "type B" (defined by one synonymous mutation C8782T and one nonsynonymous mutation T28144C) was "immunologically or environmentally adapted to a large section of the East Asian population." In a rapidly expanding epidemic seeded by serial demographic bottlenecks, neutral or mildly deleterious hitchhiking alleles routinely reach high regional frequencies by founder drift alone.
* **GISAID Sampling Ascertainment Bias:** The authors document that early GISAID depositions severely under-sampled Hubei province relative to travel-associated exports in Europe, North America, and Guangdong, invalidating raw node-count interpretations of ancestral geographic origin in unweighted networks.

---

## 3. Biological / Experimental Grounding & Claim Proportionality

* **`[Well Supported]` Inappropriateness of Uncorrected Median-Joining Networks with Distant Outgroups for Viral Phylodynamics:** The methodological conclusion that MJNs neither model substitution rate heterogeneity nor incorporate molecular clock information—and therefore fail to polarize epidemic roots using distant animal outgroups—is completely supported by phylogenetic theory and the empirical chronology of Wuhan cases.
* **`[Well Supported]` Refutation of Adaptive East Asian Host Specialization of "Type B" SARS-CoV-2:** The refutation of Forster et al.'s adaptation narrative is rigorous, proportional, and essential for preventing misinterpretation by public health and lay audiences.

---

## 4. Reproducibility & Data Completeness

* **Format & Transparency:** As a brief letter/commentary critiquing a published paper's methodology, it generates no new primary datasets or software, and all referenced sequences and dates are directly verifiable from the public GISAID records discussed in the text.
