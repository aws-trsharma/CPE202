import unittest
from ordered_list import OrderedList
from Node import Node


class TestCase(unittest.TestCase):
    def test_ordered_list_add_pop(self):
        ord1 = OrderedList()
        ord1.add(1)
        ord1.add(2)
        ord1.add(4)
        ord1.add(3)
        self.assertEqual(ord1.pop(), 4)
        self.assertEqual(ord1.pop(1), 2)
        self.assertEqual(ord1.size(), 2)

    def test_ordered_list_remove_pop(self):
        ord2 = OrderedList()
        ord2.add(2)
        ord2.add(1)
        ord2.add(4)
        ord2.add(6)
        ord2.add(7)
        ord2.remove(4)
        self.assertEqual(ord2.size(), 4)
        self.assertEqual(ord2.pop(1), 2)

    def test_ordered_list_search_forward_back(self):
        ord3 = OrderedList()
        ord3.add(1)
        ord3.add(3)
        ord3.add(5)
        ord3.add(6)
        self.assertEqual(ord3.search_forward(3), True)
        self.assertEqual(ord3.search_forward(7), False)
        self.assertEqual(ord3.search_backward(3), True)
        self.assertEqual(ord3.search_backward(9), False)
        self.assertEqual(ord3.index(3), 1)
        self.assertEqual(ord3.index(6), 3)


def main():
    unittest.main()


if __name__ == '__main__':
    main()