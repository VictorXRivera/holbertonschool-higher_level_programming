#!/usr/bin/python3
""" Inheriting from Base """
from models.base import Base


class Rectangle(Base):
    """ Class Rectangle inherting Base """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id=None)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

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
