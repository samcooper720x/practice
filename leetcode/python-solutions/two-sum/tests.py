import unittest
from solution2 import twosum

class TestTwoSum(unittest.TestCase):
    
    def test_if_target_0_returns_indices_of_0_0(self):
        nums = [0, 1, 2, 0]
        target = 0
        output = twosum(nums, target)
        self.assertEqual(output, [0, 3])

    def test_if_target_9_returns_indices_of_2_7(self):
        nums = [2, 7, 11, 15]
        target = 9
        output = twosum(nums, target)
        self.assertEqual(output, [0, 1])

    def test_if_target_6_returns_indices_of_2_4(self):
        nums = [3, 2, 4]
        target = 6
        output = twosum(nums, target)
        self.assertEqual(output, [1, 2])

    def test_if_target_6_returns_indices_of_3_3(self):
        nums = [3, 3]
        target = 6
        output = twosum(nums, target)
        self.assertEqual(output, [0, 1])
