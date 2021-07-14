def compute_agg_stats(df):
    return df.groupby('Manager').agg(sale_cnt = ('Item', 'count'),
                                     sale_mean = ('Sale_amt', 'mean')).sort_values('sale_cnt', ascending=False).reset_index()