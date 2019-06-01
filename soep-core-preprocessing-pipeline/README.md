# SOEP-Core preprocessing pipeline

This repository shows the preprocessing steps done within *ddi.py* and *soep-core/lib_py/fill_ddionrails.py*

## Requirements

- git
- python 3.6

```bash
   $ python3 --version
   Python 3.6.5
```

## Installation
### via pipenv
```bash
   $ git clone https://github.com/afuetterer/soep-core-preprocessing-pipeline.git
   ...
   $ cd soep-core-preprocessing-pipeline
   $ pip3 install pipenv
   ...
   $ export PIPENV_VENV_IN_PROJECT=1
   $ pipenv install
   ...
   $ pipenv shell
   Launching subshell in virtual environment…
```
### via virtualenv and pip
```bash
   $ git clone https://github.com/afuetterer/soep-core-preprocessing-pipeline.git
   ...
   $ cd soep-core-preprocessing-pipeline
   $ python3.6 -m venv .venv
   $ source .venv/bin/activate
   (.venv) $ pip install --upgrade pip wheel
   (.venv) $ pip install -r requirements.txt
```

## Usage

The pipeline is started via:
```bash
    (soep-core-preprocessing-pipeline) $ python pipeline.py
```

## Tests

Tests are run via:
```bash
    $ pipenv install --dev
    ...
    $ pipenv shell
    ...
    (soep-core-preprocessing-pipeline)$ pytest
```


## Acknowledgments
These other SOEP repositories are used and modified in this context: 
- ddi.py (https://github.com/ddionrails/ddi.py)
- SOEP-Core (https://github.com/kwenzig/soep-core)