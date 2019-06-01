# SOEP-Core datapackage pipeline

This repo is used for tests with frictionlessdata [datapackage pipelines](https://github.com/frictionlessdata/datapackage-pipelines).

## Acknowledgments
The data is taken from:
https://github.com/kwenzig/soep-core/tree/master/metadata


## Installation
### via pipenv
```bash
   $ git clone https://github.com/afuetterer/soep-core-datapackage-pipeline.git
   ...
   $ cd soep-core-datapackage-pipeline
   $ pip3 install pipenv
   ...
   $ export PIPENV_VENV_IN_PROJECT=1
   $ pipenv install
   ...
   $ pipenv shell
   Launching subshell in virtual environment…
 
```
## Usage

The pipeline is started via:
```bash
    (soep-core-datapackage) $ cd datapackage-pipeline/
    (soep-core-datapackage) $ dpp run ./soep-core
    ./soep-core: SUCCESS, processed 349 rows
    INFO    :RESULTS:
    INFO    :SUCCESS: ./soep-core {'bytes': 38402, 'count_of_rows': 349, 'dataset_name': 'soep-core', 'hash': '6f3d532691412a4f7e3578aa90761ea2'}

```
