import urllib.request
import urllib.parse
import json
import random
from concurrent.futures import ThreadPoolExecutor

# 25 Verified Cohort A papers (Known Invalid / Refuted / Retracted under Scrutiny)
COHORT_A_SPECS = [
    ("A01", "PMC9404229", "Viral Evolution", "PCR positive-control carryover + invalid linear clock extrapolation from single-locus amplicons", "Worobey et al. / community scrutiny"),
    ("A02", "PMC7107875", "Viral Evolution", "Tang et al. (2020) L/S lineage claim: mistaking founder effect & ascertainment for intrinsic selective advantage and misusing dN/dS on intraspecific polymorphism", "MacLean et al. (2020) Nat Microbiol"),
    ("A03", "PMC7196762", "Viral Evolution", "Forster et al. (2020) PNAS median-joining network: inappropriate distance rooting with divergent bat virus and homoplasy misinterpretation", "Sanchez-Pacheco et al. (2020) PNAS; Mavian et al. (2020) PNAS"),
    ("A04", "PMC7184484", "Molecular Evolution", "Xia (2020) MBE canine origin of SARS-CoV-2 from CpG deficiency: failed to control for broader bat sarbecovirus CpG distribution and ZAP biology", "Pollock et al. (2020) MBE"),
    ("A05", "PMC7138088", "Molecular Evolution", "Ji et al. (2020) JMV snake reservoir & spike homologous recombination claim from RSCU codon bias: invalid distance metric and background host set", "Zhang et al. (2020) JPR; Castells et al. (2020) JMV"),
    ("A06", "PMC9349972", "Viral Evolution", "Desingu et al. (2022) JMV Omicron BA.4/BA.5 mouse host origin claim: misinterpreting mutational spectra and dN/dS without phylogenetic controls", "Post-publication phylogenetic refutations"),
    ("A07", "PMC7199730", "Viral Evolution", "van Dorp et al. (2020) Infect Genet Evol recurrent mutations in SARS-CoV-2: unmasked sequencing/amplicon homoplasy artifacts and host RNA editing confounding", "De Maio et al. (2020); Turakhia et al. (2020) PLoS Genet"),
    ("A08", "PMC7428442", "Viral Epidemiology", "La Rosa et al. (2021) Northern Italy Dec 2019 wastewater SARS-CoV-2: nested PCR amplicon contamination and discordant assay results", "Environmental surveillance methodological critiques"),
    ("A09", "PMC8529295", "Viral Epidemiology", "Apolone et al. (2020) Tumori Sept 2019 SARS-CoV-2 antibodies in Italy: uncalibrated cross-reactive ELISA/neutralization without pre-pandemic negative specificity controls", "WHO/re-testing & serological specificity critiques"),
    ("A10", "PMC7276232", "Viral Evolution", "Chaw et al. (2020) JMV cooperative synonymous mutations driving SARS-CoV-2 outbreak: confounding genealogical linkage (hitchhiking) with epistatic selection", "MacLean et al. (2020) / phylogenetic linkage critiques"),
    ("A11", "PMC5182071", "Population Genomics", "Field et al. (2016) Science Singleton Density Score (SDS) polygenic adaptation on height in Britons: GIANT GWAS population stratification confounding", "Sohail et al. (2019) eLife; Berg et al. (2019) eLife"),
    ("A12", "PMC7267315", "Viral Epidemiology", "Becerra-Flores & Cardozo (2020) G614 higher case fatality rate: ecological fallacy & temporal confounding across country epidemic stages", "Volz et al. (2021); ecological confounding critiques"),
    ("A13", "PMC7375454", "Viral Genomics", "Toyoshima et al. (2020) ORF1ab variants associated with COVID-19 mortality: uncorrected ecological/country-level population structure confounding", "Phylogenetic & epidemiological confounding critiques"),
    ("A14", "PMC7247990", "Viral Epidemiology", "Bhattacharyya et al. (2020) D614G and host protease polymorphism mortality correlation: country-level ecological regression without individual-level linkage", "Ecological fallacy critiques"),
    ("A15", "PMC7395502", "Epidemiology / Stats", "Escobar et al. (2020) PNAS BCG vaccination protection against severe COVID-19: residual epidemic-stage, reporting, and spatial confounding", "Hensel et al. (2020); randomized trial & methodological refutations"),
    ("A16", "PMC7500457", "Cancer Microbiome", "Poore et al. (2020) Nature blood/tissue cancer microbiome diagnostic (Retracted): human read contamination in microbial genomes + Voom-SNM supervised batch correction leakage", "Gihawi et al. (2023) mBio"),
    ("A17", "PMC6858566", "Cancer Microbiome", "Aykut et al. (2019) Nature fungal mycobiome promotes pancreatic oncogenesis (Retracted): low-biomass sequence contamination & batch artifacts", "Fletcher et al. (2023) Nature"),
    ("A18", "PMC9567272", "Cancer Microbiome", "Narunsky-Haziza et al. (2022) Cell pan-cancer mycobiome: low-biomass human/reagent read misclassification and supervised normalization leakage", "Gihawi et al. (2023); Salzberg et al. critiques"),
    ("A19", "PMC7757858", "Cancer Microbiome", "Nejman et al. (2020) Science human tumor microbiome: low-biomass contamination controls and cross-batch classifier inflation concerns", "Tumor microbiome reanalysis literature"),
    ("A20", "PMC5617305", "Statistical Genetics", "Lippert et al. (2017) PNAS individual identification from WGS trait prediction: ancestry/demographic confounding driving apparent matching accuracy", "Erlich (2017) bioRxiv/Nature news refutation"),
    ("A21", "PMC6613792", "Statistical Genetics", "Wei & Nielsen (2019) Nat Med CCR5-delta32 homozygote mortality (Retracted): UK Biobank genotyping probe batch/calling artifact violating HWE", "Maier et al. (2020) Nat Med"),
    ("A22", "PMC3261167", "Statistical Genetics", "Sebastiani et al. (2012/2010) exceptional longevity GWAS: platform-specific SNP array strand/batch mismatch between cases and controls (Science 2010 retracted)", "MacArthur / Sebastiani Science retraction (2011)"),
    ("A23", "PMC3480734", "Population Genomics", "Turchin et al. (2012) Nat Genet polygenic adaptation on height in Europe: uncorrected population stratification in GIANT GWAS summary statistics", "Sohail et al. (2019) eLife; Berg et al. (2019) eLife"),
    ("A24", "PMC4125079", "Population Genomics", "Berg & Coop (2014) PLoS Genet polygenic adaptation signal across populations: residual GIANT GWAS stratification inflating excess variance signals", "Berg et al. (2019) eLife self-correction"),
    ("A25", "PMC3935878", "Macroevolution / Stats", "Rabosky (2014) BAMM diversification rate shifts on extant timetrees: unidentifiability of speciation/extinction rate histories and compound Poisson prior pathology", "Moore et al. (2016) PNAS; Louca & Pennell (2020) Nature"),
]

