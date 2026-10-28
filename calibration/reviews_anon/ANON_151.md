# Forensic Scientific Peer Review: ANON_151

**Overall Score:** **4.6 / 10.0** (Flawed / Overstated)
* **Score Breakdown:** Rigor: 1.2/3.5 | Claims: 1.1/2.5 | Biology: 1.1/2.0 | Reproducibility: 1.2/2.0

---

## 1. Executive Summary & Synthesis

This manuscript sequences whole-genome short-read libraries from pooled individuals across 8 species of African monogenean gill parasites (*Cichlidogyrus* spp., *Scutogyrus longicornis*, and *Kapentagyrus* spp.) and combines them with 3 published libraries and a draft genome annotation of *Cichlidogyrus casuarinus* to investigate phylogenomics and the molecular evolution of stress-response genes across 11 dactylogyrid species. Using `HybPiper v2.0`, the authors extract single-copy orthologs from OMA and BUSCO databases for phylogenomic inference (`IQ-TREE2`) alongside 48 putative stress-response genes (heat shock proteins, antioxidant enzymes, aquaporins, and *foraging* [*For*] orthologs). They then apply `PAML v4.10` (`CODEML`) to test for site-level and clade-specific positive selection and infer lineage-specific gene duplications and losses.

While generating genomic resources for non-model flatworm ectoparasites is valuable and raw reads/alignments are deposited (`PRJNA1186934`, `JBJKFK000000000`, Zenodo `10.5281/zenodo.14236484`), the evolutionary and comparative genomic conclusions suffer from four major methodological flaws:

1. **Invalid Branch-Site `CODEML` Specification & Uncorrected Multiple Testing:** In the Methods ("Positive selection of gene sites"), the clade-specific foreground tests (hypotheses IIa for *Cichlidogyrus* and IIb for Lake Tanganyika *Cichlidogyrus*) are described as comparing `M1 (site model M2a)` against a null model `M0 (site model M2a, but with dN/dS fixed to 0)`. In `PAML`, testing for episodic positive selection along foreground branches requires the Zhang, Nielsen & Yang (2005) branch-site Model A (`model = 2, NSsites = 2`, estimating $\omega_2 \ge 1$ on the foreground) compared against null Model A1 (with $\omega_2 = 1$ fixed on the foreground). Fixing $\omega = 0$ in the null model tests against complete evolutionary stasis ($d_N = 0$), which conflates relaxed purifying selection ($0 < \omega \le 1$) with positive selection ($\omega > 1$). Furthermore, 48 genes are tested across 3 hypotheses ($48 \times 3 = 144$ likelihood ratio tests) at a nominal $\alpha = 0.05$ without Benjamini-Hochberg false discovery rate (FDR) correction, and a single fixed species tree (`OMA` tree) is forced onto all `CODEML` runs despite documented gene-tree discordance (Fig. 6).
2. **Direct Contradiction Between Results and Discussion on *For* Positive Selection:** In the Results ("Detection of positive selection", line 99) and Fig. 4d, the authors report that under the Lake Tanganyika clade-specific test (IIb), only two genes (*Hsp60* and *DNAJA1*) had positively selected sites, whereas *For* was detected only in the global site test (I). Yet in the Discussion ("Signature of selection", line 110), the authors assert: *"Our analyses indicate that one For ortholog has sites under positive selection specific to species of Cichlidogyrus from Lake Tanganyika"* and build an adaptive behavioural narrative around host-searching within the Lake Tanganyika cichlid radiation.
3. **Asymmetric `HybPiper` Bait-Capture Bias Confounding Gene Loss/Duplication Claims:** Target enrichment in `HybPiper` uses exon baits extracted exclusively from a draft genome of *Cichlidogyrus casuarinus* (an ingroup member of *Cichlidogyrus*). When these *C. casuarinus* nucleotide baits are used to capture exons from short reads of the distantly related clupeid-infecting genus *Kapentagyrus* ($n = 2$ species), sequence divergence across genera directly reduces read mapping and `SPAdes` contig assembly sensitivity. Concluding that *Kapentagyrus* lost or lacked duplications in *Hsp70* (groups 3 and 4b), *Gstm2* (*Gstm2a/b*), and *Gsto* based on unrecovered `HybPiper` contigs—without whole-genome synteny or reciprocal protein-level searches—confounds bait-distance dropout with true evolutionary gene loss or duplication.
4. **Pooled-Individual DNA, Whole-Genome Amplification (WGA) Chimerism, and Internal Count Contradictions:** All libraries were constructed from pooled worm individuals (up to 30 individuals per pool), and two species pools (*C. halli* and *K. tanganicanus*) underwent Phi29 multiple displacement amplification (`Genomiphi V3`), which is notorious for uneven coverage, allelic dropout, and chimeric contig assembly. In `HybPiper`, assembling pooled polymorphic reads or WGA products can split divergent haplotypes into artificial paralogs or collapse recent paralogs. Additionally, locus counts contradict each other across the text: the Results state *"277 (OMA tree, Fig. 3) and 86 (BUSCO tree, Additional File 1)"* (line 51), the Methods reverse these numbers (*"277 BUSCO and 86 OMA loci"*, line 162), Additional File 1's caption reports *"68 single-copy orthologs... BUSCO pipeline"*, and line 68 shifts from *"48 putative stress genes"* to *"The sequences of the 42 target genes"* in consecutive sentences.

