"""
Sorts a list of integers in ascending order using the Bubble Sort algorithm
Args: arr (list of int): List of integers to be sorted
Returns: sorted list of integers
Raises: ValueError when arr is of negative size, TypeError when arr is not a list
"""


def bubble_sort(arr):
    if len(arr) < 0:
        raise ValueError("Array is of invalid size.")
    if type(arr) is not list:
        raise TypeError("arr parameter is not a list".)
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


"""
Sorts a list of integers in ascending order using the Quick Sort algorithm.
Args: arr (list of int): List of integers to be sorted.
Returns: sorted list of integers.
Raises: ValueError if arr is of negative size.
"""


def quick_sort(arr):
    if len(arr) < 0:
        raise ValueError("Array is of invalid size.")
    if type(arr) is not list:
        raise TypeError("arr parameter is not a list".)
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


"""
Sorts a list of integers in ascending order using the Insertion Sort algorithm.
Args: arr (list of ints): List of integers to be sorted
Returns: sorted list of integers.
Raises: ValueError if arr is of negative size.
"""


def insertion_sort(arr):
    if len(arr) < 0:
        raise ValueError("Array is of invalid size.")
    if type(arr) is not list:
        raise TypeError("arr parameter is not a list".)
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
