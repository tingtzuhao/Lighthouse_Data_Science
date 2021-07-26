"""
 - Connect to the hr.db (stored in supporting-files directory) with sqlite3 
 - Write a query to get the names (first_name, last_name), salary, PF of all the employees (PF is calculated as 12% of salary)

Expected columns:
    - first_name	
    - last_name	
    - salary
    - PF

Notes:
    - You can connect to DB from Jupyter Lab/Notebook, explore the table and try different queries
    - In the variable 'SQL' store only the final query ready for validation 
"""


SQL = "SELECT first_name, last_name, salary, salary*0.12 as PF FROM employees"