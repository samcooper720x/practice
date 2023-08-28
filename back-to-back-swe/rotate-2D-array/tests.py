import unittest
from solution import rotate

class TestSolution(unittest.TestCase):
    def test_rotate(self):
        matrix = [[ 1,  2,  3, 4], [ 5,  6,  7, 8], [ 9, 10, 11, 12], [13, 14, 15, 16]]
        matrix_rotated = [[13,  9, 5, 1], [14, 10, 6, 2], [15, 11, 7, 3], [16, 12, 8, 4]]
        self.assertEqual(rotate(matrix), matrix_rotated)
    
    def test_2x2(self):
        matrix = [[10, 20], [30, 40]]
        matrix_rotated = [[30, 10], [40, 20]]
        self.assertEqual(rotate(matrix), matrix_rotated)


if __name__ == '__main__':
    unittest.main()
