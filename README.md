# Cookiekaker Deep Learning Template inspired by @vasinkd and @drivendata

_A not quite logical, nad unreasonably standardized, but flexible project structure for doing and sharing data science work at certain motivation and place._

Cookiecutter Data Science is a real game changer for data science projects. I use it, but change many things, because, you know, automotization!

I made several tweaks on base of drivendata template which helps me to improve my working routine.

__HOW TO USE:__

First of all, install cookiecutter with:
```bash
$ pip install cookiecutter
```
or
```bash
$ conda install cookiecutter
```
or 
```bash
$ apt install cookiecutter
```
After that you can use template with:
```bash
$ cookiecutter https://github.com/metya/cookiekaker
```

__Features:__
- Creation of virtual envronment is limited to virtualenv.
- Creation of virtual envronment also sets up git vcs and dvc vcs and pre-commit hooks
- Good sturcture of folders from SOTA projects

### The resulting directory structure
------------

The directory structure of your new project looks like this:

```

│   .pre-commit-config.yaml <- Stores pre-commit settings
│   LICENSE
│   Makefile                <- Makefile with commands like `make data` or `make train`
│   README.md               <- The top-level README for developers using this project.
│   requirements.txt        <- The requirements file for reproducing the analysis environment, e.g.
│   setup.py                
│   test_environment.py
│   tox.ini                <- tox file with settings for running tox; see tox.testrun.org
│   __init__.py
├───app                    <- Folder for wrapper, api, applications and other buisness stuff
│       api.py
│       app.py
│       main.py
│       __init__.py
├───data                    <- Folder to store data
│   │   README.md           <- Desription about data 
│   ├───processed           <- The final, canonical data sets for modeling.
│   └───raw                 <- The original, immutable data dump.
│       ├───external        <- Data from third party sources.
│       └───interim         <- Intermediate data that has been transformed.
├── docs                    <- A default Sphinx project; see sphinx-doc.org for details
├───logs                    <- To store logs from for example tensorboard
├── models                  <- Trained and serialized models, model predictions, or model summaries
├── notebooks               <- Jupyter notebooks. Naming convention is a number (for ordering),
│                           the creator's initials, and a short `-` delimited description, e.g.
│                           `1.0-jqp-initial-data-exploration`.
├── references              <- Data dictionaries, manuals, and all other explanatory materials.
├── reports                 <- Generated analysis as HTML, PDF, LaTeX, etc.
│   ├───figures             <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └───images              <- Images for reports
└───{{ cookiecutter.repo_name }}<- Source code for use in this project.
    │   settings.py         <- illustrates how to use .env file
    │   __init__.py         <- Makes {{cookiecutter.repo_name}} a Python module
    ├───nets                <- Code of your models and nets
    │       nets.py         <- Nets
    │       predict.py      <- Evaluation sctript
    │       train.py        <- Train script
    │       __init__.py
    ├───pipelines           <- To store dvc pipelines
    ├───utils               <- Different utils functions
    │       featurize.py    <- To create features of dataset
    │       make_dataset.py <- To create final dataset
    │       utils.py        <- Different helpers
    │       __init__.py
    └───visualization       <- To visualize stuff
            visualization.py
            __init__.py
```
