# Forensic Review of FEXP_ANON_037

**Manuscript ID:** `FEXP_ANON_037`  
**Overall Score:** **7.7 / 10.0** (Strong / Sound) | **Scientific Core Score:** **5.9 / 8.0**  
* **Score Breakdown:** Rigor: 2.6/3.5 | Claims: 1.8/2.5 | Biology: 1.5/2.0 | Reproducibility: 1.8/2.0

---

## 1. Blinded Metadata Perception

* **Perceived Subfield:** Plant Evolutionary & Comparative Genomics / Polyploid Rediploidization (Lythraceae: *Sonneratia alba* and *Lagerstroemia speciosa*).
* **Study Design:** Chromosome-scale genome assembly of the mangrove *Sonneratia alba* ($2n=24$, 204.5 Mb) and inland relative *Lagerstroemia speciosa* ($2n=48$, 319.7 Mb), comparative synteny and ancestral karyotype reconstruction with *Punica granatum* ($2n=16$), multi-tissue and salt-gradient transcriptomics, and population-genetic selection analysis (DFE-alpha, SnIPRE, McDonald-Kreitman) across 24 resequenced *S. alba* individuals and 1 *S. apetala* outgroup.
* **Primary Methods:** PacBio Sequel II + Illumina + Hi-C assembly (wtdbg2, Quiver, Pilon, Juicer/3D-DNA), EvidenceModeler annotation, RAxML-NG + PAML MCMCTREE molecular dating, MCScanX + WGDI ancestral karyotype reconstruction, MAPS paleopolyploidy coalescent simulations, exact conditional binomial test and DESeq2 for RNA-seq, and DFE-alpha / SnIPRE / MK fixation index.

---

## 2. Executive Summary & Editorial Verdict

This study reports chromosome-scale genome assemblies for the mangrove tree *Sonneratia alba* (204.46 Mb across 12 chromosomes, N50 = 15.69 Mb, 97.6% anchored) and the related inland Lythraceae species *Lagerstroemia speciosa* (319.66 Mb across 24 chromosomes, N50 = 12.74 Mb, 98.1% anchored). Comparing these genomes with *Punica granatum* ($n=8$), the authors demonstrate via 3:1 syntenic ratios, $K_s$ peaks, 306-orthogroup gene tree topologies, and MAPS birth-death simulations that the common ancestor of *Sonneratia* and *Lagerstroemia* underwent a whole-genome triplication (WGT) around 64 Mya near the K-Pg boundary. Reconstructing the Ancestral Lythraceae Karyotype ($n=8 \xrightarrow{\text{WGT}} n=24$), they show that while *L. speciosa* retained $n=24$ chromosomes primarily through intra-chromosomal inversions, the mangrove *S. alba* experienced extensive chromosome fusions and fissions reducing its karyotype to $n=12$, alongside reduced transposable element accumulation (20.95% vs. 36.50%). Finally, they examine paralog expression divergence across four tissues (~60% in both species), salt-responsive expression in *S. alba*, and population-genetic selection signatures (DFE-alpha, MK test, SnIPRE) across 1-, 2-, and 3-copy WGT retention groups.

**Editorial Verdict: Minor Revision (Strong / Sound).** The primary genome assemblies, shared WGT placement, and ancestral karyotype reconstructions are technically rigorous, validated by orthogonal syntenic and phylogenomic methods, and backed by complete open data deposition in NGDC and Figshare. The main limitations lie in the downstream population-genetic and functional interpretations: (1) the DFE-alpha and SnIPRE comparison across 1-, 2-, and 3-copy WGT retention groups in *S. alba* does not control for intrinsic dosage-balance covariates (expression level, network connectivity, protein length) or include the inland *L. speciosa* baseline, conflating universal constraints on dosage-sensitive triplicated genes with mangrove-specific adaptation; (2) applying an unadjusted exact binomial test (`binom.test`) to raw HTSeq read counts across paralogs ignores biological overdispersion and effective mappable gene length differences; and (3) pooling two geographically separated Philippine island populations (Cebu and Davao) into a single SFS in DFE-alpha can bias $\alpha$ and $N_e s$ estimates if inter-island population structure exists.

### Specific Conclusions and Assessment of Support

