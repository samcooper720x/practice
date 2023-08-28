'''
https://leetcode.com/problems/missing-ranges/
Got a bit caught up with some of the edge cases here. Revisit.
'''

def find_missing_ranges(nums, lower, upper):
    missing_ranges = []
    highest_found = lower - 1

    for i in range(len(nums) + 1):
        num = nums[i] if i < len(nums) else upper + 1
        if highest_found + 1 <= num - 1:
            missing_ranges.append(notate_range(highest_found + 1, num - 1))
        highest_found = num

    return missing_ranges

def notate_range(lower, upper):
    if lower == upper:
        return str(lower)
    else:
        return f'{lower}->{upper}'

