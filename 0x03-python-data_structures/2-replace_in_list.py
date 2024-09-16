#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    # Check if index is valid (non-negative and within the list range)
    if idx < 0 or idx >= len(my_list):
        return my_list  # Return the original list if index is invalid
    else:
        # Replace the element at the specified index
        my_list[idx] = element
        return my_list  # Return the modified list
