'''
https://leetcode.com/submissions/detail/490097275/?from=explore&item_id=780
First attempt at brute force included as n3solution.py
'''
from math import floor, ceil


def longest_palindrome(s):
    if not s or len(s) == 1:
        return s
    
    longest_palindrome = s[0]

    for center in get_centers(s):
        if type(center) != int:
            palindrome = f'{s[floor(center)]}{s[ceil(center)]}'
            left_ptr = int(floor(center) - 1)
            right_ptr = int(ceil(center) + 1)

        else:
            palindrome = s[center]
            left_ptr = center - 1
            right_ptr = center + 1

        while left_ptr >= 0 and right_ptr < len(s):
            if s[left_ptr] == s[right_ptr]:
                palindrome = f'{s[left_ptr]}{palindrome}{s[right_ptr]}'

                left_ptr -= 1
                right_ptr += 1

            else:
                break

        if len(palindrome) > len(longest_palindrome):
            longest_palindrome = palindrome
    
    return longest_palindrome

def get_centers(s):
    centers = []

    for i, char in enumerate(s):
        if i == len(s) - 1:
            continue
        
        centers.append(i)

        if char == s[i + 1]:
            centers.append(i + 0.5)

    return centers

# driver code for debuggin
longest_palindrome('ccc')
