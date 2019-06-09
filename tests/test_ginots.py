import pytest
from unittest import mock
import builtins


def ginortS():
    line = input('')
    lower = []
    upper = []
    even = []
    odd = []
    for i in range(len(line)):
        if line[i].islower():
            lower.append(line[i])

        if line[i].isupper():
            upper.append(line[i])

        if line[i].isdigit():
            if int(line[i]) % 2 == 0:
                even.append(line[i])

            else:
                odd.append(line[i])

    lower.sort()
    upper.sort()
    even.sort()
    odd.sort()
    s = ""
    for i in lower:
        s = s + i

    for i in upper:
        s = s + i

    for i in odd:
        s = s + i

    for i in even:
        s= s + i

    return s


def test_ginort_1():
    with mock.patch.object(builtins, 'input', lambda _: "Sorting1234"):
        assert ginortS() == "ginortS1324"


def test_ginort_2():
    with mock.patch.object(builtins, 'input', lambda _: "1qaz2wsx3edc4rfv5tgb6yhn7ujm8ik9ol0pQWERTYUIOPASDFGHJKLZXCVBNM"):
        assert ginortS() == "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1357902468"


def test_ginort_3():
    with mock.patch.object(builtins, 'input',
                           lambda _: "qwerty123456789dfghj123456789QWERTYUIOPASDFGHJKLZXCVBNM0123456789"):
        assert ginortS() == \
               "defghjqrtwyABCDEFGHIJKLMNOPQRSTUVWXYZ1113335557779990222444666888"
