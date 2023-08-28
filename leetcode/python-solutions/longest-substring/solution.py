'''
https://leetcode.com/problems/longest-substring-without-repeating-characters/
Naive / brute force and super slow, come back and optimise.
'''
def length_of_longest_substring(s):
    longest_substring = 0

    for i, char in enumerate(s):
        substring = 1
        seen = [char]

        for j in range(i + 1, len(s)):
            if s[j] in seen:
                break
            else:
                seen.append(s[j])
                substring += 1

        if substring > longest_substring:
            longest_substring = substring

    return longest_substring

