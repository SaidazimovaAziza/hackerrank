def print_counting(number):
    result = ""
    for index in range(number):
        result += str(index+1)
    return result


number = int(input())
print(print_counting(number))

