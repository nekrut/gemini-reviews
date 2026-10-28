# Review of ANON_01

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **2.2 / 10.0** (Fundamentally Invalid)  
* **Score Breakdown:** Rigor: 0.4/3.5 | Claims: 0.5/2.5 | Biology: 0.5/2.0 | Reproducibility: 0.8/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript investigates the evolutionary relationship, recombination history, and putative animal reservoir of the novel coronavirus 2019-nCoV (MN908947). The authors align MN908947 with 271 (or 275, depending on the section) other coronavirus genomes, reconstruct a maximum-likelihood phylogeny under GTR+G in RAxML, run sliding-window similarity plots in SimPlot, and compare relative synonymous codon usage (RSCU) across 2019-nCoV, bat-SL-CoVZC45, and eight candidate vertebrate hosts using squared Euclidean distance. They conclude that 2019-nCoV is sister to bat coronaviruses ZC45 and ZXC21, that homologous recombination occurred in the spike glycoprotein with an unknown parental virus, and that snakes (*Bungarus multicinctus* and *Naja atra*) are the most likely animal reservoir based on RSCU similarity. No custom code or multiple sequence alignments are deposited, though the GenBank accession for 2019-nCoV is provided.

While the phylogenetic placement of 2019-nCoV as a close relative of bat SARS-related coronaviruses (bat-SL-CoVZC45 and bat-SL-CoVZXC21) is sound, the manuscript's two central novel conclusions—that snakes are the intermediate reservoir and that the spike sequence drop represents homologous recombination with an unknown virus—are methodologically invalid. The RSCU analysis suffers from extreme sample-size and gene-content ascertainment bias (comparing 10–64 tissue-specific CDSs in snakes and bats against 28,000–49,000 whole-genome CDSs in mammals and birds), ignores intrinsic mutational bias (CpG dinucleotide suppression and AU-richness across all coronaviruses), and uses an uncalibrated Euclidean distance without a phylogenetic or compositional null model. Furthermore, the recombination analysis conflates accelerated adaptive divergence or lineage-specific substitution rates in the hypervariable S1/receptor-binding region with homologous recombination, while withholding the bootscanning plot ("data not shown") and providing no statistical recombination tests. Resolving these flaws requires complete re-analysis with whole-genome host reference panels, dinucleotide-corrected codon models, and formal recombination detection algorithms.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **2019-nCoV is phylogenetically closest to bat SARS-like coronaviruses (bat-SL-CoVZC45 and bat-SL-CoVZXC21): [Well Supported].**  
  Maximum-likelihood phylogenetic reconstruction under GTR+G places MN908947 in a monophyletic clade sister to Clade A (bat-SL-CoVZC45 and bat-SL-CoVZXC21) with 100% bootstrap support (Section 3.1, Figure 1).

