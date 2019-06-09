import numpy
import re
import pytest
import builtins
from unittest import mock

def swap_case():
    line = input('')
    return line.swapcase()

def test_swap_case_1():
    with mock.patch.object(builtins, 'input', side_effect=['HackerRank.com presents "Pythonist 2".']):
        assert swap_case()=='hACKERrANK.COM PRESENTS "pYTHONIST 2".'

def test_swap_case_2():
    with mock.patch.object(builtins, 'input', side_effect=['22T6M2reD4']):
        assert swap_case()=='22t6m2REd4'

def test_swap_case_3():
    with mock.patch.object(builtins, 'input', side_effect=[
        'SG.2ehL62pSmsnd7c9XYYsFvV067gybBhsSM0SJ7zpAJWr8pwEFzq3ACtuSAjpL7ZnWXbASGlBnEawSnWs1 gpCySKB2.at bt5S']):
        assert swap_case()==\
               'sg.2EHl62PsMSND7C9xyySfVv067GYBbHSsm0sj7ZPajwR8PWefZQ3acTUsaJPl7zNwxBasgLbNeAWsNwS1 GPcYskb2.AT BT5s'