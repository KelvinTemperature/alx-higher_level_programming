#!/usr/bin/python3
"""CLASS TO DICTIONARY/JSON"""


def class_to_json(obj):
    """function that return the dictionary description of an obj"""

    dict_obj = {}

    if hasattr(obj, "__dict__"):
        res = obj.__dict__.copy()
    return res
