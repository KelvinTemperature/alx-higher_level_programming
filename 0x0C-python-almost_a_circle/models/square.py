#!/usr/bin/python3
"""CLASS SQUARE MODULE"""
from rectangle import Rectangle


class Square(Rectangle):
    """class to define square"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width)

    def upd(self, id=None, size=None, x=None, y=None):
        if id != None:
            self.id = id
        if size != None:
            self.size = size
        if x != None:
            self.x = x
        if y != None:
            self.y = y

    def update(self, *args, **kwargs):
        if args:
            self.upd(*args)
        elif kwargs:
            self.upd(**kwargs)

    def to_dictionary(self):
        return {"id": self.id, "size": self.width, "x": self.x, "y": self.y}
