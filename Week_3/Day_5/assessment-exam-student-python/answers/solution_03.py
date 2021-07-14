SQL = """SELECT first_name,
                last_name,
                manager_id
         FROM employees
         WHERE manager_id IN (SELECT employee_id
                              FROM employees
                              WHERE department_id IN (SELECT department_id 
                                                      FROM departments 
                                                      WHERE location_id IN (SELECT location_id 
                                                                            FROM locations 
                                                                            WHERE country_id = 'US')))""" 