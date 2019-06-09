import pytest
from unittest import mock
import builtins
import re

def hex_color():
    n=int(input(''))

    for i in range(n):
        text=input('')
        if re.findall(r'.+?(\#(?:[0-9a-fA-F]{3})(?:[0-9a-fA-F]{3})?)',text):
            m=re.findall(r'.+?(\#(?:[0-9a-fA-F]{3})(?:[0-9a-fA-F]{3})?)',text)
            for j in m:
                return j


def test_hex_color_1():
    with mock.patch.object(builtins, 'input', lambda _: 1,"color: #FfFdF8;"):
        assert hex_color() == '[#FfFdF8]'


def test_hex_color_2():
    with mock.patch.object(builtins, 'input', lambda _: 1,"color: #fff;"):
        assert hex_color() == '[#fff]'


def test_hex_color_3():
    with mock.patch.object(builtins, 'input', lambda _: 1,"color: #f9f9f9;"):
        assert hex_color() == '[#f9f9f9]'