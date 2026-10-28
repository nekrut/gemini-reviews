# Review of ANON_29

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **8.4 / 10.0** (Strong / Sound)  
* **Score Breakdown:** Rigor: 2.8/3.5 | Claims: 2.3/2.5 | Biology: 1.7/2.0 | Reproducibility: 1.6/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript proposes a dynamic, hierarchical phylogenetic nomenclature system (`Pango` lineages) for tracking actively circulating lineages of SARS-CoV-2 at scale, demonstrated on 27,767 complete genomes downloaded from GISAID on May 18, 2020. Starting from two basal lineages at the root of the pandemic (denoted A and B, distinguished by nucleotides at positions 8782 and 28144), the framework assigns numerical sub-lineage suffixes (up to three hierarchical sublevels, e.g., `A.1.1.1`, before aliasing to the next alphabetical letter `C.1`) to monophyletic clades that exhibit epidemiological spread into geographically distinct populations, contain at least five high-coverage genomes (>95% coding coverage), share at least one defining internal nucleotide substitution, and achieve >70% bootstrap support. Lineages are dynamically flagged as `active` (<1 month since last sampling), `unobserved` (1–3 months), or `inactive` (>3 months) to keep the number of active labels tractable. The curated maximum-likelihood phylogeny, lineage definitions, and automated assignment software (`pangolin` and `cov-lineages.org`) are publicly available.

This is a clear, well-conceived, and highly practical classification framework that solves an urgent epidemiological communication problem while carefully avoiding premature claims of phenotypic or antigenic divergence among early SARS-CoV-2 lineages. The primary limitations are minor internal inconsistencies and operational edge cases in the low-diversity regime of SARS-CoV-2: (1) an internal textual contradiction between the *Principles* section (which states that many earliest Hubei cases are identical to the root sequence) and the *Lineage naming rules* section (which places the root in Lineage A rather than the earlier-sampled Lineage B reference `Wuhan-Hu-1`); (2) relying on a $>70\%$ `IQ-TREE 2` ultrafast bootstrap (`UFBoot`) threshold on single-substitution branches where `UFBoot` is known to be either over-liberal (standard `UFBoot` requires $\ge 95\%$) or undefined due to polytomies, necessitating ad hoc manual overrides; and (3) a typographical hierarchy error in the main text describing `A.3` as a sub-lineage of `A.1`. Clarifying the `UFBoot` vs. synapomorphy support criteria and resolving the textual inconsistencies will strengthen the specification.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Claim 1: Constraining hierarchical depth to three numerical sublevels with alphabetical aliasing and activity-based retirement yields a scalable nomenclature for hundreds of thousands of SARS-CoV-2 genomes. [Well Supported]**  
  Applied to 27,767 genomes, the rules partition global diversity into 81 manageable lineages (primarily within A, B, and B.1) that directly map major epidemiological expansions (e.g., `A.1` in Washington State, `B.1`/`B.2` in northern Italy and Europe, `B.4` in Iran; Table 1). Capping depth at three dot-levels with alphabetical aliasing (`C`, `D`, ...) prevents indefinite label growth during prolonged serial replacement, and explicit accommodation of future recombinants via new alphabetical prefixes (line 85) is forward-looking and biologically sound.

* **Claim 2: The proposed four quantitative phylogenetic criteria (including >70% bootstrap support) objectively delineate emerging SARS-CoV-2 lineages. [Moderately Supported]**  
  Criteria (a)–(c) (≥1 shared difference from ancestor, ≥5 genomes with >95% coverage, and ≥1 shared internal substitution indicating onward transmission) are well suited to outbreak tracking. However, criterion (d)—requiring *"a bootstrap value >70% for the lineage defining node"* estimated via 1,000 `IQ-TREE 2` ultrafast bootstrap (`UFBoot`) replicates (lines 40, 92)—has two technical caveats. First, `UFBoot` support values are not equivalent to standard non-parametric Felsenstein bootstrap proportions; the `IQ-TREE` authors establish that `UFBoot` $\ge 95\%$ corresponds roughly to a $95\%$ probability that a clade is true, whereas a $70\%$ threshold is the traditional cutoff for standard non-parametric bootstrapping. Second, in SARS-CoV-2 alignments where lineage-defining branches often span a single nucleotide substitution out of ~29,900 sites (~99.97% invariant sites per branch), bootstrap resampling either drops or duplicates that single site, producing noisy support values around ~63% and forcing the authors to manually override criterion (d) for major lineages such as `B.1` and `B.2` (line 54).

