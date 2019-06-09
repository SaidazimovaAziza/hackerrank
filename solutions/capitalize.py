import math
import os
import random
import re
import sys

def solve(string):
    letters = list(string)
    result = ""
    for index in range(len(letters)):
        if index == 0:
            letters[index] = letters[index].capitalize()
        if letters[index] == " ":
            letters[index+1]=letters[index+1].capitalize()
        result = result+letters[index]
    return result


string = input()
print(solve(string))
