# Decision Letter 0


### Sarath Chandra Janga


#### Roles

This is an open access article distributed under the terms of the Creative Commons Attribution License , which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.

kMermaid: Ultrafast functional classification of microbial reads

PLOS Computational Biology

Thank you for submitting your manuscript to PLOS Computational Biology. After careful consideration, we feel that it has merit but does not fully meet PLOS Computational Biology's publication criteria as it currently stands. Therefore, we invite you to submit a revised version of the manuscript that addresses the points raised during the review process.

Please submit your revised manuscript within 60 days Jun 15 2025 11:59PM. If you will need more time than this to complete your revisions, please reply to this message or contact the journal office at ploscompbiol@plos.org. When you're ready to submit your revision, log on to https://www.editorialmanager.com/pcompbiol/ and select the 'Submissions Needing Revision' folder to locate your manuscript file.

Please include the following items when submitting your revised manuscript:

* A rebuttal letter that responds to each point raised by the editor and reviewer(s). You should upload this letter as a separate file labeled 'Response to Reviewers'. This file does not need to include responses to formatting updates and technical items listed in the 'Journal Requirements' section below.

* A marked-up copy of your manuscript that highlights changes made to the original version. You should upload this as a separate file labeled 'Revised Manuscript with Track Changes'.

* An unmarked version of your revised paper without tracked changes. You should upload this as a separate file labeled 'Manuscript'.

If you would like to make changes to your financial disclosure, competing interests statement, or data availability statement, please make these updates within the submission form at the time of resubmission. Guidelines for resubmitting your figure files are available below the reviewer comments at the end of this letter

We look forward to receiving your revised manuscript.

Sarath Chandra Janga, Ph.D

PLOS Computational Biology

PLOS Computational Biology

Additional Editor Comments :

Although reviewers agreed on the simplicity and utility of the proposed metagenomic tool kMermaid, several critical concerns were raised by all three reviewers regarding the methodology, novelty, benchmarking, and clarity. In particular, I am willing to consider a significantly revised version of the manuscript which addresses the major concerns raised by the reviewers including those highlighted below.

• Improve the benchmarking of the tool by comparing speed/accuracy against MMseq2, DIAMOND and other existing tools using standardized datasets.

• Clearly make the case for the novelty of the tool by differentiating kMermaid’s approach from existing tools (e.g., cluster definitions, ambiguity metrics).

• Provide details of the method by formalizing the algorithm, revise figures for clarity, and define terms such as "truncated reads" to avoid ambiguity.

• Justify the use of protein clusters as functional proxies or adopt orthology databases. For instance, established orthology databases (KEGG, EggNOG, Pfam) are preferred for functional annotation since clustering at 65–70% identity is a poor proxy for function.

Journal Requirements:

1) We ask that a manuscript source file is provided at Revision. Please upload your manuscript file as a .doc, .docx, .rtf or .tex. If you are providing a .tex file, please upload it under the item type u2018LaTeX Source Fileu2019 and leave your .pdf version as the item type u2018Manuscriptu2019.

2) Please provide an Author Summary. This should appear in your manuscript between the Abstract (if applicable) and the Introduction, and should be 150-200 words long. The aim should be to make your findings accessible to a wide audience that includes both scientists and non-scientists. Sample summaries can be found on our website under Submission Guidelines:

https://journals.plos.org/ploscompbiol/s/submission-guidelines#loc-parts-of-a-submission

3) Please upload all main figures as separate Figure files in .tif or .eps format. For more information about how to convert and format your figure files please see our guidelines:

https://journals.plos.org/ploscompbiol/s/figures

4) We have noticed that you have uploaded Supporting Information files, but you have not included a list of legends. Please add a full list of legends for your Supporting Information files after the references list.

5) Please amend your detailed Financial Disclosure statement. This is published with the article. It must therefore be completed in full sentences and contain the exact wording you wish to be published.

1) State the initials, alongside each funding source, of each author to receive each grant. For example: "This work was supported by the National Institutes of Health (####### to AM; ###### to CJ) and the National Science Foundation (###### to AM)."

2) State what role the funders took in the study. If the funders had no role in your study, please state: "The funders had no role in study design, data collection and analysis, decision to publish, or preparation of the manuscript."

