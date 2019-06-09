from itertools import product


def maximize_it():
    k, m = input().split()
    arr = []
    for index in range(int(k)):
        input_string = input()
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


print(maximize_it())

