def check_for_weird_or_not_weird():
    number = int(input())
    result = ""
    if number % 2 == 1:
        result = "Weird"

    else:
        if 2 <= number <= 5:
            result = "Not Weird"

        if 6 <= number <= 20:
            result = "Weird"

        if number > 20:
            result = "Not Weird"
    return result


print(check_for_weird_or_not_weird())
