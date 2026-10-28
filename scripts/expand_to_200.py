import os
import re
import json
import random
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
from build_deidentified import scrub_manuscript

with open("/Users/sergei/Projects/lit-estimation/cohorts.json") as f:
    cohorts = json.load(f)

# Move B02 (PMC8135569, Kumar et al. 2021 proCoV2) to A26
old_b02 = [r for r in cohorts["cohort_b"] if r["cohort_id"] == "B02"][0]
old_b02_as_a26 = dict(old_b02)
old_b02_as_a26.update({
    "cohort_id": "A26",
    "cohort": "A",
    "domain": "Viral Evolution",
    "ground_truth_flaw": "Kumar et al. (2021) MBE proCoV2 mutational-order rooting: coding RaTG13-matching bases as ancestral (0) in SCITE inverted APOBEC C->U reversions in North American Lineage A.1 into a false pre-Wuhan progenitor root",
    "refutation": "Pekar, Worobey et al. (2022) Science"
})

NEW_A_SPECS = [
    ("A27", "PMC4929217", "Cancer & Microbiome", "Aagaard et al. (2014) Sci Transl Med placental microbiome claim: low-biomass reagent ('kitome') contamination and batch effects without matched blank controls", "Lauder et al. (2016) Microbiome; de Goffau et al. (2019) Nature"),
    ("A28", "PMC8240556", "Cancer & Microbiome", "Mishra et al. (2021) Cell fetal in-utero gut/tissue microbiome claim: low-biomass reagent and delivery contamination mistaken for viable fetal colonization", "Kennedy et al. (2023) Nature"),
    ("A29", "PMC8110246", "Cancer & Microbiome", "Rackaityte et al. (2020) Nat Med fetal intestine Micrococcus colonization claim: low-biomass contamination and batch effects", "Kennedy et al. (2023) Nature; de Goffau et al. (2021)"),
    ("A30", "PMC1863478", "Molecular Evolution", "Bakewell et al. (2007) PNAS claim that more genes underwent positive selection in chimpanzees than humans: 4x draft chimp sequencing base-call errors and alignment artifacts inflating dN/dS", "Mallick et al. (2009) Genome Res; Schneider et al. (2009) Science"),
    ("A31", "PMC2837078", "Molecular Evolution", "Hughes et al. (2008) codon-based positive selection critique & parsimony counting: conflating relaxed purifying selection and synonymous saturation with likelihood branch-site properties", "Yang & dos Reis (2011) MBE"),
    ("A32", "PMC8264168", "Viral Epidemiology", "Fongaro et al. (2021) Sci Total Environ claim of SARS-CoV-2 in November 2019 Brazilian sewage: nested amplicon contamination and discordant target amplification", "Worobey / environmental virology scrutiny"),
    ("A33", "PMC7196402", "Viral Epidemiology", "Deslandes et al. (2020) IJAA claim of late December 2019 SARS-CoV-2 case in France from single high-Ct RdRp/E RT-PCR without sequencing confirmation or contamination controls", "Post-publication clinical virology critiques"),
    ("A34", "PMC7864798", "Viral Epidemiology", "Carrat et al. (2021) Eur J Epidemiol claim of November 2019 SARS-CoV-2 seropositivity in France: false-positive rate of ELISA/neutralization exceeding observed pre-pandemic prevalence", "Costagliola et al. (2022) Eur J Epidemiol refutation"),
    ("A35", "PMC7859469", "Viral Evolution", "Sallard et al. (2021) tracing origins of SARS-CoV-2 in coronavirus phylogenies: uncalibrated molecular clock & recombination breakpoint misinterpretations", "Lytras et al. (2022) Genome Res"),
    ("A36", "PMC7077245", "Viral Evolution", "Vilar & Iscla (2020) Return of the coronavirus 2019-nCoV: elementary phylogenetic rooting and sequence-similarity misinterpretations", "Coronaviridae phylogenetics critiques"),
    ("A37", "PMC7106301", "Viral Evolution", "Paraskevis et al. (2020) full-genome evolutionary analysis of 2019-nCoV: sliding-window SimPlot distance misinterpretation ignoring RBD recombination history", "Boni et al. (2020) Nat Microbiol"),
    ("A38", "PMC7166400", "Viral Evolution", "Benvenuto et al. (2020) JMV 2019-nCoV fast evolution and positive selection from 15 early genomes: applying FUBAR/FEL to nearly identical epidemic genomes with sequencing errors", "MacLean et al. (2020) Nat Microbiol"),
    ("A39", "PMC7174922", "Viral Genomics", "Pachetti et al. (2020) J Transl Med SARS-CoV-2 RdRp mutation hotspots: geographic sampling skew and unadjusted linkage with Spike D614G", "Phylogenetic linkage critiques"),
    ("A40", "PMC7375210", "Viral Genomics", "Koyama et al. (2020) Bull WHO variant analysis of SARS-CoV-2 genomes: unmasked sequencing artifacts and unstratified geographic variant counts", "Turakhia et al. (2020) PLoS Genet"),
    ("A41", "PMC7458444", "Viral Evolution", "Lvov et al. / Lau et al. (2020) EID emergence of SARS-CoV-2 through recombination and purifying selection: failure to separate recombinant blocks before molecular clock/selection inference", "Boni et al. (2020) Nat Microbiol"),
    ("A42", "PMC9488757", "Epidemiology / Stats", "Spurious early ecological association of BCG vaccination with COVID-19 morbidity/mortality: severe demographic, testing-rate, and epidemic-stage confounding", "Randomized BCG trial refutations"),
    ("A43", "PMC7267326", "Epidemiology / Stats", "Kloc et al. (2020) ecological correlation of BCG vaccination policy and COVID-19 mortality: ecological fallacy and country-level confounding", "Hensel et al. (2020) / RCT refutations"),
    ("A44", "PMC8759701", "Statistical Genetics", "Retracted GWAS mapping study (PMC8759701): statistical and data-integrity failures in genome-wide association analysis", "Formal Retraction Notice"),
    ("A45", "PMC11999383", "Statistical Genetics", "Retracted Mendelian randomization / GWAS causal inference study (PMC11999383): invalid instrumental variable assumptions, pleiotropy, and sample overlap", "Formal Retraction Notice"),
    ("A46", "PMC4225573", "Transcriptomics & CompBio", "Retracted gene expression profiling / transcriptomic biomarker study (PMC4225573): unadjusted multiple testing and microarray analytical errors", "Formal Retraction Notice"),
    ("A47", "PMC9468935", "Transcriptomics & CompBio", "Retracted necroptosis-related gene prognostic signature in cancer (PMC9468935): circular LASSO/Cox feature selection and validation defects", "Formal Retraction Notice"),
    ("A48", "PMC12471436", "Transcriptomics & CompBio", "Retracted machine-learning survival prediction in cancer (PMC12471436): train-test data leakage and flawed feature selection pipeline", "Formal Retraction Notice"),
    ("A49", "PMC12609430", "Transcriptomics & CompBio", "Retracted transcriptomic & signaling study (PMC12609430): internal data inconsistencies and analytical defects", "Formal Retraction Notice"),
    ("A50", "PMC13107010", "Transcriptomics & CompBio", "Retracted single-cell RNA-seq viral dissection study (PMC13107010): single-cell analytical and data-provenance failures", "Formal Retraction Notice"),
]