# 25 Verified Cohort B papers (Validated / Stress-Tested / Replicated / Rigorous Controls)
COHORT_B_SPECS = [
    ("B01", "PMC8421097", "Viral Evolution", "Martin, Weaver et al. (2021) Cell: convergent evolution of SARS-CoV-2 N501Y lineages (already reviewed: 8.6/10)", "Validated across Omicron/subsequent VOCs"),
    ("B02", "PMC8135569", "Viral Evolution", "Kumar et al. (2021) MBE: mutational order portrait of progenitor SARS-CoV-2 (already reviewed: 7.5/10)", "Validated against Huanan market / early lineage reconstructions"),
    ("B03", "PMC7990310", "Viral Evolution", "MacLean et al. (2021) PLoS Biol: natural selection in the evolution of SARS-CoV-2 in bats", "Rigorous FEL/MEME/BUSTED sarbecovirus selection benchmark"),
    ("B04", "PMC7332439", "Viral Evolution", "Korber et al. (2020) Cell: Spike D614G increases SARS-CoV-2 infectivity and frequency", "Independently replicated in vitro, in vivo, and epidemiologically"),
    ("B05", "PMC7810038", "Viral Evolution", "Worobey et al. (2020) Science: emergence of SARS-CoV-2 in Europe and North America", "Validated phylodynamic + epidemiological simulation benchmark"),
    ("B06", "PMC9348752", "Viral Evolution", "Pekar et al. (2022) Science: molecular epidemiology of multiple zoonotic origins of SARS-CoV-2", "Heavily stress-tested phylodynamic & epidemic simulation analysis"),
    ("B07", "PMC9348750", "Viral Epidemiology", "Worobey et al. (2022) Science: Huanan Seafood Market early epicenter spatial & genomic analysis", "Stress-tested spatial statistics & genomic epidemiology"),
    ("B08", "PMC8942855", "Viral Evolution", "Viana et al. (2022) Nature: rapid epidemic expansion of SARS-CoV-2 Omicron in southern Africa", "Validated genomic surveillance & selection analysis"),
    ("B09", "PMC7610519", "Viral Genomics", "Rambaut et al. (2020) Nat Microbiol: Pango dynamic nomenclature for SARS-CoV-2 lineages", "Foundational, universally adopted genomic taxonomy system"),
    ("B10", "PMC7721162", "Viral Genomics", "Turakhia et al. (2020) PLoS Genet: stability of SARS-CoV-2 phylogenies and systematic homoplasy/contamination masking", "Gold-standard phylogenetic QC benchmark"),
    ("B11", "PMC8128288", "Viral Epidemiology", "Davies et al. (2021) Science: estimated transmissibility and impact of SARS-CoV-2 B.1.1.7 in England", "Replicated across countries and modeling frameworks"),
    ("B12", "PMC8139423", "Viral Epidemiology", "Faria et al. (2021) Science: genomics and epidemiology of P.1 (Gamma) lineage in Manaus, Brazil", "Validated phylodynamic & epidemiological multi-model inference"),
    ("B13", "PMC9161372", "Viral Evolution", "Obermeyer et al. (2022) Science: PyR0 hierarchical Bayesian fitness inference across 6.4M SARS-CoV-2 genomes", "Validated against DMS and experimental neutralization"),
    ("B14", "PMC10506532", "Viral Evolution", "Bloom & Neher (2023) Virus Evol: mutational fitness effects across SARS-CoV-2 proteins from millions of sequences", "Validated against deep mutational scanning (DMS) benchmarks"),
    ("B15", "PMC5712493", "Viral Evolution", "Dudas et al. (2017) Nature: West African Ebola epidemic phylodynamics and GLM spatial spread", "Gold-standard viral phylodynamics benchmark"),
    ("B16", "PMC10653788", "Cancer Microbiome", "Gihawi et al. (2023) mBio: forensic reanalysis demonstrating human-read contamination and batch leakage in Poore et al.", "Validated forensic bioinformatics rebuttal"),
    ("B17", "PMC6428571", "Population Genomics", "Sohail et al. (2019) eLife: demonstrating uncorrected GWAS stratification in height polygenic adaptation", "Replicated in sibling/UKB analyses"),
    ("B18", "PMC6428572", "Population Genomics", "Berg et al. (2019) eLife: reduced signal for polygenic adaptation of height in UK Biobank", "Co-published independent validation of GWAS stratification"),
    ("B19", "PMC3395634", "Molecular Evolution", "Murrell et al. (2012) PLoS Genet: MEME mixed effects model for episodic diversifying selection", "Standard validated selection method with extensive simulation calibration"),
    ("B20", "PMC4408417", "Molecular Evolution", "Murrell et al. (2015) MBE: BUSTED gene-wide episodic selection test", "Standard calibrated likelihood ratio test with null/power simulations"),
    ("B21", "PMC8204705", "Molecular Evolution", "Kosakovsky Pond et al. (2020) MBE: HyPhy 2.5 platform for evolutionary hypothesis testing", "Heavily tested open-source evolutionary inference framework"),
    ("B22", "PMC7182206", "Molecular Evolution", "Minh et al. (2020) MBE: IQ-TREE 2 phylogenetic inference and model selection", "Standard benchmarked maximum-likelihood phylogenetics suite"),
    ("B23", "PMC6247931", "Viral Genomics", "Hadfield et al. (2018) Bioinformatics: Nextstrain real-time tracking of pathogen evolution", "Standard open-source phylodynamic pipeline"),
    ("B24", "PMC4302049", "Transcriptomics / Stats", "Love, Huber & Anders (2014) Genome Biol: DESeq2 moderated fold change and dispersion estimation", "Heavily benchmarked empirical Bayes differential expression method"),
    ("B25", "PMC8922736", "Transcriptomics / Stats", "Li et al. (2022) Genome Biol: rigorous evaluation of false positives in population-scale differential expression", "Validated simulation + permutation benchmark"),
]

