def filter_dataframe(df):
    return df.dropna()._get_numeric_data()