import re
import pytest
from unittest import mock
import builtins
from itertools import product

def maximize_it():
    s=input('')
    k, m = s.split()
    arr = []
    for index in range(int(k)):
        input_string = input('')
        list1 = input_string.split()
        del list1[0]
        arr.append(list1)

    result = 0
    elements = list(product(*arr))
    for j in elements:
        tmp_result = 0
        for i in j:
            tmp_result += int(i) ** 2
        if (tmp_result % int(m)) > result:
            result = tmp_result % int(m)
    return result

def test_maximize_it():
    with mock.patch.object(builtins, 'input', side_effect=['3 1000', '2 5 4','3 7 8 9','5 5 7 8 9 10']):
        assert maximize_it()== 206


def test_maximize_it():
    with mock.patch.object(builtins, 'input', side_effect=['7 30', '7 9779452 9765542 655947 1723513 2971621 8877873 2966358','7 8145469 1353512 1281184 109565 3664593 1640246 9278876',' 7 9827710 3662985 7495190 2182272 6098990 6098507 4039244',
                                                           '7 148430 4766904 8240955 4635392 5198980 4302681 7631850','7 7964390 9737228 8692231 260193 9502769 9348177 4500058','7 4990741 8226050 9982767 3136209 2095913 3780303 3245773','7 5760505 5420548 2524648 8104566 9083532 2536189 2803190']):
        assert maximize_it()== 29



def test_maximize_it():
    with mock.patch.object(builtins, 'input', side_effect=['7 513', '7 9779452 9765542 655947 1723513 2971621 8877873 2966358','7 8145469 1353512 1281184 109565 3664593 1640246 9278876',' 7 9827710 3662985 7495190 2182272 6098990 6098507 4039244'
    ,'7 148430 4766904 8240955 4635392 5198980 4302681 7631850','7 7964390 9737228 8692231 260193 9502769 9348177 4500058','7 4990741 8226050 9982767 3136209 2095913 3780303 3245773','7 5760505 5420548 2524648 8104566 9083532 2536189 2803190']):
        assert maximize_it()== 512


