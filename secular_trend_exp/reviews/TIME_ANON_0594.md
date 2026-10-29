<Blinded Review: TIME_ANON_0594>
**Composite Score:** 6.4 / 10.0 (Rigor: 2.0/3.5 | Claims: 1.5/2.5 | Biology: 1.5/2.0 | Reproducibility: 1.4/2.0)
**Bias Category:** Technical/Assay
**Verdict:** Major Revision
**Study Modality:** Hybrid Computational + Wet-Lab
**Technology Maturity:** Mid-Stage High-Throughput
**Epistemic Stage:** Basic/Mechanistic Discovery

OVERALL_SCORE: 6.4/10
VERDICT: CAVEATS
ESTIMATED_DECADE: 2020s

---

### 1. Executive Summary (SUMMARY)
This study (`TIME_ANON_0594`) isolates two psychrophilic basidiomycete yeasts from Arctic lichens—*Mrakia gelida* PAMC 26583 (from *Cladonia pyxidata*) and *Mrakia robertii* PAMC 26600 (from *Cetraria* sp.)—and generates hybrid whole-genome and linear mitochondrial genome assemblies using Oxford Nanopore PromethION long reads (`NextDenovo` / `Flye`) polished with Illumina HiSeq short reads (`NextPolish`). The nuclear assemblies span 34.1–34.2 Mb (28 contigs, 91.4% Basidiomycota BUSCO completeness, 8,918–8,919 BRAKER3 genes) for *M. gelida* PAMC 26583 and 28.7–29.0 Mb (15 contigs, 92.1% BUSCO completeness, 8,131 genes) for *M. robertii* PAMC 26600 (the first genome assembly for *M. robertii*). The authors also assemble the first annotated linear mitogenomes (20,924 bp and 21,508 bp) for the genus *Mrakia*, perform comparative orthogroup (`OrthoVenn3`) and gene-family expansion/contraction (`CAFE5`) analyses across 12 Tremellomycetes/Ustilaginomycetes genomes, catalog CAZymes (`dbCAN2`) and peptidases (`MEROPS`), and test extracellular protease/lipase activities on agar plates as well as 4-L bioreactor ethanol fermentation under low (<5%) vs. high (>50%) dissolved oxygen (DO).

While the hybrid nuclear and mitochondrial genome assemblies and public data depositions (NCBI SRA `PRJNA1288782`, ENA `PRJEB100863`/`PRJEB100532`, and Figshare) are valuable genomic resources for psychrophilic yeasts, the manuscript is marred by severe internal contradictions and unit errors in the fermentation and phenotypic sections—most notably conflating `5.46 g/L` of ethanol with `5.46% (v/v)` in the text, reporting three different fermentation temperatures (`12 °C` in Results vs. `13 °C and 16 °C` in Methods) that confound temperature with dissolved oxygen, and listing the host lichen species names as the "Scientific name of strain" in Table 1.

### 2. Methodological & Statistical Audit (WEAKNESSES & METHODOLOGICAL AUDIT)
* **Severe Unit Error Conflating `g/L` with `% (v/v)` Ethanol in Results Line 172 (~8-Fold Overstatement of Ethanol Concentration):**
  - In the Figure 5d–g legend (line 165) and y-axis, ethanol concentration is plotted in **`g/L`**, and the legend states: *"PAMC 26583 showed significantly greater ethanol production under low DO, reaching a maximum of **5.46 g/L** at 48 h"*.
  - However, in the main text of Results ("Alcohol production", line 172), the authors write: *"The ethanol concentration increased rapidly during the initial 48 h, reaching **5.46% (v/v)**, with the corresponding cell growth reaching a cell density (OD600) = 11.5. After prolonged incubation (120 h), the ethanol concentration decreased to **2.4% (v/v)**"*.
  - Four sentences later, for PAMC 26600 (line 176), they correctly convert `2.4 g/L` to `% (v/v)`: *"the ethanol concentration reached **2.4 g/L (approximately 0.3% v/v)** after 120 h"*.
  - Because the density of ethanol is $0.789\text{ g/mL}$, $5.46\text{ g/L}$ is only **$0.69\%\text{ (v/v)}$** (and $2.4\text{ g/L}$ is $0.30\%\text{ (v/v)}$)—not $5.46\%\text{ (v/v)}$ (which would equal $43.1\text{ g/L}$, impossible from standard 20 g/L glucose YPD media where the theoretical maximum Gay-Lussac yield is $\le 10.2\text{ g/L}$!). Misreporting `5.46 g/L` as `5.46% (v/v)` in line 172 is a major quantitative error.
