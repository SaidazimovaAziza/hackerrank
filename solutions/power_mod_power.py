def power(first_number, second_number):
    return first_number ** second_number


def mod_power(first_number, second_number,mod):
    return first_number**second_number%mod


first_number = int(input())
second_number = int(input())
mod = int(input())
print(power(first_number, second_number))
print(mod_power(first_number, second_number, mod))
