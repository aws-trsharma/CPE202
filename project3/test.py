import unittest
from comparison_sort import *
from heap_sort import *

class TestCase(unittest.TestCase):
    def test_sort(self):
        test1 = [4,3,6,8,2,1]
        insertion_sort(test1)
        self.assertEqual(test1, [1,2,3,4,6,8])
        test2 = [4,3,6,8,2,1]
        selection_sort(test2)
        self.assertEqual(test2,[1,2,3,4,6,8])
        test3 = [4,3,6,8,2,1]
        heap_sort(test3)
        self.assertEqual(test3, [1,2,3,4,6,8])
        test4 = [4,3,6,8,2,1]
        merge_sort(test4)
        self.assertEqual(test4, [1,2,3,4,6,8])
        test5 = [4,3,6,8,2,1]
        quicksort(test5)
        self.assertEqual(test5, [1,2,3,4,6,8])
        test6 = [4,3,6,8,2,1]
        bubble_sort(test6)
        self.assertEqual(test6, [1,2,3,4,6,8])
        test7 = [4,3,6,8,2,1]
        tim_sort(test7)
        self.assertEqual(test7, [1,2,3,4,6,8])

def main():
    # execute unit tests
    unittest.main()


if __name__ == '__main__':
    # execute main() function
    main()
