"""
https://leetcode.com/problems/first-unique-character-in-a-string/solution/
solved and tested in 28m 27s
"""

def firstUniqChar(s):
    char_instances = {}

    for char in s:
        if char in char_instances:
            char_instances[char] += 1

        else:
            char_instances.update({ char: 1 })

    for i, char in enumerate(s):
        if char_instances[char] == 1:
            return i

    return -1
