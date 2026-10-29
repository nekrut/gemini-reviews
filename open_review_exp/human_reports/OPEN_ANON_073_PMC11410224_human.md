# Decision Letter 0


### Thomas Leitner


### Samuel V Scarpino


#### Roles

This is an open access article distributed under the terms of the Creative Commons Attribution License , which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.

Thank you very much for submitting your manuscript "Fitness models provide accurate short-term forecasts of SARS-CoV-2 variant frequency" for consideration at PLOS Computational Biology.

As with all papers reviewed by the journal, your manuscript was reviewed by members of the editorial board and by several independent reviewers. In light of the reviews (below this email), we would like to invite the resubmission of a significantly-revised version that takes into account the reviewers' comments.

I agree with the reviewers that this paper represents a potentially impactful contribution related to SARS-CoV-2 variant fitness estimation, which is key for accurate risk assessment and time series forecasting. However, I also agree strongly with R1 that the authors need to account for the unstable nature of lineage assignment as new variants emerge. I'm less familiar with the operational specifics of nextstrain's assignment, but with pangolin is should be possible to use the model version in use during each variant emergence period. I also agree with both reviewers that more effort is needed on uncertainty quantification and on measuring performance in geographic locations with lower genome sampling effort. I hope that the authors pay careful attention to the detailed reviewer comments, as following them will lead to a meaningful improvement in the manuscript.

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

I agree with the reviewers that this paper represents a potentially impactful contribution related to SARS-CoV-2 variant fitness estimation, which is key for accurate risk assessment and time series forecasting. However, I also agree strongly with R1 that the authors need to account for the unstable nature of lineage assignment as new variants emerge. I'm less familiar with the operational specifics of nextstrain's assignment, but with pangolin is should be possible to use the model version in use during each variant emergence period. I also agree with both reviewers that more effort is needed on uncertainty quantification and on measuring performance in geographic locations with lower genome sampling effort. I hope that the authors pay careful attention to the detailed reviewer comments, as following them will lead to a meaningful improvement in the manuscript.

Reviewer's Responses to Questions

Comments to the Authors:

Please note here if the review is uploaded as an attachment.

Reviewer #1: Reivew is uploaded as an attachment

Reviewer #2: It was a joy to read this ms. The authors propose a framework to evaluate real-time forecasts of variant frequencies. They use the evolution of SARS-CoV-2 in 2022 as a case study.

They use their framework to compare models across different countries on a range of genomic surveillance intensity.

Perhaps what I was most excited about was the use of it to estimate minimum number of sequences needed per week is sufficient for accurate short-term forecasts. This is an incredible relevant question not just from a methodological standpoint but of capacity building and public health importance.

I have a few minor suggestions:

I suggest you use countries with much lower genomic surveillance effort as well, as while there are some differences between those countries they are all on higher end of effort. Meaning that the issues especially at the emergence of a new variant will be easier to miss.

It wasn’t clear why for Australia model’s performance was slightly different. Is it due to sampling efforts or it spurious? I suggest the authors explain this a little in more detail.

Not surprisingly, the authors found that variability in forecast errors is partially driven by data limitations. And thus, as expected, the authors focus on hypothesis that error is largest for emerging variants that present a small window of time to observe dynamics and where sequence count data is often rare. So, while their testing is sound I suggest two additional steps:

1. This would no doubt be exacerbated in countries with low effort or very pulsed effort. It would be great to see that explored. So picking two or three countries with constantly low effort and or pulsed effort will be very useful

2. To this regard, I would suggest to the authors to take their framework to evaluate models that are specifically pooling country data, such as https://www.medrxiv.org/content/10.1101/2023.01.02.23284123v4.full (cited in the ms) which address a lot of the issues related with backfilling and the under/ over estimation at emergence, heterogenous reporting. These pooled models while MLR, should be evaluated separately from single country models, for all the reasons and issues the authors state they are exploring.

While I agree with the statements that MLR models, “do not account for future mutations and can only project forwards from circulating viral diversity. This intrinsically limits the effective forecasting horizon achievable by these models.” It seems to me that the discussion should center in the purpose of the models to begin with. So, for a more balanced discussion, I would suggest the authors to add perhaps a paragraph in the discussion on the role of adding mechanism or background information (vaccine, previous waves, to understand immunity profiles of populations) onto these models, if they are to be useful beyond the nowcast, as it will no doubt affect internal dynamics and competition between variants that in turn affects sustained growth and displacement of other less fit variants.

