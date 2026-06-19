class Car:
    def __init__(self, brand):
        self.brand = brand

    def show(self):
        print(self.brand)


# Create object
c1 = Car("Ford")

# Call method
c1.show()