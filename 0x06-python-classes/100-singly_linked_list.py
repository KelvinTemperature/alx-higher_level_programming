#!/usr/bin/python3
"""Node Module"""

class Node:
    """Class Node of a singly linked list"""

    def __init__(self, data, next_node=None):
        """Initializes the class object"""
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """Property getter for data param"""
        return self.__data

    @data.setter
    def data(self, value):
        """Property setter for data param"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """Property getter for next_node param"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Property setter for next_node param"""
        if not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value

class SinglyLinkedList:
    """Class defines a singly linked list"""
    def __int__(self):
        """initializes the class object"""
        self.__head = head

