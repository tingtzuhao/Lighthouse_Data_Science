"""
Create a function that returns the mean of all digits.

Example:
    mean(42) ➞ 3.0

    mean(12345) ➞ 3.0

    mean(666) ➞ 6.0

Notes:
    - Function should always return float
"""


def mean(digits):
    lst_str = []
    for ele in str(digits):
        lst_str.append(ele)
    
    digi_sum = 0.0

    for ele in lst_str:
        digi_sum += float(ele)
        digi_avg = digi_sum / len(lst_str)
    
    return digi_avg