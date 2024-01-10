#!/usr/bin/python3
"""CLASS STUDENT"""


class Student():
    """Class Student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        obj = self.__dict__.copy()

        if type(attrs) is list:

            for val in attrs:
                if type(val) is not str:
                    return obj

            dicta = {}

            for i in range(len(attrs)):
                for key in obj:
                    if attrs[i] == key:
                        dicta[key] = obj[key]

            return dicta

        return obj
