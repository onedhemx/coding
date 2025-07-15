class Pet:
    def __init__(self, name: str, animal_type: str, age: int):
        self.name = name
        self.animal_type = animal_type
        self.age = age
    
    def __str__(self):
        return f"{self.name} | {self.animal_type} | {self.age}"

def save_to_file(self, pets, filename):
    with open(filename, "w", encoding="utf-8") as file:
        for pet in pets:
            file.write(f"{pet.name}\n{pet.animal_type}\n{pet.age}\n")

def load_from_file(filename):
    pets = []
    try:
        with open(filename, "r", encoding="utf-8") as file:
            lines = file.read().splitlines()
            for i in range(0, len(lines), 3):
                if i + 2 < len(lines):
                    pets.append(Pet(lines[i], lines[i+1], int(lines[i+2])))
    except FileNotFoundError:
        pass
    return pets

def main():
    pets = load_from_file()
    
    while True:
        print("\n1. Добавить питомца")
        print("2. Сохранить в файл")
        print("3. Загрузить из файла")
        print("4. Показать всех питомцев")
        print("0. Выход")
        choice = input("Выберите действие: ")
        
        if choice == "1":
            name = input("Имя: ")
            animal_type = input("Вид: ")
            age = int(input("Возраст: "))
            pets.append(Pet(name, animal_type, age))
            print("Пет добавлен")
        
        elif choice == "2":
            save_to_file(pets)
            print("Данные сохранены")
        
        elif choice == "3":
            pets = load_from_file()
            print("Данные загружены")
        
        elif choice == "4":
            if not pets:
                print("Список питомцев пуст.")
            else:
                print("\nСписок питомцев:")
                for i, pet in enumerate(pets, 1):
                    print(f"{i}. {pet}")
        
        elif choice == "0":
            print("Выход.  .  .")
            break
        
        else:
            print("❌")

if __name__ == "__main__":
    main()
