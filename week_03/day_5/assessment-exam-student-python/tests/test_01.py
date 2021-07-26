import pandas as pd
import numpy as np

data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
        'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
        'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(data, index=labels)


import pytest
from answers.question_01 import filter_dataframe

def test_on_number_of_rows():
    assert filter_dataframe(df).shape[0] == 8

def test_on_number_of_columns():
    assert filter_dataframe(df).shape[1] == 2

def test_on_index():
    assert filter_dataframe(df).index.tolist()  == df.dropna()._get_numeric_data().index.tolist()

def test_on_columns():
    assert filter_dataframe(df).columns.tolist()  == df.dropna()._get_numeric_data().columns.tolist()
