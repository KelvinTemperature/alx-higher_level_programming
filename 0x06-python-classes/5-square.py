#!/usr/bin/python3
"""Square Module"""


class Square:
    """Class that defines a square."""

    def __init__(self, size=0):
        """Method to initialize the square object."""
        self.__size = size

    @property
    def size(self):
        """Property Setter for the size param

        Returns:
                size of the square
        """

        return self.__size

    @size.setter
    def size(self, value):
        """Property Setter for the size param
        Args:
            Param1 (int): value for size
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = int(value)

    def area(self):
        """Method Area defines the area of the square object

        Returns:
                square of the size of the square

        """

        return self.__size ** 2

    def my_print(self):
        """Prints a square of size to the stdout
        """

        if self.__size == 0:
            print()
        else:
            i = 0
            while (i < self.__size):
                j = 0
                for j in range(self.__size):
                    print("#", end='')
                print()
                i += 1
