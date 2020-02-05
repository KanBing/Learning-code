#!/usr/bin/env python3


class Node:
    def __int__(self,data):
        self.data = data
        self.next = None


class Linked_List:
    def __int__(self, head=None):
        self.head = head

    def append(self. new_element):
        """
        """
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element
