{{cookiecutter.project_name}}
==============================

{{cookiecutter.description}}

Project Organization

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