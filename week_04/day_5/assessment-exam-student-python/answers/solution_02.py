def compute_total_sale(df):
    return df.groupby(['Region','Manager'])[['Sale_amt']].sum().sort_values('Sale_amt', ascending=False).reset_index()