# Decision Letter 0


### Joel O Wertheim


### Virginia E Pitzer


#### Roles

This is an open access article distributed under the terms of the Creative Commons Attribution License , which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.

PCOMPBIOL-D-24-01565How does date-rounding affect phylodynamic inference for public health?PLOS Computational Biology Dear Dr. Leo, Thank you for submitting your manuscript to PLOS Computational Biology. After careful consideration, we feel that it has merit but does not fully meet PLOS Computational Biology's publication criteria as it currently stands. Therefore, we invite you to submit a revised version of the manuscript that addresses the points raised during the review process. Please submit your revised manuscript within 30 days Dec 25 2024 11:59PM. If you will need more time than this to complete your revisions, please reply to this message or contact the journal office at ploscompbiol@plos.org. When you're ready to submit your revision, log on to https://www.editorialmanager.com/pcompbiol/ and select the 'Submissions Needing Revision' folder to locate your manuscript file. Please include the following items when submitting your revised manuscript:* A rebuttal letter that responds to each point raised by the editor and reviewer(s). You should upload this letter as a separate file labeled 'Response to Reviewers'. This file does not need to include responses to formatting updates and technical items listed in the 'Journal Requirements' section below.* A marked-up copy of your manuscript that highlights changes made to the original version. You should upload this as a separate file labeled 'Revised Manuscript with Track Changes'.* An unmarked version of your revised paper without tracked changes. You should upload this as a separate file labeled 'Manuscript'. If you would like to make changes to your financial disclosure, competing interests statement, or data availability statement, please make these updates within the submission form at the time of resubmission. Guidelines for resubmitting your figure files are available below the reviewer comments at the end of this letter. We look forward to receiving your revised manuscript. Kind regards, Joel O. WertheimAcademic EditorPLOS Computational Biology Virginia PitzerSection EditorPLOS Computational Biology

PLOS Computational Biology

PLOS Computational Biology

Journal Requirements: Additional Editor Comments (if provided): In addition to the reviewers’ comments and suggestions, I would also appreciate if you could address the following points. First, I believe the use of term ‘bias’ is inconsistent. The error is described as “unpredictable in its direction and compounds with decreasing date-resolution”, which sounds a lot like increasing variance to me. Bias, in contrast, would be that inferred dates are consistently younger when tip-date uncertainty is magnified [or inferred dates are older, but not both at the same time]. However, the directionality here appears to be highly model and organism dependent. Hence, it seems that tip-date uncertainty leads to greater variance and uncertainty, but not necessarily bias. Second, why does the Discussion directly name two pathogen nucleotide repositories (GISAID and Pathoplexus) and make no mention of other, larger governmental databases like GenBank, where GISAID and Pathoplexus currently import many sequences from? [Note: HTML markup is below. Please do not edit.] Reviewers' comments: Reviewer's Responses to Questions

Comments to the Authors:

Please note here if the review is uploaded as an attachment.

Reviewer #1: Phylodynamic inference uses temporal information in the form of the sampling dates of the sequences to generate time-calibrated phylogenies from which tMRCAs, evolutionary substitution rates, and epidemiological parameters can be estimated. However, sampling month and day information are not always available, so strategies like rounding the sampling dates to the day or month are commonly used. Featherstone et al. present a comprehensive study of date-rounding's effect on the inference of important epidemiological and evolutionary parameters in a phylodynamic analysis, using both simulated and empirical datasets of viral and bacterial pathogens with varying evolutionary rates and sampling windows. The negative effects of rounding were more prominent for fast-evolving RNA viruses. The authors also argue that the bias introduced by date-rounding can be reduced (although not completely removed) when the unit of time used for the rounding (i.e., day or month) is shorter than the average time to observe a substitution in the sequences. Furthermore, they discuss some strategies to facilitate sharing complete sampling dates while protecting patient confidentiality.

