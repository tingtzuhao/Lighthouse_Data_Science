import pytest
import pandas as pd
from answers.question_03 import compute_agg_stats
from supporting_files.data_loader import load_excel

df = load_excel('supporting_files/SaleData.xlsx')


def test_on_data_type():
    assert isinstance(compute_agg_stats(df), pd.DataFrame)

def test_on_correct_shape():
    assert compute_agg_stats(df).shape == (4, 3)

def test_on_ordered_values():
    res = compute_agg_stats(df)
    assert res['sale_cnt'].equals(res.sort_values('sale_cnt', ascending=False)['sale_cnt'])

def test_on_correct_answer():
    assert compute_agg_stats(df).equals(df.groupby('Manager').agg(sale_cnt = ('Item', 'count'),
                                     sale_mean = ('Sale_amt', 'mean')).sort_values('sale_cnt', ascending=False).reset_index())
