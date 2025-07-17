CREATE TABLE authors (
    id INT NOT NULL AUTO_INCREMENT,
    firstname VARCHAR(50) NOT NULL,
    lastname VARCHAR(50) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE publishers (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE books (
    id INT NOT NULL AUTO_INCREMENT,
    title VARCHAR(100) NOT NULL,
    author_id INT NOT NULL,
    publisher_id INT NOT NULL,
    year INT NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (author_id) REFERENCES authors(id),
    FOREIGN KEY (publisher_id) REFERENCES publishers(id) 
);

-- Вставка авторов
INSERT INTO authors(firstname, lastname) VALUES ('Уильям', 'Шекспир');
INSERT INTO authors(firstname, lastname) VALUES ('Виктор', 'Пелевин');
INSERT INTO authors(firstname, lastname) VALUES ('Чарльз', 'Диккенс');
INSERT INTO authors(firstname, lastname) VALUES ('Эдгар', 'Аллан По');

-- Вставка издателей
INSERT INTO publishers(name) VALUES ('Эксмо');
INSERT INTO publishers(name) VALUES ('Азбука-Аттикус');

-- Вставка книг (исправленная версия)
INSERT INTO books (title, author_id, publisher_id, year) VALUES
('Гамлет', 1, 1, 1603),
('Ромео и Джульетта', 1, 1, 1597),
('Generation П', 2, 2, 1999),
('Оливер Твист', 3, 2, 1838),
('Лигейя', 4, 2, 1838);  -- Исправлены ID автора и издателя

-- Просмотр всех книг
SELECT * FROM books;

-- Поиск книг 1838 года
SELECT b.title AS 'Название книги',
       CONCAT(a.firstname, ' ', a.lastname) AS 'Автор',
       p.name AS 'Издательство',
       b.year AS 'Год издания'
FROM books b
JOIN authors a ON b.author_id = a.id
JOIN publishers p ON b.publisher_id = p.id
WHERE b.year = 1838;

-- Обновляем год издания для книги "Гамлет"
UPDATE books
SET year = 1601
WHERE title = 'Гамлет' AND author_id = 1;  -- Уильям Шекспир

-- Проверяем изменение
SELECT b.title, 
       CONCAT(a.firstname, ' ', a.lastname) AS author,
       b.year AS new_year
FROM books b
JOIN authors a ON b.author_id = a.id
WHERE b.title = 'Гамлет';


-- Удаление книг, изданных до 1870 года
DELETE FROM books
WHERE year < 1870;

-- Проверка оставшихся книг
SELECT b.title, 
       CONCAT(a.firstname, ' ', a.lastname) AS author,
       p.name AS publisher,
       b.year
FROM books b
JOIN authors a ON b.author_id = a.id
JOIN publishers p ON b.publisher_id = p.id;
