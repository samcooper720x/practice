import unittest
from solution import remove_duplicates

class TestRemoveDuplicates(unittest.TestCase):
    
    def test_one_repeat(self):
        nums = [1,1,2]
        self.assertEqual(remove_duplicates(nums), 2)

    def test_many_repeats(self):
        nums = [0,0,1,1,1,2,2,3,3,4]
        self.assertEqual(remove_duplicates(nums), 5)

