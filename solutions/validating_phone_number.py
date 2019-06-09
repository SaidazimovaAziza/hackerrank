
import re


def checking_number_for_validating(phone_number):
    if re.search(r'[789][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]',phone_number):
        return True
    return False


number_of_phones=int(input())
for i in range(number_of_phones):
    phone_number=input()
    if checking_number_for_validating(phone_number) and len(phone_number)==10:
        print("YES")
    else:
        print("NO")