NEW_B_SPECS = [
    ("B02", "PMC7418704", "Viral Evolution", "Starr et al. (2020) Cell: deep mutational scanning of SARS-CoV-2 Spike RBD binding and expression", "Gold-standard replicated experimental evolution benchmark"),
    ("B26", "PMC7984229", "Cancer & Microbiome", "Wirbel et al. (2019) Nat Med: cross-cohort meta-analysis of fecal metagenomes in colorectal cancer across 8 studies", "Replicated leave-one-dataset-out metagenomic benchmark"),
    ("B27", "PMC9533319", "Cancer & Microbiome", "Thomas et al. (2019) Nat Med: metagenomic analysis of colorectal cancer across 7 international cohorts", "Back-to-back independent replication with Wirbel et al. (2019)"),
    ("B28", "PMC4299606", "Cancer & Microbiome", "Zeller et al. (2014) Mol Syst Biol: fecal microbiota metagenomic detection of colorectal cancer validated across French and German cohorts", "Replicated multi-country metagenomic benchmark"),
    ("B29", "PMC6707353", "Cancer & Microbiome", "Matson et al. (2018) Science: commensal microbiome associated with anti-PD-1 efficacy in metastatic melanoma with germ-free mouse validation", "Replicated across independent immunotherapy cohorts"),
    ("B30", "PMC5827966", "Cancer & Microbiome", "Gopalakrishnan et al. (2018) Science: gut microbiome modulates response to anti-PD-1 immunotherapy in melanoma patients", "Co-published independent replication of PD-1 microbiome effect"),
    ("B31", "PMC6697540", "Cancer & Microbiome", "de Goffau et al. (2019) Nature: rigorous negative-control and spike-in metagenomic/16S audit proving human placenta has no microbiome", "Definitive low-biomass contamination benchmark"),
    ("B32", "PMC4917942", "Cancer & Microbiome", "Lauder et al. (2016) Microbiome: matched air/reagent blank comparison proving placenta samples do not differ from negative controls", "Validated forensic microbiome control study"),
    ("B33", "PMC4228153", "Cancer & Microbiome", "Salter et al. (2014) BMC Biol: serial-dilution benchmark proving reagent and laboratory contamination ('kitome') dominates low-biomass microbiome data", "Foundational microbiome contamination benchmark"),
    ("B34", "PMC11333990", "Cancer & Microbiome", "Kennedy et al. (2023) Nature: multi-disciplinary forensic reanalysis refuting fetal in-utero microbiome claims", "Definitive low-biomass forensic benchmark"),
    ("B35", "PMC9110300", "Statistical Genetics", "Howe et al. (2022) Nat Genet: within-sibship GWAS across 178,086 sibling pairs separating direct genetic effects from stratification and dynastic confounding", "Gold-standard family-based GWAS benchmark"),
    ("B36", "PMC9605867", "Statistical Genetics", "Yengo et al. (2022) Nature: saturated map of common genetic variants associated with human height in 5.4M individuals with within-family replication", "Definitive large-scale GWAS benchmark"),
    ("B37", "PMC4918750", "Population Genomics", "Mathieson et al. (2015) Nature: direct ancient-DNA time-series measurement of selection in 230 ancient Eurasians", "Replicated across subsequent ancient genomics studies"),
    ("B38", "PMC6128408", "Statistical Genetics", "Khera et al. (2018) Nat Genet: genome-wide polygenic scores for common diseases validated out-of-sample in UK Biobank", "Replicated across biobanks worldwide"),
    ("B39", "PMC4495769", "Statistical Genetics", "Bulik-Sullivan et al. (2015) Nat Genet: LD Score regression (LDSC) distinguishing confounding/stratification from polygenicity in GWAS", "Universally validated statistical genetics benchmark"),
    ("B40", "PMC4636487", "Transcriptomics & CompBio", "Guinney et al. (2015) Nat Med: Consensus Molecular Subtypes (CMS1-4) of colorectal cancer across 18 datasets and 4,151 patients", "Standard replicated cancer transcriptomic taxonomy"),
    ("B41", "PMC4944528", "Transcriptomics & CompBio", "Tirosh et al. (2016) Science: single-cell RNA-seq dissection of metastatic melanoma ecosystem across 19 patients with orthogonal validation", "Foundational replicated cancer scRNA-seq study"),
    ("B42", "PMC5878932", "Transcriptomics & CompBio", "Puram et al. (2017) Cell: single-cell transcriptomic analysis of primary and metastatic head and neck cancer ecosystems", "Replicated across HNSCC cohorts"),
    ("B43", "PMC4878611", "Transcriptomics & CompBio", "Schurch et al. (2016) RNA: 48-biological-replicate empirical RNA-seq experiment benchmarking differential expression false positives and power", "Gold-standard empirical RNA-seq benchmark"),
    ("B44", "PMC8479118", "Transcriptomics & CompBio", "Squair et al. (2021) Nat Commun: empirical and simulation benchmark exposing pseudoreplication false discoveries in single-cell differential expression", "Definitive scRNA-seq statistical benchmark"),
    ("B45", "PMC7854630", "Transcriptomics & CompBio", "Zimmerman et al. (2021) Nat Commun: empirical demonstration and mixed-model solution for pseudoreplication bias in single-cell studies", "Co-published independent scRNA-seq statistical validation"),
    ("B46", "PMC4431643", "Viral Evolution", "Gire et al. (2014) Science: genomic surveillance of 2014 Ebola virus origin and transmission in West Africa", "Foundational viral genomic epidemiology study"),
    ("B47", "PMC4499780", "Viral Evolution", "Bedford et al. (2015) Nature: global circulation patterns of seasonal influenza viruses integrated with antigenic cartography", "Replicated phylodynamic benchmark"),
    ("B48", "PMC5536180", "Viral Evolution", "Grubaugh et al. (2017) Nature: genomic epidemiology of multiple Zika virus introductions into Florida", "Validated outbreak genomic epidemiology study"),
    ("B49", "PMC4869911", "Molecular Evolution", "Enard et al. (2016) eLife: empirical demonstration that viruses are a dominant driver of protein adaptation in mammals controlling for genomic confounders", "Replicated evolutionary genomics study"),
    ("B50", "PMC3106319", "Molecular Evolution", "Markova-Raina & Petrov (2011) Genome Res: empirical benchmark demonstrating high sensitivity to aligner errors and false positives in branch-site positive selection", "Definitive molecular evolution QC benchmark"),
]