Have the authors made all data and (if applicable) computational code underlying the findings in their manuscript fully available?

The PLOS Data policy requires authors to make all data and code underlying the findings described in their manuscript fully available without restriction, with rare exception (please refer to the Data Availability Statement in the manuscript PDF file). The data and code should be provided as part of the manuscript or its supporting information, or deposited to a public repository. For example, in addition to summary statistics, the data points behind means, medians and variance measures should be available. If there are restrictions on publicly sharing data or code —e.g. participant privacy or use of data from a third party—those must be specified.

PLOS authors have the option to publish the peer review history of their article ( what does this mean? ). If published, this will include your full peer review and any attached files.

If you choose “no”, your identity will remain anonymous but your review may still be made public.

Do you want your identity to be public for this peer review? For information about this choice, including consent withdrawal, please see our Privacy Policy .

While revising your submission, please upload your figure files to the Preflight Analysis and Conversion Engine (PACE) digital diagnostic tool, https://pacev2.apexcovantage.com . PACE helps ensure that figures meet PLOS requirements. To use PACE, you must first register as a user. Then, login and navigate to the UPLOAD tab, where you will find detailed instructions on how to use the tool. If you encounter any issues or have any questions when using PACE, please email us at figures@plos.org .

Please note that, as a condition of publication, PLOS' data policy requires that you make available all data used to draw the conclusions outlined in your manuscript. Data must be deposited in an appropriate repository, included within the body of the manuscript, or uploaded as supporting information. This includes all numerical values that were used to generate graphs, histograms etc.. For an example in PLOS Biology see here: http://www.plosbiology.org/article/info%3Adoi%2F10.1371%2Fjournal.pbio.1001908#s5 .

To enhance the reproducibility of your results, we recommend that you deposit your laboratory protocols in protocols.io, where a protocol can be assigned its own identifier (DOI) such that it can be cited independently in the future. Additionally, PLOS ONE offers an option to publish peer-reviewed clinical study protocols. Read more information on sharing protocols at https://plos.org/protocols?utm_medium=editorial-email&utm_source=authorletters&utm_campaign=protocols

Submitted filename: PCOMPBIOL-D-23-01974 Review.docx


# Author response to Decision Letter 0

Collection date 2024 Sep.

Submitted filename: Manuscript Review Response.pdf


# Decision Letter 1


### Thomas Leitner


### Samuel V Scarpino


#### Roles

This is an open access article distributed under the terms of the Creative Commons Attribution License , which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.

Thank you very much for submitting your manuscript "Fitness models provide accurate short-term forecasts of SARS-CoV-2 variant frequency" for consideration at PLOS Computational Biology. As with all papers reviewed by the journal, your manuscript was reviewed by members of the editorial board and by several independent reviewers. The reviewers appreciated the attention to an important topic. Based on the reviews, we are likely to accept this manuscript for publication, providing that you modify the manuscript according to the review recommendations.

Please prepare and submit your revised manuscript within 30 days. If you anticipate any delay, please let us know the expected resubmission date by replying to this email.

When you are ready to resubmit, please upload the following:

[1] A letter containing a detailed list of your responses to all review comments, and a description of the changes you have made in the manuscript. Please note while forming your response, if your article is accepted, you may have the opportunity to make the peer review history publicly available. The record will include editor decision letters (with reviews) and your responses to reviewer comments. If eligible, we will contact you to opt in or out

[2] Two versions of the revised manuscript: one with either highlights or tracked changes denoting where the text has been changed; the other a clean version (uploaded as the manuscript file).

Important additional instructions are given below your reviewer comments.

Thank you again for your submission to our journal. We hope that our editorial process has been constructive so far, and we welcome your feedback at any time. Please don't hesitate to contact us if you have any questions or comments.

PLOS Computational Biology

PLOS Computational Biology

***********************

A link appears below if there are any accompanying review attachments. If you believe any reviews to be missing, please contact ploscompbiol@plos.org immediately:

Reviewer's Responses to Questions

Comments to the Authors:

Please note here if the review is uploaded as an attachment.

