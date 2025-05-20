class Pet:
    def __init__(self, name, animal_type, hunger=0, energy=10):
        self.name = name
        self.animal_type = animal_type
        self.hunger = hunger
        self.energy = energy

    def feed(self):
        self.hunger = max(self.hunger - 2, 0)

    def play(self):
        self.hunger = min(self.hunger + 1, 10)
        self.energy = max(self.energy - 1, 0)

    def get_status(self):
        return f"{self.animal_type.capitalize()} {self.name} (голод: {self.hunger}/10, энергия: {self.energy}/10)"

    def sleep(self):
        self.energy = min(self.energy + 3, 10)

    def run(self)
        if self.energy >= 2:
            self.energy -= 2
            print(f"{self.name} побежал и потерял немного энергии.")
        else:
            print(f"{self.name} слишком устал и не может бежать.")

pet1 = Pet("Барсик", "кот")
print(pet1.get_status())
pet1.feed()
print(pet1.get_status())
pet1.play()
print(pet1.get_status()
pet1.sleep()
print(pet1.get_status())
