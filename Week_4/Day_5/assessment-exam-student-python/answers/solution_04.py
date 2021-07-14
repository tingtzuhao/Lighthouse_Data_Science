SQL = """
         select d.department_name
            ,count(*) as number_of_employees
         from employees as e
         inner join departments as d
         on e.department_id = d.department_id
         group by d.department_name
         order by number_of_employees desc
      """