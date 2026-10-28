# Review of ANON_69

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **5.2 / 10.0** (Mixed / Salvageable)  
* **Score Breakdown:** Rigor: 1.5/3.5 | Claims: 1.2/2.5 | Biology: 1.1/2.0 | Reproducibility: 1.4/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript investigates the molecular evolution of the *Rem2* gene (encoding a Ras-like RGK family small GTPase) across 175 mammalian species using codon substitution models in HyPhy (`BUSTED`, `BUSTED+S+MH`, `FEL`, `MEME`, `SLAC`, `BGM`) alongside an ancestral sequence reconstruction and AlphaFold2 structure prediction pipeline (`SPA`). The authors report that mammalian *Rem2* experiences strong purifying selection across 70% of non-invariant codon sites (with 251/627 sites invariant at the nucleotide level), shows no statistically significant evidence of gene-wide episodic diversifying selection once synonymous rate variation and multi-nucleotide substitutions are accounted for (`BUSTED+S+MH` model-averaged $p = 0.2272$), exhibits 50 putatively coevolving codon pairs in `BGM`, and maintains global fold similarity ($>0.5$ TM-score in 86% of pairwise comparisons) across extant and reconstructed ancestral protein structures. Raw alignments, HyPhy JSON outputs, and scripts are publicly available on GitHub and Zenodo.

While the core finding of strong purifying selection and absence of episodic positive selection via `BUSTED+S+MH` is solid, the broader conclusions regarding intramolecular epistasis, clinical pathogenicity, and ancestral structural divergence rest on flawed downstream analyses: (1) all selection, ancestral reconstruction (`SLAC`), and coevolution (`BGM`) analyses are conditioned on a single maximum-likelihood gene tree that disagrees with the mammalian species tree at 53.5% of bipartitions ($\text{RF} = 122/228$), a hallmark of phylogenetic noise in short conserved alignments rather than biological incomplete lineage sorting; (2) the `SPA` structural comparison computes global `TM-align` and `RMSD` scores across full-length AlphaFold2 predictions without masking the extensive N- and C-terminal intrinsically disordered regions (IDRs, $\text{pLDDT} < 50$), meaning the reported structural variance at low genetic distance is driven by random coil orientations; (3) human residues 48, 52, and 64 are misclassified as falling within the core RGK domain, and listing generic population variants (including a frameshift and a nonsense stop-gain) from `gnomAD` at those positions does not constitute evidence of epistatic disease effects; and (4) methods described in the Methods section (`GARD` recombination screening and `FMM` model fitting) are omitted from the Results. These issues can be addressed through computational re-analysis on a species-tree topology and domain-restricted structural comparisons.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Mammalian *Rem2* is subject to pervasive purifying selection and shows no evidence of gene-wide episodic diversifying selection after accounting for multi-nucleotide mutations and synonymous rate variation: [Well Supported].**  
  Table 2 clearly demonstrates that while baseline `BUSTED` ($p < 0.0001$, $\omega_3 = 23.16$) and `BUSTED+S` ($p < 0.0001$, $\omega_3 = 50.75$) reject the null hypothesis, adding multi-nucleotide substitutions in `BUSTED+S+MH` collapses $\omega_3$ to $1.0000$ ($p = 0.5000$, model-averaged $p = 0.2272$). Similarly, `FEL` identifies purifying selection at 70% of variable sites (FDR $p \le 0.10$) and `MEME` detects zero positively selected sites after FDR correction.

