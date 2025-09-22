DROP TABLE IF EXISTS employees;
DROP TABLE IF EXISTS sales;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS products;

-- Employees Table
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    name VARCHAR(50),
    department_id INT,
    job_title VARCHAR(50),
    salary DECIMAL(10, 2)
);

INSERT INTO employees VALUES
(1, 'Alice', 101, 'Engineer', 70000),
(2, 'Bob', 101, 'Engineer', 80000),
(3, 'Charlie', 102, 'Analyst', 65000),
(4, 'Daisy', 103, 'Manager', 90000),
(5, 'Ethan', 102, 'Analyst', 70000);

-- Sales Table
CREATE TABLE sales (
    sale_id INT PRIMARY KEY,
    product_id INT,
    category_id INT,
    sales_amount DECIMAL(10, 2),
    sale_date DATE
);

INSERT INTO sales VALUES
(1, 201, 10, 1000.00, '2024-01-01'),
(2, 202, 10, 1500.00, '2024-01-03'),
(3, 203, 11, 2000.00, '2024-01-04'),
(4, 201, 10, 500.00, '2024-01-05'),
(5, 203, 11, 1000.00, '2024-01-06');

-- Orders Table
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    product_id INT,
    order_date DATE,
    region VARCHAR(50),
    status VARCHAR(20),
    sales_amount DECIMAL(10, 2)
);

INSERT INTO orders VALUES
(1001, 301, 201, '2024-02-01', 'North', 'Shipped', 500.00),
(1002, 302, 202, '2024-02-01', 'North', 'Pending', 600.00),
(1003, 303, 203, '2024-02-02', 'South', 'Shipped', 800.00),
(1004, 301, 202, '2024-02-03', 'North', 'Shipped', 900.00),
(1005, 304, 203, '2024-02-03', 'South', 'Cancelled', 750.00),
(1006, 302, 201, '2024-02-04', 'North', 'Pending', 300.00);

-- Products Table
CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(50),
    category_id INT,
    price DECIMAL(10, 2)
);

INSERT INTO products VALUES
(201, 'Widget', 10, 25.00),
(202, 'Gadget', 10, 40.00),
(203, 'Thingamajig', 11, 100.00),
(204, 'Doohickey', 12, 10.00);


-- Question 1 Query

SELECT
    p.category_id,
    p.product_name,
    SUM(s.sales_amount) AS total_sales
FROM
    sales s
JOIN
    products p ON s.product_id = p.product_id
GROUP BY
    p.category_id, p.product_name
HAVING
    SUM(s.sales_amount) = (
        SELECT MAX(total_sales)
        FROM (
            SELECT
                SUM(sales_amount) AS total_sales
            FROM
                sales s2
            JOIN
                products p2 ON s2.product_id = p2.product_id
            WHERE
                p2.category_id = p.category_id
            GROUP BY
                s2.product_id
        ) AS category_sales
    )
ORDER BY
    p.category_id;

-- Question 2 Query

SELECT
    e.department_id,
    AVG(e.salary) AS avg_salary
FROM
    employees e
GROUP BY
    e.department_id
ORDER BY
    avg_salary DESC
LIMIT 1;

-- Question 3 Query

SELECT
    e.employee_id,
    e.name,
    e.salary,
    e.department_id
FROM
    employees e
JOIN (
    SELECT
        department_id,
        AVG(salary) AS avg_salary
    FROM
        employees
    GROUP BY
        department_id
) AS dept_avg ON e.department_id = dept_avg.department_id
WHERE
    e.salary > dept_avg.avg_salary;


-- Question 4 Query

SELECT
    o.region,
    o.customer_id,
    COUNT(o.order_id) AS order_count
FROM
    orders o
GROUP BY
    o.region, o.customer_id
HAVING
    COUNT(o.order_id) = (
        SELECT MAX(order_count)
        FROM (
            SELECT COUNT(o2.order_id) AS order_count
            FROM orders o2
            WHERE o2.region = o.region
            GROUP BY o2.customer_id
        ) AS region_orders
    )
ORDER BY
    o.region;

-- Question 5 Query

SELECT
    p.category_id,
    AVG(p.price) AS avg_category_price
FROM
    products p
GROUP BY
	p.category_id
HAVING
    AVG(p.price) > (SELECT AVG(price) FROM products);


-- Question 6 Query

SELECT
    p.product_id,
    p.product_name
FROM
    products p
LEFT JOIN
    orders o ON p.product_id = o.product_id
WHERE
    o.order_id IS NULL;



