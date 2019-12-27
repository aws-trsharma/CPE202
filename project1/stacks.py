"""Contains code for StackADTs
CPE202
Project 1

Author:
    Tushar Sharma
"""
from node import Node
class StackArray:
    """Stack using resizing array
    Attributes:
        arr (list) : An array
        num_items (int) : number of items
        capacity (int) : capacity
    """
    def __init__(self):
        self.capacity = 2
        self.arr = [None] * self.capacity
        self.num_items = 0

    def __repr__(self):
        """Returns a String representation of the Stack
        Returns:
          a string format for the arr
        """
        return '%s'% self.arr
    def __eq__(self, other):
        """Checks to see if 2 stack arrays are equal to each other
        args:
          other(StackArrray): comparative stack
        returns:
           boolean if StackArray's are equal to each other or not
        """
        return isinstance(other, StackArray) and self.arr == other.arr and self.num_items == \
        other.num_items and self.capacity == other.capacity

    def enlarge(self):
        """Enlarges the size of the array by 2 and creates a new array only when the capa
        city of the array is equal to the number of items
        """
        item = 0
        if self.capacity == self.num_items:
            self.capacity = self.capacity * 2
            new_arr = [None] * self.capacity
            while item < self.num_items:
                new_arr[item] = self.arr[item]
                item += 1
            self.arr = new_arr
            self.num_items = item
        return self.arr
    def shrink(self):
        """Shrinks the size of the array by 2 and creates a new array only when the capacity of
        the array is 4 times greater than the number of item
        """
        item = 0
        if self.capacity/self.num_items >= 4:
            self.capacity = self.capacity //  2
            new_arr = [None] * self.capacity
            while item < self.num_items:
                new_arr[item] = self.arr[item]
                item += 1
            self.arr = new_arr
            self.num_items = item
        return self.arr

    def is_full(self):
        """Returns if the array is full or not based off its current capacity
        """
        return self.capacity == self.num_items
    def is_empty(self):
        """Returns a boolean expression to express if the Array
        is empty or not
        returns:
           boolean: could be either True or False
        """
        return self.num_items == 0

    def push(self, item):
        """Adds a new item to the top of the stack
        args:
           item (any type): is pushed to the top of the stack
        """
        if self.num_items > 0:
            self.enlarge()
        self.arr[self.num_items] = item
        self.num_items += 1
    def pop(self):
        """Removes top item from stack
        returns:
           Type Value that is stored in top item from stack
        """
        if self.num_items == 0:
            raise IndexError
        self.num_items -= 1
        temp = self.arr[self.num_items]
        self.arr[self.num_items] = None
        self.shrink()
        return temp
    def peek(self):
        """Returns top item from stack
        returns:
            Type Value that is stored in top item from stack
        """
        if self.num_items == 0:
            return None
        return self.arr[self.num_items - 1]
    def size(self):
        """Returns number of items in a stack
        Returns:
           num_items (int): number of items in stack
        """
        return self.num_items
class StackLinked:
    """Stack using Linked Lists
    Attributes:
        top (any type): stores a Node as the top variable
        num_items (int): number of items
    """

    def __init__(self, top=None):
        if top is  None:
            self.top = None
        else:
            self.top = Node(top)
        self.num_items = 0
        if self.num_items != None:
            self.num_items += 1
    def __repr__(self):
        """Returns a string representation of the Linked Lists
           returns:
              res (string) with all the values
        """
        if self.top is None:
            return 'None'
        res = ""
        cur = self.top
        while cur is not None:
            res += repr(cur.val)
            if cur.next != None:
                res += "->"
            cur = cur.next
        res += ""
        return res
    def __eq__(self, other):
        """Returns if 2 linkedstacks are equivalent to each other
        """
        return isinstance(self, other) and self.top == other.top and\
        self.num_items == other.num_items
    def is_empty(self):
        """Returns a boolean expression to express if the Array
        is empty or not
        returns:
            boolean: could be either True or False
         """
        return self.num_items == 0
    def is_full(self):
        """Returns a boolean value if Capacity is equivalent to the number of items
        """
        pass
    def push(self, item):
        """Pushes an element to the list. If the LinkedList is
        initially empty it appends value to top of list
        Attributes:
           item (any type) : value added to list
        """
        item = Node(item)
        if self.top is  None:
            self.top = Node(item)
            self.num_items += 1
        else:
            cur = self.top
            self.top = item
            self.top.next = cur
            self.num_items += 1
    def pop(self):
        """Removes top item from stack
        returns:
           type value that is stored in top of stack
        """
        if self.num_items == 0:
            raise IndexError
        temp = self.top
        self.top = self.top.next
        self.num_items -= 1
        return temp.val
    def peek(self):
        """Returns the value stored at the top of the stack at the moment
        """
        if self.num_items == 0:
            return None
        return self.top.val.val
    def size(self):
        """Returns numbers of items in a stack
        returns:
           num_items (int): number of items in a list
        """
        return self.num_items
