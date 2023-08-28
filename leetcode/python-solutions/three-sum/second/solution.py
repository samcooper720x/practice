"""
https://leetcode.com/problems/3sum/
Solved and tested in 35m
"""


class Solution:
    def three_sum(self, nums: list[int]) -> list[list[int]]:
        if not nums or len(nums) < 3:
            return []

        nums = sorted(nums)
        output = []

        for i, num in enumerate(nums):
            if i > len(nums) - 2:
                break

            fwd_ptr, bwd_ptr = i + 1, len(nums) - 1

            while fwd_ptr < bwd_ptr:
                three = [num, nums[fwd_ptr], nums[bwd_ptr]]
                three_sum = sum(three)

                if three_sum == 0 and three not in output:
                    output.append(three)
                    fwd_ptr += 1
                    bwd_ptr -= 1
                elif three_sum < 0:
                    fwd_ptr += 1
                else:
                    bwd_ptr -= 1

        return output
