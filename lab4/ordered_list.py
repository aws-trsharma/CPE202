"""CPE 202
Lab #4:


Author:
    Tushar Sharma
"""
from Node import Node


class OrderedList:
    """Stack using resizing array
    Attributes:
        head(Node): head of the ordered list
        tail(Node): rear of the ordered list
        num_items(int): num of items in the list
    """
    def __init__(self):
        self.head = None
        self.tail = None
        self.num_items = 0

    def __eq__(self, other):
        """Returns if 2 Ordered list are equivalent to each other
        """
        return isinstance(other, OrderedList) and self.head == other.head \
              and self.tail == other.tail and self.num_items == other.num_items

    def __repr__(self):
        """Returns a string representation of the Linked Lists
                   returns:
                      res (string) with all the values
        """
        if self.head is None:
            return 'None'
        res = ""
        cur = self.head
        while cur is not None:
            res += repr(cur.val)
            if cur.next is not None:
                res += "->"
            cur = cur.next
        res += ""
        return res

    def add(self, item):
        """Adds a new item (int) to the list making sure the order is preserved
        Args:
            item(int): int to be appended to end of list
        """
        item = Node(val=item)
        if self.head is None:
            self.head = item
            self.tail = self.head
            self.num_items += 1
        elif item.val < self.head.val:
            self.head.prev = item
            item.next = self.head
            self.head = item
            self.num_items += 1
        elif item.val > self.tail.val:
            self.tail.next = item
            item.prev = self.tail
            self.tail = item
            self.num_items += 1
        else:
            cur = self.head
            while cur is not None and cur.val <= item.val:
                cur = cur.next
            next1 = cur
            prev1 = cur.prev
            prev1.next = item
            item.prev = prev1
            next1.prev = item
            item.next = next1
            self.num_items += 1

    def remove(self, item):
        """Removes an item from the list. Modifies the list accordingly
        Args:
            item(int): int to be removed in list
        """
        cur = self.head
        index = 0
        while cur is not None:
            if item == cur.val:
                item = Node(item)
                cur.next.prev = cur.prev
                cur.prev.next = cur.next
                item.prev = cur.prev
                item.next = cur.next
                self.num_items -= 1
                index += 1
                return index
            cur = cur.next
        return -1

    def search_forward(self, item):
        """Searches for the item(int) in the list by going forward
        Args:
            item(int): the item to be found in the list
        Returns:
            True if item is found
            False if item is not found
        """
        cur = self.head
        while cur is not None:
            if cur.val == item:
                return True
            cur = cur.next
        return False

    def search_backward(self, item):
        """Searches for the item backwards in the list
        Args:
            item(int): the item to be found in the list
        Returns:
            True if item is found
            False if item is not found
        """
        cur = self.tail
        while cur is not None:
            if cur.val == item:
                return True
            cur = cur.prev
        return False

    def is_empty(self):
        """Checks to see if the Ordered List is empty or not
        """
        return self.num_items == 0 

    def size(self):
        """Determines the size of the Ordered List
        """
        return self.num_items

    def index(self, item):
        """Checks What current index a certain item is at
        Args:
            item(int): where the current item is
        Returns:
            index(int): index of where item is
        """
        index = 0
        cur = self.head
        while cur is not None:
            if item == cur.val:
                return index
            cur = cur.next
            index += 1
        return -1

    def pop(self, pos=None):
        """"Takes an optional argument. If None, returns value
        at end of list. If not checks to see where position is
        on lower end or higher end and traverses list through that
        Args:
            pos(int): position of Node to be removed
        Returns:
            val1(Node): the value of the Node to be removed
        """
        if pos is None:
            val1 = self.tail.val
            cur = self.tail
            cur = cur.prev
            if self.tail is None:
                self.head == None
            else:
                self.tail.next = None
            self.num_items -= 1
            return val1
        else:
            size = self.size()
            if pos > size:
                return -1
            elif pos <= size/2:
                if pos == 0:
                    val1 = self.head.val
                    self.head = self.head.next
                    if self.head is None:
                        self.tail = None
                    else:
                        self.head.prev = None
                    self.num_items -= 1
                    return val1
                cur = self.head
                for i in range(pos):
                        cur = cur.next
                val1 = cur.val
                cur.next.prev = cur.prev
                cur.prev.next = cur.next
                self.num_items -= 1
                return val1
            else:
                if pos + 1 == size:
                    val1 = self.tail.value
                    self.tail = self.tail.prev
                    if self.tail is None:
                        self.head = None
                    else:
                        self.tail.next = None
                    return val1
                cur = self.tail
                for i in range(size - pos - 1):
                    cur = cur.prev
                val1 = cur.val
                cur.next.prev = cur.prev
                cur.prev.next = cur.next
                self.num_items -= 1
                return val1


if __name__ == '__main__':
    val = OrderedList()
    val.add(2)
    val.add(1)
    val.add(3)
    val.add(4)
    val.add(5)
    val.add(3)
    val.add(6)
    val.remove(3)
    print(val.search_forward(9))
    print(val.index(2))
    val.pop(1)
    print(val)