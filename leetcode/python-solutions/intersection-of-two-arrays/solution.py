"""
https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/674/
solved with tests in 42m 45s
"""

def find_intersections(nums1, nums2):
    intersections = []

    nums_instances = {}
    nums_instances2 = {}

    for i in nums1:
        if i in nums_instances:
            nums_instances[i] += 1
        else:
            nums_instances.update({i: 1})

    for i in nums2:
        if i in nums_instances2:
            nums_instances2[i] += 1
        else:
            nums_instances2.update({i: 1})

    for i in nums_instances:
        if i in nums_instances2:
            instances_in_1 = nums_instances[i]
            instances_in_2 = nums_instances2[i]
            instances = min(instances_in_1, instances_in_2)
            
            for _ in range(instances):
                intersections.append(i)

    return intersections
