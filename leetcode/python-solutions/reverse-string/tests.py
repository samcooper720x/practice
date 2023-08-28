import unittest
from solution import reverse

class TestReverseString(unittest.TestCase):
    
    def test_lowercase_only(self):
        s = ["h","e","l","l","o"]
        reverse_s = ["o","l","l","e","h"]
        self.assertEqual(reverse(s), reverse_s)
        
    def test_uppercase_only(self):
        s = ["H","a","n","n","a","h"]
        reverse_s = ["h","a","n","n","a","H"]
        self.assertEqual(reverse(s), reverse_s)

