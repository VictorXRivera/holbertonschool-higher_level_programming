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
        self.__size = size

    def area(self):
        """Returning square area
        """
        return self.__size ** 2

    @property
    def size(self):
        """Getter
        """
        return self.__size

    @size.setter
    def size(self, value):
        """setter
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """Printing # if true or empty space if false
        """
        if self.__size == 0:
            print("")
        for char in range(0, self.__size):
            for symbol in range(0, self.__size - 1):
                print("#", end="")
            print("#")