6) Please amend the description of the manuscript in the online submission form to "Manuscript" rather than "Cover Letter."

Reviewer's Responses to Questions

Reviewer #1: This work describes a new metagenomic functional profiler tool. The key idea seems to be to first cluster proteins into clusters. However, this is a common approach used by all functional profilers in that they work with existing clusters of orthologous genes (e.g. KEGG OC, EggNOG, COG). Once the clusters are formed, kMermaid seems to use a very standard approach of matching kmers. The approach seems pretty straightforward and perhaps there-in lies its utility.

1. Why does kMermaid have to rely on its own clusters of proteins? Why cannot it use existing databases?

2. The results in figure 2 do not seem very interesting or clear to me. For example, for part a, why would you not use BLASTX results at the cluster level as well? Also part d is hard to interpret. I am not sure I understand what is being conveyed here or that it is important.

3. Similarly figure 3 also does not seem to be conveying anything interesting in terms of a result.

4. Why does the comparison with DIAMOND also not include an evaluation of sensitivity and specificity? Also, why are other recently published tools (e.g. fmh-funprofiler: https://academic.oup.com/bioinformatics/article/40/Supplement_2/ii165/7749078 ) not included in this comparison?

Reviewer #2: This manuscript presents kMermaid, a tool to assign functions to short metagenomic reads. The ideas are interesting and the software is well implemented, but I feel that the authors are overselling the advantages of their approach compared to existing alternatives, mostly by artificially constraining the comparison to only one family of approaches (BLASTX/DIAMOND). The benchmarking is rather simplistic as well.

1. When describing the advantages of kMermaid, the authors claim that it leads to fewer ambiguous mappings, but partly this is achieved by using a different definition of ambiguity so that it applies more strictly when BLASTX is being evaluated than when kMermaid is being evaluated (Fig 2a). For example, if a read is multi-mapped to proteins A1, A2, and A3; but they all share the same cluster, then the read is ambigous at the protein level, but not at the cluster level. This is not novel in the field, but it is should be differentiated what is due to a different tool vs. a different definition of ambiguity.

BLASTX is designed to be very sensitive as well (compared to other alternatives, such as DIAMOND or mapping to nucleotide databases, such as gene catalogs), thus it will map reads to more proteins.

2. I disagree that "BLASTX remains the gold standard" for querying metagenomic reads against a large database. Despite having published many papers using metagenomics data, I have never used BLASTX for this purpose. If working in a reference-based manner, I would use nucleotide-alignment (such as bwa or strobealign) to a gene catalog (either the venerable IGC if working with the human gut [ https://doi.org/10.1038/nbt.2942 ] or a more recent one [ https://doi.org/10.1038/s41586-021-04233-4 ]) or a catalog of genomes (including MAGs, [ https://doi.org/10.1038/s41587-020-0603-3 ]). Alternatively, the authors could use the set of 1,793,361 sequences they considered (after dereplicating at 97% or 95% nucleotide identity). I would use eggnogmapper [ https://doi.org/10.1093/molbev/msab293 ] to assign functions to the genes. At the very least, the authors need to acknowledge that there are other approaches that are widely used in the field and, ideally, compare their tool to these alternatives.

3. The authors use the term "functional", but they are simply assigning to a protein cluster at 65%/70% identity. Why is this a good proxy for function? Normally, when discussing function, an orthologous group is used (KEGG being the most popular, but also eggNOG, Pfam, ... or function-specific databases such as CARD for antibiotic resistance, CAZy for carbohydrate enzymes, ...). The authors should clarify this point.

4. A typical test that is missing is to remove certain taxonomic groups from the database while using them in simulation (to mimic the case where the real world contains species/strains absent in the database). While still limited, this would be closer to a real-world scenario. I generally refrain from asking for specific experiments in reviews, but this paper is really lacking in having a more realistic benchmark.

"human samples" -> "human gut samples"

Reviewer #3: The manuscript introduces kmermaid, which is capable of performing functional classification of metagenomes. It focuses on speed, low memory consumption and disambiguation when assigning metagenomic reads against a pre-calculated database of protein clusters.

It avoids the effort of taxonomic disambiguation by performing clustering of reads translated to their amino acid sequences and counting k-mer matches against precomputed protein clusters. The algorithm is rather simple: a single read (not assembled) is translated into all possible reading frames, and the contained k-mers are compared to a set of precomputed protein clusters in what looks like a rather brute-force approach (no indexing/hashing/sorting is mentioned). The cluster with most exact matches is chosen for functional annotation transfer.

The paper is well written and the code it is accompanied with is well structured and organized. However there are a number of major concerns I have with the manuscript.

MMseq2 [1], DIAMOND, Super-FOCUS and FMAP (Fast Metagenomic Functional Profiling) also address the same research question and are established methods (several years old). The authors should carve out their novelty with respect to them and/or ideally quantify performance measures such as speed and accuracy (the current version only contains runtime comparison to DIAMOND). The introduction does not comprehensively summarize the state of the art (except for DIAMOND). The benchmark should be designed such that a more direct and comprehensive comparison is possible. Ideally, the same benchmarks from e.g. MMseq2 could be used. Thus the benchmarking with the state of the art is not rigorous/comprehensive enough.

The main algorithm isn’t presented formally and Figure 1 lacks detail and rigor. Subfigures with labels a-e (like in some of the other figures) would be desirable, also for a more structured caption of Figure 1. Alternatively, pseudo-code could be accompanied. It is not entirely clear what is meant with ‘truncated reads’ (together with the X-shaped symbols) – it could be truncation due to instrumental limitations from sequencing technology, low quality bases, incomplete synthesis (premature termination) during sequencing or the presence of a stop codon – which one is it?

Figure 2 claims that BLASTX has a large amount of ambiguous functional maps. 1. It is not clear from the manuscript whether the BLASTX ambiguity is derived from raw scores or E-values (or something else altogether), as it seems that raw scores would also lead to less ambiguous maps. 2. How about the other state of the art methods? Do they also exhibit such high levels of ambiguity?

Fig 2a) how are the 3 metagenomic samples chosen?

2c) It seems odd that the x-axis exceeds 100% (probably an artefact from KDE)

2d) the x-axis has k-mers “sorted”. It would be best to make clear that the sorting isbased on the number of clusters, a k-mer appears in. When the text refers to Figure 2d) it mentions a single cluster being common (22%), this is not obvious from the Figure, but it could be marked. Likewise the 19% of k-mers falling into >10 clusters

