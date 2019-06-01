import os
import pandas as pd

from ddi.onrails.repos import dor1
from ddi.onrails.repos import copy
from ddi.onrails.repos import convert_r2ddi
from ddi.onrails.repos import topics

from utils import soep_variable
from utils import merge_instruments
from utils.sparse_checkout import sparse_checkout


# This mapping is used in multiple tasks to rename columns in a dataframe
COLUMN_MAPPING = {
    "study": "study_name",
    "dataset": "dataset_name",
    "period": "period_name",
    "analysis_unit": "analysis_unit_name",
    "conceptual_dataset": "conceptual_dataset_name",
    "varname": "variable_name",
    "concept": "concept_name"
}


def lowercase_column_contents(df, pattern):
    """ Modifies content of all dataframe columns where column name contains
        'pattern'.
        If
            cell contains a string => lower case
        else:
            cell contains any other type => do not modify
    """
    temp = df.filter(like=pattern).applymap(
        lambda s: s.lower() if type(s) == str else s
    )
    df.update(temp)


def datasets(inpath, outpath):
    """ Reads a csv file,
        renames columns
        lowercases string content of all "_name" columns
        writes to csv
    """
    df = pd.read_csv(inpath)
    df.rename(columns=COLUMN_MAPPING, inplace=True)
    lowercase_column_contents(df, pattern="_name")
    df.to_csv(outpath, index=False)


def variables(inpath, outpath):
    """ Reads a csv file,
        renames columns
        drop duplicate rows
        lowercases string content of all "_name" columns
        writes to csv
    """
    df = pd.read_csv(inpath)
    df.rename(columns=COLUMN_MAPPING, inplace=True)
    UNIQUE_COLUMNS = ("study_name", "dataset_name", "variable_name")
    # Drop rows, if two or more rows have the same values in UNIQUE_COLUMNS
    df.drop_duplicates(subset=UNIQUE_COLUMNS, inplace=True)
    lowercase_column_contents(df, pattern="_name")
    df.to_csv(outpath, index=False)


def questions_variables(inpath, outpath):
    """ Reads a csv file,
        based on variable name determines question_name and instrument_name
        add two columns
        drop invalid rows (containing nans)
        writes to csv
    """
    COLUMNS = ("study_name", "dataset_name", "variable_name")
    df = pd.read_csv(inpath, usecols=COLUMNS)
    df["question_name"] = df["variable_name"].apply(soep_variable.determine_question)
    df["instrument_name"] = df["variable_name"].apply(soep_variable.determine_instrument)
    df.dropna(inplace=True)
    df['question_name'] = df['question_name'].astype('int')
    df.to_csv(outpath, index=False)


def concepts(inpath, outpath):
    """ Reads a csv file,
        renames columns
        drop duplicate rows
        lowercases string content of all "_name" columns
        writes to csv
    """
    df = pd.read_csv(inpath)
    df.rename(columns=COLUMN_MAPPING, inplace=True)
    UNIQUE_COLUMNS = ("concept_name", )
    # Drop rows, if two or more rows have the same values in UNIQUE_COLUMNS
    df.drop_duplicates(subset=UNIQUE_COLUMNS, inplace=True)
    lowercase_column_contents(df, pattern="_name")
    df.to_csv(outpath, index=False)


def main():
    """ Master script calls other tasks in pipeline
    """

    # make sure ddionrails directory exists
    try:
        os.mkdir("ddionrails")
    except FileExistsError:
        pass

    # make a sparse checkout from knut's version of the soep-core repository
    # This takes really long the first time
    sparse_checkout("soep-core", "https://github.com/kwenzig/soep-core", paths=("metadata", "r2ddi/v33"))
    copy.study(inpath="soep-core/metadata/study.md", outpath="ddionrails/study.md")
    copy.bibtex(inpath="soep-core/metadata/bibtex.bib",
                outpath="ddionrails/bibtex.bib",
                input_format="latin1")
    concepts("soep-core/metadata/concepts.csv", "ddionrails/concepts.csv")
    datasets("soep-core/metadata/datasets.csv", "ddionrails/datasets.csv")
    variables("soep-core/metadata/variables.csv", "ddionrails/variables.csv")
    questions_variables("ddionrails/variables.csv", "ddionrails/questions_variables.csv")

    # This step takes some time
    convert_r2ddi.Parser("soep-core", r2ddi_path="soep-core/r2ddi", version="v33").write_json()
    merge_instruments.main()
    # TODO
    # topics.Topic.import_all()


if __name__ == "__main__":
    main()