* **Fifty pairs of codon sites in *Rem2* exhibit epistatic coevolution (`BGM`), with mutations at human sites 48, 64, and 98 predicted to have deleterious clinical effects: [Overstated].**  
  First, `BGM` was evaluated at a permissive posterior probability threshold of $0.5$ (Figure 6 caption) on a gene tree with a normalized Robinson-Foulds distance of $0.535$ from the mammalian species tree, without controlling for alignment gaps or RefSeq isoform annotation differences that turn an alignment of a 340-residue human protein into 627 codon sites. Second, the text states that human sites 48, 52, 64, 98, and 319 "all... fall within the RGK region" (line 180), whereas human Rem2 residues 48, 52, and 64 lie in the unstructured N-terminal extension upstream of the Ras-like RGK core domain (which begins near residue 100 and is why residues 48–64 are absent from the 169-residue crystal structure 3CBQ in Figure 3). Third, querying `gnomAD` v4.1.0 (Table 3) and finding a frameshift (`Leu48GlyfsTer37`), a premature stop codon (`Arg64Ter`), and three rare missense SNVs/MNVs with SIFT/PolyPhen predictions does not validate epistatic fitness interactions—loss-of-function truncations and generic SIFT scores occur throughout any conserved gene regardless of coevolution.

* **Ancestral sequence reconstruction coupled with AlphaFold2 (`SPA`) reveals structural divergence and evolutionary dynamics across extant and extinct mammalian *Rem2*: [Methodologically Flawed].**  
  Over half of full-length human Rem2 (340 AA) consists of flanking N- and C-terminal intrinsically disordered regions (IDRs), and `SLAC` reconstructs ancestral states across a 627-codon gappy alignment without a phylogenetic indel model. In AlphaFold2, disordered regions have low confidence ($\text{pLDDT} < 50$, colored red/yellow in Figure 4) and are placed in arbitrary spatial conformations. Computing global backbone `RMSD` ($3.61 \pm 0.54\text{ \AA}$) and global `TM-score` ($0.62 \pm 0.11$) across the entire uncropped polypeptide—and interpreting large `TM-score` variance at tiny genetic distances ($\text{TN93} < 0.05$, Figure 5, line 226) as potential "evolutionary innovation"—confounds random IDR loop placement and RefSeq length variation with true structural evolution of the ordered GTPase fold.

* **The *Rem2* gene tree deviates from the mammalian species tree ($\text{normalized RF} = 0.535$) due to biological factors such as incomplete lineage sorting (ILS): [Overstated].**  
  A normalized RF distance of $0.535$ across 175 mammals for a highly conserved ~340-codon gene (where 40% of sites are completely invariant and 70% of variable sites are under strong purifying selection) is an expected consequence of low phylogenetic signal per short internal branch, evidenced by the numerous low-bootstrap branches in Figure 1. Attributing this topological discordance to mammalian-wide ILS (line 114) without testing whether alternative topologies are statistically indistinguishable (e.g., via an approximately unbiased [AU] topology test) is unwarranted and introduces avoidable branch-mapping errors into `SLAC` and `BGM`.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Restrict Structural Comparisons (`SPA`) to the Ordered RGK Core Domain and Mask Low-pLDDT Regions
* **WHY:** Global `TM-align` and `RMSD` calculations on full-length Rem2 are dominated by arbitrary AlphaFold2 coordinates in the N- and C-terminal IDRs ($\text{pLDDT} < 50$) and by unmodeled indel/isoform length variation in `SLAC` ancestral reconstructions.
* **WHAT:** Re-compute all pairwise `TM-score` and `RMSD` metrics after trimming extant and ancestral structures to the ordered Ras-like GTPase core domain (corresponding to PDB `3CBQ`, human residues ~100–268, or residues with $\text{pLDDT} \ge 70$).
* **HOW:** Write a short Python/Biopython filter to slice the ColabFold rank-1 PDB files to the aligned core domain coordinates (or $\text{pLDDT} \ge 70$ C$\alpha$ atoms), re-run `tmalign` on the cropped structures, and update Figure 5 and Supplementary Table S5. Separate the structural conservation of the core GTPase fold from length/sequence variation in the flanking disordered regions.

