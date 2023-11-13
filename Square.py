# Square
# Wayne Cook
# 6 November 2023
# Purpose: Define a square based on class rectangle;

from Rectangle import Rectangle

class Square(Rectangle):

    # Only need to initialize, Rectangle does rest
    def __init__(self, s):
        Rectangle.set_sides(self,s,s)
        Rectangle.set_type(self,"Square")
