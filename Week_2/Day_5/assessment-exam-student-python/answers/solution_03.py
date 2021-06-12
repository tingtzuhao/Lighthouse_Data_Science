SQL = """SELECT first_name,
                last_name,
                salary, 
                0.12*salary as PF
         FROM employees
"""