"""
https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/882/
solved and tested in 15m 45s
"""

def isAnagram(s, t):
    s_hashtable = {}
    t_hashtable = {}

    is_anagram = True
    
    if len(s) != len(t):
        return False

    for char in s:
        if char in s_hashtable:
            s_hashtable[char] += 1
        else:
            s_hashtable.update({ char: 1 })

    for char in t:
        if char in t_hashtable:
            t_hashtable[char] += 1
        else:
            t_hashtable.update({ char: 1 })

    for char in t_hashtable:
        if char not in s_hashtable:
            is_anagram = False
            continue
        if s_hashtable[char] != t_hashtable[char]:
            is_anagram = False
            continue
    
    return is_anagram
