import pytest
from unittest import mock
import builtins


def any_or_all():
    n = input('')
    num=input('')
    numbers = list(str(num).split())
    return all(int(x) >= 0 for x in numbers) and any(int(x) == int(str(x)[::-1]) for x in numbers)


def test_any_or_all():
    with mock.patch.object(builtins, 'input', lambda _: 5, "12 9 61 5 14"):
            assert any_or_all() == True


def test_any_or_all_2():
    with mock.patch.object(builtins, 'input', lambda _: 5, "1 9 5 5 4"):
            assert any_or_all() == True


def test_any_or_all_3():
    with mock.patch.object(builtins, 'input', lambda _: 5, "4 6 5 7 8"):
            assert any_or_all() == True