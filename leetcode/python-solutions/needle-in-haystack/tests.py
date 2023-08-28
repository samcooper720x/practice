import unittest
from solution import strStr

class TestSolution(unittest.TestCase):
    
    def test_with_needle(self):
        haystack = 'hello'
        needle = 'll'
        self.assertEqual(strStr(haystack, needle), 2)

    def test_with_no_needle(self):
        haystack = 'aaaaa'
        needle = 'bba'
        self.assertEqual(strStr(haystack, needle), -1)

    def test_with_empty_needle(self):
        haystack = ''
        needle = ''
        self.assertEqual(strStr(haystack, needle), 0)

    def test_with_single_char_needle(self):
        haystack = 'a'
        needle = 'a'
        self.assertEqual(strStr(haystack, needle), 0)

    def test_with_perfect_match(self):
        haystack = 'aaa'
        needle = 'aaa'
        self.assertEqual(strStr(haystack, needle), 0)

    def test_mississipi(self):
        haystack = 'mississippi'
        needle = 'issi'
        self.assertEqual(strStr(haystack, needle), 1)
