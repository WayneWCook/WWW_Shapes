# Octogon
# Wayne Cook
# 6 November 2023
# Purpose: Define a triangle based on class shape;
# Add a comment to force a change.

from Shape import Shape

class Octogon(Shape):
    # Define local class variables
    __side = 1.0

    def __init__(self,side):
        self.__side = side
        #print(f"Dimentions: {self.__side} x 8")
        Shape.set_type(self,"Octogon")

    def set_dimensions(self, side):
        self.__side = side

    def get_area(self):
        return self.__side

    def get_perimeter(self):
        return self.__side * 8
