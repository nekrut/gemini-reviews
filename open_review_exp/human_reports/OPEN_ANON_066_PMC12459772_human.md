# Decision Letter 0


### Philipp Martin Altrock


#### Roles

This is an open access article distributed under the terms of the Creative Commons Attribution License , which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.

Estimating the effectiveness of non-pharmaceutical interventions against COVID-19 transmission in the Netherlands

PLOS Computational Biology

Thank you for submitting your manuscript to PLOS Computational Biology. After careful consideration, we feel that it has merit but does not fully meet PLOS Computational Biology's publication criteria as it currently stands. Therefore, we invite you to submit a revised version of the manuscript that addresses the points raised during the review process.

Please submit your revised manuscript within 30 days Sep 07 2025 11:59PM. If you will need more time than this to complete your revisions, please reply to this message or contact the journal office at ploscompbiol@plos.org. When you're ready to submit your revision, log on to https://www.editorialmanager.com/pcompbiol/ and select the 'Submissions Needing Revision' folder to locate your manuscript file.

Please include the following items when submitting your revised manuscript:

* A rebuttal letter that responds to each point raised by the editor and reviewer(s). You should upload this letter as a separate file labeled 'Response to Reviewers'. This file does not need to include responses to formatting updates and technical items listed in the 'Journal Requirements' section below.

* A marked-up copy of your manuscript that highlights changes made to the original version. You should upload this as a separate file labeled 'Revised Manuscript with Track Changes'.

* An unmarked version of your revised paper without tracked changes. You should upload this as a separate file labeled 'Manuscript'.

If you would like to make changes to your financial disclosure, competing interests statement, or data availability statement, please make these updates within the submission form at the time of resubmission. Guidelines for resubmitting your figure files are available below the reviewer comments at the end of this letter.

We look forward to receiving your revised manuscript.

Philipp Martin Altrock, Ph.D.

PLOS Computational Biology

PLOS Computational Biology

Journal Requirements:

1) Please ensure that the CRediT author contributions listed for every co-author are completed accurately and in full.

At this stage, the following Authors/Authors require contributions: Jantien A. Backer. Please ensure that the full contributions of each author are acknowledged in the "Add/Edit/Remove Authors" section of our submission form.

The list of CRediT author contributions may be found here: https://journals.plos.org/ploscompbiol/s/authorship#loc-author-contributions

2) We ask that a manuscript source file is provided at Revision. Please upload your manuscript file as a .doc, .docx, .rtf or .tex. If you are providing a .tex file, please upload it under the item type u2018LaTeX Source Fileu2019 and leave your .pdf version as the item type u2018Manuscriptu2019.

3) Please provide an Author Summary. This should appear in your manuscript between the Abstract (if applicable) and the Introduction, and should be 150-200 words long. The aim should be to make your findings accessible to a wide audience that includes both scientists and non-scientists. Sample summaries can be found on our website under Submission Guidelines:

https://journals.plos.org/ploscompbiol/s/submission-guidelines#loc-parts-of-a-submission

4) Please upload all main figures as separate Figure files in .tif or .eps format. For more information about how to convert and format your figure files please see our guidelines:

https://journals.plos.org/ploscompbiol/s/figures

5) We have noticed that you have uploaded Supporting Information files, but you have not included a list of legends. Please add a full list of legends for your Supporting Information files after the references list.

6) Please amend your detailed Financial Disclosure statement. This is published with the article. It must therefore be completed in full sentences and contain the exact wording you wish to be published.

1) State the initials, alongside each funding source, of each author to receive each grant. For example: "This work was supported by the National Institutes of Health (####### to AM; ###### to CJ) and the National Science Foundation (###### to AM)."

Please state the initials of the authors alongside these funding sources "the Ministry of Health, Welfare and Sport and European Union’s Horizon research and innovation programme - project ESCAPE".

Reviewer's Responses to Questions

This manuscript presents an approach to estimate the effectiveness of non-pharmaceutical interventions (NPIs) on COVID-19 transmission in the Netherlands from February 2020 to October 2021. By integrating multiple data sources (including reproduction number estimates, genomic surveillance, vaccination coverage, and seroprevalence surveys), the authors simulate time-varying counterfactual reproduction numbers in the absence of NPIs. They quantify the reduction in transmission attributable to NPIs, accounting for three components: (1) seasonality, (2) variant emergence, and (3) population immunity. Overall, the manuscript is methodologically strong and timely. A few clarifications and minor revisions are suggested below.

The counterfactual reproduction number is constructed under the assumption of linear scaling with the immune fraction and multiplicative effects from variant transmissibility and seasonal variation. Please acknowledge that this approach may not fully capture heterogeneities such as contact structure or setting-specific transmission dynamics.

The manuscript introduces a time-varying basic reproduction number, which diverges from the standard epidemiological definition of R0 as a constant. This may cause confusion, especially given the presence of a separate constant “initial R0”. Consider renaming the basic reproduction number to avoid confusion.

