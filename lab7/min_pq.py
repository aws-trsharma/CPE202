"""Minimum Priority Queue
For:
    CPE202
    Sections 7 & 9
    Fall 2019
Author:
    Tushar Sharma
"""
from HuffmanNode import HuffmanNode
class MinPQ:
    """Minimum Priority Queue
    Attributes:
        capacity (int): the capacity of the queue. The default capacity is 2, but will be increased automatically.
        num_items (int): the number of items in the queue.
        arr (list): an array which contains the items in the queue.
    """
    def __init__(self, capacity=2):
        self.capacity = capacity 
        self.num_items = 0
        self.arr = [None] * self.capacity

    def __eq__(self, other):
        """
         Determines if the 2 Huffman Nodes are equivalent to each other
        :param
            other: (HuffmanNode): the other huffman node
        :return:
            boolean: T or F: D
        """
        return isinstance(MinPQ, other) and self.capacity == other.capacity and self.num_items == other.num_items\
            and self.arr == other.arr

    def __repr__(self):
        """
        Returns a string represenation of the MinPQ
        """
        return "(%s)" % self.arr

    def heapify(self, arr):
        """initialize the queue with a given array and convert the array into a min heap
        Args:
            arr (list): an array
        Returns:
            None : it returns nothing
        """
        length = len(arr)
        i = (length - 2)//2
        while i >= 0:
            self.shift_down(arr, i, length-1)
            i = i - 1
        for i in arr:
            self.insert(i)
        self.capacity = self.num_items

    def shift_down(self, arr, index, end = None):
        """
        Shifts the item at the specified index down, and it keeps shifting down recursively until
        it can no longer be shifted up
        args:
            arr: (array): array of some fixed size
            index: (int): current index of item
            end: (int): index in arr pointing to end of heap
         """
        if end is None:
            end = len(arr)
        cur = index + 1
        if cur > end or arr[cur] is None:
            return None
        arr[index], arr[cur] = arr[cur], arr[index]
        return self.shift_down(arr, cur, end)


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

    def insert(self, item):
        """inserts an item to the queue
        If the capacity == the num_items before inserting an item, enlarge the array.

        Args:
            item (*): an item to be inserted to the queue. It is of any data type.
        Returns:
            None : it returns nothing
        """
        if self.num_items > 0:
            self.enlarge()
        self.arr[self.num_items] = item
        self.num_items += 1
        self.shift_up(self.num_items-1)

    def shift_up(self, index):
        """
        Shifts the item at the specified index, and does this recursively until it
         no longer can be shifted up
        args:
            arr: (array): array of some fixed size
            index: (int): current index of item
        """
        val = index - 1
        if val < 0:
            return
        if self.arr[val] is None or self.arr[val] < self.arr[index]:
            return
        self.arr[val], self.arr[index] = self.arr[index], self.arr[val]
        return self.shift_up(val)

    def shrink(self):
        """Shrinks the size of the array by 2 and creates a new array only when the capacity of
        the array is 4 times greater than the number of item
        """
        item = 0
        if self.capacity / self.num_items >= 4:
            self.capacity = self.capacity // 2
            new_arr = [None] * self.capacity
            while item < self.num_items:
                new_arr[item] = self.arr[item]
                item += 1
            self.arr = new_arr
            self.num_items = item
        return self.arr

    def del_min(self, end= None):
        """deletes the minimum item in the queue
        If the capacity > 2 and num_items > 0 and <= capacity // 4, shrink the array

        Returns:
            * : it returns the minimum item, which has just been deleted
        Raises:
            IndexError : Raises IndexError when the queue is empty
        """
        if self.num_items == 0:
            raise IndexError
        if end is None:
            end = len(self.arr) - 1
        min_items = self.arr[0]
        self.arr[0] = self.arr[self.num_items-1]
        self.arr[end] = self.arr[self.num_items - 1]
        self.shift_down(self.arr, 0, end)
        self.shrink()
        self.num_items -= 1
        return  min_items

    def min(self):
        """returns the minimum item in the queue without deleting the item
        Returns:
            * : it returns the minimum item 
        Raises:
            IndexError : Raises IndexError when the queue is empty
        """
        return self.arr[0]

    def is_empty(self):
        """checks if the queue is empty 
        Returns:
            bool : True if empty, False otherwise. 
        """
        return self.num_items == 0

    def size(self):
        """returns the number of items in the queue 
        Returns:
            int : it returns the number of items in the queue 
        """
        return self.num_items
    """
    def heap_sort(self, arr):
        count = len(self.arr) - 1
        new_arr = [None] * len(arr)
        while count >= 0:
            arr, min1, end = self.del_min(self.heapify(arr))
            new_arr[count] = min1
            count -= 1
        return new_arr
    """
#min = MinPQ()
#min.insert(2)
#min.insert(3)
#min.insert(5)
#min.insert(9)
#min.insert(6)
#min.heapify()
#print(min)