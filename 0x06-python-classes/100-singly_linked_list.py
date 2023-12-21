#!/usr/bin/python3
"""Node Module"""


class Node:
    """Class Node of a singly linked list"""

    def __init__(self, data, next_node=None):
        """Initializes the class object"""
        self.data = data
        self.next_node = next_node

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
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value

class SinglyLinkedList:
    """Class defines a singly linked list"""
    def __str__(self):
        retn = ""
        ptr = self.__head

        while ptr is not None:
            retn += str(ptr.data)
            if ptr.next_node is not None:
                retn += "\n"
            ptr = ptr.next_node

        return retn

    def __init__(self):
        """initializes the class object"""
        self.__head = None

    def sorted_insert(self, value):
        """Inserts a new node in the correct sorted position"""
        new_node = Node(value, None)
        ptr = self.__head

        if ptr is None:
            self.__head = new_node
            return

        if value < ptr.data:
            new_node.next_node = ptr
            self.__head = new_node
            return

        while (ptr.next_node is not None) and ptr.next_node.data < value:
            ptr = ptr.next_node
        new_node.next_node = ptr.next_node
        ptr.next_node = new_node