* **Chromosome-scale genome assemblies of *S. alba* ($n=12$, 204.5 Mb) and *L. speciosa* ($n=24$, 319.7 Mb) and shared ancestral WGT (~64 Mya) post-dating divergence from *P. granatum* ($n=8$): [Well Supported].**  
  High-depth PacBio + Illumina + Hi-C scaffolding achieves >97.6% chromosome anchoring with clean Hi-C contact maps. The placement of the WGT between the *Punica* divergence (~67.8 Mya) and the *Sonneratia*–*Lagerstroemia* split (~57.8 Mya) is independently corroborated by 3:1 macrosynteny (Fig. 2c,f), orthogroup gene tree reconciliation (Fig. 2d), and MAPS simulations (Supplementary Fig. 17).
* **Differential post-WGT rediploidization produced extensive inter-chromosomal fusions/fissions and lower TE content in *S. alba* ($n=12$, 21.0% TE) compared to *L. speciosa* ($n=24$, 36.5% TE): [Well Supported].**  
  WGDI ancestral karyotype reconstruction from the $n=8$ Ancestral Lythraceae Karyotype (Fig. 2e,f) clearly documents the chromosomal fusion/fission trajectory reducing $n=24$ to $n=12$ in *S. alba*, contrasted against the karyotypically conserved $n=24$ structure of *L. speciosa*.
* **Paralogous gene pairs retained from the WGT exhibit ~60% expression divergence across tissues in both *S. alba* and *L. speciosa*: [Moderately Supported].**  
  Evaluating four tissues in both species provides a symmetric comparative baseline showing similar post-WGT regulatory divergence (~58–65% in *S. alba*, ~60% in *L. speciosa*). However, testing differential expression between paralogs with `binom.test` on raw read counts without normalizing for paralog transcript length or biological replicate overdispersion inflates statistical significance for high-count genes.
* **Three-copy WGT retentions in *S. alba* experience stronger purifying and positive selection ($\alpha, \omega_a$, FI) specifically driving mangrove adaptation to intertidal salt and waterlogging stress: [Fragile].**  
  In Fig. 4, 3-copy retained genes show both a larger fraction of strongly deleterious mutations ($N_e s < -100$) and higher adaptive substitution rates ($\alpha, \omega_a$) than 1- and 2-copy genes. However, genes retained in triplicate for 64 Myr across all angiosperms are heavily enriched for dosage-balance-sensitive regulators and core metabolic complexes, and no parallel DFE/MK control in *L. speciosa* or covariate adjustment for baseline gene expression was performed. Moreover, the links between 3-copy retention and root pneumatophore/ABA salt pathways (Fig. 5) are qualitative pathway illustrations without a formal statistical enrichment test demonstrating that salt-induced DEGs are overrepresented among 3-copy retentions.

---

## 3. Forensic Defect Inventory

### 1. Confounding of Ancestral Dosage-Balance Constraints and Population Structure in DFE-alpha / MK Selection Tests (Pillars 3, 4 & 5)
* **WHY:** In Section "Strong selection in WGT retained gene groups" (line 89; Methods line 41), the authors run DFE-alpha, SnIPRE, and McDonald-Kreitman tests on 1-copy ($n=3,439$), 2-copy ($n=4,832$), and 3-copy ($n=1,171$) WGT retention groups using 24 *S. alba* individuals pooled from two Philippine locations (Cebu, $n=12$; Davao, $n=12$) and 1 *S. apetala* outgroup. First, pooling two island populations into a single folded SFS without checking inter-population differentiation ($F_{ST}$) distorts the SFS compared to panmictic coalescent expectations. Second, 3-copy retained ohnologs systematically differ from 1-copy genes in expression level, protein length, and pleiotropic constraint across *all* paleopolyploid plants; attributing their DFE profile to mangrove intertidal adaptation without controlling for expression level or comparing against *L. speciosa* conflates general ohnolog dosage balance with habitat-specific selection.
* **WHAT:** Control for baseline gene expression level and inter-population structure in the DFE-alpha / MK comparison, and test whether 3-copy WGT retentions are actually enriched for mangrove-specific divergence.
* **HOW:** (1) Compute the folded SFS and DFE-alpha separately for the Cebu ($n=12$) and Davao ($n=12$) populations to verify that population subdivision does not drive the $\alpha$ and $\omega_a$ estimates; (2) stratify or match 1-copy, 2-copy, and 3-copy genes by mean log-TPM expression level and coding sequence length before comparing FI and SnIPRE selection effects; and (3) compare $d_N/d_S$ ($\omega$) along the *S. alba* branch vs. the *L. speciosa* branch across 1-, 2-, and 3-copy orthogroups.

