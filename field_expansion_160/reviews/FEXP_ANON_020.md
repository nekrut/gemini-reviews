# Review of FEXP_ANON_020

**Overall Score:** **3.8 / 10.0** (Flawed / Overstated) | **Scientific Core Score:** **2.9 / 8.0**  
* **Score Breakdown:** Rigor: 1.0/3.5 | Claims: 0.9/2.5 | Biology: 1.0/2.0 | Reproducibility: 0.9/2.0

---

## 1. Blinded Metadata Perception

* **Manuscript ID:** `FEXP_ANON_020`
* **Perceived Research Domain:** Veterinary molecular virology, CRESS DNA virus surveillance, and viral codon usage analysis (*Kirkoviridae* / Bovine circovirus-like virus).
* **Study Design:** Cross-sectional PCR surveillance of diarrheal fecal samples from dairy cattle ($N = 868$ samples across 71 farms in 20 Chinese provinces, April 2020–April 2022) and sheep ($N = 113$ samples across 3 provinces), whole-genome sequencing of a single bovine isolate (`AH20-1`, 3,912 bp), and bioinformatic codon usage analysis.
* **Primary Methods:** Conventional PCR and TOPO-Blunt cloning/Sanger sequencing, Neighbor-Joining (NJ) phylogenetic reconstruction in MEGA7 (1,000 bootstrap replicates), and codon usage metrics (nucleotide composition, Parity Rule 2 [PR2] bias plot, Effective Number of Codons [ENc] vs. GC3s, and Relative Synonymous Codon Usage [RSCU] via `CAIcal` server and R package `vhcub`).

---

## 2. Executive Summary & Editorial Verdict

This manuscript reports the complete genome sequence (3,912 bp; GenBank `OP778150`) of a bovine circovirus-like (BCL) CRESS DNA virus strain (`AH20-1`) detected in diarrheal cattle feces in Anhui Province, China, alongside a PCR survey of 868 diarrheal dairy cow fecal samples across 20 Chinese provinces and 113 diarrheal sheep fecal samples across 3 provinces. The authors report PCR positivity rates of 23.6% (205/868) in diarrheal cattle and 20.4% (23/113) in diarrheal sheep, classify the sequenced partial `Rep` amplicons primarily into genotype `BCLa` via Neighbor-Joining trees, and analyze codon usage bias (PR2, ENc–GC3s, RSCU) across *Kirkoviridae* `Rep` sequences.

While the multi-province PCR detection dataset documents that `BCLa`-like CRESS DNA sequences are frequently present in the feces of cattle and sheep in China, the manuscript suffers from severe methodological, analytical, and reporting defects across multiple diagnostic pillars. First, the study claims in its Results heading and Conclusion to have conducted a *"Pathogenetic investigation of BCL virus in China"* and *"provided the first systematic investigation of its pathogenicity in China"*, despite performing zero pathogenicity or challenge experiments, failing to isolate the virus in cell culture, screening zero healthy (non-diarrheal) control animals, and not testing for known enteric co-pathogens. Second, the codon usage section is internally contradictory: the text analyzes the `Rep` gene (and notes in the Discussion that BCL virus lacks a typical capsid protein), whereas the Figure 4 caption states that the plots represent the **`Cap` gene**; moreover, the authors misinterpret their own ENc values ($37\text{–}50$, mean $44.95 \pm 3.52$) as showing *"weak to strong codon usage bias"* and *"broad range of host adaptability"* without computing any host codon adaptation metrics (e.g., CAI, RCDI, or SiD) or neutrality regressions. Third, reproducibility is compromised because the Methods state that PCR and full-genome amplification primers are listed in Table 1, but Table 1 actually contains `Rep` amino acid percent identities—leaving the primer sequences completely absent from the paper—and none of the partial `Rep` sequences from the 205 cattle and 23 sheep positive samples have GenBank accession numbers reported.

### Specific Assessment of Core Claims

* **Complete genome characterization of strain `AH20-1` (3,912 bp) and high `Rep` amino acid identity (97.1%) to reference BCL virus CH (`MH316857.1`):** **[Well Supported].**  
  The complete circular genome of `AH20-1` is deposited under GenBank accession `OP778150`, and its stem-loop nonanucleotide/hairpin motif, 310-aa `Rep` open reading frame lacking the 3-aa C-terminal deletion of strain CH, and sequence similarity to porcine/bovine Kirkovirus-like sequences (Table 1) are straightforward descriptive observations.

