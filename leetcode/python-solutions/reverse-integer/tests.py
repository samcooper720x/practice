import unittest
from solution import reverse

class TestSolution(unittest.TestCase):
    
    def test_123_in_321_out(self):
        output = reverse(123)
        self.assertEqual(output, 321)

    def test_negative123_in_negative321_out(self):
        output = reverse(-123)
        self.assertEqual(output, -321)

    def test_120_in_21_out(self):
        output = reverse(120)
        self.assertEqual(output, 21)

    def test_0_in_0_out(self):
        output = reverse(0)
        self.assertEqual(output, 0)

    def test_returns_0_if_integer_over_32_bit(self):
        output = reverse(1534236469)
        self.assertEqual(output, 0)

    def test_returns_0_if_integer_over_32_bit(self):
        output = reverse(-2147483412)
        self.assertEqual(output, -2147483412)
