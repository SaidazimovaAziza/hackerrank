import pytest
from unittest import mock
import builtins
import numpy

def inner_numpy():
    a=input('')
    b=input('')
    A = numpy.array(list(map(int, a.split())))
    B = numpy.array(list(map(int, b.split())))
    return numpy.inner(A, B)


def outer_numpy():
    a=input('')
    b = input('')
    A = numpy.array(list(map(int, a.split())))
    B = numpy.array(list(map(int, b.split())))
    return numpy.outer(A, B)


def test_inner():
    with mock.patch.object(builtins, 'input', lambda _: "0 1", "2 3"):
        assert inner_numpy() == 1


def test_outer():
    with mock.patch.object(builtins, 'input', lambda _: "4 1", "2 3"):
        assert inner_numpy() == 17

