import pytest
from unittest import mock
import builtins
import re

def power():
    first_number = int(input())
    second_number = int(input())

    return first_number ** second_number


def mod_power():
    first_number = int(input())
    second_number = int(input())
    mod = int(input())
    return first_number**second_number%mod

def test_polynomials_1():
    with mock.patch.object(builtins, 'input', side_effect=['3','4','5']):
        assert mod_power()== 1

def test_polynomials_2():
    with mock.patch.object(builtins, 'input', side_effect=['3','4']):
        assert power()== 81


