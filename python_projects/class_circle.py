import math
class Circle:
    def __init__(self, r):
        self.radius = r
        self.pnum = math.pi

    def area(self):
        return self.pnum * (self.radius**2)

radius = input("Type radius of the circle:")
r_int = int(radius)
circle = Circle(r_int)
print(circle.area())

        
