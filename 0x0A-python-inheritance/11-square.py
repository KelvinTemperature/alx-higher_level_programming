#!/usr/bin/python3
"""Square Module"""


Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """Class Square from Rectangle class"""

    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(self.__size, self.__size)

    def area(self):
        return self.__size ** 2

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
