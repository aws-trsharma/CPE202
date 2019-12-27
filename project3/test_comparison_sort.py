"""
Times and Counts for the number of comparisons
"""
import time
import random
from comparison_sort import selection_sort, insertion_sort, merge_sort, quicksort
from heap_sort import heap_sort_count


def test_quick_sort_sorted():
    """
    Quick sorts a sorted list
    """
    alist = random.sample(range(10000), 1000)
    start_time = time.time()
    count = quicksort(alist)
    end_time = time.time()
    sort_time = end_time - start_time
    print("Quick Sort: (unsorted):", sort_time)
    print(count)

def test_quick_sort_unsorted():
    """
    Quick sorts a unsorted list
    """
    alist = random.sample(range(10000), 1000)
    alist.sort()
    start_time = time.time()
    count = quicksort(alist)
    end_time = time.time()
    sort_time = end_time - start_time
    print("Quick Sort: (sorted):", sort_time)
    print(count)
def test_merge_sort_unsorted():
    """
    Merge sorts a unsorted list
    """
    alist = random.sample(range(100000000), 1000)
    start_time = time.time()
    count = merge_sort(alist)
    end_time = time.time()
    sort_time = end_time - start_time
    print("Merge Sort: (unsorted):", sort_time)
    print(count)

def test_merge_sort_sorted():
    """
    Merge sorts a unsorted list
    """
    alist = random.sample(range(1000000), 1000)
    alist.sort()
    start_time = time.time()
    count = merge_sort(alist)
    end_time = time.time()
    sort_time = end_time - start_time
    print("Merge Sort: (sorted):", sort_time)
    print(count)

def test_selection_sort_sorted():
    """
    Selection sorts a sorted list
    """
    alist = random.sample(range(10000000), 1000)
    alist.sort()
    start_time = time.time()
    alist, count = selection_sort(alist)
    end_time = time.time()
    sort_time = end_time - start_time
    print("Selection Sort: (sorted):", sort_time)
    print(count)

def test_selection_sort_unsorted():
    """
    Selection sorts a unsorted list
    """
    alist = random.sample(range(100000000), 1000)
    start_time = time.time()
    alist, count = insertion_sort(alist)
    end_time = time.time()
    sort_time = end_time - start_time
    print("Selection Sort: (unsorted):", sort_time)
    print(count)

def test_insertion_sort_sorted():
    """
    Insertion sorts a sorted list
    """
    alist = random.sample(range(100000000), 1000)
    alist.sort()
    start_time = time.time()
    alist, count = insertion_sort(alist)
    end_time = time.time()
    sort_time = end_time - start_time
    print("Insertion Sort: (sorted):", sort_time)
    print(count)

def test_insertion_sort_unsorted():
    """
    Insertion sorts a unsorted list
    """
    alist = random.sample(range(10000000), 1000)
    start_time = time.time()
    alist, count = insertion_sort(alist)
    end_time = time.time()
    sort_time = end_time - start_time
    print("Insertion Sort: (unsorted):", sort_time)
    print(count)

def test_heap_sort_unsorted():
    """
    Heap Sorts a unsorted list
    """
    alist = random.sample(range(1000000000), 1000)
    start_time = time.time()
    count = heap_sort_count(alist)
    end_time = time.time()
    sort_time = end_time - start_time
    print("Heap Sort: (sorted):", sort_time)
    print(count)

def test_heap_sort_sorted():
    """
    Heap sorts a sorted list
    """
    alist = random.sample(range(1000000000), 10000)
    alist.sort()
    start_time = time.time()
    count = heap_sort_count(alist)
    end_time = time.time()
    sort_time = end_time - start_time
    print("Heap Sort: (unsorted):", sort_time)
    print(count)

def test_tim_sort_sorted():
    """
    Tim sorts a sorted list
    """
    alist = random.sample(range(100000), 1000)
    alist.sort()
    start_time = time.time()
    alist.sort()
    end_time = time.time()
    sort_time = end_time - start_time
    print("Tim Sort: (sorted)", sort_time)

def test_tim_sort_unsorted():
    """
    Tim Sorts a unsorted list
    """
    alist = random.sample(range(100000), 1000)
    start_time = time.time()
    alist.sort()
    end_time = time.time()
    sort_time = end_time - start_time
    print("Tim Sort: (unsorted)", sort_time)


test_merge_sort_unsorted()
test_merge_sort_sorted()
test_insertion_sort_sorted()
test_selection_sort_sorted()
test_selection_sort_unsorted()
test_insertion_sort_unsorted()
test_heap_sort_sorted()
test_heap_sort_unsorted()
