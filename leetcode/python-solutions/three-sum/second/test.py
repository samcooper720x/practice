import pytest

from solution import Solution


class TestSolution:
    def test_bad_inputs(self):
        assert Solution.three_sum(self, []) == []
        assert Solution.three_sum(self, [0]) == []
        assert Solution.three_sum(self, [0, 1]) == []

    def test_returns_three_sum(self):
        nums = [-1, 0, 1, 2, -1, -4]
        output = [[-1, -1, 2], [-1, 0, 1]]
        assert Solution.three_sum(self, nums) == output

    def test_with_one_element_recurring(self):
        nums = [-2, 0, 1, 1, 2]
        output = [[-2, 0, 2], [-2, 1, 1]]
        assert Solution.three_sum(self, nums) == output


