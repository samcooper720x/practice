import unittest
from solution2 import is_palindrome

class TestIsPalindrome(unittest.TestCase):
    def test_when_false(self):
        x = 9232
        self.assertEqual(is_palindrome(x), False)

    def test_when_true(self):
        x = 12321
        self.assertEqual(is_palindrome(x), True)

    def test_single_digit(self):
        x = 1
        self.assertEqual(is_palindrome(x), True)

    def test_when_negative(self):
        x = -121
        self.assertEqual(is_palindrome(x), False)
