def ginortS():
    line = input()
    lower = []
    upper = []
    even = []
    odd = []
    for i in range(len(line)):
        if line[i].islower():
            lower.append(line[i])

        if line[i].isupper():
            upper.append(line[i])

        if line[i].isdigit():
            if int(line[i]) % 2 == 0:
                even.append(line[i])

            else:
                odd.append(line[i])

    lower.sort()
    upper.sort()
    even.sort()
    odd.sort()
    s = ""
    for i in lower:
        s = s + i

    for i in upper:
        s = s + i

    for i in odd:
        s = s + i

    for i in even:
        s= s + i

    return s

print(ginortS())