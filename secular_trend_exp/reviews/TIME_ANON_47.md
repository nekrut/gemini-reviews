# Blinded Review: TIME_ANON_47
**Composite Score:** 3.8 / 10.0 (Rigor: 1.0/3.5 | Claims: 0.8/2.5 | Biology: 0.9/2.0 | Reproducibility: 1.1/2.0)
**Bias Category:** Long-Branch Attraction & Spatial Rate Heterogeneity Misinterpreted as Ancient Recombination
**Verdict:** Reject
**Study Modality:** Dry-Lab Secondary Cohort/Database Re-Analysis
**Technology Maturity:** Mature/Classical
**Epistemic Stage:** Basic/Mechanistic Discovery

---

### 1. Executive Summary

This manuscript analyzes an $\sim 13.6\ \text{kb}$ region of the SARS coronavirus (`SARS-TOR2`, positions 7,349–20,969, spanning the C-terminus of ORF1a and ORF1b) aligned at the nucleotide level against 10 reference sequences representing coronavirus Groups I (*Alphacoronavirus*: `229E`, `PEDV`, `TGEV`), II (*Betacoronavirus*: `MHV` strains, `BCoV` strains), and III (*Gammacoronavirus*: avian infectious bronchitis virus `AIBV` strains). After removing unalignable regions to create 13 sub-alignments (245–3,785 bp), the authors run the sliding-window maximum-likelihood spatial heterogeneity program PLATO and reconstruct unrooted 4-lineage phylogenies (ML, Bayesian, NJ, MP) on sub-segments. They report five putative recombinant regions (ranging from 83 bp to 863 bp in *RdRp*, *nsp9*, *nsp10*, and *nsp14*) where `SARS-TOR2` branches with Group I or Group III instead of Group II, concluding that SARS-CoV arose via host-jumping and recombination/reassortment between avian (Group III) and mammalian (Group I) coronaviruses analogous to influenza A virus.

The study's core conclusions are methodological artifacts resulting from applying a spatial likelihood-ratio scan (PLATO) and short-window unrooted quartet phylogenetics (`83 bp` to `863 bp`) to deeply divergent viral genera separated by saturated nucleotide distances. In a 4-clade unrooted tree with extreme branch lengths separating Alpha-, Beta-, and Gammacoronaviruses and `SARS-TOR2` branching near the base of Group II, local spatial conservation/variability across enzyme domains triggers PLATO false positives, and short alignments of 27 to 45 codons suffer from severe long-branch attraction (LBA) and stochastic sampling error. Furthermore, three of the five claimed recombinant regions did not even reach statistical significance in PLATO, and the authors repeatedly conflate homologous RNA recombination with segmented viral "reassortment."

---

### 2. Methodological & Statistical Audit

* **Vulnerability of PLATO to Spatial Substitution Rate Heterogeneity Across Deeply Divergent Genera:**
  PLATO (Grassly and Holmes) calculates the likelihood of a sliding window (from 5 bp up to half the alignment length) under a single global reference tree topology and a uniform HKY substitution model without among-site rate variation ($\Gamma$) in the scan step. When applied to an inter-genus alignment of Group I, II, and III coronaviruses across *ORF1ab*, distinct functional subdomains (e.g., catalytic motifs of RdRp vs flexible surface loops) evolve under vastly different purifying selection intensities and local transition/transversion biases. Because PLATO measures anomalies in regional likelihood relative to the average evolutionary rate of the alignment, any locally conserved or locally diverged motif generates a high $Z$-score even when the underlying tree topology is completely invariant.

* **Long-Branch Attraction and Stochastic Sampling Noise in Tiny Alignment Windows (83–285 bp):**
  The two main PLATO-flagged regions supporting the authors' claims are positions `15,259–15,342` (**84 bp / 28 codons** in *RdRp*) and `15,974–16,108` (**135 bp / 45 codons** in *RdRp*). Reconstructing an unrooted tree of 4 deep clades (Group I, Group II, Group III, and `SARS-TOR2`) means there are only **three possible unrooted quartet topologies**:
  1. $(\text{SARS}, \text{Group II}) \mid (\text{Group I}, \text{Group III})$ (the control tree, Fig. 1a),
  2. $(\text{SARS}, \text{Group III}) \mid (\text{Group I}, \text{Group II})$ (Fig. 1b), and
  3. $(\text{SARS}, \text{Group I}) \mid (\text{Group II}, \text{Group III})$ (Fig. 1c).
  Because the internal central branch separating `SARS-TOR2` + Group II from Groups I and III is short relative to the long terminal branches leading to `SARS-TOR2`, Group I, and Group III, a window of 28 to 45 codons contains only a handful of parsimony-informative sites across the central split. Under these conditions, site-specific compositional bias, covarion shifts, or 2–3 convergent amino acid substitutions are sufficient to flip the unrooted quartet from topology (1) to topology (2) or (3) with inflated Bayesian posterior probabilities (which are well known to overstate confidence on short, misspecified alignments).

