SQL = """SELECT job_id, 
                MAX(salary) - MIN(salary) AS salary_span
         FROM employees
         WHERE job_id != 9
         GROUP BY job_id
         ORDER BY salary_span DESC
"""