---
sidebar_position: 4
---
  
# Data dictionaries

A data dictionary is usually the last thing on a researcher's mind when publishing data. Not only because there are few data collecting platforms that take data dictionaries into consideration as output for a data collection instrument, but they are not standardized. And the only reason you need a data dictionary is if you need someone else to understand your data. When you are beginning data collection, you are the creator of your data instrument, so you know what you are collecting. But when the data is finally retrieved from the instrument, do your variable names look like Q1, Q3, Q34? What do those names represent?

## Vocabularies

When we describe something, we usually assume the recipient of our message will understand the words we are using. But sometimes the terms we use can be ambiguous or hold meaning beyond what we intended. The same holds for research data. We assume whatever research data we receive from our data instrument will make sense to those who know how to interpret it. Why even bother describing it further and just wait until someone asks for additional information?

Since 1986, the Unified Medical Language System (UMLS) has sought to help computer systems link biomedical information together. We will adopt the UMLS Metathesaurus https://uts.nlm.nih.gov/uts/umls/home to help describe variables in our datasets. For example, the concept of `ultrasound of left knee` https://uts.nlm.nih.gov/uts/umls/concept/C2322105 and possibly the corresponding hierarchy/tagging `MEDCIN > tests > imaging studies > ultrasound studies > nonvascular ultrasound of extremity` for metadata uses (using the UMLS API to and create examples on how to work with the API and our data https://documentation.uts.nlm.nih.gov/rest/home.html).

## dvDatasetMetadata.json metadata

