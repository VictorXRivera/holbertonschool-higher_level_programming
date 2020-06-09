#!/usr/bin/python3
""" Inheriting from Base """
from models.base import Base


class Rectangle(Base):
    """ Class Rectangle inherting Base """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ Getter for width """
        return self.__width

    @width.setter
    def width(self, width):
        """ Setter for width """
        self.__width = width

    @property
    def height(self):
        """ Getter for height """
        return self.__height

    @height.setter
    def height(self, height):
        """ Setter for height """
        self.__height = height

    @property
    def x(self):
        """ Getter for x """
        return self.__x

    @x.setter
    def x(self, x):
        """ Setter for x """
        self.__x = x

    @property
    def y(self):
        """ Getter for y """
        return self.__y

    @y.setter
    def y(self, y):
        """ Setter for y """
        self.__y = y

    def area(self):
        """ Area public method """
        return self.width * self.height

    def display(self):
        """ Pound printer """
        if self.width == 0 or self.height == 0:
            return None
        symbol = '#'
        shape = ""
        for height in range(self.height):
            for width in range(self.width):
                shape += str(symbol)
            if height is not self.height - 1:
                shape += "\n"
        print(shape)
