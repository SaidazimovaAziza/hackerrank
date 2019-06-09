def nested_lists():
    allscores = set()
    allnames = []
    for i in range(int(input())):
        list = []
        name = input()
        score = float(input())

        list.append(name)
        list.append(score)
        allscores.add(score)
        allnames.append(list)
    allnames.sort(key=lambda x: x[1])
    list = []
    l = sorted(allscores, reverse=True)

    first = l.pop()
    second = l.pop()

    for i in range(len(allnames)):

        if second == allnames[i][1]:
            list.append(allnames[i][0])
    list.sort()
    return list


for i in nested_lists():
    print(i)