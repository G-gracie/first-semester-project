-- SQL queries for retrieving insights

--SELECT * FROM customers;

--SELECT * FROM products

--SELECT * FROM orders

--SELECT * FROM products
--WHERE category = 'Electronics';

--Aggregation

--SELECT AVG(price) AS average_price FROM products;

--SELECT COUNT(*) AS total_orders FROM orders;

--SELECT p.product_name, SUM(o.quantity * p.price) AS total_revenue
--FROM orders o
--JOIN products p ON o.product_id = p.product_id
--GROUP BY p.product_name;

--Joins
--SELECT o.order_id, c.name AS customer_name, p.product_name, o.quantity, o.order_date
--FROM orders o
--INNER JOIN customers c ON o.customer_id = c.customer_id
--INNER JOIN products p ON o.product_id = p.product_id;

--SELECT c.name AS customer_name, o.order_id, o.order_date
--FROM customers c
--LEFT JOIN orders o ON c.customer_id = o.customer_id
--ORDER BY c.name;

--SELECT p.product_name, o.order_id, o.quantity
--FROM products p
--LEFT JOIN orders o ON p.product_id = o.product_id
--ORDER BY p.product_name;
