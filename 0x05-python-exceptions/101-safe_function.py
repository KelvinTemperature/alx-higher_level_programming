#!/usr/bin/python3
import sys

def safe_function(fct, *args):
    try:
        result = fct(*args)
    except Exception as al:
        print("Exception: {}".format(al), file=sys.stderr)
        return None
    else:
        return result
