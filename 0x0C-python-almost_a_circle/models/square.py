#!/usr/bin/python3
""" Class Square """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class Constructor """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Getter for size """
        return self.width

    @size.setter
    def size(self, size):
        """ Setter for size """
        self.width = size
        self.height = size

    def __str__(self):
        id = str(self.id)
        size = str(self.size)
        x = str(self.x)
        y = str(self.y)
        return '[Square] ({}) {}/{} - {}'.format(id, x, y, size)
