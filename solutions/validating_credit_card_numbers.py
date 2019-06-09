import re


def check_credit_number_for_validating(string1):
    string2= ''.join(string1.split('-'))
    checking=True
    for i in range(len(string2)-3):
        if string2[i] == string2[i+1] and string2[i] == string2[i+2] and string2[i] == string2[i+3]:
            checking=False
    return checking


for i in range(int(input())):
    credit_number = input()
    if (re.compile('^[4-6][0-9]{15}$').match(s) or re.compile('^[4-6][0-9]{3}(-[0-9]{4}){3}$').match(credit_number)) and check_credit_number_for_validating(credit_number):
        print("Valid")
    else:
        print("Invalid")