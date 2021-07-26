import pandas as pd
import sys
from supporting_files.data_loader import load_excel

df = load_excel('supporting_files/SaleData.xlsx')
# df = pd.read_excel('SaleData.xlsx',engine='openpyxl')


"""
Write a Pandas program to find the total sale amount (Sale_amt) region and manager wise. 
Order the dataframe by Sale_amt, starting with the highest.
Output should be DataFrame with 3 columns (order is important):
    - Region
    - Manager
    - Sale_amt
and numeric index starting with 0 (after sorting).
"""

def compute_total_sale(df):
    final_df = df.groupby(['Region', 'Manager'])[['Sale_amt']].sum().sort_values('Sale_amt', ascending=False).reset_index()
    return final_df