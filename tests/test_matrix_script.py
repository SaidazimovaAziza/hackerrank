import pytest
from unittest import mock
import builtins
import re

def matrix_script():
    s=input('')
    nm = s.split()

    n = int(nm[0])
    m = int(nm[1])
    matrix = []
    for _ in range(n):
        matrix_item = input('')
        matrix.append(matrix_item)

    text=" "
    for i in range(m):
        for j in range(n):
            text += matrix[j][i]
    return re.sub(r'([a-zA-Z0-9])([^a-zA-Z0-9]+)(?=[a-zA-Z0-9])', r'\1 ', text)

def test_print_matrix_script_1():
    with mock.patch.object(builtins, 'input', side_effect=['7 3', 'Tsi','h%x','i #','sM ','$a ','#t%','ir!']):
        assert matrix_script() == ' This is Matrix#  %!'

def test_print_matrix_script_2():
    with mock.patch.object(builtins, 'input', side_effect=['4 6', 'T%$r%r','h%Mi$i','iiaxsp','sst%ct']):
        assert matrix_script() == ' This is Matrix script'

def test_print_matrix_script_3():
    with mock.patch.object(builtins, 'input', side_effect=['7 3', 'Tsi','h%x','i #','sM ','$a ','#t%','ir!']):
        assert matrix_script() == ' This is Matrix#  %!'
