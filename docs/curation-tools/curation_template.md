---
sidebar_position: 10
---

# Data curation template

The following template is based on the CURATE(D) checklist from DCN.

:::info[Suggested Citation]

Suggested Citation: Data Curation Network (2022). "CURATE(D) Steps and Checklist for Data Curation, version 2" http://z.umn.edu/curate.

:::

This template assumes some of the following:
- Data will be published to a generalist Dataverse Project repository
- Text data will be encoded using UTF-8 standard
- Jupyter notebooks will be used to document the processes of data import and export using the Dataverse API

## **CHECK Step**

:::info[CHECK Step]

**Check data files/code and read documentation**  

In this step we secure the dataset by inventorying and reviewing the contents, applying local appraisal and selection criteria. Common CHECK steps include:  
- Review to ensure data is in scope for the repository 
- Inventory the contents of the data files (e.g., open and sample the files or code) 
- Verify all metadata provided by the researcher; check available documentation                                                                       

### Key Ethical Considerations

- Review participant agreement and data use agreements; examine potential impacts of sharing this data. Consider: 
  - Individuals and communities represented  
  - Representativeness of diverse human populations Protection or endangerment status of species 
  - Geographic locations (e.g., contested boundaries, historical and current political situations) 
  - Animal research ethics and approval 
- Is it possible that the dataset may impact a specific group? 
- Does this dataset follow compliance & institutional policy?                                                                                                                                                                 
### Essential Tasks

- [ ] Begin Curator Log to track curation decisions 
- [ ] Open the related article and supporting information if available 
- [ ] Inventory the dataset 
  - [ ] Identify file formats 
  - [ ] Review file organization, hierarchy, and naming convention(s) 
  - [ ] Extract zip files when possible 
- [ ] Create working copy of files for formal inventory and testing 
- [ ] Examine code for obvious errors/missing components, etc. 
- [ ] Check that metadata quality is rich, accurate, and complete to institutional requirements. 
- [ ] Check documentation type (circle or specify one) -- README / Codebook / Data Dictionary / Other: ____________
  - [ ] Complete 
  - [ ] Needs work  
  - [ ] If missing, document for the "Request" step 
- [ ] Check whether human subject data (data about humans regardless of IRB determination) is present. If so, 
  - [ ] Request consent form / participation agreement if not present 
  - [ ] If the data are not de-identified, document for the "Request" step.
- [ ] Check the accessibility of all files 
  - [ ] Ensure there are robust descriptions in plain text of data files and any images.  
- [ ] Check whether any visualization(s) of data are easily accessible 
  - [ ] Review alt-text and visualization descriptions. 
  - [ ] Ensure these describe, but do not interpret, associated visualizations. 
  - [ ] Check data visualizations follow accessible color contrast guidelines 
  - [ ] Recommend graphical representation ______________ 
  - [ ] Recommend web-accessible surrogate ______________

:::

## **UNDERSTAND Step**

:::info[UNDERSTAND Step]

**Understand the data (or try to)**

In this step, examine the dataset closely to understand what it is, how the files interrelate, and what information is needed to reuse. Common UNDERSTAND steps include: 

- Check for quality assurance and usability issues such as missing data, ambiguous headings, code execution failures, and data presentation concerns  
- Try to detect and extract any "hidden documentation" inherent to the data files that may facilitate reuse or expose unintended information  
- Determine if the documentation of the data is sufficient for a user with similar qualifications to the researchers to understand and reuse the data. If not, recommend or create additional documentation (e.g., a README.txt template)

### Key Ethical Considerations

- If working with human data, is this research done *with* and not *on* communities and populations involved? (You may wish to review data sources, researchers, and their connections to the communities and subjects they are serving to facilitate further conversation with researcher(s).)  
  - Are there authoritative group representatives who should be contacted in the next (request) step? 
