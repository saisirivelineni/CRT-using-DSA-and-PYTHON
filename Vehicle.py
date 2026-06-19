class Vehicle:
    def start(self):
        print("Vehicle Started")

class Bike(Vehicle):
    pass

class Car(Vehicle):
    pass

class Bus(Vehicle):
    pass

b = Bike()
b.start()

c = Car()
c.start()