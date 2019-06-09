import pytest
from unittest import mock
import builtins

"""
The function to test (would usually be loaded
from a module outside this file).
"""
def solve():
    string = input('')
    letters = list(string)
    result = ""
    for index in range(len(letters)):
        if index == 0:
            letters[index] = letters[index].capitalize()
        if letters[index] == " ":
            letters[index+1]=letters[index+1].capitalize()
        result = result+letters[index]
    return result

"""
This test will mock input of chris alan
"""


def test_solve_1():
    with mock.patch.object(builtins, 'input', lambda _: 'chris alan'):
        assert solve() == 'Chris Alan'


def test_solve_2():
    with mock.patch.object(builtins, 'input', lambda _: 'hello world'):
        assert solve() == 'Hello World'


def test_solve_3():
    with mock.patch.object(builtins, 'input', lambda _: 'hello world lol'):
        assert solve() == 'Hello World Lol'



