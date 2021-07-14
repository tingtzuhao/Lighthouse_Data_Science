"""
Write a function that takes a string and calculates the number of letters and digits within it. Return the result in a dictionary.

Examples:
    count_all("Hello World") ➞ { "LETTERS":  10, "DIGITS": 0 }

    count_all("H3ll0 Wor1d") ➞ { "LETTERS":  7, "DIGITS": 3 }

    count_all("149990") ➞ { "LETTERS": 0, "DIGITS": 6 }

Notes:
    - Tests contain only alphanumeric characters.
    - Spaces are not letters.
    - All tests contain valid strings.
    - The function should return dictionary

"""

def count_all(string):
    
    str_nspace = string.replace(' ', '')

    lst_str = []

    for ele in str_nspace:
        lst_str.append(ele)
    
    result = {'LETTERS': int, 'DIGITS': int}

    letters = []
    digits = []
    
    for ele in lst_str:
        if ele.isdigit():
            digits.append(int(ele))
        else:
            letters.append(ele)

    result['LETTERS'] = len(letters)
    result['DIGITS'] = len(digits)

    return(result)