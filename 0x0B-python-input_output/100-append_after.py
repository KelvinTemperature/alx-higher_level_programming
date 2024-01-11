#!/usr/bin/python3
"""APPEND AFTER KEY WORD LINE"""


def append_after(filename="", search_string="", new_string=""):
    """function to append new string at the
    end of line containing search string
    """

    lines = []
    with open(filename, 'r', encoding="utf-8") as fd:
        for line in fd:
            lines += [line]
            if line.find(search_string) != -1:
                lines += [new_string]

    with open(filename, 'w', encoding="utf-8") as f:
        f.write("".join(lines))
