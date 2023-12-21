#!/usr/bin/python3
"""Create a class about singly linked list"""


class Node:
    """node of a singly linked list"""

    def __init__(self, data, next_node=None):
        """Initiaize the data and next node

        Args:
            data(int): integer to store data
            next_node(Node): pointer to next node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get the data"""
        return self.__data

    @data.setter
    def data(self, value):
        """Set the data"""
        if not isinstance(value, int):
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        """Get next node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the next node"""
        if not isinstance(value, Node) and value is not None:
            raise TypeError('next_node must be a Node object')
        self.__next_node = value


class SinglyLinkedList:
    """defines a singly linked list"""

    def __init__(self):
        """Initialize a list"""

        self.__head = None

    def sorted_insert(self, value):
        """insert value in order

            Args:
                value(int): integer to add
        """

        node = Node(value)
        if self.__head is None:
            self.__head = node
        elif self.__head.data > value:
            node.next_node = self.__head
            self.__head = node
        else:
            current = self.__head
            while current.next_node is not None and\
                    current.next_node.data < value:
                current = current.next_node
            node.next_node = current.next_node
            current.next_node = node

    def __str__(self):
        """Define the print() representation of a SinglyLinkedList."""

        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))
