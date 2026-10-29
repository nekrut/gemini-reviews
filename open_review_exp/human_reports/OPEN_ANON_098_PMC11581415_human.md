# Decision Letter 0


### Anders Wallqvist


### Daniel A Beard


#### Roles

This is an open access article distributed under the terms of the Creative Commons Attribution License , which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.

Thank you very much for submitting your manuscript "Performance of localization prediction algorithms decreases rapidly with the evolutionary distance to the training set increasing" for consideration at PLOS Computational Biology.

As with all papers reviewed by the journal, your manuscript was reviewed by members of the editorial board and by several independent reviewers. In light of the reviews (below this email), we would like to invite the resubmission of a significantly-revised version that takes into account the reviewers' comments.

We cannot make any decision about publication until we have seen the revised manuscript and your response to the reviewers' comments. Your revised manuscript is also likely to be sent to reviewers for further evaluation.

When you are ready to resubmit, please upload the following:

[1] A letter containing a detailed list of your responses to the review comments and a description of the changes you have made in the manuscript. Please note while forming your response, if your article is accepted, you may have the opportunity to make the peer review history publicly available. The record will include editor decision letters (with reviews) and your responses to reviewer comments. If eligible, we will contact you to opt in or out.

[2] Two versions of the revised manuscript: one with either highlights or tracked changes denoting where the text has been changed; the other a clean version (uploaded as the manuscript file).

Important additional instructions are given below your reviewer comments.

Please prepare and submit your revised manuscript within 60 days. If you anticipate any delay, please let us know the expected resubmission date by replying to this email. Please note that revised manuscripts received after the 60-day due date may require evaluation and peer review similar to newly submitted manuscripts.

Thank you again for your submission. We hope that our editorial process has been constructive so far, and we welcome your feedback at any time. Please don't hesitate to contact us if you have any questions or comments.

PLOS Computational Biology

PLOS Computational Biology

***********************

Reviewer's Responses to Questions

Comments to the Authors:

Please note here if the review is uploaded as an attachment.

Reviewer #1: In this manuscript, the authors reported their benchmark study on the prediction accuracy of three widely used algorithms for localization into plant (or photosynthetic eukaryotes’) plastids and mitochondria using experimentally determined proteome data supplemented by homology-based data. Their results show that the performance of these tools is not practically reliable and that the accuracy becomes even worse in plant species with more evolutionary distances from (well-studied) eudicots or angiosperms. Overall, their messages are clear; this work will be an important warning for end users and encourage the developer of prediction algorithms to address this issue. But the following points should be improved before its acceptance:

1. Although the claim in the title is likely correct, they should claim only what they showed in this study.

2. The authors seem to presume that all nuclear-encoded plastid/mitochondrial proteins carry N-terminal targeting sequences. However, this assumption has not been proven (if I understand correctly). If this assumption is incorrect, we cannot expect TargetP to be 100% accurate because it only predicts the existence/absence of N-terminal signals. This point should be noted clearly.

3. More importantly, their main message, “Performance of localization prediction algorithms decreases rapidly with the evolutionary distance …,” seems to imply the existence of a general/ideal predictor applicable to the sequences of any species. However, as the authors point out, the translocation complexes can vary between species. The efficiency of recognition of a typical signal in one species can be greatly different in another species. Therefore, the only reasonable solution seems to prepare specific predictor for each evolutionary group of species. Using machine learning techniques, such a remedy would be rather trivial (if there is enough data size).

4. In this sense, the authors should show how different the N-terminal signals are between different evolutionary groups (in the case of mitochondria, animal sequences should also be compared) (like Fig.4c & d).

5. Although this does not matter for users, Wolf PSORT was released 12 years before TargetP v.2.0. Obviously, there was not much sample data for various species at that time. So, at least from the side of algorithm developers, the comparison ignoring this point does not make much sense.

6. The current explanation of the Localizer algorithm should be improved. The first version of PSORT also could treat eukaryotic sequences (PMD 1478671).

Reviewer #2: The study aims to clarify the prediction error of plastid and mitochondrion proteomes across the plant kingdom with evolutionary distance from the training standard and speculate ways to improve prediction accuracy/precision. It is a well written manuscript. While this is an ongoing issue of high relevance the novelty of the study is limited and concrete steps for improvements are not given.

Overall, the claim that the proteomes predicted and experimental vary due to errors and differences in plant physiology across evolution are known. Secondly, the prediction algorithms are mostly trained on e.g. Arabidopsis and will work best on this species as there has been the most data to train. So this is not a novel insight.

