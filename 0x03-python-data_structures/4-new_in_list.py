#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    # Create a copy of the original list
    new_list = my_list.copy()

    # Check if idx is a valid index
    if idx < 0 or idx >= len(my_list):
        return new_list

    # Replace the element at the specified index
    new_list[idx] = element

    return new_list
