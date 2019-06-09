def no_idea():
    n, m = input().split()
    array = input().split()
    a = set(input().split())
    b = set(input().split())

    sum = 0
    for i in range(int(n)):
        if array[i] in a:
            sum = sum + 1
        elif array[i] in b:
            sum = sum - 1
    return sum


print(no_idea())