import numpy
import re
import pytest
import builtins
from unittest import mock


def polynomials():
    A = [i for i in map(float, input().split())]
    b = int(input())
    return numpy.polyval(A, b)


def test_polynomials_1():
    with mock.patch.object(builtins, 'input', side_effect=['1.1 2 3','0']):
        assert polynomials()== 3.0

def test_polynomials_2():
    with mock.patch.object(builtins, 'input', side_effect=['1.1 2 3','5']):
        assert polynomials()== 40.5

def test_polynomials_3():
    with mock.patch.object(builtins, 'input', side_effect=['1 1','5']):
        assert polynomials()== 6.0