* **Claim 3: Query genomes with >70% coding region coverage can be reliably assigned to defined lineages. [Moderately Supported]**  
  While requiring >95% coverage to *define* a new lineage (line 40) and relaxing the threshold to >70% coverage to *assign* a query genome (line 83) is a reasonable operational compromise for clinical surveillance, a genome missing up to 30% of its coding sequence (~9 kb) will frequently lack coverage at the specific 1–3 diagnostic SNPs that distinguish nested sub-lineages (e.g., `B.1.x`), causing incomplete sequences to collapse back to the parent lineage (`B` or `B.1`) under step IV (line 46).

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Reconcile the Ultrafast Bootstrap Threshold with Single-Substitution Synapomorphy Support
* **WHY:** `IQ-TREE 2` ultrafast bootstrap (`UFBoot`) values at 70% are statistically anti-conservative compared to standard non-parametric bootstraps, yet on single-SNP SARS-CoV-2 branches even genuine clades without homoplasy frequently fall below 70% bootstrap support simply because only 1 site out of 29,903 is informative.
* **WHAT:** Replace or supplement criterion (d) (`bootstrap > 70%`) with an explicit homoplasy/consistency check on the defining nucleotide substitution(s) (e.g., retention index or absence of conflicting characters), and clarify that `UFBoot` values differ from standard non-parametric bootstrap proportions.
* **HOW:** In the *Lineage naming rules* (line 40) and *Methods* (line 92), specify whether criterion (d) is evaluated using standard non-parametric bootstrap (`-b`) or `UFBoot` (`-bb` / `-B`), or define node support in terms of the presence of $\ge 1$ non-homoplasious defining synapomorphy shared by $\ge 95\%$ of descendant tips.

#### 2. Quantify the Sensitivity of Lineage Assignment to Missing Data at the 70% Coverage Threshold
* **WHY:** Because early SARS-CoV-2 lineages are separated by only 1–3 mutations, a query sequence with 70%–90% coverage (typical of high-Ct amplicon dropout samples) may have `N`s at the exact lineage-defining positions, leading to systematic basal fallbacks under rule IV.
* **WHAT:** Briefly state how `pangolin` / the assignment rules handle `N`s at lineage-defining sites (e.g., imputation vs. basal fallback to parent lineage) and report the empirical call accuracy at 70% vs. 95% coverage.
* **HOW:** Mask random amplicon tiles (up to 30% of the coding region) in a test set of 1,000 complete genomes from Table 1 and report the proportion of sequences that are assigned to the correct terminal sub-lineage vs. falling back to the parent lineage (`A`, `B`, or `B.1`).

#### 3. Technical and Editorial Cleanup
* **WHY:** Two internal contradictions in the main text regarding the pandemic root sequence and the `A.1` sub-lineage labels can confuse readers implementing the nomenclature.
* **WHAT & HOW:**
  * **Root Sequence Contradiction (Line 25 vs. Line 36):** In line 25, the authors state: *"because of the early sampling and genome sequencing of COVID-19 cases in China, especially in Hubei province, it appears that the 'root sequence' of SARS-CoV-2 is known. Many of the genomes from the earliest sampled cases are genetically identical and hence also likely identical to the most recent common ancestor of all sampled viruses. ... setting the 'reference sequence' to be the 'root sequence' forms a natural starting point"*. However, in line 36 and Table 1 (line 65), the authors state that the earliest sequenced Hubei cases (including the reference `Wuhan-Hu-1`, sampled 2019-12-26) belong to derived Lineage B, whereas the root of the SARS-CoV-2 phylogeny lies in Lineage A (`Wuhan/WH04/2020`, sampled 2020-01-05). Revise line 25 to distinguish the *reference sequence* (`Wuhan-Hu-1`, Lineage B) from the *putative root sequence* (Lineage A or the A/B ancestor) so that lines 25 and 36 are consistent.
  * **Sub-lineage Label Typo (Line 54):** Fix *"We identified six lineages derived from lineage A (denoted A.1-A.6) and two descendant sub-lineages of A.1 (**A.1.1 and A.3**)"*. Since `A.3` is already one of the six primary descendant lineages of `A` (`A.1–A.6`, Table 1 line 68), the second sub-lineage of `A.1` should be `A.1.2` (or `A.1.1` only).