The manuscript is well-structured and easy to read, the methods are clearly explained, and the results are discussed in detail. This study tackles one of the major issues in Phylodynamics, while also using relevant pathogens for the analyses. I have only some minor comments for this manuscript:

• Why wasn’t the coalescent prior used for the bacterial pathogens? Adding the reason would make the methods section clearer.

• I understand that it is recommended to avoid improper priors in a Bayesian phylogenetic analysis. What is the advantage of using an improper prior like 1/X over a Uniform with a very high upper bound (let’s say 100 million for the population size)?

• Line 200: delete every in “since every the target”

• Line 203: could the authors add a brief explanation of the origin parameter? Does it represent the age of the outbreak mentioned in line 186?

• Line 230: replace “birth-tree” by “birth-death tree”

• Line 271 remove duplicated words: At the year resolution there is there is

• In figure 3, panel B, the coalescent results are missing for SARS-CoV-2. Was this done on purpose? If yes, add the justification on the figure legend.

Reviewer #2: The manuscript entitled “How does date-rounding affect phylodynamic inference for public health?” presents an elegant analysis with a clear public health application. The authors investigate whether rounding of the sampling date introduces bias in phylodynamic inference, along with the magnitude and directionality of this bias based on several parameters. They also present a solution of how to avoid the rounding while preserving patient’s confidentiality. Overall, the article is well written and presented and I recommend it for publication. A few suggestions/questions that could help improve the manuscript include:

1. Is there a possibility to include an example of a viral rapidly evolving pathogen sampled over a longer period of time (a few years or decades)? I wonder if the same “clustering in time” issue will be a problem when there are more clusters that are distributed over time (i.e. samples collected over 48 months rather than 9). As we are moving into year 5 of COVID and year 40+ with HIV, it would be interesting to consider how the dates resolution affect phylodynamic inference of viral infections of public health concern sampled over a longer period of time.

2. It is not obvious to me why the authors insist on including the coalescent tree prior for SARS-CoV-2 dataset even though it violates the sampling proportion assumption (as they highlight in the text). Since this tree prior is already not included for the bacterial infections, I would consider removing.

3. Also, I understand that there is no effective “true value” for the empirical datasets, but maybe a range of “plausible values” based on the literature could be helpful for figure 3.

4. I suggest that the last paragraph in the Introduction to be moved to the Methods as it refers to the study setting and design.

5. Line 123-124 – did you mean “rounded to weeks”? If not, then unclear why Figure 1 refers to weeks and not days.

6. A few questions about the simulation setup that are not clear from the text: please explain how you define the proportion of sequenced cases in your simulations to meet the empirical datasets. Also, what did you consider to be the outbreak duration in your simulation?

7. Please describe the tree priors at the first time you refer to them (line 160).

8. Figure 2 – order legend in the same order as colors appear in the figure.

9. Line 271 and 395 typos.

Have the authors made all data and (if applicable) computational code underlying the findings in their manuscript fully available?

The PLOS Data policy requires authors to make all data and code underlying the findings described in their manuscript fully available without restriction, with rare exception (please refer to the Data Availability Statement in the manuscript PDF file). The data and code should be provided as part of the manuscript or its supporting information, or deposited to a public repository. For example, in addition to summary statistics, the data points behind means, medians and variance measures should be available. If there are restrictions on publicly sharing data or code —e.g. participant privacy or use of data from a third party—those must be specified.

PLOS authors have the option to publish the peer review history of their article ( what does this mean? ). If published, this will include your full peer review and any attached files.

If you choose “no”, your identity will remain anonymous but your review may still be made public.

Do you want your identity to be public for this peer review? For information about this choice, including consent withdrawal, please see our Privacy Policy .