Data curators should have a metadata file to describe their dataset and that metadata is best stored in JSON format. Below is an example of the README object for a dataset, and the file will be named `dvDatasetMetadata.json` for consistency. This file will contain the metadata (data dictionary included) for the dataset and is formatted using JSON (https://www.json.org/). JSON is preferred because it is simple formatted text that we can easily work with in our scripts. We will import this file into a Jupyter notebook to provide users with the data descriptors to validate the data (which you can read more about under the [Juptyer notebook section](jupyter-notebook.md) of our guides).

The purpose of this file is to allow researchers to either read or query this file to gain a general understanding of the dataset and contents without needing to download the data and analyze it. **NOTE: we are not adding every possible property someone can come up with for this object, but only the properties that are most useful to our end-users.**

The first property of the README object will be the `metadata` object that describes our dataset (dataset title, citations, funders, etc.). We are specifically not using property names from a standard format such as DataCite in this context because the repository API is expecting different property names. The metadata properties we use will match those that the repository expects through the API. We can then simply use the object to initialize our dataset programmatically. Once the metadata has been imported into the repository, users can download the metadata in the format they choose (e.g. DataCite, Dublin Core, etc.).

Another thing to note is our `dvDatasetMetadata.json` can be comprised of not only data we know up front about the data, but also data that can be inferred from any analysis we run against the data. For example, we likely want to include basic statistical features in our `dvDatasetMetadata.json` to describe the dataset total observations (N), and possibly more fine-grained observations for categorical values in our variables. We will use scripts to generate the observations of our data and can then automatically insert them into the `dvDatasetMetadata.json` since we want this same functionality across our datasets.

:::tip

**Note: The metadata elements for the deposition/deposit should match API element names of the repository. We then use this README file to initialize our dataset.**

:::

:::note

Some elements such as DOI can be automatically added to the README file once the dataset is initialized through the API scripts if we wanted to include it.

:::

The following is the content of a `dvDatasetMetadata.json` file which describes properties of the dataset. We will later use this file to generate a `README` file to describe the dataset in a more human readable format.

```s JSON
{
    "about": "This document describes our dataset and can be thought of as the database for understanding our data. We recommend reviewing the Jupyter notebook `notebook.ipynb` file that accompanies this dataset. The notebook parses this file into sections, tables, and figures that can be quickly read to understand the dataset.",
    "metadata": {
        "title": "Development of an AI/ML-ready knee ultrasound dataset in a population-based cohort",
        "description": "<h1>About this data</h1>An ultrasound dataset to use in the discovery of ultrasound features associated with pain and radiographic change in KOA is highly innovative and will be a major step forward for the field. These ultrasound images originate from the diverse and inclusive population-based Johnston County Health Study (JoCoHS). This dataset is designed to adhere to FAIR principles and was funded in part by an Administrative Supplement to Improve the AI/ML-Readiness of NIH-Supported Data (3R01AR077060-03S1).",
        "access_right": "open",
        "prereserve_doi": true,
        "language": "eng",
        "license": "mit",
        "communities": [{"identifier":"jocoknow"}],
        "upload_type": "dataset",
        "creators": [
            {
                "name": "Gale, w. Patrick",
                "affiliation": "University of North Carolina at Chapel Hill"
            }
        ]
    },
    "dataTypes": [
        "survey",
        "ultrasound image",
        "radiographic reads"
    ],
    "softwareUsed": [
        "Qualtrics survey platform",
        "MySQL database",
        "Docker Desktop",
        "Jupyter notebook",
        "Python"
    ],
    "files": [
        {
            "dataTable.csv": {
                "description": "The data table for our dataset.",
                "encoding": "UTF-8",
                "variables": [
                    {
                        "name": "E03SUBJECTID",
                        "label": "A unique identifier for a subject in a study.",
                        "statistics": {
                            "N": 123
                        },
                        "value": {
                            "format": "Universal Unique Identifier (UUID v4)",
                            "dataType": "string (36 character)",
                            "unique": true
                        },
                        "identifier": true,
                        "required": true,
                        "ontology": {
                            "source": [
                                "https://ncit.nci.nih.gov/ncitbrowser/ConceptReport.jsp?dictionary=NCI_Thesaurus&ns=ncit&code=C69256"
                            ]
                        }
                    },
                    {
                        "name":"QID3",
                        "description": "What is your body weight?",
                        "type": "numeric",
                        "ontology": {
                            "concept": {
                                "source": "UMLS",
                                "uri": "https://uts.nlm.nih.gov/uts/umls/concept/C0005910",
                                "code": "C0005910"
                            },
                            "atom": {
                                "name": "body weight",
                                "source": "CSP",
                                "code": "0467-2841",
                                "uri": "https://uts.nlm.nih.gov/uts/umls/vocabulary/CSP/0467-2841",
                                "heirarchy": ["CRISP Thesaurus","anatomy","morphology","body physical characteristic"]
                            }
                        },
                        "required": false,
                        "statistics": {
                            "N": 123
                        }
                    },
                    {
                        "name":"QID97",
                        "description": "Are you able to leap buildings in a single bound?",
                        "type": "categorical",
                        "categories": {
                            "1": "Yes",
                            "2": "No",
                            "3": "Maybe",
                            "88": "No response"
                        },
                        "statistics": {
                            "N": 123
                        },
                        "required": true
                    }
                ]
            }
        }
    ],
    "dataCollectionStart": "2020-09-09",
    "dataCollectionEnd": "2024-02-25",
    "internalReferenceId": "1450"
}
```

## Validation

Once we have created a `dvDatasetMetadata.json` file, we can begin creating the validation scripts we will use to validate it against our data table. Now there is no perfect/standard way to do this, so we will explain our ideal method.

One of the main things we want to do is create a validation copy of our `dataTable.csv` file using the categorical labels we defined for the variables in our `dvDatasetMetadata.json` file. This is especially true if our data was generated from a paper form or some method where the answer categories and labels are not mapped for us automatically in our data exports and we were forced to manually enter them into the `dvDatasetMetadata.json` file. If you collect data using RedCAP or Qualtrics for example, these category labels and values are provided to you automatically, so there is no need to manually create them.

The main purpose of our `dvDatasetMetadata.json` file is to ensure we have described all the variables and features found within our `dataTable.csv`. We will provide Python scripts that read the variable names and data from the `dataTable.csv` file and compare it to what we have defined in our `dvDatasetMetadata.json` file. Some features of our `dvDatasetMetadata.json` can be auto-generated from our `dataTable.csv` file, in which case the properties should match up. Our validation will answer questions such as 'are all variables described in the `dvDatasetMetadata.json`' and do the variable properties match the data in the `dataTable.csv`.

We create a separate Jupyter notebook for data curation (data repository import) that runs validation checks on the data and metadata. We create a second Jupyter notebook that is from the end-user perspective (data repository export) and is included in our public dataset repository. This second notebook is used to export the data via the API, to run the same validation checks we ran before the data was imported (to verify there was no data corruption during import), and to validate again against our `dvDatasetMetadata.json`.

Next we will discuss the use of schemas to define a consistent template for our `dvDatasetMetadata.json` file.

## Schemas

Now that we have created our main `dvDatasetMetadata.json` file and made any necessary changes to it, we should consult with your stakeholders and advisory board to verify that we are presenting useful information in our metadata file. We will then make analyze and requested changes and return to the previous steps in creating and validating the `dvDatasetMetadata.json` file. Next we can consider a JSON schema to describe our `dvDatasetMetadata.json` file.

What is the usefulness of JSON schemas? A JSON schema is very useful when descriptions and required fields need to be known. We have written a Jupyter Notebook that demonstrates our methods for embedding a schema into JSON data and using that schema to validate the JSON data at https://gist.github.com/kuhlaid/7117c814957c574e001f0a548ee846a1.


## The ideal world

In most cases, data dictionaries are most universally accessible and useful in JSON format. The reason for this is that dictionaries describing a data file are usually complex objects, involving variable descriptions, statistics, requirements, exceptions, and variable categories. JSON allows you to represent each of these objects in a single file since JSON properties can contain endless numbers of objects. And most importantly, JSON allows for easy access to these objects when scripting ways to work with and describe the data output.

