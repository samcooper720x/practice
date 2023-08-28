import unittest
from solution import isAnagram

class TestIsAnagram(unittest.TestCase):
    
    def test_if_true(self):
        s = "anagram"
        t = "nagaram"
        self.assertEqual(isAnagram(s, t), True)

    def test_if_false(self):
        s = "rat"
        t = "car"
        self.assertEqual(isAnagram(s, t), False)

    def test_if_unequal(self):
        s = "ab"
        t = "a"
        self.assertEqual(isAnagram(s, t), False)