[NOTE: If reviewer comments were submitted as an attachment file, they will be attached to this email and accessible via the submission site. Please log into your account, locate the manuscript record, and check for the action link "View Attachments". If this link does not appear, there are no attachment files.] Figure resubmission: While revising your submission, please upload your figure files to the Preflight Analysis and Conversion Engine (PACE) digital diagnostic tool, https://pacev2.apexcovantage.com/ . PACE helps ensure that figures meet PLOS requirements. To use PACE, you must first register as a user. Registration is free. Then, login and navigate to the UPLOAD tab, where you will find detailed instructions on how to use the tool. If you encounter any issues or have any questions when using PACE, please email PLOS at figures@plos.org. Please note that Supporting Information files do not need this step. If there are other versions of figure files still present in your submission file inventory at resubmission, please replace them with the PACE-processed versions. Reproducibility: To enhance the reproducibility of your results, we recommend that authors of applicable studies deposit laboratory protocols in protocols.io, where a protocol can be assigned its own identifier (DOI) such that it can be cited independently in the future. Additionally, PLOS ONE offers an option to publish peer-reviewed clinical study protocols. Read more information on sharing protocols at https://plos.org/protocols?utm_medium=editorial-email&utm_source=authorletters&utm_campaign=protocols


# Author response to Decision Letter 1

Collection date 2025 Apr.

Submitted filename: response.pdf


# Decision Letter 1


### Joel O Wertheim


### Virginia E Pitzer


#### Roles

This is an open access article distributed under the terms of the Creative Commons Attribution License , which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.

We are pleased to inform you that your manuscript 'How does date-rounding affect phylodynamic inference for public health?' has been provisionally accepted for publication in PLOS Computational Biology.

Before your manuscript can be formally accepted you will need to complete some formatting changes, which you will receive in a follow up email. A member of our team will be in touch with a set of requests.

Please note that your manuscript will not be scheduled for publication until you have made the required changes, so a swift response is appreciated.

IMPORTANT: The editorial review process is now complete. PLOS will only permit corrections to spelling, formatting or significant scientific errors from this point onwards. Requests for major changes, or any which affect the scientific understanding of your work, will cause delays to the publication date of your manuscript.

Should you, your institution's press office or the journal office choose to press release your paper, you will automatically be opted out of early publication. We ask that you notify us now if you or your institution is planning to press release the article. All press must be co-ordinated with PLOS.

Thank you again for supporting Open Access publishing; we are looking forward to publishing your work in PLOS Computational Biology.

PLOS Computational Biology

PLOS Computational Biology

***********************************************************

Reviewer's Responses to Questions

Comments to the Authors:

Please note here if the review is uploaded as an attachment.

Reviewer #1: The authors have satisfactorily addressed all my comments, improving the quality and clarity of the manuscript. I have no further remarks.

Reviewer #2: I thank the authors for their careful consideration of my comments. I think the addition of the supplementary H3N2 dataset analysis strengthens the manuscript and their conclusions.

Have the authors made all data and (if applicable) computational code underlying the findings in their manuscript fully available?

The PLOS Data policy requires authors to make all data and code underlying the findings described in their manuscript fully available without restriction, with rare exception (please refer to the Data Availability Statement in the manuscript PDF file). The data and code should be provided as part of the manuscript or its supporting information, or deposited to a public repository. For example, in addition to summary statistics, the data points behind means, medians and variance measures should be available. If there are restrictions on publicly sharing data or code —e.g. participant privacy or use of data from a third party—those must be specified.

PLOS authors have the option to publish the peer review history of their article ( what does this mean? ). If published, this will include your full peer review and any attached files.

If you choose “no”, your identity will remain anonymous but your review may still be made public.

Do you want your identity to be public for this peer review? For information about this choice, including consent withdrawal, please see our Privacy Policy .


# Acceptance letter


### Joel O Wertheim


### Virginia E Pitzer


#### Roles

This is an open access article distributed under the terms of the Creative Commons Attribution License , which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.

PCOMPBIOL-D-24-01565R1

How does date-rounding affect phylodynamic inference for public health?

