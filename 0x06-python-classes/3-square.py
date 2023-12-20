#!/usr/bin/python3
class Square:
    """Class Square defines a square object
    """

    def __init__(self, size=0):
        """Initialize method that stores the size of the square

        Args:
            param1 (int): size of the square

        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = int(size)

    def area(self):
        """Method Area defines the area of the square object

        Returns:
                square of the size of the square

        """

        return self.__size ** 2
