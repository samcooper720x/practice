import pytest
from solution import longest_palindrome, get_centers


class TestSolution:
    def test_empty_input(self):
        s = ''
        assert longest_palindrome(s) == ''

    def test_single_char(self):
        s = 'a'
        assert longest_palindrome(s) == 'a'

    def test_two_chars(self):
        s = 'ac'
        assert longest_palindrome(s) == 'a' or longest_palindrome(s) == 'c'

    def test_palindrome_in_middle(self):
        s = 'cbbd'
        assert longest_palindrome(s) == 'bb'

    def test_two_options(self):
        s = 'babad'
        assert longest_palindrome(s) == 'bab' or longest_palindrome(s) == 'aba'

    def test_double_char(self):
        s = 'bb'
        assert longest_palindrome(s) == 'bb'

    def test_all_same_char(self):
        s = 'ccc'
        assert longest_palindrome(s) == 'ccc'


class TestGetCenters:
    def test_returns_indices(self):
        s = 'abcde'
        centers = [0, 1, 2, 3]
        assert get_centers(s) == centers

    def test_finds_centers_between_chars(self):
        s = 'abba'
        centers = [0, 1, 1.5, 2]
        assert get_centers(s) == centers


@pytest.mark.skip(reason='for deprecated n3 solution')
class TestReverse:
    def test_length_one(self):
        s = 'a'
        assert reverse(s) == 'a'

    def test_length_five(self):
        s = 'abcde'
        assert reverse(s) == 'edcba'