* **Post-Hoc Selection of Non-Significant PLATO Regions (`[Methodologically Flawed]`):**
  In Results and Discussion, the authors report five recombinant regions (Fig. 1d), but admit that **three of the five regions (`12,613–13,344`, `13,392–13,610`, and `18,117–18,980`) did not yield significant PLATO $Z$-scores**! They rationalize this by arguing that *"simply because the entire (or very nearly) alignment appears to represent a recombinant zone (i.e. nothing for PLATO to identify as anomalous; Fig. 1d)."* Meanwhile, the third region that *did* yield a significant PLATO score (`19,577–19,862`, $Z = 6.16$) failed to show consistent phylogenetic placement (bootstrap $<60\%$, posterior probability $<0.50$). Thus, out of the 13 manual gap-trimmed sub-alignments, PLATO and phylogenetic trees only agreed on two tiny windows (84 bp and 135 bp), while the remaining claims rely on post-hoc visual selection of sub-alignment gene trees.

* **Improper Dismissal of Synonymous Saturation:**
  Across coronavirus genera (Group I vs II vs III), synonymous third-codon positions are completely saturated ($d_S \gg 2.0$ substitutions per site). Performing primary alignment and PLATO scanning on raw DNA sequences across genera introduces severe noise from randomized third-position bases. While the authors state that removing third codon positions or using amino acids yielded identical topologies for the flagged zones, they did not re-run PLATO or parametric bootstrap simulations under a codon or amino-acid covarion model to test whether the observed quartet conflicts exceed expectations under lineage-specific rate variation without recombination.

---

### 3. Biological / Experimental Grounding & Claim Proportionality

* **Conflation of Homologous RNA Recombination with Influenza Segment "Reassortment": `[Methodologically Flawed]`**
  In the Abstract, the authors state that their findings are *"consistent with a hypothesis of viral host jumping events, concomitant with the reassortment of bird and mammalian coronaviruses, a scenario analogous to earlier outbreaks of influenzae."* Reassortment is the shuffling of discrete genomic RNA segments during co-infection by segmented viruses (such as Orthomyxoviruses, Reoviruses, or Bunyaviruses). Coronaviruses possess a single, non-segmented positive-sense RNA genome (~30 kb) and evolve via template-switching homologous recombination, not segment reassortment.

* **Claim that SARS-CoV Is a Mosaic of Avian (Group III) and Porcine/Mammalian (Group I) Coronaviruses: `[Overstated]`**
  As the authors themselves note in passing, in every putative anomalous window, `SARS-TOR2` never nests *inside* crown Group I or crown Group III; rather, the unrooted quartet simply resolves the deep internal branch in one of the two alternative arrangements. Even if taken at face value, a conflict at the root of a 4-taxon unrooted tree cannot distinguish which lineage was the donor or recipient, nor can it distinguish deep ancestral lineage sorting / rate heterogeneity from recent inter-species recombination in agricultural settings.

---

### 4. Reproducibility & Data Completeness

* **Strengths:** All 11 GenBank accession numbers (`AF304460`, `AF353511`, `AJ271965`, `AY223860`, `M95169`, `AY274119`, `AF208067`, `M55148`, `AF201929`, `AF220295`, `AF391542`), exact `SARS-TOR2` nucleotide coordinates for the 13 sub-alignments and recombinant zones, and `MODELTEST` model selections are explicitly documented in the text and Figure 1 caption.
* **Deficiencies:**
  1. The trimmed sequence alignments are only stated as *"available upon request"* rather than deposited in a permanent repository or supplementary file. Because manual gap-flank deletion created the 13 artificial sub-alignment boundaries (which directly dictated where PLATO could or could not detect anomalies), exact coordinates of the deleted gap regions before and after trimming are essential for reproducibility.
  2. Quantitative outputs for the corroborating `SplitsTree` and `BOOTSCAN` analyses mentioned in the Methods are not shown in any figure or table.
