#!/usr/bin/python3
"""This defines an inherited list class MyList"""


class MyList(list):
    """This implements sorted printing for the built-in list class"""

    def print_sorted(self):
        """Print all  list in sorted ascending order"""
        print(sorted(self))
