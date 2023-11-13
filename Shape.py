# Shapes base class
# Wayne Cook
# 6 November 2023
# Purpose: Create a base class to build uniform shapes commands

class Shape:
    # define a local variable
    type = None
    # All methods must pass in "self" as first parameter
    def __init__(self, name):
        type = name

    # Allow type to be set outside of init.
    def set_type(self,name):
        #print(f"In Shape with {name}") # for debugging
        self.type = name

    def get_type(self):
        return self.type

    # Now for two virtual functions
    # Expect subclasses to define these functions.
    def get_area(self) -> float:
        return None

    def get_perimeter(selfself) -> float:
        return None
