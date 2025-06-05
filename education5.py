class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        
    def display_info(self):
        print(f'Имя: {self.name}, ID: {self.student_id}')

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
student1 = Student('dexter', 123498765095)
student2 = Student('Broin Moser', 425786)
student3 = Student('Bebra Morgan', 6823890)
group.add_student(student1)
group.add_student(student2)
group.add_student(student3)
group.show_students()
print(group.students)
