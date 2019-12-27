"""
CPE 202: Lab 8
Linked List implementation for seperate chaining
"""
from node import Node
class LinkedList:
    """Queue Using Linked Lists
    Attributes:
        capacity: the size of the Linked List
        front: pointer to front of queue
        rear: pointer to rear of queue
        num_items: number of items in the linked list
     """
    def __init__(self):
        #the maximum number of items that can be stored in queue
        #self.capacity = capacity
        self.head = None#pointer to the front of queue
        self.num_items = 0
    def __repr__(self):
        """Returns a string representation of the Linked Lists
        returns:
           res(string) with all the values
        """
        if self.head is  None:
            return 'None'
        res = ""
        while self.head is not None:
            res += repr(self.head)
            if self.head.next != None:
                res += "->"
            self.head = self.head.next
        res += ""
        return res
    def is_empty(self):
        """Returns a boolean too see if list is empty or not
        """
        return self.num_items == 0

    def is_full(self):
        """Returns a boolean too see if the capacity is equal to the
        number of items
        """
        return self.capacity == self.num_items

    def enqueue(self, item):
        """Adds a new item to the queue by adding it to the rear
        args:
           item (Node): item added to the rear of the queue
        """
        item = Node(item)
        item.next = self.head
        self.head = item
        self.num_items += 1

    def dequeue(self):
        """Removes an element from the front of the list
        Returns:
          cur (any type): value stored in front of list. FIFO.
        """
        current = self.head
        previous = None
        found = False
        while not found:
            if current.val() == item:
                found = True
            else:
                previous = current
                current = current.next()

        if previous is None:
            self.head = current.next()
        else:
            previous.next(current.next())
        self.num_items -= 1

    #returns the number of items in the queue
    def size(self):
        """Returns the number of items in the queue
        """
        return self.num_items