How did the authors come to 2.5M k-mers. There are approx. 205 =3.2 possibilities for 5-mers. In general the choice of k is not fully motivated

The method section does not motivate some of the design choices made:

• Why 65% (1. Step) and 70% (2. Step) were used as thresholds for clustering of the precomputed model

• Why are there 2 steps, with first some 43K proteins (how are they exactly selected? From NCBI’s Prokaryotic Reference Genomes?) and then with 1.7M?

Since the 2-step clustering is non-standard and differs from plain CD-HIT, it would be good to get a sense of clustering quality as measured by a clustering coefficient like the Silhouette or Dunn index or homogeneity/separation ratio.

Was the hyperparameter (k) evaluation done according to best practices? I.e., was it conducted with proper dataset splits (inner validation sets for model/hyperparameter selection and “outer” final test set(s), which was entirely unused(!) during hyperparameter selection? How sensitive are the results to a change of k?

Limitations should be clearer. Avoiding assembly is obiouslybeneficial from a computational point of view, but lacks the uniqueness/predictive power stemming from assembled contigs.It would be desirable, if that could be quantified. The selection of 43K reference proteins most likely contains multi-domain proteins. There are occasions when read assembly is important:

1. Multidomain Proteins & Functional Context:

o Many functional proteins, especially in signaling (e.g., two-component systems) and metabolism, derive their activity from domain interactions.

o If sequence reads only cover individual domains, assigning function may be incomplete or misleading (e.g., distinguishing a full enzymatic complex from fragments).

o Assembling longer contigs helps reconstruct the true architecture of multidomain proteins.

2. Pathway Reconstruction & Gene Clustering:

o Some pathways rely on synteny (gene order and co-localization), which is lost in fragmented reads.

o Functional units like operons in prokaryotes may be misclassified if only single reads are used.

3. Taxonomic and Functional Coupling:

o If a gene is part of a mobile genetic element (e.g., plasmid, transposon), assembly can clarify if it belongs to a specific species or is horizontally transferred.

Another limitation is that beyond the precomputed protein clusters, novel proteins in metagenomes will be ignored. While this is common to many methods, it should probably be mentioned.

It would be very useful if the presented work could assess the amount of misclassification coming from unassembled reads (vs assembled reads).

Assessing the quality of the initial clustering is also important:

Regarding memory consumption, DIAMONDs strategy seems a realistic approach (scaling with input, capping at 16GB). There should be a stronger motivation for a limitation to 2GB, an amount that is exceeded by nearly any reasonable machine in use these days. It is not clear how the 2GB memory requirement is achieved – streaming/generators?

A central point is that existing methods (particularly BLASTX, not so sure about the other abovementioned methods) have a high percentage of ambiguous mappings (Fig. 2). Have the authors

Regarding speed comparisons, indexing is an extremely common method in databases to perform fast lookup. It is also used in [1]. kMermaid does not use indexing or other fast information retrieval methods hashing/LSH, sorting etc. It would be helpful to provide insides as to why such common/best practices were not deployed/necessary.

There are a few technical issues with the installation. Both on Ubuntu 20.04 (as recommended) and Mac OS 15.3, large file installation did not seem to work as described in the installation instructions: even with git-lfs installed, the file kmermaid/db/kmer_model.pkl is only 134bytes and thus not useful (not readable with pickle). The alternative method using the wget command (as per the github install instructions) does not give a larger file.

[1] Steinegger, M., Söding, J. MMseqs2 enables sensitive protein sequence searching for the analysis of massive data sets. Nat Biotechnol 35, 1026–1028 (2017). https://doi.org/10.1038/nbt.3988

Have the authors made all data and (if applicable) computational code underlying the findings in their manuscript fully available?

The PLOS Data policy requires authors to make all data and code underlying the findings described in their manuscript fully available without restriction, with rare exception (please refer to the Data Availability Statement in the manuscript PDF file). The data and code should be provided as part of the manuscript or its supporting information, or deposited to a public repository. For example, in addition to summary statistics, the data points behind means, medians and variance measures should be available. If there are restrictions on publicly sharing data or code —e.g. participant privacy or use of data from a third party—those must be specified.

PLOS authors have the option to publish the peer review history of their article ( what does this mean? ). If published, this will include your full peer review and any attached files.

If you choose “no”, your identity will remain anonymous but your review may still be made public.

Do you want your identity to be public for this peer review? For information about this choice, including consent withdrawal, please see our Privacy Policy .

Reviewer #3: Yes: Andreas Henschel

[NOTE: If reviewer comments were submitted as an attachment file, they will be attached to this email and accessible via the submission site. Please log into your account, locate the manuscript record, and check for the action link "View Attachments". If this link does not appear, there are no attachment files.]

While revising your submission, please upload your figure files to the Preflight Analysis and Conversion Engine (PACE) digital diagnostic tool, https://pacev2.apexcovantage.com/ . PACE helps ensure that figures meet PLOS requirements. To use PACE, you must first register as a user. Registration is free. Then, login and navigate to the UPLOAD tab, where you will find detailed instructions on how to use the tool. If you encounter any issues or have any questions when using PACE, please email PLOS at figures@plos.org. Please note that Supporting Information files do not need this step. If there are other versions of figure files still present in your submission file inventory at resubmission, please replace them with the PACE-processed versions.

To enhance the reproducibility of your results, we recommend that authors of applicable studies deposit laboratory protocols in protocols.io, where a protocol can be assigned its own identifier (DOI) such that it can be cited independently in the future. Additionally, PLOS ONE offers an option to publish peer-reviewed clinical study protocols. Read more information on sharing protocols at https://plos.org/protocols?utm_medium=editorial-email&utm_source=authorletters&utm_campaign=protocols


# Author response to Decision Letter 1

Collection date 2025 Sep.

Submitted filename: Reviewers-response.docx


# Decision Letter 1


### Sarath Chandra Janga


#### Roles

This is an open access article distributed under the terms of the Creative Commons Attribution License , which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.

PCOMPBIOL-D-25-00398R1

kMermaid: Ultrafast metagenomic read assignment to protein clusters by hashing of amino-acid k-mer frequencies

PLOS Computational Biology

Thank you for submitting your manuscript to PLOS Computational Biology. After careful consideration, we feel that it has merit but does not fully meet PLOS Computational Biology's publication criteria as it currently stands. Therefore, we invite you to submit a revised version of the manuscript that addresses the points raised during the review process.

Please submit your revised manuscript within 30 days Sep 26 2025 11:59PM. If you will need more time than this to complete your revisions, please reply to this message or contact the journal office at ploscompbiol@plos.org. When you're ready to submit your revision, log on to https://www.editorialmanager.com/pcompbiol/ and select the 'Submissions Needing Revision' folder to locate your manuscript file.

Please include the following items when submitting your revised manuscript:

* A rebuttal letter that responds to each point raised by the editor and reviewer(s). You should upload this letter as a separate file labeled 'Response to Reviewers'. This file does not need to include responses to formatting updates and technical items listed in the 'Journal Requirements' section below.

* A marked-up copy of your manuscript that highlights changes made to the original version. You should upload this as a separate file labeled 'Revised Manuscript with Track Changes'.

* An unmarked version of your revised paper without tracked changes. You should upload this as a separate file labeled 'Manuscript'.

If you would like to make changes to your financial disclosure, competing interests statement, or data availability statement, please make these updates within the submission form at the time of resubmission. Guidelines for resubmitting your figure files are available below the reviewer comments at the end of this letter.

We look forward to receiving your revised manuscript.

Sarath Chandra Janga, Ph.D

PLOS Computational Biology

PLOS Computational Biology

Additional Editor Comments :

In light of the minor comments raised by two of the reviewers regarding the minor issues and typos as well as providing clarity on benchmarking details, the authors should submit a revised version of the manuscript addressing these comments.

Journal Requirements:

1) Please amend your detailed Financial Disclosure statement. This is published with the article. It must therefore be completed in full sentences and contain the exact wording you wish to be published.

