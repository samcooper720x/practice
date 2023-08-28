import pytest
from solution import length_of_longest_substring


class TestSolution:
    def test_catches_empty_input(self):
        assert length_of_longest_substring('') == 0

    def test_catches_repeats(self):
        s = "bbbbb"
        assert length_of_longest_substring(s) == 1

    def test_no_repeating_characters(self):
        s = 'abcabcbb'
        assert length_of_longest_substring(s) == 3

    def test_gets_substring_not_subsequence(self):
        s = 'pwwkew'
        assert length_of_longest_substring(s) == 3

    def test_first_two_repeat(self):
        s = 'xxzqi'
        assert length_of_longest_substring(s) == 4

