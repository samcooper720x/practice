import pytest

from solution import Solution


class TestSolution:
    def test_longest_palindromic_substring(self):
        assert (
            Solution.longest_palindrome('babad') == 'bab' or
            Solution.longest_palindrome('babad') == 'aba'
        )
        assert Solution.longest_palindrome('a') == 'a'
        assert (
            Solution.longest_palindrome('ac') == 'a' or
            Solution.longest_palindrome('ac') == 'c'
        )

    def test_longest_with_double_centre(self):
        assert Solution.longest_palindrome('cbbd') == 'bb'
        assert Solution.longest_palindrome('bb') == 'bb'
        assert Solution.longest_palindrome('ccc') == 'ccc'
