#!/usr/bin/python3
"""CLASS SQUARE MODULE"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
        class to define square
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Initialization"""

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """size getter"""

        return self.width

    @size.setter
    def size(self, value):
        """size setter"""

        self.width = value
        self.height = value

    def __str__(self):
        """str implementation for str"""

        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width)

    def upd(self, id=None, size=None, x=None, y=None):
        """mathod to set parameters"""

        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """update parameters depending on args or kwargs"""

        if args:
            self.upd(*args)
        elif kwargs:
            self.upd(**kwargs)

    def to_dictionary(self):
        """instance to dictionary"""

        return {"id": self.id, "size": self.width, "x": self.x, "y": self.y}
