"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array/
solved in 40m
had solution v. early and got lost in implementation with going past end of array
"""
def remove_duplicates(nums):
    for i, i_num in enumerate(nums):
        if (i + 1) == len(nums):
            return len(nums)
        
        while nums[i + 1] == i_num:
            nums.pop(i + 1)
            if (i + 1) == len(nums):
                break

    return len(nums)
