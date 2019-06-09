import pytest
from unittest import mock
import builtins
import re


regex_pattern = r"M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"	# Do not delete 'r'.


def validating():
    return str(bool(re.match(regex_pattern, input(''))))




def test_substraction():
    with mock.patch.object(builtins, 'input', lambda _: 7, 7):
        assert subtraction_of_numbers() == 0


def test_product():
    with mock.patch.object(builtins, 'input', lambda _: 2, 2):
        assert product_of_numbers() == 4