class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(self.name + " says Woof!")


# Create object
d1 = Dog("Buddy", 3)

# Call method
d1.bark()