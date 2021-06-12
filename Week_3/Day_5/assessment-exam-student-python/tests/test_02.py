import pandas as pd

#Create a Dictionary of series
d = {'Name':pd.Series(['Andres','James','David','Vin','Steve','David','Jack',
   'Lee','David','Gasper','Betina','Andres']),
   'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])
}

#Create a DataFrame
df = pd.DataFrame(d)

import pytest
from answers.question_02 import compute_statistics


def test_on_return_tuple():
    assert type(compute_statistics(df)) == tuple

def test_on_tuple_length():
    assert len(compute_statistics(df)) == 3

def test_on_first_element_type():
    assert type(compute_statistics(df)[0]) == str

def test_on_second_element_type():
    assert type(compute_statistics(df)[1]) == float

def test_on_third_element_type():
    assert type(compute_statistics(df)[2]) == float

def test_on_correct_values():
    assert compute_statistics(df) == ('David', 
                                      pytest.approx(31.833333333333332, 0.1), 
                                      pytest.approx(0.9025000000000003,0.1))
