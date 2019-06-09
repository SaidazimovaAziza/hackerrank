import pytest
from unittest import mock
import builtins
import numpy

def concatenate():
    n=input('')
    N, M, P = map(int, n.split())
    nm=input('')
    mn=input('')
    NP = numpy.array([nm.split() for i in range(N)], int)
    MP = numpy.array([mn.split() for j in range(M)], int)

    return str(numpy.concatenate((NP, MP), axis=0))

def test_concatenate_1():
    with mock.patch.object(builtins, 'input', lambda _: "4 3 2", '1 2 \n       1 2 \n       1 2 \n       1 2 \n       ','3 4 \n       3 4  \n       3 4 '):
        assert concatenate() =="[[4, 3, 2],'\n'       [4, 3, 2],'\n''       [4, 3, 2],'\n'       [4, 3, 2],'\n''       [4, 3, 2],'\n'       [4, 3, 2],'\n'       [4, 3, 2]]"