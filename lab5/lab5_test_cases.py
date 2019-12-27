import unittest
from lab5 import *


class TestCase(unittest.TestCase):
    def test_classmates_item(self):
        var = import_classmates('classmates.tsv')
        self.assertEqual(var.num_items, 55)
        var.delete(15)
        self.assertEqual(var.num_items, 54)
        self.assertEqual(search_classmate(var, 1), var.find_min())
        self.assertEqual(search_classmate(var, 55), var.find_max())
        self.assertEqual(var.tree_height(), 10)
        print(var.inorder_list())


def main():
    unittest.main()

if __name__ == '__main__':
    main()