Line 40: Remove “(and references therein)”

Line 110: “lower than winter”

Line 135: “October 2021.”

Figure 1: The 95% confidence intervals for vaccination lines are not available. Either add uncertainty or update the legend to reflect what is shown.

Figure 4: The right panel shows shaded areas for observed breakthrough infections, but the left panel lacks this uncertainty. For consistency, clarify which lines include uncertainty intervals and which do not.

Figures 5 and 6: Display the negative y-axis to reflect effectiveness values below 0%, as mentioned in line 200. Also, include a legend explaining the values represented by the stringency index color band.

Line 280: Suggest explicitly stating the months instead of using “winter 2020/2021”

Line 287: “population level”

Lines 365 and 437: Clarify how validation data were used more clearly.

Table 1: Update the reference column to use the [number] format consistent with in-text citations. Ensure all cited studies are included each row. Specify whether waning rates per day were taken directly from referenced studies or derived by the authors based on those studies.

Reviewer #2: The manuscript titled “Estimating the effectiveness of NPIs against COVID-19 transmission in the Netherlands” quantifies the benefits of NPIs in real time by showing how NPIs lead to decrease in the effective reproduction number.

The manuscript is well-written, and overall I like the work.

I am tempted to suggest acceptance, but would like the authors to respond to some comments/questions.

Line 62-63: can you further expand on basic reproduction number? By now, there are already three kind of reproduction numbers— effective, counterfactual, and now basic.

Line 109-110: I think you meant “…. In summer 33% lower than in winter”.

Fig. 2: Please briefly describe in the main text how blue curves have been generated? Are these some sort of curve fittings to 3 data points shown in the plots?

In Fig.3: Has any equation being used to plot the curves? If so, please mention it in the main text. Or is it purely data analysis and interpolation?

Line 142-144: Please briefly add to the text how you have accounted for immunity waning. For a PloS CB reader, I would tend to expect a bit more detail description in the main text.

Line 145: may be consider changing naïve to naive (for consistency)

Line 152: Please cite some references to support this. Or is it the conclusion from Fig. 3 that vaccine induced immunity wanes faster than natural immunity?

Line 163: What are these “calculations”? Are these mathematical calculation? Please clarify on this.

Line 164: What are breakthrough infections and how are they different from reinfections?

Line 169: The sentence suggests that there is some underlying model for immunity waning. Can you bring it to the main text and discuss here?

Line 193-194: Is it a new result? If not, it will be helpful to cite some references. Same for the sentence 197-198.

Line 199: What does negative effectiveness mean? How can NPIs have negative effect?

Line 216: Are you particularly referring to Fig. 5B? If so, please update the figure reference accordingly.

Why only restrict to Netherlands? How about comparison with the results of refs. 4-9 that assume constant affect of season etc. through time?

The manuscript is about quantifying (important) the effectiveness of NPIs. We all in some sense agree about the usefulness of NPIs. But what is the cost of NPIs? Can you say anything about that? Example, economic cost, social resistance etc. Any references?

Line 106: For other variants immune escape is also at play. Yet R_0 is defined for those strains. Is it true? Shouldn’t immune escape be somehow taken care by the definition of R_0?

Have the authors made all data and (if applicable) computational code underlying the findings in their manuscript fully available?

The PLOS Data policy requires authors to make all data and code underlying the findings described in their manuscript fully available without restriction, with rare exception (please refer to the Data Availability Statement in the manuscript PDF file). The data and code should be provided as part of the manuscript or its supporting information, or deposited to a public repository. For example, in addition to summary statistics, the data points behind means, medians and variance measures should be available. If there are restrictions on publicly sharing data or code —e.g. participant privacy or use of data from a third party—those must be specified.

PLOS authors have the option to publish the peer review history of their article ( what does this mean? ). If published, this will include your full peer review and any attached files.

If you choose “no”, your identity will remain anonymous but your review may still be made public.

Do you want your identity to be public for this peer review? For information about this choice, including consent withdrawal, please see our Privacy Policy .

[NOTE: If reviewer comments were submitted as an attachment file, they will be attached to this email and accessible via the submission site. Please log into your account, locate the manuscript record, and check for the action link "View Attachments". If this link does not appear, there are no attachment files.]

While revising your submission, please upload your figure files to the Preflight Analysis and Conversion Engine (PACE) digital diagnostic tool, https://pacev2.apexcovantage.com/ . PACE helps ensure that figures meet PLOS requirements. To use PACE, you must first register as a user. Registration is free. Then, login and navigate to the UPLOAD tab, where you will find detailed instructions on how to use the tool. If you encounter any issues or have any questions when using PACE, please email PLOS at figures@plos.org. Please note that Supporting Information files do not need this step. If there are other versions of figure files still present in your submission file inventory at resubmission, please replace them with the PACE-processed versions.

