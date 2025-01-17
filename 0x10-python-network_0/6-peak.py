#!/usr/bin/python3
"""Find a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """Find a peak in the list"""
    if not list_of_integers:
        return None

    def binary_search(low, high):
        mid = (low + high) // 2
        if (mid == 0 or
           list_of_integers[mid - 1] <= list_of_integers[mid]) and \
           (mid == len(list_of_integers) - 1 or
           list_of_integers[mid + 1] <= list_of_integers[mid]):
            return list_of_integers[mid]
        elif mid > 0 and list_of_integers[mid - 1] > list_of_integers[mid]:
            return binary_search(low, mid - 1)
        else:
            return binary_search(mid + 1, high)

    return binary_search(0, len(list_of_integers) - 1)
