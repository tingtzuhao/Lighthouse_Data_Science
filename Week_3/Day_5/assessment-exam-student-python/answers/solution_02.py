def compute_statistics(df):
    mcm = df['Name'].mode().values[0]
    avg_age = df['Age'].mean()
    q1 = df['Rating'].quantile(0.25)
    q3 = df['Rating'].quantile(0.75)
    IQR = float(q3 - q1)

    return mcm,avg_age,IQR