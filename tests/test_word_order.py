import pytest
from unittest import mock
import builtins

def word_order():

    number_of_words = input('')
    dictionaty = {}
    word_order = []
    for iindex in range(int(number_of_words)):
        text = input('')
        if text in dictionaty:
            dictionaty[text] += 1

        else:
            word_order.append(text)
            dictionaty[text] = 1

    print(len(dictionaty.keys()))
    values = dictionaty.values()

    return values


def test_solve_1():
    with mock.patch.object(builtins, 'input', lambda _: '3', 'bcdef','abcdefg','abcdefg'):
        assert word_order() == [2, 1]