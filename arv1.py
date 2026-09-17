class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Dog(Animal):
    def make_sound(self):
        print("The dog barks!")

class Cat(Animal):
    def make_sound(self):
        print("The cat meows!")

class Cow(Animal):
    def make_sound(self):
        print("The cow says moo!")

animals = [
    Dog("Max", 5),
    Cat("Gabby", 4),
    Cow("Ronald", 7),
]

for animal in animals:
    animal.make_sound()