"""
https://leetcode.com/problems/3sum/solution/
Solved using sorted two pointer approach.
"""
def three_sum(nums):
    if len(nums) < 3:
        return []

    nums.sort()
    answer = []

    for i, num in enumerate(nums):
        if i == len(nums) - 2:
            break

        fwd_ptr = i + 1
        bwd_ptr = len(nums) - 1

        while fwd_ptr < bwd_ptr:
            threesum = [num, nums[fwd_ptr], nums[bwd_ptr]]

            if sum(threesum) < 0:
                fwd_ptr += 1
            elif sum(threesum) > 0:
                bwd_ptr -= 1
            else:
                if not threesum in answer:
                    answer.append(threesum)
                fwd_ptr += 1
                bwd_ptr -= 1

    return answer

# driver code for debugging
nums = [-2, -1, 0, 1, 2]
three_sum(nums)

