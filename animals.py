class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age 
        
animal = Animal('Kot', 'dog', 5)

print(f'Имя: {animal.name}, Вид: {animal.species}, Возраст: {animal.age}')


