import pytest
from unittest import mock
import builtins


def find_runner_up_score():

    set_of_scores = set()
    s = input('')
    scores = str(s).split(' ')
    for index in range(len(scores)):
        set_of_scores.add(int(scores[index]))

    list_of_scores = sorted(set_of_scores, reverse=True)
    return list_of_scores[1]


def test_find_runner_up_score_1():
    with mock.patch.object(builtins, 'input', lambda _:  "2 5 5 6 7"):
        assert find_runner_up_score() == 6



def test_find_runner_up_score_2():
    with mock.patch.object(builtins, 'input', lambda _: "2 3 5 3 5"):
        assert find_runner_up_score() == 3


def test_find_runner_up_score_3():
    with mock.patch.object(builtins, 'input', lambda _: "2 5 5 6 8"):
        assert find_runner_up_score() == 6