import pytest
from solution import group_anagrams, standardise_anagram


class TestGroupAnagrams:
    def test_empty_input(self):
        strs = ['']
        groups = [['']]
        assert group_anagrams(strs) == groups

    def test_single_letter_words(self):
        strs = ['a']
        groups = [['a']]
        assert group_anagrams(strs) == groups
    
    def test_group_anagrams(self):
        strs = ["eat","tea","tan","ate","nat","bat"]
        groups = [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
        assert group_anagrams(strs) == groups


class TestStandardiseAnagram:
    def test_sorts_chars(self):
        anagram = 'eat'
        assert standardise_anagram(anagram) == 'aet'
