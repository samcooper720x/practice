def twosum(nums, target):
    nums_dict = {}

    for index, num in enumerate(nums):
        nums_dict.update({ num: index })

    for index, num in enumerate(nums):
        complement = target - num

        if complement in nums_dict and nums_dict[complement] != index:
            one = min(index, nums_dict[complement])
            two = max(index, nums_dict[complement])

            solution = [one, two]

    return solution
    
