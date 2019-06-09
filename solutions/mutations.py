def mutate_string(string, position, character):
    lists = list(string)
    lists[position] = character
    return "".join(lists)


string = input()
i, c = input().split()
print(mutate_string(str, int(i), c))
