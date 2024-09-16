#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    # Create a new list with True or False values based on divisibility by 2
    return [
        True if x % 2 == 0 else False
        for x in my_list
    ]
