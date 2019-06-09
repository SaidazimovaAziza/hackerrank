def tuples():
    number_of_elements = int(input())
    integer_list = map(int, input().split())
    return hash(tuple(integer_list))


print(tuples())
