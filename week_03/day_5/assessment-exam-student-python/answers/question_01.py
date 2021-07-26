import pandas as pd
import numpy as np

data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
        'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
        'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(data, index=labels)

"""
Write a function that takes dataframe df (defined above) as input and returns filtered dataframe with:
        - Only numeric columns
        - Only rows without any missing values

Notes:
        - Don’t select the columns and rows manually (use filtering)
"""

def filter_dataframe(df):
    num_cols = df.dtypes[df.dtypes != object].index.tolist()
    df_all = df.dropna()
    return(df_all[num_cols])