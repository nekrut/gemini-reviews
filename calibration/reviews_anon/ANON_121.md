# Review of ANON_121

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **8.9 / 10.0** (Strong / Sound)  
* **Score Breakdown:** Rigor: 3.0/3.5 | Claims: 2.2/2.5 | Biology: 1.9/2.0 | Reproducibility: 1.8/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript systematically quantifies rates of ongoing adaptive evolution across 239 genes spanning 28 endemic human pathogenic viruses (10 viral families) to determine how widely antigenic evolution occurs among human viruses. Extending the temporal McDonald–Kreitman (MK) framework of Williamson (2003) and Bhatt et al. (2011), the authors introduce an updated-outgroup procedure that records sequential fixations at the same codon/nucleotide site across 5-year sliding windows, preventing saturation underestimation in rapidly evolving surface proteins such as influenza A/H3N2 HA1. Calibrating a threshold of ongoing adaptive evolution ($1.17 \times 10^{-3}$ adaptive mutations per codon per year) against known antigenically evolving and antigenically stable viruses, they find that 14 of 239 viral genes exceed this threshold—13 of which encode surface-exposed proteins (10 receptor-binding proteins/subunits and 3 influenza neuraminidase proteins)—identifying 10 endemic RNA viruses (influenza A/H3N2, A/H1N1pdm, B/Victoria, B/Yamagata, RSV-A, RSV-B, coronaviruses 229E and OC43-A, norovirus GII.4, and enterovirus D68) undergoing continuous antigenic adaptation. Using root-to-tip amino acid substitution regressions, they further show that SARS-CoV-2 S1 evolves 2–2.5× faster than influenza A/H3N2 HA1 and 7–10× faster than endemic seasonal coronaviruses. All Nextstrain/Snakemake pipelines, sequence alignments, Jupyter notebooks, and an interactive visualization portal (`blab.github.io/atlas-of-viral-adaptation/`) are openly archived on GitHub and Mendeley Data (`doi:10.17632/cj4n8m9kk4.1`).

This is a well-executed comparative evolutionary genomics study with exemplary open-science practices and a strong internal biological control (contrasting surface receptor-binding proteins against viral polymerases across all 28 viruses). The main methodological caveats are: (1) the binary threshold of antigenic evolution ($1.17 \times 10^{-3}$ adaptive substitutions/codon/year) is fit via logistic regression on only $N = 6$ linearly separable viruses, and the text contains a direct discrepancy between the Results (which lists influenza B/Yamagata) and the STAR Methods (which lists influenza B/Victoria) as one of the three positive calibration viruses; (2) the linear regression slope across overlapping 5-year windows (offset by 1 year) treats serially autocorrelated cumulative counts as unweighted observations, with codon-bootstrap intervals reflecting across-site variance rather than evolutionary process variance; and (3) comparing short-timescale root-to-tip amino acid substitution slopes in SARS-CoV-2 (1–3 years) against multi-decadal slopes in endemic viruses (12–54 years) is partially influenced by the time-dependent rate phenomenon (incomplete purifying selection on terminal branches). These issues can be addressed through straightforward sensitivity analyses and textual reconciliation.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Updating the outgroup sequence upon fixation corrects underestimation of adaptation rates in rapidly evolving viral proteins with recurrent site fixations: [Well Supported].**  
  In influenza A/H3N2 HA1, 12 of 92 fixed nonsynonymous sites experienced multiple sequential fixations between 1968 and 2022, causing the constant-outgroup Bhatt estimator to asymptote prematurely (Fig. 1A, 1C), whereas seasonal coronavirus 229E S1 (0 recurrently fixed sites) yields identical slopes under both estimators (Fig. 1D, 1F). This modification directly addresses a known multiple-hit limitation of alignment-based temporal MK estimators.

* **Across 239 genes in 28 endemic viruses, ongoing adaptive evolution above $1.17 \times 10^{-3}$ mutations/codon/year is concentrated in surface receptor-binding proteins of 10 RNA viruses and correlates with influenza vaccine strain update frequencies: [Well Supported].**  
  The contrast between viral polymerases ($0.0\text{--}0.7 \times 10^{-3}$ adaptive mutations/codon/year across all 28 viruses) and receptor-binding proteins ($0.0\text{--}5.7 \times 10^{-3}$; Fig. 4), the localization of 13 of 14 rapidly adapting genes to virion surfaces (Fig. 3B), and the monotonic alignment between HA1 adaptation rates and WHO vaccine updates from 2012–2023 across H3N2, H1N1pdm, B/Vic, and B/Yam (Fig. 2B) provide strong, internally consistent support.

* **A logistic regression on six benchmark viruses reliably establishes $1.17 \times 10^{-3}$ mutations/codon/year as the decision threshold for antigenic evolution: [Fragile].**  
  In a dataset of $N = 6$ observations (3 positive, 3 negative) with complete separation between the two classes (Fig. 2A), unpenalized maximum-likelihood logistic regression does not have a finite unique slope estimate, and its decision boundary is determined solely by the two boundary points (the highest negative virus and lowest positive virus) and numerical stopping/regularization settings. Furthermore, the manuscript contradicts itself on which positive boundary virus was used: Results (Section "Estimation of the threshold...", Paragraph 2) states *"influenza viruses A/H3N2 and B/Yam [11] and coronavirus 229E"*, whereas STAR Methods ("Estimation of threshold, using logistic regression") states *"influenza A/H3N2 HA1, influenza B/Vic HA1, and coronavirus 229E S1."* Because B/Yam ($1.4 \times 10^{-3}$) and B/Vic ($1.8 \times 10^{-3}$) lie near the boundary, swapping them directly shifts the midpoint threshold.

