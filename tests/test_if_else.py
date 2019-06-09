import pytest
from unittest import mock
import builtins

def check_for_weird_or_not_weird():
    number = int(input(''))
    result = ""
    if number % 2 == 1:
        result = "Weird"

    else:
        if 2 <= number <= 5:
            result = "Not Weird"

        if 6 <= number <= 20:
            result = "Weird"

        if number > 20:
            result = "Not Weird"
    return result


def test_solve_1():
    with mock.patch.object(builtins, 'input', lambda _: 2):
        assert check_for_weird_or_not_weird() == 'Not Weird'


def test_solve_2():
    with mock.patch.object(builtins, 'input', lambda _: 3):
        assert check_for_weird_or_not_weird() == 'Weird'


def test_solve_3():
    with mock.patch.object(builtins, 'input', lambda _: 4):
        assert check_for_weird_or_not_weird() == 'Not Weird'