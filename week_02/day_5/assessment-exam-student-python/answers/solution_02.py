def count_all(string):
    str_clean = [l for l in string if l.isalnum()]
    
    count_digits = len([l for l in str_clean if l.isdigit()])
    count_letters = len(str_clean) - count_digits

    return {'LETTERS': count_letters, 'DIGITS': count_digits}