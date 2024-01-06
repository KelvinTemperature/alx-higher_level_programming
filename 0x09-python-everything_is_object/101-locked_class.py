#!/usr/bin/python3
"""module that containts a class that avoids
dynmaically created attributes
"""


class LockedClass:
    """Locked Class"""

    __slots__ = ['first_name']

    def __init__(self):
        """ Init method """
        pass
