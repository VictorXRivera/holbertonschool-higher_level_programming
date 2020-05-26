#!/usr/bin/python3
"""Rectangle class"""


class Rectangle:
    """Instantiation of Rectangle"""
    def __init__(self, width=0, height=0):
        # Private instance attribute
        self.__width = width
        # Private instance attribute
        self.__height = height
    
    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    
    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value
