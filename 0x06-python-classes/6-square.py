#!/usr/bin/python3
"""Square Module"""


class Square:
    """Class that defines a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Method to initialize the square object."""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Property Getter for the size param

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
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Property Getter for the size param

        Returns:
                position of the square
        """

        return self.__position

    @position.setter
    def position(self, value):
        """Property Setter for the position param
        Args:
            Param1 (tuple): value of position
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
#        if len(value) != 2:
#            raise TypeError("position must be a tuple of 2 positive integers")
#        if not isinstance(value[0], int):
#            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(i, int) for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Method Area defines the area of the square object

        Returns:
                square of the size of the square

        """

        return self.__size ** 2

    def my_print(self):
        """Prints a square of size to the stdout
        """

        if self.size == 0:
            print()
        else:
            for i in range(self.position[1]):
                print()
            for i in range(0, self.size):
                for k in range(self.position[0]):
                    print(" ", end='')
                for j in range(self.size):
                    print('#', end='')
                print()
