---
sidebar_position: 2
---

# Curation tools

There are free tools available for curating data. Below are some of the tools we use to curate this project.

## Data curation lifecycle

At the broadest level we will utilize the data curation lifecycle model from https://www.dcc.ac.uk/sites/default/files/documents/publications/DCCLifecycle.pdf

## Workflows

The https://datacurationnetwork.org/outputs/workflows/ provides a useful workflow framework to ensure that all datasets submitted to a repository are processed consistently. We utilize the "Checklist of CURATED Steps Performed by the Data Curation Network, v.1"

## Repositories

Data repositories should implement an API for automated curation and retrieval of data for quality assurance.

## File naming

There is no single correct way to handle file naming, but we prefer to stick with simple consistent names in similar files across our datasets for data import. So all of our README metadata files will be named `README.json` and our main data table files will be named `dataTable.csv`. This way we can write automated processes that do not need to be rewritten or modified between datasets. 

The distinction should be made that while we use a common name for similar files across datasets for data import, scripted data export via the repository API can provide renaming of the files to be distinct to a dataset before analyzing. For example, the `dataTable.csv` file could be exported as `[datasetPrefix].dataTable.csv` or `studyT3.anthropometry.dataTable.csv`, although it is not recommended for scripting efficiency as we mentioned with the data import.

:::danger
Do not save your files to a repository without a file extension. The file extension should never be assumed.
:::

## Data persistence

In general data is likely reviewed by the repository every 10 years at the least to ensure that data stored within is being used. If data is not used for 10 years then it likely does not contain anything useful and should be considered for disposal.

## Missing pieces

Many open repositories such as Dataverse have no way of linking data from datasets together. For instance, if you are only interested in finding datasets with variables for `height` or `weight`, there is no way for the dataset search to look in the dataset files to find those variables. The only searchable components of the dataset are the general descriptions of the dataset such as dataset title, general description, dataset tags, etc. There is no way to expand the dataset metadata to include the data dictionary, so we can search on the data dictionary data.

See [supercharge data access](supercharge-access.md) for a solution to this data dictionary search problem.

## Advisory board

To complement the CURATED checklist, there needs to be a clear group of individuals (and roles) associated with steps in the curation process.

## Data deposit

Now we will get into how to initialize a dataset in Dataverse using the API and Python scripts. In the [README.json](data-dictionary.md#readmejson) section where we described the data dictionary, now we will see how the metadata used to create our dataset.