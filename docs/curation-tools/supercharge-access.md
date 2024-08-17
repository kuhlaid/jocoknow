---
sidebar_position: 6
---

# Supercharging access to a data repository

## Data repository searching

In 2024, data repositories are an effective choice for long-term storage, version control, and DOI preservation. However, they lack search functionality for specific variables within datasets. As a data curator, you want your users to be able to find out as much as possible about the data in your datasets before they download any of the data, and searching data dictionaries is part of the process.

To work around the data repository search deficiencies, we first need to consider a data repository with a solid API for working with our data within the repository. The National Institutes of Health lists Dataverse as a repository for general use, and it seems to have a fairly stable and functioning API, so we will focus on that repository going forward.

While we are not able to control the repository search behavior within the Dataverse platform, we might be able to use the API to our advantage. The API gives us the ability to retrieve our data programmatically. This is powerful because it allows for automation scripting and working with the data from predefined scripts.

As a web programmer I instinctively gravitated towards a solution involving a web application with a MongoDb or MySQL backend for storing copies of our data dictionaries. However, this can take a great amount of work to build and would not be a solution that general researchers would be able to set up themselves without the infrastructure to make it happen. No we do not want lack of infrastructure resources to be a barrier for researchers to adopt our solution for themselves.

### Possible solutions

#### Jupyter notebooks

Question: Could we use a Jupyter notebook to download a copy of the data dictionaries for the data repository community and build a dataset search?

Answer: Yes. This would be the most elegant and reusable design and would not require a complicated database setup or extra infrastructure. Other researchers could easily apply this to their projects.

#### The 'How'

How does a Jupyter notebook help us search data dictionaries? Well we could certainly use the built-in search of the notebook to search the files, but we can do a bit better than that. So we searched for existing plugins or modules that would allow the notebook to provide form elements, such as a search box and search button to submit a search request.

What we found was the `interactive-widgets.ipynb` notebook from https://ipywidgets.readthedocs.io/en/8.1.3/. There is a text field widget that we could use as our search box, and a `ipyvuetify` widget for a button to submit the search request. This sounds doable.