"""Contains starter code for lab 5

CPE201 Spring 2019

Instructions:
    Complete this file by writing python3 code.

"""
import random

#implement BSTNode class and get,contains,insert,delete functions in bst.py
import bst

#classmate.py is implemented for you
from classmate import classmate_factory


class TreeMap:
    """TreeMap class for lab5
    Attributes:
        tree (BSTNode): a BSTNode
        num_items: (int) the number of items in a tree
    """
    def __init__(self):
        self.tree = None
        self.num_items = 0

    def __repr__(self):
        """
        Returns a string representation of the class TreeMap
        """
        return '%s' % self.num_items

    def __eq__(self, other):
        """
        Determines if 2 TreeMap are equivalent to each other
        :param other: (TreeMap): another tree
        """
        return isinstance(other, TreeMap) and self.tree == other.tree\
            and self.num_items == other.num_items

    def __getitem__(self, key):
        """implementing this method enables getting an item with [] notation
        This function calls your get method.

        Args:
            key (*) : a key which is compareable by <,>,==
        Returns:
            * : the value associated with the key
        Raises:
            KeyError : it raises KeyError because the get function in bst.py raises the error.
        """
        return self.get(key)

    def __setitem__(self, key, val):
        """implementing this method enables setting a key value pair with [] notation
        This function calls your put method.

        Args:
            key (*) : a key which is compareable by <,>,==
            val (*): the value associated with the key
        """
        self.put(key, val)

    def __contains__(self, key):
        """implementing this method enables checking if a key exists with in notaion

        Args:
            key (*) : a key which is compareable by <,>,==
        Returns:
            bool : True is the key exists, otherwise False
        """
        return self.contains(key)

    def put(self, key, val):
        """put a key value pair into the map
        Calls insert function in bst.py

        Args:
            key (*) : a key which is compareable by <,>,==
            val (*): the value associated with the key
        """
        self.tree = bst.insert(self.tree, key, val)
        self.num_items += 1

    def get(self, key):
        """gets the value associated with a key from the map
        Calls get function in bst.py

        Args:
            key (*) : a key which is compareable by <,>,==
        Returns:
            * : the value associated with th key
        """
        return bst.get(self.tree, key)

    def contains(self, key):
        """Finds out if the TreeMap contains this certain value
        Args:
            key (*) : a key which is compareable by <,>,==
        Returns:
            bool : True is the key exists, otherwise False
        """
        return bst.contains(self.tree, key)

    def delete(self, key):
        """Deletes the key required from the Tree Node
        Args:
            key (*) : a key which is compareable by <,>,==
        """
        self.tree = bst.delete(self.tree, key)
        self.num_items -= 1

    def size(self):
        """returns the number of items in the map
        Returns:
            int : the number of items in the map
        """
        return self.num_items

    def find_min(self):
        """ Minimum value in the tree is returned
        Returns:
            Minimum value in the tree is returned
        """
        return bst.find_min(self.tree)

    def find_max(self):
        """Maximum value in the tree is returned
        Returns:
            Maximum value in the tree is returned
        """
        return bst.find_max(self.tree)

    def inorder_list(self):
        """Returns an inorder representation of the tree
        Returns:
            List in inorder representation
        """
        return bst.inorder_list(self.tree, [])

    def preorder_list(self):
        """Returns a preorder representation of the tree
        Returns:
            List in preorder representation
        """
        return bst.preorder_list(self.tree, [])

    def tree_height(self):
        """Returns the tree height of the tree
        Returns:
            Returns what the current tree height is
        """
        return bst.tree_height(self.tree)

    def range_search(self, lo_val, hi_val):
        """Searches for a certain set of values in the tree
        """
        return bst.range_search(self.tree, lo_val, hi_val)


def import_classmates(filename):
    """Imports classmates from a tsv file

    Design Recipe step 4 (Templating) is done for you.
    Complete this function by following the template.

    Args:
        filename (str) : the file name of a tsv file containing classmates

    Returns:
        TreeMap : return an object of TreeMap containing classmates.
    """
    #create an object of TreeMap
    tree_map = TreeMap()
    #create an empty list for classmates
    classmates = []
    #---- to do ----
    # complete this function by following the comments below
    #
    #open the file filename with python builtin open() function
    lines = open(filename, 'r')
    for line in lines:
        tokens = line.split("\t")
        classmate = classmate_factory(tokens)
        classmates.append(classmate)
    #read all lines in the file and assign it to variable lines
    #for each line in lines
        #split the line at tabs (\t) and assign it to a variable tokens
        #classmate = classmate_factory(tokens)
        #append the classmate to a list classmates
    #---------- ----

    #shuffle the classmates
    random.seed(2)
    random.shuffle(classmates)

    #---- to do ----
    # complete this function by following the comments below
    #
    for classmate in classmates:
        tree_map.__setitem__(classmate.sid, classmate)
    #for each classmate in classmates
        #put the classmate into the tree_map using sid (the sequential number) as the key
    #---------- ----
    return tree_map


def search_classmate(tmap, sid):
    """Searches a classmate in a TreeMap using the last name as a key
    Args:
        tmap (TreeMap) : an object of TreeMap
        sid (int) : student id
    Returns:
        Classmate : a Classmate object
    Raises:
        KeyError : if a classmate with the last name does not exist
    """
    if sid in tmap:
        return tmap[sid]
    raise KeyError("A classmate with the id does not exist!")

