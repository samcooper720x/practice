import unittest
from solution import singleNumber

class TestSolution(unittest.TestCase):
    
    def test_if_array_one_returns_one(self):
        output = singleNumber([1])
        self.assertEqual(output, 1)

    def test_finds_element_in_array_appearing_once(self):
        output = singleNumber([2, 2, 1])
        self.assertEqual(output, 1)

