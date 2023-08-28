"""
https://leetcode.com/problems/group-anagrams/
"""
from collections import defaultdict


def group_anagrams(strs):
    answer = []
    anagrams = defaultdict(list)

    for word in strs:
        standardised_anagram = standardise_anagram(word)
        anagrams[standardised_anagram].append(word)

    for groups in anagrams.values():
        answer.append(groups)
    
    return answer

def standardise_anagram(anagram):
    chars = [char for char in anagram]
    chars.sort()
    return ''.join(chars)

