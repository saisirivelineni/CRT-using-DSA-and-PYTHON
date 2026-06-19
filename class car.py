class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def start_engine(self):
        print(self.brand, "car started")

c1 = Car("Toyota", "Red")
c1.start_engine()