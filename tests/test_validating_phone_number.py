import re
import pytest
from unittest import mock
import builtins

def checking_number_for_validating():
    number_of_phones = int(input(''))
    for i in range(number_of_phones):
        phone_number = input()
        if re.search(r'[789][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]',phone_number):
            if len(phone_number)==10:
                return True
        return False


def test_checking_number_for_validating_1():
    with mock.patch.object(builtins, 'input', side_effect=[1,'9587456281']):
        assert checking_number_for_validating() == True


def test_checking_number_for_validating_2():
     with mock.patch.object(builtins, 'input', side_effect=[1, '1252478965']):
        assert checking_number_for_validating() == False


def test_checking_number_for_validating_3():
    with mock.patch.object(builtins, 'input', side_effect=[1, '8F54698745']):
        assert checking_number_for_validating() == False
