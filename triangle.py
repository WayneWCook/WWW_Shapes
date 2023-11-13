# Triangle
# Wayne Cook
# 6 November 2023
# Purpose: Define a triangle based on class shape;

from Shape import Shape

class Rectangle(Shape):
    # Define local class variables
    __height = 1.0
    __width = 1.0
    def __init__(self, height,base):
        self.__height = height
        self.__base = base
        #print(f"Dimentions: {self.__height} x {self.__width}")
        Shape.set_type(self,"Triangle")

    def set_dimensions(self, height,base):
        self.__height = height
        self.__base = base

    def get_area(self):
        return self.__height*self.__base /2.0

    def get_perimeter(self):
        return self.__height + 2 * self.__base
