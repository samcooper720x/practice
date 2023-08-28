import unittest
from solution import longestCommonPrefix

class TestLongestCommonPrefix(unittest.TestCase):
    
    def test_if_2(self):
        strs = ["flower","flow","flight"]
        self.assertEqual(longestCommonPrefix(strs), 'fl')

    def test_if_none(self):
        strs = ["dog","racecar","car"]
        self.assertEqual(longestCommonPrefix(strs), '')

    def test_if_empty_input(self):
        strs = []
        self.assertEqual(longestCommonPrefix(strs), '')

