"""
Sorts the array in ascending order after doing heapify on it
"""
from max_heap import heapify, del_max2

def sort(arr1):
    """
    Sorts the array in ascending order
    :param
        arr: (array): The array
    :return:
        The arr
    """
    count = len(arr1) - 1
    new_arr = [None] * len(arr1)
    while count >= 0:
        val = heapify(arr1)
        val, max1, end = del_max2(val)
        new_arr[count] = max1
        count -= 1
    return new_arr
