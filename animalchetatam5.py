class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age 
        
    def display_info(self):
        print(f'Имя: {animal.name}, Вид: {animal.species}, Возраст: {animal.age}')
        
animal = Animal('елвин', 'барсук', 18)
animal.display_info()
animal = Animal('собака', 'кошка', 1)
animal.display_info()
animal = Animal('пук', 'собака', 12)
animal.display_info()



class Shelter:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)
        
    def show_animals(self):
        if self.animals == 0:
            print( "Приют пуст")
        else:
            animal.display_info()
            
    def find_by_species(self, species_name):
        x = False 
        for animal in self.animals:
            if animal.species == species_name:
                animal.display_info()
                x = True
                
        if not x:
            print(f"нет животных вида {species_name}")
                
            
        
            
            
shshsh = Shelter()
animal = Animal("Мур", "собака", 3)
shshsh.add_animal(animal)
for a in shshsh.animals:
    a.display_info()
    
shshsh.find_by_species("со")
    
