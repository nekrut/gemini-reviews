<Blinded Review: TIME_ANON_0758>
**Composite Score:** 6.7 / 10.0 (Rigor: 2.2/3.5 | Claims: 1.6/2.5 | Biology: 1.4/2.0 | Reproducibility: 1.5/2.0)
**Bias Category:** Statistical/Design
**Verdict:** Major Revision
**Study Modality:** Wet-Lab Primary Experimental
**Technology Maturity:** Mature/Classical
**Epistemic Stage:** Basic/Mechanistic Discovery

OVERALL_SCORE: 6.7/10
VERDICT: CAVEATS
ESTIMATED_DECADE: 2000s

---

### 1. Executive Summary / SUMMARY
This canine population genetics study characterizes the genetic diversity and phylogenetic affinities of the feral Bali Street Dog (BSD) population by genotyping $n=40$ randomly captured street dogs from the Denpasar region of Bali across 31 polymorphic autosomal microsatellite markers (run on an ABI 377 slab-gel sequencer and scored with `STRand`). The BSD genotypes are compared against $n=20$ captive Australian dingoes and 28 American Kennel Club (AKC) breeds ($n=19$–$20$ per breed). The authors report that the BSD exhibits the highest allelic richness (239 of 366 total alleles across all 30 subpopulations; 214.6 alleles when rarefied/bootstrapped to $n=20$), highest observed ($H_O = 0.692$) and expected ($H_E = 0.736$) heterozygosity, lowest inbreeding coefficient ($F_{IS} = 0.097$), 10 unique private alleles plus 3 alleles shared exclusively with the Australian dingo at locus `C10.404`, and closest genetic distance ($D_A = 0.242$, $F_{ST} = 0.088$–$0.126$) and neighbor-joining clustering (87–90% bootstrap support) with East Asian/Australasian populations (Chow Chow, Australian dingo, Akita). While the empirical microsatellite dataset and sample-size rarefaction analysis are solid, the manuscript over-interprets these 31-STR summary statistics to claim that a viable dog population existed on Bali *prior to its geographic isolation ~12,000 years ago*—a chronological claim that is unsupported by coalescent dating and conflicts with archaeological and paleogenomic timelines for Austronesian dog dispersal into Island Southeast Asia (~3,500–5,000 years ago).

### 2. Methodological & Statistical Audit / STRENGTHS & WEAKNESSES

#### STRENGTHS
- **Sample-Size Rarefaction Bootstrap Control:** Because 40 BSD individuals were sampled versus 19–20 individuals for the dingo and each AKC breed, the authors appropriately performed 10,000 bootstrap subsamplings of $n=20$ BSDs (Table 2), confirming that BSD allelic richness (214.6 vs. 144 in dingo and 138.8 mean in AKC breeds) and expected heterozygosity ($0.727$ vs. $0.511$ and $0.573$) remain substantially higher after equalizing sample size.
- **Complementary Stepwise ($R_{ST}$) and Infinite-Alleles ($F_{ST}$) Differentiation Metrics:** Computing both Weir & Cockerham's $F_{ST}$ and Slatkin's stepwise-mutation $R_{ST}$ across all 31 loci (Table 1) provides a useful check on mutational vs. drift-driven differentiation across subpopulations.
- **Full Raw Genotype Deposition:** Providing the complete individual-level microsatellite genotype matrix (`Supplement2.xls`) and PCR multiplex conditions (`Supplement1.xls`) is a major strength for transparency and re-analysis.

#### WEAKNESSES & METHODOLOGICAL AUDIT
- **Internal Inconsistency in Private Allele Counts & Frequency Math (Table 3 vs. Abstract/Text):**
  1. The Abstract states: *"Thirteen private alleles were observed in the BSD with an additional three alleles observed only in the BSD and the Australian dingo"* (which would be 16 alleles total). However, the Results text (line 98) and Table 3 report **10 private alleles** in the BSD plus **3 alleles shared with the dingo** (13 rows total in Table 3). The Abstract conflated the total rows in Table 3 (13) with BSD-only private alleles (10) and then added the 3 dingo-shared alleles a second time!
  2. In the text describing Table 3 (line 98), the authors state that at locus `C10.404`, *"The BSD and the Australian dingo also shared three alleles not seen in any AKC breed at locus C10.404 with a combined frequency of 16.25% in the BSD and 75% in the Australian dingo."* Looking at Table 3, there are actually *four* alleles listed at `C10.404` (`168`, `170`, `172` shared with Dingo, and `174` private to BSD), where $0.0375 + 0.0625 + 0.0625 = 0.1625$ (3/80 + 5/80 + 5/80) for the three shared alleles and an additional $0.0375$ (3/80) for allele `174`.
