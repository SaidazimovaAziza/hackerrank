import pytest
from unittest import mock
import builtins
def print_full_name():
    first_name = input('')
    last_name = input('')
    return "Hello "+first_name+" "+last_name+ "! You just delved into python."


def test_print_full_name():
    with mock.patch.object(builtins, 'input', side_effect=['Chris', 'Alan']):
        assert print_full_name() == "Hello Chris Alan! You just delved into python."


def test_print_full_name_2():
    with mock.patch.object(builtins, 'input', side_effect=['Aziza', 'Sai']):
        assert print_full_name()== "Hello Aziza Sai! You just delved into python."


def test_print_full_name_3():
    with mock.patch.object(builtins, 'input', side_effect=['Vasya', 'Pupkin']):
        assert print_full_name()== "Hello Vasya Pupkin! You just delved into python."