def fetch_metadata(pmcid):
    url = f"https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=PMCID:{pmcid}&format=json"
    data = json.loads(urllib.request.urlopen(url, timeout=12).read().decode())
    res = data.get("resultList", {}).get("result", [])
    if not res:
        raise ValueError(f"Not found: {pmcid}")
    r = res[0]
    return {
        "pmcid": r.get("pmcid"),
        "pmid": r.get("pmid"),
        "doi": r.get("doi"),
        "title": r.get("title"),
        "authors": r.get("authorString"),
        "journal": r.get("journalTitle"),
        "year": int(r.get("pubYear", 0)),
        "citedByCount": int(r.get("citedByCount", 0)),
        "isOpenAccess": r.get("isOpenAccess")
    }

print("Building expanded Cohort A (50) and Cohort B (50)...")
cohort_a = list(cohorts["cohort_a"]) + [old_b02_as_a26]
for cid, pmcid, domain, flaw, refut in NEW_A_SPECS:
    m = fetch_metadata(pmcid)
    m.update({"cohort_id": cid, "cohort": "A", "domain": domain, "ground_truth_flaw": flaw, "refutation": refut})
    cohort_a.append(m)

cohort_b = [r for r in cohorts["cohort_b"] if r["cohort_id"] != "B02"]
for cid, pmcid, domain, note, val in NEW_B_SPECS:
    m = fetch_metadata(pmcid)
    m.update({"cohort_id": cid, "cohort": "B", "domain": domain, "validation_note": note, "validation": val})
    cohort_b.append(m)
