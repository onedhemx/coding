CREATE TABLE customers (
    customer_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
    phone VARCHAR(15)
);

DESCRIBE customers;

CREATE TABLE pizzas (
    pizza_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
    category VARCHAR(20),
    price DECIMAL(5,2) CHECK ( price>=0 )
);

CREATE TABLE employees (
    employee_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
    role VARCHAR(30),
    salary DECIMAL(8,2) CHECK (salary > 0)
    
);

CREATE TABLE orders (
    order_id  INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT,
    order_date DATE,
    employee_id INT,
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

CREATE TABLE order_items (
    order_id INT, 
    pizza_id INT, 
    PRIMARY KEY (order_id, pizza_id),
    quantity INT CHECK(quantity > 0),
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (pizza_id) REFERENCES pizzas(pizza_id)
    
);

INSERT INTO customers (name, phone)
VALUE
('ВАСЯ ПУПКИН','89606543475'),
('Мария Иванова','88128745544'),
('ЮРКО ГАГАРЕНКО','88005553555');

SELECT * FROM customers;

INSERT INTO employees (name, role, salary)
VALUES

INSERT INTO pizzas (name, price)
values
('пепероби','750'),
('Терияки','460'),
('Чоризо фреш ','800');

INSERT INTO orders (customer_id, order_date, employee_id)
VALUES (1, CURDATE(), 2);

SET @last_order_id = LAST_INSERT_ID();

INSERT INTO order_items (order_id, pizza_id, quantity)
VALUES
(@last_order_id, 1, 1),
(@last_order_id, 3, 1);

INSERT INTO orders (customer_id, order_date, employee_id)
VALUES (2, CURDATE(), 1);

SET @new_order_id = LAST_INSERT_ID();

INSERT INTO order_items (order_id, pizza_id, quantity)
VALUES (@new_order_id, 2, 2);

UPDATE pizzas 
SET pizzas = price * 1.15;
SELECT * FROM pizzas;

UPDATE clients
SET phone_number = '89034760011'
WHERE client_id = 1;

ALTER TABLE pizzas
ADD COLUMN category VARCHAR(20);

UPDATE pizzas SET category = 'ВЕГАНСКАЯ' WHERE pizza_id IN (1, 2, 3);
UPDATE pizzas SET category = 'ОСТРАЯ' WHERE pizza_id IN (2, 3);



https://onlinetestpad.com/ev62sampou6wo

