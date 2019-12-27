"""
Max Heap allows user to insert and delete elements in the list
while maintaining a max heap order. This is where the parent child is
greater than the children.
"""


def insert(arr, item, end):
    """
    Puts an item to the end of the array and returns the array arr
    args:
        arr: (array) array of some fixed size
        item: (int) current index in the array
        end: (int) index in arr pointing to the end of the heap
    Returns
        Returns an array new_arr
    """
    if end is None or (end == len(arr) - 1 and end != -1):
        raise IndexError
    if not arr:
        arr.append(item)
    else:
        arr[end + 1] = item
        shift_up(arr, end + 1)
    return arr


def del_max(arr, end=None):
    """
    Deletes the max item and maintains the heap order
    args:
        arr: (array) array of some fixed size
        end: (int) index in arr pointing to end of heap if given
    Returns:
        arr, deleted max item, and the end index of the heap
    """
    if end is None:
        end = len(arr) - 1
    min_items = arr[0]
    arr[0] = arr[end]
    arr[end] = arr[0]
    shift_down(arr, 0, end)
    return arr, min_items, end - 1


def del_max2(arr, end=None):
    """
    Deletes the max item and maintains the heap order
    args:
        arr: (array) array of some fixed size
        end: (int) index in arr pointing to end of heap if given
    Returns:
        arr, deleted max item, and the end index of the heap
    """
    if end is None:
        end = len(arr) - 1
    min_items = arr[0]
    arr[0] = arr[end]
    arr[end] = -9999
    shift_down(arr, 0, end-1)
    return arr, min_items, end - 1


def shift_up(arr, index):
    """
    Shifts the item at the specified index, and does this recursively until it
     no longer can be shifted up
    args:
        arr: (array): array of some fixed size
        index: (int): current index of item
    """
    val = (index-1)//2
    if val < 0 or arr[val] >= arr[index]:
        return
    head_node = (index - 1)//2
    arr[head_node], arr[index] = arr[index], arr[head_node]
    return shift_up(arr, head_node)


def shift_down(arr, index, end):
    """
    Shifts the item at the specified index down, and it keeps shifting down recursively until
    it can no longer be shifted up
    args
        arr: (array): array of some fixed size
        index: (int): current index of item
        end: (int): index in arr pointing to end of heap
    """
    shift = shift_down_helper(arr, index, end)
    if shift < 0 or arr[index] > arr[shift]:
        return
    arr[shift], arr[index] = arr[index], arr[shift]
    return shift_down(arr, shift, end)


def shift_down_helper(arr, index, end):
    """
    Helps the shift_down function by comparing left and right children and seeing which path if
    prefers to take
    :param
        arr:(arr) array of some fixed size
        index: (int): current index of item
    :return:
        index (int): index of item to switch with
    """
    left = (2 * index) + 1
    right = (2 * index) + 2
    if right > end or (arr[right] is None) or (arr[left] is None):
        return -1
    if arr[left] > arr[right]:
        return left
    else:
        return right


def heapify(arr):
    """
    Builds a heap out of the array
    args:
        arr: (array) array of some fixed size
    Returns:
        returns arr
    """
    length = len(arr)
    i = ((length - 1) - 1)//2
    while i >= 0:
        shift_down(arr, i, length)
        i = i - 1
    return arr
