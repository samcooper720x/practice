"""
https://leetcode.com/problems/two-sum/
"""
import pdb

def twosum(nums, target):
    array_size = len(nums)
    
    for i in range(array_size):
        for j in range(array_size):
            if j == i:
                continue

            twosum = nums[i] + nums[j]
            if twosum == target:
                return [i, j]

            j += 1
        
        i += 1
