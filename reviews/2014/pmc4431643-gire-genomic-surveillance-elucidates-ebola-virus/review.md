# Review of PMC4431643 (PMID:25214632)

**Manuscript Title:** Genomic surveillance elucidates Ebola virus origin and transmission during the 2014 outbreak  
**Authors:** Gire SK, Goba A, Andersen KG, Sealfon RS, Park DJ, Kanneh L, Jalloh S, Momoh M, Fullah M, Dudas G, Wohl S, Moses LM, Yozwiak NL, Winnicki S, Matranga CB, Malboeuf CM, Qu J, Gladden AD, Schaffner SF, Yang X, Jiang PP, Nekoui M, Colubri A, Coomber MR, Fonnie M, Moigboi A, Gbakie M, Kamara FK, Tucker V, Konuwa E, Saffa S, Sellu J, Jalloh AA, Kovoma A, Koninga J, Mustapha I, Kargbo K, Foday M, Yillah M, Kanneh F, Robert W, Massally JL, Chapman SB, Bochicchio J, Murphy C, Nusbaum C, Young S, Birren BW, Grant DS, Scheiffelin JS, Lander ES, Happi C, Gevao SM, Gnirke A, Rambaut A, Garry RF, Khan SH, Sabeti PC.  
**Journal / Preprint:** *Science* (2014; `PMC4431643` / `PMID:25214632` / `10.1126/science.1259657`)  
**Calibration Study Cohort:** Cohort B — Validated Control (`B46` | Double-Blinded as `ANON_84`)  
**Overall Score:** **9.2 / 10.0** (Exemplary)
* **Score Breakdown:** Rigor: 3.2/3.5 | Claims: 2.3/2.5 | Biology: 1.9/2.0 | Reproducibility: 1.8/2.0

---

## 1. Executive Summary & Synthesis

`ANON_84` presents real-time genomic surveillance of the 2014 West African Ebola virus (`EBOV`) outbreak in Sierra Leone. The authors sequenced 99 `EBOV` genomes from 78 patients (representing $>70\%$ of confirmed cases diagnosed in Sierra Leone from late May through mid-June 2014) to a median coverage depth of $\sim 2,000\times$ using Nextera library preparation and Illumina sequencing, validated across independent technical replicates and four alternative library preparation protocols (Fig. S1, Table S2). In addition, metagenomic sequencing of 35 `EBOV`-negative suspected cases identified coinfections and differential diagnoses including Lassa virus, HIV-1, enterovirus A, and *Plasmodium* parasites.

Combining the 78 patient consensus genomes with 3 published Guinean sequences and 20 historical `EBOV` genomes, the authors identify 341 fixed substitutions separating the 2014 West African lineage from historical central African viruses, 55 single-nucleotide polymorphisms (SNPs) arising within the 2014 outbreak, and 263 intrahost single-nucleotide variants (`iSNVs`, Minor Allele Frequency $\ge 0.5\%$ validated across duplicate libraries). Integrating phylogenetic and molecular clock reconstruction (`BEAST`, `RAxML`) with epidemiological contact-tracing records from Kenema Government Hospital (`KGH`), the study traces the divergence of the 2014 West African lineage from central African `EBOV` to $\sim 2004$, dates the most recent common ancestor (`tMRCA`) of the 2014 outbreak to late February 2014, demonstrates the simultaneous co-introduction of two genetically distinct Guinean lineages (`cluster 1` and `cluster 2`) into Sierra Leone via a single traditional healer's funeral in May 2014, and proves human-to-human transmission of a sub-consensus intrahost variant (`position 10,218`) that subsequently fixed to define `cluster 3` (Fig. 3D, F). All sequence reads and assemblies were released immediately into the public domain (`NCBI BioProject PRJNA257197`) prior to publication, and every genomic position overlapping existing PCR diagnostic assays (`Table S3`) was systematically cataloged.

---

## 2. Claim-by-Claim Audit

1. **The 2014 West African `EBOV` outbreak diverged from central African lineages around 2004 (`tMRCA`: July 2004; 95% HPD: October 2002–May 2005) and arose from a single zoonotic introduction into the human population in late February 2014 (`Fig. 2`, `Fig. S5`):** `[Well Supported]`
   - Molecular clock dating (`BEAST`) and root-to-tip regression (`Fig. 2C–E`) show strong temporal clock signal across historical and 2014 isolates, refuting the hypothesis that the 2014 variant had been cryptically endemic in West Africa since the 1976 split while supporting a single zoonotic spillover in Guinea in early 2014 followed by sustained human-to-human transmission.

