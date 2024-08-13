# single inheritance is a type of inheritance where a class inherits properties and behaviours from a single parent class. this is the simplest and most common form of inheritance.

class Animal:

    def __init__(self, name, species) -> None:
        self.name = name
        self.species = species
  
    def make_sound(self):
        print("sound made by the animmal")

class Cat(Animal):

    def __init__(self, name, breed) -> None:
        Animal.__init__(self, name, species='cat')

        self.breed = breed

    def make_sound(self):
        print("meaww")

c1= Cat("kitten", "cat")
c1.make_sound()