cohort_b.sort(key=lambda x: x["cohort_id"])

cohort_c = list(cohorts["cohort_c"])
used_pmcids = {x["pmcid"] for x in cohort_a + cohort_b + cohort_c}

STRATA_C = [
    ("Viral Evolution", '(TITLE:"phylodynamic" OR TITLE:"molecular clock" OR TITLE:"viral evolution" OR TITLE:"spillover" OR TITLE:"genomic epidemiology") AND (TITLE:"virus" OR TITLE:"SARS-CoV-2" OR TITLE:"influenza" OR TITLE:"dengue" OR TITLE:"rabies" OR TITLE:"mpox")'),
    ("Molecular Evolution", '(TITLE:"positive selection" OR TITLE:"dN/dS" OR TITLE:"codon" OR TITLE:"purifying selection" OR TITLE:"adaptive evolution") AND (TITLE:"evolution" OR TITLE:"phylogen" OR TITLE:"genome" OR TITLE:"mammalian")'),
    ("Cancer & Microbiome", '(TITLE:"microbiome" OR TITLE:"metagenom" OR TITLE:"16S" OR TITLE:"microbiota") AND (TITLE:"cancer" OR TITLE:"tumor" OR TITLE:"colorectal" OR TITLE:"gut") AND (TITLE:"classifier" OR TITLE:"biomarker" OR TITLE:"signature" OR TITLE:"dysbiosis")'),
    ("Statistical Genetics", '(TITLE:"genome-wide association" OR TITLE:"polygenic" OR TITLE:"GWAS" OR TITLE:"heritability" OR TITLE:"Mendelian randomization") AND (TITLE:"stratification" OR TITLE:"selection" OR TITLE:"risk score" OR TITLE:"trait" OR TITLE:"architecture")'),
    ("Transcriptomics & CompBio", '(TITLE:"RNA-seq" OR TITLE:"single-cell" OR TITLE:"differential expression" OR TITLE:"transcriptom") AND (TITLE:"machine learning" OR TITLE:"network" OR TITLE:"deconvolution" OR TITLE:"signature" OR TITLE:"prognostic")'),
]

