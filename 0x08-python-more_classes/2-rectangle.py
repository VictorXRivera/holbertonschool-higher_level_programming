#!/usr/bin/python3
"""Rectangle class"""

class Rectangle:
    """Defining Rectangle
    """
    def __init__(self, width=0, height=0):
        """Instantiation of width and height with edge cases
        Attributes:
            width: private instance attribute
            height: private instance attribute
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height

    def area(self):
        """Return area of rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """Return perimeter of rectangle
        """
        if self.__width is 0 or self.__height is 0:
            return 0
        return 2 * (self.__width + self.__height)

    @property
    def width(self):
        """Getter for width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter with edge cases
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter with edge cases
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