* **Contradictory Fermentation Temperatures Between Results and Methods, Confounding Dissolved Oxygen with Temperature:**
  - In Results (line 170), the authors state that ethanol production was evaluated *"under controlled dissolved oxygen (DO) conditions at **12 °C** (Fig. 5 d–g)"*.
  - However, in Materials and Methods ("Ethanol fermentation experiments", tail line 35), they state that the strains *"were cultivated in YPD media under low (< 5%) and high (> 50%) dissolved oxygen (DO) conditions at **13 °C and 16 °C, respectively**"*.
  - First, `12 °C` directly contradicts `13 °C and 16 °C`. Second, if low-DO was run at `13 °C` while high-DO was run at `16 °C` (which is above the strains' 4–10 °C optimum and close to their upper thermal limit), then temperature is completely confounded with dissolved oxygen in Fig. 5d–g! Furthermore, the bioreactor runs in Fig. 5d–g have no biological replicates ($n = 1$ time series per condition) and no error bars.
* **Taxonomic Mislabeling in Table 1 ("Scientific name of strain"):**
  - In Table 1 (line 35), the row labeled `"Scientific name of strain"` lists **`Cladonia pyxidata`** for PAMC 26583 and **`Cetraria sp.`** for PAMC 26600. *Cladonia pyxidata* and *Cetraria* sp. are the **host lichens** from which the yeasts were isolated (as stated in line 28), not the scientific names of the yeast strains (*Mrakia gelida* and *Mrakia robertii*).
* **Multiple Internal Inconsistencies Across Text, Tables, and Methods:**
  - **Upper growth temperature limit:** Introduction (line 16) and Results (line 162) state that both strains *"cannot grow above 20 °C"*, whereas Results line 28 and Table 1 (lines 52–53) report positive growth (`+`) at `20 °C` and `"no growth above 25 °C"`.
  - **Enzyme assay temperatures:** Results line 162 and Fig. 5a report protease, lipase, and chitinase assays at `4, 10, and 20 °C`, whereas Materials and Methods (line 214) states they *"were tested at 4 °C and 10 °C"*.
  - **Genome size and gene count discrepancies:** Line 66 reports assembled genome sizes of `34.082 Mb` (scaffold length `33.9 Mb`) and `28.729 Mb`, whereas Table 2 (line 75) reports `34.211 Mb` and `28.976 Mb`; line 118 reports `8,919` predicted genes for PAMC 26583, whereas Table 2 (line 80) reports `8918`.
  - **Duplicate Methods sentences with conflicting software versions:** In "Gene annotation" (tail line 11) and "Repetitive sequence annotation" (tail line 16), the authors state `EggNOG-mapper (v2.1.13)` and `RepeatMasker (v4.2.0)` in the first half of the paragraph and then repeat the same steps with `EggNOG mapper (v.2.1.12)` and `RepeatMasker (v4.0.7)` three sentences later.

### 3. Biological / Experimental Grounding & Claim Proportionality (STRENGTHS)
* **`[Well Supported]` High-contiguity hybrid nuclear and linear mitochondrial genome assemblies for *M. gelida* PAMC 26583 and *M. robertii* PAMC 26600:**
  - The combination of ONT PromethION long reads, Illumina polishing, RNA-Seq-assisted BRAKER3 annotation (~90–92% BUSCO completeness), and `Flye` linear mitogenome assembly (confirming loss of mitochondrial *cox2* and *atp8* and potential *nad2-nad3* fusion in Mrakiaceae) is bioinformatically solid and well-documented.
* **`[Moderately Supported]` Expansion of histone gene clusters (H2A, H2B, H3, H4) and MFS transporters in the *Mrakia* / Cystofilobasidiales lineage:**
  - The `OrthoVenn3` and `CAFE5` comparative analyses across 12 basidiomycete genomes clearly document elevated histone copy numbers and 58–59 MFS transporter genes in both *Mrakia* species.
* **`[Overstated]` Reporting `5.46% (v/v)` ethanol production in Results line 172:**
  - Actually `5.46 g/L` ($\approx 0.69\%\text{ v/v}$) according to Fig. 5d and its legend.

### 4. Reproducibility & Data Completeness
* **Comprehensive Multi-Repository Data Availability (`1.4 / 2.0`):**
  - Raw ONT and Illumina reads (`PRJNA1288782`, `SRX29599295–SRX29599302`), nuclear and mitochondrial genome assemblies (`GCA_977009815`, `GCA_977005135`, `GCA_977005115`, `GCA_977005125` under `PRJEB100863` and `PRJEB100532`), and protein/annotation/orthogroup files (`Figshare: 10.6084/m9.figshare.29500520.v1`) are all publicly deposited. Score is tempered by the conflicting software version numbers and temperature parameters in the Methods text.
</Blinded Review: TIME_ANON_0594>
