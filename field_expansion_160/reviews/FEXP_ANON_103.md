# Forensic Review of `FEXP_ANON_103`

**Overall Score:** **3.4 / 10.0** (Flawed / Overstated) | **Scientific Core Score:** **2.6 / 8.0**
* **Score Breakdown:** Rigor: 0.9/3.5 | Claims: 0.7/2.5 | Biology: 1.0/2.0 | Reproducibility: 0.8/2.0

---

## 1. Blinded Metadata Perception

* **Perceived Field & Subfield:** Biodiversity Informatics / Entomology (Online taxonomic, biogeographic, and image database for Chinese Odonata—dragonflies and damselflies).
* **Study Design Archetype:** Database/web-portal descriptive paper (`Odonata of China`, `http://dragonflies.kiz.ac.cn`) built on React, Spring Boot, MySQL, MinIO, and Docker, aggregating taxonomic descriptions, provincial distributions, iNaturalist/monograph photographs (814 species), and COI DNA barcodes (309 species) for 820 Chinese odonate taxa.
* **Temporal & Venue Signals:** Recent (2024–2025) biodiversity database article with severe internal taxonomic and data-scope contradictions.

---

## 2. Executive Summary & Editorial Verdict

This manuscript describes the *Odonata of China* web database (`http://dragonflies.kiz.ac.cn`), which compiles species descriptions, provincial distribution maps, photographs (814 species), and DNA barcode sequences (309 species) for 820 Chinese dragonfly and damselfly taxa across 3 suborders and 172 genera.

**Editorial Verdict: Reject / Major Revision Required (Flawed / Overstated).** While a centralized digital catalog of Chinese Odonata is a useful entomological resource, the manuscript contains disqualifying taxonomic and factual contradictions:
1. **Scrambled Suborder Taxonomy in Table 1, Methods, and Discussion:** In Materials and Methods (line 30), Table 1 (lines 36–38), and Discussion (line 105), the authors completely permute the three suborders of Odonata, asserting that **Zygoptera** (damselflies) consists of only **1 family, 1 genus, and 3 species**, while assigning the 524 species of true dragonflies (Anisoptera) to **Anisozygoptera** (the relict living-fossil suborder represented in China solely by *Epiophlebia*, which actually has 1 family, 1 genus, and 3 species) and assigning damselfly counts (13 families, 65 genera, 293 species) to **Anisoptera**. Even worse, Results (line 90) directly contradicts Table 1 by reporting **23 families** (14 Zygoptera, 1 Anisozygoptera, 8 Anisoptera), and Discussion (line 105) replaces `Anisozygoptera` with `Epiprocta` alongside `Anisoptera`.
2. **Unfulfilled "Multiomics" Headline Claim:** The Abstract (line 5) and Introduction (line 18) claim that the database integrates *"multiomics data"* including *"genomic and transcriptomic data for 20 representative families"*. However, the Results section (lines 56–101; Figs. 2–3) contains no genomics or transcriptomics module (only single-locus DNA barcode BLAST alignment for 309 species), and the Discussion (line 117) admits that *"The next phase involves incorporating these omics resources into our centralized database"*.

### Assessment of Specific Claims

* **The database compiles taxonomic, morphological, provincial distribution, photographic (814 species), and DNA barcode (309 species) records for 820 Chinese Odonata species in a React/Spring Boot/MySQL/MinIO web portal (Abstract; Methods, lines 30–45; Results, lines 58–100): `[Well Supported]`**  
  The core species catalog, provincial map lookup, iNaturalist/monograph photo gallery, and nucleotide barcode alignment interface are clearly described and illustrated in Figures 1–3.
* **The 820 species in Odonata of China comprise Anisoptera (13 families, 65 genera, 293 species), Zygoptera (1 family, 1 genus, 3 species), and Anisozygoptera/Epiprocta (8 families, 106 genera, 524 species) (Methods, line 30; Table 1, lines 35–39; Discussion, line 105): `[Methodologically Flawed]`**  
  This is a fundamental entomological error. In China, the relict suborder **Anisozygoptera** (family Epiophlebiidae, genus *Epiophlebia*) has 1 family, 1 genus, and 3 species; **Zygoptera** (damselflies) has 13–14 families, 65 genera, and 293 species; and **Anisoptera** (true dragonflies) has 8 families, 106 genera, and 524 species. The authors shifted the row labels of Table 1 and propagated the error into the prose of both the Methods and Discussion, while contradicting it in Results line 90 (which lists 23 families: 14 Zygoptera, 1 Anisozygoptera, and 8 Anisoptera).
* **Odonata of China currently features multiomics (whole-genome, transcriptomic, and mitogenomic) data across 20 representative families (Abstract, line 5; Introduction, line 18): `[Overstated]`**  
  No genomic or transcriptomic browsers, download tables, or search modules exist in the Results (Figs. 2–3). In Discussion (line 117), the authors explicitly state that *"The next phase involves incorporating these omics resources into our centralized database"*, confirming that the multiomics data are not yet integrated into the live platform.
* **The database provides a formalized metadata specification document in Appendix 1 (Discussion, line 105): `[Methodologically Flawed]`**  
  No `Appendix 1` is present in the manuscript or supplementary information.

