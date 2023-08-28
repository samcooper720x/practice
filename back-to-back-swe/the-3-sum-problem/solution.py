def three_sum(nums):
    if len(nums) < 3:
        return []

    target = 0
    solution = []
    twosum_dict = {}

    for i, a_num in enumerate(nums):
        if i == len(nums):
            break
        for j, b_num in enumerate(nums, start=i+1):
            twosum_dict.update({ (a_num + b_num): [i, j] })

    for k, c_num in enumerate(nums):
        complement = target - c_num

        if complement in twosum_dict and k not in twosum_dict[complement]:
            threesum = []
            for index in twosum_dict[complement]:
                threesum.append(nums[index])
            threesum.append(c_num)

            solution.append(threesum)

    return solution

# driver code to test
testanswer = three_sum([-1, 0, 11])
print(testanswer)