Reviewer #1: Overall, the manuscript is of great importance to public health and specifically estimation and evaluation of variant dynamics. The authors made significant improvements to the manuscript in the course of their revisions, and I would highly recommend this article for publication in PLOS Computational Biology, contingent on a few minor revisions/suggestions:

- Suggested edit in methods titled “Comparing forecasts using retrospective clade designations and real-time designations” -> “The main analysis discussed in…. accessed on a particular date” (date instead of what is written now which is data)

- Suggest clarifying terminology, when referring to Nextclade version to indicate that this means the clade designation model. It might be confusing to a reader who is already thinking about time-stamped versions of the data to distinguish between the two, but this distinction is critical to understanding the difference between the real-time and retrospective variant calling.

- I would suggest calling a variant by its pangolin with Nextclade beside it throughout e.g. BQ.1 (Omicron 22E)

- I would clarify in the description of the downsampling, that we might expect that when sequencing declines overall, it would also decline in recent weeks, instead of the recent weeks being the upper limit, and so the analysis may not reflect the real-time impact of reducing sequencing quantity unless the speed of sequencing is prioritized.

- I’m not sure why the hierarchical MLR results are not included in Figures 2 and 3, and instead are an add on in Figure 7. The manuscript might read more smoothly if the hierarchical MLR is presented alongside the other models including the single country MLR. Right now it appears like a secondary analysis

- I would suggest that the authors describe in further detail why they think the coverage is so low in high sequencing countries? Is this because the model is underdispersed/over confident? If so, could they offer any possible solutions to this problem in the discussion (e.g. a different observation model, models accounting for heterogeneity in facilities, etc.)

- Figures S10-17 are a bit confusing, which lines represent the fit to the real time next clade and which lines are fit to the current nextclade? As presented, there appears to only be one model fit, it would be helpful to present the model fit to both input data sets to compare accuracy to both the real time and retrospective assignments. In general, like these figures though because they make clear some examples of the forecasts versus the later observations.

Reviewer #3: In the article: "Fitness models provide accurate short-term forecasts of SARS-CoV-2 variant frequency" the authors provide a nice demonstration of the performance of different variant forecasting models for SARS-CoV-2 variants and provide estimates for the sample size necessary for countries surveillance programs. The article is well written and covers an important topic, particularly as the US is considering a new variant forecasting competition. Based on their revisions to reviewer feedback I believe this article should be accepted for publication, but I have a single suggestion the authors should consider adding.

Suggestion: The authors provide a sample size that they feel would be sufficient to have reasonable data for stable variant forecasting based on a nice downsampling analysis. One issue is that many countries are not currently reporting 1,000 cases a week, some not even 200! It would be useful if the authors could try and speak to these countries regarding the genomic sequence sample sizes necessary. My feeling is that it should be reasonable to carry out nowcast/forecasts in a scenario where there are 200 reported cases a week and all of them are sequenced, though I think it's an interesting question. It would be great if the authors could analyze the fraction of reported cases being sequenced in their sample size analysis (maybe some simple back-of-the-envelope calculations could be made) to see if they can provide any guidance in these scenarios where there are smaller reported case counts.

Have the authors made all data and (if applicable) computational code underlying the findings in their manuscript fully available?

The PLOS Data policy requires authors to make all data and code underlying the findings described in their manuscript fully available without restriction, with rare exception (please refer to the Data Availability Statement in the manuscript PDF file). The data and code should be provided as part of the manuscript or its supporting information, or deposited to a public repository. For example, in addition to summary statistics, the data points behind means, medians and variance measures should be available. If there are restrictions on publicly sharing data or code —e.g. participant privacy or use of data from a third party—those must be specified.

PLOS authors have the option to publish the peer review history of their article ( what does this mean? ). If published, this will include your full peer review and any attached files.

If you choose “no”, your identity will remain anonymous but your review may still be made public.

Do you want your identity to be public for this peer review? For information about this choice, including consent withdrawal, please see our Privacy Policy .

While revising your submission, please upload your figure files to the Preflight Analysis and Conversion Engine (PACE) digital diagnostic tool, https://pacev2.apexcovantage.com . PACE helps ensure that figures meet PLOS requirements. To use PACE, you must first register as a user. Then, login and navigate to the UPLOAD tab, where you will find detailed instructions on how to use the tool. If you encounter any issues or have any questions when using PACE, please email us at figures@plos.org .

