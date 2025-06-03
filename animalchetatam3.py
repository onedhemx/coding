class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age 
        
    def display_info(self):
        print(f'Имя: {animal.name}, Вид: {animal.species}, Возраст: {animal.age}')
        
animal = Animal('собвака', 'кошка', 1)
animal.display_info()


class Shelter:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)
            
            
shshsh = Shelter()
animal = Animal("Мур", "собака", 2)
shshsh.add_animal(animal)

for animals in shshsh.add_animal:
    animals.display_info
