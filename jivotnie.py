class Animal:
    def make_sound(self):
        print("животное живет")

class Dog(Animal):
    def make_sound(self):
        print("гаав гав ав гав гав")

class Cat(Animal):
    def make_sound(self):
        print("мяу мяу мяу мур мур мяу")


animals = [Dog(), Cat(), Animal()]

for animal in animals:
    animal.make_sound()
