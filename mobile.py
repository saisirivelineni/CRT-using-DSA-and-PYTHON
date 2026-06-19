class Mobile:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def make_call(self):
        print("Calling...")

    def show_details(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Price: {self.price}")


phone = Mobile("Samsung", "S24", 80000)

phone.show_details()
phone.make_call()