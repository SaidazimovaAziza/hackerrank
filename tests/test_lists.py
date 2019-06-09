import pytest
from unittest import mock
import builtins

def lists():
    number_of_operations = int(input(''))
    list_of_elements = []
    for index in range(number_of_operations):
        s=input('')
        command = s.split(" ")
        if command[0] == "insert":
            list_of_elements.insert(int(command[1]), int(command[2]))
        if command[0] == "print":
            print(list_of_elements)
        if command[0] == "remove":
            list_of_elements.remove(int(command[1]))
        if command[0] == "append":
            list_of_elements.append(int(command[1]))
        if command[0] == "sort":
            list_of_elements.sort()
        if command[0] == "pop":
            list_of_elements.pop()
        if command[0] == "reverse":
            list_of_elements.reverse()



def test_solve_1():
    with mock.patch.object(builtins, 'input', side_effect=['12','insert 0 5', 'insert 1 10','insert 0 6', 'print']):
        assert lists() == [6, 5, 10]