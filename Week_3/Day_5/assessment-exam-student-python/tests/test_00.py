import pandas as pd
import numpy as np

data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
        'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
        'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(data, index=labels)


import pytest
from answers.question_00 import filter_animals


def test_on_return_type():
    assert isinstance(filter_animals(df,'cat'), pd.DataFrame)

def test_on_number_of_rows():
    assert len(filter_animals(df,'cat')) == 2

def test_on_return_type_when_bad_animal():
    assert isinstance(filter_animals(df,'pigeon'), pd.DataFrame)

def test_on_correct_answer():
    assert filter_animals(df,'cat').equals(df[(df.age < 3) & (df.animal =='cat')])
