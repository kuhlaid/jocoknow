---
sidebar_position: 3
---

# Our approach to JoCoKnow

## Determining the technology

The key requirements for our technology choices are open source, FAIR principles of use, strong community support of the technology, and automation capable. Patrick Gale is an expert in the following technologies that were chosen for our approach to the implementation of this project.

### Dataverse data repository and archive

Patrick has reviewed and tested various data repository software for years, but the Dataverse most extensively since UNC hosts and supports a local installation of the software and Patrick's work with the developers of the software at Harvard University. Our approach to using the Dataverse is primarily through the software API to enable automated deposit and retrieval of data. The automation allows for reuse of scripts, when combined with the management of large numbers of datasets becomes a necessity for efficiency and quality control.

### Data table and metadata file formats 

As we outline in our long-term preservation plan, the use of plain formatted text files is the primary focus of our data preservation efforts. Storing our data tables and metadata within these formats ensures accessibility across operating systems and computing environments. 

Our metadata will utilize JSON formatted text which is a simple text format widely used by software developers and researchers in general. Whether JSON is used for codebooks or data dictionaries, it allows for automated validation and linking of data their data descriptors. JSON is also the format of Jupyter notebooks which we will discuss next. 

### Jupyter notebook scripting framework

This is likely the best tool to have in your data curation toolbox. A Jupyter notebook is not only the visual eye candy for representing your metadata, but it provides you with the tools to download and work with much of the data. This is significant because we can run data analyses from within the notebook and save the results and notes from those analyses within a single file. The best thing about these notebooks is they are JSON formatted (you will notice we talk at great lengths about JSON in this proposal). In our KG and data repository, we will provide notebook examples and best practices and demonstrate the power of these notebooks.

### Docusaurus documentation framework

Docusaurus is a popular open-source tool for documentation. We will use this as our KG website framework since it is easy to manage and publish online since it does not require a database. The documentation will be written in plain text Markdown format. 

### GitHub code repository

We plan to use GitHub as our main public repository for our KG. GitHub allows for quick automated builds to a hosting service such as Vercel, and GitHub is a leader in code repository hosting and a familiar resource for developers. We will archive a copy of the KG to the data repository for long term storage/archiving and citation. GitHub also improves our outreach efforts through their repository discussion and issue boards. 