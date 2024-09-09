---
sidebar_position: 8
---

# Curation log considerations

When developing a curation log, you need to consider the format and workflow for creating the log. If you rarely curate data, then a simple text file may provide all the logging you need. However, will you work from a template or simply start from scratch? Do you want to know the order your steps were taken along with a timestamp of when they were completed? These are some things to consider before starting your log.

## Log format

The preferred format for the curation log is JSON or something similar, using a standard schema across datasets, to facilitate running checks against the log with scripts to verify completeness of all elements. JSON format allows you to treat your curation log as you would a database, with defined fields such as step id and decisions array. You can then build a simple program that lets you choose a curation step from a curation log template and then enter decisions or responses to that step. Your program then would add your responses to a JSON file. Taking it further your program could also parse you JSON response file and generate a Markdown file that could be used to document your curation log in a simplified user view.

## Possible workflow

We can use a Jupyter notebook to read a curation log JSON template file and generate a dataset curation log based on the template and responses from the curator. The template will never have data directly added to it. For example, a Python script could loop through the list of steps outlined in the curation template and if a value is empty then prompt the curator for an answer. An alternative could be that the user can select an item from the checklist and log an entry for that checklist category. As the data curation process progresses, steps can be shifted around as needed in the curation template if it seems more appropriate for a given set of data. The generated curation log would be created as answers to the steps in the template are answered. The template checking scripts will not care about the order of the curation steps, only that steps are completed or labeled `NA` or some other appropriate response.

Later you could parse the JSON responses to either show them in the order they were completed or organize them by the checklist order. Having the data in JSON format allows for flexibility later for displaying and ordering the data as needed.

## Curation checklist reference

```json
{
    "about": "This is a data curation checklist reference derived from DCN CURATE(D) steps for data curation. Each step is labeled with an identifier to link the steps to the action associated with the step. This reference will be used to create the curation log for a dataset.",
    "type": "CurationChecklistReference",
    "steps": [
        {
            "check": [
                {
                    "id": "c1",
                    "name": "Begin Curator Log to track curation decisions"
                },
                {
                    "id": "c2",
                    "name": "Open the related article and supporting information if available"
                },
                {
                    "id": "c3",
                    "name": "Inventory the dataset",
                    "steps": [
                        {
                            "check": [
                                {
                                    "id": "c4",
                                    "name": "Identify file formats"
                                },
                                {
                                    "id": "c5",
                                    "name": "Review file organization, hierarchy, and naming convention(s)"
                                },
                                {
                                    "id": "c6",
                                    "name": "Extract zip files when possible"
                                }
                            ]
                        }
                    ]
                },
                {
                    "id": "c7",
                    "name": "Create working copy of files for formal inventory and testing"
                },
                {
                    "id": "c8",
                    "name": "Examine code for obvious errors/missing components, etc."
                },
                {
                    "id": "c9",
                    "name": "Check that metadata quality is rich, accurate, and complete to institutional requirements."
                },
                {
                    "id": "c10",
                    "name": "Check documentation type (circle or specify one) -- README / Codebook / Data Dictionary / Other"
                }
            ],
            "understand": [
                {
                    "id": "u1",
                    "name": "Examine files, organization, and documentation more thoroughly"
                }
            ]
        }
    ]
}
```



## Curation log example (with data)

The following curation log uses the checklist reference above to document steps taken and decisions made.

```json
{
  "about": "This document logs the steps and transformations (if any) to the dataset during the curation process.",
  "datasetSelected": "1457",
  "datasetDescription": "JoCoHS E03 Ultrasound image reference data for machine learning",
  "startDate": "2024-08-27",
  "endDate": "",
  "curator": [
    {
      "name": "w. Patrick Gale"
    }
  ],
  "CurationLog": {
    "steps": [
        {
            "id": "c1",
            "response": [
              {"desc":"",
              "date":"[timestamp]"}
            ]
        }
    ]
  },
  "ProvenenceLog": {
    "transformations":[]
  }
}
```

