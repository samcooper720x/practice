from math import log10

def is_palindrome(x):
    '''
    :type x: int
    :rtype: bool
    '''
    
    if x < 0:
        return False

    if x < 10:
        return True

    y = 0
    copy_x = x 

    digits = int(log10(x) + 1)

    for i in range(digits):
        y = (y * 10) + (copy_x % 10)
        copy_x = (copy_x - (copy_x % 10)) / 10

    if x == y:
        return True
    else:
        return False
