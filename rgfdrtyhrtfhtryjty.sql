CREATE TABLE groups (
    id INT AUTO_INCREMENT PRIMARY KEY,
    group_name VARCHAR(50) NOT NULL
);

CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(110) NOT NULL,
    group_id INT NOT NULL,
    FOREIGN KEY (group_id) REFERENCES groups(id)
);

insert INTO groups (group_name) values ('группа ни');
insert INTO groups (group_name) values ('группа бэ');
insert INTO groups (group_name) values ('группа пу');

INSERT INTO students (name, group_id) VALUES ("Хамзат", 2);
INSERT INTO students (name, group_id) VALUES ("Аввакум", 3);
INSERT INTO students (name, group_id) VALUES ("Ивон", 1);
INSERT INTO students (name, group_id) VALUES ("Демитрий", 2);
INSERT INTO students (name, group_id) VALUES ("Эльбрус", 3);
