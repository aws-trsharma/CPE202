"""CPE 202 Lab 3
Tushar Sharma
"""
from node import Node
class QueueArray:
    """Queue using Circular Array format
    args:
        capacity: number of items allowed in the circular array
        front: pointer to front of queue
        rear: pointer to rear of queue
        items: array capped by capacity of variable
        num_items: number of items in array
    """
    def __init__(self, capacity):
        #the maximum number of items that can be stored in queue
        self.capacity = capacity
        self.front = 0 #pointer to the front of queue
        self.rear = 0 #pointer to the rear of queue
        self.items = [None] * self.capacity#array whose size is the capacity
        self.num_items = 0#number of items in array
    def __repr__(self):
        """Returns string representation of Queue Array
        return "%s" % self.items
        """
        return "%s" % self.items
    def __eq__(self, other):
        """Determines if One Queue Array is equivalent to another Queue Array
        returns:
         a boolean if the Queue Array is equivalent to the other array
        """
        return isinstance(other, QueueArray) and self.front == other.front and  self.rear == other.rear\
        and self.items == other.items and self.num_items == other.num_items
    def is_empty(self):
        """Determines if the Array is empty or not
        """
        return self.num_items == 0
    def is_full(self):
        """Determines if a Array is full or not. Takes into account that the size of the array
        must be one less than the capacity
        """
        return self.num_items == self.capacity 
    def enqueue(self, item):
        """Adds an item to the rear of the queue. It uses the remainder of rear / capacity to get
        index for new element
        args:
            item (Node): new Node added to the end of queue
        """
        val = Node(item)
        if self.is_full():
            raise IndexError
        if self.num_items == 0:
            self.items[self.front] = val
            self.num_items += 1
        else:
            self.rear += 1
            self.rear %= self.capacity
            if self.rear == self.capacity:
                self.rear = 0
            self.items[self.rear] = val
            self.num_items += 1
    def dequeue(self):
        """Removes and returns the Node that is currently at the front of the array
        returns:
           Value currently stored at first in the array
        """
        temp = self.items[self.front]
        self.items[self.front] = None
        self.front += 1
        self.num_items -= 1
        return temp
    #returns the number of items in the queue
    def size(self):
        """Returns size of queue array
        """
        return self.num_items
#You must have the same functionalities for the Linked List Implementation
class QueueLinked:
    """Queue Using Linked Lists
    Attributes:
        capacity: the size of the Linked List
        front: pointer to front of queue
        rear: pointer to rear of queue
        num_items: number of items in the linked list
     """
    def __init__(self, capacity):
        #the maximum number of items that can be stored in queue
        self.capacity = capacity
        self.front = None#pointer to the front of queue
        self.rear = None#pointer to the rear of queue
        self.num_items = 0 #number of items in array
    def __repr__(self):
        """Returns a string representation of the Linked Lists
        returns:
           res(string) with all the values
        """
        if self.front is  None:
            return 'None'
        res = ""
        while self.front is not None:
            res += repr(self.front)
            if self.front.next != None:
                res += "->"
            self.front = self.front.next
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
        val = Node(item)
        if self.front is  None:
            self.front = val
            self.rear = val
            self.num_items += 1
        else:
            cur = self.rear
            cur.next = val
            self.rear = val
            self.num_items += 1
    def dequeue(self):
        """Removes an element from the front of the list
        Returns:
          cur (any type): value stored in front of list. FIFO.
        """
        cur = self.front
        self.front = self.front.next
        self.num_items -= 1
        return cur

    #returns the number of items in the queue
    def size(self):
        """Returns the number of items in the queue
        """
        return self.num_items
