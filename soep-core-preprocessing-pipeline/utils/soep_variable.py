import re
from string import ascii_lowercase

QUESTION_IN_VARIABLE_NAME_REGEX = re.compile(r"^[a-z]*([0-9]{2})")
INSTRUMENT_IN_VARIABLE_NAME_REGEX = re.compile(r"^([a-z]{1,2})([hp])")
YEAR_LETTERS = list(ascii_lowercase) + [f"b{char}" for char in list("abcdefghijklm")]
SOEP_FIRST_YEAR = 1984
INSTRUMENT_TYPES = {"p": "pe", "h": "hh"}


def determine_question(variable_name: str):
    """returns a question number for a given SOEP variable

    :param variable_name: Variable name using SOEP schema
    :type variable_name: str
    :return: question id (int)

    none otherwise

    :Example:
    >>> import soep_variable
    >>> soep_variable.determine_question("bbpbbil02")
    2
    """
    try:
        question = QUESTION_IN_VARIABLE_NAME_REGEX.match(variable_name).group(1)
        return int(question)
    except AttributeError:
        return None


def determine_instrument(variable_name: str):
    """returns an instrument name for a given SOEP variable

    :param variable_name: Variable name using SOEP schema
    :return: instrument_name (str)

    none otherwise

    >>> import soep_variable
    >>> soep_variable.determine_instrument("apbbil01")
    soep-core-1984-pe
    """
    try:
        year_letter = INSTRUMENT_IN_VARIABLE_NAME_REGEX.match(variable_name).group(1)
        instrument_type = INSTRUMENT_IN_VARIABLE_NAME_REGEX.match(variable_name).group(
            2
        )
        instrument_type = INSTRUMENT_TYPES[instrument_type]
        year = YEAR_LETTERS.index(year_letter) + SOEP_FIRST_YEAR
        return f"soep-core-{year}-{instrument_type}"
    except (AttributeError, ValueError):
        return None
