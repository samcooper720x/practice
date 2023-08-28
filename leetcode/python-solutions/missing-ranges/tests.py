import pytest
from solution import find_missing_ranges, notate_range


class TestSolution:
    def test_recognises_ranges_as_inclusive(self):
        nums = []
        lower, upper = 1, 1
        assert find_missing_ranges(nums, lower, upper) == ['1']

    def test_handles_negatives(self):
        nums = [-1]
        lower, upper = -2, -1
        assert find_missing_ranges(nums, lower, upper) == ['-2']

    def test_none_missing(self):
        nums = [-1]
        lower, upper = -1, -1
        assert find_missing_ranges(nums, lower, upper) == []

    def test_returns_missing_range(self):
        nums = []
        lower, upper = -3, -1
        assert find_missing_ranges(nums, lower, upper) == ['-3->-1']

    def test_with_multiple_missing(self):
        nums = [0, 1, 3, 50, 75]
        lower, upper = 0, 99
        assert find_missing_ranges(nums, lower, upper) == ['2', '4->49', '51->74', '76->99']

    def test_highest_found_tracks_nums(self):
        nums = [0, 1]
        lower, upper = 0, 3
        assert find_missing_ranges(nums, lower, upper) == ['2->3']


class TestNotateRange:
    def test_catches_zero_range(self):
        lower, upper = 1, 1
        assert notate_range(lower, upper) == '1'
    
    def test_puts_an_arrow(self):
        lower, upper = 9, 17
        assert notate_range(lower, upper) == '9->17'

