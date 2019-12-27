"""HuffmanNode
CPE202
Author:
    Tushar Sharma
"""


class HuffmanNode:
    """
    Represents a leaf or internal node
    Args:
        frequency: #of times character is present in data
        char: Specific character which is being stored. Only if a leaf node
        left: A reference to left subtree
        right: A reference to right subtree
    """
    def __init__(self, frequency, char=None, left=None, right=None):
        self.freq = frequency
        self.char = char
        self.left = left
        self.right = right

    def __eq__(self, other):
        """
        Determines if the 2 Huffman Nodes are equivalent to each other
        :param
            other: (HuffmanNode): the other huffman node
        :return:
            boolean: T or F: D
        """
        return isinstance(HuffmanNode, other) and self.freq == other.freq \
            and self.char == other.char and self.left == other.left and self.right == other.right

    def __repr__(self):
        """
        Returns a string representation of the Huffman Node
        """
        return "HuffmanTNode(freq:%d, char:%s, left:%s, right:%s)" % (self.freq, self.char, self.left, self.right)

    def __lt__(self, other):
        """Implementing this function let you compare two HuffmanNode objects
         with < in your program
        Args:
            other (HuffmanNode): other HUffmanNode object to be compared with self
        Returns:
            True if self <= other, else return False
        """
        if self.freq < other.freq:
            return True
        elif self.freq == other.freq:
            if ord(self.char) < ord(other.char):
                return True
            return False
        return False


