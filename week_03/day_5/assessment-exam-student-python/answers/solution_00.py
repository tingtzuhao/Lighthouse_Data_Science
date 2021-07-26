def filter_animals(df, animal):
    return df[(df.age < 3) & (df.animal == animal)]