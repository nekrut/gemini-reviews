# Blinded Review: TIME_ANON_25
**Composite Score:** 2.8 / 10.0 (Rigor: 0.6/3.5 | Claims: 0.5/2.5 | Biology: 0.7/2.0 | Reproducibility: 1.0/2.0)
**Bias Category:** Bioinformatic Contamination / rRNA & Repeat Misannotation / Redundant-Read Weighting Artifact
**Verdict:** Reject
**Study Modality:** Hybrid Computational + Wet-Lab Functional Validation
**Technology Maturity:** Mid-Stage High-Throughput
**Epistemic Stage:** Basic/Mechanistic Discovery

---

### 1. Executive Summary

This manuscript characterizes small RNAs from adult *Clonorchis sinensis* liver flukes harvested from the bile ducts of wild cats using Solexa/Illumina deep sequencing ($14.8\text{ million}$ raw reads; $11.19\text{ million}$ clean reads), cross-species alignment to Sanger miRBase (Release 13.0) and the *Schistosoma japonicum* reference genome, Mfold/MirCheck secondary-structure prediction, and SYBR Green stem-loop RT-qPCR. The authors report identifying "62,512 conserved *C. sinensis* miRNAs which belonged to 284 families" alongside 6 novel miRNAs (`cis-mir-001` through `cis-mir-019`), conclude that *C. sinensis* maintains vertebrate-, insect-, and nematode-specific miRNAs to "enlarge its host range," and propose that *C. sinensis* miRNAs lack a standard 1st-to-9th nucleotide seed boundary due to elevated uracil frequencies at positions 1, 14, and 22.

Forensic audit of the sequences, read counts, and bioinformatic pipeline reveals multiple fatal flaws:
1. By aligning short ($18\text{--}23\text{ nt}$) reads from flukes harvested from mammalian bile ducts against all of miRBase allowing $\le 2$ mismatches without filtering host feline RNA or verifying precursor hairpins in the parasite genome, the authors conflate 62,512 unique read variants (isomiRs, sequencing errors, and host mammalian RNA contaminants) with distinct miRNA genes, and misinterpret host/false-positive matches to vertebrate and viral miRNAs as an evolutionary strategy of the flatworm.
2. Among the 6 "novel miRNAs" in Table 2, none has a detected `miRNA*` passenger strand, 4 are supported by only $5\text{--}13$ reads out of $11.2\text{ million}$, `cis-mir-002` (`5'-CUGGUCAUCAUCAUCAUCAUA-3'`) is a simple $(\text{UCA})_5$ trinucleotide repeat, and `cis-mir-019` (`5'-UAGAGGAAUUGACGGAAGGGCA-3'`, 5 sequencing reads but an RT-qPCR signal $67.32\times$ higher than *actin*) is an exact 22-nt fragment of universally conserved eukaryotic **18S ribosomal RNA** that escaped Rfam filtering.
3. The claimed "nucleotide bias" and "shifted seed region" (high U at positions 1, 14, and 22; high G at positions 6, 12, and 18) were computed across $2,093,879$ *redundant* reads rather than unique miRNA loci, meaning the position profile simply reflects the nucleotide sequence of the single hyper-abundant transcript `miR-71` ($\sim 600,000$ reads) rather than an evolutionary shift in seed architecture across the miRNA repertoire.

---

### 2. Methodological & Statistical Audit

1. **rRNA Degradation Fragment and Simple Sequence Repeat Misannotated as "Novel miRNAs" (Table 2):**
   * **`cis-mir-019` (`5'-UAGAGGAAUUGACGGAAGGGCA-3'`):** In Table 2 (line 62), this 22-nt sequence was observed only **5 times** in $11.19\text{ million}$ sequencing reads, yet its stem-loop RT-qPCR expression level relative to $\beta$-actin is **$67.32 \pm 12.87$** (five orders of magnitude higher than `cis-mir-006`, which had 108 sequencing reads but a qPCR level of $0.001$). Sequence inspection immediately explains this paradox: `5'-UAGAGGAAUUGACGGAAGGGCA-3'` is 100% identical to the universally conserved eukaryotic **18S rRNA** core sequence. Because 18S rRNA is present at massive copy numbers in total RNA, RT-qPCR primers targeting this 22-nt window amplify 18S rRNA fragments directly, proving that `cis-mir-019` is an unremoved rRNA breakdown product rather than a novel miRNA.
   * **`cis-mir-002` (`5'-CUGGUCAUCAUCAUCAUCAUA-3'`):** Supported by only 5 reads (Table 2, line 58), positions 4–21 of this 21-nt read consist of a pure $(\text{UCA})_6$ trinucleotide microsatellite repeat.
   * **Absence of `miRNA*` strands and violation of stated criteria:** In the Methods (line 152), the authors state that *"Predicted precursors that miRNAs and miRNA* can be found in its both arms were deemed as high probability."* Yet in the Results (line 51), they report that zero `miRNA*` sequences were detected for any of the 6 novel candidates, and 4 of the 6 candidates have $\le 13$ reads out of $11.19\text{ million}$ clean reads.

