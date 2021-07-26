/* SQL Exercise
====================================================================
We will be working with database northwind.db we have set up and connected to in the activity Connect to Remote PostgreSQL Database earlier.


-- MAKE YOURSELF FAIMLIAR WITH THE DATABASE AND TABLES HERE



https://www.w3resource.com/mysql-exercises/northwind/products-table-exercises/

--==================================================================
/* TASK I
-- Q1. Write a query to get Product name and quantity/unit.
*/
SELECT productname, quantityperunit
FROM products;

/* TASK II
Q2. Write a query to get most expense and least expensive Product list (name and unit price)
*/
SELECT MIN(unitprice), MAX(unitprice)
FROM products;

/* TASK III
Q3. Write a query to count current and discontinued products.
*/
SELECT Count(ProductName)
FROM Products
GROUP BY Discontinued;

/* TASK IV
Q4. Select all product names and their category names (77 rows)
*/
SELECT productname, categoryname
FROM products JOIN categories ON products.categoryid = categories.categoryid;

/* TASK V
Q5. Select all product names, unit price and the supplier region that don't have suppliers from USA region. (26 rows)
*/
SELECT productname, unitprice, region
FROM products JOIN suppliers ON products.supplierid = suppliers.supplierid
WHERE country != 'USA'

/* TASK VI
Q6. Get the total quantity of orders sold.( 51317)
*/
SELECT SUM(quantity) FROM order_details

/* TASK VII
Q7. Get the total quantity of orders sold for each order.(830 rows)
*/
SELECT SUM(quantity) FROM order_details
GROUP BY orderid

/* TASK VIII
Q8. Get the number of employees who have been working more than 5 year in the company. (9 rows)
*/
SELECT * FROM employees
WHERE EXTRACT(YEAR FROM AGE(CURRENT_TIMESTAMP, hiredate)) > 5