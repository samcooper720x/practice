"""
https://leetcode.com/problems/single-number/
solved and tested in 12m 55s
"""
def singleNumber(nums):
    instances_of_ints = {}

    for num in nums:
        if num not in instances_of_ints:
            instances_of_ints.update({num: 1})

        else:
            instances_of_ints[num] += 1

    for key in instances_of_ints:
        if instances_of_ints[key] == 1:
            return key