---

## 2. Claim-by-Claim Audit

### Claim 1: A *foraging* (*For*) ortholog exhibits positively selected sites specific to Lake Tanganyika *Cichlidogyrus* species, reflecting behavioural adaptation to the cichlid adaptive radiation.
* **Support Level:** `[Methodologically Flawed]`
* **Evidence & Technical Critique:**
  - **Internal contradiction between Results and Discussion:** In the Results (line 99) and Fig. 4d, the Lake Tanganyika clade-specific test (IIb) identifies only *Hsp60* and *DNAJA1* (*Hsp40*). *For* is listed only under global test I (across the entire 11-species phylogeny, Fig. 4b). The claim in the Discussion (line 110) that *For* underwent Lake Tanganyika-specific positive selection directly contradicts the paper's own Results and Fig. 4d.
  - **Misconfigured foreground null model:** As described in the Methods (chunk 2, line 3), the foreground tests (IIa and IIb) compared model M2a against a null model with $\omega$ fixed to $0$ rather than the standard branch-site null model with foreground $\omega_2 = 1$ fixed (Zhang et al. 2005). Any site evolving under partial purifying selection ($0 < \omega < 1$) on the foreground branches will reject $\omega = 0$, invalidating the LRT for positive selection.

### Claim 2: Twenty-four stress genes show global positive selection across dactylogyrids (I), six show clade-specific selection in *Cichlidogyrus* (IIa), and two (*Hsp60*, *DNAJA1*) show selection in Lake Tanganyika *Cichlidogyrus* (IIb).
* **Support Level:** `[Methodologically Flawed]`
* **Evidence & Technical Critique:**
  - **Uncorrected multiple hypothesis testing and tree misspecification:** Conducting 144 LRTs (48 genes $\times$ 3 hypotheses) without FDR control guarantees numerous false positives at $p < 0.05$. Moreover, the authors forced the `OMA` species tree onto all 48 stress-gene `CODEML` runs even though their own Robinson-Foulds MDS ordination (Fig. 6) demonstrates substantial topological discordance between individual stress-gene trees and the species tree. Forcing an discordant topology onto site and branch-site codon models forces `CODEML` to explain hemiplasy/paralogy via recurrent nonsynonymous substitutions, inflating $\hat{\omega}$ and Bayes Empirical Bayes (BEB) posteriors.