2. **Unfiltered Mammalian Host Contamination and Loose ($\le 2$ Mismatch) Short-Read Matching:**
   * Adult worms were collected from the bile ducts of wild cats (*Felis catus*), where flukes ingest host blood, bile, and sloughed biliary epithelial cells. Total RNA was extracted from whole homogenized worms without aligning reads against a mammalian/feline host reference genome to subtract host small RNAs.
   * All non-ncRNA reads were searched against all of Sanger miRBase v13 allowing up to 2 mismatches (`mismatches <= 2`, line 152) without requiring a corresponding pre-miRNA hairpin in a trematode genome (only $19.46\%$ of clean reads mapped to *S. japonicum*). For an 18–21 nt read, allowing 2 mismatches against the entire multi-kingdom miRBase database generates thousands of spurious cross-kingdom matches, while true host feline miRNAs match vertebrate miRBase entries perfectly.
   * Furthermore, the authors refer to 62,512 unique sequencing reads matching miRBase as *"62,512 conserved C. sinensis miRNAs"* (Abstract line 9), confusing 62,512 redundant/erroneous read variants (isomiRs and sequencing error singletons) with distinct miRNA genes.

3. **Weighting Position-Specific Nucleotide Frequencies by Redundant Read Counts:**
   * In Lines 97–105 and Discussion Line 122, the authors compute position-by-position nucleotide frequencies across all $2,093,879$ total conserved miRNA reads rather than across non-redundant canonical miRNA sequences.
   * Because a single family (`miR-71`, accounting for $33.24\%$ of reads, plus `miR-277b`) makes up a massive fraction of the total read pool, weighting every read equally turns the position-specific base composition plot into a mirror of the sequence of `miR-71` (which begins with $5'\text{-U}$, has $\text{G/C}$ across positions 6–9, and has $\text{U}$ at position 14), leading the authors to erroneously conclude that *C. sinensis* has evolved a "shifted seed region."

4. **Internal Arithmetic Inconsistencies:**
   * **Inconsistent denominators for miRNA abundance percentages (Line 90 vs. Table 1):** Table 1 (line 45) states that total "Known miRNAs" reads $= 2,093,879$. However, Line 90 states that `miR-71` had $597,871$ reads accounting for $26.79\%$ of total reads (which implies a denominator of $597,871 / 0.2679 = 2,231,695$, whereas $597,871 / 2,093,879 = 28.55\%$), and immediately states that `miR-277b` had $98,845$ reads accounting for $7.97\%$ (which implies a denominator of $98,845 / 0.0797 = 1,240,213$, whereas $98,845 / 2,093,879 = 4.72\%$). The two percentages in the same sentence use incompatible denominators differing by nearly 1 million reads.
   * **Contradictory first-nucleotide Uracil percentage (Line 97 vs. Line 104):** Line 97 states that Uracil is the first nucleotide in **$70.07\%$** of the $2,093,879$ reads, whereas Line 104 states that Uracil is at the 1st position in **$68.01\%$** of reads.

---

### 3. Biological / Experimental Grounding & Claim Proportionality

* **Claim that *C. sinensis* possesses vertebrate-, insect-, and nematode-specific miRNAs to "adapt and modify the host" and "easily enlarge its host range" (Abstract line 9, Results line 71):** **Methodologically Flawed / Biologically Implausible.** Metazoan miRNA families follow strict clade-specific evolutionary origins; flatworms (Lophotrochozoa) do not carry vertebrate-specific or insect-specific miRNA families. Detecting vertebrate miRNAs in RNA extracted from parasites living inside cat bile ducts is the expected signature of host tissue/bile contamination, not cross-kingdom miRNA acquisition.
* **Claim of "site-directed evolution and mutagenesis" in the middle and tail of *C. sinensis* miRNAs (Abstract line 9, Results line 78):** **Overstated.** Comparing 2-mismatch short reads against miRBase orthologs from insects and vertebrates and interpreting the allowed mismatches at positions 10–22 as "active innovation" or "site-directed evolution" ignores both sequencing error and the fact that the alignment filter itself (`mismatches <= 2`) selected those variants.

---

### 4. Reproducibility & Data Completeness

* **Positives:** Raw small RNA sequencing reads were deposited in NCBI GEO under accession number `GSE22244` (line 32), and the *C. sinensis* $\beta$-actin control accession (`EU109284`) and primer pair are specified (line 159).
* **Deficiencies:**
  1. None of the stem-loop RT primers or gene-specific forward/reverse qPCR primers for the 6 candidate novel miRNAs (`cis-mir-001` to `cis-mir-019`) are provided in the Methods or listed in the Additional Files.
  2. Exact software parameters for SOAP read mapping, Mfold folding window length, and MirCheck filtering thresholds are not fully specified.
