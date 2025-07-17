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


INSERT INTO authors(firstname, lastname) VALUES ("Уильям", "Шекспир");
INSERT INTO authors(firstname, lastname) VALUES ("Виктор", "Пелевин");
INSERT INTO authors(firstname, lastname) VALUES ("Чарльз", "Диккенс");

SELECT * FROM authors;

INSERT INTO publishers(name) VALUES ("Эксмо");
INSERT INTO publishers(name) VALUES ("Азбука-Аттикус");

SELECT * FROM publishers;


INSERT INTO books(title, author_id, publisher_id, year)  VALUES ('Гамлет', 1, 1, 1603);
INSERT INTO books(title, author_id, publisher_id, year)  VALUES ('Большие надежды', 1, 1, 1861);

SELECT * FROM books;
