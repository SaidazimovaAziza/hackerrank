import re
import pytest
from unittest import mock
import builtins

def nested_lists():
    allscores = set()
    allnames = []
    for i in range(int(input())):
        list = []
        name = input()
        score = float(input())

        list.append(name)
        list.append(score)
        allscores.add(score)
        allnames.append(list)
    allnames.sort(key=lambda x: x[1])
    list = []
    l = sorted(allscores, reverse=True)

    first = l.pop()
    second = l.pop()

    for i in range(len(allnames)):

        if second == allnames[i][1]:
            list.append(allnames[i][0])
    list.sort()
    return list


def test_nested_lists_1():
    with mock.patch.object(builtins, 'input', side_effect=['5', 'Harry','37.21','Berry','37.21','Tina','37.2','Akriti','41','Harsh','39']):
        assert nested_lists() == ['Berry','Harry']

def test_nested_lists_2():
    with mock.patch.object(builtins, 'input', side_effect=['4', 'Prashant','32','Pallavi','36','Dheeraj','39','Shivam','40']):
        assert nested_lists() == ['Pallavi']

def test_nested_lists_3():
    with mock.patch.object(builtins, 'input', side_effect=[ '5', 'Harsh','20','Berria','20','Varun','19','Kakunami','19','Vikas','21']):
        assert nested_lists() == ['Berria','Harsh']

