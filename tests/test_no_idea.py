import re
import pytest
from unittest import mock
import builtins
def no_idea():
    n, m = input().split()
    array = input().split()
    a = set(input().split())
    b = set(input().split())

    sum = 0
    for i in range(int(n)):
        if array[i] in a:
            sum = sum + 1
        elif array[i] in b:
            sum = sum - 1
    return sum


def test_no_idea_1():
    with mock.patch.object(builtins, 'input', side_effect=['3 2', '1 5 3','3 1','5 7']):
        assert no_idea() == 1

def test_no_idea_2():
    with mock.patch.object(builtins, 'input', side_effect=['5 5', '1 2 3 4 5','1 3 5 7 9','2 4 6 8 10']):
        assert no_idea() == 1

def test_no_idea_3():
    with mock.patch.object(builtins, 'input', side_effect=['5 5', '999999991 999999992 999999993 999999994 999999999','999999991 999999993 999999995 999999999 999999997','999999990 999999992 999999996 999999998 999999994']):
        assert no_idea() == 1
