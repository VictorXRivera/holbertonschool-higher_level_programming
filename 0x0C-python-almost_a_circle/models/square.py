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

    def update(self, *args, **kwargs):
        arg = len(args)
        if arg >= 1:
            self.id = args[0]
        elif "id" in kwargs:
            self.id = kwargs["id"]
        if arg >= 2:
            self.size = args[1]
        elif "size" in kwargs:
            self.size = kwargs["size"]
        if arg >= 3:
            self.x = args[2]
        elif "x" in kwargs:
            self.x = kwargs["x"]
        if arg >= 4:
            self.y = args[3]
        elif "y" in kwargs:
            self.y = kwargs["y"]
