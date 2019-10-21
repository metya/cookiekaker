# Cookiecutter Cookiekaker Data Science Template inspired by @vasinkd and @drivendata

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
- May choose python3.5, python3.6, python3.7, python3.8


- Creation of virtual envronment is limited to virtualenv.
- Creation of virtual envronment also sets up git vcs and dvc vcs and pre-commit hooks
- Project library renamed from src to project_name which lets you use the created library on your machine from anythere
- Added pipeline folder to store all dvc pipelines there
- Added data/features folder
- Added settings.py to illustrate how to use .env file
- Added an empty noteboook "1.0-{{cookiecutter.author_name}}-dvc-pipeline.ipynb" to store all dvc pipelines creation commands and to illustrate that numeration of notebooks is a good idea
- Cleared make_dataset.py since I find it too restrictive and confusing
- Removed aws sync functions
- Removed data folder from .gitignore since dvc version control takes care of .gitignore
- Removed tox.ini since .pre-commit.yaml is enough for me

### The resulting directory structure
------------

The directory structure of your new project looks like this:

```
├── LICENSE
├── Makefile           <- Makefile with commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   ├── features       <- Features may be stored here
│   ├── inference      <- Inference stages may be stored here
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default Sphinx project; see sphinx-doc.org for details
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── .pre-commit-config.yaml <- Stores pre-commit settings
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── __init__.py
│
└── <project_name>     <- Source code for use in this project.
    ├── __init__.py    <- Makes {{cookiecutter.repo_name}} a Python module
    │    
    ├── settings.py <- illustrates how to use .env file
    │
    ├── data           <- Scripts to download or generate data
    │   └── make_dataset.py
    │
    ├── features       <- Scripts to turn raw data into features for modeling
    │   └── featurize.py
    │
    └── models         <- Scripts to train models and then use trained models to make
        │                 predictions
        └── train.py
```
