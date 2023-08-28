import unittest
from solution import find_intersections

class TestFindIntersection(unittest.TestCase):
    
    def test_finds_multiple_instances(self):
        array_1 = [1, 2, 2, 1]
        array_2 = [2, 2]
        intersections = find_intersections(array_1, array_2)
        self.assertEqual(intersections, [2, 2])

    def test_find_mulitple_intersections(self):
        array_1 = [4, 9, 5]
        array_2 = [9, 4, 9, 8, 4]
        intersections = find_intersections(array_1, array_2)
        self.assertEqual(intersections, [4, 9])
