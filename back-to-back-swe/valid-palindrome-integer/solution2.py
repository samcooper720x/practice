import math

def is_palindrome(x):
    if x == 0:
        return False

    if x < 10:
        return True

    no_of_digits = int(math.log10(x)) + 1
    mask = int(math.pow(10, no_of_digits - 1))

    for i in range(no_of_digits // 2):
        big_digit = x // mask
        little_digit = x % 10

        if big_digit != little_digit:
            return False

        x %= mask
        x //= 10

        mask //= 100

    return True
