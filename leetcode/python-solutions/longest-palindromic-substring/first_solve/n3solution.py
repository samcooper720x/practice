'''
https://leetcode.com/problems/longest-palindromic-substring/
Times out on leetcode acceptance test with long string.
'''
def longest_palindrome(s):
    if not s:
        return ''

    longest_palindromic_ss = s[0]

    for i, char in enumerate(s):
        if i == len(s) - 1:
            break

        substring = char

        for j in range(i + 1, len(s)):
            substring = f'{substring}{s[j]}'
            if substring != reverse(substring):
                continue
            if len(substring) > len(longest_palindromic_ss):
                longest_palindromic_ss = substring
                continue

    return longest_palindromic_ss

def reverse(substring):
    substring = list(substring)

    fwd_ptr = 0
    bwd_ptr = len(substring) - 1

    while fwd_ptr < bwd_ptr:
        tmp = substring[fwd_ptr]
        substring[fwd_ptr] = substring[bwd_ptr]
        substring[bwd_ptr] = tmp

        fwd_ptr += 1
        bwd_ptr -= 1

    return ''.join(substring)

