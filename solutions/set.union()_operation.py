def set_union():
    n = int(input())
    first_set = set(input().split())
    m = int(input())
    second_set = set(input().split())
    return len(first_set | second_set)


print(set_union())