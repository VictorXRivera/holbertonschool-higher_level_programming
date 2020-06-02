#!/usr/bin/python3
"""Empty class Geometry"""


class BaseGeometry:
    """Geometry Class"""

    def integer_validator(self, name, value):
        """Edge cases
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        self.value = value
        self.name = name
    
    def area(self):
        """Area"""
        raise Exception("area() is not implemented")


class Rectangle(BaseGeometry):
    """Rectangle Class"""
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
