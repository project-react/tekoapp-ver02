import random


def random_password():
    num_upper_case = random.randint(1, 5)
    num_lower_case = random.randint(1, 7 - num_upper_case)
    num = 8 - num_upper_case - num_lower_case
    password = ''

    for n in range(num_upper_case):
        x = random.randint(65, 90)
        password += chr(x)

    for n in range(num_lower_case):
        x = random.randint(97, 122)
        password += chr(x)

    for n in range(num):
        x = random.randint(48, 57)
        password += chr(x)

    return password

