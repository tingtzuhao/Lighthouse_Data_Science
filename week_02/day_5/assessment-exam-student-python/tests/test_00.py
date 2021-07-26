import pytest
from answers.question_00 import filter_list

def test_on_return():
    assert filter_list('abc123') is not None

def test_on_return_list():
    assert type(filter_list('abc123')) == list

def test_on_correct_length():
    assert len(filter_list([1, 2, 3, "a", "b", 4])) == 4

def test_on_returns_integers():
    assert filter_list([1, 2, 3, "a", "b", 4]) == [1,2,3,4]

def test_on_empty_list():
    assert filter_list(['a','v','c']) == []
    

