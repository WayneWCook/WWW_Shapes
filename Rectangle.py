# Rectangle
# Wayne Cook
# 6 November 2023
# Purpose: Define a rectangle based on class shape;

from Shape import Shape

class Rectangle(Shape):
    # Define local class variables
    __height = 1.0
    __width = 1.0
    def __init__(self, h,w):
        self.__height = h
        self.__width = w
        #print(f"Dimentions: {self.__height} x {self.__width}")
        Shape.set_type(self,"Rectangle")

    def set_sides(self, h, w):
        self.__height = h
        self.__width = w

    def get_area(self):
        return self.__height*self.__width

    def get_perimeter(self):
        return 2 * self.__height + 2 * self.__width
