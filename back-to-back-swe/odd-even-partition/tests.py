import unittest
from .oddeven import partition_by_odd_even

class TestOddEvenPartition(unittest.TestCase):
    
    def test_returns_odd_even_partitioned_linked_list(self):
        linked_list = [{"value":5,"next":1},{"value":1,"next":2},{"value":3,"next":3},{"value":7,"next":4},{"value":3,"next":0}]
        partitioned_list = [{"next":1,"value":5},{"next":2,"value":3},{"next":3,"value":3},{"next":4,"value":1},{"next":0,"value":7}]
        self.assertEqual(partition_by_odd_even(linked_list), partitioned_list)

if __name__ == '__main__':
    unittest.main()
