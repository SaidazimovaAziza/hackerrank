def minion_game():
    string = input()
    stuart = 0
    kevin = 0
    for j in range(len(string)):
        k = len(string) - j
        if string[j] == 'A' or string[j] == 'E' or string[j] == 'I' or string[j] == 'O' or string[j] == 'U':
            stuart += k
        else:
            kevin += k

    if stuart == kevin:
        return "Draw"
    elif stuart > kevin:
        return "Kevin " + str(stuart)
    else:
        return "Stuart " + str(kevin)


print(minion_game())
