def is_alnum(line):
    return any(index.isalnum() for index in line)


def is_alpha(line):
    return any(index.isalpha() for index in line)


def is_digit(line):
    return any(index.isdigit() for index in line)


def is_lower(line):
    return any(index.islower() for index in line)


def is_upper(line):
    return any(index.isupper() for index in line)


line = input()
print(is_alnum(line))
print(is_alpha(line))
print(is_digit(line))
print(is_lower(line))
print(is_upper(line))