import pytest
from unittest import mock
import builtins


def is_leap_year():
    year = int(input(''))
    leap = False
    if year % 4 == 0:
        leap = True
        if year % 100 == 0:
            leap = False
    if year % 400 == 0:
        leap = True
    return leap

def test_leap():
    with mock.patch.object(builtins, 'input', lambda _: "1990"):
            assert is_leap_year() == False
