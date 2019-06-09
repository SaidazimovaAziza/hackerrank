import re
import pytest
from unittest import mock
import builtins

regex_integer_in_range = r"^[1-9][0-9]{5}$"	# Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"(?<=(\d)\d)\1"	# Do not delete 'r'.


def validating_postal_code():
    P = input('')
    return bool(re.match(regex_integer_in_range, P) and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)


def test_validating_postal_code_1():
    with mock.patch.object(builtins, 'input', lambda _: '110000'):
        assert validating_postal_code() == False


def test_validating_postal_code_2():
    with mock.patch.object(builtins, 'input', lambda _: '111456'):
        assert validating_postal_code() == True


def test_validating_postal_code_3():
    with mock.patch.object(builtins, 'input', lambda _: '101201'):
        assert validating_postal_code() == True