# Circle
# Wayne Cook
# 6 November 2023
# Purpose: Define a circle based on class shape;

from Shape import Shape

class Circle(Shape):
    __radius = 1.0
    def __init__(self, rad):
        self.__radius = rad
        Shape.set_type(self,"Circle")

    def get_area(self):
        return self.__radius*self.__radius * 3.14159

    def get_perimeter(self):
        return 2 * self.__radius * 3.14159
