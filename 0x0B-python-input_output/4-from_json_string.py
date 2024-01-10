#!/usr/bin/python3
"""FROM JSON TO STRING"""


import json


def from_json_string(my_str):
    """function to return object from json string"""

    return json.loads(my_str)
