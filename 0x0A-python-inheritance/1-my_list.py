#!/usr/bin/python3
"""Mylist Module"""


class MyList(list):
    """Class that inherites from list"""

    def print_sorted(self):
        list_sorted = self.copy()
        list_sorted.sort()
        print(list_sorted)
