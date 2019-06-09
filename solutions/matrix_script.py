import math
import os
import random
import re
import sys


def matrix_script():

    nm = input().split()

    n = int(nm[0])
    m = int(nm[1])
    matrix = []
    for _ in range(n):
        matrix_item = input()
        matrix.append(matrix_item)

    text=" "
    for i in range(m):
        for j in range(n):
            text += matrix[j][i]
    return re.sub(r'([a-zA-Z0-9])([^a-zA-Z0-9]+)(?=[a-zA-Z0-9])', r'\1 ', text)


print(matrix_script())

