CREATE TABLE students (
    id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    group_name VARCHAR(20)
);

CREATE TABLE teachers (
    id INT PRIMARY KEY AUTO_INCREMENT,
    full_name VARCHAR(100) NOT NULL,
    department VARCHAR(50)
);

CREATE TABLE courses (
    id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(100) NOT NULL,
    semester INT,
    exam_type VARCHAR(20)
);

-- students
INSERT INTO students (first_name, last_name, group_name) VALUES
('Алексей', 'Иванов', 'Группа A'),
('Мария', 'Петрова', 'Группа B'),
('Дмитрий', 'Смирнов', 'Группа A');

-- teachers
INSERT INTO teachers (full_name, department) VALUES
('Ирина Кузнецова', 'Математика'),
('Сергей Волков', 'Физика');

-- courses
INSERT INTO courses (title, semester, exam_type) VALUES
('Математика 1', 1, 'экзамен'),
('Физика 1', 1, 'зачёт'),
('Информатика', 2, 'экзамен'),
('История', 2, 'зачёт');

SELECT * FROM students
WHERE group_name = 'Группа A';

SELECT * FROM courses
WHERE exam_type = 'экзамен';

SELECT * FROM teachers
WHERE department = 'Математика';

UPDATE students
SET last_name = 'Новиков'
WHERE id = 1;

UPDATE courses
SET exam_type = 'экзамен'
WHERE id = 2;

DELETE FROM teachers
WHERE full_name = 'Сергей Волков';
