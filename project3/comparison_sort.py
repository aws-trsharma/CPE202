"""
Authors: Tushar Sharma and Gaurav Joshi
CPE 202: Project 3
"""
import random
random.seed(1)


def selection_sort(alist):
    """
    Sorts a list by selecting max values from the unsorted part and prepending them to
    the sorted part
    Counts the number of comparisons
    :param
        alist(list): unsorted list
    :return:
        count(int): the count of the number of comparisons
        alist (arr): the sorted list
    """
    count = 0
    for i in range(len(alist)-1, 0, -1):
        pos_max = 0
        for j in range(1, i+1):
            if alist[j] > alist[pos_max]:
                pos_max = j
            count += 1
        temp = alist[i]
        alist[i] = alist[pos_max]
        alist[pos_max] = temp
    return alist, count

def insertion_sort(alist):
    """
    Sorts a list by swapping and inserting the smallesst element in the last position
    :param
        alist: (list): unsorted list
    :return:
        alist (arr): the sorted list
        count(int): the count of the number of comparisons
    """
    count = 0
    for i in range(1, len(alist)):
        count += 1
        j = i
        while j > 0 and alist[j-1] > alist[j]:
            alist[j-1], alist[j] = alist[j], alist[j-1]
            j -= 1
            count += 1
    return alist, count


def merge_sort(alist, count=None):
    """
    Merge Sort divides up an array as much as it possible and then compares the array values
    :param
       alist: (list): unsorted list
       count(int): the count of the number of comparisons
    :return:
         count(int): the count of the number of comparisons
    """
    count = 0
    if len(alist) > 1:
        mid = len(alist)//2
        left_half = alist[:mid]
        right_half = alist[mid:]
        count += merge_sort(left_half, count)
        count += merge_sort(right_half, count)
        i = 0
        j = 0
        k = 0
        while i < len(left_half) and j < len(right_half):
            count += 1
            if left_half[i] < right_half[j]:
                alist[k] = left_half[i]
                i = i+1
            else:
                alist[k] = right_half[j]
                j = j+1
            k = k+1
        while i < len(left_half):
            count += 1
            alist[k] = left_half[i]
            i = i + 1
            k = k + 1
        while j < len(right_half):
            count += 1
            alist[k] = right_half[j]
            j = j+1
            k = k+1
    return count


def quicksort(arr, start=None, stop=None, total=0):
    """
    Quicksort sorts the algorith by picking a pivot and comparing values based off that
    :param
        arr: the array
        start: where the sorting starts from
        stop: where the sorting ends from
        total: counts the number of comparisons
    :return:
        count: the number of comparisons
    """
    if start is None:
        start = 0
    if stop is None:
        stop = len(arr) - 1
    if start < stop:
        pivotindex, total = partitionrand(arr, start, stop)

        total += quicksort(arr, start, pivotindex - 1, total)
        total += quicksort(arr, pivotindex + 1, stop, total)
    return total


def partitionrand(arr, start, stop):
    """
    helper function to partition the array
    :param
        arr: the array
        start: the place where comparisons start
        stop: the place where comparisons stop
    """
    randpivot = random.randrange(start, stop)

    arr[start], arr[randpivot] = arr[randpivot], arr[start]
    return partition(arr, start, stop)


def partition(arr, start, stop):
    """
    Helper function to partition the array
    :param
        arr: the array
        start: the place where comparisons start
        stop: the place where comparisons stop
    :return:
    """
    count = 0
    pivot = start
    i = start + 1
    for j in range(start + 1, stop + 1):
        if arr[j] <= arr[pivot]:
            count += 1
            arr[i], arr[j] = arr[j], arr[i]
            i = i + 1
    count += 1
    arr[pivot], arr[i - 1] = arr[i - 1], arr[pivot]
    pivot = i - 1
    return pivot, count

def bubble_sort(alist):
    '''
    Compares adjacent values and swaps
    :param
    alist (list): The array we are sorting
    :return:
    count (int): The number of comparisons
    '''
    count = 0
    for total in range(len(alist)-1, 0, -1):
        count += 1
        for i in range(total):

            if alist[i] > alist[i+1]:
                count += 1
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

    return count

def tim_sort(arr1):
    """Uses python's in built sorting algorithm to sort.
    Combo of quick sort and merge sort
    args:
      arr1(list): The array we are sorting
    Returns:
       sorted list
    """
    return arr1.sort()
