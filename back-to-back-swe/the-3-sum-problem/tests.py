import unittest
from solution import three_sum

class TestThreeSum(unittest.TestCase):
    def test_empty(self):
        nums = []
        self.assertEqual(three_sum(nums), [])

    def test_zero(self):
        nums = [0]
        self.assertEqual(three_sum(nums), [])

    def test_find_sums(self):
        nums = [-1,0,1,2,-1,-4]
        self.assertEqual(three_sum(nums), [[-1, -1, 2], [-1, 0, 1]])
