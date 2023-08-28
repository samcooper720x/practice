"""
https://leetcode.com/problems/reverse-integer/
solved with tests in 54'19"
"""
def reverse(x):
    sign_stored = ''

    if x < 0:
        sign_stored = '-'
        x = abs(x)

    input_as_str = str(x)
    number_of_digits = len(input_as_str)
    
    first_digit = x % 10
    
    if number_of_digits <= 1:
        return first_digit

    output_as_str = f'{sign_stored}{first_digit}'
    operator = 1 

    for i in range(number_of_digits):
        operator *= 10
        digit = (x // operator) % 10
        if (i + 1) >= number_of_digits and digit == 0:
            continue
        output_as_str = f'{output_as_str}{digit}'
    
    x_reversed = int(output_as_str)

    if x_reversed.bit_length() > 31:
        return 0

    return x_reversed 