* **2019-nCoV has the most similar codon usage bias to snakes (*Bungarus multicinctus* and *Naja atra*), implicating snakes as a likely wildlife reservoir: [Methodologically Flawed].**  
  This conclusion rests on three compounding errors:
  1. *Severe sampling and ascertainment bias (Pillar 2):* In Section 2.3, the authors compute RSCU for *B. multicinctus* from just 38 CDSs (5,381 codons), *N. atra* from 64 CDSs (9,587 codons), and *Rhinolophus sinicus* from 10 CDSs (8,081 codons), whereas *Erinaceus europaeus*, *Marmota*, *Manis javanica*, *Gallus gallus*, and *Homo sapiens* are represented by whole-genome datasets of 28,947 to 49,453 CDSs (16.7 million to 40.6 million codons). Small GenBank depositions for snakes are heavily enriched for venom gland toxins (which have atypical, AT-biased compositional profiles) and do not represent genome-wide translational selection in snakes.
  2. *Confounding by viral mutational pressure (Pillar 3 & 6):* Table 1 shows that both 2019-nCoV and bat-SL-CoVZC45 strongly prefer U- and A-ending codons (e.g., Phe UUU = 1.41/1.33, Leu CUU = 1.75/1.77, Val GUU = 1.95/1.89, Pro CCU = 1.94/1.82) and avoid CpG-containing codons (Ser UCG = 0.11/0.15, Pro CCG = 0.16/0.26, Thr ACG = 0.20/0.24, Ala GCG = 0.15/0.24). This is a universal feature of coronavirus RNA-dependent RNA polymerase mutational bias and ZAP-mediated CpG evasion, not translational adaptation to a cold-blooded reptile host. Notably, bat-SL-CoVZC45—a known bat virus—has an almost identical RSCU profile to 2019-nCoV (Table 1; squared Euclidean distance between 2019-nCoV and bat-SL-CoVZC45 across the 20 codons shown in Table 1 is ~0.18, far smaller than the 13.54 distance to *B. multicinctus*), which directly falsifies the premise that RSCU distance identifies the specific host species.
  3. *Biological implausibility (Pillar 6):* All known *Betacoronavirus* species infect strictly mammalian hosts; no betacoronavirus has ever been shown to replicate in ectothermic reptiles.

* **Homologous recombination occurred within the spike glycoprotein between Clade A bat coronaviruses and an origin-unknown coronavirus: [Overstated].**  
  A localized drop in nucleotide sequence similarity in a SimPlot sliding window (Figure 2) across the spike S1 region (nucleotides 1–783 of S) is necessary but insufficient to establish homologous recombination. In the absence of a second identifiable parental lineage ("no similar sequence was found with known sequence in the database", Section 4), a drop in similarity between 2019-nCoV and Clade A can arise from elevated diversifying selection, insertions/deletions, or ancestral polymorphism in the surface-exposed receptor-binding domain. The authors mention a bootscanning plot in Section 2.2 and Section 4 ("data not shown"), which cannot be verified, and perform no formal statistical tests for recombination breakpoints (e.g., PHI test, RDP4, GARD).

* **Homologous recombination in the spike glycoprotein explains cross-species transmission and "limited person-person spread": [Overstated].**  
  The manuscript provides no functional, structural, receptor-binding, or epidemiological analysis linking the spike sequence divergence to host tropism or human-to-human transmissibility. Claiming that spike recombination explains "limited person-person spread" (Sections 1 and 4) is pure speculation.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Replace Partial GenBank CDS Sets with Complete Reference Transcriptomes for Host RSCU Comparisons
* **WHY:** Comparing 10–64 banked genes in bats and snakes against >28,000 whole-genome CDSs in other mammals introduces severe sampling variance and gene-family ascertainment bias (e.g., snake venom transcripts), invalidating the Euclidean distances in Figure 3B and Table 1.
* **WHAT:** Recompute host RSCU profiles using exclusively whole-genome coding sequence annotations across all compared vertebrate species, and include a wide panel of known coronavirus hosts as positive controls.
* **HOW:** Download the complete RefSeq/Ensembl CDS fasta files for *Rhinolophus sinicus* (or *Rhinolophus ferrumequinum*), *Naja naja* / *Notechis scutatus* / *Python bivittatus* (whole-genome snake assemblies), alongside the existing mammalian and avian genomes. Re-run `CodonW` to obtain genome-wide RSCU tables and recompute the squared Euclidean distances $d_{ik} = \sum_{j=1}^{59} (X_{ij} - X_{kj})^2$.

