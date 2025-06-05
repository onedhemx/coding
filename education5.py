class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        
    def display_info(self):
        print(f'Имя: {self.name}, ID: {self.student_id}')
        
student = Student('dexter', 123498765095)
student.display_info()

class Group:
    def __init__(self):
        self.students = []
        
    def add_student(self, student):
        self.students.append(student)
        
    def show_students(self):
        if self.student == 0 :
            print('Список пуст')
        else:
            for student in self.student:
                student.display_info()
group = Group()
group.add_student('Broin Moser')
group.add_student('Bebra Morgan')
print(group.students)
