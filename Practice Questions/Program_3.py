# Write a Rectangle class in Python language, allowing you to build a rectangle with length and width attributes.
# Create a Perimeter() method to calculate the perimeter of the rectangle and a Area() method to calculate the area of ​​the rectangle.
# Create a method display() that display the length, width, perimeter and area of an object created using an instantiation on rectangle class.
# Create a Parallelepipede child class inheriting from the Rectangle class and with a height attribute and another Volume() method to calculate the volume of the Parallelepiped.

import traceback
import sys


class Rectangle:
    def __init__(self, lenght_rect, bredth_rect):
        self.length_rect = lenght_rect
        self.bredth_rect = bredth_rect

    def perimeter(self):
        return f'Perimeter Of Rectangle :   {2 * (self.length_rect * self.bredth_rect)}'

    def area(self):
        return f'Area Of Rectangle :   {(self.length_rect * self.bredth_rect)}'

    def __str__(self) -> str:
        return f'\n\nLength of Rectangle : {self.length_rect}\nBredth Of Rectangle : {self.bredth_rect}'

class Parallelepipede(Rectangle):
    def __init__(self, lenght_rect, bredth_rect, height_rect):
        Rectangle.__init__(self, lenght_rect, bredth_rect)
        self.height_rect = height_rect

    def volume(self):
        return f'Volume Of Rectangle    :   {self.length_rect * self.bredth_rect * self.height_rect}'

    def __str__(self) -> str:
        return f'{super().__str__()}\nheight Of Rectangle : {self.height_rect}'


if __name__ == "__main__":
    input_container_for_check = ['Yes', 'yes', '1']
    while True:
        try:
            lenght_rect = float(input('Enter the Length :   '))
            bredth_rect = float(input('Enter the Breath :   '))
            break
        except ValueError as e:
            print('Please, Use Correct Input\n{}\n'.format(sys.exc_info()[1]))

    if(str(input('Want Volume (Yes / No) : ')) in input_container_for_check):
        while True:
            try:
                height_rect = float(input('Enter the Height :   '))
                rectangle_object = Rectangle(lenght_rect, bredth_rect)
                parallelepipede_object = Parallelepipede(lenght_rect, bredth_rect, height_rect)
                print(rectangle_object.area())
                print(rectangle_object.perimeter())
                print(parallelepipede_object.volume())
                break
            except ValueError:
                print('Please, Use Correct Value\n')
            except (NameError, TypeError):
                print('Error, Function\n')

    else:
        rectangle_object = Rectangle(lenght_rect, bredth_rect)

    
    

    

