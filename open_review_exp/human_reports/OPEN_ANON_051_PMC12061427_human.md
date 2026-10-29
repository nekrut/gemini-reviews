# Decision Letter 0


### Sushmita Roy


### Jean Fan


#### Roles

This is an open access article distributed under the terms of the Creative Commons Attribution License , which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.

Transfer learning of multicellular organization via single-cell and spatial transcriptomics

PLOS Computational Biology

Thank you for submitting your manuscript to PLOS Computational Biology. After careful consideration, we feel that it has merit but does not fully meet PLOS Computational Biology's publication criteria as it currently stands. Therefore, we invite you to submit a revised version of the manuscript that addresses the points raised during the review process.

​Please submit your revised manuscript within 60 days Feb 17 2025 11:59PM. If you will need more time than this to complete your revisions, please reply to this message or contact the journal office at ploscompbiol@plos.org. When you're ready to submit your revision, log on to https://www.editorialmanager.com/pcompbiol/ and select the 'Submissions Needing Revision' folder to locate your manuscript file.

Please include the following items when submitting your revised manuscript:

* A rebuttal letter that responds to each point raised by the editor and reviewer(s). You should upload this letter as a separate file labeled 'Response to Reviewers'. This file does not need to include responses to formatting updates and technical items listed in the 'Journal Requirements' section below.

* A marked-up copy of your manuscript that highlights changes made to the original version. You should upload this as a separate file labeled 'Revised Manuscript with Track Changes'.

* An unmarked version of your revised paper without tracked changes. You should upload this as a separate file labeled 'Manuscript'.

If you would like to make changes to your financial disclosure, competing interests statement, or data availability statement, please make these updates within the submission form at the time of resubmission. Guidelines for resubmitting your figure files are available below the reviewer comments at the end of this letter

We look forward to receiving your revised manuscript.

PLOS Computational Biology

PLOS Computational Biology

Journal Requirements:

1) We ask that a manuscript source file is provided at Revision. Please upload your manuscript file as a .doc, .docx, .rtf or .tex. If you are providing a .tex file, please upload it under the item type u2018LaTeX Source Fileu2019 and leave your .pdf version as the item type u2018Manuscriptu2019.

2) Please upload all main figures as separate Figure files in .tif or .eps format. For more information about how to convert and format your figure files please see our guidelines:

https://journals.plos.org/ploscompbiol/s/figures

3) Please ensure that the funders and grant numbers match between the Financial Disclosure field and the Funding Information tab in your submission form. Note that the funders must be provided in the same order in both places as well. State the initials, alongside each funding source, of each author to receive each grant. For example: "This work was supported by the National Institutes of Health (####### to AM; ###### to CJ) and the National Science Foundation (###### to AM)." State what role the funders took in the study. If the funders had no role in your study, please state: "The funders had no role in study design, data collection and analysis, decision to publish, or preparation of the manuscript.".

If you did not receive any funding for this study, please simply state: u201cThe authors received no specific funding for this work.u201d

Reviewer's Responses to Questions

Comments to the Authors:

Please note here if the review is uploaded as an attachment.

Reviewer #1: This manuscript presents a transfer learning framework for predicting the spatial positions of single cells based on scRNA-seq and spatial transcriptomics data. While the topic is interesting, the benchmark is conducted with low standards, with only mapping-based algorithms compared. In fact, many deconvolution-based algorithms have been proposed to solve the same questions, including RCTD, cell2location, DestVI, CARD, Redeconve, CytoSPACE, etc. Deconvolution-based algorithms have higher accuracy than mapping-based algorithms. Without demonstrating the advantages compared with currently available deconvolution-based algorithms, the current tool cannot be recommended for publication.

Reviewer #2: In this study, Shi et al. present iSORT, an algorithm that combines single-cell data and spatial transcriptomics through a transfer learning approach to reconstruct spatial organization. The authors benchmark iSORT against state-of-the-art methods using datasets from the human dorsolateral prefrontal cortex (DLPFC), mouse embryo, and mouse brain, assessing its performance in spatial distribution reconstruction. iSORT effectively identifies spatial patterns at the single-cell level, pinpoints spatial-organizing genes (SOGs) that drive these patterns, and infers pseudo-growth trajectories using the concept of SpaRNA velocity. Overall, iSORT demonstrates accuracy and efficiency in mapping single-cell and spatial transcriptomics data.

However, the authors should address several issues related to this methods.

1. In this study, the most scRNA-seq input was derived from the gene expression of spatial transcriptomics (ST) data at each spot, with the spatial coordinates removed. Since Visium data does not achieve true single-cell resolution and SeqFish only detects thousands of genes, these cannot be considered genuine single-cell data. It is crucial to evaluate iSORT's performance on different ST platform paired with real single cell data to determine whether it can effectively address batch effects between single-cell and ST technologies, enabling the reconstruction of spatial patterns and facilitating downstream analyses.

