"""
Contains Node class for BST
CPE202

Author:
    Section: 07
    Tushar Sharma
"""


class BSTNode:
    """Node class for BST
    Attributes:
        key(int): a key
        val(*): a value of any type
        left(BSTNode): left subtree
        right(BST Node): a right subtree
    """
    def __init__(self, key, val, left=None, right=None):
        """The constructor
        Args:
            key(int): a key
            val(*): a value of any type
            left (BSTNode): left subtree
            right(BSTNode): right subtree
        """
        self.key = key
        self.val = val
        self.left = left
        self.right = right

    def __eq__(self, other):
        """
        Determines if 2 trees are equivalent to each other
        :param other: (BSTNode): another tree
        """
        return isinstance(other, BSTNode) and self.key == other.key \
               and self.val == other .val and self.left == other.left \
               and self.right == other.right

    def __repr__(self):
        """
        Returns a string representation of the BST Node
        """
        return "BSTNode(key:%d, val:%s, left:%s, right:%s)"\
               % (self.key, self.val, self.left, self.right)


def get(bst, key):
    """
    searches for the key and returns the value associated with it
    args:
        bst (BSTNode): bst
        key(int): the key
    :return:
        *: the value associated with key
     Raises:
        KeyError: When the key is not in the tree
    """
    if bst is None:
        return KeyError('This Key Error does not exist')
    if bst.key == key:
        return bst.val
    if bst.key > key:
        return get(bst.left, key)
    return get(bst.right, key)


def contains(bst, key):
    """
    searches for the key and returns boolean associated with it
    args:
        bst(BSTNode): a bst
        key(int): a key
    :return:
        T or F: if it is contained in the list
    Raises:
        KeyError: When the key is not in the tree
    """
    if bst is None:
        return False
    if bst.key == key:
        return True
    if bst.key > key:
        return contains(bst.left, key)
    return contains(bst.right, key)


def insert(bst, key, val):
    """
    Inserts a key value pair to the bst
    args:
        bst (BSTNode): a bst
        key(int) : a key
        val(*): a value of any type
    Returns: BSTNode : a bst
    """
    if bst is None:
        return BSTNode(key, val)
    if bst.key > key:
        bst.left = insert(bst.left, key, val)
    else:
        bst.right = insert(bst.right, key, val)
    return bst


def delete(bst, key):
    """
    Delete a node with the key from bst
    :param
        bst (BSTNode): bst
        key (int): the key
    :return:
         BSTNode: the root of bst
    Raises:
        KeyError: When the key is not in the tree
    """
    if bst is None:
        raise KeyError('The key does not exist')
    if bst.key == key:
        if bst.left and bst.right:
            replacement = get_replacement(bst.right)
            bst = delete(bst, replacement.key)
            bst.key, bst.val = replacement.key, replacement.val
            return bst
        elif bst.left:
            return bst.left
        return bst.right
    if bst.key > key:
        bst.left = delete(bst.left, key)
    else:
        bst.right = delete(bst.right, key)
    return bst


def get_replacement(bst):
    """
    get a replacement BST Node
    :param
        bst: (BSTNode): a bst
    :return:
        BSTNode: a replacement node
    Raises:
        ValueError: when the tree is empty
    """
    if bst is None:
        raise ValueError('The tree is empty!')
    if bst.left is None:
        return bst
    return get_replacement(bst.left)


def find_min(bst):
    """
    Returns the minimum of the function
    args:
        BST: (BSTNode): a bst
    :return:
        minimum of Binary Search tree
    """
    if bst is None:
        raise ValueError
    if bst.left is None:
        return bst.val
    return find_min(bst.left)


def find_max(bst):
    """
    Returns the maximum of the function
    args:
        BST: (BSTNode): a bst
    :return:
        maximum of Binary Search Tree
    """
    if bst is None:
        raise ValueError
    if bst.right is None:
        return bst.val
    return find_max(bst.right)


def inorder_list(bst, accum=[]):
    """
    Traverses the tree using inorder method and appends it to output list
    :param
        bst: (BSTNode): a bst
        accum: (list): list which appends value based on order they are added, currently empty
    :return:
        accum: (list): list which appends value based on order they are added
    """
    if bst is None:
        return accum
    accum = inorder_list(bst.left, accum)
    accum.append(int(bst.key))
    accum = inorder_list(bst.right, accum)
    return accum


def preorder_list(bst, accum=[]):
    """
    Traverses the tree using preorder method and appends it to output list
    :param
        bst: (BSTNode): a bst
        accum: (list): list which appends value based on order they are added, currently empty
    :return:
        accum: (list): list which appends value based on order they are added
    """
    if bst is None:
        return accum
    accum.append(bst.key)
    accum = preorder_list(bst.left, accum)
    accum = preorder_list(bst.right, accum)
    return accum


def tree_depth(bst):
    """
    Returns the depth of the tree
    :param
        bst: a Node
    :return:
        returns the height of the tree
    """
    if bst is None:
        return 0
    left = tree_depth(bst.left)
    right = tree_depth(bst.right)
    if left > right:
        return left + 1
    return right + 1


def tree_height(bst):
    """
    Returns the depth of the tree
    :param
        bst: a Nonde
    :return:
        returns the height of the tree

    """
    return tree_depth(bst) - 1


def range_search(bst, lo_val, hi_val):
    """
    searches keys in the given range
    :param
        bst: (BSTNode): a bst
        lo: (int): the inclusive low end of the key range
        hi: (int): the exclusive high end of the key range
    :return:
        list: a list of values associated with the keys in the range
    """
    return range_helper(bst, lo_val, hi_val, [])


def range_helper(bst, lo_val, hi_val, accum):
    """
        searches keys in the given range
        :param
            bst: (BSTNode): a bst
            lo: (int): the inclusive low end of the key range
            hi: (int): the exclusive high end of the key range
        :return:
            list: a list of values associated with the keys in the range
        """
    if bst is None:
        return accum
    if bst.key >= hi_val:
        return range_helper(bst.left, lo_val, hi_val, accum)
    if bst.key < lo_val:
        return range_helper(bst.right, lo_val, hi_val, accum)
    accum = range_helper(bst.left, lo_val, hi_val, accum)
    accum.append(bst.val)
    accum = range_helper(bst.right, lo_val, hi_val, accum)
    return accum

