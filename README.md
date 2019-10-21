# Cookiekaker Cookiecutter Data Science Template inspired by @vasinkd and @drivendata

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
├── LICENSE
├── Makefile           <- Makefile with commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
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
└── nets     <- Source code for nets and other stuff use in this project.
    ├── __init__.py    <- Makes {{cookiecutter.repo_name}} a Python module
    │    
    ├── settings.py <- illustrates how to use .env file
    │
    └── models         <- Scripts to train models and then use trained models to make
        │                 predictions
        └── train.py
```