def fetch_metadata(pmcid):
    url = f"https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=PMCID:{pmcid}&format=json"
    data = json.loads(urllib.request.urlopen(url, timeout=10).read().decode())
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

print("Fetching Cohort A and Cohort B metadata...")
cohort_a = []
for cid, pmcid, domain, flaw, refutation in COHORT_A_SPECS:
    m = fetch_metadata(pmcid)
    m.update({"cohort_id": cid, "cohort": "A", "domain": domain, "ground_truth_flaw": flaw, "refutation": refutation})
    cohort_a.append(m)

cohort_b = []
for cid, pmcid, domain, note, validation in COHORT_B_SPECS:
    m = fetch_metadata(pmcid)
    m.update({"cohort_id": cid, "cohort": "B", "domain": domain, "validation_note": note, "validation": validation})
    cohort_b.append(m)

used_pmcids = {x["pmcid"] for x in cohort_a + cohort_b}

# Sample Cohort C (25 Stratified Wild Papers from Europe PMC Open Access, 5 per domain)
STRATA_C = [
    ("Viral Evolution", '(TITLE:"phylodynamic" OR TITLE:"molecular clock" OR TITLE:"viral evolution" OR TITLE:"spillover") AND (TITLE:"virus" OR TITLE:"SARS-CoV-2" OR TITLE:"influenza" OR TITLE:"dengue")'),
    ("Molecular Evolution", '(TITLE:"positive selection" OR TITLE:"dN/dS" OR TITLE:"codon" OR TITLE:"purifying selection") AND (TITLE:"evolution" OR TITLE:"phylogen" OR TITLE:"genome")'),
    ("Cancer & Microbiome", '(TITLE:"microbiome" OR TITLE:"metagenom" OR TITLE:"16S") AND (TITLE:"cancer" OR TITLE:"tumor" OR TITLE:"colorectal" OR TITLE:"gut") AND (TITLE:"classifier" OR TITLE:"biomarker" OR TITLE:"signature")'),
    ("Statistical Genetics", '(TITLE:"genome-wide association" OR TITLE:"polygenic" OR TITLE:"GWAS" OR TITLE:"heritability") AND (TITLE:"stratification" OR TITLE:"selection" OR TITLE:"risk score" OR TITLE:"trait")'),
    ("Transcriptomics & CompBio", '(TITLE:"RNA-seq" OR TITLE:"single-cell" OR TITLE:"differential expression" OR TITLE:"transcriptom") AND (TITLE:"machine learning" OR TITLE:"network" OR TITLE:"deconvolution" OR TITLE:"signature")'),
]

