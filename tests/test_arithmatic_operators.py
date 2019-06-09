import pytest
from unittest import mock
import builtins

def sum_of_numbers():
    first_number = int(input(''))
    second_number = int(input(''))
    return first_number+second_number


def product_of_numbers():
    first_number = int(input(''))
    second_number = int(input(''))
    return first_number*second_number


def subtraction_of_numbers():
    first_number = int(input(''))
    second_number = int(input(''))
    return first_number-second_number


def test_substraction():
    with mock.patch.object(builtins, 'input', lambda _: 7, 7):
        assert subtraction_of_numbers() == 0


def test_product():
    with mock.patch.object(builtins, 'input', lambda _: 2, 2):
        assert product_of_numbers() == 4


def test_sum():
    with mock.patch.object(builtins, 'input', lambda _: 3, 3):
        assert sum_of_numbers() == 6