2. The manuscript compares iSORT with other methods using simulated SC data. However, additional comparative analyses are necessary to demonstrate the robustness of iSORT's performance. The authors analyze single-cell data generated from spatial transcriptomics data, but this method may not accurately represent real-world situations where SC and ST data originate from different samples and different technologies. It could be beneficial for the authors to evaluate iSORT's performance by incorporating various noise levels into the SC data.

3. When the single-cell data and spatial transcriptomics data have different numbers of genes, how should genes be selected for integration, particularly when the ST data, obtained from image-based technologies, includes only a few hundred genes? Can iSORT assist in identifying more spatially dominant genes from the scRNA-seq data, which contains a larger gene set?

4. The authors claim that the SOGs identified by iSORT are more effective than the SVGs detected by Moran's I and SpatialDE based on gene knockout experiments. What are the key differences genes between the SOGs and SVGs? The authors should provide additional evidence, such as gene expression patterns for the SOGs, and discuss the biological significance of these genes and their relationship to tissue structure and domains.

5. The results in Fig. 5 is confusing. It employs UMAP reduction to present the pseudo-time and RNA velocity results of scTour, while iSORT's results are shown in physical space. It might be better to use a consistent format to demonstrate and compare the two different methods.

Reviewer #3: In this manuscript, the authors established iSORT, a novel mapping method between single-cell and spatial transcriptomes. They also proposed two downstream analysis methods for spatial RNA velocity estimation and spatial gene identification, respectively. I have the following concerns:

