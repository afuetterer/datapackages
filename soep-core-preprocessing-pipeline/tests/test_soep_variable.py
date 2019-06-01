import pytest

from utils import soep_variable


testdata = [
    ("akmup", None),
    ("apbbil01", 1),
    ("zp5501", 55),
    ("isced11_10", 11),
    # ("bbp12302", 123),
]

@pytest.mark.parametrize("input,expected", testdata)
def test_determine_question(input, expected):
    output = soep_variable.determine_question(input)
    assert output == expected


testdata = [
    ("akmup", None),
    ("apbbil01", "soep-core-1984-pe"),
    ("zp5501", "soep-core-2009-pe"),
    ("bah7106", "soep-core-2010-hh")
]

@pytest.mark.parametrize("input,expected", testdata)
def test_determine_instrument(input, expected):
    output = soep_variable.determine_instrument(input)
    print(input, output)
    assert output == expected