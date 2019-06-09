import math
import os
import random
import re
import sys


def company_logo():
    chars = input()
    dict = {}
    for letter in chars:
        if letter in dict:
            dict[letter] += 1
        else:
            dict[letter] = 1
    sorted_list = sorted(dict.items(), key=lambda x: x[0])
    sorted_list.sort(reverse=True, key=lambda x: x[1])
    sorted_list = sorted_list[:3]
    return sorted_list


for element in company_logo():
    print(element[0], element[1])


