#!/usr/bin/python3
"""APPEND TEXT TO FILE"""


def append_write(filename="", text=""):
    """function to append text to a file"""

    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
