class Triangle:
    def __init__(self, b, h,):
        self.height = h
        self.base = b

    def area(self):
        return self.base/2 * self.height

Triangle = Triangle(5, 10)
print(Triangle.area())
