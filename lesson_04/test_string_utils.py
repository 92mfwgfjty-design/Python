import pytest
from string_utils import StringUtils


string_utils = StringUtils()


# CAPITALIZE

@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
    ("123", "123"),
    ("04 апреля 2023", "04 апреля 2023"),
    ("", ""),
    ("   ", "   "),
    ("HELLO", "Hello"),
])
def test_capitalize(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


# TRIM

@pytest.mark.parametrize("input_str, expected", [
    ("   skypro", "skypro"),
    ("  hello world", "hello world"),
    ("python", "python"),
    ("123", "123"),
    ("04 апреля 2023", "04 апреля 2023"),
    ("", ""),
    ("   ", ""),
    ("  123  ", "123  "),
])
def test_trim(input_str, expected):
    assert string_utils.trim(input_str) == expected


# CONTAINS

@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "S", True),
    ("SkyPro", "U", False),
    ("hello world", "world", True),
    ("123", "2", True),
    ("04 апреля 2023", "апреля", True),
    ("", "a", False),
    ("   ", "a", False),
    ("SkyPro", "sky", False),
])
def test_contains(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected


# DELETE_SYMBOL

@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "k", "SyPro"),
    ("SkyPro", "Pro", "Sky"),
    ("banana", "a", "bnn"),
    ("hello world", "l", "heo word"),
    ("123456", "3", "12456"),
    ("04 апреля 2023", " ", "04апреля2023"),
    ("SkyPro", "X", "SkyPro"),
    ("", "a", ""),
    ("   ", " ", ""),
])
def test_delete_symbol(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected


# NEGATIVE TESTS: NONE

@pytest.mark.parametrize("method, args", [
    ("capitalize", (None,)),
    ("trim", (None,)),
    ("contains", (None, "a")),
    ("delete_symbol", (None, "a")),
])
def test_methods_with_none(method, args):
    with pytest.raises(AttributeError):
        getattr(string_utils, method)(*args)
