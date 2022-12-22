#!/usr/bin/python3
"""Linkedlist practice with alx

This is an implementation of linked list data
data structure in python
"""


class Node:
    """Defines blueprint for linked list data structure

    Integer linked list
    """

    def __init__(self, data, next_node=None):
        """Constructor function

        Args:
            data (int): must be an integer
            next_node (Node): must be a Node instance or None
        """
        if isinstance(data, int) is False:
            raise TypeError("data must be an intger")
        if isinstance(next_node, Node) is False\
                and next_node is not None:
            raise TypeError("next_node must be a Node object")
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """Getter for data

        Returns:
            int: value of self.__data
        """
        return self.__data

    @data.setter
    def data(self, value):
        """setter for data

        Args:
            value (int): must be an integer
        """
        if isinstance(value, int) is False:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Getter for next_node

        Returns:
            Node: next node of self
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Setter for next_node

        Args:
            value (int): must be an integer
        """
        if isinstance(value, Node) is False\
                and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Linkedlist wrapper

    This class hold the reference to the head of a Linkedlist
    """

    def __init__(self):
        """Constructor function

        initialises the head node
        """
        self.__head = None

    def __str__(self):
        """stringify elements of the Linkedlist

        Returns:
            str: string consisting of element of
            the Linkedlist seperated by newline
        """
        head = self.__head
        lst_str = ""
        while head:
            lst_str += str(head.data)
            if isinstance(head.next_node, Node) is True:
                lst_str += "\n"
            head = head.next_node
        return lst_str

    def sorted_insert(self, value):
        """Insert new node in sorted order
        Args:
             value (Node): must be a node object
        """
        head = None
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
            return
        head = self.__head
        if head.data > new_node.data:
            new_node.next_node = head
            self.__head = new_node
            return
        while isinstance(head.next_node, Node) is True:
            if head.next_node.data > new_node.data:
                new_node.next_node = head.next_node
                head.next_node = new_node
                return
            head = head.next_node
        head.next_node = new_node
        return
