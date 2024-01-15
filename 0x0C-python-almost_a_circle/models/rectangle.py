#!/usr/bin/python3
"""RECTANGLE MODEL"""
from models.base import Base


class Rectangle(Base):
    """
        class rectangle implementation
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructors"""

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """width getter"""

        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """height getter"""

        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """x getter"""

        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""

        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """y getter"""

        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""

        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """area method"""

        return self.__width * self.__height

    def display(self):
        """display method to print to stdout"""

        for i in range(self.__y):
            print()

        for i in range(self.__height):
            print(" " * self.__x, end='')
            print('#' * self.__width)

    def __str__(self):
        """str method implementation"""

        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.__x, self.__y, self.__width, self.__height)

    def upd(self, id=None, width=None, height=None, x=None, y=None):
        """set the values of the class"""

        if id is not None:
            self.id = id
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """set value depending on args or kwargs"""

        if args:
            self.upd(*arg)
        elif kwargs:
            self.upd(**kwargs)

    def to_dictionary(self):
        """class properties to dictionary"""

        return {"id": self.id, "width": self.__width,
                "height": self.__height, "x": self.__x, "y": self.__y}
