"""
 - Connect to the hr.db (stored in supporting-files directory) with sqlite3 
 - Write a query to display the names (first_name, last_name) and department ID of all employees in departments 3 or 10 in ascending order by department ID.


Expected columns:
    - first_name	
    - last_name	
    - department_id

Notes:
    - You can connect to DB from Jupyter Lab/Notebook, explore the table and try different queries
    - In the variable 'SQL' store only the final query ready for validation 
"""


SQL = '''
SELECT first_name, last_name, department_id FROM employees
WHERE department_id IS 3 OR department_id IS 10
ORDER BY department_id ASC'''
