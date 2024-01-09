#!/usr/bin/python3
"""Base Geometry Module"""


class BaseGeometry():
    """Base Geometry Class"""

    def area(self):
        raise Exception("a() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
