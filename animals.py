class Animal:
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Bow Bow")

class Cat(Animal):
    def sound(self):
        print("Meow")

class Cow(Animal):
    def sound(self):
        print("Moo")

Dog().sound()
Cat().sound()
Cow().sound()