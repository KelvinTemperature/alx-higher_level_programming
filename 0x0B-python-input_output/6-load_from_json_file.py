#!/usr/bin/python3
"""LOAD FROM JSON FILE"""
import json


def load_from_json_file(filename):
    """function to load from json file"""

    with open(filename, 'r', encoding="utf-8") as f:
        x = json.load(f)
        return x
