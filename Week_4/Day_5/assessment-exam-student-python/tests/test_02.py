import pytest
import pandas as pd
from answers.question_02 import compute_total_sale
from supporting_files.data_loader import load_excel

df = load_excel('supporting_files/SaleData.xlsx')



def test_on_data_type():
    assert isinstance(compute_total_sale(df), pd.DataFrame)

def test_on_correct_shape():
    assert compute_total_sale(df).shape == (8, 3)

def test_on_ordered_values():
    res = compute_total_sale(df)
    assert res['Sale_amt'].equals(res.sort_values('Sale_amt', ascending=False)['Sale_amt'])

def test_on_correct_answer():
    assert compute_total_sale(df).equals(df.groupby(['Region','Manager'])[['Sale_amt']].sum().sort_values('Sale_amt', ascending=False).reset_index())

