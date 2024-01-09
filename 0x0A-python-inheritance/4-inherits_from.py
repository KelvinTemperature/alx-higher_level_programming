#!/usr/bin/python3
"""inherits From Module"""


def inherits_from(obj, a_class):
    """
        function that checks if the object is an a class
        the inherited (directly or indirectly) from the
        specified class
    """

    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)
