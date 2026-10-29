</Agent System Instructions>
<Blinded Review: TIME_ANON_0201>
**Composite Score:** 8.2 / 10.0 (Rigor: 2.9/3.5 | Claims: 2.1/2.5 | Biology: 1.6/2.0 | Reproducibility: 1.6/2.0)
**Bias Category:** None (Methodologically Sound)
**Verdict:** Minor Revision
**Study Modality:** Hybrid Computational + Wet-Lab
**Technology Maturity:** Mature/Classical
**Epistemic Stage:** Basic/Mechanistic Discovery

---

### 1. Executive Summary
This mitogenomic and molecular phylogenetics study reports the complete mitochondrial genome sequence (15,816 bp) of the solitary stolidobranch ascidian *Herdmania momus* and evaluates the phylogenetic placement of Tunicata within Metazoa using a 54-taxon, 13-protein concatenated alignment (2,136 unambiguously aligned amino acid sites). The *H. momus* mtDNA contains the canonical 37 tunicate mitochondrial genes (13 proteins, 2 rRNAs, 24 tRNAs) encoded on a single strand, exhibits an AT content of 63.5% and 9.21% non-coding sequence (including an 89-bp duplicated element), and displays radical gene order rearrangement compared to its close pyurid relative *Halocynthia roretzi* (sharing only a single two-gene block, *trnW–trnI*, and breaking the otherwise conserved tunicate *cox2–cytb* block). Using Principal Component Analysis (PCA) of amino acid composition and comparing homogeneous (mtREV+$\Gamma_4$, GTR+$\Gamma_4$), site-heterogeneous (CAT+$\Gamma_4$ variants), and site- and time-heterogeneous (nhPhyloBayes CAT+BP+$\Gamma_4$) substitution models, the authors demonstrate that while homogeneous models place tunicates outside Bilateria or with *Xenoturbella* due to severe compositional bias and long-branch attraction (LBA), CAT+mtREV/GTR and CAT+BP models recover monophyletic Chordata ($\text{PP} = 0.96$) and Olfactores (Tunicata + Craniata, $\text{PP} = 0.94$–$0.96$). Furthermore, root-to-tip branch length regression ($R^2 = 0.88$) across nucleotide alignments of protein-coding (8,130 bp) and rRNA (806 bp) partitions demonstrates a genome-wide evolutionary rate acceleration in tunicates.

### 2. Methodological & Statistical Audit
- **Phylogenetic Modeling of Systematic Biases:** This is a textbook demonstration of diagnosing and overcoming systematic phylogenetic error (compositional heterogeneity + lineage-specific rate acceleration). The authors first quantify the amino acid compositional divergence of tunicates via PCA (PC1 = 53.1%, PC2 = 15.3%, showing Tunicata and Gnathostomata at opposite extremes of PC1), and then systematically test 6 Bayesian model specifications (Table 2) alongside ML (PhyML mtREV+$\Gamma_4$ and C20+$\Gamma_4$).
- **MCMC Convergence & Model Comparison:** Multiple independent MCMC chains (3 chains for PhyloBayes 3.1 models; 5 chains for nhPhyloBayes CAT+BP+$\Gamma_4$) were run from random starting trees. One minor methodological limitation is that convergence was assessed "by monitoring the marginal likelihood through cycles" rather than reporting quantitative bipartition discrepancy metrics (`maxdiff` and effective sample size `effsize` via `bpcomp`/`tracecomp`), and the CAT+BP model used fixed C60 empirical profiles (`Le et al.`) rather than free profile estimation due to computational complexity.
- **Minor Table / Text Discrepancies:**
  - In the Results (line 72), the text states that *Doliolum nationalis* has "13.1% of the total genome length" as non-coding regions, whereas Table 1 (line 84) reports `14.71%` (2,405 bp / 16,351 bp = 14.71%).
  - In comparing rRNA vs. protein-coding evolutionary rates (Figure 6), the authors regress root-to-tip distances from the two partitions ($R^2 = 0.88$, $n = 54$) using ordinary least squares without phylogenetic independent contrasts (PIC). Because root-to-tip paths share internal branches across the tree, the 54 data points are phylogenetically non-independent, which inflates the nominal $R^2$ (though the qualitative visual separation of the 7 tunicate tips is unmistakable).

### 3. Biological / Experimental Grounding & Claim Proportionality
- **Claim 1:** Extensive mitochondrial gene order rearrangements occur within Stolidobranchia (*H. momus* vs. *H. roretzi*), demonstrating that extreme mitogenomic plasticity is a general feature across tunicate orders. `[Well Supported]` — Directly proved by the complete *H. momus* assembly and synteny comparison (Fig. 3).
- **Claim 2:** Accounting for site- and time-heterogeneous amino acid replacement (CAT and CAT+BP models) resolves the mitogenomic long-branch attraction artifact and recovers Olfactores (Tunicata + Craniata) and Chordata monophyly for the first time with full 13-protein mitogenomic data. `[Well Supported]` — Strongly supported by Bayesian posterior probabilities ($\text{PP} = 0.94$–$0.96$ across CAT+mtREV, CAT+GTR, and CAT+BP), while transparently reporting that ML C20 bootstrap support remains $<50\%$.
- **Claim 3:** The elevated substitution rate in tunicate mtDNA affects both protein-coding and rRNA genes equally, arguing against episodic positive selection on respiratory proteins alone as the primary driver. `[Well Supported]` — Supported by the ~3:1 proportional scaling of branch lengths in both partitions.

### 4. Reproducibility & Data Completeness
- Reproducibility is exemplary: the complete annotated *H. momus* mtDNA sequence was deposited in EMBL (`FN296153`), long-PCR primer sequences are provided in the Methods, Gblocks trimming parameters are explicitly specified, and all three concatenated alignments (amino acid 13-protein, nucleotide 13-protein, and nucleotide rRNA) plus the full accession table are provided as Additional Files in Nexus format.
</Blinded Review: TIME_ANON_0201>
