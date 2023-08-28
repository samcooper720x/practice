import pytest
from solution import three_sum


class TestThreeSum:
    def test_handles_bad_inputs(self):
        assert three_sum([]) == []
        assert three_sum([0, 1]) == []
    
    def test_three_sum(self):
        nums = [-1,0,1,2,-1,-4]
        answer = [[-1,-1,2],[-1,0,1]]
        assert three_sum(nums) == answer

    def test_no_duplicates(self):
        nums = [0,0,0,0]
        answer = [[0, 0, 0,]]
        assert three_sum(nums) == answer

    def test_find_all_possible(self):
        nums = [-2,0,1,1,2]
        answer = [[-2,0,2],[-2,1,1]]
        assert three_sum(nums) == answer