To enhance the reproducibility of your results, we recommend that authors of applicable studies deposit laboratory protocols in protocols.io, where a protocol can be assigned its own identifier (DOI) such that it can be cited independently in the future. Additionally, PLOS ONE offers an option to publish peer-reviewed clinical study protocols. Read more information on sharing protocols at https://plos.org/protocols?utm_medium=editorial-email&utm_source=authorletters&utm_campaign=protocols


# Author response to Decision Letter 1

Collection date 2025 Sep.

Submitted filename: Response_to_reviewers.pdf


# Decision Letter 1


### Philipp Martin Altrock


#### Roles

This is an open access article distributed under the terms of the Creative Commons Attribution License , which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.

We are pleased to inform you that your manuscript 'Estimating the effectiveness of non-pharmaceutical interventions against COVID-19 transmission in the Netherlands' has been provisionally accepted for publication in PLOS Computational Biology.

Before your manuscript can be formally accepted you will need to complete some formatting changes, which you will receive in a follow up email. A member of our team will be in touch with a set of requests.

Please note that your manuscript will not be scheduled for publication until you have made the required changes, so a swift response is appreciated.

IMPORTANT: The editorial review process is now complete. PLOS will only permit corrections to spelling, formatting or significant scientific errors from this point onwards. Requests for major changes, or any which affect the scientific understanding of your work, will cause delays to the publication date of your manuscript.

Should you, your institution's press office or the journal office choose to press release your paper, you will automatically be opted out of early publication. We ask that you notify us now if you or your institution is planning to press release the article. All press must be co-ordinated with PLOS.

Thank you again for supporting Open Access publishing; we are looking forward to publishing your work in PLOS Computational Biology.

Philipp Martin Altrock, Ph.D.

PLOS Computational Biology

PLOS Computational Biology

***********************************************************

Reviewer's Responses to Questions

Comments to the Authors:

Please note here if the review is uploaded as an attachment.

Reviewer #1: All comments have been addressed.

Have the authors made all data and (if applicable) computational code underlying the findings in their manuscript fully available?

The PLOS Data policy requires authors to make all data and code underlying the findings described in their manuscript fully available without restriction, with rare exception (please refer to the Data Availability Statement in the manuscript PDF file). The data and code should be provided as part of the manuscript or its supporting information, or deposited to a public repository. For example, in addition to summary statistics, the data points behind means, medians and variance measures should be available. If there are restrictions on publicly sharing data or code —e.g. participant privacy or use of data from a third party—those must be specified.

PLOS authors have the option to publish the peer review history of their article ( what does this mean? ). If published, this will include your full peer review and any attached files.

If you choose “no”, your identity will remain anonymous but your review may still be made public.

Do you want your identity to be public for this peer review? For information about this choice, including consent withdrawal, please see our Privacy Policy .


# Acceptance letter


### Philipp Martin Altrock


#### Roles

This is an open access article distributed under the terms of the Creative Commons Attribution License , which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.

PCOMPBIOL-D-25-00738R1

Estimating the effectiveness of non-pharmaceutical interventions against COVID-19 transmission in the Netherlands

I am pleased to inform you that your manuscript has been formally accepted for publication in PLOS Computational Biology. Your manuscript is now with our production department and you will be notified of the publication date in due course.

The corresponding author will soon be receiving a typeset proof for review, to ensure errors have not been introduced during production. Please review the PDF proof of your manuscript carefully, as this is the last chance to correct any errors. Please note that major changes, or those which affect the scientific understanding of the work, will likely cause delays to the publication date of your manuscript.

Soon after your final files are uploaded, unless you have opted out, the early version of your manuscript will be published online. The date of the early version will be your article's publication date. The final article will be published to the same URL, and all versions of the paper will be accessible to readers.

You will receive an invoice from PLOS for your publication fee after your manuscript has reached the completed accept phase. If you receive an email requesting payment before acceptance or for any other service, this may be a phishing scheme. Learn how to identify phishing emails and protect your accounts at https://explore.plos.org/phishing .

Thank you again for supporting PLOS Computational Biology and open-access publishing. We are looking forward to publishing your work!

PLOS Computational Biology | Carlyle House, Carlyle Road, Cambridge CB4 3DN | United Kingdom ploscompbiol@plos.org | Phone +44 (0) 1223-442824 | ploscompbiol.org | @PLOSCompBiol

This section collects any data citations, data availability statements, or supplementary materials included in this article.


## Supplementary Materials

Submitted filename: Response_to_reviewers.pdf


## Data Availability Statement

All data is publicly available, either as open data or as additional data sets on the github repository accompanying this study: github.com/rivm-syso/effectiveness_NPIs. This repository also contains the code used to produce the results and analyses presented in this manuscript.

Articles from PLOS Computational Biology are provided here courtesy of PLOS
