#!/usr/bin/python3
""" Inheriting from Base """
from models.base import Base


class Rectangle(Base):
    """ Class Rectangle inherting Base """

    def __init__(self, width, height, x=0, y=0, id=None):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if height <= 0:
            raise ValueError("height must be > 0")
        if x < 0:
            raise ValueError("x must be >= 0")
        if y < 0:
            raise ValueError("y must be >= 0")
        super().__init__(id=None)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    def area(self):
        """ Area public method """
        return self.width * self.height

    @property
    def width(self):
        """ Getter for width """
        return self.__width

    @width.setter
    def width(self):
        """ Setter for width """
        self.width = width

    @property
    def height(self):
        """ Getter for height """
        return self.__height

    @height.setter
    def height(self):
        """ Setter for height """
        self.height = height

    @property
    def x(self):
        """ Getter for x """
        return self.__x

    @x.setter
    def x(self):
        """ Setter for x """
        self.x = x

    @property
    def y(self):
        """ Getter for y """
        return self.__y

    @y.setter
    def y(self):
        """ Setter for y """
        self.y = y
