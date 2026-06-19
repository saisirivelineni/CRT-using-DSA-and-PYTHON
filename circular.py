class Circle:
    PI = 3.14

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return Circle.PI * self.radius * self.radius

    def circumference(self):
        return 2 * Circle.PI * self.radius