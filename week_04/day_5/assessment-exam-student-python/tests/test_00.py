import pytest
from answers.question_00 import pie_chart

def test_on_dictionary():
    assert type(pie_chart({ "a": 1, "b": 2 })) == dict

def test_on_correct_keys():
    res = pie_chart({ "a": 1, "b": 2 })
    assert res.get('a') is not None and res.get('b') is not None

def test_on_data_types():
    res = pie_chart({ "a": 1, "b": 2 })
    assert type(res.get('a')) == float and type(res.get('b')) == float

def test_on_correct_answer():
    res = pie_chart({ "a": 30, "b": 15, "c": 55 })
    assert res == { "a": 108, "b": 54, "c": 198 }

