#!/usr/bin/python3
""" Inheriting from Rectangle """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square class """
    def __init__(self, size):
        """ Instantiation of size """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """ Return area of Square """
        return self.__size ** 2

    def __str__(self):
        """ Print statement """
        return "[Rectangle] " + str(self.__size) + "/" + str(self.__size)
