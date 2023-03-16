#  Define a Circle class allowing to create a circleC (O, r) with center O(a, b) and radius r using the constructor:
from math import pi

class Circle:
    def __init__(self, a_, b_, radius) -> None:
        self.a_ = a_
        self.b_ = b_
        self.radius = radius

# 2 - Define a Area() method of the class which calculates the area of ​​the circle.
    def AreaOfCircle(self, ):
        return pi * self.radius ** 2
# 3 - Define a Perimeter() method of the class which allows you to calculate the perimeter of the circle.
    def Perimeter(self):
        return 2 * pi * self.radius
# 4 - Define a testBelongs() method of the class which allows to test whether a point A(x, y) belongs to the circle C(O, r) or not
    def testBelongs(self):
        pass