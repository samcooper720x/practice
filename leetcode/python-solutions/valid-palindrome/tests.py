import unittest
from solution import isPalindrome

class TestIsPalindrome(unittest.TestCase):
    
    @unittest.skip("tests partial functionality with different return value")
    def test_drops_case_nonalphanum(self):
        s = "A man, a plan, a canal: Panama"
        t = "amanaplanacanalpanama"
        self.assertEqual(isPalindrome(s), t)

    def test_if_true(self):
        s = "A man, a plan, a canal: Panama"
        self.assertEqual(isPalindrome(s), True)

    def test_if_false(self):
        s = "race a car"
        self.assertEqual(isPalindrome(s), False)