2. **The Sierra Leone outbreak stemmed from the simultaneous introduction of two genetically distinct viruses (`cluster 1` and `cluster 2`, differing by 5 SNPs) linked to a single funeral in Guinea (`Fig. 3A–C`):** `[Well Supported]`
   - Independent contact-tracing investigations (`Fig. 3A`) and genomic phylogenies (`Fig. 3B–C`) converge directly: the earliest Sierra Leonean cases attended the funeral of a Guinean traditional healer who had treated `EBOV` patients, and their viral sequences partition into two distinct clades (`cluster 1`, $n=6$, and `cluster 2`) separated by 5 mutations acquired in Guinea prior to cross-border transmission.

3. **Shared intrahost variation (`iSNV` at position `10,218` with $5\% < \text{MAF} < 95\%$ in 12 patients) demonstrates human-to-human transmission of a mixed viral population across multiple hosts (`Fig. 3D, F`):** `[Well Supported]`
   - Intrahost variant calling was rigorously filtered ($\ge 2,000\times$ coverage, duplicate independent libraries per sample, comparison of Nextera vs. Epicentre/TruSeq/NuGEN protocols in `Fig. S1` and `Table S2`). The probability of recurrent *de novo* mutation at position `10,218` across 12 epidemiologically linked patients is negligible ($p < 10^{-9}$), providing direct empirical proof of a wide enough transmission bottleneck in `EBOV` to co-transmit both alleles of a polymorphism before its fixation in `cluster 3`.

4. **The observed intra-outbreak substitution rate ($\sim 1.9 \times 10^{-3}\text{ substitutions/site/year}$, `Fig. 4F`) is roughly double the inter-outbreak evolutionary rate ($\sim 0.8 \times 10^{-3}\text{ substitutions/site/year}$) and reflects incomplete purifying selection over short sampling windows (`Fig. 4F–G`):** `[Well Supported]`
   - The authors explicitly compare the ratio of nonsynonymous to synonymous variants (`dN/dS`, `Fig. 4G`) across intrahost (`iSNV`), intra-outbreak (`2014`), and inter-outbreak branches, correctly attributing the elevated short-term substitution rate and enriched nonsynonymous polymorphism to transient deleterious/slightly deleterious mutations that have not yet been purged by purifying selection (`line 56`), rather than claiming adaptive acceleration of the viral polymerase.

---

## 3. Technical & Methodological Critique

### 3.1. Time-Dependent Evolutionary Rate Effects on Deep vs. Shallow Node Dating
- As shown in `Fig. 4F–G`, the short-term intra-outbreak evolutionary rate ($\sim 1.9 \times 10^{-3}\text{ subs/site/year}$) is more than twice the long-term inter-outbreak rate ($\sim 0.8 \times 10^{-3}\text{ subs/site/year}$) due to incomplete purifying selection on terminal branches. When a single relaxed molecular clock model in `BEAST` is fit simultaneously to tips sampled over a 3-month window (`March–June 2014`) and historical outbreaks spanning 38 years (`1976–2014`), the rate elevation on shallow 2014 branches can pull the inferred `tMRCA` of the intermediate split (`2004`, 95% HPD `2002–2005`) slightly toward the present unless a time-dependent rate model or internal-branch partitioning is applied. The authors mitigate this by performing separate root-to-tip and `BEAST` analyses with and without the 1976 root and by comparing intra- vs. inter-outbreak clocks (`Fig. S5`, `Fig. 4F`), which yields consistent overlap.

### 3.2. Geographic Sampling Asymmetry in Guinea vs. Sierra Leone
- Whereas Sierra Leonean cases were densely sampled ($>70\%$ of confirmed cases through mid-June 2014 via `KGH`), only 3 Guinean genomes from March 2014 were available for comparison. Consequently, as the authors appropriately caveat on line 44 (*"in areas represented by available sequence data"*), additional unsampled viral sublineages circulating concurrently in Guinea or Liberia during May–June 2014 could not be ruled out.

### 3.3. Minor Textual Typo
- In the caption to `Fig. 2` (`line 30`), *"Rooting the phytogeny"* should read *"Rooting the phylogeny"*.

---

## 4. Actionable Recommendations

1. **Partition Terminal vs. Internal Branch Clocks in `BEAST`:**
   - In supplementary molecular clock sensitivity analyses, fit a two-epoch or internal/external branch-partitioned substitution model in `BEAST` to verify that transient nonsynonymous mutations within the 3-month 2014 outbreak window do not bias the `tMRCA` estimate of the 2004 divergence node.
2. **Correct Typographical Error in `Fig. 2` Caption:**
   - Replace `"phytogeny"` with `"phylogeny"` on line 30.