* **PCR positivity rates of 23.6% (205/868) in diarrheal cattle across 17/20 provinces and 20.4% (23/113) in diarrheal sheep, dominated by genotype `BCLa`:** **[Moderately Supported].**  
  The PCR survey demonstrates widespread fecal presence of BCL-related DNA across Chinese cattle and sheep farms, and closeness of cattle and sheep `Rep` sequences is consistent with shared viral circulation or common environmental/dietary exposure. However, because the PCR primer sequences were omitted from the manuscript (broken reference to Table 1) and the partial `Rep` sequences from the survey were not deposited with GenBank accessions, independent verification of amplicon specificity and the Fig. 3B phylogeny is currently blocked.

* **First systematic investigation of BCL virus pathogenicity in China and association with bovine/ovine diarrhea:** **[Methodologically Flawed].**  
  Section 3.3 is titled *"Pathogenetic investigation of BCL virus in China"* and the Conclusion states *"Our study identified the BCL virus in bovine diarrheal feces and provided the first systematic investigation of its pathogenicity in China"*. In reality, no pathogenicity study was performed: (1) viral isolation on MDBK cells failed (incorrectly spelled *"Martin-Darby Bovine Kidney cells"*, line 125); (2) **zero non-diarrheal healthy cattle or sheep controls** were tested to determine whether BCL DNA is equally prevalent in asymptomatic animals; and (3) fecal samples were not screened for standard bovine/ovine diarrheal pathogens (e.g., BVDV, BCoV, rotavirus, *Cryptosporidium*). Because small CRESS DNA viruses detected in feces often infect gut protozoa, fungi, or dietary plant/insect matter rather than vertebrate enterocytes, case-only fecal PCR detection provides zero evidence of pathogenicity.

* **Codon usage analysis demonstrates that natural selection rather than mutational pressure shapes `Rep` evolution and confers broad host adaptability:** **[Methodologically Flawed].**  
  The authors report ENc values ranging from 37 to 50 (mean $44.95 \pm 3.52$) and state in line 116 both that this indicates *"weak to strong codon usage bias"* (contradicting their own threshold of $\text{ENc} < 35$ for strong bias on the same page) and that *"the GC3s values were positively correlated with the ENc values, indicating a weak codon usage bias"*. Under Wright's ENc–GC3s model, points with $\text{ENc} \approx 45$ that positively track GC3s near the expected curve reflect predominantly mutational/compositional bias rather than strong translational selection. Furthermore, no host codon usage reference tables (bovine, porcine, or ovine) were included, and no host adaptation indices (CAI or Similarity Index $D(A,B)$) or neutrality plots ($\text{GC}_{12}$ vs. $\text{GC}_3$) were computed to support the claim of *"broad range of host adaptability"*.

---

## 3. Forensic Defect Inventory

### Defect 1: Broken Table Cross-Reference and Complete Omission of PCR Primer Sequences (Pillar 7)
* **Location:** Section "DNA/RNA extraction of viruses and polymerase chain reaction" (line 33) and Table 1 (lines 36–51).
* **Diagnostic Finding:** Line 33 states: *"Primers for CRESS DNA virus detection and full-length amplification are listed in Table 1 ."* However, Table 1 is titled *"Rep amino acid identity analysis of Bo-Circo-like virus AH20-1 strain and the other circovirus-like virus strains"* and contains no primer sequences. No other table exists in the manuscript. Without primer sequences, target coordinates, or amplicon sizes, the PCR screening of 981 livestock samples cannot be replicated or evaluated for cross-reactivity.
* **Remediation:** Add a dedicated table listing all diagnostic and full-genome amplification primer names, $5'\to 3'$ sequences, binding coordinates relative to `OP778150`, and expected amplicon lengths (in bp).

### Defect 2: Case-Only Sampling Confounded with "Pathogenicity" (Pillar 1, Pillar 2 & Pillar 5)
* **Location:** Introduction (line 20), Section "Pathogenetic investigation of BCL virus in China" (lines 101–103), Conclusion (line 130).
* **Diagnostic Finding:** The study sampled exclusively diarrheal feces ($N = 868$ cattle, $N = 113$ sheep) without any matched healthy control feces and without testing for established enteric pathogens, yet labels Section 3.3 a *"Pathogenetic investigation"* and claims in the Conclusion to have *"provided the first systematic investigation of its pathogenicity in China"*. This directly contradicts the authors' admission in the Discussion (line 125) that *"it is not clear whether the virus is a direct pathogen"*.
* **Remediation:** Rename Section 3.3 to *"Molecular prevalence survey of BCL virus in diarrheal cattle and sheep in China"* and remove all claims in the Conclusion and Abstract implying that pathogenicity was investigated or established.

