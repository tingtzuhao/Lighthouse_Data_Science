import pytest
from answers.question_01 import mean

def test_on_number():
    res = type(mean(12345))
    assert res == float or res == int 

def test_on_float():
    assert type(mean(12345)) == float

def test_on_right_answer():
    assert mean(12345) == 3