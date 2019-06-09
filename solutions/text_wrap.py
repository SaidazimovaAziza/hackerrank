import textwrap

def wrap():
    string, max_width = input(), int(input())
    result = textwrap.fill(string,max_width)
    return result


print(wrap())