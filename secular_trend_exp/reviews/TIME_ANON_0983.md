<Blinded Review: TIME_ANON_0983>
**Composite Score:** 4.2 / 10.0 (Rigor: 1.2/3.5 | Claims: 1.1/2.5 | Biology: 1.0/2.0 | Reproducibility: 0.9/2.0)
**Bias Category:** Statistical/Design
**Verdict:** Major Revision
**Study Modality:** Wet-Lab Primary Experimental
**Technology Maturity:** Commodity/Hype-Cycle Template
**Epistemic Stage:** Clinical/Observational

OVERALL_SCORE: 4.2/10
VERDICT: FAILED
ESTIMATED_DECADE: 2010s

---

### 1. Executive Summary / SUMMARY
This hospital-based candidate-gene case-control study investigates the association of three *CD40* single-nucleotide polymorphisms (`rs1883832 C/T`, `rs1569723 A/C`, and `rs4810485 G/T`) and plasma soluble CD40 (sCD40) levels (measured by ELISA) with systemic lupus erythematosus (SLE) in a Chinese cohort from Guangxi ($n = 205$ SLE cases, $n = 220$ age- and sex-matched outpatient controls). Genotyping was performed via SNaPshot and Sanger sequencing confirmation. The authors report that `rs1883832 T` is associated with increased SLE risk ($\text{OR} = 1.517$, $95\%\ \text{CI}: 1.157\text{--}1.990$, $P = 0.003$), whereas `rs1569723 A/C` ($P = 0.805$) and `rs4810485 G/T` ($P = 0.719$) show no association ($P > 0.80$). They further claim that all three SNPs are in strong linkage disequilibrium ($|D'| = 0.841\text{--}0.922$), that haplotype `T-C-T` is associated with SLE ($\text{OR} = 1.408$, $P = 0.013$), and that `rs1883832 TT/CT` genotypes are associated with higher plasma sCD40 in SLE patients. Forensic audit of Tables 2 and 3 reveals a mathematical impossibility in the reported haplotype counts and LD structure: in Table 3, the haplotype `T-C-T` has count $211$ in SLE cases—which is 100% of all `rs1883832 T` alleles ($211$, Table 2) and leaves only $4$ `rs1569723 C` alleles for `C-C-G` ($6$) + `C-C-T` ($4$), causing the marginal allele counts in Table 3 to directly contradict Table 2! Moreover, it is mathematically impossible for `rs1883832` to have an allele frequency difference of $10.4\%$ ($51.5\%$ vs. $41.1\%$, $P = 0.003$) while two SNPs in near-complete LD with it (`rs1569723` and `rs4810485`, $|D'| = 0.87$, $r^2 \approx 0.75$ given ~50% MAF, and comprising $>94\%$ two-haplotype `T-C-T` / `C-A-G` structure in Table 3) have $<1\%$ allele frequency difference ($P = 0.805$ and $P = 0.719$).

### 2. Methodological & Statistical Audit / STRENGTHS & WEAKNESSES

#### STRENGTHS
- **Clear primer documentation and Sanger confirmation:** Table 1 provides the exact forward, reverse, and SNaPshot extension primers (`EF`) for all three *CD40* SNPs, and genotypes were verified by sequencing.
- **Combined genetic and soluble biomarker measurement:** Both *CD40* genotypes and plasma sCD40 ELISA levels were measured in the same 205 cases and 220 controls.

