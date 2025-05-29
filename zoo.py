class Animal:
    def __init__(self, name, species, age):
        
        """
        класс Animal
        
        :param name: Кличка животного
        :param species: Вид животного
        :param age: Возраст животного
        """
        
        self.name  = name
        self.species = species
        self.age  = age
        
    def make_sound(self, ):
        print(f'{self.name} гав гав гав')
        
    def info(self):
        return f"кличка {self.name}\n вид {sel.species} \n Возраст {sel.age}"
        
class Zoo:
    def __init__(self, animals):
        self.animals = []
        
        def add_animal(self, animal: Animal):
             """Добавляет животное в зоопарк"""
            self.animals.append(animal)
            print(f"Добавлено животное: {animal.name} ({animal.species})")
            
    def show_animals(self):
        """Выводит информацию о всех животных"""
        if not self.animals:
            print("В зоопарке пока нет животных")
            return
        
        print("\nСписок животных в зоопарке:")
        for i, animal in enumerate(self.animals, 1):
            print(f"\nЖивотное #{i}")
            print(animal.info())
    
    def make_all_sounds(self):
        """Заставляет всех животных подать голос"""
        if not self.animals:
            print("В зоопарке пока нет животных")
            return
    
    
