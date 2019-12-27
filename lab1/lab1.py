"""LAB1
CPE202
"""



#1
def get_max(int_list):
    """Iterative function that finds a maximun in a list of integers
    args:
      int_list(int): a list of int values
    returns:
         int: sum of int values
    """
    if len(int_list) == 0:
        return None
    max1 = int_list[0]
    for val in int_list:
        if val > max1:
            max1 = val
    return max1

#2
def reverse(word):
    """Recursive function to reverse string
    args:
      word: a string
    return:
      string: the string reversed
    """
    # to-do: write the function body.
    if len(word) == 0:
        return word
    if len(word) == 1:
        return word[0]
    else:
        return word[-1] + reverse(word[:-1])
#3
def search(list1, val):
    """Recursive function which searches a list of integers and returns the
    index using binary search
    Args:
      list1(int): a list of int values
      val (int): the int the search searches for
    Returns:
      index: the value of where the number was found
    by following the step #2 of the design recipe here.
    """
    try:
        if len(list1) >= 1:
            mid = (len(list1) - 1)//2
            if list1[mid] == val:
                return mid
            elif list1[mid] < val:
                mid += 1
                return mid + search(list1[mid:], val)
            else:
                return search(list1[:mid+1], val)
    except:
        return None
#4
def fib(pos):
    """Recursive function to compute the nth Fibonacci number of Fibonacci Numbers
    Args:
      pos: int which is the nth Number in the Fibonacci Sequence
    Returns:
      returns nth Fibonacci Number
    """
    if pos == 0 or pos == 1:
        return pos
    else:
        return fib(pos-1) + fib(pos-2)
#5.1 factorial iterative version
def factorial_iter(number):
    """
    Computes a factorial number n! using an iterative method
    Args:
       number: int which is the number factorial product you must find
    Returns:
       product: the factorial computed
    """
    i = 1
    product = 1
    while i <= number:
        product = product * i
        i += 1
    return product
#5.2 factorial recursive version
def factorial_rec(number):
    """
    Computes a factorial number n! using a recursive method
    Args:
      number: int which is the number factorial product you must find
    Returns:
      product: the factorial computer
    """
    if number == 1 or number == 0:
        return 1
    else:
        return number * factorial_rec(number - 1)