#### 2. Evaluate Sensitivity of Selection, ASR, and Coevolution Analyses to the Mammalian Species Tree
* **WHY:** Conditioning `SLAC`, `BGM`, and `FEL` on a noisy ML gene tree ($\text{normalized RF} = 0.535$ vs. the NCBI/TimeTree mammalian phylogeny) creates spurious parallel substitutions on misresolved branches, which directly inflates false positives in `BGM` branch-co-occurrence tests and distorts ancestral sequences.
* **WHAT:** Re-run the HyPhy pipeline (`BUSTED+S+MH`, `FEL`, `SLAC`, `BGM`) using the established mammalian species tree topology (with branch lengths optimized under the codon model in HyPhy) and perform an IQ-TREE topology test (`-zb 10000 -au`) comparing the ML gene tree against the species tree.
* **HOW:** Pass the pruned NCBI/TimeTree species topology for the 175 taxa into IQ-TREE (`-g` or `-z`) to compute the AU test $p$-value, run the existing Snakemake/HyPhy scripts on the species tree, and report only those `BGM` coevolving pairs that remain supported (at posterior probability $\ge 0.80$ or $\ge 0.90$ rather than $0.50$) across both topologies.

#### 3. Audit the 627-Codon Alignment for RefSeq Isoform Artifacts and Report Missing `GARD`/`FMM` Results
* **WHY:** Human Rem2 is 340 codons long, meaning nearly half of the 627 alignment columns arise from insertions, unaligned N/C-terminal RefSeq `XM_` prediction artifacts, or retained introns in non-human mammals. Furthermore, `GARD` (lines 44–46) and `FMM` (Table 1, row 6) are detailed in the Methods but never reported in the Results.
* **WHAT:** Report the `GARD` and `FMM` outputs in the Results (or remove them from the Methods if not executed), and quantify what fraction of the 627 alignment sites have high gap/masking fractions ($>50\%$ gaps).
* **HOW:** Summarize the gap distribution per column from the `codon-msa` output, restrict `BGM` and `FEL` summary percentages to columns present in $>70\%$ of taxa (or mapped to the 340 human canonical codons), and reconcile the sequence count discrepancy between Methods line 31 ($186 - 9 = 177$ sequences) and Results line 99 ($175$ sequences).

#### 4. Correct the Domain Annotation and Clinical Framing of Human Sites 48, 52, 64, and 98
* **WHY:** Residues 48, 52, and 64 are located in the N-terminal disordered region of human Rem2, not the RGK GTPase domain, and presence of rare variants (especially frameshift and nonsense alleles) in `gnomAD` v4.1.0 is a measure of standing population variation, not clinical disease association or epistasis.
* **WHAT:** Correct the domain mapping of human sites 48, 52, and 64, and reframe Table 3 as a descriptive catalog of rare standing polymorphism in `gnomAD` rather than evidence of epistatic pathogenicity.
* **HOW:** Update lines 180–198 and the Abstract ("some of which are predicted to have deleterious effects on human health") to accurately state which `BGM` sites fall in the N-terminal regulatory tail versus the RGK core domain, and remove the frameshift (`Leu48GlyfsTer37`) and stop-gain (`Arg64Ter`) variants from the discussion of amino-acid coevolution.

#### 5. Technical, Mathematical, and Editorial Cleanup
* **WHY:** Coordinate mismatches, typographical sign errors, and incomplete sentences reduce technical clarity.
* **WHAT & HOW:**
  1. **Table 3 (line 197):** Codon site 98 is listed at `Genome Position (hg38: chr14) 22,884,863`, whereas codons 48 and 64 are at `23,353,918` and `23,353,969`. Position `22,884,863` is the **GRCh37/hg19** coordinate (`chr14:22,884,863` lifts over to `chr14:23,354,071` in GRCh38/hg38). Fix the coordinate so all rows use hg38.
  2. **Line 119 and Line 269:** Fix the tilde-to-minus conversion errors where "$\sim 50$" is printed as "$-50$" ("The $\omega_3$ rate... was $-50$") and "$\sim 200$ million years" is printed as "$-200$ million years".
  3. **Line 172 and Line 180:** Fix the broken sentences "Additionally, t coevolving sites may be related..." (line 172) and "When we reviewed putatively interacting, we noticed..." (line 180).
  4. **Line 279:** Fix the truncated first letter in Funding Statement ("he author(s) declare...").