### 2. Unnormalized Exact Binomial Test (`binom.test`) for Paralog Expression Divergence (Pillars 3 & 4)
* **WHY:** In Section "Transcriptome sequencing and analysis" (Methods line 34), expression divergence between WGT paralogs $A$ and $B$ is tested by applying `binom.test(counts_A, counts_A + counts_B, p = 0.5)` to uniquely mapped HTSeq read counts per tissue. Raw read counts scale linearly with effective mappable CDS/transcript length: if paralog $A$ is 15% longer than paralog $B$, equal molar transcript abundance yields a 53.5% vs. 46.5% read split, which `binom.test` flags as highly significant ($P < 10^{-5}$ at 2,000 total reads) even after Bonferroni correction. Furthermore, `binom.test` ignores biological replicate variance.
* **WHAT:** Normalize paralog read counts by effective mappable gene length and account for biological replicate dispersion when calling differentially expressed gene pairs (DEGPs).
* **HOW:** Replace `binom.test` on raw HTSeq counts with length-normalized TPM/FPKM ratios tested across the 3 biological replicates via a paired linear/negative-binomial model (or set a minimum fold-change threshold, e.g., $|\log_2(\text{TPM}_A / \text{TPM}_B)| \ge 1$ alongside the adjusted $P < 0.05$ criterion) and report the updated percentage of DEGPs in Supplementary Tables 6 and 8.

### 3. Lack of Formal Enrichment Testing for Salt-Responsive DEGs Among WGT Retentions (Pillars 1 & 5)
* **WHY:** In Section "WGT retained genes for root development and salt tolerance" (lines 97–102, Fig. 5), the authors report 83 three-copy retention groups and 283 two-copy retention pairs with at least one copy upregulated under high salt, highlighting ABA and auxin transport candidates. Because a 3-copy group has three chances (and a 2-copy pair has two chances) for "at least one copy" to be upregulated compared to a 1-copy gene, raw counts of groups with $\ge 1$ upregulated member are mathematically biased toward multi-copy groups unless evaluated at the individual gene level against a hypergeometric null.
* **WHAT:** Perform a formal gene-level Fisher's exact test comparing the proportion of salt-upregulated DEGs among 1-copy, 2-copy, and 3-copy retained genes.
* **HOW:** Tabulate the exact fraction of individual genes upregulated under 250 mM and 500 mM NaCl in 1-copy ($n=3,439$), 2-copy ($n=4,832$), and 3-copy ($n=1,171$) categories and report the odds ratio and Fisher's exact $P$-value in the main text.

---

## 4. Quantitative Rubric Scoring

| Rubric Dimension | Score | Max | Forensic Justification |
| :--- | :---: | :---: | :--- |
| **1. Methodological & Statistical Rigor** | **2.6** | **3.5** | High technical quality in the primary deliverable (chromosome-scale *S. alba* and *L. speciosa* assemblies), fossil-calibrated MCMCTREE dating, WGDI ancestral karyotype reconstruction, and MAPS coalescent validation of the shared WGT. Deducted 0.9 pts for unnormalized `binom.test` paralog expression testing, unstratified DFE-alpha/MK comparisons across copy-number groups, and pooling two island populations into one SFS. |
| **2. Claim-to-Evidence Alignment** | **1.8** | **2.5** | Core claims regarding the ~64 Mya WGT and contrasting post-WGT chromosomal rediploidization ($n=12$ vs $n=24$) are strongly supported; adaptive narratives linking 3-copy WGT retention directly to mangrove pneumatophores and intertidal selection are correlative and lack an inland DFE control. |
| **3. Data Integrity & Biological Plausibility** | **1.5** | **2.0** | Symmetric inclusion of the inland Lythraceae comparator (*L. speciosa*) and outgroup (*P. granatum*) provides a strong comparative design; biological discussion of WGT buffering and karyotype compaction in mangroves is plausible and well contextualized. |
| **4. Reproducibility & Data Integrity** | **1.8** | **2.0** | Complete public data availability in NGDC GSA (`CRA004284`), GWH (`GWHBCIQ00000000`, `GWHBCKL00000000`), and Figshare (`10.6084/m9.figshare.25118819`, `25118831`), with clear documentation of software versions and parameters. |
| **Scientific Core Score** | **5.9** | **8.0** | Sum of Rigor + Claims + Biology (`2.6 + 1.8 + 1.5`). |
| **Total Composite Score** | **7.7** | **10.0** | **Strong / Sound** (`2.6 + 1.8 + 1.5 + 1.8`). |
