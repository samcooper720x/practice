"""
https://leetcode.com/problems/rotate-array/
solved in 28m 16s
should try solving without using pop and insert though...
"""
def rotate(nums, k):
    i = 0
    while i < k:
        last_element = nums.pop()
        nums.insert(0, last_element)
        i += 1

    return nums