### Defect 3: Self-Contradictory Codon Usage Analysis and `Rep` vs. `Cap` Gene Labeling Error (Pillar 3, Pillar 6 & Pillar 7)
* **Location:** Section "Role of host codon usage selection pressure on Rep gene in Kirkoviridae family" (lines 109–116), Figure 4 caption (line 114), Discussion (line 121).
* **Diagnostic Finding:**
  1. **Gene identity contradiction (`Rep` vs. `Cap`):** The section header and main text (lines 109–116) state that codon usage was analyzed on the **`Rep` gene** of *Kirkoviridae*, and Discussion line 121 explicitly states that BCL virus *"lack[s] the typical capsid protein"*. Yet the caption of Figure 4 (line 114) reads: *"Fig. 4: Host codon usage selection pressure on **Cap gene** of Kirkoviridae family virus evolution."*
  2. **Threshold contradiction:** Line 70 and line 116 define $\text{ENc} < 35$ as high/strong codon bias and $\text{ENc} > 50$ as random usage. Observing a range of $37\text{–}50$ (mean $44.95 \pm 3.52$) means *zero* sequences fell into the strong bias regime ($<35$), yet line 116 describes $37\text{–}50$ as *"weak to strong codon usage bias"* before immediately calling it *"weak codon usage bias"* two sentences later.
  3. **Unsubstantiated host adaptation and selection claims:** Concluding that natural selection outweighed mutational pressure and demonstrated *"a broad range of host adaptability"* without running a $\text{GC}_{12}$ vs. $\text{GC}_3$ neutrality regression, quantifying residuals from Wright's expected ENc curve $\text{ENc}_{\text{exp}} = 2 + s + \frac{29}{s^2 + (1-s)^2}$, or comparing viral RSCU to cattle/sheep/swine host codon tables is methodologically invalid.
* **Remediation:** Correct the Figure 4 caption from `Cap gene` to `Rep gene`, correct the textual interpretation of $\text{ENc} \in [37, 50]$ to weak/moderate bias, perform a formal neutrality plot ($\text{GC}_{12}$ vs. $\text{GC}_3$) and host Codon Adaptation Index (CAI) / Similarity Index analysis if host adaptation claims are retained, and list the exact GenBank accessions of the *Kirkoviridae* sequences analyzed in Figure 4.

### Defect 4: Missing GenBank Accessions for Clinical Survey Isolates and Incomplete Phylogenetic Methods (Pillar 3 & Pillar 7)
* **Location:** Section "Phylogenetic analysis" (line 55), Figure 3B (line 106), Section "Data availability" (line 152), and text typos (lines 103, 116, 125).
* **Diagnostic Finding:**
  1. Only a single GenBank accession (`OP778150`) is provided. None of the partial `Rep` sequences from the cattle and sheep survey used to build Figure 3B have accession numbers reported.
  2. Section "Phylogenetic analysis" (line 55) states only that NJ trees were built with 1,000 bootstrap replicates in MEGA7, omitting the evolutionary substitution/distance model, alignment algorithm, and sequence length of the partial `Rep` region.
  3. Typographical errors include *"in the k family"* (for *Kirkoviridae* family, line 116), *"Martin-Darby Bovine Kidney cells"* (for Madin-Darby, line 125), and *"BCLvirus"* (line 103).
* **Remediation:** Deposit all sequenced partial `Rep` amplicons from cattle and sheep in GenBank and provide their accession numbers, specify the sequence alignment method and substitution distance models used in MEGA7, and correct the typographical errors.

---

## 4. Quantitative Rubric Scoring

| Rubric Dimension | Score | Max | Diagnostic Justification |
| :--- | :---: | :---: | :--- |
| **1. Methodological & Statistical Rigor** | **1.0** | **3.5** | Case-only diarrheal sampling without healthy controls or co-pathogen testing; self-contradictory ENc interpretation and unsupported selection/host-adaptability claims lacking neutrality plots or host codon tables; basic NJ trees without substitution model specification. |
| **2. Claim-to-Evidence Alignment** | **0.9** | **2.5** | Claims to have provided "the first systematic investigation of its pathogenicity in China" and demonstrated "host codon usage selection pressure" and "broad range of host adaptability" are unsubstantiated by the actual data. |
| **3. Data Integrity & Biological Plausibility** | **1.0** | **2.0** | Whole-genome characterization of `AH20-1` (`OP778150`) and multi-province PCR detection in cattle and sheep are plausible, but Figure 4 contradicts the text by labeling the analyzed gene as `Cap` rather than `Rep`, and fecal CRESS DNA detection is conflated with active enteric pathogenesis. |
| **4. Reproducibility & Data Integrity** | **0.9** | **2.0** | Broken cross-reference to Table 1 leaves all PCR and sequencing primers completely missing from the manuscript; partial `Rep` sequences from the survey (Fig. 3B) and reference accessions for Fig. 4 are not reported. |
| **Total Composite Score** | **3.8** | **10.0** | **Flawed / Overstated** (Scientific Core Score: **2.9 / 8.0**) |
