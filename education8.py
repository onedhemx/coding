class Student:
    def __init__(self, name, student_id, grades):
        self.__name = name
        self.__student_id = student_id
        self.__grades = grades

    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__student_id

    def get_grades(self):
        return self.__grades

    def display_info(self):
        print(f'Имя: {self.__name}, ID: {self.__student_id}, Оценки: {self.__grades}')

    def add_grade(self, grade):
        self.__grades.append(grade)
    def get_average(self):
        return sum(self.__grades)/len(self.__grades)

class Group:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def show_students(self):
        if not self.students:
            print('Список пуст')
        else:
            for student in self.students:
                student.display_info()

    def find_by_name(self, name):
        for student in self.students:
            if student.get_name() == name:
                return student
        return None

group = Group()
student1 = Student('Dexter', 123498765095, [5, 4, 3])
student2 = Student('Broin Moser', 42578634234, [5, 5, 5])
student3 = Student('Bebra Morgan', 68238903424, [4, 5, 2])
group.add_student(student1)
group.add_student(student2)
group.add_student(student3)
name_to_find = 'loh'
found_student = group.find_by_name(name_to_find)
if found_student:
    print('Найден студент:')
    found_student.display_info()
else:
    print(f'Студент с именем "{name_to_find}" не найден.')
print(f'Средняя оценка 1 студента - {student1.get_average()}')
print(f'Средняя оценка 2 студента - {student2.get_average()}')
print(f'Средняя оценка 3 студента - {student3.get_average()}')
group.show_students()
