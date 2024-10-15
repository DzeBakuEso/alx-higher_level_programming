#!/usr/bin/python3
"""
This module defines a class MyList @ inheritsthe built-in list class.
Classes:
MyList: Inherits list provides a method to print list sorted ascding order.
"""


class MyList(list):
    """
    This class inherits list prvidees additinal method prinist sorted order.
    Methods:
print_sorted(): Prints list sorted in ascding ordr without chgingnl list.
    """
    def print_sorted(self):

        """
        This method prints the list in ascending order.

        Returns:
            None
        """
        print(sorted(self))