Please note that, as a condition of publication, PLOS' data policy requires that you make available all data used to draw the conclusions outlined in your manuscript. Data must be deposited in an appropriate repository, included within the body of the manuscript, or uploaded as supporting information. This includes all numerical values that were used to generate graphs, histograms etc.. For an example in PLOS Biology see here: http://www.plosbiology.org/article/info%3Adoi%2F10.1371%2Fjournal.pbio.1001908#s5 .

To enhance the reproducibility of your results, we recommend that you deposit your laboratory protocols in protocols.io, where a protocol can be assigned its own identifier (DOI) such that it can be cited independently in the future. Additionally, PLOS ONE offers an option to publish peer-reviewed clinical study protocols. Read more information on sharing protocols at https://plos.org/protocols?utm_medium=editorial-email&utm_source=authorletters&utm_campaign=protocols

Review your reference list to ensure that it is complete and correct. If you have cited papers that have been retracted, please include the rationale for doing so in the manuscript text, or remove these references and replace them with relevant current references. Any changes to the reference list should be mentioned in the rebuttal letter that accompanies your revised manuscript.

If you need to cite a retracted article, indicate the article’s retracted status in the References list and also include a citation and full reference for the retraction notice.


# Author response to Decision Letter 1

Collection date 2024 Sep.

Submitted filename: #ncov-forecasting-fit reviewer response round 2.pdf


# Decision Letter 2


### Thomas Leitner


### Samuel V Scarpino


#### Roles

This is an open access article distributed under the terms of the Creative Commons Attribution License , which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.

We are pleased to inform you that your manuscript 'Fitness models provide accurate short-term forecasts of SARS-CoV-2 variant frequency' has been provisionally accepted for publication in PLOS Computational Biology.

Before your manuscript can be formally accepted you will need to complete some formatting changes, which you will receive in a follow up email. A member of our team will be in touch with a set of requests.

Please note that your manuscript will not be scheduled for publication until you have made the required changes, so a swift response is appreciated.

IMPORTANT: The editorial review process is now complete. PLOS will only permit corrections to spelling, formatting or significant scientific errors from this point onwards. Requests for major changes, or any which affect the scientific understanding of your work, will cause delays to the publication date of your manuscript.

Should you, your institution's press office or the journal office choose to press release your paper, you will automatically be opted out of early publication. We ask that you notify us now if you or your institution is planning to press release the article. All press must be co-ordinated with PLOS.

Thank you again for supporting Open Access publishing; we are looking forward to publishing your work in PLOS Computational Biology.

PLOS Computational Biology

PLOS Computational Biology

***********************************************************


# Acceptance letter


### Thomas Leitner


### Samuel V Scarpino


#### Roles

This is an open access article distributed under the terms of the Creative Commons Attribution License , which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.

PCOMPBIOL-D-23-01974R2

Fitness models provide accurate short-term forecasts of SARS-CoV-2 variant frequency

I am pleased to inform you that your manuscript has been formally accepted for publication in PLOS Computational Biology. Your manuscript is now with our production department and you will be notified of the publication date in due course.

The corresponding author will soon be receiving a typeset proof for review, to ensure errors have not been introduced during production. Please review the PDF proof of your manuscript carefully, as this is the last chance to correct any errors. Please note that major changes, or those which affect the scientific understanding of the work, will likely cause delays to the publication date of your manuscript.

Soon after your final files are uploaded, unless you have opted out, the early version of your manuscript will be published online. The date of the early version will be your article's publication date. The final article will be published to the same URL, and all versions of the paper will be accessible to readers.

Thank you again for supporting PLOS Computational Biology and open-access publishing. We are looking forward to publishing your work!

PLOS Computational Biology | Carlyle House, Carlyle Road, Cambridge CB4 3DN | United Kingdom ploscompbiol@plos.org | Phone +44 (0) 1223-442824 | ploscompbiol.org | @PLOSCompBiol

This section collects any data citations, data availability statements, or supplementary materials included in this article.


## Supplementary Materials

(A) Variant sequence counts categorized by Nextstrain clade at 4 different analysis dates.

(A) +30 day frequency forecasts for variants in bimonthly intervals using the MLR model for Australia. Each forecast trajectory is shown as a different colored line. Retrospective smoothed frequency is shown as a thick black line.