Dear Dr Featherstone,

I am pleased to inform you that your manuscript has been formally accepted for publication in PLOS Computational Biology. Your manuscript is now with our production department and you will be notified of the publication date in due course.

The corresponding author will soon be receiving a typeset proof for review, to ensure errors have not been introduced during production. Please review the PDF proof of your manuscript carefully, as this is the last chance to correct any errors. Please note that major changes, or those which affect the scientific understanding of the work, will likely cause delays to the publication date of your manuscript.

Soon after your final files are uploaded, unless you have opted out, the early version of your manuscript will be published online. The date of the early version will be your article's publication date. The final article will be published to the same URL, and all versions of the paper will be accessible to readers.

Thank you again for supporting PLOS Computational Biology and open-access publishing. We are looking forward to publishing your work!

PLOS Computational Biology | Carlyle House, Carlyle Road, Cambridge CB4 3DN | United Kingdom ploscompbiol@plos.org | Phone +44 (0) 1223-442824 | ploscompbiol.org | @PLOSCompBiol

This section collects any data citations, data availability statements, or supplementary materials included in this article.


## Supplementary Materials

Fig A in S1 File. Mean posterior variance for parameters of interest for each replicate of simulated data varying across date resolution. Individual lines track mean posterior variance for each simulated dataset and boxplots are given to summarise variance in each condition at each date resolution. Rows correspond to individual parameters, columns correspond to simulation conditions (underlying parameters matching each empirical dataset), and colour corresponds to tree prior or reproductive number interval. (A) Mean posterior variance in substitution rate across simulation scenarios. (B) Posterior variance in tMRCA, a measure of the age of the population driving the outbreak. (C) Posterior variance in reproductive number reproductive number.

Fig B in S1 File. Desnsitrees (overlaid posterior trees) for empirical data with columns corresponding to pathogen under each combination of date resolution and tree prior. For the H1N1 and SARS-CoV-2 treatments, Year resolution causes trees to collapse to instantaneous bursts.

Fig C in S1 File. Adjusted phylodynamic likelihood against adjusted phylogenetic likelihood with panels corresponding to each simulation condition. Points correspond to mean posterior likelihood for each simulated dataset under each simulation condition. Colour corresponds to date resolution. Likelihoods are adjusted by subtracting the mean phylodynamic or phylogenetic likelihood at day resolution from each the means under month and year resolution. Resulting points therefore show the difference phylodynamic and phylogenetic likelihoods due to date-rounding with the point ( 0 , 0 ) representing likelihood at day resolution for each dataset. Month resolution generally results in smaller differences that Year resolution, suggesting coarser date resolution results in more perturbed likelihoods. There is also generally more error in phylodynamic likelihood than phylogenetic likelihood.

Fig D in S1 File. Posterior distributions for the substitution rate, tMRCA, and R 0 for the H3N2 dataset. The x-axis corresponds to the date resolution used in each re-analysis, and horizontal lines denote the median and 95% HPD bounds in each distribution. Overall, the H3N2 dataset is less sensitive to date rounding, but displays the same patterns of bias with decreasing date resolution as the comparable viral datasets of H1N1 and SARS-CoV-2 in the main text.

Fig E in S1 File. The number of samples over time for each empirical dataset. Date-roundinghas the effect of moving each sampling within a month or year to the middle of that month oryear ( 1 5 t h of themonth or June 1 5 t h of the year).

Table A in S1 File. Mean posterior estimates of substitution rate and tMRCA forempirical data with 95% HPD in brackets. The lower table gives mean posterior estimatesof R ∙ forempirical data with 95% HPD in brackets.

Submitted filename: response.pdf


## Data Availability Statement

All of the code and date required to reproduce the simulation study, empirical analyses, and figures/tables are available at https://github.com/LeoFeatherstone/pdp

Articles from PLOS Computational Biology are provided here courtesy of PLOS
