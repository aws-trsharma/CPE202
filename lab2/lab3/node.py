"""CPE 202: Lab3
Tushar Sharma
"""
class Node:
    """Node class for linked lists
    Attributes:
      val (any type) : stored in Node
    """
    def __init__(self, val=None):
        self.val = val
        self.next = None
    def __repr__(self):
        """Returns a string representation of the Node
        """
        return repr(self.val)
    def __eq__(self, other):
        """Checks to see if 2 Nodes are equal to each other
        args:
         other (Node): comparative Node
        returns:
         boolean if Nodes are equal to each other or not
        """
        return isinstance(other, Node) and self.val == other.val