* **SARS-CoV-2 S1 accumulates amino acid substitutions 2–2.5× faster than influenza A/H3N2 HA1 and 7–10× faster than seasonal coronaviruses 229E and OC43, including within Omicron clade 21L: [Moderately Supported].**  
  The root-to-tip regression slopes in Fig. 5 clearly show rapid amino acid accumulation in SARS-CoV-2 S1 ($\sim 20 \times 10^{-3}$ substitutions/residue/year), both globally and within Omicron clade 21L (BA.2 and descendants). However, unlike the MK estimator (which filters out low-frequency polymorphisms below $15\%$ and weights fixations above $75\%$), root-to-tip tip distances include terminal-branch mutations and transient segregating polymorphisms. Because the SARS-CoV-2 regressions span only 3 years (Fig. 5A) or ~1.2 years (Omicron 21L, Fig. 5B) compared to 12–54 years for the endemic viruses, a portion of the elevated root-to-tip slope reflects short-timescale polymorphism inflation and clonal interference among co-circulating sublineages (BA.5, BQ.1, XBB.1.5) rather than long-term lineage fixation rate alone.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Reconcile the B/Yam vs. B/Vic Discrepancy and Replace the $N=6$ Logistic Threshold with a Non-Parametric Empirical Null Distribution
* **WHY:** Fitting a logistic regression to $N=6$ completely separated data points is statistically degenerate, and the text contradicts itself regarding whether influenza B/Yamagata (Results, line 50) or B/Victoria (STAR Methods, line 13) was used as the third positive control.
* **WHAT:** Reconcile the text and code regarding B/Yam vs. B/Vic, and supplement the $N=6$ midpoint threshold with an empirical $95\%$ or $99\%$ upper quantile derived from the 174 non-surface (internal) proteins across the 28 viruses.
* **HOW:** Check `adaptive-evolution-analysis/` to confirm whether B/Yam or B/Vic was passed to the logistic regression and update the text so Results and STAR Methods match. In addition, compute the $99\text{th}$ percentile of estimated adaptation rates across the 174 non-surface proteins (Fig. 3B, right panel) as an internal genome-wide null threshold for background non-antigenic adaptation, and show that the same 13 surface proteins exceed this empirical internal-protein bound.

#### 2. Control for Terminal-Branch Polymorphisms When Comparing SARS-CoV-2 S1 to Endemic Viruses
* **WHY:** Root-to-tip regressions over a 1–3 year window (Fig. 5A–B) include deleterious or neutral singleton/terminal-branch substitutions that have not yet been purged or fixed, inflating short-term molecular clock slopes relative to 30–50 year regressions (Fig. 5C–L).
* **WHAT:** Re-compute the amino acid substitution rates in Fig. 5 restricting exclusively to *internal branches* (or trunk branches) of the time-resolved TreeTime phylogenies.
* **HOW:** In the Python root-to-tip traversal script, exclude mutations occurring on terminal tip branches (or restrict to internal nodes with $\ge 5$ descendant tips) for SARS-CoV-2, Omicron 21L, and the 10 endemic viruses, and report the internal-branch amino acid substitution rate alongside the full root-to-tip slope.

#### 3. Evaluate Sensitivity to Overlapping Temporal Windows and Minimum Window Sample Size ($n \ge 3$)
* **WHY:** Partitioning alignments into 5-year windows offset by 1 year creates 80% overlap between adjacent windows, and allowing windows with as few as $n = 3$ sequences means that a single sequence in a sparse historical window carries a $33.3\%$ frequency weight (exceeding the $15\%$ polymorphism cutoff) while 3 of 3 sequences ($100\%$) trigger a "fixation" event ($>75\%$) that permanently updates the outgroup list.
* **WHAT:** Test the sensitivity of the updated-outgroup estimator to non-overlapping windows and stricter minimum sample-size thresholds per window.
* **HOW:** Re-run `rate_of_adaptation.ipynb` requiring at least $n \ge 10$ sequences per window (or requiring fixations to persist across two consecutive non-overlapping windows before appending to the updated outgroup list) and report the correlation with the baseline rates in a supplementary figure.

#### 4. Technical, Mathematical, and Editorial Cleanup
* **WHY:** Minor figure numbering and typographical inconsistencies appear between the main text and STAR Methods.
* **WHAT & HOW:**
  1. **Results (line 107) vs. End of Manuscript (line 38 of part 2):** In Results (Section "Comparison of rates of evolution...", Paragraph 3), the text refers to *"Figure S3 lists the rate of amino acid substitution and the rate of adaptation in the receptor-binding protein of each virus"*, whereas at the end of the manuscript this figure is titled *"Figure 6. Comparison of rates of amino acid substitution to rates of adaptation."* Harmonize the label to either `Figure 6` or `Supplementary Figure S3` throughout.
  2. **Discussion (Paragraph 2, line 114):** Fix typos *"fasting-evolving"* $\to$ *"fastest-evolving"* and *"especially striking its pace"* $\to$ *"especially striking in its pace"*.
  3. **Key Resources Table (lines 48–89 of part 2):** Remove the blank template rows under `Antibodies`, `Bacterial and virus strains`, `Biological samples`, `Chemicals`, and `Critical commercial assays` or populate them with `"N/A"`.
