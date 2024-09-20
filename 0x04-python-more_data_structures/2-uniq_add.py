#!/usr/bin/python3
def uniq_add(my_list=[]):
    # Convert the list to a set to remove duplicates
    uniq_list = set(my_list)
    # Sum all the elements in the unique list
    return sum(uniq_list)