(A) +30 day frequency forecasts for variants in bimonthly intervals using the MLR model for Brazil. Each forecast trajectory is shown as a different colored line. Retrospective smoothed frequency is shown as a thick black line.

(A) +30 day frequency forecasts for variants in bimonthly intervals using the MLR model for South Africa. Each forecast trajectory is shown as a different colored line. Retrospective smoothed frequency is shown as a thick black line.

(A) +30 day frequency forecasts for variants in bimonthly intervals using the MLR model for Trinidad and Tobago. Each forecast trajectory is shown as a different colored line. Retrospective smoothed frequency is shown as a thick black line.

(A) +30 day frequency forecasts for variants in bimonthly intervals using the MLR model for United Kingdom. Each forecast trajectory is shown as a different colored line. Retrospective smoothed frequency is shown as a thick black line.

(A) +30 day frequency forecasts for variants in bimonthly intervals using the MLR model for Vietnam. Each forecast trajectory is shown as a different colored line. Retrospective smoothed frequency is shown as a thick black line.

(A) The proportion of estimates lying within the 95% confidence intervals (CIs) of posterior latent frequencies across lag times (-30,-30). (B) The proportion of estimates lying within the 95% confidence intervals (CIs) of posterior predictive sample frequencies across lag times (-30,-30). We generate the posterior predictive sample frequencies by sampling random counts for each variant using their posterior latent frequencies conditioning on the total sequences being those observed retrospectively.

(A-H) Mean absolute error for MLR as a function of days since date of estimation, starting from 30 day hindcasts to 30 days forecasts. Intervals shown have width of two standard errors of the mean. We compare retrospective Nextstrain clade assignments made today (‘Current Nextclade’) to Nextstrain clade assignments available in Oct 2022 (‘Real- time Nextclade’). We find that errors are qualitatively similar regardless of Nextclade version with errors being potentially higher for the current Nextclade version.

Forecasts from MLR fit to data generated using retrospective Nextstrain clade designations (‘Current Nextclade’) (A) and Nextstrain clade assignments available in Oct 2022 (‘Real-time Nextclade’) (B).

Forecasts from MLR fit to data generated using retrospective Nextstrain clade designations (‘Current Nextclade’) (A) and Nextstrain clade assignments available in Oct 2022 (‘Real-time Nextclade’) (B).

Forecasts from MLR fit to data generated using retrospective Nextstrain clade designations (‘Current Nextclade’) (A) and Nextstrain clade assignments available in Oct 2022 (‘Real-time Nextclade’) (B).

Forecasts from MLR fit to data generated using retrospective Nextstrain clade designations (‘Current Nextclade’) (A) and Nextstrain clade assignments available in Oct 2022 (‘Real-time Nextclade’) (B).

Forecasts from MLR fit to data generated using retrospective Nextstrain clade designations (‘Current Nextclade’) (A) and Nextstrain clade assign- ments available in Oct 2022 (‘Real-time Nextclade’) (B).

Forecasts from MLR fit to data generated using retrospective Nextstrain clade designations (‘Current Nextclade’) (A) and Nextstrain clade assignments available in Oct 2022 (‘Real-time Nextclade’) (B).

Forecasts from MLR fit to data generated using retrospective Nextstrain clade designations (‘Current Nextclade’) (A) and Nextstrain clade assignments available in Oct 2022 (‘Real-time Nextclade’) (B).

Forecasts from MLR fit to data generated using retrospective Nextstrain clade designations (‘Current Nextclade’) (A) and Nextstrain clade assignments available in Oct 2022 (‘Real-time Nextclade’) (B).

Submitted filename: PCOMPBIOL-D-23-01974 Review.docx

Submitted filename: Manuscript Review Response.pdf

Submitted filename: #ncov-forecasting-fit reviewer response round 2.pdf


## Data Availability Statement

Sequence data including date and location of collection as well as clade annotation was obtained via the Nextstrain-curated data set that pulls data from GISAID database. A full list of sequences analyzed with accession numbers, derived data of sequence counts and case counts, along with all source code used to analyze this data and produce figures is available via the GitHub repository github.com/blab/ncov-forecasting-fit.

Articles from PLOS Computational Biology are provided here courtesy of PLOS