Abstract is not clearly stating that the study is limited to plastid and mitochondria and which 4 species were used to assess the predictors. The authors make claims using only Arabidopsis, Chlamydomonas, Zea mays, P patens to choose the best predictor. There are a lot more experimental data out there so the authors could do a more substantial analysis across several individuals computationally and then also using experimental data sets. However, the authors need to compare their assessment of 3 predictors with other assessments. For example, the comparison of >10 predictors against multiple experimental data sets and classifiers in Arabidopsis (e.g. SUBAcon and/or the SUBA4 (Bioinformatics. 2014 Dec 1;30(23):3356-64. doi: 10.1093/bioinformatics/btu550. Epub 2014 Aug 22.). The latter had a full assessment of ~20 predictors including TargetP and WolfPSORT. This paper also found a TargetP to be one of the strongest predictors for plastid using a far more rigid methodology for comparing to experimental data alone. The authors may also need to consider Predotar (Proteomics. 2004 Jun;4(6):1581-90. doi: 10.1002/pmic.200300776.) which is still a strong predictor for mitochondria using NTS and the training set may be more widespread perhaps.

Secondly, the cropPAL dataset mentioned by the authors has 12 species including experimental data and was used to describe the divergence of the subcellular proteomes to some degree across 6 monocots and 6 dicots from different branches of the plant kingdom ( Plant J. 2020 Nov;104(3):812-827. doi: 10.1111/tpj.14961. Epub 2020 Sep 16). Can the authors discuss this and emphasis how their claim is different or more substantial?

Also, the experimental sets used to verify predictors need to be described in more detail. What were the QC parameters in this data set. The authors assume that these are correct and maybe complete. Experimental data sets are also error prone to contamination and missing proteins. If using MS data, this method tends to detect similar protein families across species, namely prevalent proteins and those that form detectable peptides. Hence all proteomes generated by MS tend to plateau towards the same group of but always miss the rest of proteins. In that light, the authors state a large number of false positives but to what degree is this correct? The experimental plastid/mitochondria datasets are much smaller than expected so a lot of the false positives may actually be correct? Another point not discussed by the authors is how experimental discrepancies are being dealt with?

Most literature expect plastid and mitochondrion proteomes to be around 10-15%. The authors mention 5%. The evidence for this needs to be described.

The evolutionary approach is very interesting and more convincing and as mentioned earlier I would not readily assume that the differences seen in the prediction are errors. Can the authors clarify that the prediction error definition is? Is it prediction compared to experimental? If so, what about missing experimental proteins that are in the plastid/mitochondrion?

Proteins are known to be conserved as well as in distinctly different organelles amongst different species. The authors show the training set for TargetP per species but what is the distribution of the training standard compared to the test data sets of 147 species? Is it comparable or is the training standard skewed differently to the test? This needs to be clearer in the text.

There are several individual predictors and ensemble predictors/classifiers that take evolution into account. These have not been considered or discussed (e.g. BaCelLo - Bioinformatics. 2006 Jul 15;22(14):e408-16. doi: 10.1093/bioinformatics/btl222.). How do more balanced predictors perform?

The results suggest also that apart from distance there are other relationships limited to e.g. clades etc. Which is interesting and may warrant more investigation as this has not been done systematically before. The authors suggest an algorithm with better adjustment to evolutionary distance but do not propose how this would work.

Dual targeted proteins: This has been looked at a few times (e.g. in the cropPAL data set and in Arabidopsis versus Zea mays or Oryza and other species to some degree) and should be discussed here. In general, most predictors struggle predicting dual targeted proteins even if training on the species they are predicting. This is a long-standing issue and yet has not been well addressed in this study! The authors need to discuss the literature (e.g. New Phytol. 2009;183(1):224-236. doi: 10.1111/j.1469-8137.2009.02832.x.)

Choosing protein families is an interesting approach as such and it leads to the conundrum to include families with proteins only existent in the plastid or in the mitochondria versus families with proteins that have members sent to different locations. How are these considered? This may have introduced a lot of missed proteins that are not really missed.

Pan proteome and genome training would be good idea but how to is not described.

Figures need stand-alone legends. Please review each and add missing explanations particularly the supplementary.

Reviewer #3: The paper titled "Performance of localization prediction algorithms decreases rapidly with the evolutionary distance to the training set increasing" presents a very interesting and systematic evaluation to plant organelle proteomes. The study took a big collection of known plant organelle proteome data as a basis to evaluate three major computational prediction tools. I think this is a good study. I also personally favor its conclusion. I have only two minor comments, as follows:

1 As this is computational biology, I think the authors should present the major mathematical formulations in the main text, not only in supps.

2 I think the code and datasets for reproducing the study should also be deposited publicly. Zenodo and Github are recommended.

Have the authors made all data and (if applicable) computational code underlying the findings in their manuscript fully available?

The PLOS Data policy requires authors to make all data and code underlying the findings described in their manuscript fully available without restriction, with rare exception (please refer to the Data Availability Statement in the manuscript PDF file). The data and code should be provided as part of the manuscript or its supporting information, or deposited to a public repository. For example, in addition to summary statistics, the data points behind means, medians and variance measures should be available. If there are restrictions on publicly sharing data or code —e.g. participant privacy or use of data from a third party—those must be specified.

Reviewer #3: No: Please deposit codes publicly, in GitHub.

PLOS authors have the option to publish the peer review history of their article ( what does this mean? ). If published, this will include your full peer review and any attached files.

If you choose “no”, your identity will remain anonymous but your review may still be made public.

Do you want your identity to be public for this peer review? For information about this choice, including consent withdrawal, please see our Privacy Policy .

Reviewer #1: Yes: Kenta Nakai

While revising your submission, please upload your figure files to the Preflight Analysis and Conversion Engine (PACE) digital diagnostic tool, https://pacev2.apexcovantage.com . PACE helps ensure that figures meet PLOS requirements. To use PACE, you must first register as a user. Then, login and navigate to the UPLOAD tab, where you will find detailed instructions on how to use the tool. If you encounter any issues or have any questions when using PACE, please email us at figures@plos.org .

Please note that, as a condition of publication, PLOS' data policy requires that you make available all data used to draw the conclusions outlined in your manuscript. Data must be deposited in an appropriate repository, included within the body of the manuscript, or uploaded as supporting information. This includes all numerical values that were used to generate graphs, histograms etc.. For an example in PLOS Biology see here: http://www.plosbiology.org/article/info%3Adoi%2F10.1371%2Fjournal.pbio.1001908#s5 .

To enhance the reproducibility of your results, we recommend that you deposit your laboratory protocols in protocols.io, where a protocol can be assigned its own identifier (DOI) such that it can be cited independently in the future. Additionally, PLOS ONE offers an option to publish peer-reviewed clinical study protocols. Read more information on sharing protocols at https://plos.org/protocols?utm_medium=editorial-email&utm_source=authorletters&utm_campaign=protocols


# Author response to Decision Letter 0

Collection date 2024 Nov.

Submitted filename: Response to Reviewers.pdf


# Decision Letter 1


### Anders Wallqvist


### Daniel A Beard


#### Roles

This is an open access article distributed under the terms of the Creative Commons Attribution License , which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.

Thank you very much for submitting your manuscript "Reliability of plastid and mitochondrial localisation prediction declines rapidly with the evolutionary distance to the training set increasing" for consideration at PLOS Computational Biology.

As with all papers reviewed by the journal, your manuscript was reviewed by members of the editorial board and by several independent reviewers. In light of the reviews (below this email), we would like to invite the resubmission of a significantly-revised version that takes into account the reviewers' comments.

You will note that Reviewer 3, in particular, has important outstanding concerns that need to be considered and addressed in a revised paper.

We cannot make any decision about publication until we have seen the revised manuscript and your response to the reviewers' comments. Your revised manuscript is also likely to be sent to reviewers for further evaluation.

When you are ready to resubmit, please upload the following:

[1] A letter containing a detailed list of your responses to the review comments and a description of the changes you have made in the manuscript. Please note while forming your response, if your article is accepted, you may have the opportunity to make the peer review history publicly available. The record will include editor decision letters (with reviews) and your responses to reviewer comments. If eligible, we will contact you to opt in or out.

[2] Two versions of the revised manuscript: one with either highlights or tracked changes denoting where the text has been changed; the other a clean version (uploaded as the manuscript file).

Important additional instructions are given below your reviewer comments.

Please prepare and submit your revised manuscript within 60 days. If you anticipate any delay, please let us know the expected resubmission date by replying to this email. Please note that revised manuscripts received after the 60-day due date may require evaluation and peer review similar to newly submitted manuscripts.

Thank you again for your submission. We hope that our editorial process has been constructive so far, and we welcome your feedback at any time. Please don't hesitate to contact us if you have any questions or comments.

PLOS Computational Biology

PLOS Computational Biology

***********************

Reviewer's Responses to Questions

Comments to the Authors:

Please note here if the review is uploaded as an attachment.

Reviewer #1: Since I confirmed that the authors' responses to my points are reasonable, I now recommend its acceptance as is.

Reviewer #2: The authors have put substantial work into improving the manuscript. It is now much clearer that this study focusses on plastid and mitochondria across cornerstones of the plant kingdom.

I agree that many prediction algorithms are not accessible 5 or more years after publication, highlighting a serious issue in our system.

The authors also adjusted and increased their conclusions substantially to reflect the data limitations and findings.

Reviewer #3: I do not think the authors face my questions and concerns with a consolidated scientific response. I believe none of my concerns is addressed. In particular, no reproducible instruction is provided in zenodo. The codes and XLS files are thus useless. Therefore, I am sorry that I suggest to reject this paper because the background information (data/codes/instructions for reproducing) is not fully published.

Have the authors made all data and (if applicable) computational code underlying the findings in their manuscript fully available?

The PLOS Data policy requires authors to make all data and code underlying the findings described in their manuscript fully available without restriction, with rare exception (please refer to the Data Availability Statement in the manuscript PDF file). The data and code should be provided as part of the manuscript or its supporting information, or deposited to a public repository. For example, in addition to summary statistics, the data points behind means, medians and variance measures should be available. If there are restrictions on publicly sharing data or code —e.g. participant privacy or use of data from a third party—those must be specified.

Reviewer #3: No: No reproducible instruction is provided based only on public information

PLOS authors have the option to publish the peer review history of their article ( what does this mean? ). If published, this will include your full peer review and any attached files.

If you choose “no”, your identity will remain anonymous but your review may still be made public.

Do you want your identity to be public for this peer review? For information about this choice, including consent withdrawal, please see our Privacy Policy .

Reviewer #1: Yes: Kenta Nakai

While revising your submission, please upload your figure files to the Preflight Analysis and Conversion Engine (PACE) digital diagnostic tool, https://pacev2.apexcovantage.com . PACE helps ensure that figures meet PLOS requirements. To use PACE, you must first register as a user. Then, login and navigate to the UPLOAD tab, where you will find detailed instructions on how to use the tool. If you encounter any issues or have any questions when using PACE, please email us at figures@plos.org .

Please note that, as a condition of publication, PLOS' data policy requires that you make available all data used to draw the conclusions outlined in your manuscript. Data must be deposited in an appropriate repository, included within the body of the manuscript, or uploaded as supporting information. This includes all numerical values that were used to generate graphs, histograms etc.. For an example in PLOS Biology see here: http://www.plosbiology.org/article/info%3Adoi%2F10.1371%2Fjournal.pbio.1001908#s5 .

To enhance the reproducibility of your results, we recommend that you deposit your laboratory protocols in protocols.io, where a protocol can be assigned its own identifier (DOI) such that it can be cited independently in the future. Additionally, PLOS ONE offers an option to publish peer-reviewed clinical study protocols. Read more information on sharing protocols at https://plos.org/protocols?utm_medium=editorial-email&utm_source=authorletters&utm_campaign=protocols


# Author response to Decision Letter 1

Collection date 2024 Nov.

Submitted filename: Response to Reviewers_Rev2.docx


# Decision Letter 2


### Anders Wallqvist


### Daniel A Beard


#### Roles

This is an open access article distributed under the terms of the Creative Commons Attribution License , which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.

We are pleased to inform you that your manuscript 'Reliability of plastid and mitochondrial localisation prediction declines rapidly with the evolutionary distance to the training set increasing' has been provisionally accepted for publication in PLOS Computational Biology.

Before your manuscript can be formally accepted you will need to complete some formatting changes, which you will receive in a follow up email. A member of our team will be in touch with a set of requests.

Please note that your manuscript will not be scheduled for publication until you have made the required changes, so a swift response is appreciated.

IMPORTANT: The editorial review process is now complete. PLOS will only permit corrections to spelling, formatting or significant scientific errors from this point onwards. Requests for major changes, or any which affect the scientific understanding of your work, will cause delays to the publication date of your manuscript.

Should you, your institution's press office or the journal office choose to press release your paper, you will automatically be opted out of early publication. We ask that you notify us now if you or your institution is planning to press release the article. All press must be co-ordinated with PLOS.

Thank you again for supporting Open Access publishing; we are looking forward to publishing your work in PLOS Computational Biology.

PLOS Computational Biology

PLOS Computational Biology

***********************************************************


# Acceptance letter


### Anders Wallqvist


### Daniel A Beard


#### Roles

This is an open access article distributed under the terms of the Creative Commons Attribution License , which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.

PCOMPBIOL-D-24-00460R2

Reliability of plastid and mitochondrial localisation prediction declines rapidly with the evolutionary distance to the training set increasing

I am pleased to inform you that your manuscript has been formally accepted for publication in PLOS Computational Biology. Your manuscript is now with our production department and you will be notified of the publication date in due course.

The corresponding author will soon be receiving a typeset proof for review, to ensure errors have not been introduced during production. Please review the PDF proof of your manuscript carefully, as this is the last chance to correct any errors. Please note that major changes, or those which affect the scientific understanding of the work, will likely cause delays to the publication date of your manuscript.

Soon after your final files are uploaded, unless you have opted out, the early version of your manuscript will be published online. The date of the early version will be your article's publication date. The final article will be published to the same URL, and all versions of the paper will be accessible to readers.

Thank you again for supporting PLOS Computational Biology and open-access publishing. We are looking forward to publishing your work!

PLOS Computational Biology | Carlyle House, Carlyle Road, Cambridge CB4 3DN | United Kingdom ploscompbiol@plos.org | Phone +44 (0) 1223-442824 | ploscompbiol.org | @PLOSCompBiol

This section collects any data citations, data availability statements, or supplementary materials included in this article.


## Supplementary Materials

Proteomes of each species from KEGG (Kyoto Encyclopedia of Genes and Genomes) were used as an input for the three algorithm to get proteins predicted as plastid and mitochondria. Their experimental proteomes were taken from organelle proteome databases and literature (see methods ). Predicted and experimentally verified plastid (on the left) and mitochondrial (on the right) proteins were plotted as a percentage of all proteins encoded by a given species.

The number of experimentally verified plastid proteins that got predicted as mitochondrial proteins by the three algorithms (on the left) and experimentally verified mitochondrial proteins that got predicted as plastid proteins (on the right).

All proteins from the four photosynthetic eukaryotes and sorting of protein clusters into plastid (on the left) and mitochondrial family (on the right). Each circle is a protein from a species. In the first step (shown on top), source protein sequences from available species were clustered into protein families (shown at the bottom). If a protein family consisted of an experimentally verified plastid protein (in green, on the left) or a mitochondrial protein (in orange, on the right), the protein family was sorted as a plastid or mitochondrial protein family.

Comparison of chloroplast+thylakoid proteins predicted by TargetP2.0 with experimentally localised proteins across species. Each Venn diagram represent data similar to that of Fig 1A , expect now supplemented with ‘thylakoid’ predicted proteins under the category ‘plastid’. The Ven diagrams show an overlap between predicted (left circles) and experimentally verified organelle proteomes (right circles, grey). The underscored numbers in the bottom corners show the total number of predicted (bottom left) and experimentally confirmed proteins (bottom right). The numbers of proteins that overlap (true positives) are provided in the top right corner in bold, while the numbers of non-overlapping ones (false positives) are shown next to each circle. See also the key for the Venn diagrams on the bottom right.

The targetP2.0 training proteins were downloaded from the original publication and based on their swissprot IDs, their full taxonomy was recovered and number of training proteins per species is plotted here for plastid (a) and mitochondria (b) (with species color coded as per their taxonomy, taxonomy class ‘others’ include: protozoa, insect, nematode, fish, amphibian, amoebozoa, dinoflagellate).

Experimentally verified Physcomitrium organelle proteins that were missed by each algorithm (i.e. the false negative) were used as queries to BaCeLlo to check whether it can sort them correctly. BaCeLlo sorted ca. 50% of them to mitochondria or cytosol, regardless of their verified locations, showing overall affinity for mitochondrial sorting and a lack of reignition for targeting sequence.

Dually targeted proteins predicted in Arabidopsis by the Ambiguous Targeting Predictor (ATP) compared with mass-spec confirmed dual targeted proteins from Arabidopsis shows that ATP missed more than half of Arabidopsis dual targeted proteins and predicted ten times more proteins to be dually targeted.

cropPAL incorporates a dozen algorithms of which if the majority of algorithm sorts a protein to plastid and mitochondria both, we consider it to be predicted dual targeted. For a given protein, if at least one experimental study experimentally showed plastid and mitochondrial localization, we consider it to be experimentally verified dual targeted protein. If more than one study converge onto plastid and mitochondria, cropPAL labels it as ‘experimental consensus’. Overlap of the three categories (predicted, experimentally verified and experimental consensus) is shown for six species, and they generally underscore overprediction of dual targeting.

Submitted filename: Response to Reviewers.pdf

Submitted filename: Response to Reviewers_Rev2.docx


## Data Availability Statement

Supplementary figures are available in the supplementary information file. Additional supplementary data, in-house scripts and source data for the main and supplementary figures are available on Zenedo: https://zenodo.org/records/13924211 .

Articles from PLOS Computational Biology are provided here courtesy of PLOS