rng = random.Random(20261030)
c_idx = 26

print("Sampling 75 additional Cohort C wild papers (15 per subfield -> 20 per subfield = 100 total)...")
for domain, q_base in STRATA_C:
    q = f'{q_base} AND IN_EPMC:Y AND OPEN_ACCESS:Y AND PUB_YEAR:[2018 TO 2025] AND PUB_TYPE:"Journal Article" NOT PUB_TYPE:"Review" NOT PUB_TYPE:"Retracted Publication" NOT PUB_TYPE:"Preprint"'
    url = f"https://www.ebi.ac.uk/europepmc/webservices/rest/search?query={urllib.parse.quote(q)}&format=json&pageSize=250"
    data = json.loads(urllib.request.urlopen(url, timeout=20).read().decode())
    pool = [
        r for r in data.get("resultList", {}).get("result", [])
        if r.get("pmcid") and r.get("pmcid") not in used_pmcids
        and r.get("pmid")
        and not any(w in r.get("title", "") for w in ["Correction", "Erratum", "Retraction"])
    ]
    # Stratify 15 new papers per domain: 5 High (>=25), 5 Mid (5-24), 5 Low (0-4)
    high = [r for r in pool if int(r.get("citedByCount", 0)) >= 25]
    mid = [r for r in pool if 5 <= int(r.get("citedByCount", 0)) < 25]
    low = [r for r in pool if int(r.get("citedByCount", 0)) < 5]

    picked = []
    for bucket, k in [(high, 5), (mid, 5), (low, 5)]:
        if len(bucket) >= k:
            picked.extend(rng.sample(bucket, k))
        else:
            picked.extend(bucket)
    while len(picked) < 15 and len(pool) > len(picked):
        rem = [r for r in pool if r not in picked]
        picked.append(rng.choice(rem))

    for r in picked[:15]:
        used_pmcids.add(r.get("pmcid"))
        cites = int(r.get("citedByCount", 0))
        cite_tier = "High (>=25)" if cites >= 25 else ("Mid (5-24)" if cites >= 5 else "Low (0-4)")
        cohort_c.append({
            "cohort_id": f"C{c_idx:03d}" if c_idx >= 100 else f"C{c_idx:02d}",
            "cohort": "C",
            "domain": domain,
            "citation_tier": cite_tier,
            "pmcid": r.get("pmcid"),
            "pmid": r.get("pmid"),
            "doi": r.get("doi"),
            "title": r.get("title"),
            "authors": r.get("authorString"),
            "journal": r.get("journalTitle"),
            "year": int(r.get("pubYear", 0)),
            "citedByCount": cites,
            "isOpenAccess": r.get("isOpenAccess")
        })
        c_idx += 1

with open("/Users/sergei/Projects/lit-estimation/cohorts_200.json", "w") as f:
    json.dump({"cohort_a": cohort_a, "cohort_b": cohort_b, "cohort_c": cohort_c}, f, indent=2)

print(f"Saved cohorts_200.json: A={len(cohort_a)}, B={len(cohort_b)}, C={len(cohort_c)}")
