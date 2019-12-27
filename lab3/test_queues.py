import unittest
from queues import *
from node import *
class TestCase(unittest.TestCase):
    def test_Queue_Linked(self):
        s = QueueLinked(4)
        s.enqueue(1)
        s.enqueue(2)
        s.enqueue(3)
        s.enqueue(4)
        self.assertEqual(s.front, Node(1))
        self.assertEqual(s.rear, Node(4))
        s.dequeue()
        self.assertEqual(s.num_items, 3)
        self.assertEqual(s.front, Node(2))
    def test_Queue_Linked(self):
       s = QueueArray(8)
       s.enqueue(1)
       s.enqueue(2)
       s.enqueue(3)
       s.enqueue(4)
       self.assertEqual(s.dequeue(), Node(1))
       s.enqueue(5)
       self.assertEqual(s.dequeue(), Node(2))
       s.enqueue(6)
       s.enqueue(7)
       s.enqueue(8)
       s.enqueue(9)
       self.assertEqual(s.num_items,7)
def main():
       unittest.main()
if __name__ == '__main__':
   main()
