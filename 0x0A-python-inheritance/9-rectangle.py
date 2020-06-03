#!/usr/bin/python3
""" Rectangle class inheriting from BaseGeometry """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Child class Rectangle """

    def __init__(self, width, height):
        """ Instantiation of width and height """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ Return area of Rectangle """
        return self.__width * self.__height

    def __str__(self):
        """ Print statement """
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
