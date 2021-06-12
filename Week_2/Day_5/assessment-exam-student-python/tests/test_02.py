import pytest
from answers.question_02 import count_all

def test_on_dictionary():
    assert type(count_all("Hello World")) == dict

def test_on_correct_keys():
    res = count_all("Hello World")
    assert res.get('LETTERS') is not None and res.get('DIGITS') is not None

def test_on_datatypes():
    res = count_all("H3ll0 Wor1d")
    assert type(res.get('LETTERS')) == int  and type(res.get('DIGITS')) == int

def test_on_string_without_numbers():
    res = count_all("Hello World")
    assert res.get('LETTERS') == 10 and res.get('DIGITS') == 0

def test_on_string_without_letters():
    res = count_all("149990")
    assert res.get('LETTERS') == 0 and res.get('DIGITS') == 6

def test_on_correct_values():
    res = count_all("H3ll0 Wor1d")
    assert res.get('LETTERS') == 7  and res.get('DIGITS') == 3