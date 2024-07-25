class Shape():
    def what_am_i(self):
        return print("Я - фигура!")
        
class Rectangle(Shape):
    def __init__(self, side1, side2, side3):
        self.s1 = side1
        self.s2 = side2
        self.s3 = side3

    def calc_per_rect(self):
        return self.s1+self.s2+self.s3
Rectangle = Rectangle(4, 5, 6)
print(Rectangle.calc_per_rect())
Rectangle.what_am_i()

class Square(Shape):
    def __init__(self,side1,side2,side3,side4):
        Square.s1 = side1
        Square.s2 = side2
        Square.s3 = side3
        Square.s4 = side4

    def change_per(self, diff):
        Square.s1 += diff
        Square.s2 += diff
        Square.s3 += diff
        Square.s4 += diff

    def calc_per_square(self):
        return Square.s1+Square.s2+Square.s3+Square.s4

SQ1 = Square(5, 4, 3, 5)
n = input("Input number: ")
SQ1.change_per(int(n))
SQ1.calc_per_square()
print(SQ1.calc_per_square())
SQ1.what_am_i()

