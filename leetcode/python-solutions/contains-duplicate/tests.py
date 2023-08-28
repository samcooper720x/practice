import unittest
from solution2 import contains_duplicates

class TestContainsDuplicates(unittest.TestCase):
    def test_contains_one(self):
        nums = [1,2,3,1]
        self.assertEqual(contains_duplicates(nums), True)

    def test_contains_none(self):
        nums = [1,2,3,4]
        self.assertEqual(contains_duplicates(nums), False)

    def test_contains_multiple(self):
        nums = [1,1,1,3,3,4,3,2,4,2]
        self.assertEqual(contains_duplicates(nums), True)

if __name__ == '__main__':
    unittest.main()