rng = random.Random(20261027)
cohort_c = []
c_idx = 1

print("Sampling Cohort C (Wild Stratified Sample)...")
for domain, q_base in STRATA_C:
    q = f'{q_base} AND IN_EPMC:Y AND OPEN_ACCESS:Y AND PUB_YEAR:[2019 TO 2025] AND PUB_TYPE:"Journal Article" NOT PUB_TYPE:"Review" NOT PUB_TYPE:"Retracted Publication" NOT PUB_TYPE:"Preprint"'
    url = f"https://www.ebi.ac.uk/europepmc/webservices/rest/search?query={urllib.parse.quote(q)}&format=json&pageSize=100"
    data = json.loads(urllib.request.urlopen(url, timeout=15).read().decode())
    pool = [
        r for r in data.get("resultList", {}).get("result", [])
        if r.get("pmcid") and r.get("pmcid") not in used_pmcids
        and r.get("pmid")
        and "Correction" not in r.get("title", "")
        and "Erratum" not in r.get("title", "")
    ]
    # Stratify pool by citations: 2 high (>=25 cites), 2 mid (5-24 cites), 1 low (0-4 cites)
    high = [r for r in pool if int(r.get("citedByCount", 0)) >= 25]
    mid = [r for r in pool if 5 <= int(r.get("citedByCount", 0)) < 25]
    low = [r for r in pool if int(r.get("citedByCount", 0)) < 5]
    
    picked = []
    for bucket, k in [(high, 2), (mid, 2), (low, 1)]:
        if len(bucket) >= k:
            picked.extend(rng.sample(bucket, k))
        else:
            picked.extend(bucket)
    while len(picked) < 5 and len(pool) > len(picked):
        rem = [r for r in pool if r not in picked]
        picked.append(rng.choice(rem))
        
    for r in picked[:5]:
        used_pmcids.add(r.get("pmcid"))
        cites = int(r.get("citedByCount", 0))
        cite_tier = "High (>=25)" if cites >= 25 else ("Mid (5-24)" if cites >= 5 else "Low (0-4)")
        cohort_c.append({
            "cohort_id": f"C{c_idx:02d}",
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

all_cohorts = {"cohort_a": cohort_a, "cohort_b": cohort_b, "cohort_c": cohort_c}
with open("/Users/sergei/Projects/lit-estimation/cohorts.json", "w") as f:
    json.dump(all_cohorts, f, indent=2)

print(f"Saved cohorts.json: A={len(cohort_a)}, B={len(cohort_b)}, C={len(cohort_c)}")
