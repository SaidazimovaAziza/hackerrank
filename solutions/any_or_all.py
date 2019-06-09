def any_or_all():
    n, numbers = int(input()), list(map(int, input().split()))
    return all(x >= 0 for x in numbers) and any(x == int(str(x)[::-1]) for x in numbers)


print(any_or_all())