CREATE TABLE users (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
    email VARCHAR(100)
);

CREATE TABLE categories (
    category_id INT PRIMARY KEY AUTO_INCREMENT,
    category_name VARCHAR(50)
);

CREATE TABLE products (
    product_id INT PRIMARY KEY AUTO_INCREMENT,
    product_name VARCHAR(100),
    category_id INT,
    price DECIMAL(10,2),
    FOREIGN KEY (category_id) REFERENCES categories(category_id)
);

CREATE TABLE orders (
    order_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    order_date DATE,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

CREATE TABLE order_items (
    order_item_id INT PRIMARY KEY AUTO_INCREMENT,
    order_id INT,
    product_id INT,
    quantity INT,
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

INSERT INTO users (name, email) VALUES
('Иван Иванов', 'ivan@example.com'),
('Мария Петрова', 'maria@example.com'),
('Алексей Смирнов', 'alexey@example.com');

INSERT INTO categories (category_name) VALUES
('Электроника'),
('Одежда'),
('Книги');

INSERT INTO products (product_name, category_id, price) VALUES
('Смартфон', 1, 15000.00),
('Футболка', 2, 500.00),
('Ноутбук', 1, 45000.00);

INSERT INTO orders (user_id, order_date) VALUES
(1, '2025-09-01'),
(2, '2025-09-02'),
(3, '2025-09-03');

INSERT INTO order_items (order_id, product_id, quantity) VALUES
(1, 1, 2),
(1, 2, 3),
(2, 3, 1), 
(3, 2, 2),
(3, 1, 1);

SELECT 
    o.order_id,
    u.name AS user_name,
    o.order_date,
    SUM(p.price * oi.quantity) AS total_amount
FROM orders o
JOIN users u ON o.user_id = u.user_id
JOIN order_items oi ON o.order_id = oi.order_id
JOIN products p ON oi.product_id = p.product_id
GROUP BY o.order_id, u.name, o.order_date;

SELECT 
    p.product_name,
    c.category_name
FROM products p
JOIN categories c ON p.category_id = c.category_id;

SELECT 
    c.category_name,
    COUNT(p.product_id) AS product_count
FROM categories c
LEFT JOIN products p ON c.category_id = p.category_id
GROUP BY c.category_name;

UPDATE products
SET price = 16000.00
WHERE product_name = 'Смартфон';

DELETE FROM order_items WHERE order_id = 2;
DELETE FROM orders WHERE order_id = 2;

ALTER TABLE users
ADD COLUMN status VARCHAR(20) DEFAULT 'active';

UPDATE users
SET status = 'vip'
WHERE user_id = (
    SELECT user_id FROM orders o
    JOIN (
        SELECT order_id, SUM(p.price * oi.quantity) AS total_amount
        FROM order_items oi
        JOIN products p ON oi.product_id = p.product_id
        GROUP BY order_id
        ORDER BY total_amount DESC
        LIMIT 1
    ) max_order ON o.order_id = max_order.order_id
);

