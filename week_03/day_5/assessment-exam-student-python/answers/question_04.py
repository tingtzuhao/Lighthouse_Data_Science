"""
 - Connect to the hr.db (stored in supporting-files directory) with sqlite3 
 - Write a query to get the difference (salary_span) between min and max salary for each job ID excluding programmer (job_id = 9) and sort it, starting with the highest salary_span.



Expected columns:
    - job_id	
    - salary_span

Notes:
    - Use employees table
    - You can connect to DB from Jupyter Lab/Notebook, explore the table and try different queries
    - In the variable 'SQL' store only the final query ready for validation 
"""


SQL = """
SELECT job_id, max(salary)-min(salary) as salary_span FROM employees
WHERE job_id != 9
GROUP BY job_id
ORDER BY salary_span DESC"""