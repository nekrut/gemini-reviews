<Blinded Review: TIME_ANON_0485>
**Composite Score:** 7.8 / 10.0 (Rigor: 2.7/3.5 | Claims: 2.0/2.5 | Biology: 1.6/2.0 | Reproducibility: 1.5/2.0)
**Scientific Core Score:** 6.3 / 8.0
**Bias Category:** None (Methodologically Sound)
**Verdict:** Minor Revision
**Study Modality:** Hybrid Computational + Wet-Lab
**Technology Maturity:** Mid-Stage High-Throughput
**Epistemic Stage:** Basic/Mechanistic Discovery

OVERALL_SCORE: 7.8/10
VERDICT: PASS
ESTIMATED_DECADE: 2010s

---

### 1. Executive Summary / SUMMARY
This phylogenomic and phylogeographic study evaluates the information content and phylogenetic/demographic utility of Anchored Hybrid Enrichment (AHE; 415 vertebrate-anchored loci sequenced across 43 individuals representing 9 genera of Australian *Eugongylus*-group skinks plus outgroup *Lerista bougainvillii*) compared against transcriptome-mined exons (TM; 1,650 single-exon loci across 11 individuals). Using partitioned Maximum Likelihood concatenation (RAxML) and coalescent species-tree inference propagating gene-tree bootstrap uncertainty (STEAC over 1,000 PHYML bootstrap trees per locus), alongside isolation-with-migration coalescent modeling (`3s`) across five phylogeographic lineage pairs, the authors demonstrate that AHE loci contain higher average parsimony-informative characters (PICs) per locus than shorter random transcriptome exons (25.4 vs. 19.2 PICs/locus on the matched 11-taxon set), fully resolve intraspecific phylogeographic and congeneric relationships (except the rapid Tasmanian *Niveoscincus* radiation), and yield nucleotide divergence and coalescent $\tau$ estimates that correlate strongly with transcriptome divergence ($r = 0.97$ and $r = 0.91$). At deeper intergeneric nodes, the authors transparently report and analyze strongly supported topological conflict ($\text{BP} \ge 90$) between RAxML concatenation and STEAC species trees regarding the placements of *Pseudemoia* and *Cryptoblepharus*. The study is methodologically rigorous and open-data compliant (Dryad `doi:10.5061/dryad.g4mj2`), with minor numerical typos in Table 1 and low statistical power ($n=4\text{–}5$ pairs) in the `3s` demographic correlation tests.

### 2. Methodological & Statistical Audit / STRENGTHS / WEAKNESSES & METHODOLOGICAL AUDIT

#### STRENGTHS
- **Matched Taxon and Locus Subsampling Controls:** Directly compares 415 AHE loci against 1,650 TM exons by pruning the AHE dataset to the exact 11 taxa present in the TM dataset and comparing against both 10,000 random draws of 415 TM exons and the top 415 most informative TM exons (Table 1, Fig. 3).
- **Gene-Tree Uncertainty Propagation in Species-Tree Estimation:** Rather than feeding point-estimate ML gene trees into STEAC, the authors select per-locus nucleotide substitution models via MrAIC (across 24 models) and propagate 1,000 PHYML bootstrap pseudoreplicates per locus (415,000 trees for AHE; 1,650,000 trees for TM) into STEAC.
- **Explicit Spatial Profiling of Informative Sites:** Quantifies PIC density as a function of distance from the conserved probe center (Fig. 1a–b), both raw and normalized by locus length distribution, demonstrating why AHE retains phylogeographic signal within $\pm 200\text{ bp}$ of the anchor.

