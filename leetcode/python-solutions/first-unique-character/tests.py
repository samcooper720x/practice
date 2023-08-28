import unittest
from solution import firstUniqChar

class TestSolution(unittest.TestCase):
    
    def test_one(self):
        s = "leetcode"
        self.assertEqual(firstUniqChar(s), 0)

    def test_two(self):
        s = "loveleetcode"
        self.assertEqual(firstUniqChar(s), 2)

    def test_no_unique(self):
        s = "aabb"
        self.assertEqual(firstUniqChar(s), -1)