1) State what role the funders took in the study. If the funders had no role in your study, please state: "The funders had no role in study design, data collection and analysis, decision to publish, or preparation of the manuscript.".

2) Please ensure that the Figures Files are uploaded in a correct numerical order in the online submission form.

If the reviewer comments include a recommendation to cite specific previously published works, please review and evaluate these publications to determine whether they are relevant and should be cited. There is no requirement to cite these works unless the editor has indicated otherwise.

Reviewer's Responses to Questions

Reviewer #1: I appreciate the authors’ considerable effort in improving the benchmark and the figures, and I think the authors have resolved most of my concerns.

Regarding my previous comments:

1. I agree with the authors that there is value in using the new database where proteins are clustered using AA words.

2. Thank you for your detailed clarification for the content in figure 2. There are some small typos: In Figure 2.a, “≤5” should be “≥5”, and in Figure 2.c, consider limiting the x-axis to be between 0 and 100%.

3. The benchmark in Figure 3 is clearer and shows that kMermaid is among the best performing tools in terms of sensitivity and coverage in most cases. The authors should specify how “% match” is calculated. Is it the same for all tools? If “% match” is the sensitivity at the cluster level for kMermaid, but at the protein level for the other tools, this might not be a fair comparison.

Some additional typos and minor issues that I spotted:

