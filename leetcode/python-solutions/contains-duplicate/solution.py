"""
https://leetcode.com/problems/contains-duplicate/
solved in 12m
"""
def contains_duplicates(nums):
    numdict = {}
    for num in nums:
        if num in numdict:
            return True
        else:
            numdict.update({ num: 1 })
    return False
