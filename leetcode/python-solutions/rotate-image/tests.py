import unittest
from solution import rotate

class TestRotate(unittest.TestCase):
    def test_3by3(self):
        matrix = [[1,2,3],[4,5,6],[7,8,9]]
        rotated = [[7,4,1],[8,5,2],[9,6,3]]
        self.assertEqual(rotate(matrix), rotated)

    def test_4by4(self):
        matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]] 
        rotated = [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]] 
        self.assertEqual(rotate(matrix), rotated)

    def test_1by1(self):
        matrix = [[1]] 
        rotated = [[1]] 
        self.assertEqual(rotate(matrix), rotated)

    def test_2by2(self):
        matrix = [[1,2],[3,4]]
        rotated = [[3,1],[4,2]]
        self.assertEqual(rotate(matrix), rotated)

    def test_empty(self):
        matrix = []
        rotated = []
        self.assertEqual(rotate(matrix), rotated)

    def test_6by6(self):
        matrix = [[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6]]
        rotated = [[1,1,1,1,1,1],[2,2,2,2,2,2],[3,3,3,3,3,3],[4,4,4,4,4,4],[5,5,5,5,5,5],[6,6,6,6,6,6]]
        self.assertEqual(rotate(matrix), rotated)
