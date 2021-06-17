class Pets:

    dogs = []

    def __init__(self, dogs):
        self.dogs = dogs
    
    def walk(self):
        self.dogs.walk()       


class Dog:
    species = 'mammal'
    is_hungry = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        return f'{self.name} is {self.age} years old'

    def speak(self, sound):
        return f'{self.name} says {sound}'

    def eat(self):
        self.is_hungry = False

    def walk(self):
        stri = 'walking'
        print(f"{self.name} is {stri}")


class RussellTerrier(Dog):
    def run(self, speed):
        return f'{self.name} runs {speed}'


class Bulldog(Dog):
    def run(self, speed):
        return f'{self.name} runs {speed}'


dog1 = Dog('Tom', 1)
dog2 = Dog('Jerry', 2)
dog3 = Dog('Butt', 3)
pet1 = Pets(dog1)
pet2 = Pets(dog2)
pet3 = Pets(dog3)
pet1.walk()
pet2.walk()
pet3.walk()