#### WEAKNESSES & METHODOLOGICAL AUDIT
- **Mathematical impossibility / internal contradiction between Table 2 (Single-SNP counts) and Table 3 (Haplotype counts):**
  - In **Table 2** (`SLE patients`, $2n = 410$ alleles):
    - `rs1883832`: $C = 199$, $T = 211$.
    - `rs1569723`: $A = 195$, $C = 215$.
    - `rs4810485`: $G = 199$, $T = 211$.
  - Now sum the marginal allele counts across the 6 haplotypes in **Table 3** (`SLE patients`, $2n = 410$):
    - Position 1 (`rs1883832` $T$): `T-C-T` ($211$) + `T-A-T` ($5$) $= \mathbf{216}$ $T$ alleles and $176 + 8 + 6 + 4 = \mathbf{194}$ $C$ alleles (contradicting Table 2's $211$ $T$ and $199$ $C$).
    - Position 2 (`rs1569723` $C$): `T-C-T` ($211$) + `C-C-G` ($6$) + `C-C-T` ($4$) $= \mathbf{221}$ $C$ alleles and $176 + 8 + 5 = \mathbf{189}$ $A$ alleles (contradicting Table 2's $215$ $C$ and $195$ $A$).
    - Position 3 (`rs4810485` $T$): `T-C-T` ($211$) + `C-A-T` ($8$) + `C-C-T` ($4$) + `T-A-T` ($5$) $= \mathbf{228}$ $T$ alleles and $176 + 6 = \mathbf{182}$ $G$ alleles (contradicting Table 2's $211$ $T$ and $199$ $G$ by 17 alleles!).
  - Do the same check for **Controls** ($2n = 440$) in **Table 3**:
    - Position 1 (`rs1883832` $T$): `T-C-T` ($189$) + `T-A-T` ($9$) $= \mathbf{198}$ $T$ alleles and $207 + 13 + 14 + 8 = \mathbf{242}$ $C$ alleles, whereas **Table 2** reports $\mathbf{181}$ $T$ alleles and $\mathbf{259}$ $C$ alleles (a 17-allele discrepancy!).
    - Position 2 (`rs1569723` $C$): `T-C-T` ($189$) + `C-C-G` ($14$) + `C-C-T` ($8$) $= \mathbf{211}$ $C$ alleles and $207 + 13 + 9 = \mathbf{229}$ $A$ alleles, whereas **Table 2** reports $\mathbf{227}$ $C$ alleles and $\mathbf{213}$ $A$ alleles (the major/minor alleles are inverted!).
    - Position 3 (`rs4810485` $T$): `T-C-T` ($189$) + `C-A-T` ($13$) + `C-C-T` ($8$) + `T-A-T` ($9$) $= \mathbf{219}$ $T$ alleles and $207 + 14 = \mathbf{221}$ $G$ alleles, whereas **Table 2** reports $221$ $T$ and $219$ $G$.
  - Furthermore, because `rs1883832`, `rs1569723`, and `rs4810485` span less than $6\ \text{kb}$ at the *CD40* locus and are in tight linkage disequilibrium ($r^2 > 0.70$, with `T-C-T` and `C-A-G` making up $>90\%$ of chromosomes), it is genetically and mathematically impossible for `rs1883832` to shift by $+10.4\%$ between cases and controls ($P = 0.003$) while `rs1569723` and `rs4810485` on the exact same yin-yang haplotypes (`T-C-T` / `C-A-G`) shift by only $+0.8\%$ ($P = 0.805$) and $+1.3\%$ ($P = 0.719$).
- **Direct reversal of SLE vs. Control sCD40 values between Results text and Figure 1 legend:**
  - Line 74 (Results text) states: *"The serum CD40 levels were significantly higher in the group of patients with SLE than those in the control group [(mean +/- SD 58.5 +/- 22.8 pg/ml, n = 205) vs, (mean +/- SD 41.7 +/- 13.2 pg/ml, n = 220); P < 0.001]."*
  - Line 77 (Figure 1 legend) states the exact opposite: *"The expression of CD40 was significantly increased in patients with SLE compared to that in control subjects [(mean +/- SD 41.7+/- 13.2 pg/ml, n = 205) vs (mean +/- SD 58.5+/- 22.8 pg/ml, n = 220); P < 0.001]."*
- **Inaccurate Odds Ratio for `C-A-T` in Table 3:** For `C-A-T` ($8/410$ in SLE vs. $13/440$ in controls), the exact odds ratio is $\frac{8 \times 427}{402 \times 13} = 0.653$, whereas Table 3 prints `0.735 (0.253–2.138)`.
- **Uncontrolled ethnic/population stratification in a multi-ethnic region (Guangxi):** The study was conducted at Youjiang Medical University for Nationalities in Guangxi (a region with a large Zhuang minority population alongside Han Chinese), yet the Methods state only *"All study subjects were Chinese"* without stratifying or matching by ethnic group (Zhuang vs. Han).

### 3. Biological / Experimental Grounding & Claim Proportionality
- **Claim that plasma sCD40 is elevated in SLE patients compared to controls:** `[Moderately Supported]` — Plausible and consistent with clinical literature, though the Figure 1 legend swaps the case and control means ($41.7$ vs. $58.5\ \text{pg/ml}$).
- **Claim that `rs1883832 C/T` and haplotype `T-C-T` significantly increase SLE risk while tightly linked SNPs `rs1569723` and `rs4810485` have zero effect:** `[Methodologically Flawed]` — Directly invalidated by the marginal allele sum contradictions between Table 2 and Table 3 ($17$-allele discrepancy in controls and SLE cases) and the mathematical incompatibility of strong LD ($>90\%$ `T-C-T` / `C-A-G` haplotypes) with discordant single-SNP allele frequencies.

### 4. Reproducibility & Data Completeness
While primer sequences (Table 1) and aggregate genotype/haplotype tables (Tables 2–3) are included in the article, the severe arithmetic contradictions between Table 2 and Table 3 and the absence of individual-level genotype data prevent independent verification or reconciliation of the genotyping counts.
</Blinded Review: TIME_ANON_0983>
