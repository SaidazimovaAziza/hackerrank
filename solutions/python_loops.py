def square_of_number(number):
    result = ""
    for index in range(number):
        result = result + str(index**2)
    return result


number = int(input())
print(square_of_number(number))
