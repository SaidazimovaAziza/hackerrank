def mod(first_number, second_number):
    return first_number%second_number


def div(first_number, second_number):
    return first_number//second_number


def div_mod(first_number,second_number):
    return divmod(first_number,second_number)


first_number=int(input())
second_number=int(input())
print(mod(first_number,second_number))
print(div(first_number,second_number))
print(divmod(first_number,second_number))