#### WEAKNESSES & METHODOLOGICAL AUDIT
- **Numerical Typos in Table 1:**
  - In Table 1 (line 106), the row `Anchored-enriched (AHE) | All samples` lists `N samples = 44`, whereas the Abstract (line 7), Methods (lines 35, 40), and Results (line 88) consistently state that `43 individuals` (42 ingroup + 1 outgroup) were included in the final dataset.
  - In Table 1 (line 117), the row `TM data pruned to number of AHE loci (highest PICs)` lists `% identity` as `Max = 99.1`, `Min = 95.3`, and `Mean = 90.1`. Mathematically, the mean of a distribution (90.1%) cannot be smaller than its minimum value (95.3%); `90.1` and `95.3` appear to be transposed between the `Min` and `Mean` columns.
- **Binomial Heterozygote Calling Formula Edge Case:** On line 49, consensus base calling for coverage $>9\times$ is described as `p = (1 - pbinom(nMax, n, 0.5))` where the most common base was called unless $p > 0.05$. Note that in R, `1 - pbinom(nMax, n, 0.5)` is $\text{Prob}(X > n_{\text{Max}})$ rather than $\text{Prob}(X \ge n_{\text{Max}})$, and testing whether $n_{\text{Max}}$ is *consistent* with a 50:50 heterozygote vs. a homozygote with sequencing error requires comparing the binomial likelihood of a heterozygote ($p=0.5$) against the sequencing error rate ($\epsilon \approx 0.01$) rather than testing upper-tail $p > 0.05$ under $p=0.5$ (under $p=0.5$, any read split close to 50:50 has $1 - \text{pbinom}(n_{\text{Max}}, n, 0.5) > 0.05$, which correctly triggers the IUPAC ambiguity code, though a true homozygote with $n_{\text{Max}} = n$ gives $1 - \text{pbinom}(n, n, 0.5) = 0 \le 0.05$).
- **Low Sample Size ($n=4\text{–}5$ Lineage Pairs) and Model Discrepancy in `3s` Coalescent Comparisons:** In Figure 4, Pearson correlations are computed across only $n=5$ lineage pairs (Fig. 4a–b) and $n=4$ lineage pairs (Fig. 4c, where $r=0.85$ has one-tailed $P=0.07$, two-tailed $P=0.15$). Moreover, `3s` likelihood-ratio tests favored isolation-with-migration (Models 1 & 2) over strict isolation (Model 0) for all 5 pairs, directly conflicting with prior `dadi` 2D-SFS analyses on $N=5$ transcriptomes per lineage that rejected gene flow. As the authors note in the Discussion, unmodeled intralocus recombination or selection on conserved coding anchors can inflate apparent gene-flow likelihoods in `3s`.

### 3. Biological / Experimental Grounding & Claim Proportionality
- **Claim 1: Anchored Hybrid Enrichment (AHE) loci resolve both congeneric and intraspecific phylogeographic relationships with accuracy matching 1,650 transcriptome-mined exons.** `[Well Supported]` — Directly supported by identical, 100%-supported topologies across the 11-taxon benchmark and consistent phylogeographic splits in *Carlia*, *Lampropholis*, and *Saproscincus*.
- **Claim 2: Deep intergeneric relationships in the Australian *Eugongylus* radiation exhibit short internodes and strong concatenation vs. species-tree incongruence for *Pseudemoia* and *Cryptoblepharus*.** `[Well Supported]` — Clearly documented by comparing partitioned RAxML and STEAC bootstrap trees (Fig. 2).
- **Claim 3: `3s` coalescent modeling on AHE loci recovers divergence times concordant with population-level `dadi` SFS estimates.** `[Moderately Supported]` — The positive trend ($r = 0.85$ across $n=4$ pairs) is encouraging, but statistically underpowered ($P = 0.07$ one-tailed) and accompanied by opposite model-selection conclusions regarding post-divergence gene flow.

### 4. Reproducibility & Data Completeness
- All sequence alignments, assemblies, trees, and custom processing scripts are deposited in Dryad (`doi:10.5061/dryad.g4mj2`), and museum voucher/permit numbers and Additional files 1–5 are thoroughly documented.
</Blinded Review: TIME_ANON_0485>
