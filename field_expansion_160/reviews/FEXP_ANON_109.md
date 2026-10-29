# Forensic Review of `FEXP_ANON_109`

**Overall Score:** **3.3 / 10.0** (Flawed / Overstated) | **Scientific Core Score:** **2.5 / 8.0**
* **Score Breakdown:** Rigor: 0.9/3.5 | Claims: 0.8/2.5 | Biology: 0.8/2.0 | Reproducibility: 0.8/2.0

---

## 1. Blinded Metadata Perception

* **Perceived Field & Subfield:** Conservation Genetics, Molecular Phylogenetics & Biogeography (Mitochondrial genome sequencing and MaxEnt species distribution modeling of the endangered spotted pond turtle *Geoclemys hamiltonii* across the Indus–Ganges–Brahmaputra river basins).
* **Study Design Archetype:** Dual-component study combining (1) Illumina NovaSeq 6000 mitogenome sequencing (`16,509 bp`, GenBank `OP344485`) and 13-PCG Bayesian/ML phylogenetics across 42 Geoemydidae turtles, and (2) MaxEnt 3.4.4 habitat suitability modeling (`n = 136` GBIF/literature points) and `FRAGSTATS` patch metrics under CMIP6 (`BCC-CSM2-MR`, SSP245 and SSP585 for 2021–2040 and 2061–2080).
* **Temporal & Venue Signals:** Post-2023 South Asian conservation genetics + SDM study sharing verbatim SDM boilerplate with `FEXP_ANON_102`.

---

## 2. Executive Summary & Editorial Verdict

This study sequences and characterizes the complete mitochondrial genome (`16,509 bp`, GenBank `OP344485`) of an adult male spotted pond turtle (*Geoclemys hamiltonii*) sampled in New Delhi, India, reconstructs a 13-PCG Bayesian and Maximum Likelihood phylogeny of 42 Geoemydidae species, and models current and future habitat suitability (`MaxEnt`) and fragmentation (`FRAGSTATS`) across the Indus–Ganges–Brahmaputra (IGB) river basins.

**Editorial Verdict: Reject / Major Revision Required (Flawed / Overstated).** Both the mitogenomic component and the ecological modeling component contain serious technical and reporting defects:
1. **Truncated Mitogenome Table, Codon/Anticodon Inversion, and Stop-Codon Contradictions:** In Table 1 ("List of annotated mitochondrial genes of *Geoclemys hamiltonii*", lines 88–124), the gene annotation table is truncated after `trnE` (`14,162–14,229`), omitting the final $2,280\text{ bp}$ of the mitogenome (`cytb`, `trnT`, `trnP`, and the Control Region). Worse, **every single one of the 20 tRNAs listed in Table 1 reports the mRNA codon (e.g., `ATG` for `trnM`, `TTC` for `trnF`, `GAA` for `trnE`) instead of the tRNA anticodon (`CAT`, `GAA`, `TTC`)** under the `Anti-codon` column header. In addition, the Results prose (line 125) states that five PCGs (`nad1`, `nad2`, `cox3`, `nad4`, `cytb`) have **incomplete** `TAA` stop codons (consistent with their non-triplet lengths in Table 1: `nad1 = 968 bp`, `nad2 = 1,039 bp`, `cox3 = 784 bp`), whereas Table 1 lists complete `TAA` stop codons for all of them.
2. **Contradictory Animal Ethics Statement & Unknown Wild Provenance:** In Methods (line 30), the authors state that sedating an endangered CITES Appendix I / Indian Schedule I turtle with subcutaneous Alfaxalone (`20–30 mg/kg SC`) and drawing hind-limb blood *"is not concerned with animal ethics issues, and does not require ethics committee or institutional review board approval"*, and in the very next sentence contradict themselves by claiming *"The experimental protocols were approved by the host institutions"* without providing any ethics approval or Schedule I wildlife permit number. Because the turtle was an ornamental commercial specimen found in New Delhi without wild locality provenance, claims that this sequence represents a native Indian wild population (as opposed to the captive Chinese sequence `ON243873` from which it differs by only $7\text{ bp}$ out of $16,509\text{ bp}$) are unsubstantiated.
3. **SDM Validation & Landscape Metric Confusion (`LPI` vs. `LSI`):** The MaxEnt workflow confuses 50-run bootstrap replication with $n-1$ leave-one-out jackknife (line 70), reports only **training AUC** (`0.902 ± 0.016`, line 147) with no test AUC or TSS, fails to state how many predictors survived collinearity filtering, and repeatedly misinterprets the **Largest Patch Index (`LPI`)** as **"patch shape complexity"** (which is `LSI`, Landscape Shape Index) in both the Abstract (line 5) and Results (line 163).

