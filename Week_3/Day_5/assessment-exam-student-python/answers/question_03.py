"""
 - Connect to the hr.db (stored in supporting-files directory) with sqlite3 
 - Write a query to find the names (first_name, last_name) of the employees who have a manager who works for a department based in the United States. 
 

Expected columns:
    - first_name	
    - last_name	
    - manager_id

Notes:
    - Use tables employees, departments and locations
    - You shouldn’t use JOINs here. 
    - You can connect to DB from Jupyter Lab/Notebook, explore the table and try different queries
    - In the variable 'SQL' store only the final query ready for validation 
"""


SQL = """
SELECT first_name, last_name, manager_id
    FROM employees
    WHERE manager_id in (SELECT manager_id
                            FROM employees
                            WHERE department_id in (SELECT department_id
                                                        FROM departments
                                                        WHERE location_id in (SELECT location_id
                                                                                FROM locations
                                                                                WHERE country_id in (SELECT country_id
                                                                                                        FROM countries
                                                                                                        WHERE country_name is 'United States of America'))))"""