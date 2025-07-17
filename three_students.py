def get_student_info(student_num):
    print(f"\nВведите данные студента {student_num}:")
    name = input("Имя: ")
    age = int(input("Возраст: "))
    gpa = float(input("Средний балл: "))
    group = input("Группа: ").upper()
    return {'name': name, 'age': age, 'gpa': gpa, 'group': group}

def analyze_students(students):
    # Находим студента с максимальным баллом
    top_student = max(students, key=lambda x: x['gpa'])
    
    # Вычисляем средний возраст
    avg_age = sum(s['age'] for s in students) / len(students)
    
    # Проверяем, есть ли студенты из одной группы
    groups = [s['group'] for s in students]
    duplicate_groups = [g for g in set(groups) if groups.count(g) > 1]
    has_same_group = len(duplicate_groups) > 0
    
    return top_student, avg_age, has_same_group, duplicate_groups

def main():
    students = []
    for i in range(1, 4):
        students.append(get_student_info(i))
    
    top_student, avg_age, has_same_group, duplicate_groups = analyze_students(students)
    
    print("\nРезультаты:")
    print(f"Студент с самым высоким баллом: {top_student['name']}, {top_student['age']} лет, "
          f"группа {top_student['group']}, балл {top_student['gpa']}")
    print(f"Средний возраст студентов: {avg_age:.1f} лет")
    
    if has_same_group:
        print(f"Есть студенты из одной группы: Да (группа {', '.join(duplicate_groups)})")
    else:
        print("Есть студенты из одной группы: Нет")

if __name__ == "__main__":
    main()