### Assessment of Specific Claims

* **The 13-PCG Bayesian and ML phylogenies confirm the monophyly of Batagurinae and the sister relationship of G. hamiltonii to the Pangshura + Batagur clade (Abstract; Results, line 137; Fig. 3): `[Well Supported]`**  
  The concatenated 13-PCG tree topology agrees with established Testudines phylogenomic and mitogenomic trees (`Thomson et al., 2021`), recovering *G. hamiltonii* as sister to *Pangshura* + *Batagur* and recovering the known paraphyly of Geoemydinae relative to *Rhinoclemmys*.
* **Table 1 accurately annotates the gene coordinates, anticodons, and stop codons of the 16,509 bp G. hamiltonii mitogenome (Results, lines 88–125; Table 1): `[Methodologically Flawed]`**  
  Table 1 is truncated at base `14,229` (omitting `cytb`, `trnT`, `trnP`, and `CR`), lists mRNA codons instead of tRNA anticodons for all 20 tRNAs, and lists complete `TAA` stop codons for `nad1` (`968 bp`), `nad2` (`1,039 bp`), `cox3` (`784 bp`), and `nad4` (`1,377 bp` with a `+15 bp` spacer) in contradiction to the prose in line 125. Furthermore, Figure 2's legend (line 130) mislabels the Control Region secondary structure as *"the origin of L-strand replication"*.
* **Comparative habitat quality assessment shows that "patch shape complexity denoted by the LPI" is 71.3% higher in the western range (7.90) than in the eastern range (4.61) (Abstract, line 5; Results, line 163; Fig. 7): `[Methodologically Flawed]`**  
  In `FRAGSTATS`, `LPI` is the **Largest Patch Index** (the percentage of the landscape occupied by the largest patch), whereas **patch shape complexity** is measured by `LSI` (Landscape Shape Index). Confusing `LPI` with `LSI` invalidates the geometric interpretation of patch complexity in both the Abstract and Results.
* **Future climate change will reduce G. hamiltonii suitable habitat by 65.73%–70.53% in 2021–2040 ("over the next 50 years") and 70.31%–75.30% in 2061–2080 (Abstract; Results, line 155; Discussion, line 184): `[Fragile]`**  
  First, `2021–2040` is a contemporary/near-term window (already underway when the data were accessed in May 2023), not "50 years" in the future, making a sudden $65.7\text{--}70.5\%$ immediate drop relative to the baseline indicative of environmental clamping/mismatch between baseline and `BCC-CSM2-MR` rasters rather than gradual 50-year warming. Second, the model reports only training AUC (`0.902`), uses a single GCM (`BCC-CSM2-MR`), and does not report which predictors survived $|r| > 0.8$ filtering in the main text.

---

## 3. Forensic Defect Inventory

### 3.1. Mitogenome Annotation Errors & Truncated Table 1 (Pillar 3, Pillar 6 & Pillar 7)
* **Location:** Table 1 (lines 88–124), Results (line 125), and Figure 2 legend (line 130).
* **Defect 1 (Truncated Table 1):** Table 1 stops at `trnE` (`14,162–14,229`), omitting `cytb`, `trnT`, `trnP`, and `CR` (`14,230–16,509`).
* **Defect 2 (Codons Reported as Anticodons):** In Table 1, every tRNA entry in the `Anti-codon` column is actually the corresponding amino acid's **mRNA codon** (e.g., `trnF = TTC` instead of `GAA`; `trnV = GTA` instead of `TAC`; `trnL2 = TTA` instead of `TAA`; `trnI = ATC` instead of `GAT`; `trnQ = CAA` instead of `TTG`; `trnM = ATG` instead of `CAT`; `trnW = TGA` instead of `TCA`; etc.).
* **Defect 3 (Stop-Codon Contradictions):** Line 125 states that `nad1, nad2, cox3, nad4, and cytb` have incomplete `TAA` stop codons (`T--` or `TA-`), but Table 1 records complete `TAA` stop codons for `nad1`, `nad2`, `cox3`, and `nad4` (and a `+15 bp` intergenic spacer after `nad4`, where incomplete stop codons require polyadenylation cleavage at an immediately adjacent downstream tRNA).
* **Defect 4 ($O_L$ vs. Control Region Confusion):** Figure 2 caption (line 130) describes the Control Region domain map as *"The linear representation and stem-loop structure of the origin of L-strand replication"*, whereas $O_L$ is the 25-bp spacer between `trnN` and `trnC` (line 103).

