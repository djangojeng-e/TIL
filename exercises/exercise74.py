class Circle():
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius**2*3.14


# Create circle instance with radius 2

circle = Circle(2)
print(circle.area())