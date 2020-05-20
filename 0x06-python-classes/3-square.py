#!/usr/bin/python3
"""Writing class Square that defines a square by using attribute, try/except"""


class Square:
    """Class Square that defines a square using an private attribute.

    Attributes:
        size: private attribute to define square with
    """
    def __init__(self, size=0):
        """Intializing size as private attribute as well as insanisation of attribute
        Args:
            size: attribute
        """
        # Private attribute
        try:
            if isinstance(size, int):
                self.__size = size
        except TypeError:
            print("size must be an integer")
        else:
            if int(size) >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
    def area(self):
        return self
