#!/usr/bin/python3
# Finds a peak in a list of unsorted integers.

def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers."""
    if list_of_integers is None or list_of_integers == []:
        return None
    for i in range(len(list_of_integers)):
        if i == 0:
            if list_of_integers[i] >= list_of_integers[i + 1]:
                return list_of_integers[i]
        elif i == len(list_of_integers) - 1:
            if list_of_integers[i] >= list_of_integers[i - 1]:
                return list_of_integers[i]
        elif list_of_integers[i] >= list_of_integers[i - 1] and list_of_integers[i] >= list_of_integers[i + 1]:
            return list_of_integers[i]