import pandas as pd
import sys
from supporting_files.data_loader import load_excel

df = load_excel('supporting_files/SaleData.xlsx')


"""
Write a function to count the manager wise sale (sale_cnt)
and mean value of sale amount (sale_mean). 
Order the output dataframe by sale_cnt, starting with the highest.
Output should be DataFrame with 3 columns (order is important):
    - Manager
    - sale_cnt
    - sale_mean
and numeric index starting with 0 (after sorting).
"""

def compute_agg_stats(df):
    final_df = pd.DataFrame()
    final_df['Manager'] = df.groupby('Manager').size().index
    final_df['sale_cnt'] = df.groupby('Manager').size().values
    final_df['sale_mean'] = df.groupby('Manager')['Sale_amt'].mean().values
    final_df = final_df.sort_values('sale_cnt', ascending=False).reset_index(drop=True)
    return final_df