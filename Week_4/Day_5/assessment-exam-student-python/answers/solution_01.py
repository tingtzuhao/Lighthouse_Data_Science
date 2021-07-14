def even_odd_transform(lst,repeat):
    for _ in range(repeat):
        lst = [v-2 if v % 2 == 0 else v+2 for v in lst]
    
    return lst