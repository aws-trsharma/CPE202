import unittest
from max_heap import *
from heap_sort import *


class MyTest(unittest.TestCase):
    def test_heap(self):
        arr = [None] * 5
        for i in range(5):
            # insert
            print("arr = insert(", arr, i + 1, i - 1, ")")
            arr = insert(arr, i + 1, i - 1)
        self.assertEqual(arr, [5, 4, 2, 1, 3])

        self.assertRaises(IndexError, insert, arr, 0, 4)

        end = len(arr) - 1
        print("arr, v, end = mh.del_max(", arr, ", ", end, ")")
        arr, v, end = del_max(arr, end)
        self.assertEqual(v, 5)
        print("arr, v, end = mh.del_max(", arr, ", ", end, ")")
        arr, v, end = del_max(arr, end)
        self.assertEqual(v, 4)
        print("arr, v, end = mh.del_max(", arr, ", ", end, ")")
        arr, v, end = del_max(arr, end)
        self.assertEqual(v, 3)
        print("arr, v, end = mh.del_max(", arr, ", ", end, ")")
        arr, v, end = del_max(arr, end)
        self.assertEqual(v, 2)

        # heapify
        arr = [1, 2, 3, 4, 5]
        arr = heapify(arr)
        self.assertEqual(arr, [5, 4, 3, 1, 2])
        end = len(arr) - 1
        for i in range(5):
            arr, v, end = del_max(arr, end)
            arr[end + 1] = v
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_sort(self):
        arr = [1, 3, 2, 5, 4]
        self.assertEqual(sort(arr), [1, 2, 3, 4, 5])
        arr = [1, 3, 3, 3, 2]
        self.assertEqual(sort(arr), [1, 2, 3, 3, 3])
        arr = [5, 4, 3, 2, 1]
        self.assertEqual(sort(arr), [1, 2, 3, 4, 5])
        arr = [1]
        self.assertEqual(sort(arr), [1])


if __name__ == '__main__':
    unittest.main()