1. In the “Creating kMermaid’s k-mer frequency cluster model using nested hashing” section, the authors used “for each k-mer k, a map of clusters containing k”, which is confusing as k can both indicate a k-mer and the length of a k-mer. Consider changing it to “for each k-mer w”.

2. In the “Assigning protein maps to reads using the pre-computed k-mer model” section, the author claimed that the score would be the sum of k-mer frequencies for the k-mers in the query sequence, but in the formula, the frequency is summed over $k_i\in C$ (all the k-mers in the cluster C), which is inconsistent.

3. Do the “composite score” and the “confidence score” refer to the same thing?

4. I’m still a bit confused by the description of hyperparameter search: “k=5 was selected as it optimized the performance on truncated reference AA sequences”. It might be better to specify which metric they are optimizing: is it based on cluster purity, or AUROC of the downstream classification task, or something else?

5. “The cluster frequency” is better written as “The frequency of k-mers in the cluster”.

6. “The k-mer frequencies for each cluster C were defined by the count of the k-mer in the cluster C divided by the total number of proteins in the cluster.” Can this k-mer frequency be >1 if this k-mer appear multiple times in the same protein?

7. In Figure 3.c, consider using log scale for the y-axis.

Reviewer #2: This version addresses my previous concerns.

Reviewer #3: Most of the previous issues have been fully addressed. One remaining issue is the argument why Silhouette and Dunn index have not been calculate (the authors claim that it is impossible in the absence of centroids). No, it is not true that the Silhouette or Dunn index require the presence or calculation of centroids.

