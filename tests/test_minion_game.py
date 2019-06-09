import re
import pytest
from unittest import mock
import builtins

def minion_game():
    string = input('')
    stuart = 0
    kevin = 0
    for j in range(len(string)):
        k = len(string) - j
        if string[j] == 'A' or string[j] == 'E' or string[j] == 'I' or string[j] == 'O' or string[j] == 'U':
            stuart += k
        else:
            kevin += k

    if stuart == kevin:
        return "Draw"
    elif stuart > kevin:
        return "Kevin " + str(stuart)
    else:
        return "Stuart " + str(kevin)




def test_minion_game_1():
    with mock.patch.object(builtins, 'input', lambda _: 'BANANA'):
        assert minion_game() == 'Stuart 12'


def test_minion_game_2():
    with mock.patch.object(builtins, 'input', lambda _: 'BAANANAS'):
        assert minion_game() == 'Kevin 19'

def test_minion_game_3():
    with mock.patch.object(builtins, 'input', lambda _: 'ANANAS'):
        assert minion_game() == 'Kevin 12'
