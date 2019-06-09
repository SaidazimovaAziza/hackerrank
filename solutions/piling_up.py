tests = int(input())

for test in range(0, tests):
    count = int(input())
    cubes = list(map(int, input().split()))
    status = "Yes"
    pile = []

    while len(cubes) > 0:
        first = cubes[0]
        last = cubes[len(cubes) - 1]

        if first >= last:
            if len(pile) > 0 and pile[len(pile) - 1] < first:
                status = "No"
                break
            else:
                pile.append(first)
                del (cubes[0])
        else:
            if len(pile) > 0 and pile[len(pile) - 1] < last:
                status = "No"
                break
            else:
                pile.append(last)
                del (cubes[len(cubes) - 1])

    print(status)