Have the authors made all data and (if applicable) computational code underlying the findings in their manuscript fully available?

The PLOS Data policy requires authors to make all data and code underlying the findings described in their manuscript fully available without restriction, with rare exception (please refer to the Data Availability Statement in the manuscript PDF file). The data and code should be provided as part of the manuscript or its supporting information, or deposited to a public repository. For example, in addition to summary statistics, the data points behind means, medians and variance measures should be available. If there are restrictions on publicly sharing data or code —e.g. participant privacy or use of data from a third party—those must be specified.

PLOS authors have the option to publish the peer review history of their article ( what does this mean? ). If published, this will include your full peer review and any attached files.

If you choose “no”, your identity will remain anonymous but your review may still be made public.

Do you want your identity to be public for this peer review? For information about this choice, including consent withdrawal, please see our Privacy Policy .

Reviewer #3: Yes: Andreas Henschel

[NOTE: If reviewer comments were submitted as an attachment file, they will be attached to this email and accessible via the submission site. Please log into your account, locate the manuscript record, and check for the action link "View Attachments". If this link does not appear, there are no attachment files.]

While revising your submission, please upload your figure files to the Preflight Analysis and Conversion Engine (PACE) digital diagnostic tool, https://pacev2.apexcovantage.com/ . PACE helps ensure that figures meet PLOS requirements. To use PACE, you must first register as a user. Registration is free. Then, login and navigate to the UPLOAD tab, where you will find detailed instructions on how to use the tool. If you encounter any issues or have any questions when using PACE, please email PLOS at figures@plos.org. Please note that Supporting Information files do not need this step. If there are other versions of figure files still present in your submission file inventory at resubmission, please replace them with the PACE-processed versions.

To enhance the reproducibility of your results, we recommend that authors of applicable studies deposit laboratory protocols in protocols.io, where a protocol can be assigned its own identifier (DOI) such that it can be cited independently in the future. Additionally, PLOS ONE offers an option to publish peer-reviewed clinical study protocols. Read more information on sharing protocols at https://plos.org/protocols?utm_medium=editorial-email&utm_source=authorletters&utm_campaign=protocols


# Author response to Decision Letter 2

Collection date 2025 Sep.

Submitted filename: response_to_reviewers_plos_comp_bio.docx


# Decision Letter 2


### Sarath Chandra Janga


#### Roles

This is an open access article distributed under the terms of the Creative Commons Attribution License , which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.

We are pleased to inform you that your manuscript 'kMermaid: Ultrafast metagenomic read assignment to protein clusters by hashing of amino-acid k-mer frequencies' has been provisionally accepted for publication in PLOS Computational Biology.

Before your manuscript can be formally accepted you will need to complete some formatting changes, which you will receive in a follow up email. A member of our team will be in touch with a set of requests.

Please note that your manuscript will not be scheduled for publication until you have made the required changes, so a swift response is appreciated.

IMPORTANT: The editorial review process is now complete. PLOS will only permit corrections to spelling, formatting or significant scientific errors from this point onwards. Requests for major changes, or any which affect the scientific understanding of your work, will cause delays to the publication date of your manuscript.

Should you, your institution's press office or the journal office choose to press release your paper, you will automatically be opted out of early publication. We ask that you notify us now if you or your institution is planning to press release the article. All press must be co-ordinated with PLOS.

