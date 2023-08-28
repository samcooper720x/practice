import unittest
from solution2 import rotate

class TestSolution(unittest.TestCase):
    
    def test_rotate_by_3_places(self):
        nums = [1, 2, 3, 4, 5, 6, 7]
        k = 3
        nums = rotate(nums, k)
        self.assertEqual(nums, [5, 6, 7, 1, 2, 3, 4])

    def test_rotate_by_2_places(self):
        nums = [-1, -100, 3, 99]
        k = 2
        nums = rotate(nums, k)
        self.assertEqual(nums, [3, 99, -1, -100])
