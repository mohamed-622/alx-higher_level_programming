#!/usr/bin/python3

class MyList(list):
    """Subclass of list with additional functionality."""

    def print_sorted(self):
        """Prints the list in sorted order (ascending)."""
        sorted_list = sorted(self)
        print(sorted_list)
