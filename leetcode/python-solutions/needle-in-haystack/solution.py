"""
https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/885/
solved and tested in 54m 03s
"""

def strStr(haystack, needle):

    haystack_dict = {}

    needle_len = len(needle)
    limit = len(haystack) - needle_len

    if needle == '':
        return 0

    if needle_len == 1:
        for i, char in enumerate(haystack):
            if char == needle:
                return i

    for i, char in enumerate(haystack):
        if i > limit:
            break

        potential_needle = f'{haystack[i:i+needle_len]}'

        if potential_needle in haystack_dict:
            haystack_dict[potential_needle].append(i)
        else:
            haystack_dict.update({ potential_needle: [i] })

    if needle in haystack_dict:
        return haystack_dict[needle][0]

    else:
        return -1
