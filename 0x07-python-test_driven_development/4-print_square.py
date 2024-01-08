#!/usr/bin/python3
"""Print Square Module"""


def print_square(size):
    """Function to Print Square"""

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for num in range(size):
        print('#' * size)
