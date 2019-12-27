import unittest
from stacks import *
from node import *

class TestCase(unittest.TestCase):
    def test_Stack_Array1(self):
        s = StackArray()
        s.push(1)
        s.push(2)
        self.assertEqual(s.is_full(), True)
        s.push(3)
        self.assertEqual(s.num_items, 3)
        self.assertEqual(s.capacity, 4)
        self.assertEqual(s.pop(), 3)
        print(s)
        s.push(3)
        s.push(4)
        s.push(5)
        s.push(6)
        s.push(7)
        s.push(8)
        print(s)
        s.pop()
        s.pop()
        s.pop()
        s.pop()
        s.pop()
        s.pop()
        print(s)
        self.assertEqual(s.pop(), 2)
    def test_Stack_linked(self):
        s = StackLinked()
        s.push(1)
        s.push(2)
        self.assertEqual(s.pop(),2)
        s.push(3)
        self.assertEqual(s.pop(), 3)
        self.assertEqual(s.peek(), 1)
def main():
    unittest.main()
if __name__ == '__main__':
   #s = StackArray()
   #s.push(1)
   #s.push(2)
   #s.push(3)
   #s.push(4)
   #s.push(5)
   #s.pop()
   #s.pop()
   #print(s)
   #print (s.num_items)
   #s = StackLinked()
   #print(s)
   #s.push(1)
   #print(s)
   #.push(2)
   #print(s)
   #s.push(3)
   #print(s)
   #s.pop()
   #print(s)
   #print(s.peek())
   #print(s)
   main()