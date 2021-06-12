SQL = """SELECT first_name,
                last_name,
                department_id 
         FROM employees
         WHERE department_id IN (3,10) 
         ORDER BY department_id
"""