### 3.2. Ethics / Regulatory Contradiction & Captive Specimen Provenance (Pillar 2 & Pillar 6)
* **Location:** Methods ("Species identification and sampling", line 30) and Discussion (line 176).
* **Defect:** Performing pharmacological sedation (`20–30 mg/kg Alfaxolone SC`) and venipuncture on a live CITES Appendix I / Indian Wildlife (Protection) Act Schedule I endangered vertebrate requires formal animal ethics and statutory wildlife permits; claiming it *"does not require ethics committee or institutional review board approval"* while simultaneously claiming *"The experimental protocols were approved by the host institutions"* without permit numbers is contradictory. Moreover, because the specimen was kept for *"ornamental commercial purposes"* in New Delhi, its geographic origin is unknown.

### 3.3. SDM Methodological Flaws & FRAGSTATS Metric Misidentification (Pillar 3, Pillar 4 & Pillar 7)
* **Bootstrap vs. $n-1$ Jackknife Confusion (Line 70):** Verbatim boilerplate shared with `FEXP_ANON_102`: *"we used the bootstrapping replication approach... The model utilized the training data on each occurrence point as n-1 and examined the model execution with the residual points and 50 runs as replicates."*
* **Training-Only AUC & Inequality Sign Typo (Lines 72, 147):** Line 72 writes *"`<0.9` is regarded as an exceptional model"* (instead of `>0.9`), and line 147 reports only training AUC (`0.902 ± 0.016`), with no test AUC or TSS.
* **`LPI` Misidentified as "Patch Shape Complexity" (Lines 5, 163):** Line 163 states *"The level of patch shape complexity denoted by the LPI for the west range (7.90) has increased by 71.3% compared to the eastern range (4.61)"*, confusing Largest Patch Index (`LPI`) with Landscape Shape Index (`LSI`).
* **Taxonomy Typo in Methods (Line 49):** Writes *"42 Geoemydinae species"* instead of `42 Geoemydidae species` (and misspells *Pangshura* as `"Paghshura"` in line 176 and Testudines as `"Testunines"` in line 127).

---

## 4. Quantitative Rubric Scoring

| Rubric Dimension | Score | Max | Forensic Justification |
| :--- | :---: | :---: | :--- |
| **1. Methodological & Statistical Rigor** | **0.9** | 3.5 | Valid 13-PCG phylogenetic inference, but SDM relies solely on training AUC, confuses bootstrap with $n-1$ jackknife, omits final predictor list from main text, and confuses `LPI` with `LSI` shape complexity. |
| **2. Claim-to-Evidence Alignment** | **0.8** | 2.5 | Claims an ornamental trade turtle in New Delhi represents a native Indian geo-referenced mitogenome; misinterprets immediate 2021–2040 SDM drop (-65.7% to -70.5%) as a 50-year future decline; confuses `LPI` with patch shape complexity in Abstract/Results. |
| **3. Data Integrity & Biological Plausibility** | **0.8** | 2.0 | All 20 tRNAs in Table 1 list mRNA codons instead of tRNA anticodons; stop codons in Table 1 contradict gene lengths and prose; contradictory ethics exemption statement for sedating/bleeding a Schedule I / CITES I turtle. |
| **4. Reproducibility & Data Integrity** | **0.8** | 2.0 | Mitogenome deposited in GenBank (`OP344485`) and GBIF DOI cited (`10.15468/dl.ce6mmr`), but Table 1 is truncated at base 14,229 (missing `cytb`, `trnT`, `trnP`, `CR`) and SDM occurrence table/rasters are not directly included in the main text. |
| **Total Composite Score** | **3.3** | **10.0** | **Flawed / Overstated** (**Scientific Core Score: 2.5 / 8.0**) |
