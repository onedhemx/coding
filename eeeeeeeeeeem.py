import sqlite3
import random

conn = sqlite3.connect("university.db")
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS students")
cur.execute("DROP TABLE IF EXISTS courses")
cur.execute("DROP TABLE IF EXISTS connection")

cur.execute("""
CREATE TABLE students (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER  NOT NULL
)
""")

cur.execute("""
CREATE TABLE courses (
    course_id INTEGER PRIMARY KEY AUTOINCREMENT,
    courses_name TEXT NOT NULL
)
""")

cur.execute("""
CREATE TABLE connection (
    connection_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    course_id INTEGER,
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
)
""")

names = ["Anna", "Boris", "Clara", "David", "Elena", "Fedor", "Galina", "Igor", "Tigran", "Lina", "Ursa", "Naga", "Tyler", "Popa", "Jopa", "мистир бысьт", "Dexter", "Rauf", "Faik", "Nix", "Radik"]
for _  in range(20):
  name = random.choice(names)
  age = random.randint(18, 60)
  cur.execute("INSERT INTO students (name, age) VALUES (?, ?)", (name, age))


courses_names = ["Математика", "Физика", "Информатика", "История", "Литература"]
for course_name in courses_names:
    cur.execute("INSERT INTO courses (courses_name) VALUES (?)", (course_name,))
    
cur.execute("SELECT student_id FROM students")
student_ids = [row[0] for row in cur.fetchall()]
cur.execute("SELECT course_id FROM courses")
course_ids = [row[0] for row in cur.fetchall()]

for student_id in student_ids:
    num_courses = random.randint(1, 3)  # студент может быть на 1-3 курсах
    enrolled_courses = random.sample(course_ids, num_courses)
    for course_id in enrolled_courses:
        cur.execute(
            "INSERT INTO connection (student_id, course_id) VALUES (?, ?)",
            (student_id, course_id)
        )



conn.commit()
conn.close()
