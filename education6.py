class Student:
    def __init__(self, name, student_id, grades):
        self.name = name
        self.student_id = student_id
        self.grades = grades
        
    def display_info(self):
        print(f'Имя: {self.name}, ID: {self.student_id}, Оценки: {self.grades}')
    
    def add_grade(self, grade):
        self.grades.append(grades)
        
    def get_average(self):
        return sum(self.grades)/len(self.grades)

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

group = Group()
student1 = Student('Dexter', 123498765095,  [5, 4 , 3])
student2 = Student('Broin Moser', 42578634234, [5, 5, 5 ])
student3 = Student('Bebra Morgan', 68238903424, [4, 5 , 2 ])
group.add_student(student1)
group.add_student(student2)
group.add_student(student3)
print(f'Средняя оценка 1 студента - {student1.get_average()}')
print(f'Средняя оценка 2 студента - {student2.get_average()}')
print(f'Средняя оценка 3 студента - {student3.get_average()}')
group.show_students()
