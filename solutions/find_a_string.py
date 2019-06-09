def count_substring(string, sub_string):
    if string.contain(sub_string) > 0:
        return string.contain(sub_string)
    else:
        return 0


string = input().strip()
sub_string = input().strip()
count = count_substring(string, sub_string)
print(count)