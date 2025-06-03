class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age 
        
    def display_info(self):
        print(f'Имя: {animal.name}, Вид: {animal.species}, Возраст: {animal.age}')
        
animal = Animal('собвака', 'кошка', 1)
animal.display_info()