#### 2. Benchmark RSCU Host Prediction Using Known Coronavirus-Host Pairs and Control for Dinucleotide Bias
* **WHY:** Table 1 demonstrates that the known bat coronavirus bat-SL-CoVZC45 has virtually the same U/A-ending codon preference as 2019-nCoV, yet is distant from *R. sinicus* in Figure 3A. Without showing that Euclidean RSCU distance accurately assigns known coronaviruses (e.g., bat-SL-CoVZC45, SARS-CoV, MERS-CoV, MHV, IBV) to their verified natural hosts (bats, camels, mice, chickens), RSCU similarity cannot be used for host inference.
* **WHAT:** Perform a positive-control validation and separate background nucleotide composition from translational codon usage bias.
* **HOW:** 
  1. Compute the $d_{ik}$ distance matrix between a control panel of 10–20 coronaviruses with known hosts and the candidate host genomes; report the classification accuracy.
  2. Calculate the effective number of codons ($ENC$) vs. GC3s plot and dinucleotide odds ratios ($\rho_{CpG} = f_{CpG} / (f_C f_G)$) for 2019-nCoV to test whether codon usage variance is explained by mutational bias rather than host translational selection.

#### 3. Perform Formal Statistical Recombination Testing and Show Bootscan Support
* **WHY:** Visual inspection of a SimPlot similarity drop against a single sister clade (Clade A) without a second donor lineage cannot distinguish recombination from lineage-specific rate acceleration in the spike S1 subunit. Furthermore, referencing "Bootscanning plot analysis (data not shown)" in Section 4 violates basic reporting standards.
* **WHAT:** Apply formal statistical recombination detection methods across the ungrouped alignment and include the bootscan figure.
* **HOW:** Run the alignment of 2019-nCoV and individual representative *Sarbecovirus* genomes (rather than consensus clades grouping 267 disparate viruses into "Clade C") through RDP4 (implementing RDP, GENECONV, BootScan, MaxChi, Chimaera, SiScan, and 3Seq) and HyPhy GARD. Report the Bonferroni-corrected $p$-values and 95% confidence intervals for any inferred breakpoints.

#### 4. Temper Title, Abstract, and Discussion Claims Regarding Snakes and Transmission
* **WHY:** Even with whole-genome CDS data, synonymous codon usage is a weak, non-specific correlate of viral host range that cannot identify a specific reservoir species.
* **WHAT:** Remove claims that snakes are the likely wildlife reservoir of 2019-nCoV and that spike recombination caused "limited person-person spread."
* **HOW:** Revise the Abstract, Section 1 (line 24), Section 3.3 (line 74), and Section 4 (lines 150–156) to frame the sequence comparison strictly as showing high overall genome identity to *Rhinolophus* bat coronaviruses (ZC45/ZXC21) with localized divergence in the S1 coding region.

#### 5. Technical, Mathematical, and Editorial Cleanup
* **WHY:** Multiple numerical inconsistencies and grammatical errors across sections obscure the exact dataset analyzed.
* **WHAT & HOW:**
  * **Sample size inconsistency:** Section 2.1 states 271 GenBank sequences plus MN908947 (= 272 genomes total, matching Figure 1 caption and Section 4 line 150), but Section 3.1 line 58 states "Phylogenetic analysis of 276 coronavirus genomes" and sums Clade C (267) + Clade B (2) + Clade A (2) + 2019-nCoV (1) = 272. Reconcile the exact number of sequences (272 vs. 276) across all sections.
  * **CDS count error:** Section 2.3 (line 50) states "2019-nCoV genome (1CDS's, 9672 codons), bat-SL-CoVZC45 genome (1CDS's, 9680 codons)." Coronavirus genomes contain ~10–14 distinct open reading frames (ORF1ab, S, ORF3a, E, M, N, etc.), not "1 CDS"; clarify that all viral ORFs were concatenated into a single sequence per genome.
  * **Table 1 truncation and formatting:** Provide the full 59-codon RSCU table (currently truncated after Gln CAA at line 130) and capitalize *Manis javanica* in the Table 1 header.
  * **Grammatical fixes:** Correct repeated instances of "may occured" / "may occurred" (lines 8, 24, 61, 63, 150, 156) to "may have occurred" and "bat coronovirus" (lines 8, 24, 58, 156) to "bat coronavirus."
