def word_order():
    number_of_words = int(input())
    dictionaty = {}
    word_order = []
    for iindex in range(number_of_words):
        text = input()
        if text in dictionaty:
            dictionaty[text] += 1

        else:
            word_order.append(text)
            dictionaty[text] = 1

    print(len(dictionaty.keys()))
    values = dictionaty.values()
    return values


for each in word_order():
    print(each, end=" ")

