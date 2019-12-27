"""
Sorts the array in ascending order after doing heapify on it
"""
from max_heap import heapify, del_max2, del_max

def heap_sort_count(arr1):
    """
    Sorts the array in ascending order
    :param
        arr: (array): The array
    :return:
        The count of the array
    """
    store = 0
    count = len(arr1) - 1
    while count >= 0:
        store += del_max2(arr1)
        count -= 1
    return store

def heap_sort(arr1):
    """
    Sorts the array in ascending
    :param
        arr1: (array): The array
    :return:
        The new array
    """
    count = len(arr1) - 1
    new_arr = [None] * len(arr1)
    while count >= 0:
        val = heapify(arr1)
        val, max1, end = del_max(val)
        new_arr[count] = max1
        count -= 1
    for arr in range(len(new_arr)):
        arr1[arr] = None
        arr1[arr] = new_arr[arr]
    return arr1