Thank you again for supporting Open Access publishing; we are looking forward to publishing your work in PLOS Computational Biology.

Sarath Chandra Janga, Ph.D

PLOS Computational Biology

PLOS Computational Biology

***********************************************************


# Acceptance letter


### Sarath Chandra Janga


#### Roles

This is an open access article distributed under the terms of the Creative Commons Attribution License , which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.

PCOMPBIOL-D-25-00398R2

k Mermaid: Ultrafast metagenomic read assignment to protein clusters by hashing of amino-acid k -mer frequencies

I am pleased to inform you that your manuscript has been formally accepted for publication in PLOS Computational Biology. Your manuscript is now with our production department and you will be notified of the publication date in due course.

The corresponding author will soon be receiving a typeset proof for review, to ensure errors have not been introduced during production. Please review the PDF proof of your manuscript carefully, as this is the last chance to correct any errors. Please note that major changes, or those which affect the scientific understanding of the work, will likely cause delays to the publication date of your manuscript.

Soon after your final files are uploaded, unless you have opted out, the early version of your manuscript will be published online. The date of the early version will be your article's publication date. The final article will be published to the same URL, and all versions of the paper will be accessible to readers.

You will receive an invoice from PLOS for your publication fee after your manuscript has reached the completed accept phase. If you receive an email requesting payment before acceptance or for any other service, this may be a phishing scheme. Learn how to identify phishing emails and protect your accounts at https://explore.plos.org/phishing .

Thank you again for supporting PLOS Computational Biology and open-access publishing. We are looking forward to publishing your work!

PLOS Computational Biology | Carlyle House, Carlyle Road, Cambridge CB4 3DN | United Kingdom ploscompbiol@plos.org | Phone +44 (0) 1223-442824 | ploscompbiol.org | @PLOSCompBiol

This section collects any data citations, data availability statements, or supplementary materials included in this article.


## Supplementary Materials

(a) Percent correct labels by each method for 3 typical read lengths evaluated. (b) Percent of input reads mapped by each method for 3 typical read lengths evaluated.

(a) Spearman correlation between k Mermaid’s assignment score and the maximum BLASTX percent identity per read for all reverse-translated nucleotide segments (lengths = 125, 150, 200 base pairs) of each unseen RefSeq protein that was mapped by both methods without thresholding. To prevent overplotting, reads were down sampled to 100,000 (40% of total). (b) Histograms showing the k Mermaid score of all reverse-translated nucleotide segments (lengths = 125, 150, 200 base pairs) of each unseen RefSeq protein that was mapped by both kMermaid and BLASTX at > 66.6 percent identity. The dashed lines denote the read length-specific thresholds determined by maintaining a false positive rate < 0.05. (c) The percent of all input reads able to be classified by k Mermaid compared to BLASTX for sequencing from 3 representative colitis samples, chosen randomly. k Mermaid’s optimal scoring threshold was determined by maximizing the percentage of the assignments that agree with BLASTX hits (Sensitivity, dark blue) while retaining a high ratio of assignments that agree with BLASTX to assignments that disagree with BLASTX (Accuracy, light blue). (d) Correlation between the proportion of reads concordant with BLASTX and the mean assignment scores (log-transformed) for all proteins in the cluster. Distributions of these metrics broken down by number of reads mapped to the cluster where clusters in the bottom tertile have the lowest number of mapped reads and clusters in the top tertile contain the highest.

Submitted filename: Reviewers-response.docx

Submitted filename: response_to_reviewers_plos_comp_bio.docx


## Data Availability Statement

Availability and usage kMermaid is freely available as an open-source command line program written in Python that requires a user-provided input file containing query sequences in either fastq or fasta format. The precomputed k-mer frequency model and files containing the protein cluster members and cluster representatives are both accessible and used as internal default parameters in kMermaid. Complete download and installation instructions are found at [GITHUB_REPO_REDACTED] Availability of data and materials All data is used in this work is publicly available. The LOTUS trial paired end sequencing metagenomic reads from ulcerative colitis patients fastq files used for benchmarking are available through SRA: PRJEB50699.

Articles from PLOS Computational Biology are provided here courtesy of PLOS
