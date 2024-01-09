#!/usr/bin/python3
"""MyInt Module"""


class MyInt(int):
    """Class MyInt"""

    def __eq__(self, other):
        int_cp = super().__ne__(other)
        return int_cp

    def __ne__(self, other):
        int_cp = super().__eq__(other)
        return int_cp
