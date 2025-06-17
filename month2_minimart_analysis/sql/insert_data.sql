-- SQL script to insert sample data
--customers data
INSERT INTO customers (name, email, join_date) VALUES
('Grace Emmanuel', 'grace.emmanuel@gmail.com.com', '2023-06-01'),
('Samuel Obi', 'samuelobi@gmail.com', '2023-07-15'),
('Linda Wilson', 'linda@gmail.com', '2023-08-10'),
('Wasiz Sani', 'ibrahim.sani@yahoo.com', '2024-01-20'),
('Ngozi Nwachukwu', 'ngozi.nwachukwu@outlook.com', '2024-03-12');

--products data
INSERT INTO products (product_name, category, price) VALUES
('Wireless Mouse', 'Electronics', 25.99),
('Bluetooth Headphones', 'Electronics', 79.50),
('Water Bottle', 'Home & Kitchen', 12.00),
('Notebook (A5)', 'Stationery', 4.99),
('Smartphone Stand', 'Accessories', 9.75);


--order data
INSERT INTO orders (customer_id, product_id, quantity, order_date) VALUES
(1, 1, 2, '2024-06-01'),
(2, 3, 1, '2024-06-05'),
(3, 2, 1, '2024-06-07'),
(4, 4, 5, '2024-06-10'),
(5, 5, 3, '2024-06-12');
