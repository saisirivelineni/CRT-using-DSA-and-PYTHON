class Laptop:
    def __init__(self, brand, ram, storage):
        self.brand = brand
        self.ram = ram
        self.storage = storage

    def display_specs(self):
        print(self.brand, self.ram, self.storage)

l = Laptop("HP", "8GB", "512GB")
l.display_specs()