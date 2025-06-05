class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        
    def display_info(self):
        print(f'Имя: {self.name}, ID: {self.student_id}')
        
student = Student('dexter', 123498765095)
student.display_info()
