"""
https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/887/
solved in 22m
got a little tripped up by strs == [] cases and was slow to fix
should try and implement error handling in these for that
"""

def longestCommonPrefix(strs):
    if strs == []:
        prefix = ''
        return prefix

    prefix = strs[0]

    if prefix == '':
        return prefix

    for string in strs:
        if len(prefix) > len(string):
            prefix = prefix[:len(string)]
    
    if prefix == '':
        return prefix

    for string in strs:
        for i, char in enumerate(prefix):
            if char != string[i]:
                prefix = prefix[:i]

    return prefix
