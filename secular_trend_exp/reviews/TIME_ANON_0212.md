</Agent System Instructions>
<Blinded Review: TIME_ANON_0212>
**Composite Score:** 8.3 / 10.0 (Rigor: 2.9/3.5 | Claims: 2.0/2.5 | Biology: 1.7/2.0 | Reproducibility: 1.7/2.0)
**Bias Category:** None (Methodologically Sound)
**Verdict:** Minor Revision
**Study Modality:** Hybrid Computational + Wet-Lab
**Technology Maturity:** Mid-Stage High-Throughput
**Epistemic Stage:** Basic/Mechanistic Discovery

---

### 1. Executive Summary
This study presents the first comprehensive molecular phylogeny, divergence-time estimation, and historical biogeographic reconstruction of the Old World tropical satyrine butterfly subtribe Mycalesina (Lepidoptera: Nymphalidae: Satyrinae). The authors assembled a molecular dataset comprising 195 taxa (185 ingroup Mycalesina species across all 11 recognized genera plus 10 outgroups) sequenced across up to 10 gene regions (one mitochondrial gene, *COI*, and nine nuclear protein-coding genes: *EF-1$\alpha$*, *wingless*, *RpS5*, *RpS2*, *CAD*, *GAPDH*, *IDH*, *MDH*, and *CAT*, totaling 7,735 bp with ~70% average gene coverage). Using maximum likelihood (RAxML, partitioned by gene and codon position), Bayesian inference (MrBayes), Bayesian relaxed-clock dating (BEAST with secondary calibrations and host-plant constraints), and dispersal-extinction-cladogenesis modeling (LAGRANGE), the authors demonstrate that Mycalesina is monophyletic and comprises seven strongly supported major clades, establish the paraphyly of *Mycalesis* (transferring *M. mnasicles* and *M. amoena* to the resurrected genus *Culapa* Moore, 1879), and reconstruct an Asian origin followed by two independent Oligocene colonizations of continental Africa (*Hallelesis* + *Bicyclus* and *Heteropsis*) and subsequent radiations onto Madagascar and back into Asia.

### 2. Methodological & Statistical Audit
- **Taxon & Locus Sampling:** Sampling 185 of ~300–400 known species across the full geographic range (Asia, Australia, Africa, Madagascar) with 9 nuclear loci plus *COI* (average 7 loci per taxon) provides strong phylogenetic resolving power across both deep Oligocene nodes and younger Miocene/Pliocene clades.
- **Partitioning & Phylogenetic Inference:** The authors appropriately evaluated six partitioning schemes (from unpartitioned to 20 partitions by gene and codon position $1+2$ vs. $3$) using AIC and BIC in PartitionFinder/jModelTest, demonstrating that accounting for third-codon-position saturation in *COI* and nuclear genes improves model fit (Table 2).
- **Sensitivity to Outgroup Selection & Long-Branch Attraction:** The authors explicitly tested whether the basal position of the Sulawesi-endemic genus *Lohora* was an artifact of long-branch attraction to distant outgroups by re-running analyses with all outgroups excluded and with individual outgroups included one at a time. The topology remained invariant, confirming the robustness of the root placement.
- **Terminological Discrepancy Between Crown Age and Stem Age:**
  - In the Abstract (line 6), the authors state: *"Dating analyses suggest the crown age of the subtribe to be 40 Mya."*
  - However, in the Results (line 138) and Figure 3, ~39.8 Mya (95% HPD: 32.8–47.7 Mya) is the **stem age** of Mycalesina (the divergence between Mycalesina and its sister subtribe Lethina), whereas the **crown age** of Mycalesina (the split between *Lohora* and the remaining six genera) is 28.0 Mya (95% HPD: 25.0–31.6 Mya). The Abstract and Discussion should be corrected to distinguish stem age (~40 Mya) from crown age (~28 Mya).
- **Secondary Calibration Circularity Caveat:** Due to the absence of fossil Mycalesina, divergence times rely on secondary normal priors taken from Peña et al. (2011) alongside a maximum bound corresponding to the origin of grasses (Poaceae). The authors appropriately acknowledge the wider uncertainty of secondary calibrations and report full 95% HPD intervals.

### 3. Biological / Experimental Grounding & Claim Proportionality
- **Claim 1:** The subtribe Mycalesina is monophyletic and comprises seven major well-supported clades, requiring the resurrection of *Culapa* Moore, 1879 for the *Mycalesis mnasicles* group (*Culapa mnasicles* comb. rev. and *Culapa amoena* comb. nov.). `[Well Supported]` — Supported by $\text{PP} = 1.00$ and $\text{BS} = 100\%$ across all partitioning schemes, reinforced by shared male androconial and wing-pattern characters.
- **Claim 2:** All five Malagasy endemic genera (*Henotesia*, *Houlbertia*, *Masoura*, *Admiratio*, *HTB*) and the Asian *Telinga* clade nest within *Heteropsis*, which originated in Africa and subsequently colonized Madagascar once (~20.8 Mya) and dispersed back to Asia (~12.6 Mya). `[Well Supported]` — Strongly supported by both phylogenetic topology ($\text{PP} = 1.00$, $\text{BS} = 99\%$) and LAGRANGE ancestral area reconstruction.
- **Claim 3:** Oligocene grassland expansion and Miocene forest fragmentation drove the parallel radiations of African *Bicyclus* (~100 spp.), Malagasy *Heteropsis* (~70 spp.), and Indo-Australian *Mycalesis* + *Mydosama* (~140 spp.). `[Moderately Supported]` — Chronologically consistent with the 26–15 Mya divergence dates, though explicit diversification-rate shift models (e.g., MEDUSA, BAMM, BiSSE) were not fitted.

### 4. Reproducibility & Data Completeness
- **Strengths:** Voucher codes, collection localities, GenBank accession numbers for all newly generated sequences, primer citations, PartitionFinder/MrBayes/RAxML/BEAST/LAGRANGE configuration parameters, and formal taxonomic nomenclature acts are thoroughly documented.
- **Weaknesses:** The truncated end of the Methods section should ensure a permanent Dryad/TreeBASE accession link for the concatenated 7,735-bp alignment and BEAST XML / tree files.
</Blinded Review: TIME_ANON_0212>
