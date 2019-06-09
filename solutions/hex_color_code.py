import re


def hex_color():
    n=int(input())

    for i in range(n):
        text=input()
        if re.findall(r'.+?(\#(?:[0-9a-fA-F]{3})(?:[0-9a-fA-F]{3})?)',text):
            m=re.findall(r'.+?(\#(?:[0-9a-fA-F]{3})(?:[0-9a-fA-F]{3})?)',text)
            for j in m:
                return j


print(hex_color())