### Claim 3: *Cichlidogyrus* underwent clade-specific gene duplications in *Hsp70* (group 4b), *Gstm2* (*Gstm2a/b*), and *Gsto* relative to *Kapentagyrus*, and all 11 monogenean species completely lack *Cyp* (cytochrome P450), *Gsts*, and *Gstk*.
* **Support Level:** `[Overstated]`
* **Evidence & Technical Critique:**
  - **Reference bait bias in `HybPiper`:** `HybPiper` was run using nucleotide exon baits derived solely from *C. casuarinus*. While absence of *Cyp*, *Gsts*, and *Gstk* in the *C. casuarinus* draft genome annotation is consistent with broader neodermatan flatworm gene losses, inferring that *Kapentagyrus* lacks paralogs present in *Cichlidogyrus* (*Hsp70* group 4b, *Gstm2a*, *Gsto*) is confounded by lower bait-to-read sequence identity in *Kapentagyrus* and unequal sequencing depth/WGA bias across pooled libraries. Conversely, apparent "duplications" in pooled *Cichlidogyrus* samples can arise from assembling divergent alleles from up to 30 pooled worms.

### Claim 4: Phylogenomic analyses of OMA and BUSCO single-copy orthologs resolve the monophyly of Lake Tanganyika *Cichlidogyrus* species (clade 1) and place *Scutogyrus longicornis* nested within *Cichlidogyrus* (clade 2).
* **Support Level:** `[Well Supported]`
* **Evidence & Technical Critique:**
  - Both supermatrix ML (`IQ-TREE2` with `ModelFinder` and 1,000 ultrafast bootstraps + SH-aLRT) and coalescent (`ASTRAL-III v5.7.8`) analyses strongly support the nesting of *Scutogyrus* within *Cichlidogyrus* and the monophyly of the four sampled Lake Tanganyika *Cichlidogyrus* species (Fig. 3, Additional File 1), consistent with prior ribo-mitochondrial phylogenies. However, the manuscript must resolve the three-way discrepancy in reported locus counts (277 vs. 86 vs. 68 for OMA and BUSCO datasets across lines 51, 162, and Additional File 1).

---

## 3. Concrete Actionable Recommendations

1. **Re-run Branch-Site Positive Selection Tests with Valid `CODEML` Models, Gene-Specific Trees, and FDR Control:**
   - For hypotheses IIa and IIb, replace the invalid $\omega = 0$ null model with the standard `PAML` branch-site test (`model = 2, NSsites = 2`: alternative model with $\omega_2 \ge 1$ free on the foreground vs. null model with `fix_omega = 1, omega = 1` on the foreground, evaluated against $\chi^2_1$ or the 50:50 $\chi^2_0:\chi^2_1$ mixture).
   - Run `CODEML` using each gene's own ML gene tree (in addition to the species tree) to eliminate false-positive $\omega > 1$ signals caused by topological discordance.
   - Apply Benjamini-Hochberg FDR correction ($q < 0.05$) across all tested genes for each hypothesis, and provide a supplementary table reporting $\ln L_{\text{null}}$, $\ln L_{\text{alt}}$, $2\Delta\ln L$, raw $p$-values, FDR $q$-values, parameter estimates ($\hat{\omega}$, proportions $p_0, p_1, p_2$), and BEB site coordinates.
2. **Rectify the *For* Contradiction in the Discussion:**
   - Remove the unsupported claim in the Discussion (line 110) that *For* exhibits Lake Tanganyika-specific positive selection (test IIb), or reconcile it explicitly with the Results and Fig. 4d.
3. **Control for `HybPiper` Bait-Distance Asymmetry and Pooled/WGA Paralog Artifacts:**
   - Translate `SPAdes` whole-genome assemblies (`de novo` assembled outside `HybPiper`) of *Kapentagyrus* and *Cichlidogyrus* species and search them with `TBLASTN` / `HMMER` profiles (`Pfam` domains for HSP70, GST) to verify whether "missing" paralogs in *Kapentagyrus* are genuinely absent from the genome or merely missed by *C. casuarinus* nucleotide baits.
   - Report per-sample read mapping rates, exon recovery fractions, and `HybPiper` paralog warnings, explicitly distinguishing WGA-amplified pools (*C. halli*, *K. tanganicanus*) from unamplified pools.
4. **Correct Internal Locus-Count Discrepancies:**
   - Reconcile the conflicting OMA and BUSCO locus numbers between line 51 (277 OMA / 86 BUSCO), line 162 (277 BUSCO / 86 OMA), and Additional File 1 (68 BUSCO), and fix the discrepancy between 48 and 42 target stress genes on line 68.
