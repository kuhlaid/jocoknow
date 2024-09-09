---
sidebar_position: 9
---

# Testing our technology

When beginning this project, we needed to consider the technologies used in the implementation of our processes. Patrick Gale is our technology expert and his experience with developing application integration processes led him to choose the tools outlined in our [approach](/docs/jocoknow-basics/approach.md).

## Reviewing the repository API

One of the requirements we set in choosing a data repository was ensuring the data deposit and retrieval could be automated efficiently. 

### Dataset creation and file ingest

Going into this project we knew a large number of datasets with similar structure and metadata would be generated for our data repository. Manually slogging through a GUI interface clicking on buttons to create a dataset, then filling out a long form and probably forgetting one of the key fields in the process, then trying to manually select files to upload and clicking upload buttons, then selecting the review link... Manually doing these tasks can easy take hours to process one dataset. Automating this process can bring that time down to seconds.

While we are still talking manual processes, trying to provide others with instructions for reproducing your process using a GUI is nearly impossible. The interface is always changing and no one ever updates the documentation, so users are simply lost. Not to mention differences in user displays and devices which can change the UI entirely from user to user. Reproducibility through manual processes is highly error prone and leads to quality assurance questions.

We wanted to standardize the process with reproducible steps not simply for ourselves but for anyone else who wanted to utilize our methods. To do this we created a Jupyter notebook with Python scripts to test the API endpoints we would be using for data ingest (found at https://github.com/kuhlaid/dv-api-test). This notebook serves several purposes:

- It does not require someone to manually try to set up a Python environment (which is a pain even for developers and likely a non-starter for those not familiar with Python).
- It can be easily run from a free cloud platform such as Google Colab, so only requires a web browser.
- It is plain text so it is an accessible coding environment.
- It allows us to abstract much of the convoluted data repository API processes to make API use much more accessbile to non-coders.

### The core Dataverse ingest code


We also developed a simple but effective Python package (https://github.com/kuhlaid/DvApiMod5.13) used with the API testing notebook; simplifing many of the processes needed to test