#!/usr/bin/python3
"""The same class instance module"""


def is_same_class(obj, a_class):
    """Function to check the object is an instance of the class"""

    return type(obj) is a_class
