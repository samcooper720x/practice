import unittest
from solution import find_and_replace_pattern

class TestPatternMatching(unittest.TestCase):
    def test_all_match(self):
        words = ["aa", "bb"]
        pattern = "cc"
        output = words
        self.assertEqual(find_and_replace_pattern(words, pattern), output)

    def test_aba(self):
        words = ["aac", "bbc", "bcb", "yzy"]
        pattern = "ghg"
        output = ["bcb", "yzy"]
        self.assertEqual(find_and_replace_pattern(words, pattern), output)

    def test_no_match(self):
        words = ["aa", "bb"]
        pattern = "zy"
        output = []
        self.assertEqual(find_and_replace_pattern(words, pattern), output)

