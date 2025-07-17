class Student:
    def __init__(self, id, name, group, gpa):
        self.id = id
        self.name = name
        self.group = group
        self.gpa = gpa

    def __str__(self):
        return f"{self.id}: {self.name} (Группа {self.group}, GPA: {self.gpa})"


class StudentModel:
    def __init__(self):
        self.students = []
        self.next_id = 1

    def add_student(self, name, group, gpa):
        student = Student(self.next_id, name, group, gpa)
        self.students.append(student)
        self.next_id += 1
        return student

    def get_all_students(self):
        return self.students.copy()

    def delete_student(self, id):
        for i, student in enumerate(self.students):
            if student.id == id:
                return self.students.pop(i)
        return None


class StudentView:
    def show_menu(self):
        print("\n=== Управление студентами ===")
        print("1. Добавить студента")
        print("2. Удалить студента")
        print("3. Показать всех студентов")
        print("4. Выход")

    def get_choice(self):
        return input("Выберите действие: ")

    def get_student_input(self):
        name = input("ФИО студента: ")
        group = input("Группа: ")
        gpa = float(input("Средний балл (GPA): "))
        return name, group, gpa

    def get_student_id(self):
        return int(input("ID студента для удаления: "))

    def show_students(self, students):
        print("\n--- Список студентов ---")
        if not students:
            print("Студентов нет")
        for student in students:
            print(student)

    def show_message(self, message):
        print(f">> {message}")



class StudentController:
    def __init__(self):
        self.model = StudentModel()
        self.view = StudentView()

    def run(self):
        while True:
            self.view.show_menu()
            choice = self.view.get_choice()

            if choice == '1':
                self._add_student()
            elif choice == '2':
                self._delete_student()
            elif choice == '3':
                self._show_students()
            elif choice == '4':
                break
            else:
                self.view.show_message("Неверный ввод!")

    def _add_student(self):
        data = self.view.get_student_input()
        student = self.model.add_student(*data)
        self.view.show_message(f"Добавлен: {student.name}")

    def _delete_student(self):
        student_id = self.view.get_student_id()
        student = self.model.delete_student(student_id)
        if student:
            self.view.show_message(f"Удален: {student.name}")
        else:
            self.view.show_message("Студент не найден")

    def _show_students(self):
        students = self.model.get_all_students()
        self.view.show_students(students)
