#!/usr/bin/python3
"""BASE CLASS MODULE"""
import json
import csv
from os import path


class Base:
    """Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """
            initialization
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
            static method to return json string
            of list_dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
            class method to save list to file
        """

        if list_objs is not None:
            list_objs = [i.to_dictionary() for i in list_objs]

        with open("{}.json".format(cls.__name__), 'w', encoding="utf-8") as f:
            f.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """
            Class method to convert json string to
            a list
        """

        if json_string is None or not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """method that loads a dictionary to an instance"""

        from models.rectangle import Rectangle
        from models.square import Square

        if cls is Rectangle:
            dum = Rectangle(1, 1)
        elif cls is Square:
            dum = Square(1)
        else:
            dum = None

        dum.update(**dictionary)
        return dum

    @classmethod
    def load_from_file(cls):
        """method to load file to instances"""

        file_name = "{}.json".format(cls.__name__)

        if not path.isfile(file_name):
            return []
        with open(file_name, 'r', encoding="utf-8") as f:
            return [cls.create(**d) for d in cls.from_json_string(f.read())]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        '''Saves object to csv file.'''
        from models.rectangle import Rectangle
        from models.square import Square
        if list_objs is not None:
            if cls is Rectangle:
                list_objs = [[o.id, o.width, o.height, o.x, o.y]
                             for o in list_objs]
            else:
                list_objs = [[o.id, o.size, o.x, o.y]
                             for o in list_objs]
        with open('{}.csv'.format(cls.__name__), 'w', newline='',
                  encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        '''Loads object to csv file.'''
        from models.rectangle import Rectangle
        from models.square import Square
        ret = []
        with open('{}.csv'.format(cls.__name__), 'r', newline='',
                  encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                row = [int(r) for r in row]
                if cls is Rectangle:
                    d = {"id": row[0], "width": row[1], "height": row[2],
                         "x": row[3], "y": row[4]}
                else:
                    d = {"id": row[0], "size": row[1],
                         "x": row[2], "y": row[3]}
                ret.append(cls.create(**d))
        return ret

    @staticmethod
    def draw(list_rectangles, list_square):
        """opens window and draw all rectangle and squares"""

        import turtle
        import time
        from random import randrange

        turtle.Screen().colormode(255)
        for i in list_rectangles + list_squares:
            t = turtle.Turtle()
            t.color((randrange(255), randrange(255), randrange(255)))
            t.pensize(1)
            t.penup()
            t.pendown()
            t.setpos((i.x + t.pos()[0], i.y - t.pos()[1]))
            t.pensize(10)
            t.forward(i.width)
            t.left(90)
            t.forward(i.height)
            t.left(90)
            t.forward(i.width)
            t.left(90)
            t.forward(i.height)
            t.left(90)
            t.end_fill()

        time.sleep(5)
