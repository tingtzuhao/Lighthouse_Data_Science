import pytest
from answers.question_01 import even_odd_transform

def test_on_return_list():
    assert type(even_odd_transform([3, 4, 9], 3)) == list

def test_on_correct_length():
    assert len(even_odd_transform([3, 4, 9], 3)) == 3

def test_on_integers():
    res = even_odd_transform([3, 4, 9], 3)
    is_integer = [type(v) == int for v in res]

    assert all(is_integer)

def test_on_correct_answer():
    assert even_odd_transform([3, 4, 9], 3) == [9, -2, 15]