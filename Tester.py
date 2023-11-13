# Testing of shapes
# Wayne Cook
# 6 November 2023
# Purpose: Try creating an instance of Circle and printing area and perimeter.

# In order to access the __init__ function in Circle, import must be as follows:
from Circle import Circle
from Rectangle import Rectangle
from Square import Square

def main():
    rad = float(input("What is the radius of your circle? "))
    circ1 = Circle(rad)
    print("Your figure is a ",circ1.get_type())
    print("The area is: ",circ1.get_area())
    print("The perimeter is: ",circ1.get_perimeter())
# The the rectangle code
    h = float(input("What is the height of your rectangle? "))
    w = float(input("What is the width of your rectangle? "))
    rec1 = Rectangle(h, w)
    print("Your figure is a ",rec1.get_type())
    print("The area is: ",rec1.get_area())
    print("The perimeter is: ",rec1.get_perimeter())
# Try the Square code
    s = float(input("What is the Square's side? "))
    sqr1 = Square(s)
    print("Your figure is a ",sqr1.get_type())
    print("The area is: ", sqr1.get_area())
    print("The perimeter is: ",sqr1.get_perimeter())

main()