1. iSORT is a reference-based mapping method. The authors should compare iSORT with state-of-the-art reference-based mapping methods such as CytoSPACE ( https://www.nature.com/articles/s41587-023-01697-9 ), STEM ( https://www.nature.com/articles/s42003-023-05640-1 ) and Celloc ( https://onlinelibrary.wiley.com/doi/10.1002/smsc.202400139 ).

2. Inclusion of multiple ST references is a highlight feature of iSORT, but the tests demonstrating such advantage are not sufficient.

3. Although the authors emphasize the introduction of transfer learning in their algorithm, I could not exactly find which part of the algorithm adopts such a transfer learning strategy in Figure 1. It seems that the term "density ratio transfer" would more accurately describe the strategy.

4. For spatial RNA velocity, the authors could compare their method with the latest method SIRV ( https://academic.oup.com/nargab/article/6/3/lqae100/7728020 ).

5. For spatial gene identification, the rationale for equation (13) is not clear. In addition, the authors could perform ssGSEA/GSVA analysis to check whether the spatial-organizing genes found by their method are more enriched for known key development-related genes or disease genes.

6. To better quantify the performance, the authors could compare their spatial-organizing gene identification method with the previous methods in simulated datasets, using a benchmarking strategy similar to the recent report ( https://genomebiology.biomedcentral.com/articles/10.1186/s13059-023-03145-y ).

Have the authors made all data and (if applicable) computational code underlying the findings in their manuscript fully available?

The PLOS Data policy requires authors to make all data and code underlying the findings described in their manuscript fully available without restriction, with rare exception (please refer to the Data Availability Statement in the manuscript PDF file). The data and code should be provided as part of the manuscript or its supporting information, or deposited to a public repository. For example, in addition to summary statistics, the data points behind means, medians and variance measures should be available. If there are restrictions on publicly sharing data or code —e.g. participant privacy or use of data from a third party—those must be specified.

PLOS authors have the option to publish the peer review history of their article ( what does this mean? ). If published, this will include your full peer review and any attached files.

If you choose “no”, your identity will remain anonymous but your review may still be made public.

Do you want your identity to be public for this peer review? For information about this choice, including consent withdrawal, please see our Privacy Policy .

[NOTE: If reviewer comments were submitted as an attachment file, they will be attached to this email and accessible via the submission site. Please log into your account, locate the manuscript record, and check for the action link "View Attachments". If this link does not appear, there are no attachment files.]

While revising your submission, please upload your figure files to the Preflight Analysis and Conversion Engine (PACE) digital diagnostic tool, https://pacev2.apexcovantage.com/ . PACE helps ensure that figures meet PLOS requirements. To use PACE, you must first register as a user. Registration is free. Then, login and navigate to the UPLOAD tab, where you will find detailed instructions on how to use the tool. If you encounter any issues or have any questions when using PACE, please email PLOS at figures@plos.org. Please note that Supporting Information files do not need this step. If there are other versions of figure files still present in your submission file inventory at resubmission, please replace them with the PACE-processed versions.

To enhance the reproducibility of your results, we recommend that authors of applicable studies deposit laboratory protocols in protocols.io, where a protocol can be assigned its own identifier (DOI) such that it can be cited independently in the future. Additionally, PLOS ONE offers an option to publish peer-reviewed clinical study protocols. Read more information on sharing protocols at https://plos.org/protocols?utm_medium=editorial-email&utm_source=authorletters&utm_campaign=protocols


# Author response to Decision Letter 1

Collection date 2025 Apr.

Submitted filename: Response to Reviewers.pdf


# Decision Letter 1


### Sushmita Roy


### Jean Fan


#### Roles

This is an open access article distributed under the terms of the Creative Commons Attribution License , which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.

We are pleased to inform you that your manuscript 'Transfer learning of multicellular organization via single-cell and spatial transcriptomics' has been provisionally accepted for publication in PLOS Computational Biology.

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

Reviewer #1: The authors have addressed all my concerns.

Reviewer #2: The authors have addressed all my comments. Thank authors for their efforts.

Reviewer #3: The authors have largely addressed my previous concern, making the overall quality of the manuscript suitable to be accepted.

Have the authors made all data and (if applicable) computational code underlying the findings in their manuscript fully available?

The PLOS Data policy requires authors to make all data and code underlying the findings described in their manuscript fully available without restriction, with rare exception (please refer to the Data Availability Statement in the manuscript PDF file). The data and code should be provided as part of the manuscript or its supporting information, or deposited to a public repository. For example, in addition to summary statistics, the data points behind means, medians and variance measures should be available. If there are restrictions on publicly sharing data or code —e.g. participant privacy or use of data from a third party—those must be specified.

PLOS authors have the option to publish the peer review history of their article ( what does this mean? ). If published, this will include your full peer review and any attached files.

If you choose “no”, your identity will remain anonymous but your review may still be made public.

Do you want your identity to be public for this peer review? For information about this choice, including consent withdrawal, please see our Privacy Policy .

Reviewer #2: Yes: Can Yang


# Acceptance letter


### Sushmita Roy


### Jean Fan


#### Roles

This is an open access article distributed under the terms of the Creative Commons Attribution License , which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.

PCOMPBIOL-D-24-01905R1

Transfer learning of multicellular organization via single-cell and spatial transcriptomics

I am pleased to inform you that your manuscript has been formally accepted for publication in PLOS Computational Biology. Your manuscript is now with our production department and you will be notified of the publication date in due course.

The corresponding author will soon be receiving a typeset proof for review, to ensure errors have not been introduced during production. Please review the PDF proof of your manuscript carefully, as this is the last chance to correct any errors. Please note that major changes, or those which affect the scientific understanding of the work, will likely cause delays to the publication date of your manuscript.

Soon after your final files are uploaded, unless you have opted out, the early version of your manuscript will be published online. The date of the early version will be your article's publication date. The final article will be published to the same URL, and all versions of the paper will be accessible to readers.

Thank you again for supporting PLOS Computational Biology and open-access publishing. We are looking forward to publishing your work!

PLOS Computational Biology | Carlyle House, Carlyle Road, Cambridge CB4 3DN | United Kingdom ploscompbiol@plos.org | Phone +44 (0) 1223-442824 | ploscompbiol.org | @PLOSCompBiol

This section collects any data citations, data availability statements, or supplementary materials included in this article.


## Supplementary Materials

The supplementary document provides eight notes, ten tables, and twenty-three supplementary figures for the main text.

Submitted filename: Response to Reviewers.pdf


## Data Availability Statement

All relevant data are within the paper and its Supporting Information files. The original public data used in this paper can be accessed through the following links: (1) FISH data from the Berkeley Drosophila Transcription Network Project (BDTNP): https://shiny.mdc-berlin.de/DVEX/ ; (2) 10X Visium data of the human dorsolateral prefrontal cortex (DLPFC): http://spatial.libd.org/spatialLIBD/ ; (3) Adult mouse cortical cell datasets (GEO accession GSE71585): https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE71585 ; (4) Mouse embryo data: https://content.cruk.cam.ac.uk/jmlab/SpatialMouseAtlas2020/ ; (5) Seurat objects ST data (10X Genomics Visium) of mouse brain: https://satijalab.org/seurat/articles/spatial_vignette.html ; (6) 10X Visium data of mouse brain: https://www.ebi.ac.uk/biostudies/arrayexpress/studies/E-MTAB-11114 ; (7) MERFISH data of mouse brain: https://portal.brain-map.org/atlases-and-data/bkp/abc-atlas ; (8) MERFISH data of human MTG: https://doi.org/10.5061/dryad.x3ffbg7mw ; (9) SMART-seq data of human MTG: https://portal.brain-map.org/atlases-and-data/rnaseq/human-mtg-smart-seq ; (10) Single-cell RNA-seq and Spatial Transcriptomics data of developing human heart: https://data.mendeley.com/datasets/mbvhhf8m62/2 ; (11) Human artery data: https://doi.org/10.5281/zenodo.15132967 . The iSORT algorithm is available on GitHub: [GITHUB_REPO_REDACTED] .

Articles from PLOS Computational Biology are provided here courtesy of PLOS
