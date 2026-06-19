class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, roll):
        super().__init__(name, age)
        self.roll = roll

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

s = Student("Ravi", 20, 101)
t = Teacher("Kiran", 35, "Maths")

print(s.name, s.roll)
print(t.name, t.subject)