- Are there labels or other descriptive indicators that could be applied to better represent or protect an identified group of people impacted by this dataset? (Example: [TK labels](https://localcontexts.org/labels/traditional-knowledge-labels/))                                                     

### Essential Tasks

- [ ] Examine files, organization, and documentation more thoroughly. 
  - [ ] Are there changes that could enhance the dataset? 
  - [ ] Are there missing data? 
  - [ ] Could a user with similar qualifications to the author's understand and reuse these data and reproduce the results? Are the data, documentation and/or metadata presented in a way that aids in interpretation? (e.g., [README Example](https://deepblue.lib.umich.edu/data/Deep\_Blue\_Data\_Example\_Readme.txt)) 
- [ ] Record all questions and concerns in Curation Log.  

*Tasks vary based on file formats and subject domain. Sample tasks based on format:* 

**Tabular Data (e.g, Microsoft Excel) Questions:**

- [ ] Check the organization of the data–is it well-structured? 
- [ ] Are headers/codes clearly defined? 
- [ ] Is quality control clearly defined? 
- [ ] Is methodology clear and sufficient? 

**Database(s) Questions:**

- [ ] Is there documentation on tables, relationships, queries, etc? 
- [ ] Can the data  be exported (to CSV(s), TXT or other) easily? 
- [ ] Which tables or queries are the relevant ones used in a publication? 

**Code Questions:**

- [ ] Does the provided code execute without errors? 
- [ ] Is the code commented, i.e., did the author provide descriptive information on sections of code? 
- [ ] Is data for input missing? Are environmental conditions and parameters noted? Is it clear which language(s) and version(s) are used? 
- [ ] Does the code use absolute paths or relative paths? If absolute paths, is this documented in the README? 
- [ ] Are packages or additional libraries used? Is so, is this noted with clear use instructions?  
- [ ] Are any data organized consistently for access by the code? 
- [ ] Is there an indication of whether the depositor intends users to be able to run the code and reproduce results, or just see the process used?  

To view additional UNDERSTAND steps based on format, view the following primers:

- [Acrobat PDF](http://hdl.handle.net/11299/210210) Primer 
- [ATLAS.ti](http://hdl.handle.net/11299/210211) Primer 
- [Confocal Microscopy Image](http://hdl.handle.net/11299/210206) Primer 
- [Geodatabase](http://hdl.handle.net/11299/202823 ) Primer 
- [GeoJSON](http://hdl.handle.net/11299/210208) Primer 
- [Jupyter Notebook](http://hdl.handle.net/11299/202815 ) Primer 
- [Microsoft Access](http://hdl.handle.net/11299/202827 ) Primer 
- [Microsoft Excel](http://hdl.handle.net/11299/202816 ) Primer 
- [netCDF](http://hdl.handle.net/2027.42/145724)  Primer and 
- [Tutorial using NCAR dataset](http://hdl.handle.net/11299/202825 ) 
- [SPSS](http://hdl.handle.net/11299/202812 ) Primer 
- [STL](http://hdl.handle.net/11299/211352) Primer 
- [R](http://hdl.handle.net/11299/210209) Primer 
- [Tableau](http://hdl.handle.net/11299/210207) Primer (Twitter primer?) 
- [Wordpress.com](http://hdl.handle.net/11299/202811 ) Primer

:::

## **REQUEST Step**

:::info[REQUEST Step]

**Request missing information or changes**

In this step, generate a list of questions to help the researcher fix any errors or issues and enrich the usability of the data. Common REQUEST steps include: 

- Triage and prioritize issues. 
- Identify and highlight those with the highest data reuse implications 
- Convey a sense of urgency, as there it becomes more difficult to get responses from researchers as time passes.  
- Collaborate with the researcher(s) to make necessary changes 
- Communicate any changes you, the curator, will make on their behalf 
- Pause and consider how best to frame and communicate requests. This should be the start of a conversation.

### Key Ethical Considerations

- Consider asking researchers if their participants will be notified that their data (in addition to published results) are being shared.  
- If you feel uncomfortable about sharing the data in its current state and/or it does not meet your institution's requirements, reserve the right not to publish. 
- Consider asking researcher(s) if there are limitations to how data could/should be used to include in documentation. (Based on, e.g., representativeness of sample).

### Essential Tasks

- [ ] Ask about additional data contributors, beyond publication authors. Consider using the Contributor Roles Taxonomy to communicate this: https://casrai.org/credit/  
- [ ] Summarize conversations / outreach efforts in Curator Log  

Sample email to researcher:

```
Dear [*name of the data set author or contact*],  

Thank you for depositing your data set, [*title of the data set*], to [*name of repository*].  

After we receive a data set, we review it to ensure that the data we host is as complete and understandable as possible. We have reviewed your data set and have the following recommendations for you:  

- Recommendation #1 
- Recommendation #2 
- Recommendation #3 
- Recommendation #4   

We look forward to hearing your response. Please let us know if you have any questions about our recommendations. We would be happy to talk with you or meet in person to discuss our review of your data, if you would like 

Sincerely,

[*Name of Curator*]
```
:::

## **AUGMENT Step**

:::info[AUGMENT Step]

**Augment the dataset**

In this step we ensure metadata conforms to repository and/or appropriate discipline standards; adjust metadata to improve findability and accessibility; and improve documentation to make data more understandable, interoperable and reusable. Common AUGMENT steps include: 

- Enhance metadata to best facilitate discoverability, such as by ensuring datasets have a persistent identifier. 
- Create and apply metadata for the data record, including descriptive keywords 
- When appropriate, structure and present metadata in domain-specific schemas to facilitate interoperability with other systems 
- Implement any other agreed-on enhancements to metadata or documentation following discussion with researcher

### Key Ethical Considerations

- Make sure bibliographic information reflects the correct author attribution. 
- Ensure any augmentation by the depositor to resolve ethical questions from previous steps is completed.

### Essential Tasks

- [ ] Review information received from the researcher from initial deposit and all subsequent conversations 
- [ ] Update, as appropriate: 
  - [ ] Metadata 
  - [ ] Documentation (README, Codebook, Data Dictionary, Other) 
  - [ ] Replacement files 
  - [ ] Organization and Arrangement of files 
  - [ ] Documentation of file organization, hierarchy, and naming convention(s)  
- [ ] Facilitate discoverability: 
  - [ ] Add links to related publications, grants, reports, source data, etc. 
  - [ ] Provide additional description of files as appropriate for external indexing or other purposes. 
  - [ ] Add subject terms 
- [ ] Ensure keywords are sufficient and representative 
- [ ] Record all changes in the Curation Log 
- [ ] Provide suggestions to improve accessibility of content (e.g., alt-text or additional descriptions; color contrast; etc.)

:::

## **TRANSFORM Step**

:::info[Transform file formats]

In this step, consider the file formats in the dataset to make them more interoperable, reusable, preservation friendly, and non-proprietary when possible.<sup>[1](#footnote-1)</sup> Common TRANSFORM steps include: 

- Identify specialized file formats and their restrictions (e.g., Is the software freely available? If so, link to it or archive it alongside the data)  
- Propose open source or more reusable formats when appropriate 
- Retain original file formats 

#### Footnote 1

> *<sup>1</sup>See Cornell's list of preservation format recommendations: [http://guides.library.cornell.edu/ecommons/formats](http://guides.library.cornell.edu/ecommons/formats)*

### Key Ethical Considerations

- Consider how best to navigate researcher bandwidth limitations and ownership of data with repository commitments to reducing barriers to reuse. 
- Decide how to balance the potential benefits of transformation with the risks of mistakes and loss of content/context, especially if the curator or repository will be performing transformation. Document the decision.

### Essential Tasks

- [ ] Check whether preferred file formats are in use 
  - [ ] If not, recommend conversion 
  - [ ] Retain original formats 
- [ ] Check whether software needed is readily available 
  - [ ] Suggest open source options, if applicable and appropriate 
  - [ ] Ensure software and software version is documented  
- [ ] Convert any data visualization(s) that are not accessible (e.g., R [visualizations](https://github.com/DataCurationNetwork/data-primers/blob/master/R%20Data%20Curation%20Primer/R-data-curation-primer.md#accessibility-considerations), which need to be converted for screen reader use, or visualizations that do not meet color contrast guidelines) Reorganize files as appropriate  
- [ ] Standardize file names  
- [ ] Record any transformations in Curator Log

:::

## **EVALUATE Step**

:::info[EVALUATE Step]

**Evaluate and rate the dataset**

In this step, review the dataset and companion data record against international standards, including FAIR,<sup>[2](#footnote-2)</sup> CARE,<sup>[3](#footnote-2)</sup> and FATE.<sup>[4](#footnote-2)</sup> Common EVALUATE steps: 
- Score the dataset and recommend ways to increase the FAIRness of the data 
- Review data for ethical concerns in line with CARE and FATE 

#### Footnote 2

> *<sup>2</sup> Rubric evaluating the FAIR principles are based on the scoring matrix by Dunning, de Smaele, & Böhmer ([2017](http://dx.doi.org/10.2218/ijdc.v12i2.567)).  
> <sup>3</sup> CARE principles: [https://www.gida-global.org/care](https://www.gida-global.org/care) 
> <sup>4</sup> FATE in AI: [https://www.microsoft.com/en-us/research/theme/fate/](https://www.microsoft.com/en-us/research/theme/fate/)*

### Key Ethical Considerations

- Final review--remember it is not too late to surface any ethical concerns. 
- Verify the words/language being used are not racist/harmful. 
- Remind the submitter of their responsibility if they choose to ignore requests for de-identification or similar concerns.

### Essential Tasks

- [ ] Test that files successfully download 
- [ ] Check that any transformations didn't introduce problems 
- [ ] Review final state of data and record with researcher before publication 
- [ ] Add any final changes to Curator Log  

*This is a sample checklist for evaluating datasets against a set of principles.*  

### FAIR evaluation

Findable:  
- [ ] Metadata exceeds researcher/ title/ date.  
- [ ] There is a unique Persistent ID (DOI, Handle, PURL, etc.).  
- [ ] Data/record is discoverable via web search engines.

Accessible:  
- [ ] Data/ record are retrievable via a standard protocol (e.g., HTTP).  
- [ ] Data/ record are free, open (e.g., via a download link).

Interoperable:
- [ ] Metadata is formatted in a standard schema (e.g., Dublin Core).  Metadata is provided in machine-readable format (OAI feed). 

Reusable:
- [ ] Data include sufficient metadata and supporting documentation about the data characteristics for reuse. 
- [ ] A way to contact the researcher directly for further questions is provided 
- [ ] There are clear indicators of who created, owns, and stewards the data. 
- [ ] Data are released with clear data usage terms (e.g., a CC License).
  
:::

## **DOCUMENT Step**

:::info[DOCUMENT Step]

**Document curation activities throughout**

In the Curator Log mentioned throughout this guide, record the significant treatments or actions applied to the dataset. This is for your archival record keeping (distinct from documentation the researcher(s) created to accompany their own datasets). DOCUMENT requires: 
- Recording all information relevant to the tracking and administration of the deposit, about who did what to the dataset and when 
- Tracking communication with the researcher(s)

### Key Ethical Considerations

- Document that disclosure risk review has taken place. State if changes from original data have been made, but do not give enough detail on changes to reverse-engineer any anonymization. 
- Include consent (or waiver) and/or IRB approval of sharing with administrative documentation. 
- Consider collecting contributor demographics.

### Essential Tasks

- [ ] Ensure the following information is captured in the Curator Log: 
  - [ ] Activities taken during the CURATE process 
  - [ ] Accessioning & deposit records (Names, dates, contact information, submission agreements, etc.) 
  - [ ] Repository collection metadata 
  - [ ] Provenance logs (changes by curators in the Transform step) 
  - [ ] Service workflow 
  - [ ] Correspondences and other interactions 
  - [ ] Preservation packaging 
  - [ ] Any additional requirements at your institution

:::