---

## 3. Forensic Defect Inventory

### 3.1. Suborder Taxonomic Permutation & Family Count Contradiction (Pillar 3, Pillar 6 & Pillar 7)
* **Location:** Materials and Methods (line 30), Table 1 (lines 33–39), Results ("Phylogeny and species", line 90), and Discussion (line 105).
* **Defect:**
  * **Table 1 & Methods (line 30):** Lists `Anisoptera (13 families, 65 genera, 293 species)`, `Zygoptera (1 family, 1 genus, 3 species)`, and `Anisozygoptera (8 families, 106 genera, 524 species)`, summing to `22 families`. Every suborder is mismatched with its taxonomic counts.
  * **Results (line 90):** States that Chinese Odonata are divided into `3 suborders and 23 families`: `Zygoptera (14 families)`, `Anisozygoptera (1 family)`, and `Anisoptera (8 families)` ($14 + 1 + 8 = 23$ families, contradicting the 22 families in Abstract, Table 1, and Discussion).
  * **Discussion (line 105):** Repeats the scrambled counts from Table 1 (`Zygoptera includes 1 family, 1 genus, and 3 species`) but substitutes `suborder Epiprocta` for `Anisozygoptera`, even though in odonate systematics Epiprocta is the clade uniting Anisoptera and Anisozygoptera.

### 3.2. Misrepresentation of Planned Future Features as Existing Database Content (Pillar 1 & Pillar 5)
* **Multiomics Datasets:** Claimed as an active feature of the database in the Abstract (line 5) and Introduction (line 18), but revealed in Discussion (line 117) to be planned for *"The next phase"*. Furthermore, Discussion (line 117) claims to list *"20 families"* but actually lists **21 family names**, 19 of which are misspelled by truncating the standard zoological family suffix `-idae` to `-ida` or `-id` (`Devadattida`, `Calopterygida`, `Euphaeida`, `Philogangida`, `Philosinida`, `Argiolestida`, `Pseudolestida`, `Lestida`, `Synlestida`, `Coenagrionida`, `Platystictida`, `Aeshnida`, `Gomphida`, `Chlorogomphid`, `Cordulegastrida`, `Corduliida`, `Macromiida`, `Synthemistida`, `Libellulida`).
* **Computer Vision / Image Identification:** Results ("Overview", line 58) claims the Identification module *"is primarily concerned with DNA barcode-based identification and morphological image-based identification"*, and Discussion (line 113) cites an ArcFace/ResNet model. However, Results ("Identification", line 95) and Figure 3D show that the Identification module only performs nucleotide sequence alignment (BLAST).
* **Spectroscopy Data:** Discussion (line 107) claims to have collected *"taxonomic (spectroscopy, descriptive, gene and protein sequences, identification keys)"*, whereas no spectroscopy data exist in the database.

### 3.3. Inconsistent Species Coverage Statistics & Missing Appendix (Pillar 7)
* **Contradictory Total Species Counts for China:** The total number of known Odonata species in China is variously stated as *"over 900"* (Abstract, line 5; Introduction, line 16), *"over 1000"* (Introduction, line 10), **820** (implied by Methods line 30, which claims that 814 species with photos represent *"99.3% coverage of currently recognized Odonata taxa in China"*, confusing the denominator of 820 database species with all species in China), and **983** (implied by Discussion line 105, which states that 820 species account for *"83.42% of the total known dragonfly species in China"*).
* **Missing Appendix 1 & Unarchived Code:** `Appendix 1` (referenced in line 105) is missing, and no source code or bulk database dump (e.g., Zenodo/Figshare SQL dump or FASTA barcode file) is deposited to ensure long-term archival permanence independent of the institutional web server.

---

## 4. Quantitative Rubric Scoring

| Rubric Dimension | Score | Max | Forensic Justification |
| :--- | :---: | :---: | :--- |
| **1. Methodological & Statistical Rigor** | **0.9** | 3.5 | Standard React/Spring Boot/MySQL/MinIO web architecture, but undermined by a lack of bulk data export APIs, unimplemented image-recognition/multiomics modules, and contradictory summary statistics (`22` vs `23` families; `99.3%` vs `83.42%` coverage). |
| **2. Claim-to-Evidence Alignment** | **0.7** | 2.5 | Abstract and Introduction claim integrated multiomics (genomes/transcriptomes across 20 families) and image-based identification, which Discussion line 117 and Results line 95 reveal are not yet incorporated into the database. |
| **3. Data Integrity & Biological Plausibility** | **1.0** | 2.0 | Disqualifying taxonomic inversion in Table 1, Methods, and Discussion that assigns 1 family and 3 species to Zygoptera (damselflies) and 524 species to Anisozygoptera, plus 19 misspelled family names (`-ida`) in line 117. |
| **4. Reproducibility & Data Integrity** | **0.8** | 2.0 | Live web URL provided, but `Appendix 1` is missing, Table 1 contradicts Results line 90, and no static archival dump (Zenodo/Figshare) or source code repository is provided. |
| **Total Composite Score** | **3.4** | **10.0** | **Flawed / Overstated** (**Scientific Core Score: 2.6 / 8.0**) |
