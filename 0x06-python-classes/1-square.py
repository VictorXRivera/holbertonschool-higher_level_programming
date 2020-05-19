#!/usr/bin/python3
"""Writing class Square that defines a square by using attribute"""


class Square:
    """Class Square that defines a square using an private attribute.

    Attributes:
        size: private attribute to define square with
    """
    def __init__(self, size):
        """Intializing size as private attribute as well as insanisation of attribute
        Args:
            size: attribute
        """
        # Private attribute
        self.__size = size
