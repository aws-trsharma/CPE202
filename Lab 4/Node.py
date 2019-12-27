"""CPE 202 Lab 4
Author: Tushar Sharma
"""


class Node:
    """Node class for Linked Lists
    Attributes:
      prev(int): is a pointer to the previous node
      next(int) is a pointer to the next node
      val (any type): stored in Node
    """

    def __init__(self, prev=None, next=None, val=None):
        self.prev = prev
        self.val = val
        self.next = next

    def __repr__(self):
        """Returns a string representation of the Node
        """
        return repr(self.val)

    def __eq__(self, other):
        """Checks to see if 2 Nodes are equal to each other
        args:
            other (Node): comparative Node
        returns:
            boolean if Node's are equal to each other or not
        """
        return isinstance(other, Node) and self.val == other.val
