import re
import pytest
from unittest import mock
import builtins
def pilling_up():
    tests = int(input())

    for test in range(0, tests):
        count = int(input())
        cubes = list(map(int, input().split()))
        status = "Yes"
        pile = []

        while len(cubes) > 0:
            first = cubes[0]
            last = cubes[len(cubes) - 1]

            if first >= last:
                if len(pile) > 0 and pile[len(pile) - 1] < first:
                    status = "No"
                    break
                else:
                    pile.append(first)
                    del (cubes[0])
            else:
                if len(pile) > 0 and pile[len(pile) - 1] < last:
                    status = "No"
                    break
                else:
                    pile.append(last)
                    del (cubes[len(cubes) - 1])

        return status


def test_pilling_up_1():
    with mock.patch.object(builtins, 'input', side_effect=['1','6','4 3 2 1 3 4']):
        assert pilling_up()== "Yes"


def test_pilling_up_2():
    with mock.patch.object(builtins, 'input', side_effect=['1','3','1 3 2']):
        assert pilling_up() == "No"