- **Table 4 Caption vs. Matrix Content Mismatch:** The caption for Table 4 states *"Nei's DA distance (lower triangle) and mean FST estimates (upper triangle) between each pair of 9 dog subpopulations represented graphically in Figure 3"*, but the table actually prints a **30 $\times$ 30 matrix** of all 30 breeds! Furthermore, closer inspection of row/column `MBT` (Miniature Bull Terrier) in Table 4 reveals a transposed/corrupted block: in the lower triangle (`DA`), `MBT` vs `BMD`, `BS`, `BT` are `0.42, 0.34, 0.37`, whereas in the upper triangle (`FST`) at `MBT` vs `BMD`, `BS`, `BT`, the values jump to `0.54, 0.52, 0.54` (which are actually the `DA` distances of `BLT`!), proving that the upper/lower triangles of Table 4 were scrambled around rows `BLT`/`MBT` during manual spreadsheet formatting.
- **No Multiple-Testing Correction for 930 HWE Tests:** Testing Hardy-Weinberg equilibrium across 31 loci $\times$ 30 populations = 930 tests at an unadjusted $\alpha = 0.05$ yields an expected $930 \times 0.05 = 46.5$ false-positive deviations by chance alone. Thus, observing 3–4 loci with $p < 0.05$ in BSD and AKC breeds is completely consistent with random noise under the null hypothesis, whereas only the dingo (12 loci with $p < 0.05$, $F_{IS} = 0.194$, likely due to sampling captive dingoes from multiple regional backgrounds—Wahlund effect—or captive inbreeding) shows genuine departure.
- **Linked Markers Treated as Independent:** Five autosomes (`CFA06`, `CFA11`, `CFA15`, `CFA20`, `CFA23`) are represented by two markers each (average spacing ~23.5 cM), plus one unmapped marker (`PEZ02`), slightly violating the assumption of independent loci in bootstrap and structure analyses.
- **Absence of Admixture / Clustering Analysis (`STRUCTURE`):** Relying solely on pairwise $F_{ST}/D_A$ and a 9-population Neighbor-Joining tree (arbitrarily selecting 4 non-Asian breeds out of 25) cannot distinguish ancient shared ancestry from modern admixture or quantify the actual proportion of European vs. East Asian ancestry in the BSD.

### 3. Biological / Experimental Grounding & Claim Proportionality
- **Claim 1:** *The Bali Street Dog is highly genetically diverse ($H_E = 0.736$) and clusters genetically with East Asian dog breeds (Chow Chow, Akita) and the Australian dingo.* `[Well Supported]` — Robustly demonstrated by allelic richness, rarefied heterozygosity, private allele sharing with the dingo, and genetic distance metrics.
- **Claim 2:** *A viable and diverse population of dogs existed on the island of Bali prior to its geographic isolation approximately 12,000 years ago.* `[Overstated]` — Completely unsupported by the data. High heterozygosity and shared alleles with Chow Chow and dingo in a street dog population are fully explained by the introduction of domestic dogs during the Neolithic/Austronesian expansion (~3,500–5,000 years BP, which the authors themselves note is when dingoes arrived in Australia and humans expanded from China/Taiwan into Indonesia) maintained at a large effective population size ($N \approx 800,000$) without breed bottlenecks. No coalescent or divergence-time modeling is performed to support a $>12,000$-year Pleistocene presence on Bali.

### 4. Reproducibility & Data Completeness
- **Data & Protocol Completeness:** Very strong; both the full PCR primer/multiplex protocol (`Supplement1.xls`) and the complete individual-level genotype matrix (`Supplement2.xls`) are provided as supplementary files, alongside exact software versions (`STRand`, `Genepop v3.4`, `DISPAN`, `POPTREE`, `TREEVIEW v1.6.6`).
</Blinded Review: TIME_ANON_0758>
