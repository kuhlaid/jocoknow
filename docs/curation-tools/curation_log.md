---
sidebar_position: 8
---

# Curation log format

The preferred format for the curation log should be JSON, using a standard schema across datasets, to facilitate running checks against the log with scripts to verify completeness of all elements.

## Workflow

We can use a Jupyter notebook to read a curation log JSON template file and generate a dataset curation log based on the template and responses from the curator. The template will never have data directly added to it. For example, a Python script could loop through the list of steps outlined in the curation template and if a value is empty then prompt the curator for an answer. As the data curation process progresses, steps can be shifted around as needed in the curation template if it seems more appropiate for a given set of data. The generated curation log would be created as answers to the steps in the template are answered. The template checking scripts will not care of the order of the curation steps, only that steps are completed or labeled `NA` or some other appropriate response.

## Curation checklist reference

```json
{
    "about": "This is a data curation checklist reference derived from DCN CURATE(D) steps for data curation. Each step is labeled with an identifier to link the steps to the action associated with the step. This reference will be used to create the curation log for a dataset.",
    "type": "CurationChecklistReference",
    "steps":[
        {
            "check":[
                {
                "id":"c1",
                "name": "Begin Curator Log to track curation decisions"
                }
            ],
            "understand":[
                {
                "id":"u1",
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
            "checked": "yes",
            "decision": []
        }
    ]
  },
  "ProvenenceLog": {
    "transformations":[]
  }
}
```