#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    # Check if index is within valid range
    if 0 <= idx < len(my_list):
        # Use slicing to remove the item at index idx
        my_list = my_list[:idx] + my_list[idx + 1:]
    return my_list
