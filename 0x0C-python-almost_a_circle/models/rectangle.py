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
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """ Getter for height """
        return self.__height

    @height.setter
    def height(self, height):
        """ Setter for height """
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """ Getter for x """
        return self.__x

    @x.setter
    def x(self, x):
        """ Setter for x """
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """ Getter for y """
        return self.__y

    @y.setter
    def y(self, y):
        """ Setter for y """
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
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

    def __str__(self):
        id = str(self.id)
        width = str(self.width)
        height = str(self.height)
        x = str(self.x)
        y = str(self.y)
        return '[Rectangle] ({}) {}/{} - {}/{}'.format(id, x, y, width, height)
