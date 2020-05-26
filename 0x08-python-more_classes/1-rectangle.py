#!/usr/bin/python3
"""Rectangle class"""


class Rectangle:
    """
    defining a rectangle
    """
    def __init__(self, width=0, height=0):
        """instantiation of width and height
        """
        # Private attri. width
        self.__width = width
        #Private attri. height
        self.__height = height
    
    @property
    def height(self):
        """Getter for width
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter with edge cases
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value

    @property
    def width(self):
        """Getter for height
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter with edge cases
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__width = value
